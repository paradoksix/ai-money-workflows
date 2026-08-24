$ErrorActionPreference = "Stop"
$root = Join-Path $PSScriptRoot "upstreams"
New-Item -ItemType Directory -Force -Path $root | Out-Null

$repos = @(
  @{ Name="01-nano-banana-pro-creative-director"; Url="https://github.com/sirlifehacker/Nano-Banana-Pro-Creative-Director.git"; Commit="1c82b35f1db29e9f0ed35f5e0680148241a371b5" },
  @{ Name="02-linkedin-jobs-decision-maker"; Url="https://github.com/sirlifehacker/n8n-automations.git"; Commit="dcab49176024e410a1cc555ea8bda3f21f4c6f1f" },
  @{ Name="03-b2b-lead-search-engine"; Url="https://github.com/sirlifehacker/lead-gen-hacker.git"; Commit="9ed891f4bc2666f19941ea8c03841555c4812b66" },
  @{ Name="04-social-story-scraper"; Url="https://github.com/sirlifehacker/social-story-scraper.git"; Commit="69de2889cbe8a80124581d5f5b2abede4d221b3f" },
  @{ Name="05-insurance-lawyer-lead-gen"; Url="https://github.com/lucaswalter/n8n-ai-automations.git"; Commit="08e33b6d589789bc06957611cf932d3602b81117" }
)

foreach ($r in $repos) {
  $dest = Join-Path $root $r.Name
  if (Test-Path $dest) {
    Write-Host "[skip] $($r.Name) zaten var"
    continue
  }
  Write-Host "[clone] $($r.Url)"
  git clone $r.Url $dest
  git -C $dest checkout $r.Commit
  Write-Host "[ok] $($r.Name) @ $($r.Commit)"
}
