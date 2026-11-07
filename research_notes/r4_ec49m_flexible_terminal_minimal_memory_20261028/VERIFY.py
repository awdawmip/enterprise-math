#!/usr/bin/env python3
"""EC49M exact positive-rational auxiliary BRC observation certificates.
All calculations use only Python standard-library fractions; no float output.
"""
import json
from fractions import Fraction as F
from itertools import product

W = ("U", "V", "C0", "C1")
WP = (F(3, 8), F(3, 8), F(1, 8), F(1, 8))
WQ = (F(1, 8), F(1, 8), F(3, 8), F(3, 8))
YP = (F(1, 4), F(3, 4), F(1, 2), F(1, 2))
YQ = (F(3, 4), F(1, 4), F(1, 2), F(1, 2))
A_BY_W = (1, 0, 0, 1)


def obs_compressed(p0, p1, q0, q1, r00, r01, r10, r11):
    """W observed at first stage; later sees own A and Y, but forgets W."""
    take = (p0, p1, F(1), F(1))
    buy = (q1, q0, q0, q1)
    accept = ((r00, r01), (r10, r11))
    rv = []
    for ww, yy in ((WP, YP), (WQ, YQ)):
        a = F(0)
        t = F(0)
        for w in range(4):
            aa = A_BY_W[w]
            first = take[w]
            sensor = first * buy[w]
            a += ww[w] * sensor * (yy[w] * accept[aa][1] + (1 - yy[w]) * accept[aa][0])
            t += ww[w] * (first + sensor)
        rv.append((a, t))
    return rv[0][0], rv[1][0], rv[0][1], rv[1][1]


def obs_full(p0, p1, buy_by_w, accept_by_w_y):
    """Keep W at second stage; W-specific purchase and terminal accept rule."""
    take = (p0, p1, F(1), F(1))
    rv = []
    for ww, yy in ((WP, YP), (WQ, YQ)):
        a = F(0)
        t = F(0)
        for w in range(4):
            first = take[w]
            sensor = first * buy_by_w[w]
            a += ww[w] * sensor * (yy[w] * accept_by_w_y[2 * w + 1] + (1 - yy[w]) * accept_by_w_y[2 * w])
            t += ww[w] * (first + sensor)
        rv.append((a, t))
    return rv[0][0], rv[1][0], rv[0][1], rv[1][1]


def fmt(x):
    return str(x)


assert sum(WP) == sum(WQ) == 1
for ww, yy in ((WP, YP), (WQ, YQ)):
    assert all(z > 0 for z in ww)
    assert all(0 < y < 1 for y in yy)
    assert len([ww[w] * ((1 - yy[w]) if y == 0 else yy[w]) for w in range(4) for y in (0, 1)]) == 8

# Rescuing EC49L's irrational-only rational target under relaxed terminal acceptance.
target = (F(7, 64), F(13, 64), F(27, 32), F(41, 32))
rescue = (F(1), F(0), F(3, 4), F(1, 4), F(0), F(1), F(1, 2), F(1, 2))
assert obs_compressed(*rescue) == target

# Four compressed information cells (A,Y). Compute their linear acceptance coefficients
# P(cell)-2 Q(cell) before purchase factors q_A, as a function of first-stage p0,p1.
def coefficient(a, y, p0, p1):
    first = (p0, p1, 1, 1)
    Pmass = sum(WP[w] * first[w] * ((1 - YP[w]) if y == 0 else YP[w])
                for w in range(4) if A_BY_W[w] == a)
    Qmass = sum(WQ[w] * first[w] * ((1 - YQ[w]) if y == 0 else YQ[w])
                for w in range(4) if A_BY_W[w] == a)
    return Pmass - 2 * Qmass

coeff_endpoints = {}
for a in (0, 1):
    for y in (0, 1):
        z = [coefficient(a, y, F(p0), F(p1)) for p0, p1 in product((0, 1), repeat=2)]
        assert max(z) <= 0
        coeff_endpoints[f"A{a}_Y{y}"] = [fmt(v) for v in z]

compressed_max = None
compressed_winner = None
compressed_total = 0
for bits in product((F(0), F(1)), repeat=8):
    compressed_total += 1
    o = obs_compressed(*bits)
    val = o[0] - 2 * o[1]
    if compressed_max is None or val > compressed_max:
        compressed_max, compressed_winner = val, tuple(int(x) for x in bits)
assert compressed_total == 256 and compressed_max == 0

full_max = None
full_winner = None
full_total = 0
for bits in product((F(0), F(1)), repeat=14):
    full_total += 1
    o = obs_full(bits[0], bits[1], bits[2:6], bits[6:14])
    val = o[0] - 2 * o[1]
    if full_max is None or val > full_max:
        full_max, full_winner = val, tuple(int(x) for x in bits)
assert full_total == 16384 and full_max == F(7, 16)

# Explicit maximizer: U,V buy sensor and accept only (U,Y=0),(V,Y=1).
witness_full = obs_full(F(1), F(1), (F(1), F(1), F(0), F(0)),
                        (F(1), F(0), F(0), F(1), F(0), F(0), F(0), F(0)))
assert witness_full == (F(9, 16), F(1, 16), F(7, 4), F(5, 4))
assert witness_full[0] - 2 * witness_full[1] == F(7, 16)

# Direct per-W optimal contribution bound: sum_y (P(w,y)-2Q(w,y))_+,
# with U,V optionally stopped and C0,C1 forced but no observation-cost term in L.
per_w = []
for w in range(4):
    gain = sum(max(F(0), WP[w] * (YP[w] if y else 1 - YP[w])
                         - 2 * WQ[w] * (YQ[w] if y else 1 - YQ[w]))
               for y in (0, 1))
    per_w.append(gain)
assert per_w == [F(7, 32), F(7, 32), F(0), F(0)]
assert sum(per_w) == full_max

# The additional single bit D=TEST for U/V, CAL for C0/C1, plus own A,
# uniquely labels the four reachable non-stopped second-stage W histories.
D = ("TEST", "TEST", "CAL", "CAL")
assert len({(A_BY_W[w], D[w]) for w in range(4)}) == 4
assert len({A_BY_W[w] for w in range(4)}) == 2

report = {
    "schema": "EC49M_EXACT_CERTIFICATE_V1",
    "source_atoms_per_measure": 8,
    "all_latent_atoms_strictly_positive": True,
    "ec49l_target": [fmt(x) for x in target],
    "relaxed_terminal_rational_rescue_policy": [fmt(x) for x in rescue],
    "rescue_vector": [fmt(x) for x in obs_compressed(*rescue)],
    "compressed_full_terminal_pure_policies_exhaustively_checked": compressed_total,
    "full_history_full_terminal_pure_policies_exhaustively_checked": full_total,
    "total_deterministic_policies_checked": compressed_total + full_total,
    "compressed_max_alpha_minus_2beta": fmt(compressed_max),
    "compressed_example_maximizer": compressed_winner,
    "full_max_alpha_minus_2beta": fmt(full_max),
    "full_maximizer": full_winner,
    "full_witness": [fmt(x) for x in witness_full],
    "per_W_exact_upper": [fmt(x) for x in per_w],
    "separation_gap": fmt(full_max - compressed_max),
    "compressed_terminal_cell_coefficient_endpoints": coeff_endpoints,
    "one_bit_D_separates_all_reachable_W_after_own_action_A": True,
    "general_real_behavioral_result": "analytic linear-sign certificate and per-W upper bound, not inferred solely from enumeration",
    "rational_full_recall_target_theorem": "rational convex hull of rational pure-policy vectors plus rational Kuhn conversion; mathematical argument in PROOF.md",
    "scope": "finite positive-rational auxiliary BRC, cost T=number of first actions plus sensor purchases, terminal decisions only after purchase",
}
print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
