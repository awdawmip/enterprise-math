#!/usr/bin/env bash
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd)
src=${1:-"$here/../recovered/src"}
compiler=${CXX:-g++}
inc=()
for dir in "$src"/brc_residual_sort_*/; do inc+=("-I$dir"); done
build=${TMPDIR:-/tmp}/brc_prefix_verify_$(basename "$here")
mkdir -p "$build"
for mode in optimized sanitized; do
    flags=(-O3 -DNDEBUG)
    if [[ $mode == sanitized ]]; then flags=(-O1 -g0 -fsanitize=address,undefined -fno-omit-frame-pointer); fi
    "$compiler" -std=c++20 "${flags[@]}" "${inc[@]}" "$here/verify7.cpp" -o "$build/$mode"
    if [[ $mode == sanitized ]]; then
        ASAN_OPTIONS=detect_leaks=0 UBSAN_OPTIONS=halt_on_error=1 "$build/$mode"
    else
        "$build/$mode"
    fi
done
