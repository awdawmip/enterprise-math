"""Minimum equal-mass chain impulse as balanced integer consensus transport.

This E001 specialization generalizes the uniform-closing-score chain result.
No generic majorization/isotonic-regression novelty is claimed.

Assume ``m>=2`` equal-mass bodies in one canonical 1D chain with contact normals
from body ``i`` to ``i+1``.  The initial momenta are non-increasing,

    p_0 >= p_1 >= ... >= p_{m-1},

so every declared contact is closing or already comoving.  A non-negative
contact impulse vector ``j`` acts through the path incidence matrix.  If ``p'``
is the final momentum vector, the first ``k`` body momenta satisfy the exact
prefix-transfer identity

    j_k = sum_{i<k} p_i - sum_{i<k} p'_i,

for ``k=1,...,m-1``.

Requiring all final contacts to be nonclosing is exactly requiring ``p'`` to be
a non-decreasing integer vector with the same total momentum.  Among all such
vectors, the balanced integer consensus vector maximizes every prefix sum:
write

    P = a*m + r,  0 <= r < m,

then

    b = (a,...,a, a+1,...,a+1)

with ``m-r`` copies of ``a`` followed by ``r`` copies of ``a+1``.  Therefore the
prefix transfers from ``p`` to ``b`` are componentwise no larger than those for
any other feasible after-state.  They are the unique componentwise-least
non-negative contact impulse vector.

Consequences:

* if ``r=0``, exact integer comoving consensus is possible;
* if ``r>0``, the minimal final state has exactly one ``+1`` contact score,
  between the low and high momentum plateaus;
* the result depends on the initial profile through prefix mass and total
  momentum, not through a pairwise independent impulse guess.

The theorem is purely about finite integer model coordinates.  It does not
assert kinetic-energy conservation, restitution, continuum force, or physical
uniqueness beyond the declared optimization/order criterion.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_relative_scores,
)


def _require_integer_tuple(name: str, values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    result = tuple(values)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in result):
        raise ValueError(f"{name} entries must be integers")
    return result


def balanced_integer_consensus(
    total_momentum: int,
    body_count: int,
) -> tuple[int, ...]:
    """Return the unique non-decreasing integer vector with range <=1 and given sum."""
    if isinstance(total_momentum, bool) or not isinstance(total_momentum, int):
        raise ValueError("total_momentum must be an integer")
    if isinstance(body_count, bool) or not isinstance(body_count, int) or body_count <= 0:
        raise ValueError("body_count must be a positive integer")
    low, high_count = divmod(total_momentum, body_count)
    return (
        (low,) * (body_count - high_count)
        + (low + 1,) * high_count
    )


def chain_minimum_impulse_from_momenta(
    momenta: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Return the componentwise-least contact impulse for a non-increasing profile."""
    values = _require_integer_tuple("momenta", momenta)
    if len(values) < 2:
        raise ValueError("chain requires at least two bodies")
    if any(left < right for left, right in zip(values, values[1:])):
        raise ValueError("initial momenta must be non-increasing along the chain")

    target = balanced_integer_consensus(sum(values), len(values))
    running_before = 0
    running_after = 0
    impulses: list[int] = []
    for index in range(len(values) - 1):
        running_before += values[index]
        running_after += target[index]
        transfer = running_before - running_after
        if transfer < 0:
            raise AssertionError("non-increasing initial profile failed prefix-majorization")
        impulses.append(transfer)
    return tuple(impulses)


def chain_candidate_is_nonclosing(
    momenta: tuple[int, ...] | list[int],
    impulse_vector: tuple[int, ...] | list[int],
) -> bool:
    """Independent path-incidence feasibility check for bounded regression oracles."""
    values = _require_integer_tuple("momenta", momenta)
    impulses = tuple(impulse_vector)
    if len(values) < 2 or len(impulses) != len(values) - 1:
        raise ValueError("impulse_vector must have one entry per adjacent body pair")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in impulses
    ):
        raise ValueError("impulse entries must be non-negative integers")

    after = [0] * len(values)
    after[0] = values[0] - impulses[0]
    for body in range(1, len(values) - 1):
        after[body] = values[body] + impulses[body - 1] - impulses[body]
    after[-1] = values[-1] + impulses[-1]
    return all(left <= right for left, right in zip(after, after[1:]))


def _validate_equal_mass_chain(state: ContactNetworkMomentum1D) -> None:
    contact_count = len(state.contacts)
    if contact_count < 1 or len(state.masses) != contact_count + 1:
        raise ValueError("chain requires n contacts on n+1 bodies")
    if len(set(state.masses)) != 1:
        raise ValueError("balanced-consensus chain theorem requires equal masses")
    expected_contacts = tuple(
        ContactChannel1D(index, index + 1, 1)
        for index in range(contact_count)
    )
    if state.contacts != expected_contacts:
        raise ValueError("chain theorem requires canonical consecutive +1 contacts")
    scores = contact_relative_scores(state)
    if any(score > 0 for score in scores):
        raise ValueError("initial chain must have no separating contact")


@dataclass(frozen=True)
class ChainConsensusImpulseSolution1D:
    before: ContactNetworkMomentum1D
    impulse_vector: tuple[int, ...]
    minimum_total_impulse: int
    balanced_final_momenta: tuple[int, ...]
    final_scores: tuple[int, ...]
    surplus_contact: int | None
    exact_comoving_consensus: bool


def solve_equal_mass_chain_consensus_impulse(
    state: ContactNetworkMomentum1D,
) -> ChainConsensusImpulseSolution1D:
    """Apply the prefix-majorization minimum impulse to one equal-mass chain."""
    _validate_equal_mass_chain(state)
    impulses = chain_minimum_impulse_from_momenta(state.momenta)
    step = apply_contact_impulse_vector(state, impulses)
    target = balanced_integer_consensus(state.total_momentum, len(state.masses))
    if step.after.momenta != target:
        raise AssertionError("minimum chain impulse failed balanced integer consensus")

    final_scores = step.relative_scores_after
    if any(score < 0 for score in final_scores):
        raise AssertionError("minimum chain impulse left a closing contact")
    nonzero = tuple(index for index, score in enumerate(final_scores) if score != 0)
    if any(score not in (0, 1) for score in final_scores):
        raise AssertionError("balanced consensus produced a contact score outside {0,1}")
    if len(nonzero) > 1:
        raise AssertionError("balanced consensus produced more than one surplus contact")

    remainder = state.total_momentum % len(state.masses)
    if remainder == 0:
        expected_surplus = None
        if nonzero:
            raise AssertionError("divisible total momentum should give exact consensus")
    else:
        low_count = len(state.masses) - remainder
        expected_surplus = low_count - 1
        if nonzero != (expected_surplus,):
            raise AssertionError("surplus contact disagrees with balanced momentum remainder")

    return ChainConsensusImpulseSolution1D(
        before=state,
        impulse_vector=impulses,
        minimum_total_impulse=sum(impulses),
        balanced_final_momenta=target,
        final_scores=final_scores,
        surplus_contact=expected_surplus,
        exact_comoving_consensus=remainder == 0,
    )
