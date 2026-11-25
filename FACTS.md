# Verified facts used on the site (checked 2026-11-25)

| Claim on the site | Source |
|---|---|
| Opens GeoJSON (.geojson, .json), KML, KMZ, GPX | README Features, CHANGELOG 0.4.0 |
| KML, KMZ, GPX are converted to GeoJSON; KMZ: the KML document inside | README, CHANGELOG 0.4.0 and 0.4.1 |
| Map with MapLibre on OpenFreeMap, dark or positron style to match appearance | README Features and Privacy |
| Click a feature: properties in a popup; table map button selects and zooms | README Features and Usage |
| Stats: feature count, geometry types, vertex count | README Features |
| Paste ⌘V, welcome screen Paste from Clipboard | README, CHANGELOG 0.2.0 |
| Recents on welcome screen and File > Open Recent | CHANGELOG 0.4.0 |
| Set as Default… asks macOS for each format; never default on its own (Alternate rank) | CHANGELOG 0.4.1 |
| Finder thumbnails show the GeoPeek icon, without reading .geojson/.kml/.kmz/.gpx | README Thumbnails, CHANGELOG 0.4.0 |
| JSON that is not GeoJSON opens as a colored read-only page | README JSON fallback |
| "Basemap unavailable" chip, geometry on a plain background | README, CHANGELOG 0.3.0 |
| macOS 15.0 or later | README Requirements, project.pbxproj MACOSX_DEPLOYMENT_TARGET = 15.0 |
| Universal (Apple silicon and Intel) | `file` on GeoPeek 0.4.1 DMG binaries: x86_64 + arm64 for app and both extensions |
| Signed and notarized | CHANGELOG 0.3.0 (Developer ID, release script notarizes); 0.4.1 app has a stapled ticket |
| Version 0.4.1, 2,780,712 bytes, released 2026-11-23 | GitHub Release v0.4.1 |
| `brew install --cask serifsadi/geopeek/geopeek`, `brew trust --cask ...` | homebrew-geopeek README, app README Troubleshooting |
| Files read locally, not uploaded; map background requests to tiles.openfreemap.org without file contents | README Privacy. Site no longer says these are the *only* requests (README also notes attribution links and the MapLibre logo open in the browser) |
| App and QL extension sandboxed, user-selected read-only, network client | entitlements files |
| Thumbnail extension has no network entitlement | GeoPeekThumbnailExtension.entitlements |
| No tracking, no collected data in privacy manifests, no analytics | README Privacy (PrivacyInfo.xcprivacy) |
| App UI is English only | **Verified** 2026-11-24 on GeoPeek-0.4.1.dmg: app has only `en.lproj`; QL extension `Base.lproj` + `en.lproj`; app, QL and thumbnail extensions `CFBundleDevelopmentRegion` = en, no `CFBundleLocalizations` |
| MIT License | LICENSE |
| Accent #f97316 (dark), #c2410c (light) | Shared/GeoRenderer.swift (`--accent`, `dataColor`) |
| OpenFreeMap's privacy policy covers its tile service (linked: https://openfreemap.org/privacy/) | **Verified** 2026-11-24: page returns 200, "Last Updated: October 8, 2026", "This policy also covers our public tile service at https://tiles.openfreemap.org, including when our maps are embedded in other websites or apps." Plain link, the site loads nothing from it |
| Open files by double-click, ⌘O, or drag onto the window | **Verified**: README Usage ("Double-click ..., use `Cmd + O`, or drag and drop"), README Features (Drag & Drop), CHANGELOG 0.1.0 ("drag and drop or with ⌘O") |
| "Homebrew 7 does not load a third-party tap until it is trusted"; install command trusts the cask; `brew trust --cask serifsadi/geopeek/geopeek` | **Verified**: README Troubleshooting, same wording |
| Preview missing: System Settings > General > Login Items & Extensions > Quick Look; `qlmanage -r` and `killall QuickLookUIService`; remove older copies of GeoPeek.app | **Verified**: README Troubleshooting. TR label "Giriş Öğeleri ve Uzantılar › Hızlı Bakış" is from Turkish third-party guides, **not checked** on a Mac set to Turkish |
| No account | **Verified**: owner confirmation 2026-11-24 (Şerif). README and CHANGELOG do not mention accounts; consistent with the app (no sign-in, privacy manifests collect no data) |
| Developer Şerif Şadi Şenkule, Ankara, Türkiye | Site footer and `src/site.ts` already name Şerif Şadi Şenkule and link https://serifsadi.dev. GitHub profile location is Ankara. Ankara and Türkiye on the privacy page are from the owner’s statement for this submission (2026-11-25), not from the app README |
| Free from GitHub Releases and Homebrew; Mac App Store copy is a one-time purchase with the same features; no in-app purchases or subscriptions | Owner statement 2026-11-25. App repo `RELEASING.md` describes the same app for the Developer ID disk image and the Mac App Store package. The app README does not mention a price. No StoreKit usage was found in the README or changelog |
| No ads and no crash reporting | Owner statement 2026-11-25. README Privacy: no analytics; privacy manifests declare no tracking and no collected data |
| Map requests send the user’s IP address and the requested tiles to OpenFreeMap. OpenFreeMap does not use cookies or tracking. Access logs do not store IP addresses. Error logs may include IP and the requested URL. Server logs are deleted after 7 days. Security-incident logs, which may include IP addresses, are deleted when the investigation ends or after 30 days, whichever comes first | **Verified** 2026-11-25 at https://openfreemap.org/privacy/ (Last Updated: October 8, 2026). The policy says it also covers https://tiles.openfreemap.org. Wording on the page, not the shorter “up to 7 days / up to 30 days” summary: error logs are deleted after 7 days; security-incident IP logs are deleted after the investigation or 30 days, whichever comes first; all other server logs are deleted after 7 days |
| App Store purchases and refunds are handled by Apple. The developer receives no payment details. Refunds: https://reportaproblem.apple.com | Owner statement 2026-11-25. Standard Apple purchase handling; not described in the app README |
| Contact email contact@geopeek.app | Owner chose this address on 2026-11-25. It is active Cloudflare email routing. Used as a mailto link on the privacy and support pages, EN and TR. GitHub issues stay as the other contact path |
| Set as Default… is in the GeoPeek menu and on the welcome screen | CHANGELOG 0.4.1 |
| "Lightweight Mac app and Quick Look extension" | README intro ("A lightweight macOS app and Quick Look extension") |
| Finder column view shows the same Quick Look preview; ↑ ↓ move between files | 0.4.1 screen recordings in light and dark (geopeek-shots-041/{light,dark}/column-arrows*.mp4, column-*.png) |
| This website: no cookies; Cloudflare Web Analytics for visit counts (injected at the edge, cookieless, aggregate statistics); static; downloads hosted on GitHub | This repo: static Astro build; no cookies and no analytics script in dist (Cloudflare injects the Web Analytics beacon at the edge); DMG URL in src/site.ts points to GitHub Releases |
