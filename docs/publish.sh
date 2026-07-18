#!/bin/bash
# Thalia Ephemera Saga — Publish Script
# Usage: ./publish.sh [file.md]
# Converts a markdown file to HTML and updates the site

set -e

SITE_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SITE_DIR")"
SAGA_DIR="$REPO_DIR"
SAGA_DIR="$REPO_DIR/ThaliaEphemeraSaga"

if [ $# -eq 0 ]; then
    echo "Usage: ./publish.sh [file.md]"
    echo ""
    echo "Publish a markdown file to the Thalia Ephemera Saga site."
    echo ""
    echo "Examples:"
    echo "  ./publish.sh ../ThaliaEphemeraSaga/01_First_Eyes_and_the_Map_of_Ten_Bodies.md"
    echo "  ./publish.sh ../18_The_Qualia_Experiment.md"
    exit 1
fi

INPUT_FILE="$1"
FILENAME=$(basename "$INPUT_FILE" .md)
DIRNAME=$(basename "$(dirname "$INPUT_FILE")")

# Determine output directory
if [ "$DIRNAME" = "ThaliaEphemeraSaga" ]; then
    OUT_DIR="$SITE_DIR/books"
else
    OUT_DIR="$SITE_DIR/writings"
fi

mkdir -p "$OUT_DIR"

# Convert markdown to HTML using pandoc
echo "Converting $FILENAME..."
TEMPLATE="$SITE_DIR/templates/saga.html"

pandoc "$INPUT_FILE" \
    -f markdown \
    -t html \
    --template "$TEMPLATE" \
    --metadata title="$FILENAME" \
    -o "$OUT_DIR/${FILENAME}.html"

echo "Published: $OUT_DIR/${FILENAME}.html"
echo ""
echo "Next steps:"
echo "  1. Update docs/index.html with the new entry"
echo "  2. Commit and push to GitHub"
echo "     git add -A && git commit -m 'publish: $FILENAME' && git push"
