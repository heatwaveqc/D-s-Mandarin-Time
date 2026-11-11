#!/usr/bin/env bash
set -euo pipefail
mkdir -p assets/audio
if [[ -s assets/audio/nihao.ogg ]]; then
  echo "Pilot audio exists; not replacing a credited asset."
  exit 0
fi
# Original 1.1s human Mandarin pronunciation recording, CC BY-SA 3.0.
# Author: Sjors Provoost, see docs/AUDIO_ASSETS.md.
source_url="https://upload.wikimedia.org/wikipedia/commons/7/7d/Zh_n%C7%90_h%C7%8Eo.ogg"
curl --fail --location --show-error --silent --retry 3 "$source_url" --output assets/audio/nihao.ogg
python3 - <<'PY'
from pathlib import Path
data = Path("assets/audio/nihao.ogg").read_bytes()
if not data.startswith(b"OggS") or not (1000 < len(data) < 50000):
    raise SystemExit("Invalid or unexpectedly sized Ogg recording")
print(f"Recorded Mandarin Ogg sample: {len(data)} bytes; Ogg header confirmed")
PY
