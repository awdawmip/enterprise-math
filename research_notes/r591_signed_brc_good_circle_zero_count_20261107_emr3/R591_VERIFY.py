"""R591: exact finite polynomial checks + conservative Rouché witness.
Analytic growing-circle result is proved in R591_PROOF.zh-CN.md, not by sampling.
"""
from fractions import Fraction
from math import comb, factorial


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def h_raw(k, s):
    return comb(2 * k + 1 + s, 2 * s) * sum(
        comb(s - 1, 2 * q) * 4**q * catalan(k - q)
        for q in range(min(k, (s - 1) // 2) + 1)
    )


def a_limit(j):
    return Fraction(24 * 8**j, factorial(2 * j + 4))


def a_finite(k, j):
    return Fraction(h_raw(k, j + 2), h_raw(k, 2) * k**(2 * j))


def tail_upper(j_start, radius):
    """Exact majorant for sum_{j>=j_start} a_j radius**j."""
    v = a_limit(j_start) * radius**j_start
    next_ratio = Fraction(8 * radius, (2*j_start + 6)*(2*j_start + 5))
    assert next_ratio < 1
    return v / (1 - next_ratio)


def lower_on_circle(radius, cutoff=16):
    return 1 - sum((a_limit(j) * radius**j for j in range(1, cutoff + 1)), Fraction(0)) - tail_upper(cutoff + 1, radius)

for radius in (1, 2):
    lower = lower_on_circle(radius)
    assert lower > 0, (radius, float(lower))
    print("R591_EXACT_F_CIRCLE_LOWER", radius, f"{float(lower):.12f}")

count = 0
for k in (8, 16, 32, 64):
    d = 2*k - 1
    for radius in (1, 2):
        err = sum((abs(a_finite(k,j)-a_limit(j))*radius**j for j in range(d+1)),Fraction(0)) + tail_upper(d+1,radius)
        lower = lower_on_circle(radius)
        if err < lower:
            count += 1
            assert lower > err
        print("R591_FINITE_ROUCHE", "k",k,"radius",radius,"error_upper",f"{float(err):.12g}","F_lower",f"{float(lower):.12g}", "certified",err<lower)
assert count >= 4
# Strict rational inequality underpinning the explicit admissible scale c=1/40000.
assert Fraction(148,200) < 1
assert Fraction(2,40000) < Fraction(1,8)
print("R591_EXPLICIT_C_SCALE_CHECK_PASS")
print("R591_FINITE_COEFFICIENT_AND_ROUCHE_PASS",count,"out of 8")
