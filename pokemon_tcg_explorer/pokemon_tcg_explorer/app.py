"""Pokémon TCG Explorer — Streamlit.  Ejecutar:  py -m streamlit run app.py"""
from pathlib import Path

import streamlit as st

from src.models import PokemonEntry
from src.repository import CardRepository, slugify
from src.theme import apply_theme
from src.ui import hero, variant_grid

st.set_page_config(page_title="Pokémon TCG Explorer", page_icon="🃏", layout="wide")

repo = CardRepository(Path(__file__).parent / "data" / "pokemon")

# ---------- Estado ----------
st.session_state.setdefault("theme", "Claro")

# ---------- Menú lateral ----------
with st.sidebar:
    st.markdown("## 🃏 TCG Explorer")
    dark = st.toggle("🌙 Modo oscuro", value=st.session_state["theme"] == "Oscuro")
    st.session_state["theme"] = "Oscuro" if dark else "Claro"
    st.divider()

    entries = repo.list_pokemon()
    names = [e.name for e in entries]
    selected = st.radio("Cartas", names, label_visibility="collapsed") if names else None

    st.divider()
    with st.expander("➕ Añadir carta futura"):
        with st.form("add_pokemon", clear_on_submit=True):
            new_name = st.text_input("Nombre del Pokémon")
            new_desc = st.text_area("Descripción breve", height=90)
            new_types = st.text_input("Tipos (separados por coma)")
            if st.form_submit_button("Guardar") and new_name.strip():
                repo.save(PokemonEntry(
                    name=new_name.strip().title(),
                    description=new_desc.strip(),
                    types=[t.strip().title() for t in new_types.split(",") if t.strip()],
                ))
                st.rerun()

apply_theme(st.session_state["theme"])

# ---------- Pantalla principal ----------
if not selected:
    st.info("Aún no hay cartas. Añade una desde el menú lateral.")
    st.stop()

entry = repo.get(slugify(selected))
hero(entry)

st.subheader(f"Variantes disponibles ({len(entry.variants)})")
if not entry.variants:
    st.caption("Aún no hay variantes registradas. Se llenarán mediante scraping.")
    st.stop()

finishes = sorted({v.finish for v in entry.variants})
sets = sorted({v.set_name for v in entry.variants})
c1, c2 = st.columns(2)
f_finish = c1.multiselect("Acabado", finishes)
f_set = c2.multiselect("Set", sets)

shown = [v for v in entry.variants
         if (not f_finish or v.finish in f_finish) and (not f_set or v.set_name in f_set)]
variant_grid(shown, entry.name)
