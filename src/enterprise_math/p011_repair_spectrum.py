"""P011 irreversibility spectrum as exact provenance-repair complexity.

For a finite deterministic map ``F : X -> Y``, retaining only ``F(x)`` while
asking to recover the original label ``x`` requires exactly ``|F^{-1}(y)|``
repair symbols on output fiber ``y``.  Hence the canonical P011 collision
spectrum is equally the binomial spectrum of local minimum repair alphabets.

This is a mathematical reconstruction statement.  It does not assert that a
many-to-one physical process stores, exposes, or reverses the discarded label.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Mapping
from math import comb
from typing import TypeVar

X = TypeVar("X", bound=Hashable)
Y = TypeVar("Y", bound=Hashable)
Z = TypeVar("Z", bound=Hashable)


def _finite_map(mapping: Mapping[X, Y]) -> dict[X, Y]:
    result = dict(mapping)
    if not result:
        raise ValueError("mapping must have a nonempty finite domain")
    return result


def fiber_sizes(mapping: Mapping[X, Y]) -> dict[Y, int]:
    """Return sizes of all nonempty fibers over the reached image."""

    current = _finite_map(mapping)
    return dict(Counter(current.values()))


def provenance_repair_profile(mapping: Mapping[X, Y]) -> dict[Y, int]:
    """Local minimum repair alphabet for recovering the original state label.

    The value over reached output ``y`` is exactly ``|F^{-1}(y)|``.
    """

    return fiber_sizes(mapping)


def maximum_provenance_repair_alphabet(mapping: Mapping[X, Y]) -> int:
    """Global minimum alphabet size for exact provenance recovery over ``F``."""

    return max(provenance_repair_profile(mapping).values())


def collision_repair_count(mapping: Mapping[X, Y], order: int) -> int:
    """P011 ``J_order`` written from local repair alphabet sizes."""

    current = _finite_map(mapping)
    if order < 1:
        raise ValueError("order must be positive")
    if order > len(current):
        return 0
    return sum(comb(size, order) for size in provenance_repair_profile(current).values())


def collision_repair_spectrum(mapping: Mapping[X, Y]) -> tuple[int, ...]:
    """Return ``(J_1,...,J_N)`` for an N-state domain."""

    current = _finite_map(mapping)
    return tuple(
        collision_repair_count(current, order)
        for order in range(1, len(current) + 1)
    )


def repair_alphabet_distribution(mapping: Mapping[X, Y]) -> dict[int, int]:
    """Count reached outputs by their local minimum repair alphabet size."""

    current = _finite_map(mapping)
    counts = Counter(provenance_repair_profile(current).values())
    return {size: counts.get(size, 0) for size in range(1, len(current) + 1)}


def reconstruct_repair_distribution_from_spectrum(
    spectrum: tuple[int, ...] | list[int],
) -> dict[int, int]:
    """P011 binomial inversion interpreted as repair-size reconstruction."""

    values = tuple(spectrum)
    if not values:
        raise ValueError("spectrum must be nonempty")
    n = values[0]
    if not isinstance(n, int) or n < 1:
        raise ValueError("J_1 must be a positive integer domain size")
    if len(values) != n:
        raise ValueError("full spectrum must contain exactly J_1 through J_N")
    if any(not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("spectrum entries must be nonnegative integers")

    padded = (0,) + values
    return {
        size: sum(
            (-1) ** (order - size) * comb(order, size) * padded[order]
            for order in range(size, n + 1)
        )
        for size in range(1, n + 1)
    }


def compose_maps(first: Mapping[X, Y], second: Mapping[Y, Z]) -> dict[X, Z]:
    """Return ``second ∘ first`` on the finite domain of ``first``."""

    left = _finite_map(first)
    right = dict(second)
    missing = set(left.values()) - set(right)
    if missing:
        raise ValueError("second map must cover the reached image of first")
    return {state: right[mid] for state, mid in left.items()}


def reachable_second_fiber_sizes(
    first: Mapping[X, Y], second: Mapping[Y, Z]
) -> dict[Z, int]:
    """Fiber sizes of ``second`` restricted to the reached image of ``first``."""

    left = _finite_map(first)
    right = dict(second)
    reached = set(left.values())
    missing = reached - set(right)
    if missing:
        raise ValueError("second map must cover the reached image of first")
    counts = Counter(right[mid] for mid in reached)
    return dict(counts)


def composition_repair_profile(
    first: Mapping[X, Y], second: Mapping[Y, Z]
) -> dict[Z, int]:
    """Exact local repair profile after postcomposition.

    For each reached ``z``:

        r_{G∘F}(z) = sum_{y in im(F), G(y)=z} r_F(y).
    """

    first_profile = provenance_repair_profile(first)
    right = dict(second)
    missing = set(first_profile) - set(right)
    if missing:
        raise ValueError("second map must cover the reached image of first")

    totals: dict[Z, int] = {}
    for mid, local_repair in first_profile.items():
        out = right[mid]
        totals[out] = totals.get(out, 0) + local_repair
    return totals


def composition_repair_bound(
    first: Mapping[X, Y], second: Mapping[Y, Z]
) -> dict[str, int | bool]:
    """Return the exact maximum repair and its sharp product upper bound."""

    first_max = maximum_provenance_repair_alphabet(first)
    second_profile = reachable_second_fiber_sizes(first, second)
    second_max = max(second_profile.values())
    composed_max = max(composition_repair_profile(first, second).values())
    bound = first_max * second_max
    if composed_max > bound:
        raise AssertionError("composition repair exceeded product upper bound")
    return {
        "first_max": first_max,
        "second_reachable_max": second_max,
        "composed_max": composed_max,
        "product_bound": bound,
        "equality": composed_max == bound,
    }


def composition_bound_equality_witness(
    first: Mapping[X, Y], second: Mapping[Y, Z]
) -> Z | None:
    """Find a target fiber certifying equality in the product bound, if any.

    Equality occurs exactly when one maximum-size reachable ``G`` fiber is made
    entirely of maximum-size ``F`` fibers.
    """

    first_profile = provenance_repair_profile(first)
    right = dict(second)
    missing = set(first_profile) - set(right)
    if missing:
        raise ValueError("second map must cover the reached image of first")

    first_max = max(first_profile.values())
    groups: dict[Z, list[Y]] = {}
    for mid in first_profile:
        groups.setdefault(right[mid], []).append(mid)
    second_max = max(len(group) for group in groups.values())

    for out, mids in groups.items():
        if len(mids) == second_max and all(first_profile[mid] == first_max for mid in mids):
            return out
    return None
