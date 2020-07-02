#!/bin/sh

BUILDSCRIPTS="$(dirname "$0")"

source "$BUILDSCRIPTS/output_formatting.sh"

# Sort imports
echo "Sorting Imports..."
isort --recursive --atomic .
end_section "-"

# Run black auto formatter
echo "Formatting with Black..."
black .
end_section "-"
