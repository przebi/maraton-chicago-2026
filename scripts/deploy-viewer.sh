#!/bin/bash
# Deploy viewer.html → https://przebi.netlify.app
# Usage: ./scripts/deploy-viewer.sh

set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Load credentials
if [ ! -f .netlify-deploy.env ]; then
  echo "ERROR: .netlify-deploy.env not found in $ROOT"
  exit 1
fi
set -a
source ./.netlify-deploy.env
set +a

# Sync viewer.html → deploy/index.html
cp viewer.html deploy/index.html
echo "[1/2] Copied viewer.html → deploy/index.html"

# Deploy
echo "[2/2] Deploying to https://przebi.netlify.app..."
netlify deploy --site="$NETLIFY_SITE_ID" --dir="$ROOT/deploy" --prod --no-build 2>&1 | tail -8
