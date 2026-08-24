#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)/upstreams-disputed"
mkdir -p "$ROOT"
git clone "https://github.com/YonkoSam/whatsapp-python-chatbot.git" "$ROOT/whatsapp-python-chatbot"
git -C "$ROOT/whatsapp-python-chatbot" checkout "8a1ae46805410b11d43eebf023ab23df41f9d116"
echo "UYARI: Bu repo ile ilişkili $275 gelir iddiasının güvenilirliği Reddit yorumlarında tartışmalı."
