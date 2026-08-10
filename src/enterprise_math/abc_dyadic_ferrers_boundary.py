"""Ferrers/lattice-path duality for the P025 dyadic threshold staircase.

For s ordered thresholds and h+1 dyadic orbit nodes, the activation matrix
B[k,j]=[rho_j>=T_k] has two exact boundary coordinates:

* threshold-centric crossing depths j_k;
* node-centric ranks r_j = number of thresholds reached at node j.

They are dual:

    r_j = # {k : j_k <= j},
    j_k = min {j : r_j >= k},

with infinity/None when threshold k is not reached.

The 1-region is a Ferrers monotone region and its boundary is a lattice path
with s vertical and h+1 horizontal steps.  Its area is both

    sum_j r_j

and

    sum_k (h+1-j_k)_+.

This module records the exact finite duality and boundary encoding.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_dyadic_threshold_staircase import (
    DyadicThresholdStaircase,
    activation_matrix_from_crossings,
)


@dataclass(frozen=True)
class DyadicFerrersBoundary:
    horizon_steps: int
    threshold_count: int
    crossing_depths: tuple[int | None, ...]
    node_ranks: tuple[int, ...]
    activation_matrix: tuple[tuple[bool, ...], ...]
    boundary_word: str
    activation_area: int
    complement_area: int
    crossing_area: int
    rank_area: int
    duality_verified: bool
    area_identity_verified: bool


def node_ranks_from_crossings(
    horizon_steps: int,
    crossing_depths: tuple[int | None, ...],
) -> tuple[int, ...]:
    """Return per-node number of thresholds already reached."""
    matrix = activation_matrix_from_crossings(horizon_steps, crossing_depths)
    if not matrix:
        raise ValueError("crossing_depths must be nonempty")
    ranks = tuple(
        sum(1 for row in matrix if row[column])
        for column in range(horizon_steps + 1)
    )
    if any(right < left for left, right in zip(ranks, ranks[1:])):
        raise AssertionError("node ranks must be nondecreasing along the orbit")
    return ranks


def crossings_from_node_ranks(
    node_ranks: tuple[int, ...], threshold_count: int
) -> tuple[int | None, ...]:
    """Recover threshold crossing depths from nondecreasing node ranks."""
    if not node_ranks:
        raise ValueError("node_ranks must be nonempty")
    if isinstance(threshold_count, bool) or not isinstance(threshold_count, int) or threshold_count < 1:
        raise ValueError("threshold_count must be a positive integer")
    if any(
        isinstance(rank, bool)
        or not isinstance(rank, int)
        or not 0 <= rank <= threshold_count
        for rank in node_ranks
    ):
        raise ValueError("node ranks must lie in 0..threshold_count")
    if any(right < left for left, right in zip(node_ranks, node_ranks[1:])):
        raise ValueError("node ranks must be nondecreasing")
    return tuple(
        next((column for column, rank in enumerate(node_ranks) if rank >= level), None)
        for level in range(1, threshold_count + 1)
    )


def boundary_word_from_node_ranks(
    node_ranks: tuple[int, ...], threshold_count: int
) -> str:
    """Encode ranks as a monotone path with H=node and V=threshold steps."""
    crossings_from_node_ranks(node_ranks, threshold_count)  # validation
    word: list[str] = []
    current = 0
    for rank in node_ranks:
        while current < rank:
            word.append("V")
            current += 1
        word.append("H")
    while current < threshold_count:
        word.append("V")
        current += 1
    result = "".join(word)
    if result.count("H") != len(node_ranks) or result.count("V") != threshold_count:
        raise AssertionError("boundary word lost rectangle dimensions")
    return result


def node_ranks_from_boundary_word(
    boundary_word: str,
    horizon_steps: int,
    threshold_count: int,
) -> tuple[int, ...]:
    """Decode the Ferrers boundary path back to per-node ranks."""
    if set(boundary_word) - {"H", "V"}:
        raise ValueError("boundary_word may contain only H and V")
    if boundary_word.count("H") != horizon_steps + 1:
        raise ValueError("boundary_word has wrong number of H steps")
    if boundary_word.count("V") != threshold_count:
        raise ValueError("boundary_word has wrong number of V steps")
    rank = 0
    ranks: list[int] = []
    for step in boundary_word:
        if step == "V":
            rank += 1
        else:
            ranks.append(rank)
    result = tuple(ranks)
    crossings_from_node_ranks(result, threshold_count)  # monotonic/range validation
    return result


def ferrers_boundary_from_staircase(
    staircase: DyadicThresholdStaircase,
) -> DyadicFerrersBoundary:
    """Return the exact dual coordinates, lattice path and area identity."""
    h = staircase.horizon_steps
    s = len(staircase.thresholds)
    crossings = staircase.crossing_depths
    ranks = node_ranks_from_crossings(h, crossings)
    recovered = crossings_from_node_ranks(ranks, s)
    if recovered != crossings:
        raise AssertionError("rank/crossing duality failed")

    word = boundary_word_from_node_ranks(ranks, s)
    decoded = node_ranks_from_boundary_word(word, h, s)
    if decoded != ranks:
        raise AssertionError("lattice-path boundary failed to recover node ranks")

    rank_area = sum(ranks)
    crossing_area = sum(
        0 if depth is None else (h + 1 - depth)
        for depth in crossings
    )
    if rank_area != crossing_area:
        raise AssertionError("Ferrers area double-count identity failed")
    total = s * (h + 1)
    return DyadicFerrersBoundary(
        horizon_steps=h,
        threshold_count=s,
        crossing_depths=crossings,
        node_ranks=ranks,
        activation_matrix=staircase.activation_matrix,
        boundary_word=word,
        activation_area=rank_area,
        complement_area=total - rank_area,
        crossing_area=crossing_area,
        rank_area=rank_area,
        duality_verified=True,
        area_identity_verified=True,
    )
