# Renders public/og.png and public/og-tr.png from real assets (app icon + Quick Look capture).
import pathlib, sys
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[2]
tpl = (root/'scripts/og/og.html').read_text()
icon = (root/'src/assets/brand/icon.png').as_uri()
qldir = root/'src/assets/shots/dark'
ql = next(qldir.glob('scene-ql-popup.*')).as_uri()  # full window incl. title bar (Open with GeoPeek)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for name, title, facts in [('og.png', 'Press Space.<br>See the map.', 'Quick Look for Mac'), ('og-tr.png', 'Space’e bas.<br>Haritayı gör.', 'Mac için Quick Look')]:
        html = tpl.replace('ICON', icon).replace('QL', ql).replace('TITLE', title).replace('FACTS', facts)
        f = root/'scripts/og/_tmp.html'; f.write_text(html)
        pg = b.new_page(viewport={'width': 1200, 'height': 630})
        pg.goto(f.as_uri()); pg.wait_for_timeout(300)
        pg.screenshot(path=str(root/'public'/name))
        f.unlink()
    b.close()
print('ok')
