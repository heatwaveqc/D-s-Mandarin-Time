#!/usr/bin/env bash
set -euo pipefail
mkdir -p assets/kung-fu
files=(
  "Kung Fu Border Left - Seamless Tile.png"
  "Kung Fu Border Left Terminator - Seamless.png"
  "Kung Fu Border Right - Seamless Tile.png"
  "Kung Fu Border Right Terminator - Seamless.png"
  "Kung Fu Border Top (left half) - Seamless Tile.png"
  "Kung Fu Border Top (right half) - Seamless Tile.png"
  "Kung Fu Corner Top-Left - Seamless.png"
  "Kung Fu Corner Top-Right - Seamless.png"
)
for name in "${files[@]}"; do
  out="assets/kung-fu/$name"
  if [[ ! -s "$out" ]]; then
    encoded="${name// /%20}"
    curl --fail --location --silent --show-error --retry 3 \
      "https://raw.githubusercontent.com/heatwaveqc/GATES/main/assets/seamless/$encoded" \
      --output "$out"
  fi
done
python3 - <<'PY'
from pathlib import Path
images = list(Path('assets/kung-fu').glob('*.png'))
if len(images) != 8:
    raise SystemExit(f'Expected 8 Kung Fu border PNGs; found {len(images)}')
for p in images:
    b = p.read_bytes()
    if b[:8] != b'\x89PNG\r\n\x1a\n' or len(b) < 1000:
        raise SystemExit(f'Invalid PNG: {p}')
print('Validated 8 self-hosted Kung Fu ornamental PNGs')
PY
