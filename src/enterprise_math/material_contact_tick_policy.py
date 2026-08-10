"""Exact policy comparator for batched versus guarded contact impulse application.

The material-contact tick first quantizes every named contact-local reservoir and
produces one nonnegative delivered impulse vector ``J``.  Batched application
updates the network by the total additive increment ``K J``.

A different world law may insist that the same delivered quanta are applied one
unit at a time, with contact ``i`` legal only while its current relative score is
negative.  Since additive score/body increments commute, every guarded word with
count vector ``J`` reaches the same final additive state as the batch.  The
policy difference is therefore exactly the finite causal question

    does there exist a legal guarded word with count vector J?

For initial score ``r``, coupling ``K`` and prefix count vector ``n``, the exact
prefix score is

    r(n) = r + K n.

So guarded realizability is finite reachability on the integer box
``0 <= n_i <= J_i``.

If every off-diagonal coupling is nonpositive, any currently enabled remaining
action can be moved to the front of any legal completion: actions originally
before it can only make its own guard more negative, while moving it earlier can
only make their guards more negative.  Therefore, on a Z-coupled system:

* if one guarded realization exists, every greedy scheduler that repeatedly
  chooses any currently enabled remaining contact succeeds;
* if such a greedy scheduler gets stuck, no guarded realization exists.

For diagonal coupling, contacts are independent.  Before the ``k``-th unit on
contact ``i`` its score is ``r_i + K_ii*k`` for ``k=0,...,J_i-1``.  An arithmetic
progression is negative throughout iff its maximum endpoint is negative, so the
exact coordinate criterion is

    J_i=0
    or max(r_i, r_i + K_ii*(J_i-1)) < 0.

For the usual contact Gram the diagonal is positive and this reduces to the last
pre-action score test.  The endpoint form remains correct for arbitrary integer
diagonal matrices and avoids a hidden sign assumption.

Positive cross-coupling can make a valid batched vector causally unrealizable.
For the equal-mass q=1 three-leaf star, ``r=(-1,-1,-1)`` and ``K`` has diagonal
2/off-diagonal 1.  Batch ``J=(1,1,1)`` is algebraically valid, but any first unit
raises the other two scores to zero, so no sequential guarded word realizes the
remaining units.

Finite reachability and the Z-matrix exchange argument are standard.  The E001
value is the exact world-policy boundary after material quantization.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import prod
from typing import Callable, Sequence

from .material_contact_network_impulse_1d import (
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_contact_network_tick_1d import ContactMaterialNetworkTick1D


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _integer_vector(
    values: Sequence[int],
    *,
    name: str,
    nonnegative: bool = False,
) -> Vector:
    result = tuple(values)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    for value in result:
        _require_int(name, value)
        if nonnegative and value < 0:
            raise ValueError(f"{name} entries must be nonnegative")
    return result


def _square_integer_matrix(
    values: Sequence[Sequence[int]],
    dimension: int,
) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if len(rows) != dimension or any(len(row) != dimension for row in rows):
        raise ValueError("coupling matrix must match score dimension")
    for row in rows:
        for value in row:
            _require_int("coupling entry", value)
    return rows


def score_after_counts(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    counts: Sequence[int],
) -> Vector:
    """Return exact contact scores after an unguarded prefix-count vector."""
    scores = _integer_vector(initial_scores, name="initial_scores")
    matrix = _square_integer_matrix(coupling, len(scores))
    prefix = _integer_vector(counts, name="counts", nonnegative=True)
    if len(prefix) != len(scores):
        raise ValueError("counts must match score dimension")
    return tuple(
        scores[row]
        + sum(
            matrix[row][column] * prefix[column]
            for column in range(len(scores))
        )
        for row in range(len(scores))
    )


def enabled_remaining_contacts(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    prefix_counts: Sequence[int],
    target_counts: Sequence[int],
) -> tuple[int, ...]:
    """Remaining target actions whose current local closing guard is true."""
    scores = _integer_vector(initial_scores, name="initial_scores")
    matrix = _square_integer_matrix(coupling, len(scores))
    prefix = _integer_vector(
        prefix_counts,
        name="prefix_counts",
        nonnegative=True,
    )
    target = _integer_vector(
        target_counts,
        name="target_counts",
        nonnegative=True,
    )
    if len(prefix) != len(scores) or len(target) != len(scores):
        raise ValueError("count vectors must match score dimension")
    if any(used > required for used, required in zip(prefix, target, strict=True)):
        raise ValueError("prefix counts cannot exceed target counts")
    current = score_after_counts(scores, matrix, prefix)
    return tuple(
        index
        for index, (used, required) in enumerate(
            zip(prefix, target, strict=True)
        )
        if used < required and current[index] < 0
    )


def coupling_is_z_matrix(coupling: Sequence[Sequence[int]]) -> bool:
    rows = tuple(tuple(row) for row in coupling)
    if not rows:
        raise ValueError("coupling matrix must be nonempty")
    matrix = _square_integer_matrix(rows, len(rows))
    return all(
        row == column or matrix[row][column] <= 0
        for row in range(len(matrix))
        for column in range(len(matrix))
    )


def coupling_is_diagonal(coupling: Sequence[Sequence[int]]) -> bool:
    rows = tuple(tuple(row) for row in coupling)
    if not rows:
        raise ValueError("coupling matrix must be nonempty")
    matrix = _square_integer_matrix(rows, len(rows))
    return all(
        row == column or matrix[row][column] == 0
        for row in range(len(matrix))
        for column in range(len(matrix))
    )


@dataclass(frozen=True)
class GuardedImpulseRealization:
    target_counts: Vector
    realizable: bool
    word: tuple[int, ...] | None
    visited_count_states: int
    total_count_states: int

    @property
    def delivered_total(self) -> int:
        return sum(self.target_counts)


def exact_guarded_impulse_realization(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> GuardedImpulseRealization:
    """Exact BFS on the finite prefix-count lattice."""
    scores = _integer_vector(initial_scores, name="initial_scores")
    matrix = _square_integer_matrix(coupling, len(scores))
    target = _integer_vector(
        target_counts,
        name="target_counts",
        nonnegative=True,
    )
    if len(target) != len(scores):
        raise ValueError("target_counts must match score dimension")

    zero = (0,) * len(target)
    total_states = prod(value + 1 for value in target)
    queue: deque[Vector] = deque([zero])
    predecessor: dict[Vector, tuple[Vector, int] | None] = {zero: None}

    while queue:
        prefix = queue.popleft()
        if prefix == target:
            word: list[int] = []
            current = prefix
            while predecessor[current] is not None:
                previous, action = predecessor[current]
                word.append(action)
                current = previous
            word.reverse()
            return GuardedImpulseRealization(
                target_counts=target,
                realizable=True,
                word=tuple(word),
                visited_count_states=len(predecessor),
                total_count_states=total_states,
            )

        for action in enabled_remaining_contacts(scores, matrix, prefix, target):
            nxt = tuple(
                value + (1 if index == action else 0)
                for index, value in enumerate(prefix)
            )
            if nxt in predecessor:
                continue
            predecessor[nxt] = (prefix, action)
            queue.append(nxt)

    return GuardedImpulseRealization(
        target_counts=target,
        realizable=False,
        word=None,
        visited_count_states=len(predecessor),
        total_count_states=total_states,
    )


def _lowest_enabled(enabled: tuple[int, ...], _: Vector) -> int:
    return enabled[0]


def _highest_enabled(enabled: tuple[int, ...], _: Vector) -> int:
    return enabled[-1]


def _least_used_enabled(enabled: tuple[int, ...], counts: Vector) -> int:
    return min(enabled, key=lambda index: (counts[index], index))


GREEDY_CHOOSERS: dict[str, Callable[[tuple[int, ...], Vector], int]] = {
    "LOWEST": _lowest_enabled,
    "HIGHEST": _highest_enabled,
    "LEAST_USED": _least_used_enabled,
}


@dataclass(frozen=True)
class ZGreedyGuardedRealization:
    target_counts: Vector
    policy: str
    realizable: bool
    word: tuple[int, ...] | None
    stuck_prefix_counts: Vector | None
    stuck_scores: Vector | None


def z_greedy_guarded_realization(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
    *,
    policy: str = "LOWEST",
) -> ZGreedyGuardedRealization:
    """Arbitrary-choice greedy decision procedure for Z-coupled systems."""
    scores = _integer_vector(initial_scores, name="initial_scores")
    matrix = _square_integer_matrix(coupling, len(scores))
    target = _integer_vector(
        target_counts,
        name="target_counts",
        nonnegative=True,
    )
    if len(target) != len(scores):
        raise ValueError("target_counts must match score dimension")
    if not coupling_is_z_matrix(matrix):
        raise ValueError("Z-greedy theorem requires nonpositive off-diagonal coupling")
    if policy not in GREEDY_CHOOSERS:
        raise ValueError("unknown greedy policy")

    chooser = GREEDY_CHOOSERS[policy]
    counts: Vector = (0,) * len(target)
    word: list[int] = []
    while counts != target:
        enabled = enabled_remaining_contacts(scores, matrix, counts, target)
        if not enabled:
            return ZGreedyGuardedRealization(
                target_counts=target,
                policy=policy,
                realizable=False,
                word=None,
                stuck_prefix_counts=counts,
                stuck_scores=score_after_counts(scores, matrix, counts),
            )
        action = chooser(enabled, counts)
        counts = tuple(
            value + (1 if index == action else 0)
            for index, value in enumerate(counts)
        )
        word.append(action)

    return ZGreedyGuardedRealization(
        target_counts=target,
        policy=policy,
        realizable=True,
        word=tuple(word),
        stuck_prefix_counts=None,
        stuck_scores=None,
    )


def diagonal_guarded_realizable_closed_form(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> bool:
    """Exact independent-contact criterion for arbitrary integer diagonal coupling."""
    scores = _integer_vector(initial_scores, name="initial_scores")
    matrix = _square_integer_matrix(coupling, len(scores))
    target = _integer_vector(
        target_counts,
        name="target_counts",
        nonnegative=True,
    )
    if len(target) != len(scores):
        raise ValueError("target_counts must match score dimension")
    if not coupling_is_diagonal(matrix):
        raise ValueError("closed form requires diagonal coupling")

    return all(
        count == 0
        or max(
            scores[index],
            scores[index] + matrix[index][index] * (count - 1),
        )
        < 0
        for index, count in enumerate(target)
    )


@dataclass(frozen=True)
class BatchedGuardedTickPolicyReport:
    delivered_impulse_vector: Vector
    initial_scores: Vector
    coupling_gram: Matrix
    guarded_realizable: bool
    guarded_word: tuple[int, ...] | None
    batch_after_matches_guarded_after: bool | None
    z_coupled: bool

    @property
    def batch_is_causally_realizable(self) -> bool:
        return self.guarded_realizable


def compare_batched_tick_to_guarded_sequential(
    tick: ContactMaterialNetworkTick1D,
) -> BatchedGuardedTickPolicyReport:
    """Check whether one already-quantized batch vector has a guarded realization."""
    if not isinstance(tick, ContactMaterialNetworkTick1D):
        raise TypeError("tick must be ContactMaterialNetworkTick1D")
    initial_scores = contact_relative_scores(tick.before)
    gram = contact_coupling_gram(tick.before)
    delivered = tick.delivered_impulse_vector
    exact = exact_guarded_impulse_realization(initial_scores, gram, delivered)

    matches: bool | None = None
    if exact.realizable:
        batch_step = apply_contact_impulse_vector(tick.before, delivered)
        if batch_step.after != tick.after:
            raise AssertionError(
                "material batch after-state disagreed with delivered vector"
            )
        # Any legal guarded word with this count vector has the same additive
        # body/contact-score after-state because additions depend only on counts.
        matches = True

    return BatchedGuardedTickPolicyReport(
        delivered_impulse_vector=delivered,
        initial_scores=initial_scores,
        coupling_gram=gram,
        guarded_realizable=exact.realizable,
        guarded_word=exact.word,
        batch_after_matches_guarded_after=matches,
        z_coupled=coupling_is_z_matrix(gram),
    )
