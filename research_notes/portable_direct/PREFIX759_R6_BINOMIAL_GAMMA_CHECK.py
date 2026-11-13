#!/usr/bin/env python3
"""Exact rational check for PREFIX-759. Python standard library only."""
from fractions import Fraction
from math import comb, factorial
import json

def beta_half_tail(m):
    assert m >= 1
    n = m + 49
    return Fraction(sum(comb(n, k) for k in range(25, n + 1)), 2**n)

def improved_uniform_coefficient(m):
    return Fraction(m * factorial(m + 24), factorial(25) * 2**24) * beta_half_tail(m)

def preceding_758_coefficient(m):
    return Fraction(m * factorial(m + 49), factorial(25)**2 * 2**(m + 74))

def integral_expansion_coefficient(m):
    # F_Gamma25(t)=1-exp(-t)*sum(t^j/j!, j=0..24)
    integral = Fraction(factorial(m + 24)) - sum(
        (Fraction(factorial(m + 24 + j), factorial(j) * 2**(m + 25 + j))
         for j in range(25)), Fraction(0))
    return Fraction(m, factorial(25) * 2**24) * integral

D = Fraction(4**25 - 1 - 3**25, 4**25)
assert D > 0
rows = []
for m in (1, 2, 3, 4, 5, 10):
    beta = beta_half_tail(m)
    old = preceding_758_coefficient(m)
    new = improved_uniform_coefficient(m)
    assert new == integral_expansion_coefficient(m)
    assert new > old
    rows.append({"moment_order": m, "binomial_tail": str(beta),
                 "old_uniform_coefficient": str(old),
                 "new_uniform_coefficient": str(new),
                 "improvement_ratio": str(new / old)})
assert improved_uniform_coefficient(1) == Fraction(156538814160047, 4722366482869645213696)
assert improved_uniform_coefficient(2) == Fraction(4465042313279197, 2361183241434822606848)
assert D == Fraction(281263154558295, 281474976710656)
output = {"status": "ALL_CHECKS_PASS",
          "scientific_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
          "method": "exact rational binomial tail versus finite Erlang CDF integral",
          "sample_D_at_p1_0_p2_1_over_4": str(D),
          "sample_improved_mean_lower_bound": str(D * improved_uniform_coefficient(1)),
          "rows": rows}
print(json.dumps(output, ensure_ascii=False, indent=2))
