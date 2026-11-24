# geopeek-web

Production candidate for https://geopeek.app. Astro static site, EN at `/`, TR at `/tr/`.
Not deployed. Intended as its own repository (`geopeek-web`), separate from the app repo.

## Run
```bash
npm install
npm run build      # static output in dist/
npx astro preview  # http://localhost:4321
```
`dist/` is plain HTML. Opening `dist/index.html` from disk works for a quick look, but links use absolute
paths (`/support/`), so use the preview server to click around.

## Layout
- `src/site.ts`: release facts (version, DMG URL and size, brew command). Update on each release.
- `src/i18n/strings.ts`: all copy, EN and TR. No em dashes. Claims must match the app repo.
- `src/components/HeroScene.astro`: Finder > Space > Quick Look animation (CSS, 8 s loop), pause button,
  reduced-motion still, stacked phone layout.
- `src/assets/shots/{light,dark}/`: captures, swapped by file name. See `PLACEHOLDERS.md`.
- `scripts/shoot.py`, `scripts/record-hero.py`: full-page screenshots and hero MP4 from the preview server.
- `scripts/og/make-og.py`: renders `public/og.png` and `public/og-tr.png`.
- `wrangler.jsonc`: Cloudflare Workers Static Assets (`dist`), not deployed.

## Rules for this site
- No cookies, no analytics, no web fonts, no third-party requests. JavaScript only for the pause and copy buttons.
- Only verified product facts (see `FACTS.md`). No App Store line until it is live. No performance numbers.
- Map attribution in the footer: OpenFreeMap, OpenMapTiles, © OpenStreetMap contributors (ODbL). See `CREDITS.md`.

## Deploy (later, after approval)
```bash
npm run build && npx wrangler deploy
```
