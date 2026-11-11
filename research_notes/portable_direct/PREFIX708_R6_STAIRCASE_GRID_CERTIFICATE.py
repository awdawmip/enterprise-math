#!/usr/bin/env python3
"""PREFIX-708: exact rational 1024x1024 staircase exclusion certificate.

Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependencies: PREFIX-705 survivor monotonicity, PREFIX-706 rational witness,
PREFIX-707 two-sided single-clock variance cell bound and Efron-Stein tensor bound.
This program independently reconstructs all 189 survivor-count rows.
"""
from bisect import bisect_left
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json

N, DEN, GRID = 189, 1 << 18, 1024
PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"

@lru_cache(None)
def inside(m, k, a):
    return 40 * (m + 1) * comb(m, k) * a**k * (DEN - a)**(m-k) > DEN**m

@lru_cache(None)
def wide(m, k):
    if k > m // 2:
        return wide(m, m-k)
    mid = k * DEN // m
    assert inside(m, k, mid)
    if k == 0:
        left_lo = left_hi = 0
    else:
        lo, hi = 0, mid
        assert not inside(m, k, lo)
        while hi-lo > 1:
            x = (lo+hi)//2
            if inside(m, k, x):
                hi = x
            else:
                lo = x
        left_lo, left_hi = lo, hi
    lo, hi = mid, DEN
    assert not inside(m, k, hi)
    while hi-lo > 1:
        x = (lo+hi)//2
        if inside(m, k, x):
            lo = x
        else:
            hi = x
    right_lo, right_hi = lo, hi
    if 4*(right_lo-left_hi) > DEN:
        return True
    if 4*(right_hi-left_lo) < DEN:
        return False
    raise AssertionError(("uncertified width", m, k))

rows = [{0: 1}]
for m in range(1, N+1):
    new = defaultdict(int)
    for k, v in rows[-1].items():
        new[k] += v
        new[k+1] += v
    rows.append({k: v for k, v in new.items() if wide(m, k)})
assert len(rows) == N+1 and not rows[-1]
assert sum(len(r) for r in rows[:N]) == 9529
assert rows[25] == {k: comb(25, k) for k in range(1,25)}

@lru_cache(None)
def moments(p):
    a, b = p.numerator, p.denominator
    A, C = F(0), F(0)
    for n, row in enumerate(rows[:N]):
        if a == 0:
            num = row.get(0, 0) * b**n
        elif a == b:
            num = row.get(n, 0) * b**n
        else:
            num = sum(v * a**k * (b-a)**(n-k) for k, v in row.items())
        s = F(num, b**n)
        A += s
        C += (2*n+1)*s
    d, D2 = N-A, N*N-2*N*A+C
    return A, C, d, D2

def cap(l, r):
    A_l, _, _, D2_l = moments(l)
    _, C_r, d_r, _ = moments(r)
    return min(C_r + A_l - A_l*A_l,
               N + D2_l - d_r - d_r*d_r)

caps = [cap(F(i, 2*GRID), F(i+1, 2*GRID)) for i in range(GRID)]
b = F(559812917, 1000000)
ordered = sorted(caps)
counts = [bisect_left(ordered, b-u) for u in caps]
n_cert = sum(counts)
positive_gaps = [b-u-ordered[k-1] for u, k in zip(caps, counts) if k]
min_gap = min(positive_gaps)
fraction = F(n_cert, GRID*GRID)
area = fraction / 4
ratio_to_prefix707 = fraction/F(16,81)
assert n_cert == 345931
assert fraction == F(345931,1048576)
assert min_gap > F(2672,1000000)
assert ratio_to_prefix707 == F(28020411,16777216)
assert sum(1 for k in counts if k == 0) > 0
# The strictly positive gap applies to every selected closed cell.
result = {
    "schema":"PREFIX708_R6_EXACT_STAIRCASE_CERTIFICATE_V1",
    "date":"2026-11-12 Asia/Shanghai",
    "scientific_pin":PIN,
    "source_preconditions":[
        "PREFIX700 189-level frozen survivor recurrence",
        "PREFIX705 certified stochastic monotonicity of all survivor tails",
        "PREFIX706 certified W(e)-mu(e)/2 > 559812917/1000000",
        "PREFIX707 two-sided cell variance enclosure and Efron-Stein bound"
    ],
    "rows":N, "nonzero_survivor_count_cells":9529,
    "grid_cells_per_axis":GRID,
    "certified_closed_cells":n_cert,
    "excluded_area":str(area),
    "fraction_of_full_square":str(fraction),
    "area_ratio_to_PREFIX707":str(ratio_to_prefix707),
    "uniform_gap_strict_lower_bound":"2672/1000000",
    "minimum_exact_gap_floor_millionths":min_gap.numerator*1000000//min_gap.denominator,
    "verification":"ALL_CHECKS_PASS PREFIX708-R6",
    "admission":"AUTHOR_RECOMPUTED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED"
}
Path(__file__).with_name("PREFIX708_R6_RESULTS.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(result["verification"])
print("cells:",n_cert,"area:",area,"fraction:",fraction)
print("min gap strict > 2672/1000000; ratio:",ratio_to_prefix707)
