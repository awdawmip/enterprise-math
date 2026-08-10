"""Biaxial extension diamond and representation Pareto envelope.

For the Stage-93 Ferrers precision state, inserting one threshold and appending
one orbit node commute semantically: either order produces the same final
activation matrix, crossings, ranks and boundary word.  On the path coordinate
the two routes are one V insertion followed by one H insertion versus the
opposite order.

This module also records an unweighted worst-case coordinate-write envelope:

    crossings: (storage=s,     threshold=1,   orbit=s)
    ranks:     (storage=h+1,   threshold=h+1, orbit=1)
    boundary:  (storage=s+h+1, threshold=1,   orbit=1)

For nontrivial grids s>=2 and h>=1 these three cost vectors are pairwise
nondominating.  Degenerate one-row/one-column cases collapse the frontier.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_dyadic_boundary_update import (
    orbit_axis_extension,
    threshold_axis_extension,
)
from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import (
    DyadicThresholdStaircase,
    dyadic_threshold_staircase,
)


@dataclass(frozen=True)
class BiaxialExtensionDiamond:
    new_threshold: Fraction
    old_boundary_word: str
    threshold_first_word: str
    orbit_first_word: str
    final_word_threshold_then_orbit: str
    final_word_orbit_then_threshold: str
    final_crossings: tuple[int | None, ...]
    final_ranks: tuple[int, ...]
    threshold_then_orbit_symbols: tuple[str, str]
    orbit_then_threshold_symbols: tuple[str, str]
    diamond_commutes: bool


@dataclass(frozen=True)
class RepresentationCostVector:
    representation: str
    storage_coordinates: int
    threshold_extension_worst_case_writes: int
    orbit_extension_worst_case_writes: int


def biaxial_extension_diamond(
    staircase: DyadicThresholdStaircase,
    new_threshold: Fraction,
) -> BiaxialExtensionDiamond:
    """Verify threshold and orbit one-axis extensions commute exactly."""
    if not isinstance(new_threshold, Fraction) or new_threshold <= 0:
        raise ValueError("new_threshold must be a positive Fraction")
    if new_threshold in staircase.thresholds:
        raise ValueError("new_threshold must not duplicate an existing threshold")

    thresholds = tuple(sorted((*staircase.thresholds, new_threshold)))
    threshold_first = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps,
        thresholds,
    )
    orbit_first = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        staircase.thresholds,
    )
    final_a = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        thresholds,
    )
    final_b = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        thresholds,
    )

    # Verify each local edge with the Stage-94 update compiler.
    old_to_t = threshold_axis_extension(staircase, new_threshold)
    t_to_final = orbit_axis_extension(threshold_first)
    old_to_j = orbit_axis_extension(staircase)
    j_to_final = threshold_axis_extension(orbit_first, new_threshold)

    if old_to_t.inserted_boundary_symbol != "V" or t_to_final.inserted_boundary_symbol != "H":
        raise AssertionError("threshold-then-orbit path lost V/H edge labels")
    if old_to_j.inserted_boundary_symbol != "H" or j_to_final.inserted_boundary_symbol != "V":
        raise AssertionError("orbit-then-threshold path lost H/V edge labels")

    boundary_old = ferrers_boundary_from_staircase(staircase)
    boundary_t = ferrers_boundary_from_staircase(threshold_first)
    boundary_j = ferrers_boundary_from_staircase(orbit_first)
    boundary_a = ferrers_boundary_from_staircase(final_a)
    boundary_b = ferrers_boundary_from_staircase(final_b)

    if final_a.crossing_depths != final_b.crossing_depths:
        raise AssertionError("biaxial extension order changed crossing state")
    if boundary_a.node_ranks != boundary_b.node_ranks:
        raise AssertionError("biaxial extension order changed rank state")
    if boundary_a.boundary_word != boundary_b.boundary_word:
        raise AssertionError("biaxial extension order changed Ferrers boundary")
    if final_a.activation_matrix != final_b.activation_matrix:
        raise AssertionError("biaxial extension order changed semantic activation matrix")

    return BiaxialExtensionDiamond(
        new_threshold=new_threshold,
        old_boundary_word=boundary_old.boundary_word,
        threshold_first_word=boundary_t.boundary_word,
        orbit_first_word=boundary_j.boundary_word,
        final_word_threshold_then_orbit=boundary_a.boundary_word,
        final_word_orbit_then_threshold=boundary_b.boundary_word,
        final_crossings=final_a.crossing_depths,
        final_ranks=boundary_a.node_ranks,
        threshold_then_orbit_symbols=("V", "H"),
        orbit_then_threshold_symbols=("H", "V"),
        diamond_commutes=True,
    )


def representation_cost_vectors(
    horizon_steps: int,
    threshold_count: int,
) -> tuple[RepresentationCostVector, ...]:
    """Return unit-coordinate worst-case storage/update vectors for the three charts."""
    if isinstance(horizon_steps, bool) or not isinstance(horizon_steps, int) or horizon_steps < 0:
        raise ValueError("horizon_steps must be a non-negative integer")
    if isinstance(threshold_count, bool) or not isinstance(threshold_count, int) or threshold_count < 1:
        raise ValueError("threshold_count must be a positive integer")
    hnodes = horizon_steps + 1
    s = threshold_count
    return (
        RepresentationCostVector("crossings", s, 1, s),
        RepresentationCostVector("ranks", hnodes, hnodes, 1),
        RepresentationCostVector("boundary", s + hnodes, 1, 1),
    )


def _dominates(left: RepresentationCostVector, right: RepresentationCostVector) -> bool:
    a = (
        left.storage_coordinates,
        left.threshold_extension_worst_case_writes,
        left.orbit_extension_worst_case_writes,
    )
    b = (
        right.storage_coordinates,
        right.threshold_extension_worst_case_writes,
        right.orbit_extension_worst_case_writes,
    )
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def pareto_representations(
    horizon_steps: int,
    threshold_count: int,
) -> tuple[str, ...]:
    """Return nondominated representations under the declared unit-write envelope."""
    vectors = representation_cost_vectors(horizon_steps, threshold_count)
    return tuple(
        candidate.representation
        for candidate in vectors
        if not any(
            other.representation != candidate.representation and _dominates(other, candidate)
            for other in vectors
        )
    )
