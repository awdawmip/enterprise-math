#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
OCTAVE_BIN="${OCTAVE_BIN:-octave}"
OUT="${1:-output}"
# Never mix an old scientific run with a new one. Choose a fresh directory.
if [ -e "$OUT" ]; then echo "Refusing existing output directory: $OUT" >&2; exit 2; fi
mkdir -p -- "$OUT"
OUT="$(realpath -- "$OUT")"
case "$OUT" in *"'"*) echo 'Quote in output path is unsupported' >&2; exit 2;; esac
{
  date -u '+Started %Y-%m-%dT%H:%M:%SZ'
  command -v "$OCTAVE_BIN" || true
  "$OCTAVE_BIN" --version
  python3 --version
  "$OCTAVE_BIN" --quiet --eval "addpath(pwd); generate_benchmarks('$OUT');"
  python3 run_brc.py --out "$OUT" --smoke
  python3 run_brc.py --out "$OUT"
  python3 run_brc.py --out "$OUT" --verify-only
  "$OCTAVE_BIN" --quiet --eval "addpath(pwd); analyze_results('$OUT');"
  date -u '+Finished %Y-%m-%dT%H:%M:%SZ'
} 2>&1 | tee "$OUT/execution.log"
