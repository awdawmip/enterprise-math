#!/usr/bin/env python3
"""R005-A p=4 finite Legendre/Oppermann transport certificate.

External premise (Sorenson-Webster 2025):
Oppermann's conjecture, hence Legendre's conjecture, was computationally
verified for every integer t <= N = 7.05e13.

R005 transport:
For the fourth-power basin
    k^4 < n < (k+1)^4,
the exact factor-screen horizon is
    F = (k+1)^2 - 1.

For every candidate prime witness q <= F:
1. If q > k^2, then q^2 lies in the fourth-power basin and is an exclusive
   collision for q.
2. If q <= k^2, put x=k^2/sqrt(q) and
       t=max(k+1, floor(x)+1).
   A prime r with t^2 < r < (t+1)^2 satisfies r>F and
       k^4 < q*r < (k+1)^4,
   so q*r is an exclusive collision for q.

The largest t is attained at the smallest candidate prime q=2:
    t_max(k) = floor(k^2/sqrt(2)) + 1
             = floor(sqrt(k^4/2)) + 1.

Thus a finite verified Legendre range t<=N forces the ENTIRE candidate witness
universe in every fourth-power basin with t_max(k)<=N.
"""

from __future__ import annotations

from math import isqrt
import json

LEGENDRE_VERIFIED_N = 70_500_000_000_000


def t_max(k: int) -> int:
    return isqrt((k**4) // 2) + 1


def largest_k_for_verified_t(N: int) -> int:
    lo, hi = 1, 20_000_000
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if t_max(mid) <= N:
            lo = mid
        else:
            hi = mid - 1
    return lo


def witness_upper_inequality_margin(k: int, q: int, t: int) -> int:
    """Integer proxy for sqrt(q)*(t+1) < (k+1)^2."""
    return (k + 1) ** 4 - q * (t + 1) ** 2


def main() -> None:
    K = largest_k_for_verified_t(LEGENDRE_VERIFIED_N)
    assert K == 9_985_091
    assert t_max(K) <= LEGENDRE_VERIFIED_N
    assert t_max(K + 1) > LEGENDRE_VERIFIED_N

    examples = []

    k = 10
    q = 101
    F = (k + 1) ** 2 - 1
    assert k * k < q <= F
    n = q * q
    assert k**4 < n < (k + 1) ** 4
    examples.append({"k": k, "q": q, "type": "q^2", "n": n})

    k = 10
    q = 2
    t = t_max(k)
    r = 5051
    assert t == 71
    assert t * t < r < (t + 1) * (t + 1)
    assert r > (k + 1) ** 2 - 1
    n = q * r
    assert k**4 < n < (k + 1) ** 4
    examples.append({"k": k, "q": q, "type": "q*r", "t": t, "r": r, "n": n})

    result = {
        "status": (
            "R005-A P4 FINITE LEGENDRE TRANSPORT / "
            "ARITHMETIC CONSEQUENCE VERIFIED / EXTERNAL COMPUTATION PREMISE"
        ),
        "external_premise": {
            "verified_t_max": LEGENDRE_VERIFIED_N,
            "property": (
                "a prime exists between t^2 and (t+1)^2 for every "
                "positive integer t through the verified bound"
            ),
            "stronger_source_property": (
                "the cited computation verifies Oppermann, hence Legendre"
            ),
        },
        "transport": {
            "formula": "t_max(k)=floor(k^2/sqrt(2))+1",
            "largest_k": K,
            "t_max_at_largest_k": t_max(K),
            "t_max_at_next_k": t_max(K + 1),
            "conclusion": (
                "Every candidate divisor witness in every p=4 basin "
                f"2<=k<={K} is forced; therefore the unique least safe "
                "basis is the entire candidate prime set up to F=(k+1)^2-1."
            ),
        },
        "sanity_examples": examples,
        "boundary": (
            "k=9985092 is not a counterexample; it is only the first k whose "
            "worst-case transported square index exceeds the external verified "
            "Legendre/Oppermann range."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
