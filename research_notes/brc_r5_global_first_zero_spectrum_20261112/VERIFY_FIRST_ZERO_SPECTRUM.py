#!/usr/bin/env python3
"""R5 global first-zero spectrum: exact verification on the frozen 15-atom fixture.

Run from a checkout of the stacked PR branch:
python research_notes/brc_r5_global_first_zero_spectrum_20261112/VERIFY_FIRST_ZERO_SPECTRUM.py

Depends on the self-contained exact parent VERIFY_R5_UNIFORM_ROBUST_15.py
at the inherited frozen R5 branch; it re-executes the parent assertions.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
from runpy import run_path

root = Path(__file__).resolve().parents[1]
fixture = root / "brc_r5_uniform_robust_sharp_15_20261112" / "VERIFY_R5_UNIFORM_ROBUST_15.py"
g = run_path(str(fixture))   # Includes full parent rectangle and lower-bound checks.

X, H, x, L, U, E = (g[z] for z in ("X", "H", "x", "L", "U", "eps"))
V, IX, moves, partial, N = (g[z] for z in ("V", "IX", "moves", "partial", "N"))
assert N == 32768 and len(X) == len(V) == 28 and len(moves) == 15

core = {IX[(0, 3)], IX[(1, 3)], IX[(0, 2)], IX[(6, 1)]}
margins = []
for k in range(28):
    b = min(X[k] + x * L * H[k], X[k] + x * U * H[k])
    c = sum((min(F(0), atom[k]) for atom in moves), F(0))
    margins.append(b + E * c)
outside = [(margins[k], V[k]) for k in range(28) if k not in core]
assert len(outside) == 24
assert all(v > 0 for v, _ in outside)
assert min(outside) == (F(71458139439, 72283608110000000), (2, 1))
assert margins[IX[(0, 2)]] == margins[IX[(6, 1)]] == 0
assert all(X[k] + x * r * H[k] > 0
           for k in (IX[(0, 2)], IX[(6, 1)]) for r in (L, U))
assert all(sum(min(F(0), atom[k]) for atom in moves) < 0
           for k in (IX[(0, 2)], IX[(6, 1)]))

k0, k1 = IX[(0, 3)], IX[(1, 3)]
weights = tuple(int(36 * atom[k0]) for atom in moves)
assert weights == (336, 184, 18, 169, 64, 84, 299, 126, 52, 16,
                   -420, -483, -144, -221, -80)
sums = {sum(weights[a] for a in range(15) if s & (1 << a))
        for s in range(N)}
assert len(sums) == 2293 and (min(sums), max(sums)) == (-1348, 1348)
Nfixed = {-h for h in sums if h <= -3}
assert len(Nfixed) == 1144 and min(Nfixed) == 3 and max(Nfixed) == 1348
assert all(F(0) < 36*x/n < E for n in Nfixed)
negative1 = {-int(36*partial[s][k1]) for s in range(N)
             if partial[s][k1] < 0}
assert negative1 == {108, 432, 540}

# Exact all-real-r fixed capacity witnesses: 28 inequalities at L and U.
witness = {}
for s in range(1, N):
    n = -int(36*partial[s][k0])
    if n not in Nfixed or n in witness:
        continue
    t = 36*x/n
    base = tuple(X[k] + t*partial[s][k] for k in range(28))
    if all(base[k] + x*r*H[k] >= 0
           for r in (L, U) for k in range(28)):
        witness[n] = s
assert len(witness) == 1144 and sum(witness.values()) == 9387630
assert {n:witness[n] for n in (3,420,910,1348)} == {
    3:1050, 420:1024, 910:30724, 1348:31744}

# For each moving family, target0 increases, target1 is the only
# coordinate capable of vanishing strictly before E.
moving = {15:1023, 12:991, 3:1022}
for q,s in moving.items():
    assert 36*partial[s][k1] == -36*q
    assert 36*partial[s][k0] > 0
    rho = (1-q*E/x)/23
    assert L < rho < U
    assert X[k1] + x*U*H[k1] == 0
    assert X[k1] + x*rho*H[k1] == q*E

# The 3432 moving/fixed coincidences are all and only the solutions
# to x*(1-23r)/q = 36*x/n within the open ray.
atlas = defaultdict(list)
for q in (15,12,3):
    rho=(1-q*E/x)/23
    for n in Nfixed:
        r = (1-F(36*q,n))/23
        assert L < r < U and rho < r
        assert x*(1-23*r)/q == 36*x/n
        atlas[r].append((q,n))
multiplicity = Counter(map(len,atlas.values()))
assert (sum(map(len,atlas.values())), len(atlas)) == (3432, 2905)
assert multiplicity == Counter({1:2603, 2:77, 3:225})
assert set(atlas[F(0)]) == {(15,540),(12,432),(3,108)}

def spectrum_size(r):
    active = {q for q in (15,12,3)
              if (1-q*E/x)/23 < r < U}
    return 1144 + len(active) - len(atlas.get(r,()))

assert spectrum_size(F(0)) == 1144
assert spectrum_size(F(-10)) == 1144
assert spectrum_size(F(1,1000)) == 1147
assert spectrum_size(L) == spectrum_size(U) == 1144

print("FROZEN_PARENT 0c15f0d5e70748eca288dd01767561b8c55c57ad")
print("MASKS",N,"COORDINATES",len(X))
print("STRICT_POSITIVE_MARGIN_OTHER_24",min(outside)[0])
print("TWO_ENDPOINT_ONLY_COORDINATES",[(0,2),(6,1)])
print("INTERIOR_BOTTLENECK_COORDINATES",[(0,3),(1,3)])
print("FIXED_FIRST_ZERO_VALUES",len(Nfixed),"N_MIN_MAX",min(Nfixed),max(Nfixed))
print("FIXED_WITNESS_MASK_CHECKSUM",sum(witness.values()))
print("MOVING_SLOPE_FAMILIES_Q",(15,12,3))
print("MOVING_WITNESS_MASKS",moving)
print("MOVING_FIXED_COLLISION_PAIRS",sum(map(len,atlas.values())))
print("DISTINCT_COLLISION_PARAMETERS",len(atlas))
print("COLLISION_MULTIPLICITIES",dict(sorted(multiplicity.items())))
print("ZERO_R_TRIPLE_RESONANCE",atlas[F(0)])
print("PASS_R5_GLOBAL_TWO_COORDINATE_FIRST_ZERO_AND_COLLISION_ATLAS")
