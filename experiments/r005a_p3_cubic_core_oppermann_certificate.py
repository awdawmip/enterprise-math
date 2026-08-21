#!/usr/bin/env python3
"""R005-A cubic core reduction + finite Oppermann transport certificate.

External premise (Sorenson-Webster 2025):
Oppermann's conjecture was computationally verified for every integer
t <= 7.05e13.

R005 p=3 structure:
For the cubic basin A=k^3 < n < (k+1)^3, let F=floor(sqrt(U)), U=(k+1)^3-1.
Generic R005 facts already established:
- every residual composite has at least two distinct non-forced candidate prime divisors;
- every non-forced candidate witness q satisfies q<=sqrt(A)=k^(3/2).

Cubic core theorem: if every prime candidate q<=k is forced, then there is no residual composite.

Oppermann transport: for q<=k set y=sqrt(k^3/q) and t=ceil(y). The first-half Oppermann prime t^2 < r < t(t+1) gives an exclusive collision q*r.
The worst t occurs at q=2: t_max(k)=ceil(sqrt(k^3/2)).
"""

from __future__ import annotations
from math import isqrt
import json

OPPERMANN_VERIFIED_N = 70_500_000_000_000


def ceil_sqrt_half_cube(k: int) -> int:
    m = k**3
    t = isqrt(m // 2)
    while 2 * t * t < m:
        t += 1
    while t > 0 and 2 * (t - 1) * (t - 1) >= m:
        t -= 1
    return t


def largest_k_for_verified_t(N: int) -> int:
    lo, hi = 1, 5_000_000_000
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ceil_sqrt_half_cube(mid) <= N:
            lo = mid
        else:
            hi = mid - 1
    return lo


def cubic_horizon(k: int) -> int:
    return isqrt((k + 1) ** 3 - 1)


def main() -> None:
    K = largest_k_for_verified_t(OPPERMANN_VERIFIED_N)
    assert K == 2_150_153_225
    assert ceil_sqrt_half_cube(K) <= OPPERMANN_VERIFIED_N
    assert ceil_sqrt_half_cube(K + 1) > OPPERMANN_VERIFIED_N

    k = 10
    q = 2
    t = 23
    r = 541
    A = k**3
    U = (k + 1) ** 3 - 1
    F = cubic_horizon(k)
    assert t * t < r < t * (t + 1)
    assert r > F
    assert A < q * r <= U

    for k0 in (3, 4, 10, 100):
        assert k0 * k0 > cubic_horizon(k0)

    result = {
        "status": "R005-A CUBIC CORE + FINITE OPPERMANN TRANSPORT / ARITHMETIC CONSEQUENCE VERIFIED / EXTERNAL COMPUTATION PREMISE",
        "cubic_core_theorem": {
            "sufficient_for_unique_least_basis": "every candidate prime witness q<=k is forced",
            "reason": "a residual needs two distinct non-forced q1,q2>k; T-A14 gives q1*q2<=k^3, so a further factor is required, but every factor of a residual is >k, forcing n>=(k+1)^3 outside the basin",
        },
        "oppermann_transport": {
            "verified_t_max": OPPERMANN_VERIFIED_N,
            "worst_index_formula": "t_max(k)=ceil(sqrt(k^3/2))",
            "largest_certified_k": K,
            "t_max_at_largest_k": ceil_sqrt_half_cube(K),
            "t_max_at_next_k": ceil_sqrt_half_cube(K + 1),
            "conclusion": f"Under the published finite Oppermann verification, every cubic basin 2<=k<={K} has a unique least safe divisor-witness basis.",
        },
        "sanity_example": {"k": 10, "q": 2, "t": 23, "r": 541, "exclusive_collision": q * r},
        "boundary": f"k={K+1} is not a counterexample; it is only the first k whose worst-case Oppermann index exceeds the external verified range.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
