# Jafar Puppet

Webcam face tracking that animates a chest-up Jafar puppet, for OBS.

## Quick try (Chrome or Edge)
1. Open `index.html`. If the camera won't start from a file, serve the folder instead: `python -m http.server 8000`, then open `http://localhost:8000`.
2. Click **Start camera**, allow access, look straight ahead, then click **Calibrate**.
3. Tune head motion, mouth, blink and smoothing. Settings are saved in the browser.

## OBS, option A: Browser Source (transparent, cleanest)
1. Close OBS. Launch it with the flag `--enable-media-stream` (Windows: right-click the OBS shortcut → Properties → Target, add it after the closing quote).
2. Add **Browser Source**. Use **Local file** pointing to `index.html`, or URL `http://localhost:8000/?output`. With a local file, add `?output` in the custom URL field if offered; otherwise use the localhost URL.
3. Width 1080, height 1080. Done. The background is transparent.

Note: Windows often lets only one app use a webcam. If OBS also has your webcam as a source, the puppet may show "camera busy".

## OBS, option B: window capture + green
1. Open `index.html?output&bg=green` in Chrome.
2. In OBS, add **Window Capture** of that Chrome window, then add the **Chroma Key** filter.

## Known limits (v1)
- Head turns are a 2.5D warp, so large turns (over ~25°) will look stretched. Clamp with the Head motion slider.
- Closed eyes and the open mouth are painted in code, not hand-drawn art.
- First load needs internet (tracking library and model).
