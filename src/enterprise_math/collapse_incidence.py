"""E001.2/E001.3 collapse-target incidence algebra.

Let M[z, b] be one exactly finite 0/1 relation: terminal collapse target ``z``
is reachable by body ``b``.  Then the natural-number Gram product ``M^T M``
has off-diagonal entry equal to the number of shared terminal collapse targets
for a body pair.  Boolean nonzero support is therefore the exact collision
graph for the E001 target semantics.

The same inverted relation gives a k-body overlap spectrum.  If ``c_z`` is the
number of bodies incident to target ``z``, then

    W_k = sum_z binom(c_z, k).

Adding one new body with target set S changes the spectrum by the exact Pascal
increment

    Delta W_k = sum_(z in S) binom(c_z, k-1),

where ``c_z`` is the occupancy before insertion.  Thus higher shared-target
witness counts can be maintained incrementally with integer arithmetic rather
than recomputed from all body subsets.

The spectrum counts witnesses, not necessarily distinct body groups: one group
can contribute at several shared targets.  This module does not identify these
counts with force, energy, probability, or thermodynamic entropy.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from itertools import combinations
from math import comb

from .common_collapse import iter_terminal_collapse_targets
from .engineering_collision import Body2D, Pair

Target2D = tuple[int, int]


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


def overlap_spectrum_from_occupancies(
    occupancies: Mapping[Target2D, int], max_order: int | None = None
) -> tuple[tuple[int, int], ...]:
    """Return W_k=sum_z binom(c_z,k) from non-negative integer occupancies."""
    if any(
        isinstance(count, bool) or not isinstance(count, int) or count < 0
        for count in occupancies.values()
    ):
        raise ValueError("target occupancies must be non-negative integers")
    observed_max = max(occupancies.values(), default=0)
    if max_order is None:
        max_order = observed_max
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 0:
        raise ValueError("max_order must be a non-negative integer")
    return tuple(
        (
            order,
            sum(comb(count, order) for count in occupancies.values() if count >= order),
        )
        for order in range(2, max_order + 1)
    )


def insertion_spectrum_delta(
    occupancies: Mapping[Target2D, int],
    new_targets: Iterable[Target2D],
    max_order: int | None = None,
) -> tuple[tuple[int, int], ...]:
    """Exact Pascal-law change in W_k caused by inserting one target-set body."""
    targets = tuple(new_targets)
    if len(targets) != len(set(targets)):
        raise ValueError("one body may be incident to each target at most once")
    if any(
        isinstance(count, bool) or not isinstance(count, int) or count < 0
        for count in occupancies.values()
    ):
        raise ValueError("target occupancies must be non-negative integers")
    future_max = max((occupancies.get(target, 0) + 1 for target in targets), default=0)
    if max_order is None:
        max_order = future_max
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 0:
        raise ValueError("max_order must be a non-negative integer")
    return tuple(
        (
            order,
            sum(
                comb(occupancies.get(target, 0), order - 1)
                for target in targets
                if occupancies.get(target, 0) >= order - 1
            ),
        )
        for order in range(2, max_order + 1)
    )


def collapse_incidence_report(bodies: list[Body2D]) -> CollapseIncidenceReport:
    """Build the exact terminal incidence relation and its overlap spectrum."""
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")

    by_target: dict[Target2D, list[int]] = {}
    emitted_memberships = 0
    for body in sorted(bodies):
        for target in iter_terminal_collapse_targets(body):
            by_target.setdefault(target, []).append(body.body_id)
            emitted_memberships += 1

    pair_counts: Counter[Pair] = Counter()
    occupancies: dict[Target2D, int] = {}
    max_occupancy = 0
    for target, occupants in by_target.items():
        occupancy = len(occupants)
        occupancies[target] = occupancy
        max_occupancy = max(max_occupancy, occupancy)
        if occupancy < 2:
            continue
        for left_id, right_id in combinations(occupants, 2):
            pair_counts[(left_id, right_id)] += 1

    spectrum = overlap_spectrum_from_occupancies(occupancies)
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
