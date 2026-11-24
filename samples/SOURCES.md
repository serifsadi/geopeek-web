# GeoPeek 0.4.1 website sample files: sources

All geometry and names come unmodified from OpenStreetMap (fetched 2026-11-24 via api.openstreetmap.org and Overpass API).
License: ODbL 1.0. Attribution required: "© OpenStreetMap contributors" (https://www.openstreetmap.org/copyright).
Basemap in captures: OpenFreeMap tiles (OpenMapTiles schema, © OpenMapTiles, © OpenStreetMap contributors), as shown in the in-map attribution.

- city-parks.geojson: 23 leisure=park ways around Taksim/Beşiktaş (Overpass, osm_base 2026-07-15). Names as in OSM; area_ha computed from geometry. osm_id per feature.
- bus-stops.geojson: 28 named highway=bus_stop nodes in bbox 28.980,41.032,28.995,41.042 (OSM API map call). osm_id per feature.
- hiking-trails.kml: Sultans Trail stages ST615 "Eyüp - Istanbul" (relation/19946374, ~7.3 km) and ST616 "Epilogue" (relation/20056264, ~4.2 km). Member ways joined end to end; no smoothing.
- bike-route.gpx: "Üsküdar-Hidiv Kasrı" bicycle route (relation/17515214, OSM distance tag 4.44 km; 4 track segments as mapped). No timestamps or elevation (none in OSM).
- neighborhoods.kmz: 14 admin_level=8 mahalle boundaries in Beyoğlu/Şişli/Beşiktaş around Taksim (relation/full for each).
