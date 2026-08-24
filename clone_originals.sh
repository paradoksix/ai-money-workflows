#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)/upstreams"
mkdir -p "$ROOT"
clone_pin() {
  local name="$1" url="$2" commit="$3"
  local dest="$ROOT/$name"
  if [ -d "$dest/.git" ]; then
    echo "[skip] $name zaten var"
    return
  fi
  echo "[clone] $url"
  git clone "$url" "$dest"
  git -C "$dest" checkout "$commit"
  echo "[ok] $name @ $commit"
}
clone_pin "01-nano-banana-pro-creative-director" "https://github.com/sirlifehacker/Nano-Banana-Pro-Creative-Director.git" "1c82b35f1db29e9f0ed35f5e0680148241a371b5"
clone_pin "02-linkedin-jobs-decision-maker" "https://github.com/sirlifehacker/n8n-automations.git" "dcab49176024e410a1cc555ea8bda3f21f4c6f1f"
clone_pin "03-b2b-lead-search-engine" "https://github.com/sirlifehacker/lead-gen-hacker.git" "9ed891f4bc2666f19941ea8c03841555c4812b66"
clone_pin "04-social-story-scraper" "https://github.com/sirlifehacker/social-story-scraper.git" "69de2889cbe8a80124581d5f5b2abede4d221b3f"
