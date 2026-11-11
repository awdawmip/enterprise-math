#!/usr/bin/env bash
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
src=${1:-"$here/../recovered/src"}
inc=()
for dir in "$src"/brc_residual_sort_*/; do inc+=("-I$dir"); done
binary=$(mktemp)
trap 'rm -f "$binary"' EXIT
g++ -std=c++20 -O2 "${inc[@]}" "$here/probe_sweep.cpp" -o "$binary"
"$binary"
