#!/bin/bash
# Deploy viewer.html → https://przebi.github.io/maraton-chicago-2026/
# GitHub Pages auto-deploys from docs/ folder on main branch.
# Usage: ./scripts/deploy-viewer.sh

set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Sync files → docs/
cp viewer.html docs/index.html
cp runs.html docs/runs.html
echo "[1/3] Synced viewer.html + runs.html → docs/"

# Stage + commit (idempotent)
git add docs/index.html docs/runs.html
if git diff --staged --quiet; then
  echo "[2/3] No changes in docs/, skipping commit"
else
  git commit -m "deploy: sync docs/ with viewer.html + runs.html"
  echo "[2/3] Committed docs/ sync"
fi

# Push to main → GitHub Pages auto-rebuild
echo "[3/3] Pushing to main (GitHub Pages auto-rebuild ~30-60s)..."
git push 2>&1 | tail -3
echo "Live URL: https://przebi.github.io/maraton-chicago-2026/"
