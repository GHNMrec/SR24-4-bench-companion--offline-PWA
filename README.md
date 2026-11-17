# SR24•4 Bench Companion

Offline step-by-step guide for per-channel direct-out mods on a Mackie SR24•4. Single self-contained `index.html` (images and fonts embedded). No network needed.

## Use on phone
**Easiest (any phone):** host the folder on GitHub Pages / any static https host, open `index.html`, then *Add to Home Screen*. The service worker caches everything; works in airplane mode and keeps your progress ticks.

**Direct file:** copy `index.html` to the phone and open it in Chrome (Android). On iOS, Files-app/file:// viewing often blocks JavaScript storage; use the hosted + Add to Home Screen route, or open it from a local server.

Progress is saved in the browser (localStorage) per device.

## Rebuild
Edit `src/template.html`, then `python3 src/build.py` (inlines `src/img/*.jpg` and `src/fonts/*.woff2` into `index.html`).

## Safety
Mixer contains mains voltage and large reservoir caps. Unplug, bleed C6, C5, C1, C2, C7 through 1–2.2 kΩ 5 W and confirm <1 V before touching anything.
