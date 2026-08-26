"""Cross-stratum signed shared-core geometry for P017 mirror cells.

Unlike partial-cell overlap refinement, these identities compare *different*
anchor-surviving radii after their exact full cores are already fixed.
Shared prime-power core content is forced into the signed radius difference or
sum.  This gives a common-center geometric constraint across exact strata and
strictly generalizes the 2*S spacing of one repeated full-core cell.
"""

from __future__ import annotations

from math import gcd

from .p017_core_cell_lattice import exact_full_core_pair


def _require_radius_pair(k: int, left: int, right: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    for name, value in (("left", left), ("right", right)):
        if isinstance(value, bool) or not isinstance(value, int) or not (1 <= value < k):
            raise ValueError(f"{name} must satisfy 1 <= radius < k")
    if left == right:
        raise ValueError("radii must be distinct")
    center = k * (k + 1)
    if gcd(left, center) != 1 or gcd(right, center) != 1:
        raise ValueError("both radii must survive the anchor sieve")


def signed_shared_core_geometry(k: int, left: int, right: int) -> dict[str, int]:
    """CG01-CG02: shared exact-core content divides signed radius geometry.

    Write exact full cores

        (A_r,B_r), (A_s,B_s)

    for lower/upper mirror states M-r,M+r and M-s,M+s.  Then

        gcd(A_r,A_s), gcd(B_r,B_s) | |r-s|,
        gcd(A_r,B_s), gcd(B_r,A_s) | r+s.

    The four gcds are pairwise coprime because opposite cores at either one
    radius are coprime.  Since all gcds are odd and r,s are odd,

        2*G_same | |r-s|,
        2*G_cross | r+s,
        4*G_same*G_cross | |r^2-s^2|.
    """
    _require_radius_pair(k, left, right)
    a_r, b_r = exact_full_core_pair(k, left)
    a_s, b_s = exact_full_core_pair(k, right)

    lower_lower = gcd(a_r, a_s)
    upper_upper = gcd(b_r, b_s)
    lower_upper = gcd(a_r, b_s)
    upper_lower = gcd(b_r, a_s)
    components = (lower_lower, upper_upper, lower_upper, upper_lower)

    for i, first in enumerate(components):
        for second in components[i + 1 :]:
            if gcd(first, second) != 1:
                raise AssertionError("shared-core overlap classes are not pairwise coprime")

    same_product = lower_lower * upper_upper
    cross_product = lower_upper * upper_lower
    delta = abs(left - right)
    radius_sum = left + right
    square_delta = abs(left * left - right * right)

    if delta % (2 * same_product) != 0:
        raise AssertionError("same-side shared cores did not divide the even radius difference")
    if radius_sum % (2 * cross_product) != 0:
        raise AssertionError("cross-side shared cores did not divide the even radius sum")
    total_overlap = same_product * cross_product
    if square_delta % (4 * total_overlap) != 0:
        raise AssertionError("total shared-core overlap did not divide the radius-square difference")

    return {
        "left_radius": left,
        "right_radius": right,
        "left_lower_core": a_r,
        "left_upper_core": b_r,
        "right_lower_core": a_s,
        "right_upper_core": b_s,
        "lower_lower_gcd": lower_lower,
        "upper_upper_gcd": upper_upper,
        "lower_upper_gcd": lower_upper,
        "upper_lower_gcd": upper_lower,
        "same_side_overlap": same_product,
        "cross_side_overlap": cross_product,
        "total_overlap": total_overlap,
        "radius_difference": delta,
        "radius_sum": radius_sum,
        "radius_square_difference": square_delta,
    }


def repeated_full_core_spacing(k: int, left: int, right: int) -> dict[str, int]:
    """CG03: recover fixed-cell 2ab spacing as a cross-stratum corollary."""
    data = signed_shared_core_geometry(k, left, right)
    a = int(data["left_lower_core"])
    b = int(data["left_upper_core"])
    if (a, b) != (int(data["right_lower_core"]), int(data["right_upper_core"])):
        raise ValueError("radii must have the same exact full-core pair")
    spacing = 2 * a * b
    delta = int(data["radius_difference"])
    if delta % spacing != 0:
        raise AssertionError("repeated exact full-core cell lost its 2ab spacing")
    return {"core_product": a * b, "spacing_modulus": spacing, "radius_difference": delta}


def prefix_large_core_exclusion(k: int, core_divisor: int, radius_limit: int) -> dict[str, object]:
    """CG04: large shared core divisors cannot repeat densely near the origin.

    For anchor-surviving radii 1<=r<=R, collect sides whose exact full core is
    divisible by the declared odd divisor D.  If D>R, each orientation occurs at
    most once.  If D>2R, at most one incidence occurs across both orientations.
    """
    if isinstance(core_divisor, bool) or not isinstance(core_divisor, int) or core_divisor <= 0 or core_divisor % 2 == 0:
        raise ValueError("core_divisor must be a positive odd integer")
    if isinstance(radius_limit, bool) or not isinstance(radius_limit, int) or not (1 <= radius_limit < k):
        raise ValueError("radius_limit must satisfy 1 <= R < k")
    center = k * (k + 1)
    if gcd(core_divisor, center) != 1:
        raise ValueError("core_divisor must be transverse to the square-basin center")

    lower_hits: list[int] = []
    upper_hits: list[int] = []
    for radius in range(1, radius_limit + 1):
        if gcd(radius, center) != 1:
            continue
        lower, upper = exact_full_core_pair(k, radius)
        if lower % core_divisor == 0:
            lower_hits.append(radius)
        if upper % core_divisor == 0:
            upper_hits.append(radius)

    if core_divisor > radius_limit:
        if len(lower_hits) > 1 or len(upper_hits) > 1:
            raise AssertionError("large same-side core divisor repeated inside too short a prefix")
    if core_divisor > 2 * radius_limit:
        if len(lower_hits) + len(upper_hits) > 1:
            raise AssertionError("very large core divisor repeated across signed prefix incidences")

    return {
        "core_divisor": core_divisor,
        "radius_limit": radius_limit,
        "lower_hits": tuple(lower_hits),
        "upper_hits": tuple(upper_hits),
        "total_hits": len(lower_hits) + len(upper_hits),
    }
