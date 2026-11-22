"""BRC-style convex recoalescence of exact P2-zone Walsh cutoff worlds.

Every cutoff z in the exact linear-Walsh zone

    z2(k) <= z <= C=floor((k-1)/2)

defines a nonnegative orientation detector which is positive exactly on a basin
prime.  Therefore any convex combination of such cutoff worlds is again an
exact nonnegative prime detector.

This branching/recoalescence is analytically nontrivial because it softens the
incidence language.  Let nu_z>=0, sum nu_z=1.  On a prime target with opposite
support S, the incidence-optimal branch at z counts every squarefree divisor

d|rad(S), d<=C

whose largest prime P^+(d) has already entered the visible cutoff.  Hence after
recoalescence the effective divisor coefficient is the cutoff-tail probability

    alpha_nu(d)=sum_{z>=P^+(d)} nu_z.

For a terminal composite target p*q, z<p is required for p to remain in the
high deletion band.  Thus the effective coefficient of one opposite divisor
unit d on that deletion edge is the band mass

    beta_nu(d,p)=sum_{P^+(d)<=z<p} nu_z.

The hard one-cutoff compiler is recovered when nu is a point mass.  A distributed
nu replaces hard scale steps by a task-designed monotone tail/band kernel while
preserving exact prime semantics.  This is a direct BRC/P021-style example:
branch over proof precisions, execute exact worlds, then safely recoalesce.

The mixture floor resource is likewise exact:

    Psi_nu = sum_z nu_z Psi_A(C,z).

No statement here chooses an analytically optimal nu or bounds the recoalesced
boundary discrepancy.  It is a finite exact compiler, not a Legendre proof.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import prod

from .legendre import is_prime
from .p017_mirror import anchor_surviving_radius, mirror_pair, mirror_transverse_supports
from .p017_p018_walsh_p2_cutoff_pareto import (
    exact_linear_cutoff_zone,
    p2_zone_orientation_weight,
)
from .p017_p018_walsh_smooth_shadow_main import anchor_coprime_smooth_shadow


def _normalize_mixture(k: int, mixture: tuple[tuple[int, Fraction], ...]) -> tuple[tuple[int, Fraction], ...]:
    z2, C = exact_linear_cutoff_zone(k)
    if not mixture:
        raise ValueError("mixture must be nonempty")
    merged: dict[int, Fraction] = {}
    for cutoff, weight in mixture:
        if isinstance(cutoff, bool) or not isinstance(cutoff, int) or not (z2 <= cutoff <= C):
            raise ValueError("every cutoff must lie in the exact P2-to-half zone")
        w = Fraction(weight)
        if w < 0:
            raise ValueError("mixture weights must be nonnegative")
        merged[cutoff] = merged.get(cutoff, Fraction(0, 1)) + w
    normalized = tuple(sorted((z, w) for z, w in merged.items() if w))
    total = sum((w for _z, w in normalized), start=Fraction(0, 1))
    if total != 1:
        raise ValueError("mixture weights must sum exactly to one")
    return normalized


def _largest_prime_of_squarefree_divisor(divisor: int) -> int:
    if divisor == 1:
        return 1
    remaining = divisor
    largest = 1
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            largest = p
            remaining //= p
            if remaining % p == 0:
                raise ValueError("divisor must be squarefree")
        p += 2
    if remaining > 1:
        largest = remaining
    return largest


def mixture_divisor_tail_weight(
    k: int,
    divisor: int,
    mixture: tuple[tuple[int, Fraction], ...],
) -> Fraction:
    """Return alpha_nu(d)=nu{z>=P^+(d)}."""
    normalized = _normalize_mixture(k, mixture)
    C = exact_linear_cutoff_zone(k)[1]
    if isinstance(divisor, bool) or not isinstance(divisor, int) or divisor < 1 or divisor > C:
        raise ValueError("divisor must satisfy 1<=d<=C")
    largest = _largest_prime_of_squarefree_divisor(divisor)
    return sum((w for z, w in normalized if z >= largest), start=Fraction(0, 1))


def mixture_deletion_band_weight(
    k: int,
    divisor: int,
    high_prime: int,
    mixture: tuple[tuple[int, Fraction], ...],
) -> Fraction:
    """Return beta_nu(d,p)=nu{P^+(d)<=z<p}."""
    normalized = _normalize_mixture(k, mixture)
    C = exact_linear_cutoff_zone(k)[1]
    if not (1 <= divisor <= C):
        raise ValueError("divisor must satisfy 1<=d<=C")
    largest = _largest_prime_of_squarefree_divisor(divisor)
    p = int(high_prime)
    return sum((w for z, w in normalized if largest <= z < p), start=Fraction(0, 1))


def _squarefree_divisors_from_support(support: tuple[int, ...], cutoff: int) -> tuple[int, ...]:
    values = [1]
    for prime in tuple(sorted(support)):
        values += [value * prime for value in list(values) if value <= cutoff // prime]
    return tuple(sorted(set(values)))


def cutoff_mixture_orientation_point(
    k: int,
    radius: int,
    orientation: str,
    mixture: tuple[tuple[int, Fraction], ...],
) -> dict[str, object]:
    """Evaluate one convexly recoalesced orientation and verify its divisor kernel."""
    normalized = _normalize_mixture(k, mixture)
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")
    if orientation not in ("upper", "lower"):
        raise ValueError("orientation must be 'upper' or 'lower'")

    branch_rows = tuple(
        (z, w, p2_zone_orientation_weight(k, radius, z, orientation))
        for z, w in normalized
    )
    mixed_weight = sum(
        (w * int(row["linear_weight"]) for _z, w, row in branch_rows),
        start=Fraction(0, 1),
    )
    target_prime = bool(branch_rows[0][2]["target_prime"])
    if (mixed_weight > 0) != target_prime:
        raise AssertionError("convex cutoff recoalescence lost exact prime positivity")

    lower_state, upper_state = mirror_pair(k, radius)
    lower_support_raw, upper_support_raw = mirror_transverse_supports(k, radius)
    if orientation == "upper":
        target_state = upper_state
        opposite_support = tuple(int(p) for p in lower_support_raw)
    else:
        target_state = lower_state
        opposite_support = tuple(int(p) for p in upper_support_raw)
    C = exact_linear_cutoff_zone(k)[1]

    if target_prime:
        divisors = _squarefree_divisors_from_support(opposite_support, C)
        reconstructed = sum(
            (mixture_divisor_tail_weight(k, d, normalized) for d in divisors),
            start=Fraction(0, 1),
        )
        if reconstructed != mixed_weight:
            raise AssertionError("mixture prime weight did not equal its tail-kernel divisor expansion")
    else:
        reconstructed = None

    return {
        "k": k,
        "radius": radius,
        "orientation": orientation,
        "mixture": normalized,
        "target_state": target_state,
        "target_prime": target_prime,
        "mixed_orientation_weight": mixed_weight,
        "prime_divisor_kernel_reconstruction": reconstructed,
        "positive_iff_prime": True,
        "branch_rows": branch_rows,
    }


def cutoff_mixture_profile(
    k: int,
    mixture: tuple[tuple[int, Fraction], ...],
) -> dict[str, object]:
    """Aggregate the exact mixture and its convex smooth-shadow floor resource."""
    normalized = _normalize_mixture(k, mixture)
    total = Fraction(0, 1)
    prime_exists = False
    rows: list[dict[str, object]] = []
    for radius in range(1, k):
        if not anchor_surviving_radius(k, radius):
            continue
        for orientation in ("upper", "lower"):
            row = cutoff_mixture_orientation_point(k, radius, orientation, normalized)
            rows.append(row)
            total += Fraction(row["mixed_orientation_weight"])
            prime_exists = prime_exists or bool(row["target_prime"])
    if (total > 0) != prime_exists:
        raise AssertionError("cutoff mixture aggregate lost exact prime-existence equivalence")

    smooth_rows = tuple(
        (z, w, anchor_coprime_smooth_shadow(k, z)["smooth_shadow_count_Psi"])
        for z, w in normalized
    )
    one_orientation_smooth = sum(
        (w * int(psi) for _z, w, psi in smooth_rows), start=Fraction(0, 1)
    )
    return {
        "k": k,
        "mixture": normalized,
        "mixed_weighted_prime_signal": total,
        "prime_exists": prime_exists,
        "positive_iff_prime_exists": (total > 0) == prime_exists,
        "one_orientation_convex_smooth_shadow_main": one_orientation_smooth,
        "symmetric_convex_smooth_shadow_main": 2 * one_orientation_smooth,
        "smooth_shadow_branch_rows": smooth_rows,
        "safe_convex_recoalescence": True,
        "rows": tuple(rows),
    }
