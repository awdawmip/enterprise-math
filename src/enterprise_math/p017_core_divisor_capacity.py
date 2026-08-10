"""Signed composite-divisor packing for P017 full-core incidences.

Write M=k(k+1).  Encode a lower mirror incidence by signed point x=+r and an
upper incidence by x=-r, so every core divisor D attached to the incidence
satisfies

    D | M-x.

Assume D is positive, odd, and transverse to M.  Anchor-surviving radii are odd,
so every signed point is odd.  The two conditions

    x = M (mod D),
    x = 1 (mod 2)

combine into one *fixed* residue class modulo 2D.  Intersecting that class with

    -(k-1) <= x <= k-1

therefore gives the exact raw aligned capacity for D; filtering those finitely
many points by gcd(|x|,M)=1 gives the exact anchor-surviving aligned capacity.
Any selected valid signed-incidence family is a subset of this anchor list.

The older universal estimate

    m_D <= floor((k-1)/D)+1

remains a convenient alignment-free corollary.  The exact aligned/anchor count
can be strictly smaller and is the preferred finite capacity when k and D are
known.  In particular D>k-1 still has total reuse capacity at most one across
*both* mirror orientations.

This simultaneously:

* extends CG11's prime-power packing bound to arbitrary odd transverse divisors;
* sharpens the cross-orientation part of CG04 by using mandatory odd parity;
* supplies exact aligned and anchor-filtered column capacities for multi-prime
  products consumed by the P017/P018 terminal-capacity bridge.

The congruence argument is elementary CRT/parity arithmetic.  This module is a
P017 owner-local discovery result and reserves no canonical L-number.
"""

from __future__ import annotations

from math import gcd


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")


def _require_divisor(k: int, divisor: int) -> None:
    _require_k(k)
    if (
        isinstance(divisor, bool)
        or not isinstance(divisor, int)
        or divisor <= 0
        or divisor % 2 == 0
    ):
        raise ValueError("divisor must be a positive odd integer")
    if gcd(divisor, k * (k + 1)) != 1:
        raise ValueError("divisor must be transverse to M=k(k+1)")


def signed_divisor_residue(k: int, divisor: int) -> dict[str, int]:
    """Return the unique odd signed-point residue modulo 2D."""
    _require_divisor(k, divisor)
    center = k * (k + 1)
    residue_mod_d = center % divisor
    residue = residue_mod_d if residue_mod_d % 2 == 1 else residue_mod_d + divisor
    modulus = 2 * divisor
    if not 0 <= residue < modulus or residue % 2 != 1 or (center - residue) % divisor:
        raise AssertionError("signed divisor residue failed CRT/parity normalization")
    return {
        "k": k,
        "divisor": divisor,
        "center": center,
        "residue": residue,
        "modulus": modulus,
    }


def raw_signed_divisor_points(k: int, divisor: int) -> tuple[int, ...]:
    """Enumerate every signed odd point in the divisor residue class."""
    data = signed_divisor_residue(k, divisor)
    residue = int(data["residue"])
    modulus = int(data["modulus"])
    radius_limit = k - 1

    start = residue
    while start - modulus >= -radius_limit:
        start -= modulus
    while start < -radius_limit:
        start += modulus

    points: list[int] = []
    point = start
    while point <= radius_limit:
        if point != 0:
            points.append(point)
        point += modulus
    for point in points:
        if point % 2 != 1 or (int(data["center"]) - point) % divisor:
            raise AssertionError("raw signed point escaped its parity/divisor class")
    return tuple(points)


def signed_divisor_capacity(k: int, divisor: int) -> dict[str, object]:
    """Return exact aligned capacities and the alignment-free universal bound."""
    _require_divisor(k, divisor)
    center = k * (k + 1)
    raw = raw_signed_divisor_points(k, divisor)
    anchor = tuple(point for point in raw if gcd(abs(point), center) == 1)
    universal = (k - 1) // divisor + 1

    if len(raw) > universal:
        raise AssertionError("signed divisor progression exceeded floor((k-1)/D)+1")
    if len(anchor) > len(raw):
        raise AssertionError("anchor filtering increased signed divisor incidence")
    if divisor > k - 1 and len(anchor) > 1:
        raise AssertionError("D>k-1 was reused across signed mirror orientations")

    return {
        "k": k,
        "divisor": divisor,
        "signed_residue": signed_divisor_residue(k, divisor)["residue"],
        "signed_modulus": 2 * divisor,
        "raw_signed_points": raw,
        "anchor_signed_points": anchor,
        "raw_count": len(raw),
        "anchor_count": len(anchor),
        "exact_aligned_capacity": len(raw),
        "exact_anchor_capacity": len(anchor),
        "universal_capacity": universal,
        "globally_single_use": divisor > k - 1,
    }


def selected_signed_divisor_incidence_capacity(
    k: int,
    divisor: int,
    signed_points: tuple[int, ...],
) -> dict[str, object]:
    """Certify a selected incidence family against exact and universal capacities."""
    _require_divisor(k, divisor)
    if len(set(signed_points)) != len(signed_points):
        raise ValueError("signed points must be distinct")
    center = k * (k + 1)
    limit = k - 1
    for point in signed_points:
        if isinstance(point, bool) or not isinstance(point, int) or point == 0 or abs(point) > limit:
            raise ValueError("signed points must be nonzero integers in the P017 signed interval")
        if point % 2 != 1:
            raise ValueError("anchor-surviving signed points must be odd")
        if gcd(abs(point), center) != 1:
            raise ValueError("signed point must survive the anchor sieve")
        if (center - point) % divisor:
            raise ValueError("divisor must divide M-x at every selected incidence")

    capacity = signed_divisor_capacity(k, divisor)
    anchor_points = tuple(int(point) for point in capacity["anchor_signed_points"])
    if any(point not in anchor_points for point in signed_points):
        raise AssertionError("selected valid incidence escaped the exact anchor residue list")
    if len(signed_points) > int(capacity["exact_anchor_capacity"]):
        raise AssertionError("selected incidences exceeded exact anchor capacity")

    return {
        "k": k,
        "divisor": divisor,
        "selected_signed_points": signed_points,
        "selected_count": len(signed_points),
        "exact_aligned_capacity": int(capacity["exact_aligned_capacity"]),
        "exact_anchor_capacity": int(capacity["exact_anchor_capacity"]),
        "universal_capacity": int(capacity["universal_capacity"]),
    }
