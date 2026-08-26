"""Deterministic nearest-remainder bound for two-prime Walsh conductors.

Let m=p*q be a product of two distinct odd primes transverse to the pronic
center.  At any fixed root phase the signed root cube has exactly four roots:

* two pure roots +/-C with coefficient +1;
* two mixed roots +/-rho with coefficient -1.

For a centered tent of radius R<m/2, write

    w_R(d)=max(0,1-d/R)

for the tent value at least absolute residue distance d from zero.  Evenness of
the tent gives the exact shape

    T_m(R)=2[w_R(d_pure)-w_R(d_mixed)],

so

    |T_m(R)|<=2.

Now apply the nearest-remainder descent to the parent square scale k.  If

    delta=min(k mod m, m-(k mod m)),

then

    B_m(k)=(delta/k) T_m(delta)

with the appropriate forward/backward pronic root center.  Therefore

    |B_m(k)| <= 2*delta/k.

For a conductor in the actual reusable symmetric core m<=C=floor((k-1)/2),
nearest-remainder gives delta<m/2, hence

    |B_m(k)| < m/k <= C/k < 1/2.

This is a phase-independent pointwise bound for every two-prime reusable Walsh
column.  It does not sum the pair-conductor family and does not prove Legendre's
conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff
from .p017_p018_walsh_tent_complement_descent import (
    generalized_selected_tent,
    nearest_remainder_selected_descent,
)


def _two_odd_prime_factors(modulus: int) -> tuple[int, int]:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 1 or modulus % 2 == 0:
        raise ValueError("modulus must be an odd integer >1")
    factors: list[int] = []
    remaining = modulus
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            factors.append(p)
            if remaining % p == 0:
                raise ValueError("modulus must be squarefree")
        p += 2
    if remaining > 1:
        factors.append(remaining)
    if len(factors) != 2 or factors[0] * factors[1] != modulus:
        raise ValueError("modulus must be the product of exactly two distinct odd primes")
    return factors[0], factors[1]


def least_absolute_residue(value: int, modulus: int) -> int:
    residue = value % modulus
    return min(residue, modulus - residue)


def pair_child_tent_formula(center: int, radius: int, modulus: int) -> dict[str, object]:
    """Verify T=2(w_pure-w_mixed) for one pair conductor at R<m/2."""
    p, q = _two_odd_prime_factors(modulus)
    if not (2 * radius < modulus):
        raise ValueError("pair child formula requires R<m/2")
    if gcd(center, modulus) != 1:
        raise ValueError("center must be transverse to the pair conductor")

    # Mixed root: +center mod p, -center mod q.
    inv_p_q = pow(p, -1, q)
    mixed = (center + p * (((-2 * center) * inv_p_q) % q)) % modulus
    if mixed % p != center % p or mixed % q != (-center) % q:
        raise AssertionError("mixed pair root CRT reconstruction failed")

    d_pure = least_absolute_residue(center, modulus)
    d_mixed = least_absolute_residue(mixed, modulus)

    def w(distance: int) -> Fraction:
        return Fraction(radius - distance, radius) if distance < radius else Fraction(0, 1)

    predicted = 2 * (w(d_pure) - w(d_mixed))
    direct = generalized_selected_tent(center, radius, modulus)
    if direct != predicted:
        raise AssertionError("two-prime selected tent did not equal pure-minus-mixed pair formula")
    if abs(direct) > 2:
        raise AssertionError("two-prime child tent exceeded absolute ceiling two")
    return {
        "center": center,
        "radius": radius,
        "modulus_m": modulus,
        "prime_factors": (p, q),
        "pure_root_distance": d_pure,
        "mixed_root_distance": d_mixed,
        "pure_tent_weight": w(d_pure),
        "mixed_tent_weight": w(d_mixed),
        "direct_child_tent": direct,
        "pure_minus_mixed_formula": predicted,
        "absolute_child_ceiling_two": True,
    }


def pair_conductor_nearest_bound(k: int, modulus: int) -> dict[str, object]:
    """Return |B_m(k)|<=2 delta/k and the reusable-core <1/2 corollary."""
    _two_odd_prime_factors(modulus)
    data = nearest_remainder_selected_descent(k, modulus)
    delta = int(data["nearest_remainder_delta"])
    center = int(data["child_center"])
    if delta == 0:
        raise AssertionError("transverse pair conductor has zero nearest remainder")
    child = pair_child_tent_formula(center, delta, modulus)
    parent = data["parent_selected_tent"]
    ceiling = Fraction(2 * delta, k)
    if abs(parent) > ceiling:
        raise AssertionError("two-prime parent Walsh column exceeded nearest-remainder ceiling")

    C = reusable_floor_product_cutoff(k)
    reusable = modulus <= C
    reusable_ceiling = None
    if reusable:
        reusable_ceiling = Fraction(modulus, k)
        if ceiling > reusable_ceiling:
            raise AssertionError("nearest-remainder pair ceiling exceeded m/k")
        if reusable_ceiling >= Fraction(1, 2):
            raise AssertionError("reusable pair conductor failed strict half-unit ceiling")

    return {
        **data,
        "pair_child": child,
        "absolute_parent_ceiling_2delta_over_k": ceiling,
        "reusable_symmetric_core": reusable,
        "reusable_pair_ceiling_m_over_k": reusable_ceiling,
        "reusable_pair_strictly_below_half": (not reusable) or reusable_ceiling < Fraction(1, 2),
    }
