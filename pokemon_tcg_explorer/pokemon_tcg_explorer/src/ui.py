"""Componentes visuales reutilizables."""
from __future__ import annotations

from html import escape

import streamlit as st

from .models import CardVariant, PokemonEntry

EMOJI = {"Slowpoke": "🦛", "Snorlax": "😴"}


def hero(entry: PokemonEntry) -> None:
    chips = "".join(f'<span class="chip">{escape(t)}</span>' for t in entry.types)
    dex = f"#{entry.dex_number:03d}" if entry.dex_number else ""
    st.markdown(
        f"""<div class="hero">
        <div class="muted">{dex}</div>
        <h1 style="margin:0 0 .4rem">{escape(entry.name)}</h1>
        {chips}
        <p style="margin-top:.9rem">{escape(entry.description)}</p>
        </div>""",
        unsafe_allow_html=True,
    )


def variant_card(v: CardVariant, entry_name: str) -> str:
    thumb = (f'<img src="{escape(v.image_url)}" alt="{escape(v.name)}">'
             if v.image_url else EMOJI.get(entry_name, "🃏"))
    lines = [
        f"📦 {escape(v.set_name)}" + (f" · {escape(v.series)}" if v.series else ""),
        f"🔢 {escape(v.number)}" if v.number else "",
        f"⭐ {escape(v.rarity)} · ✨ {escape(v.finish)}",
        f"📅 {v.year}" if v.year else "",
        escape(v.notes) if v.notes else "",
    ]
    meta = "<br>".join(l for l in lines if l)
    warn = "" if v.verified else '<div class="warn">⚠ Pendiente de verificar</div>'
    return (f'<div class="card"><div class="thumb">{thumb}</div>'
            f'<h4>{escape(v.name)}</h4><div class="meta">{meta}</div>{warn}</div>')


def variant_grid(variants: list[CardVariant], entry_name: str, cols: int = 3) -> None:
    for i in range(0, len(variants), cols):
        row = st.columns(cols)
        for col, v in zip(row, variants[i:i + cols]):
            col.markdown(variant_card(v, entry_name), unsafe_allow_html=True)
        st.write("")
