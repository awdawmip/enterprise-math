"""Order-robustness layers for an already-quantized contact impulse target.

A material-contact tick produces one nonnegative delivered count vector ``J``.
There are then several distinct causal claims:

1. **BATCHED**: apply the additive vector ``J`` without intermediate guards;
2. **SOME_GUARDED_ORDER**: at least one unit-action permutation of ``J`` is legal;
3. **Z_GREEDY_ROBUST**: for nonpositive off-diagonal coupling, every scheduler
   that repeatedly chooses any *currently enabled* remaining action succeeds
   whenever a completion exists;
4. **EVERY_PERMUTATION**: every literal multiset permutation of ``J`` is legal,
   even those that do not consult enabledness before choosing the next action.

The last property has a closed form.  Before an action ``i`` executes, its own
prior count ranges from ``0`` to ``J_i-1`` and every other prior count ranges
from ``0`` to ``J_j``.  Therefore the largest score that contact ``i`` can have
before one of its required actions, over all literal permutations, is

    W_i = r_i
          + max(0, K_ii*(J_i-1))
          + sum_(j!=i) J_j * max(0, K_ij).

Every target permutation is guarded-legal iff ``W_i<0`` for every contact with
``J_i>0``.  This criterion is exact for arbitrary integer coupling matrices; it
is not restricted to contact Gram signs.

This also exposes a useful nonmonotonicity.  Negative cross-coupling can enable
a required contact that is initially disabled, so a larger coupled target may
be realizable while one of its componentwise smaller subvectors is not.  Yet
additional self/cross impulse can later destroy realizability.  Guarded target
realizability is therefore neither a componentwise lower set nor an upper set.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .material_contact_network_impulse_1d import (
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_contact_network_tick_1d import ContactMaterialNetworkTick1D
from .material_contact_tick_policy import (
    GREEDY_CHOOSERS,
    coupling_is_z_matrix,
    exact_guarded_impulse_realization,
    z_greedy_guarded_realization,
)


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _normalize(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> tuple[Vector, Matrix, Vector]:
    scores = tuple(initial_scores)
    target = tuple(target_counts)
    if not scores:
        raise ValueError("initial_scores must be nonempty")
    if len(target) != len(scores):
        raise ValueError("target_counts must match score dimension")
    for value in scores:
        _require_int("initial score", value)
    for value in target:
        _require_int("target count", value)
        if value < 0:
            raise ValueError("target counts must be nonnegative")
    matrix = tuple(tuple(row) for row in coupling)
    if len(matrix) != len(scores) or any(
        len(row) != len(scores) for row in matrix
    ):
        raise ValueError("coupling matrix must match score dimension")
    for row in matrix:
        for value in row:
            _require_int("coupling entry", value)
    return scores, matrix, target


def worst_preaction_scores(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> tuple[int | None, ...]:
    """Maximum possible pre-action score for each required contact."""
    scores, matrix, target = _normalize(
        initial_scores,
        coupling,
        target_counts,
    )
    result: list[int | None] = []
    for index, count in enumerate(target):
        if count == 0:
            result.append(None)
            continue
        worst = scores[index] + max(
            0,
            matrix[index][index] * (count - 1),
        )
        worst += sum(
            target[other] * max(0, matrix[index][other])
            for other in range(len(target))
            if other != index
        )
        result.append(worst)
    return tuple(result)


def every_target_permutation_is_guarded(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> bool:
    """Exact iff criterion for legality of every multiset permutation."""
    worst = worst_preaction_scores(
        initial_scores,
        coupling,
        target_counts,
    )
    return all(value is None or value < 0 for value in worst)


def negative_cross_enable_band(
    target_score_before: int,
    cross_coupling: int,
) -> bool:
    """Whether one negative cross update enables an initially disabled target."""
    _require_int("target_score_before", target_score_before)
    _require_int("cross_coupling", cross_coupling)
    return (
        cross_coupling < 0
        and 0 <= target_score_before < -cross_coupling
    )


@dataclass(frozen=True)
class TargetOrderRobustnessReport:
    target_counts: Vector
    some_guarded_order: bool
    every_permutation_guarded: bool
    worst_preaction_scores: tuple[int | None, ...]
    z_coupled: bool
    z_greedy_policy_results: tuple[tuple[str, bool], ...]

    @property
    def batched_only(self) -> bool:
        return not self.some_guarded_order

    @property
    def schedule_exists_but_not_order_robust(self) -> bool:
        return self.some_guarded_order and not self.every_permutation_guarded


def target_order_robustness_report(
    initial_scores: Sequence[int],
    coupling: Sequence[Sequence[int]],
    target_counts: Sequence[int],
) -> TargetOrderRobustnessReport:
    scores, matrix, target = _normalize(
        initial_scores,
        coupling,
        target_counts,
    )
    exact = exact_guarded_impulse_realization(scores, matrix, target)
    all_orders = every_target_permutation_is_guarded(scores, matrix, target)
    if all_orders and not exact.realizable:
        raise AssertionError("all-order legality failed to imply existence")

    z_coupled = coupling_is_z_matrix(matrix)
    greedy_results: list[tuple[str, bool]] = []
    if z_coupled:
        for policy in GREEDY_CHOOSERS:
            result = z_greedy_guarded_realization(
                scores,
                matrix,
                target,
                policy=policy,
            )
            if result.realizable != exact.realizable:
                raise AssertionError("Z-greedy policy disagreed with exact realization")
            greedy_results.append((policy, result.realizable))

    return TargetOrderRobustnessReport(
        target_counts=target,
        some_guarded_order=exact.realizable,
        every_permutation_guarded=all_orders,
        worst_preaction_scores=worst_preaction_scores(scores, matrix, target),
        z_coupled=z_coupled,
        z_greedy_policy_results=tuple(greedy_results),
    )


def material_tick_order_robustness(
    tick: ContactMaterialNetworkTick1D,
) -> TargetOrderRobustnessReport:
    """Compile order robustness for one already-quantized material tick."""
    if not isinstance(tick, ContactMaterialNetworkTick1D):
        raise TypeError("tick must be ContactMaterialNetworkTick1D")
    return target_order_robustness_report(
        contact_relative_scores(tick.before),
        contact_coupling_gram(tick.before),
        tick.delivered_impulse_vector,
    )
