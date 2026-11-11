#!/usr/bin/env bash
set -euo pipefail
mkdir -p assets/audio
if [[ -s assets/audio/nihao.mp3 ]]; then
  echo "Pilot audio exists; not replacing an existing reviewed asset."
  exit 0
fi
source_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Zh_n%C7%90_h%C7%8Eo.ogg"
tmpfile="$(mktemp --suffix=.ogg)"
trap 'rm -f "$tmpfile"' EXIT
curl --fail --location --show-error --silent --retry 3 "$source_url" --output "$tmpfile"
ffmpeg -nostdin -hide_banner -loglevel error -y -i "$tmpfile" -ac 1 -ar 24000 -codec:a libmp3lame -b:a 48k assets/audio/nihao.mp3
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 assets/audio/nihao.mp3
test "$(wc -c < assets/audio/nihao.mp3)" -gt 1000
test "$(wc -c < assets/audio/nihao.mp3)" -lt 50000
echo "Small, decoded Mandarin audio verified."
