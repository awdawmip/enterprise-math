"""Exact criterion for collapsing continuation types in LEGO interaction space.

Suppose fine continuation types are merged into coarse types and a finite integer
response is represented in the product-binomial interaction basis.  By repeated
Vandermonde identity, a response depends only on coarse type totals iff its fine
interaction coefficient a_k depends only on the blockwise sums of k.

Thus future-safe type collapse can be tested directly on irreducible interaction
coefficients: merged types are indistinguishable precisely when no interaction
coefficient remembers how selected witnesses were distributed inside a coarse
type block.
"""

from __future__ import annotations

CountVector = tuple[int, ...]


def coarse_interaction_order(
    fine_order: CountVector,
    fine_to_coarse: tuple[int, ...],
    coarse_type_count: int,
) -> CountVector:
    if not isinstance(fine_order, tuple) or not fine_order:
        raise ValueError("fine_order must be a non-empty tuple")
    if len(fine_order) != len(fine_to_coarse):
        raise ValueError("fine_order and fine_to_coarse must have equal length")
    if isinstance(coarse_type_count, bool) or not isinstance(coarse_type_count, int) or coarse_type_count <= 0:
        raise ValueError("coarse_type_count must be a positive integer")
    result = [0] * coarse_type_count
    for value, coarse in zip(fine_order, fine_to_coarse):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("interaction orders must be non-negative integers")
        if isinstance(coarse, bool) or not isinstance(coarse, int) or not (0 <= coarse < coarse_type_count):
            raise ValueError("fine_to_coarse entries must index coarse types")
        result[coarse] += value
    return tuple(result)


def interaction_spectrum_descends(
    fine_coefficients: dict[CountVector, int],
    fine_to_coarse: tuple[int, ...],
    coarse_type_count: int,
) -> bool:
    """Whether fine coefficients are constant on each block-sum order fiber."""
    seen: dict[CountVector, int] = {}
    for fine_order, coefficient in fine_coefficients.items():
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise ValueError("interaction coefficients must be integers")
        coarse_order = coarse_interaction_order(
            fine_order, fine_to_coarse, coarse_type_count
        )
        if coarse_order in seen and seen[coarse_order] != coefficient:
            return False
        seen[coarse_order] = coefficient
    return True


def induced_coarse_interaction_spectrum(
    fine_coefficients: dict[CountVector, int],
    fine_to_coarse: tuple[int, ...],
    coarse_type_count: int,
) -> dict[CountVector, int]:
    """Return the unique coarse coefficient A_K when descent is exact."""
    result: dict[CountVector, int] = {}
    for fine_order, coefficient in fine_coefficients.items():
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise ValueError("interaction coefficients must be integers")
        coarse_order = coarse_interaction_order(
            fine_order, fine_to_coarse, coarse_type_count
        )
        existing = result.get(coarse_order)
        if existing is not None and existing != coefficient:
            raise ValueError("interaction spectrum does not descend to the proposed type collapse")
        result[coarse_order] = coefficient
    return result
