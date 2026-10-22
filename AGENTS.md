# AGENTS.md — Jafar Puppet

- Source: `src/app.html`. Art: `art/jafar.png` (627×627, transparent). Build: `python3 build.py` → `index.html` (art inlined).
- Never edit `index.html` by hand; edit `src/app.html` and rebuild.
- Rig coordinates (eyes, mouth, pivot, face) live in the `RIG` object, in art pixels. New art = re-measure these.
- Tracking: MediaPipe tasks-vision 0.10.14 from jsdelivr; model from Google storage. Needs internet on first load.
- Keep it one file, no framework. Settings go in localStorage (wrapped in try/catch).
- Test hooks: `window.__pose` (target pose) and `window.__faceSeen()` (suppresses idle mode).
