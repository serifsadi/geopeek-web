# Records the hero animation from the local preview as PNG frames, then encodes MP4 with ffmpeg.
# usage: python3 scripts/record-hero.py <width> <dpr> <scheme> <out.mp4> [lang]
import sys, pathlib, subprocess, tempfile
from playwright.sync_api import sync_playwright
width, dpr, scheme, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]
lang = sys.argv[5] if len(sys.argv) > 5 else 'en'
fps, dur = 25, 8000
tmp = pathlib.Path(tempfile.mkdtemp())
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg = b.new_page(viewport={'width': width, 'height': 1200}, color_scheme=scheme, device_scale_factor=dpr)
    pg.goto('http://127.0.0.1:4321' + ('/tr/' if lang == 'tr' else '/')); pg.wait_for_load_state('networkidle')
    el = pg.query_selector('.scene'); el.scroll_into_view_if_needed(); pg.wait_for_timeout(500)
    pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
    n = int(dur / 1000 * fps)
    for i in range(n):
        pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={i*1000/fps}}})")
        el.screenshot(path=str(tmp / f'f{i:04d}.png'), animations='allow')
    b.close()
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-framerate', str(fps), '-i', str(tmp / 'f%04d.png'),
                '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20',
                '-movflags', '+faststart', out], check=True)
print(out)
