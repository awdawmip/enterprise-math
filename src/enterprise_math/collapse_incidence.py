"""E001.2 collapse-target incidence algebra.

Let M[z, b] be one exactly finite 0/1 relation: terminal collapse target ``z``
is reachable by body ``b``.  Then the natural-number Gram product ``M^T M``
has off-diagonal entry equal to the number of shared terminal collapse targets
for a body pair.  Boolean nonzero support is therefore the exact collision
graph for the E001 target semantics.

The same inverted relation also gives a k-body overlap spectrum.  If ``c_z`` is
the number of bodies incident to target ``z``, then

    W_k = sum_z binom(c_z, k)

counts shared-target witnesses for unordered k-body groups.  This module keeps
that statement purely finite and integer-valued; it does not identify the
spectrum with force, energy, probability, or thermodynamic entropy.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from math import comb

from .common_collapse import iter_terminal_collapse_targets
from .engineering_collision import Body2D, Pair


@dataclass(frozen=True)
class CollapseIncidenceReport:
    """Exact finite statistics of the body-to-collapse-target incidence relation."""

    body_count: int
    emitted_memberships: int
    occupied_targets: int
    max_target_occupancy: int
    collision_pairs: tuple[Pair, ...]
    pair_multiplicities: tuple[tuple[Pair, int], ...]
    overlap_spectrum: tuple[tuple[int, int], ...]


def collapse_incidence_report(bodies: list[Body2D]) -> CollapseIncidenceReport:
    """Build the exact terminal incidence relation and its overlap spectrum."""
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")

    by_target: dict[tuple[int, int], list[int]] = {}
    emitted_memberships = 0
    for body in sorted(bodies):
        for target in iter_terminal_collapse_targets(body):
            by_target.setdefault(target, []).append(body.body_id)
            emitted_memberships += 1

    pair_counts: Counter[Pair] = Counter()
    max_occupancy = 0
    occupancy_counts: list[int] = []
    for occupants in by_target.values():
        occupancy = len(occupants)
        occupancy_counts.append(occupancy)
        max_occupancy = max(max_occupancy, occupancy)
        if occupancy < 2:
            continue
        for left_id, right_id in combinations(occupants, 2):
            pair_counts[(left_id, right_id)] += 1

    spectrum = tuple(
        (
            order,
            sum(comb(occupancy, order) for occupancy in occupancy_counts if occupancy >= order),
        )
        for order in range(2, max_occupancy + 1)
    )
    if spectrum:
        pair_witness_total = sum(pair_counts.values())
        if spectrum[0][0] != 2 or spectrum[0][1] != pair_witness_total:
            raise AssertionError("second-order collapse spectrum failed double-count identity")

    pair_multiplicities = tuple(sorted(pair_counts.items()))
    return CollapseIncidenceReport(
        body_count=len(bodies),
        emitted_memberships=emitted_memberships,
        occupied_targets=len(by_target),
        max_target_occupancy=max_occupancy,
        collision_pairs=tuple(pair for pair, _count in pair_multiplicities),
        pair_multiplicities=pair_multiplicities,
        overlap_spectrum=spectrum,
    )
