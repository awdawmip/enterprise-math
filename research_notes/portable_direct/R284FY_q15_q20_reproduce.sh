#!/usr/bin/env bash
# Reproduce R284FY using the ORIGINAL pinned R284FV implementation files.
# Usage from research_notes/portable_direct:
#   bash R284FY_q15_q20_reproduce.sh . ./R284FY_calculation
set -euo pipefail
src="${1:-.}"
out="${2:-./R284FY_calculation}"
mkdir -p "$out"
out="$(cd "$out" && pwd)"
g++ -O3 -std=c++17 "$src/R284FV_stable_cut_scan.cpp" -o "$out/R284FY_stable_cut_scan"
printf 'q,n,all_histograms,stable_survivors,edge0_survivors,edge01_survivors,sha256_of_stable_list\n' > "$out/R284FY_results.csv"
for q in $(seq "${Q_MIN:-15}" "${Q_MAX:-20}"); do
  for n in $((4*q+8)) $((4*q+9)); do
    "$out/R284FY_stable_cut_scan" "$q" "$n" "$out"
    python3 - "$src" "$out" "$q" "$n" <<'PY'
import hashlib, importlib.util, math, pathlib, sys
src, out, q, n = sys.argv[1], pathlib.Path(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
file = out / f'R284FV_q{q}_n{n}_stable.txt'
raw = file.read_bytes()
hist = [tuple(map(int, line.split())) for line in raw.decode('utf-8').splitlines()]
assert all(len(x) == 7 and sum(x) == n and min(x) >= 0 for x in hist)
assert len(hist) == (7 if n == 4*q+8 else 66)
spec = importlib.util.spec_from_file_location('pinned_R284FV', pathlib.Path(src) / 'R284FV_prefix_count_lattice.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.Q = q
one = [x for x in hist if mod.safe_path(x, 0)]
two = [x for x in one if mod.safe_path(x, 1)]
A, B = 2*q+5, 2*q+3
F0 = (0,0,0,0,A,B,0)
F = [(0,0,0,0,A,B,1),(0,0,0,0,A,B+1,0),(0,0,0,0,A+1,B,0),
     (0,0,0,1,A-1,B,1),(0,0,0,1,A,B,0),
     (0,0,1,0,A-1,B,1),(0,0,1,0,A,B,0),
     (0,1,0,0,A-1,B,1),(0,1,0,0,A,B,0),(1,0,0,0,A,B,0)]
assert sorted(one) == sorted([F0] if n == 4*q+8 else F), (q, n)
assert not two, (q, n)
with (out / 'R284FY_results.csv').open('a', encoding='utf-8') as f:
    f.write(f'{q},{n},{math.comb(n+6, 6)},{len(hist)},{len(one)},{len(two)},{hashlib.sha256(raw).hexdigest()}\n')
print('EXACT_PASS', q, n, 'stable', len(hist), 'first', len(one), 'two_edges', len(two))
PY
  done
done
