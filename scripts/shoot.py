# Full-page screenshots of the local preview (npx astro preview --port 4321).
import sys, pathlib
from playwright.sync_api import sync_playwright
BASE = 'http://127.0.0.1:4321'
out = pathlib.Path(next((a for a in sys.argv[1:] if not a.startswith('--')), '/workspace/geopeek-web-shots')); out.mkdir(parents=True, exist_ok=True)
jobs = []
for page, slug in [('home', '/'), ('support', '/support/'), ('privacy', '/privacy/')]:
    for lang, pre in [('en', ''), ('tr', '/tr')]:
        for dev, vp, dpr in [('desktop', (1440, 900), 1), ('mobile', (390, 844), 2)]:
            for scheme in ['light', 'dark']:
                jobs.append((f'{page}-{lang}-{dev}-{scheme}', pre + slug, vp, dpr, scheme))
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for name, path, vp, dpr, scheme in jobs:
        pg = b.new_page(viewport={'width': vp[0], 'height': vp[1]}, color_scheme=scheme, device_scale_factor=dpr, reduced_motion=('reduce' if '--reduce' in sys.argv else 'no-preference'))
        pg.goto(BASE + path); pg.wait_for_load_state('networkidle')
        if 'support' in name:
            pg.evaluate("document.querySelectorAll('details').forEach((d,i)=>{if(i<3)d.open=true})")
        pg.evaluate("""async()=>{for(const i of document.images){i.loading='eager'};
          for(let y=0;y<document.body.scrollHeight;y+=500){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,80))}
          await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));window.scrollTo({top:0,behavior:'instant'})}""")
        # freeze the hero on its final frame (Quick Look open, popup shown) so the page reads as a still
        pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=6200})")
        pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(300)
        broken = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.currentSrc||i.src)")
        sw = pg.evaluate('document.documentElement.scrollWidth')
        h = pg.evaluate('document.documentElement.scrollHeight')
        # grow the viewport to the page height so the sticky header is not stitched mid-page
        # (hero panel width is capped at 1120px, so a tall viewport does not change the layout)
        pg.set_viewport_size({'width': vp[0], 'height': h}); pg.wait_for_timeout(400)
        pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=6200})"); pg.wait_for_timeout(150)
        pg.screenshot(path=str(out / f'{name}.png'), full_page=True)
        print(name, 'scrollWidth', sw, 'viewport', vp[0], 'broken', broken)
        pg.close()
    b.close()
