#!/usr/bin/env bash
set -euo pipefail
paths=(apps packages infrastructure scripts package.json pyproject.toml compose.yaml)
if rg -n --glob '!docs/**' --glob '!README.md' --glob '!scripts/check-no-real-trading.*' 'ENABLE_REAL_TRADING=true|/api/v3/order|fapi/v1/order|sapi/|binance|ccxt|alpaca|interactivebrokers|secret_key|private_key' "${paths[@]}"; then
  echo "Potential real trading or secret pattern found" >&2
  exit 1
fi
echo "No real trading patterns found"
