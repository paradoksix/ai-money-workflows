$ErrorActionPreference = "Stop"
$root = Join-Path $PSScriptRoot "upstreams-disputed"
New-Item -ItemType Directory -Force -Path $root | Out-Null
$dest = Join-Path $root "whatsapp-python-chatbot"
git clone "https://github.com/YonkoSam/whatsapp-python-chatbot.git" $dest
git -C $dest checkout "8a1ae46805410b11d43eebf023ab23df41f9d116"
Write-Host "UYARI: Bu repo ile ilişkili $275 gelir iddiasının güvenilirliği Reddit yorumlarında tartışmalı."
