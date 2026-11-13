#!/usr/bin/env python3
"""PREFIX-755-R6, exact finite certificate for survivor-tail monotonicity.
Frozen BRC width/recurrence from PREFIX754_R6_INDEPENDENT_GRID_REPLAY.py.
For each n <=188: a[n,k] counts surviving length-n paths with k successes;
b[n,k] = a[n,k]/binom(n,k). Exhaustively check symmetry and central
unimodality of b; algebraic theorem then proves S_n(p) monotone for
ALL real p in [0,1/2]. No floats, NumPy, network or external services.
"""
import json
from collections import defaultdict
from functools import lru_cache
from math import comb

N = 189
W = 1 << 18

@lru_cache(maxsize=None)
def inside(n, k, x):
    return 40 * (n + 1) * comb(n, k) * x**k * (W - x)**(n - k) > W**n

@lru_cache(maxsize=None)
def wide(n, k):
    if k > n//2:
        return wide(n, n-k)
    mid = k * W // n
    assert inside(n, k, mid), ("midpoint-not-inside", n, k)
    if k == 0:
        lo = hi = 0
    else:
        a, b = 0, mid
        while b-a > 1:
            x = (a+b)//2
            if inside(n, k, x):
                b=x
            else:
                a=x
        lo, hi = a, b
    a, b = mid, W
    while b-a > 1:
        x = (a+b)//2
        if inside(n, k, x):
            a=x
        else:
            b=x
    if 4 * (a-hi) > W:
        return True
    if 4 * (b-lo) < W:
        return False
    raise ValueError(("undecidable-width", n, k))

rows = [{0: 1}]
for n in range(1, N+1):
    conv = defaultdict(int)
    for k, a in rows[-1].items():
        conv[k] += a
        conv[k+1] += a
    rows.append({k:v for k,v in conv.items() if wide(n,k)})

assert not rows[N], "nonzero-final-survivor"
assert sum(len(row) for row in rows[:N]) == 9529
symmetry_checks = 0
bernstein_pairs = 0
strict_pairs = 0
strict_rows = []
positive_positions = 0
for n, row in enumerate(rows[:N]):
    assert all(0<=k<=n and a>=1 for k,a in row.items())
    positive_positions += len(row)
    for k in range(n+1):
        assert row.get(k, 0) == row.get(n-k, 0), ("asymmetry",n,k)
        symmetry_checks += 1
    this_strict = 0
    for k in range(n//2):
        # Normalized inequality without division:
        # b[n,k+1]>=b[n,k] iff the cross product below is nonnegative.
        left = row.get(k+1,0) * comb(n,k)
        right = row.get(k,0) * comb(n,k+1)
        assert left >= right, ("Bernstein-unimodality",n,k,left,right)
        bernstein_pairs += 1
        if left > right:
            strict_pairs += 1
            this_strict += 1
    if this_strict:
        strict_rows.append(n)

assert bernstein_pairs == 8836
assert strict_pairs == 4511
assert len(strict_rows) == 164
assert strict_rows[0] == 25 and strict_rows[-1] == 188
assert symmetry_checks == sum(n+1 for n in range(N)) == 17955

result = {
    "schema":"PREFIX755_R6_BERNSTEIN_MONOTONICITY_EXACT_V1",
    "research_scope":"external two-Gamma clock auxiliary; 189-layer frozen BRC survivor count",
    "scientific_pin":"awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "source_algorithm":"PREFIX754_R6_INDEPENDENT_GRID_REPLAY.py frozen width/recursion",
    "arithmetic":"exact Python unbounded integers; rational comparisons by integer cross-products",
    "max_survival_layer":N,
    "positive_survivor_positions_layers_0_to_188":positive_positions,
    "survivor_positions_layer_189":len(rows[N]),
    "symmetry_integer_checks":symmetry_checks,
    "normalized_Bernstein_monotonicity_crossproduct_checks":bernstein_pairs,
    "strict_crossproduct_checks":strict_pairs,
    "equal_crossproduct_checks":bernstein_pairs-strict_pairs,
    "layers_with_some_strict_crossproduct":len(strict_rows),
    "strict_layer_min":strict_rows[0],
    "strict_layer_max":strict_rows[-1],
    "algebraic_transfer":[
        "b_nk symmetric and nondecreasing for k<=floor(n/2)",
        "b_nk = b_n0 + sum_{j=1}^{floor(n/2)} (b_nj-b_n,j-1) 1{j<=k<=n-j}",
        "P_p(j<=Bin(n,p)<=n-j) nondecreasing for 0<=p<=1/2",
        "S_n(p) nondecreasing on [0,1/2] for every 0<=n<=188",
        "Gamma(N,1) mixture survival and independent max stochastically nondecreasing",
        "mu(p,z) and raw M2(p,z) coordinatewise nondecreasing"
    ],
    "mathematical_acceptance":"AUTHOR_EXACT_INTEGER_FINITE_CERTIFICATE_UNREVIEWED_NOT_ADMITTED"
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
print("ALL_CHECKS_PASS PREFIX755-R6")
