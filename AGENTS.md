# Botonera Agent Notes

## Project Structure
- `botonera.html` - Main and only page. Single-file app, all JS/CSS embedded.
- `serv.py` - Python HTTP server with auto port selection (8000-8099), graceful Ctrl+C shutdown.
- `itemz.json` - Preset sound library (~200 entries with 6-digit hex colors).

## Commands
```bash
python serv.py   # Auto-selects available port, Ctrl+C to stop
```

## LocalStorage Keys
- `botonera_sounds` - Sound buttons array with `{name, url, emoji, color, textColor, category?}`
- `botonera_categories` - Categories array with `{id, name}`

## Default Categories (10 preset modules)
RISAS, TV/SHOW/CINE, APLAUSOS CELEBRACIONES, ANIMALS, ELECTRONICS, CARS, DEVICES, MUSIC, REGIONAL, INSULTOS

## Audio Normalization
Web Audio API with `AudioContext`, `createGain`, `createMediaElementSource`. Toggle via toolbar button. When enabled, all audio goes through a master gain node at 0.85.

## Color Format
Colors use 6-digit hex (`#RRGGBB`). Transparency slider (20-100%) adds alpha dynamically at render time.

## Categories / Modules
- **3-column grid layout**, each category is a square module
- Double-click module title to rename inline
- Drag & drop sounds between modules or to the "Sin categoría" module
- Right-click any sound button for context menu: Edit, Delete, or Move to category
- "Sin categoría" module catches uncategorized sounds
- Categories stored separately in localStorage, sounds reference by `id`
- Toolbar filter dropdown to view single category normally

## Transparency Control
Range slider in toolbar (20-100%) controls button opacity. Applied dynamically at render, not stored.

## No Build/Test
This is a static HTML file. No tests, no build, no linting.