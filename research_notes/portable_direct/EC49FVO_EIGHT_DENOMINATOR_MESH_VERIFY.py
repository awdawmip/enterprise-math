#!/usr/bin/env python3
"""EC49FVO: exact p=11 eight-denominator certificate; frozen BRC16943.

Reproduce with: python EC49FVO_EIGHT_DENOMINATOR_MESH_VERIFY.py
No floating point, randomness, nonstandard dependency or native X6 experiment.
"""
from fractions import Fraction
from math import gcd, lcm

P = 11
U = Fraction(4822040484, 8132285009)
GAMMA = Fraction(141024, 1653649)
MODULUS = 160160
CHART_FACTOR = 91


def fmod(q):
    return (q.numerator * pow(q.denominator, -1, P)) % P


u = fmod(U)
g = fmod(GAMMA)
i637 = pow(637, -1, P)
rows = []
for z in range(P):
    la = ((637 - 3 * z) * i637) % P
    lb = (u * (1 + g * z)) % P
    a = (1 - (1 - z) * la) % P
    b = (1 - (1 - z) * lb) % P
    rows.append((z, a, b, la, lb))
assert [row for row in rows if row[3] == row[4]] == [
    (3, 10, 10, 10, 10)
]
c, d = (-3 * i637) % P, (u * g) % P


def no_projective_root(h, n):
    """All eleven affine F_11 points and the homogeneous infinity point."""
    assert h > 0 and n > 0
    for z, a, b, la, lb in rows:
        if z == 3:
            q = (pow(la, n - 1, P) * pow(a, h - 1, P)
                 * (n * a - h * (1 - z) * la)) % P
        else:
            q = ((pow(a, h, P) * pow(la, n, P)
                  - pow(b, h, P) * pow(lb, n, P))
                 * pow((la - lb) % P, -1, P)) % P
        if q == 0:
            return False
    return ((pow(c, h + n, P) - pow(d, h + n, P))
            * pow((c - d) % P, -1, P)) % P != 0


# The nonsingular mod-p points depend only on h,n modulo 10,
# with the singular point imposing an additional mod-11 linear condition.
patterns = set()
for h0 in range(1, 11):
    for n0 in range(1, 11):
        if all(
            ((pow(a, h0, P) * pow(la, n0, P)
              - pow(b, h0, P) * pow(lb, n0, P))
             * pow((la - lb) % P, -1, P)) % P != 0
            for z, a, b, la, lb in rows if z != 3
        ) and ((pow(c, h0 + n0, P) - pow(d, h0 + n0, P))
               * pow((c - d) % P, -1, P)) % P != 0:
            patterns.add((h0 % 10, n0 % 10))
assert len(patterns) == 44


def certified(h, n):
    return ((h % 10, n % 10) in patterns
            and (9 * h + 10 * n) % 11 != 0)


for h in range(1, 111):
    for n in range(1, 111):
        assert certified(h, n) == no_projective_root(h, n)
print("projective_mask: 44/100 nonsingular exponent residues; 12100/12100 full comparisons PASS")

# Denominator d_j = r * 2^(j-e); coordinate y = 91 * 2^j * (h/d_j)
# = scale*h.  Every d_j <= k=2^j for j>=7.
SPECS = (
    ("k", 1, 0),
    ("7k/8", 7, 3),
    ("13k/16", 13, 4),
    ("k/2", 1, 1),
    ("k/4", 1, 2),
    ("k/8", 1, 3),
    ("k/16", 1, 4),
    ("7k/16", 7, 4),
)


def scale(r, e):
    assert (CHART_FACTOR * 2**e) % r == 0
    return CHART_FACTOR * 2**e // r


for name, r, e in SPECS:
    assert MODULUS % (scale(r, e) * lcm(110, r)) == 0, name


def period_points(j, spec):
    """Complete finite integer-coordinate residue mask in [0,160160)."""
    _name, r, e = spec
    assert j >= e + 1
    step = scale(r, e)
    d_mod = r * pow(2, j - e, 110) % 110
    return {
        step * h for h in range(1, MODULUS // step)
        if gcd(h, 2*r) == 1 and certified(h, d_mod - h)
    }


def direct_points(j, indices):
    k = 2**j
    points = {0, CHART_FACTOR * k}
    for ix in indices:
        _name, r, e = SPECS[ix]
        denom = r * 2**(j - e)
        step = scale(r, e)
        points.update(
            step * h for h in range(1, denom)
            if gcd(h, denom) == 1 and certified(h, denom - h)
        )
    return sorted(points)


def cyclic_gap(points):
    return max(
        [v - u for u, v in zip(points, points[1:])]
        + [points[0] + MODULUS - points[-1]]
    )


def osc(points):
    rho = Fraction(len(points), MODULUS)
    extrema = [Fraction(0)]
    for i, y in enumerate(points):
        extrema.extend((i - rho*y, i + 1 - rho*y))
    return max(extrema) - min(extrema)


period_stats = []
leave_one_out_gaps = [0] * 5
for j in range(11, 31):
    layers = [period_points(j, spec) for spec in SPECS]
    points = sorted(set().union(*layers))
    assert len(points) == 1220
    assert len(set().union(*layers[:3])) == 800
    gap = cyclic_gap(points)
    disc = osc(points)
    assert gap == 455
    assert disc == (Fraction(684, 77) if j % 2 else Fraction(1088, 143))
    period_stats.append((j, len(points), gap, disc))
    for cut in range(3, 8):
        leave = sorted(set().union(*(layers[i] for i in range(8) if i != cut)))
        leave_one_out_gaps[cut - 3] = max(leave_one_out_gaps[cut - 3], cyclic_gap(leave))
print("20/20 periodic states PASS: 1220 points/160160, cyclic gap=455")
print("periodic local discrepancy oscillation: odd=684/77; even=1088/143")
assert leave_one_out_gaps == [600, 546, 696, 630, 637]
print("leave-one-out max gaps (k/2,k/4,k/8,k/16,7k/16):", leave_one_out_gaps)

for j in range(7, 14):
    y = direct_points(j, range(8))
    max_gap = max(v-u for u, v in zip(y, y[1:]))
    assert max_gap == {7:364, 8:390, 9:416, 10:455, 11:455, 12:455, 13:455}[j]
    # Independently compare the direct fractions to the corresponding clipped periodic mask.
    residue = sorted(v for v in set().union(*(period_points(j, spec) for spec in SPECS))
                     if 0 < v < 91 * 2**j)
    # For larger j a single mask period repeats, so use it only in the first period.
    if 91 * 2**j <= MODULUS:
        assert y[1:-1] == residue
    print("direct", j, "k=", 2**j, "certified_count=", len(y)-2,
          "max_integer_chart_gap=", max_gap)
assert Fraction(1220, MODULUS) * CHART_FACTOR == Fraction(61, 88)
assert Fraction(2*455, 91) == 10
print("ALL PASS: 8 denominators; |I|>10/H covers for H>=128; density 61k/88; |E|<=684/77")
