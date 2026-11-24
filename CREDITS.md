# Credits and data sources

## Sample data (all from OpenStreetMap, ODbL 1.0)
Attribution: "© OpenStreetMap contributors", https://www.openstreetmap.org/copyright.
Geometry and names are unmodified OSM data, fetched 2026-11-24 via api.openstreetmap.org and the Overpass API.
The files are in `samples/` (with the original `SOURCES.md`).

| File | Content | OSM source |
|---|---|---|
| `city-parks.geojson` | 23 `leisure=park` ways around Taksim, Maçka, Beşiktaş. Properties `name`, `leisure`, `area_ha` (computed from geometry), `osm_id` | Overpass, osm_base 2026-07-15. Example: Maçka Demokrasi Parkı = way/26970150 |
| `bus-stops.geojson` | 28 named `highway=bus_stop` nodes, bbox 28.980,41.032,28.995,41.042 | OSM API map call, 2026-11-24; `osm_id` per feature |
| `hiking-trails.kml` | Sultans Trail stages ST615 "Eyüp - Istanbul" (relation/19946374, about 7.3 km) and ST616 "Epilogue" (relation/20056264, about 4.2 km); member ways joined end to end, no smoothing | OSM relations |
| `bike-route.gpx` | "Üsküdar-Hidiv Kasrı" bicycle route (relation/17515214, OSM distance 4.44 km), 4 track segments as mapped, no time or elevation | OSM relation |
| `neighborhoods.kmz` | 14 `admin_level=8` mahalle boundaries around Taksim (relations 7980976, 7982393, 7982394, 7982395, 7982396, 7982397, 7982475, 7982476, 7982477, 7982478, 7982482, 9296001, 9319824, 9319855) | OSM relation/full |

Used on the site (light and dark captures): `city-parks.geojson` (hero, map, table, stats), `hiking-trails.kml` and `bike-route.gpx` (formats).
The Finder captures show all five file names. The old Zoning_District images (unknown source) are removed.

## Basemap in every map image
"© OpenFreeMap © OpenMapTiles © OpenStreetMap contributors", printed under the hero, under each map image and in the footer.
- Tiles and styles: OpenFreeMap (https://openfreemap.org), `dark` for dark captures, `positron` for light captures.
- Schema: © OpenMapTiles (https://openmaptiles.org).
- Map data: © OpenStreetMap contributors, ODbL.
- Rendered by MapLibre GL JS 5.24.1 (BSD-3-Clause) inside GeoPeek.

## Captures
GeoPeek 0.4.1 (build 4), window-only `screencapture -o`, Retina 2x, 2026-11-24. No retouching.
The Quick Look title bar (system "Open with ..." button for the default app) is clipped by CSS layout in the hero
and the social image, not edited in the files.

## Site
- Fonts: system fonts only. No web fonts.
- Icons: inline SVG. App icon and screenshots: GeoPeek, MIT License.
