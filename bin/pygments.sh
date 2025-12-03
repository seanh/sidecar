#!/bin/bash
# 
# Update the theme's Pygments CSS files with the latest versions from Pygments.
#
# Requires:
#
# * The `pygmentize` command: `uv tool install pygments`
# * jq
set -euo pipefail

for theme in $(pygmentize -L styles --json | jq --raw-output '.styles | keys | join(" ")')
do
  pygmentize -S "$theme" -f html -a .highlight | grep --invert-match 'line-height' > static/css/pygments/"$theme".css
done
