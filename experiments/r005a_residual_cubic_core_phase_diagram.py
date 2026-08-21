#!/usr/bin/env python3
"""R005-A residual cubic core and collapse-dimension prime-gap phase diagram.

For a p-power basin A=k^p, U=(k+1)^p-1, a generic residual composite requires two distinct non-forced candidate prime divisors q1,q2 with q1*q2<=A and at least one further prime factor. Therefore forcing all candidate primes q<=floor(cuberoot(U)) is sufficient for a unique least safe witness basis.

Asymptotically:
- least-basis core q ~ k^(p/3), cofactor x ~ k^(2p/3), interval length ~ x/k = x^(1 - 3/(2p));
- full forcing q ~ k^(p/2), cofactor x ~ k^(p/2), interval length ~ x/k = x^(1 - 2/p).

Compare with Baker-Harman-Pintz theta=0.525=21/40.
"""

from __future__ import annotations
from fractions import Fraction
from math import isqrt
import json

BHP_THETA = Fraction(21, 40)


def integer_cuberoot(n: int) -> int:
    lo, hi = 0, 1
    while hi**3 <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def least_exponent(p: int) -> Fraction:
    return Fraction(1, 1) - Fraction(3, 2 * p)


def full_exponent(p: int) -> Fraction:
    return Fraction(1, 1) - Fraction(2, p)


def main() -> None:
    rows = []
    for p in range(2, 11):
        least = least_exponent(p)
        full = full_exponent(p)
        rows.append({
            "p": p,
            "least_basis_short_interval_exponent": f"{least.numerator}/{least.denominator}",
            "least_decimal": float(least),
            "bhp_suffices_for_least_asymptotically": least > BHP_THETA,
            "full_forcing_short_interval_exponent": f"{full.numerator}/{full.denominator}",
            "full_decimal": float(full),
            "bhp_suffices_for_full_asymptotically": full > BHP_THETA,
        })

    assert [r["p"] for r in rows if r["bhp_suffices_for_least_asymptotically"]] == list(range(4, 11))
    assert [r["p"] for r in rows if r["bhp_suffices_for_full_asymptotically"]] == list(range(5, 11))

    for k in range(2, 101):
        U = (k + 1)**3 - 1
        assert integer_cuberoot(U) == k

    for p in range(2, 9):
        for k in range(2, 50):
            U = (k + 1)**p - 1
            assert integer_cuberoot(U) <= isqrt(U)

    result = {
        "status": "R005-A RESIDUAL CUBIC CORE PHASE DIAGRAM / EXACT EXPONENT ALGEBRA",
        "generic_core": "C(U)=floor(U^(1/3))",
        "bhp_theta": "21/40",
        "rows": rows,
        "thresholds": {
            "BHP_implies_asymptotic_unique_least_basis_for_fixed_p": "p>=4",
            "BHP_implies_asymptotic_full_forcing_for_fixed_p": "p>=5",
            "critical_p3_least_exponent": "1/2",
            "p4_least_exponent": "5/8",
            "p4_full_exponent": "1/2",
            "p2_least_exponent": "1/4",
        },
        "cubic_identity": "floor((((k+1)^3-1)^(1/3)))=k for every k>=0",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
