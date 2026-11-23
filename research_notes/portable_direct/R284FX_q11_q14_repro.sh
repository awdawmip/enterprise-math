#!/usr/bin/env bash
# R284FX: exact q=11..14 extension using the original R284FV flow oracles.
# Run from anywhere: bash research_notes/portable_direct/R284FX_q11_q14_repro.sh
set -euo pipefail
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
work_dir="$(mktemp -d)"
trap 'rm -rf "$work_dir"' EXIT
g++ -O3 -std=c++17 "$source_dir/R284FV_stable_cut_scan.cpp" -o "$work_dir/stable"
# The only change in the original R284FV Python oracle is its declared q interval.
sed 's/assert 7<=Q<=10 and n in (4\*Q+8,4\*Q+9)/assert 11<=Q<=14 and n in (4*Q+8,4*Q+9)/'   "$source_dir/R284FV_prefix_count_lattice.py" > "$work_dir/prefix.py"
grep -q 'assert 11<=Q<=14' "$work_dir/prefix.py"
for q in 11 12 13 14; do
  for offset in 8 9; do
    n=$((4*q+offset))
    "$work_dir/stable" "$q" "$n" "$work_dir"
    python3 "$work_dir/prefix.py" "$q" "$n" "$work_dir"
  done
done
