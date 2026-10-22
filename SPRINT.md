# Sprint 1 — Jafar Puppet v1

Goal: webcam drives a chest-up Jafar puppet that works as an OBS source.

| # | Task | Status |
|---|------|--------|
| 1 | Pick art (GPT grid, option 4), remove white background | Done |
| 2 | Mesh-warp rig: head yaw/pitch/roll with parallax, jaw drop, breathing | Done |
| 3 | Procedural eyelids + lash line, mouth opening + teeth, gaze shift | Done |
| 4 | MediaPipe Face Landmarker: blendshapes + head matrix | Done (untested on a real webcam) |
| 5 | Smoothing, calibration, sensitivity sliders, mirror toggle | Done |
| 6 | Idle fallback (drift to neutral, auto-blink) | Done |
| 7 | `?output` transparent mode, `&bg=green` fallback | Done |
| 8 | Test with real webcam + OBS, tune numbers | Open (Nabil) |

## Definition of Done
- Opens from one file, no install.
- Blink, mouth, head turn/tilt follow Nabil's face at 30+ fps on the streaming PC.
- No visible jitter at rest after calibration.
- Character never freezes when tracking drops.
- Shows in OBS with a clean transparent (or keyable green) background.

## Deviations from the PRD
- Single-file HTML + raw WebGL instead of Vite + React + PixiJS. Reason: small tool, no build step, and it loads directly in OBS (Philosophy allows single-file for small tools).
- No separate art layers. Eyelids and mouth are painted in code over the one image, and the head moves by mesh warp. Reason: we only have one flat image; this avoids manual layer splitting for v1.
- Gaze moved in-socket (small shift) rather than separate pupil layers.
