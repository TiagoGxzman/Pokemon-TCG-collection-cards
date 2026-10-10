"""Modelos de dominio. Un Pokémon agrupa muchas variantes de carta."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class CardVariant:
    name: str                      # Ej: "Snorlax (Holo)"
    set_name: str                  # Ej: "Jungle"
    series: str = ""               # Ej: "Base"
    number: str = ""               # Ej: "11/64"
    rarity: str = ""               # Ej: "Holo Rare"
    finish: str = "Normal"         # Normal / Holo / Reverse Holo / Full Art ...
    year: int | None = None
    image_url: str = ""            # Lo llenará el scraper
    notes: str = ""
    verified: bool = False         # False = pendiente de validar con fuente oficial

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "CardVariant":
        known = cls.__dataclass_fields__.keys()
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass
class PokemonEntry:
    name: str
    description: str               # Breve: qué hace la carta / el Pokémon en el juego
    types: list[str] = field(default_factory=list)
    dex_number: int | None = None
    variants: list[CardVariant] = field(default_factory=list)

    @property
    def slug(self) -> str:
        return self.name.strip().lower().replace(" ", "-")

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "PokemonEntry":
        return cls(
            name=d["name"],
            description=d.get("description", ""),
            types=d.get("types", []),
            dex_number=d.get("dex_number"),
            variants=[CardVariant.from_dict(v) for v in d.get("variants", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
