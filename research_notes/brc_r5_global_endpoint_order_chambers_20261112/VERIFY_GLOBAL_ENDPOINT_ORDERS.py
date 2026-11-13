#!/usr/bin/env python3
"""Exact finite proof: global legal 15-atom order counts in R5 parameter r.

Runs the immutable original P/Q--BRC 28-coordinate fixture. Python stdlib only.
The values in this file are exact rational checks, not numerical tolerances.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from runpy import run_path

parent = (Path(__file__).resolve().parent.parent /
          "brc_r5_sharp_nonlocal_fifteen_ray_20261111" /
          "VERIFY_R5_SHARP_RAY.py")
z = run_path(str(parent))
X, IX, steps, D, eps = (z[k] for k in ("X", "IX", "steps", "D", "eps_max"))
assert len(X) == 28 and len(steps) == 15
x = X[IX[(1, 3)]]
assert x == X[IX[(0, 3)]] == F(155682221, 25142124560000000)
assert eps == F(9, 115400000)
H = [0] * 28
for i, a in ((1, -23), (2, 28), (6, -5)):
    H[IX[(i, 3)]] = a
    H[IX[(i, 1)]] = -a
assert not any(z["obs"](H))
A = [tuple(int(36 * alpha * v) for v in move)
     for j, i, alpha, move in steps]
assert all(F(sum(A[j][k] for j in range(15)), 36) == D[k]
           for k in range(28))
P = [(0,) * 28] + [None] * ((1 << 15) - 1)
for mask in range(1, 1 << 15):
    b = mask & -mask
    j = b.bit_length() - 1
    P[mask] = tuple(P[mask ^ b][k] + A[j][k] for k in range(28))

rlo = F(-427508577031693280, 628800490619)
rhi = F(1, 23)
# These are exactly the intersection of all nonnegativity half-lines
# for the initial and complete-15-atom endpoint states.
low, high = [], []
for endpoint in (X, tuple(X[k] + eps * D[k] for k in range(28))):
    for k, a in enumerate(H):
        if a:
            root = -endpoint[k] / (x * a)
            (low if a > 0 else high).append(root)
assert max(low) == rlo and min(high) == rhi

# Endpoint feasibility of a prefix mask is a finite system of 28
# inequalities affine in r. It is a closed interval or empty.
end_intervals = []
for mask in range(1 << 15):
    lower, upper = rlo, rhi
    for k in range(28):
        v = X[k] + eps * F(P[mask][k], 36)
        h = H[k]
        if h:
            root = -v / (x * h)
            if h > 0: lower = max(lower, root)
            else: upper = min(upper, root)
        elif v < 0:
            lower, upper = F(1), F(0)
            break
    end_intervals.append((lower, upper) if lower <= upper else None)

right_counts = Counter(upper for interval in end_intervals if interval
                       for lower, upper in (interval,) if upper < rhi)
left_counts = Counter(lower for interval in end_intervals if interval
                      for lower, upper in (interval,) if lower > rlo)
q_values = (15, 12, 3)
roots = tuple((1 - F(q) * eps / x) / 23 for q in q_values)
assert roots == tuple(sorted(roots))
assert roots == (F(-16881105436483, 2066058754891),
                 F(-13486918620883, 2066058754891),
                 F(-3304358174083, 2066058754891))
assert sum(z is not None for z in end_intervals) == 16462
assert len(end_intervals) - 16462 == 16306
assert not left_counts
assert right_counts == Counter({roots[0]: 3592,
                                roots[1]: 3347,
                                roots[2]: 2414})
# Every disappearing mask is limited by the same coordinate (1,3),
# with P_k=-36*q and r=(1-q*eps/x)/23, q=15,12,3.
limiting_k = IX[(1, 3)]
for mask, interval in enumerate(end_intervals):
    if interval and interval[1] in roots:
        q = q_values[roots.index(interval[1])]
        assert P[mask][limiting_k] == -36 * q
        assert (X[limiting_k] + x * interval[1] * H[limiting_k]
                + eps * F(P[mask][limiting_k], 36)) == 0

def counts(r):
    feasible = [it is not None and it[0] <= r <= it[1]
                for it in end_intervals]
    backward = [0] * (1 << 15)
    backward[0] = 1
    for mask in range(1, 1 << 15):
        if feasible[mask]:
            bits = mask
            while bits:
                b = bits & -bits
                backward[mask] += backward[mask ^ b]
                bits -= b
    # Independent forward Boolean-lattice recurrence.
    forward = [0] * (1 << 15)
    forward[0] = 1
    for mask in range(1 << 15):
        if feasible[mask]:
            for j in range(15):
                nxt = mask | (1 << j)
                if nxt != mask and feasible[nxt]:
                    forward[nxt] += forward[mask]
    assert forward[-1] == backward[-1]
    return sum(feasible), backward[-1]

b = (rlo,) + roots + (rhi,)
expected = ((16462, 88224369664), (12870, 22377295168),
            (9523, 8884916032), (7109, 3514190816))
for i in range(4):
    midpoint = (b[i] + b[i+1]) / 2
    assert counts(midpoint) == expected[i], (i, midpoint)
assert counts(rlo) == expected[0]
for i, gate in enumerate(roots):
    assert counts(gate) == expected[i]  # right-closed loss gate
assert counts(rhi) == expected[-1]
print('FIXTURE_SHA_REF', '435e77af0d180eac32bd1f9c4c464bc4010b7551')
print('TOTAL_MASKS', len(P), 'INTERVAL_VALID_MASKS', 16462)
print('R_DOMAIN', rlo, rhi)
print('ONLY_RIGHT_GATE_VALUES', roots)
print('GATE_MASKS_REMOVED', (3592, 3347, 2414))
print('CHAMBER_FEASIBLE_MASKS_AND_LEGAL_ORDERS', expected)
print('ORDER_DROPS', tuple(expected[i][1] - expected[i+1][1]
                           for i in range(3)))
print('BOTH_INDEPENDENT_DP_RECURRENCES_MATCH', True)
print('PASS_R5_GLOBAL_ENDPOINT_ORDER_FOUR_CHAMBERS')
