"""Exact disjoint-cell decomposition of the residual P017 hard core.

This L3 bridge uses only canonical P017 ingredients:

* the unique full ``k``-smooth core / large-prime tail decomposition (L020
  machinery, exposed by ``square_basin_smooth_tail``);
* the canonical L053 full-core CRT progression.

The extra condition ``S=a*b<k`` is the discovery-stage residual hard-core cut
used by P017 PR #150.  It is deliberately kept as a WIP hypothesis rather than
silently promoted to canonical status.

For every residual radius ``r`` put ``M=k(k+1)`` and write uniquely

    M-r = a*q_minus,
    M+r = b*q_plus,

where ``a,b`` are the ordered lower/upper full ``k``-smooth cores and the tails
are primes greater than ``k``.  The ordered key ``(a,b)`` is therefore unique.
Canonical L053 places ``r`` in one residue class modulo the odd product
``S=a*b``.  Anchor survival forces ``r`` odd, so one exact cell occupies one
class modulo ``2S``.

If ``r_t=r+2S*t`` is another bounded parity-compatible lift, then exact integer
transport gives

    q_minus(t) = q_minus(0) - 2*b*t,
    q_plus(t)  = q_plus(0)  + 2*a*t.

Conversely, whenever both transported tails are primes greater than ``k``, the
full smooth cores of the two mirror states are again exactly ``a,b``.  Hence the
residual hard-core radii are a *disjoint union* of these simultaneous-prime
lifts:

    N_hard(k) = sum_(ordered cells a,b) P_{a,b}(k).

This is an exact counting identity, not a sieve estimate and not a Legendre
proof.  Its purpose is to connect the structural bridge to later global upper
bounds without double counting cells or prime-tail states.
"""

from __future__ import annotations

from .legendre import is_prime
from .p017_cofactor_window import square_basin_smooth_tail
from .p017_mirror import anchor_surviving_radius, mirror_center, mirror_pair
from .p017_mirror_crt import observed_mirror_full_core_idempotent


def _require_k_radius(k: int, radius: int) -> None:
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")
    if isinstance(radius, bool) or not isinstance(radius, int):
        raise ValueError("radius must be an integer")
    if not 1 <= radius < k:
        raise ValueError("require 1 <= radius < k")


def residual_hard_core_record(k: int, radius: int) -> dict[str, int]:
    """Return the unique ordered full-core/tail record of one residual radius."""
    _require_k_radius(k, radius)
    if not anchor_surviving_radius(k, radius):
        raise ValueError("radius must survive the anchor sieve")

    center = mirror_center(k)
    lower, upper = mirror_pair(k, radius)
    lower_data = square_basin_smooth_tail(k, lower)
    upper_data = square_basin_smooth_tail(k, upper)
    if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
        raise ValueError("residual hard core requires both mirror states composite")

    a = int(lower_data["smooth_core"])
    b = int(upper_data["smooth_core"])
    q_minus = int(lower_data["tail"])
    q_plus = int(upper_data["tail"])
    product = a * b

    if a <= 1 or b <= 1:
        raise ValueError("residual hard core requires two nontrivial full cores")
    if product >= k:
        raise ValueError("residual hard-core cut requires a*b < k")
    if q_minus <= k or q_plus <= k or not is_prime(q_minus) or not is_prime(q_plus):
        raise ValueError("residual hard core requires two prime tails greater than k")
    if a % 2 == 0 or b % 2 == 0:
        raise AssertionError("anchor-surviving full cores must be odd")
    if lower != a * q_minus or upper != b * q_plus:
        raise AssertionError("smooth-core/tail reconstruction failed")

    return {
        "k": k,
        "radius": radius,
        "center": center,
        "lower": lower,
        "upper": upper,
        "lower_core": a,
        "upper_core": b,
        "core_product": product,
        "lower_tail": q_minus,
        "upper_tail": q_plus,
    }


def residual_affine_cell(k: int, seed_radius: int) -> dict[str, object]:
    """Reconstruct every bounded simultaneous-prime lift of one exact cell."""
    seed = residual_hard_core_record(k, seed_radius)
    canonical = observed_mirror_full_core_idempotent(k, seed_radius)

    a = int(seed["lower_core"])
    b = int(seed["upper_core"])
    s = a * b
    center = int(seed["center"])
    q_minus_0 = int(seed["lower_tail"])
    q_plus_0 = int(seed["upper_tail"])

    if (int(canonical["lower_core"]), int(canonical["upper_core"])) != (a, b):
        raise AssertionError("L053 full-core key disagrees with the unique smooth decomposition")
    if int(canonical["modulus"]) != s:
        raise AssertionError("L053 modulus is not the full-core product")

    parity_lifts = tuple(
        int(candidate)
        for candidate in canonical["full_core_lifts"]
        if int(candidate) % 2 == 1
    )
    orbit: list[dict[str, int | bool]] = []
    residual_lifts: list[int] = []

    for candidate in parity_lifts:
        delta = candidate - seed_radius
        if delta % (2 * s):
            raise AssertionError("parity-compatible L053 lift escaped the 2S lattice")
        t = delta // (2 * s)
        q_minus = q_minus_0 - 2 * b * t
        q_plus = q_plus_0 + 2 * a * t

        if center - candidate != a * q_minus:
            raise AssertionError("lower affine tail transport failed")
        if center + candidate != b * q_plus:
            raise AssertionError("upper affine tail transport failed")
        if a * q_minus + b * q_plus != 2 * center:
            raise AssertionError("weighted affine conservation failed")

        simultaneous_prime = (
            q_minus > k
            and q_plus > k
            and is_prime(q_minus)
            and is_prime(q_plus)
        )
        anchor_ok = anchor_surviving_radius(k, candidate)
        exact_same_cell = False

        if simultaneous_prime:
            # Because a,b are k-smooth and q_-,q_+ are primes >k, the unique
            # L020 smooth decomposition must recover the same ordered cores.
            lower_data = square_basin_smooth_tail(k, center - candidate)
            upper_data = square_basin_smooth_tail(k, center + candidate)
            exact_same_cell = (
                int(lower_data["smooth_core"]) == a
                and int(upper_data["smooth_core"]) == b
                and int(lower_data["tail"]) == q_minus
                and int(upper_data["tail"]) == q_plus
            )
            if not exact_same_cell:
                raise AssertionError("simultaneous-prime lift changed its unique full-core key")
            if not anchor_ok:
                raise AssertionError("simultaneous large-prime lift failed anchor survival")
            residual_lifts.append(candidate)

        orbit.append(
            {
                "t": t,
                "radius": candidate,
                "lower_tail": q_minus,
                "upper_tail": q_plus,
                "anchor_survives": anchor_ok,
                "simultaneous_prime": simultaneous_prime,
                "exact_same_cell": exact_same_cell,
            }
        )

    return {
        **seed,
        "cell_key": (a, b),
        "parity_modulus": 2 * s,
        "parity_lifts": parity_lifts,
        "orbit": tuple(orbit),
        "residual_lifts": tuple(residual_lifts),
        "simultaneous_prime_count": len(residual_lifts),
    }


def residual_hard_core_partition(k: int) -> dict[str, object]:
    """Partition all residual hard-core radii into disjoint ordered cells exactly."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >= 2")

    grouped: dict[tuple[int, int], list[int]] = {}
    residual_radii: list[int] = []
    for radius in range(1, k):
        try:
            record = residual_hard_core_record(k, radius)
        except ValueError:
            continue
        key = (int(record["lower_core"]), int(record["upper_core"]))
        grouped.setdefault(key, []).append(radius)
        residual_radii.append(radius)

    cells: dict[tuple[int, int], dict[str, object]] = {}
    reconstructed: list[int] = []
    for key, radii in sorted(grouped.items()):
        cell = residual_affine_cell(k, radii[0])
        actual = tuple(sorted(radii))
        predicted = tuple(sorted(int(r) for r in cell["residual_lifts"]))
        if predicted != actual:
            raise AssertionError("simultaneous-prime affine lifts did not equal the exact residual cell")
        if tuple(cell["cell_key"]) != key:
            raise AssertionError("cell reconstruction changed the ordered full-core key")
        cells[key] = cell
        reconstructed.extend(predicted)

    if sorted(reconstructed) != sorted(residual_radii):
        raise AssertionError("cell decomposition lost or double-counted residual radii")
    if len(reconstructed) != len(set(reconstructed)):
        raise AssertionError("distinct ordered full-core cells overlap in radius")

    cell_mass = sum(int(cell["simultaneous_prime_count"]) for cell in cells.values())
    if cell_mass != len(residual_radii):
        raise AssertionError("hard-core count identity failed")

    return {
        "k": k,
        "residual_radii": tuple(residual_radii),
        "residual_count": len(residual_radii),
        "cell_count": len(cells),
        "cells": cells,
        "cell_prime_lift_mass": cell_mass,
    }
