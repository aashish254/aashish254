#!/usr/bin/env bash
# verify-repo-integrity.sh
# Automated health, link, and structure verification script for the profile repository.

set -euo pipefail

echo "========================================="
echo " Verifying Repository Integrity & Assets"
echo "========================================="

# 1. Check core files
REQUIRED_FILES=("README.md" "docs/architecture-patterns.md" "docs/developer-onboarding.md" ".github/workflows/profile-ci.yml")

for file in "${REQUIRED_FILES[@]}"; do
  if [[ -f "$file" ]]; then
    echo "  ✓ Found: $file"
  else
    echo "  ✗ Missing required file: $file"
    exit 1
  fi
done

# 2. Check internal markdown links
echo "Checking internal document references..."
grep -o 'docs/[a-zA-Z0-9_-]*\.md' README.md | while read -r link; do
  if [[ -f "$link" ]]; then
    echo "  ✓ Valid link: $link"
  else
    echo "  ✗ Broken relative link in README: $link"
    exit 1
  fi
done

echo "========================================="
echo " All repository integrity checks passed!"
echo "========================================="
