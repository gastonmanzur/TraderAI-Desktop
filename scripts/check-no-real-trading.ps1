$ErrorActionPreference = "Stop"
$matches = rg -n --glob '!docs/**' --glob '!README.md' --glob '!scripts/check-no-real-trading.*' 'ENABLE_REAL_TRADING=true|/api/v3/order|fapi/v1/order|sapi/|binance|ccxt|alpaca|interactivebrokers|secret_key|private_key' apps packages infrastructure scripts package.json pyproject.toml compose.yaml
if ($LASTEXITCODE -eq 0) { Write-Error "Potential real trading or secret pattern found" }
Write-Output "No real trading patterns found"
