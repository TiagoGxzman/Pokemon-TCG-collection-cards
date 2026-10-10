# 🃏 Pokémon TCG Explorer

Aplicación web hecha con **Streamlit** para explorar las variantes de cartas Pokémon TCG (Slowpoke y Snorlax), con menú lateral, modo claro/oscuro y arquitectura preparada para crecer mediante scraping.

---

## 📋 Requisitos

- **Python 3.10 o superior** (probado con 3.14)
- **pip** (viene incluido con Python)
- Un navegador web

Verifica tu instalación:

```powershell
python --version
```

> Si `python` no responde en Windows, usa `py --version`.

---

## 🚀 Instalación y ejecución

### 1. Descarga el proyecto

Descomprime la carpeta `pokemon_tcg_explorer` o clónala desde GitHub:

```bash
git clone <URL-DE-TU-REPOSITORIO>
```

### 2. Entra a la carpeta del proyecto

La carpeta que contiene `app.py`:

```powershell
cd pokemon_tcg_explorer
```

### 3. (Opcional, recomendado) Crea un entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Si PowerShell bloquea la activación, ejecuta una vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

### 4. Instala las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 5. Ejecuta la aplicación

```powershell
python -m streamlit run app.py
```

Alternativa en Windows:

```powershell
py -m streamlit run app.py
```

Se abrirá automáticamente el navegador en **http://localhost:8501**. Si no se abre, copia esa dirección en tu navegador.

Para detener la app, presiona `Ctrl + C` en la terminal.

---

## ❓ Solución de problemas

| Problema | Solución |
|---|---|
| `streamlit no se reconoce como nombre de un cmdlet` | El comando no está en el PATH. Usa siempre `python -m streamlit run app.py`. |
| `python no se reconoce` | Usa `py` en lugar de `python`, o reinstala Python marcando **"Add Python to PATH"**. |
| `No module named streamlit` | Ejecuta `python -m pip install -r requirements.txt` con el mismo Python que usas para correr la app. |
| `.venv/Scripts/python.exe no se reconoce` | VS Code apunta a un entorno virtual que no existe. Crea el `.venv` (paso 3) o elige otro intérprete con `Ctrl+Shift+P` → **Python: Select Interpreter**. |
| Puerto 8501 ocupado | Ejecuta `python -m streamlit run app.py --server.port 8502`. |

---

## 🧭 Uso de la aplicación

- **Menú lateral izquierdo:** lista de cartas disponibles. Haz clic en una para ver su descripción y variantes.
- **Filtros:** en la pantalla principal puedes filtrar las variantes por *set* y *acabado*.
- **🌙 Modo oscuro:** interruptor en la parte superior del menú lateral.
- **➕ Añadir carta futura:** desplegable en el menú lateral. Escribe nombre, descripción y tipos; la carta aparece de inmediato en el menú.

---

## 🗂️ Estructura del proyecto

```
pokemon_tcg_explorer/
├── app.py                  # Interfaz principal (menú + pantalla principal)
├── requirements.txt        # Dependencias
├── README.md               # Este archivo
├── .streamlit/config.toml  # Configuración de Streamlit
├── data/pokemon/           # Un archivo JSON por Pokémon
│   ├── slowpoke.json
│   └── snorlax.json
└── src/
    ├── models.py           # Modelos: PokemonEntry y CardVariant
    ├── repository.py       # Capa de datos (hoy JSON, mañana BD/API)
    ├── theme.py            # Tema claro/oscuro
    ├── ui.py               # Componentes visuales
    └── scrapers/base.py    # Contrato para futuros scrapers
```

---

## 🔌 Cómo expandir el proyecto

### Añadir un Pokémon a mano
Crea un archivo `data/pokemon/<nombre>.json` con esta forma (o usa el formulario de la app):

```json
{
  "name": "Pikachu",
  "dex_number": 25,
  "types": ["Eléctrico"],
  "description": "Descripción breve de la carta.",
  "variants": [
    {
      "name": "Pikachu (Base Set)",
      "set_name": "Base Set",
      "series": "Base",
      "number": "58/102",
      "rarity": "Común",
      "finish": "Normal",
      "year": 1999,
      "image_url": "",
      "notes": "",
      "verified": true
    }
  ]
}
```

### Añadir datos con scraping
1. Crea `src/scrapers/mi_fuente.py` con una clase que herede de `Scraper` y devuelva un `PokemonEntry`.
2. Guarda el resultado con `repo.save(entry)`.
3. El Pokémon aparecerá solo en el menú lateral, sin tocar la interfaz.
4. Rellena `image_url` para mostrar la imagen real de cada carta.
5. Marca `verified: true` cuando el dato venga de una fuente oficial.

---

## ⚠️ Aviso sobre los datos

Los datos iniciales de Slowpoke y Snorlax se cargaron manualmente y están marcados con `verified: false` (la tarjeta muestra "⚠ Pendiente de verificar"). Valídalos con una fuente oficial, como la [Pokémon TCG API](https://pokemontcg.io/), antes de publicar.

---

## 🔄 Flujo de trabajo del proyecto

Desarrollo ágil (Scrum / XP), ciclo CRISP-ML, documentación continua, código en GitHub y despliegue del dashboard con Streamlit.
