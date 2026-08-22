"""Dirichlet-transform semantics of the Prime-BRC shadow carry spectrum.

A cross-denominator shadow edge has two strict q-hits

    a*q < M < (a+1)*q,   q>k.

For every d>=1 the scaled modulus d*q has no bulk contribution.  Therefore its
complete carry state is exactly the signed divisor incidence of the adjacent
multipliers:

    kappa_{dq} = 1[d|a] + 1[d|a+1]
    chi_{dq}   = 1[d|a] - 1[d|a+1].

Consequently any divisor transform H(n)=sum_{d|n} h(d) is recovered by
sum/detail over the scaled carry spectrum.  Euler's identity
sum_{d|n} phi(d)=n gives the exact unit-defect conservation

    sum_d phi(d) chi_{dq} = -1.

This is an exact arithmetic/BRC bridge, not a prime-existence theorem.
"""

from __future__ import annotations

from math import gcd

from .legendre import square_carry
from .prime_brc_phase import square_midpoint_defect
from .prime_brc_shadow_staircase import cross_denominator_edge


def divisors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    small = []
    large = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return tuple(small + list(reversed(large)))


def euler_phi(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    value = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            value -= value // p
        p = 3 if p == 2 else p + 2
    if x > 1:
        value -= value // x
    return value


def scaled_shadow_carry_spectrum(k: int, p: int) -> dict[str, object]:
    """Return the complete nonzero d*q spectrum of one shadow edge C_p=1."""
    edge = cross_denominator_edge(k, p)
    if edge["edge"] != 1:
        raise ValueError("p must support a shadow edge")
    q = int(edge["q"])
    a = p
    support_ds = sorted(set(divisors(a)).union(divisors(a + 1)))
    records = []
    for d in support_ds:
        modulus = d * q
        kappa = square_carry(k, modulus)
        chi = square_midpoint_defect(k, modulus)
        expected_kappa = int(a % d == 0) + int((a + 1) % d == 0)
        expected_chi = int(a % d == 0) - int((a + 1) % d == 0)
        if kappa != expected_kappa or chi != expected_chi:
            raise AssertionError("scaled carry != signed adjacent-divisor incidence")
        records.append(
            {
                "d": d,
                "modulus": modulus,
                "kappa": kappa,
                "chi": chi,
                "divides_lower_multiplier": a % d == 0,
                "divides_upper_multiplier": (a + 1) % d == 0,
            }
        )
    return {
        "k": k,
        "p": p,
        "q": q,
        "lower_multiplier": a,
        "upper_multiplier": a + 1,
        "records": tuple(records),
    }


def weighted_shadow_transform(k: int, p: int, weights: dict[int, int]) -> dict[str, int]:
    """Verify the universal finite Dirichlet-transform sum/detail law.

    ``weights`` is an arbitrary finite integer-valued h(d).  Put

        H(n)=sum_{d|n}h(d).

    The routine verifies

        sum h(d) kappa_{dq}=H(a)+H(a+1),
        sum h(d) chi_{dq}=H(a)-H(a+1).
    """
    edge = cross_denominator_edge(k, p)
    if edge["edge"] != 1:
        raise ValueError("p must support a shadow edge")
    q = int(edge["q"])
    a = p
    kappa_sum = 0
    chi_sum = 0
    for d, h in weights.items():
        if d < 1:
            raise ValueError("weight keys must be positive divisors")
        kappa_sum += h * square_carry(k, d * q)
        chi_sum += h * square_midpoint_defect(k, d * q)
    H_a = sum(h for d, h in weights.items() if a % d == 0)
    H_b = sum(h for d, h in weights.items() if (a + 1) % d == 0)
    if kappa_sum != H_a + H_b or chi_sum != H_a - H_b:
        raise AssertionError("weighted shadow transform failed")
    return {
        "kappa_sum": kappa_sum,
        "chi_sum": chi_sum,
        "lower_transform": H_a,
        "upper_transform": H_b,
    }


def totient_unit_defect_conservation(k: int, p: int) -> dict[str, object]:
    """Verify sum phi(d) chi_{dq}=-1 over the finite divisor support."""
    edge = cross_denominator_edge(k, p)
    if edge["edge"] != 1:
        raise ValueError("p must support a shadow edge")
    a = p
    q = int(edge["q"])
    support = sorted(set(divisors(a)).union(divisors(a + 1)))
    chi_total = 0
    kappa_total = 0
    for d in support:
        weight = euler_phi(d)
        chi_total += weight * square_midpoint_defect(k, d * q)
        kappa_total += weight * square_carry(k, d * q)
    if chi_total != -1:
        raise AssertionError("totient-weighted polarity failed unit-defect conservation")
    if kappa_total != 2 * a + 1:
        raise AssertionError("totient-weighted carry amount failed adjacent-sum recovery")
    return {
        "k": k,
        "p": p,
        "q": q,
        "totient_chi_sum": chi_total,
        "totient_kappa_sum": kappa_total,
        "expected_unit_defect": -1,
        "expected_adjacent_sum": 2 * a + 1,
        "status": "EXACT_DIRICHLET_TRANSFORM_CONSERVATION_NOT_PRIME_EXISTENCE",
    }
