#!/bin/sh
# Web encodes of the real Finder column-view recordings (native 1600x960, no interpolation).
# Source: warm-cache takes, captured at ~11.7 fps real time in a 24 fps container; output keeps 24 fps
# so no captured frame is dropped. Poster = first frame of the video, so play starts without a jump.
# usage: scripts/media/encode-column.sh /workspace/geopeek-shots-041
set -e
SRC=${1:-/workspace/geopeek-shots-041}; OUT=$(dirname "$0")/../../public/media
for t in light dark; do
  ffmpeg -y -loglevel error -i "$SRC/$t/column-arrows.mp4" -an -vf "fps=24" \
    -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 20 -preset slow -tune stillimage -movflags +faststart "$OUT/column-$t.mp4"
  ffmpeg -y -loglevel error -i "$SRC/$t/column-arrows.mp4" -an -vf "fps=24" \
    -c:v libvpx-vp9 -crf 32 -b:v 0 -row-mt 1 -deadline good "$OUT/column-$t.webm"
  ffmpeg -y -loglevel error -i "$SRC/$t/column-arrows.mp4" -frames:v 1 -c:v libwebp -quality 88 "$OUT/column-$t-poster.webp"
done
ls -la "$OUT"
