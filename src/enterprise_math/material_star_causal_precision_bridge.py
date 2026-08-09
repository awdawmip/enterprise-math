"""Precision/action-language bridge for the E001 branching star.

This thin bridge consumes two existing owners without re-owning either theorem:

* ``material_star_response_precision_phase``: static minimum relation at impulse
  denominator ``s``;
* ``material_star_local_action_language``: causal reachability when one local
  numerator quantum is delivered only to a currently closing contact.

At physical closing quantum ``q`` and impulse denominator ``s``, the local
numerator action language sees the scaled integer closing demand

    Q = q*s.

Therefore the causal theorem applies directly to the static precision relation
at ``Q``.  In particular, the *entire* static minimum relation is locally
reachable exactly when

    Q = 1    or    Q >= k+1.

For ``q=1`` this gives a non-monotone coverage story under genuine divisibility
refinement:

* ``s=1``: every static minimum is causal;
* ``2 <= s <= k``: the finer static minimum relation contains causally
  unreachable members;
* ``s >= k+1``: every static minimum is causal again.

The causal coverage gap and the static optimum are different observables.  For
``q=1`` and every ``1<=s<=k``, *all* legal local schedules have numerator total
exactly ``s`` and hence physical total impulse exactly one.  This follows from

    static minimum total = Q = s

in this range together with the causal word-length bound ``S<=Q``.

At the first denominator ``s=k+1`` the situation changes sharply.  The static
minimum becomes the unique symmetric numerator vector

    (1,...,1)

of total ``k``, i.e. physical impulse ``k/(k+1)``.  A balanced legal word that
updates each contact once reaches this optimum.  But the equally legal word

    0,0,1,2,...,k-1

reaches ``(2,1,...,1)`` of numerator total ``k+1``, i.e. physical impulse one.
Thus ``s=k+1`` is the first precision at which local schedule selection can
change the *physical total response* for the q=1 star.

This produces a useful three-layer separation:

1. at ``s=k`` a symmetric static minimum exists and is causally reachable, but
   the full static minimum relation is not causally reachable;
2. at ``s=k+1`` the static minimum relation is unique;
3. nevertheless the local causal operation language still has a nonminimum
   terminal branch unless a scheduler/simultaneity law is declared.

So increasing precision can expose a lower-resource causal path without making
that path the unique causal dynamics.  Precision, static optimization and
causal selection are separate world-law coordinates.

All arithmetic here is exact finite lattice arithmetic.  No continuum force,
restitution, energy law, hidden substeps, or claim that a particular scheduler
is physical is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .material_star_local_action_language import (
    star_replay_local_contact_word,
    star_run_local_unit_policy,
    star_terminal_is_causally_reachable,
)
from .material_star_response_precision_phase import (
    star_minimum_response_relation_at_precision,
    star_response_refinement_phase,
    star_symmetric_minimum_numerators,
)


def _require_leaf_count(leaf_count: int) -> None:
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def star_precision_causal_minimum_relation(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[tuple[int, ...], ...]:
    """Filter the static minimum numerator relation by local causal reachability."""
    _require_leaf_count(leaf_count)
    _require_positive("closing_quantum", closing_quantum)
    _require_positive("denominator", denominator)
    scaled_closing = closing_quantum * denominator
    relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, denominator
    )
    return tuple(
        vector
        for vector in relation
        if star_terminal_is_causally_reachable(vector, scaled_closing)
    )


def star_precision_minimum_relation_is_fully_causal(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> bool:
    """Return the exact ``Q=1 or Q>=k+1`` causal-coverage criterion."""
    _require_leaf_count(leaf_count)
    _require_positive("closing_quantum", closing_quantum)
    _require_positive("denominator", denominator)
    scaled_closing = closing_quantum * denominator
    predicted = scaled_closing == 1 or scaled_closing >= leaf_count + 1
    relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, denominator
    )
    actual = len(
        star_precision_causal_minimum_relation(
            leaf_count, closing_quantum, denominator
        )
    ) == len(relation)
    if predicted != actual:
        raise AssertionError("precision causal-coverage formula disagrees with relation filter")
    return predicted


def star_q1_first_schedule_divergence_denominator(leaf_count: int) -> int:
    """Return the first q=1 denominator where legal schedules can change total response."""
    _require_leaf_count(leaf_count)
    return leaf_count + 1


@dataclass(frozen=True)
class StarQ1ScheduleBranchCertificate:
    leaf_count: int
    denominator: int
    balanced_word: tuple[int, ...]
    balanced_terminal: tuple[int, ...]
    concentrated_word: tuple[int, ...]
    concentrated_terminal: tuple[int, ...]

    @property
    def balanced_physical_total(self) -> Fraction:
        return Fraction(sum(self.balanced_terminal), self.denominator)

    @property
    def concentrated_physical_total(self) -> Fraction:
        return Fraction(sum(self.concentrated_terminal), self.denominator)


def star_q1_first_schedule_branch_certificate(
    leaf_count: int,
) -> StarQ1ScheduleBranchCertificate:
    """Construct the two exact legal branches at ``s=k+1``."""
    _require_leaf_count(leaf_count)
    denominator = leaf_count + 1
    balanced_word = tuple(range(leaf_count))
    concentrated_word = (0, 0) + tuple(range(1, leaf_count))
    balanced = star_replay_local_contact_word(
        leaf_count, denominator, balanced_word
    )
    concentrated = star_replay_local_contact_word(
        leaf_count, denominator, concentrated_word
    )
    expected_balanced = (1,) * leaf_count
    expected_concentrated = (2,) + (1,) * (leaf_count - 1)
    if balanced != expected_balanced:
        raise AssertionError("balanced q=1 precision branch lost unique minimum response")
    if concentrated != expected_concentrated:
        raise AssertionError("concentrated q=1 precision branch lost overdelivery witness")
    return StarQ1ScheduleBranchCertificate(
        leaf_count=leaf_count,
        denominator=denominator,
        balanced_word=balanced_word,
        balanced_terminal=balanced,
        concentrated_word=concentrated_word,
        concentrated_terminal=concentrated,
    )


@dataclass(frozen=True)
class StarPrecisionCausalReport:
    leaf_count: int
    closing_quantum: int
    denominator: int
    scaled_closing: int
    static_minimum_total_numerator: int
    static_minimum_count: int
    causal_minimum_count: int
    static_minimum_unique: bool
    full_static_minimum_relation_is_causal: bool
    symmetric_static_minimum_exists: bool
    symmetric_static_minimum_is_causal: bool
    lowest_index_terminal_numerator_total: int
    least_used_terminal_numerator_total: int

    @property
    def lowest_index_physical_total(self) -> Fraction:
        return Fraction(self.lowest_index_terminal_numerator_total, self.denominator)

    @property
    def least_used_physical_total(self) -> Fraction:
        return Fraction(self.least_used_terminal_numerator_total, self.denominator)

    @property
    def sampled_policy_total_diverges(self) -> bool:
        return (
            self.lowest_index_terminal_numerator_total
            != self.least_used_terminal_numerator_total
        )


def star_precision_causal_report(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> StarPrecisionCausalReport:
    """Combine static precision and local causal response without choosing a law."""
    _require_leaf_count(leaf_count)
    _require_positive("closing_quantum", closing_quantum)
    _require_positive("denominator", denominator)
    phase = star_response_refinement_phase(
        leaf_count, closing_quantum, denominator
    )
    static_relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, denominator
    )
    causal_relation = star_precision_causal_minimum_relation(
        leaf_count, closing_quantum, denominator
    )
    scaled_closing = closing_quantum * denominator
    symmetric = star_symmetric_minimum_numerators(
        leaf_count, closing_quantum, denominator
    )
    lowest = star_run_local_unit_policy(
        leaf_count, scaled_closing, "LOWEST_INDEX"
    )
    balanced = star_run_local_unit_policy(
        leaf_count, scaled_closing, "LEAST_USED"
    )
    return StarPrecisionCausalReport(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        denominator=denominator,
        scaled_closing=scaled_closing,
        static_minimum_total_numerator=phase.minimum_total_numerator,
        static_minimum_count=len(static_relation),
        causal_minimum_count=len(causal_relation),
        static_minimum_unique=len(static_relation) == 1,
        full_static_minimum_relation_is_causal=(
            len(causal_relation) == len(static_relation)
        ),
        symmetric_static_minimum_exists=symmetric is not None,
        symmetric_static_minimum_is_causal=(
            symmetric is not None
            and star_terminal_is_causally_reachable(
                symmetric, scaled_closing
            )
        ),
        lowest_index_terminal_numerator_total=lowest.delivered_total,
        least_used_terminal_numerator_total=balanced.delivered_total,
    )
