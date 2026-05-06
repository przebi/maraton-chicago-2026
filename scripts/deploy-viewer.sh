#!/bin/bash
# Deploy viewer.html → https://przebi.netlify.app
# Usage: ./scripts/deploy-viewer.sh

set -e
cd "$(dirname "$0")/.."

# Load credentials
source .netlify-deploy.env

# Sync viewer.html → deploy/index.html
cp viewer.html deploy/index.html
echo "[1/2] Copied viewer.html → deploy/index.html"

# Deploy
echo "[2/2] Deploying to https://przebi.netlify.app..."
netlify deploy --site="$NETLIFY_SITE_ID" --dir=deploy --prod --no-build 2>&1 | tail -8
