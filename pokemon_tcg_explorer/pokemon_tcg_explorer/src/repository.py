"""Capa de datos. La UI solo conoce `CardRepository`, nunca los archivos.

Para escalar: cambia la implementación (SQLite, Postgres, API) sin tocar la UI.
Los scrapers solo necesitan llamar a `repo.save(entry)`.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Protocol

from .models import PokemonEntry


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


class Repository(Protocol):
    def list_pokemon(self) -> list[PokemonEntry]: ...
    def get(self, slug: str) -> PokemonEntry | None: ...
    def save(self, entry: PokemonEntry) -> None: ...


class CardRepository:
    """Un archivo JSON por Pokémon en data/pokemon/. Escritura atómica."""

    def __init__(self, data_dir: Path):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def list_pokemon(self) -> list[PokemonEntry]:
        entries = []
        for f in sorted(self.data_dir.glob("*.json")):
            try:
                entries.append(PokemonEntry.from_dict(json.loads(f.read_text("utf-8"))))
            except (json.JSONDecodeError, KeyError):
                continue  # archivo corrupto: se ignora sin romper la app
        return sorted(entries, key=lambda e: e.name)

    def get(self, slug: str) -> PokemonEntry | None:
        f = self.data_dir / f"{slug}.json"
        if not f.exists():
            return None
        return PokemonEntry.from_dict(json.loads(f.read_text("utf-8")))

    def save(self, entry: PokemonEntry) -> None:
        target = self.data_dir / f"{slugify(entry.name)}.json"
        tmp = target.with_suffix(".tmp")
        tmp.write_text(json.dumps(entry.to_dict(), ensure_ascii=False, indent=2), "utf-8")
        tmp.replace(target)  # atómico
