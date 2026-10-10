"""Contrato para futuros scrapers / conectores de API.

Ejemplo de uso futuro:

    class PokemonTcgApiScraper(Scraper):
        def fetch(self, pokemon_name): ...   # consulta la fuente
    repo.save(PokemonTcgApiScraper().fetch("Slowpoke"))
"""
from __future__ import annotations

from abc import ABC, abstractmethod

from ..models import PokemonEntry


class Scraper(ABC):
    source_name: str = "unknown"

    @abstractmethod
    def fetch(self, pokemon_name: str) -> PokemonEntry:
        """Devuelve un PokemonEntry con todas sus variantes."""
