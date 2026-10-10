# 🃏 Pokémon TCG Explorer

Explorador de variantes de cartas Pokémon TCG (Slowpoke y Snorlax), hecho con **Streamlit**.

## Ejecutar
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Arquitectura (escalable)
```
app.py              → UI (menú lateral + pantalla principal)
src/models.py       → Modelos (PokemonEntry, CardVariant)
src/repository.py   → Capa de datos (hoy JSON, mañana SQLite/Postgres/API)
src/scrapers/base.py→ Contrato para scrapers futuros
src/theme.py        → Tema claro/oscuro
src/ui.py           → Componentes visuales
data/pokemon/*.json → Un archivo por Pokémon
```

## Cómo expandir con scraping
1. Crea `src/scrapers/mi_fuente.py` heredando de `Scraper` y devuelve un `PokemonEntry`.
2. Llama `repo.save(entry)`: aparece automáticamente en el menú lateral.
3. Rellena `image_url` en cada variante para mostrar la imagen real.
4. Marca `verified: true` cuando el dato venga de una fuente oficial.

## Ciclo de trabajo
Desarrollo ágil (Scrum/XP), ciclo CRISP-ML, documentación obligatoria, despliegue con Streamlit Community Cloud desde GitHub.

## Aviso sobre datos
Los datos semilla se cargaron manualmente y están marcados `verified: false`. Valídalos contra una fuente oficial (p. ej. Pokémon TCG API) antes de publicar.
