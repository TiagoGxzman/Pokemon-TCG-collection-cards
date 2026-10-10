"""Tema claro/oscuro mediante variables CSS."""
from __future__ import annotations

import streamlit as st

PALETTES = {
    "Claro": dict(bg="#F6F7FB", surface="#FFFFFF", text="#1F2430", muted="#6B7280",
                  border="#E5E7EB", accent="#E11D48", chip="#FDE8EC"),
    "Oscuro": dict(bg="#0F1220", surface="#181C2E", text="#EDEFF7", muted="#9AA3B8",
                   border="#2A3050", accent="#FB7185", chip="#2B1F2E"),
}


def apply_theme(mode: str) -> None:
    p = PALETTES[mode]
    st.markdown(
        f"""
<style>
:root {{
  --bg:{p['bg']}; --surface:{p['surface']}; --text:{p['text']}; --muted:{p['muted']};
  --border:{p['border']}; --accent:{p['accent']}; --chip:{p['chip']};
}}
.stApp, [data-testid="stHeader"] {{ background: var(--bg); color: var(--text); }}
[data-testid="stSidebar"] {{ background: var(--surface); border-right: 1px solid var(--border); }}
.stApp p, .stApp label, .stApp span, .stApp h1, .stApp h2, .stApp h3, .stApp li {{ color: var(--text); }}
.muted {{ color: var(--muted) !important; }}
.hero {{ background: var(--surface); border:1px solid var(--border); border-radius:18px; padding:1.4rem 1.6rem; margin-bottom:1.2rem; }}
.chip {{ display:inline-block; background:var(--chip); color:var(--accent) !important; border-radius:999px;
        padding:2px 12px; font-size:.78rem; font-weight:600; margin-right:6px; }}
.card {{ background: var(--surface); border:1px solid var(--border); border-radius:16px; padding:1rem;
        height:100%; transition: transform .15s, box-shadow .15s; }}
.card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,.12); }}
.card h4 {{ margin:.2rem 0 .1rem; font-size:1.02rem; }}
.thumb {{ height:150px; border-radius:12px; display:flex; align-items:center; justify-content:center;
         background: var(--chip); font-size:3rem; margin-bottom:.7rem; overflow:hidden; }}
.thumb img {{ max-height:100%; max-width:100%; object-fit:contain; }}
.meta {{ font-size:.82rem; color: var(--muted) !important; line-height:1.5; }}
.warn {{ font-size:.72rem; color: var(--accent) !important; }}
</style>
""",
        unsafe_allow_html=True,
    )
