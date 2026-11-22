"""P017 partial/full-core cell lattice and exact refinement identities.

This module records a route-pruning result for the square-basin mirror program.
Partial lower/upper smooth-core divisibility cells are closed under intersection:
compatible intersections replace each side by the lcm of the requested cores.
The exact full-core strata are the terminal labels of this divisibility refinement,
and partial-cell counts are their two-dimensional divisor-poset zeta transform.

The divisor lattice, CRT, and Moebius inversion are classical.  The P017 value is
to show that candidate-cell overlap bookkeeping contains no information beyond
exact full-core refinement; genuine new leverage must couple distinct exact cells.
"""

from __future__ import annotations

from math import gcd, lcm

from .factor_precision import smallest_prime_factor
from .p017_cofactor_window import square_basin_smooth_tail


def _require_k(k: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")


def _require_positive_odd(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0 or value % 2 == 0:
        raise ValueError(f"{name} must be a positive odd integer")


def _is_k_smooth(value: int, k: int) -> bool:
    """Return whether every prime factor of value is at most k."""
    _require_positive_odd("value", value)
    _require_k(k)
    remaining = value
    while remaining > 1:
        prime = smallest_prime_factor(remaining)
        if prime > k:
            return False
        while remaining % prime == 0:
            remaining //= prime
    return True


def admissible_partial_core_pair(k: int, lower_core: int, upper_core: int) -> bool:
    """Check the P017 partial-core hypotheses for an oriented mirror cell."""
    _require_k(k)
    _require_positive_odd("lower_core", lower_core)
    _require_positive_odd("upper_core", upper_core)
    center = k * (k + 1)
    return (
        gcd(lower_core, upper_core) == 1
        and gcd(lower_core * upper_core, center) == 1
        and _is_k_smooth(lower_core, k)
        and _is_k_smooth(upper_core, k)
    )


def raw_partial_core_progression(k: int, lower_core: int, upper_core: int) -> dict[str, object]:
    """Return the unique odd CRT progression before the common anchor filter.

    The cell requires

        lower_core | M-r,
        upper_core | M+r,
        r odd,

    where M=k(k+1).  For an admissible pair the three moduli are coprime, so the
    solution is one residue class modulo 2*lower_core*upper_core.
    """
    if not admissible_partial_core_pair(k, lower_core, upper_core):
        raise ValueError("partial core pair is not admissible")
    center = k * (k + 1)
    a = lower_core
    b = upper_core
    product = a * b

    if product == 1:
        residue_mod_product = 0
    elif b == 1:
        residue_mod_product = center % a
    else:
        step = (-2 * center * pow(a, -1, b)) % b
        residue_mod_product = (center + a * step) % product

    odd_residue = residue_mod_product if residue_mod_product % 2 else residue_mod_product + product
    if not (1 <= odd_residue < 2 * product):
        raise AssertionError("odd CRT representative escaped its canonical range")

    raw_radii = tuple(range(odd_residue, k, 2 * product)) if odd_residue < k else ()
    return {
        "k": k,
        "lower_core": a,
        "upper_core": b,
        "core_product": product,
        "residue": odd_residue,
        "modulus": 2 * product,
        "raw_radii": raw_radii,
    }


def partial_core_cell(k: int, lower_core: int, upper_core: int) -> tuple[int, ...]:
    """Return anchor-surviving radii in one oriented partial-core cell."""
    data = raw_partial_core_progression(k, lower_core, upper_core)
    center = k * (k + 1)
    radii = tuple(r for r in data["raw_radii"] if gcd(r, center) == 1)
    for r in radii:
        if (center - r) % lower_core or (center + r) % upper_core:
            raise AssertionError("partial-core cell lost its defining divisibility")
    return radii


def intersect_partial_core_cells(
    k: int,
    lower_a: int,
    upper_b: int,
    lower_c: int,
    upper_d: int,
) -> dict[str, object]:
    """CC01: compatible cell intersections lcm-promote sidewise.

    Put A=lcm(lower_a,lower_c), B=lcm(upper_b,upper_d).  If gcd(A,B)>1 the
    intersection is empty: a shared odd transverse prime would divide both
    M-r and M+r, hence 2M, contradicting transversality.  Otherwise

        C(a,b) intersect C(c,d) = C(A,B).
    """
    if not admissible_partial_core_pair(k, lower_a, upper_b):
        raise ValueError("first partial core pair is not admissible")
    if not admissible_partial_core_pair(k, lower_c, upper_d):
        raise ValueError("second partial core pair is not admissible")

    combined_lower = lcm(lower_a, lower_c)
    combined_upper = lcm(upper_b, upper_d)
    left = set(partial_core_cell(k, lower_a, upper_b))
    right = set(partial_core_cell(k, lower_c, upper_d))
    actual = tuple(sorted(left.intersection(right)))

    conflict = gcd(combined_lower, combined_upper) > 1
    if conflict:
        expected: tuple[int, ...] = ()
    else:
        if not admissible_partial_core_pair(k, combined_lower, combined_upper):
            raise AssertionError("compatible lcm promotion left the admissible core family")
        expected = partial_core_cell(k, combined_lower, combined_upper)
    if actual != expected:
        raise AssertionError("partial-core cell intersection failed lcm closure")

    return {
        "combined_lower": combined_lower,
        "combined_upper": combined_upper,
        "combined_product": combined_lower * combined_upper,
        "cross_side_conflict": conflict,
        "intersection": actual,
    }


def exact_full_core_pair(k: int, radius: int) -> tuple[int, int]:
    """Return the canonical lower/upper full k-smooth core label of one radius."""
    _require_k(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1 <= radius < k")
    center = k * (k + 1)
    if gcd(radius, center) != 1:
        raise ValueError("radius must survive the anchor sieve")

    lower = square_basin_smooth_tail(k, center - radius)
    upper = square_basin_smooth_tail(k, center + radius)
    a = int(lower["smooth_core"])
    b = int(upper["smooth_core"])
    if a % 2 == 0 or b % 2 == 0 or gcd(a, b) != 1 or gcd(a * b, center) != 1:
        raise AssertionError("exact anchor-surviving full cores lost odd transverse coprimality")
    return a, b


def exact_full_core_strata(k: int) -> dict[tuple[int, int], tuple[int, ...]]:
    """Partition all anchor-surviving radii by their exact full-core pair."""
    _require_k(k)
    center = k * (k + 1)
    buckets: dict[tuple[int, int], list[int]] = {}
    for radius in range(1, k):
        if gcd(radius, center) != 1:
            continue
        label = exact_full_core_pair(k, radius)
        buckets.setdefault(label, []).append(radius)
    return {label: tuple(radii) for label, radii in buckets.items()}


def partial_cell_zeta_count(k: int, lower_core: int, upper_core: int) -> dict[str, int]:
    """CC02: partial-cell count is the zeta sum of exact full-core strata."""
    if not admissible_partial_core_pair(k, lower_core, upper_core):
        raise ValueError("partial core pair is not admissible")
    direct = len(partial_core_cell(k, lower_core, upper_core))
    strata = exact_full_core_strata(k)
    zeta = sum(
        len(radii)
        for (a, b), radii in strata.items()
        if a % lower_core == 0 and b % upper_core == 0
    )
    if direct != zeta:
        raise AssertionError("partial-cell zeta identity failed")
    return {"direct_count": direct, "zeta_count": zeta}


def _divisors(value: int) -> tuple[int, ...]:
    result: list[int] = []
    d = 1
    while d * d <= value:
        if value % d == 0:
            result.append(d)
            if d * d != value:
                result.append(value // d)
        d += 1
    return tuple(sorted(result))


def _moebius(value: int) -> int:
    if value == 1:
        return 1
    remaining = value
    sign = 1
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            sign = -sign
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        sign = -sign
    return sign


def exact_stratum_moebius_count(k: int, lower_core: int, upper_core: int) -> dict[str, int]:
    """CC03: recover one exact full-core stratum by double Moebius inversion.

    Only multipliers that divide some actually represented full core can produce
    a nonzero cell, so the apparently infinite divisor-poset inversion is finite
    on the square basin.
    """
    if not admissible_partial_core_pair(k, lower_core, upper_core):
        raise ValueError("target exact core pair is not admissible")
    strata = exact_full_core_strata(k)
    direct = len(strata.get((lower_core, upper_core), ()))

    lower_multipliers: set[int] = set()
    upper_multipliers: set[int] = set()
    for a, b in strata:
        if a % lower_core == 0:
            lower_multipliers.update(_divisors(a // lower_core))
        if b % upper_core == 0:
            upper_multipliers.update(_divisors(b // upper_core))

    inversion = 0
    for u in lower_multipliers:
        mu_u = _moebius(u)
        if mu_u == 0:
            continue
        for v in upper_multipliers:
            mu_v = _moebius(v)
            if mu_v == 0:
                continue
            a = lower_core * u
            b = upper_core * v
            if gcd(a, b) > 1 or gcd(a * b, k * (k + 1)) > 1:
                count = 0
            elif not (_is_k_smooth(a, k) and _is_k_smooth(b, k)):
                count = 0
            else:
                count = len(partial_core_cell(k, a, b))
            inversion += mu_u * mu_v * count

    if inversion != direct:
        raise AssertionError("double Moebius inversion failed to recover exact stratum")
    return {"direct_count": direct, "moebius_count": inversion}


def residual_strict_refinement_steps(k: int, initial_product: int) -> int:
    """CC04: bound strict odd-core refinement depth while the product stays < k.

    Every strict componentwise divisibility refinement multiplies the odd core
    product by an odd integer at least three.  This function returns the maximum
    number of such strict steps allowed before the product can no longer remain
    below k.
    """
    _require_k(k)
    if isinstance(initial_product, bool) or not isinstance(initial_product, int) or initial_product <= 0:
        raise ValueError("initial_product must be a positive integer")
    if initial_product % 2 == 0:
        raise ValueError("initial_product must be odd")
    steps = 0
    product = initial_product
    while 3 * product < k:
        product *= 3
        steps += 1
    return steps
