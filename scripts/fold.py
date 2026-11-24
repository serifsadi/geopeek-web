# Viewport (not full-page) checks of the hero fold and the scene panel fit.
import sys, pathlib
from playwright.sync_api import sync_playwright
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/workspace/geopeek-web-shots')
path = sys.argv[2] if len(sys.argv) > 2 else '/'
tag = sys.argv[3] if len(sys.argv) > 3 else ''
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for w, h in [(1024, 640), (1280, 720), (1440, 900)]:
        for scheme in ['light', 'dark']:
            pg = b.new_page(viewport={'width': w, 'height': h}, color_scheme=scheme)
            pg.goto('http://127.0.0.1:4321' + path); pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(300)
            # first paint: animation at t=0 (Finder list)
            pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=0})"); pg.wait_for_timeout(250)
            r = pg.evaluate("(()=>{const r=document.querySelector('.scene').getBoundingClientRect();const f=document.querySelector('.sc-fwrap').getBoundingClientRect();return [r.top,r.height,r.width,f.top]})()")
            pg.screenshot(path=str(out / f'fold{tag}-{w}x{h}-{scheme}-top.png'))
            pg.evaluate("window.scrollTo({top:document.querySelector('.scene').getBoundingClientRect().top + scrollY - 56 - 12, behavior:'instant'})")
            pg.wait_for_timeout(200)
            pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=6200})"); pg.wait_for_timeout(250)
            r2 = pg.evaluate("(()=>{const r=document.querySelector('.scene').getBoundingClientRect();return [r.top,r.bottom]})()")
            pg.screenshot(path=str(out / f'fold{tag}-{w}x{h}-{scheme}-scene.png'))
            print(f'{w}x{h} {scheme}: scene top@load={r[0]:.0f} h={r[1]:.0f} w={r[2]:.0f} finderTop={r[3]:.0f} | scrolled top={r2[0]:.0f} bottom={r2[1]:.0f} fits={r2[1]<=h}')
            pg.close()
    b.close()
