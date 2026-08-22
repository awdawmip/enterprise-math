"""Prime-BRC q-block Dirichlet-transform tomography and local parity annihilation.

For q coprime to M=k(k+1), let A_q and B_q be the integer multiplier blocks
whose q-multiples lie strictly below/above M inside the consecutive-square
basin.  For every arithmetic weight h of finite support, with divisor transform

    H(n)=sum_{d|n} h(d),

the scaled midpoint-polarity spectrum satisfies

    sum_d h(d) chi_{dq}
      = sum_{a in A_q} H(a) - sum_{b in B_q} H(b).

This is finite double-counting: a d*q hit is exactly a q-hit whose multiplier is
divisible by d.

Two important specializations:

* h=phi: H(n)=n, recovering signed first moments and the -1 unit defect on a
  two-hit adjacent-multiplier shadow edge;
* h=mu: H(n)=1[n=1].  When every multiplier in the block is >1, the complete
  Mobius-weighted polarity sum vanishes identically.  This is an exact local
  Prime-BRC expression of the classical sieve parity obstruction, not an
  estimate.
"""

from __future__ import annotations

from math import gcd, isqrt

from .prime_brc_phase import square_basin_frame, square_midpoint_defect
from .prime_brc_shadow_transform import divisors, euler_phi


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    x = n
    parity = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def multiplier_blocks(k: int, q: int) -> dict[str, object]:
    """Return strict lower/upper multiplier blocks for q-multiples."""
    if k < 2 or q < 2:
        raise ValueError("require k>=2 and q>=2")
    frame = square_basin_frame(k)
    L = int(frame["lower"])
    M = int(frame["center"])
    U = int(frame["upper"])
    if gcd(q, M) != 1:
        raise ValueError("q-block transform requires q coprime to M")
    lower = tuple(range(L // q + 1, M // q + 1))
    upper = tuple(range(M // q + 1, (U - 1) // q + 1))
    for a in lower:
        if not L < a * q < M:
            raise AssertionError("lower multiplier block escaped its strict half")
    for b in upper:
        if not M < b * q < U:
            raise AssertionError("upper multiplier block escaped its strict half")
    return {
        "k": k,
        "q": q,
        "lower_multipliers": lower,
        "upper_multipliers": upper,
    }


def weighted_block_transform(k: int, q: int, weights: dict[int, int]) -> dict[str, int]:
    """Verify the universal finite q-block transform identity."""
    blocks = multiplier_blocks(k, q)
    lower = tuple(int(x) for x in blocks["lower_multipliers"])
    upper = tuple(int(x) for x in blocks["upper_multipliers"])
    lhs = 0
    for d, h in weights.items():
        if d < 1:
            raise ValueError("weight keys must be positive")
        lhs += h * square_midpoint_defect(k, d * q)

    def H(n: int) -> int:
        return sum(h for d, h in weights.items() if n % d == 0)

    lower_transform = sum(H(a) for a in lower)
    upper_transform = sum(H(b) for b in upper)
    rhs = lower_transform - upper_transform
    if lhs != rhs:
        raise AssertionError("q-block Dirichlet-transform identity failed")
    return {
        "lhs": lhs,
        "rhs": rhs,
        "lower_transform": lower_transform,
        "upper_transform": upper_transform,
    }


def totient_first_moment(k: int, q: int) -> dict[str, int]:
    """Recover exact signed/summed multiplier first moments from scaled carry."""
    blocks = multiplier_blocks(k, q)
    lower = tuple(int(x) for x in blocks["lower_multipliers"])
    upper = tuple(int(x) for x in blocks["upper_multipliers"])
    max_multiplier = max((*lower, *upper), default=0)
    weights = {d: euler_phi(d) for d in range(1, max_multiplier + 1)}
    result = weighted_block_transform(k, q, weights)
    expected_signed = sum(lower) - sum(upper)
    expected_total = sum(lower) + sum(upper)
    if result["lhs"] != expected_signed:
        raise AssertionError("totient polarity failed multiplier first moment")
    return {
        "signed_first_moment": expected_signed,
        "total_first_moment": expected_total,
        "lower_first_moment": sum(lower),
        "upper_first_moment": sum(upper),
    }


def mobius_polarity_annihilation(k: int, q: int) -> dict[str, object]:
    """Verify exact local parity annihilation when all q-block multipliers >1.

    Since sum_{d|n}mu(d)=0 for every n>1, the complete scaled polarity sum

        sum_d mu(d) chi_{dq}

    is identically zero whenever neither multiplier block contains 1.
    """
    blocks = multiplier_blocks(k, q)
    lower = tuple(int(x) for x in blocks["lower_multipliers"])
    upper = tuple(int(x) for x in blocks["upper_multipliers"])
    values = lower + upper
    if not values or min(values) <= 1:
        raise ValueError("annihilation interface requires nonempty multiplier blocks all >1")
    max_multiplier = max(values)
    weights = {d: mobius(d) for d in range(1, max_multiplier + 1)}
    result = weighted_block_transform(k, q, weights)
    if result["lhs"] != 0:
        raise AssertionError("Mobius-weighted q-block polarity did not annihilate")
    return {
        "k": k,
        "q": q,
        "mobius_polarity_sum": 0,
        "lower_multipliers": lower,
        "upper_multipliers": upper,
        "status": "EXACT_LOCAL_PARITY_ANNIHILATION",
    }
