"""Schedule-independent least-action solver for an unequal-mass 1D contact chain.

This E001 owner consumes the declared contact-network coupling from
``material_contact_network_impulse_1d``.  It does not claim a new generic
M-matrix/Z-matrix/chip-firing theorem.

Assume a canonical path of ``n>=1`` contacts on ``n+1`` bodies:

* body masses are arbitrary positive integers;
* contact ``i`` joins bodies ``i`` and ``i+1`` with normal ``+1``;
* the initial contact score vector ``r=B^T D p`` is componentwise non-positive
  (every declared contact is closing or comoving).

For ``L=lcm_i(m_i)`` and ``D_i=L/m_i``, the path coupling is

    K_ii     = D_i + D_{i+1},
    K_i,i-1 = -D_i,
    K_i,i+1 = -D_{i+1}.

Thus ``K`` has positive diagonal and non-positive off-diagonal entries.  We seek
non-negative integer delivered impulses ``j`` satisfying

    r + K j >= 0.

Two finite facts give an exact least-action algorithm.

1. Explicit feasible upper witness.
   Choose the least integer ``T>=0`` such that for every body prefix

       P_k + T M_k >= 0,

   including the full component, where ``P_k`` and ``M_k`` are prefix momentum
   and prefix mass.  Set

       U_k = P_k + T M_k,    k=1,...,n.

   These are the contact prefix transfers from the initial state to a final
   state with the first ``n`` body momenta ``-T*m_i`` and the last body carrying
   the remaining conserved total.  The resulting scaled velocities are
   non-decreasing, so ``U`` is a feasible non-negative impulse vector.

2. Least-action update.
   Start at ``j=0``.  Repeatedly choose *any* currently violated contact
   ``i`` (score ``<0``) and replace ``j_i`` by ``j_i+1``.  Suppose the current
   vector is componentwise below any feasible vector ``v``.  If ``j_i=v_i``,
   then the non-positive off-diagonal entries imply the current score at ``i``
   is at least the feasible score at ``v``, contradicting violation.  Hence
   every chosen coordinate is strictly below every feasible vector before the
   increment.  The iteration therefore stays below every feasible vector and,
   in particular, below ``U``.  It terminates after at most ``sum(U)`` unit
   increments and returns the unique componentwise-least feasible impulse.

Consequently the result is independent of the order in which violated contacts
are processed.  This schedule-independence is a property of this aligned path
Z-coupling specialization; it is not claimed for arbitrary contact networks,
whose Gram matrices can have positive off-diagonal entries.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)


def _ceil_div_nonnegative(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    if numerator <= 0:
        return 0
    return (numerator + denominator - 1) // denominator


def _validate_weighted_chain(state: ContactNetworkMomentum1D) -> None:
    contact_count = len(state.contacts)
    if contact_count < 1 or len(state.masses) != contact_count + 1:
        raise ValueError("weighted chain requires n contacts on n+1 bodies")
    expected = tuple(
        ContactChannel1D(index, index + 1, 1)
        for index in range(contact_count)
    )
    if state.contacts != expected:
        raise ValueError("weighted chain requires canonical consecutive +1 contacts")
    if any(score > 0 for score in contact_relative_scores(state)):
        raise ValueError("initial weighted chain must have no separating contact")


def weighted_chain_priority(
    contact_count: int,
    priority: tuple[int, ...] | list[int] | None = None,
) -> tuple[int, ...]:
    """Validate or construct one deterministic violated-contact priority order."""
    if isinstance(contact_count, bool) or not isinstance(contact_count, int) or contact_count <= 0:
        raise ValueError("contact_count must be a positive integer")
    if priority is None:
        return tuple(range(contact_count))
    result = tuple(priority)
    if any(isinstance(index, bool) or not isinstance(index, int) for index in result):
        raise ValueError("priority entries must be integers")
    if len(result) != contact_count or set(result) != set(range(contact_count)):
        raise ValueError("priority must be a permutation of all contact indices")
    return result


@dataclass(frozen=True)
class WeightedChainUpperWitness1D:
    shift_parameter: int
    prefix_impulse_vector: tuple[int, ...]
    final_momenta: tuple[int, ...]
    final_scores: tuple[int, ...]


def weighted_chain_feasible_upper_witness(
    state: ContactNetworkMomentum1D,
) -> WeightedChainUpperWitness1D:
    """Construct the explicit finite feasible upper witness used for termination."""
    _validate_weighted_chain(state)
    prefix_momentum = 0
    prefix_mass = 0
    shift = 0
    for momentum, mass in zip(state.momenta, state.masses):
        prefix_momentum += momentum
        prefix_mass += mass
        shift = max(
            shift,
            _ceil_div_nonnegative(-prefix_momentum, prefix_mass),
        )

    impulses: list[int] = []
    prefix_momentum = 0
    prefix_mass = 0
    for momentum, mass in zip(state.momenta[:-1], state.masses[:-1]):
        prefix_momentum += momentum
        prefix_mass += mass
        impulse = prefix_momentum + shift * prefix_mass
        if impulse < 0:
            raise AssertionError("weighted-chain upper witness produced negative impulse")
        impulses.append(impulse)

    step = apply_contact_impulse_vector(state, tuple(impulses))
    if any(score < 0 for score in step.relative_scores_after):
        raise AssertionError("weighted-chain upper witness is not feasible")

    expected_prefix = tuple(-shift * mass for mass in state.masses[:-1])
    expected_last = state.total_momentum - sum(expected_prefix)
    expected_momenta = expected_prefix + (expected_last,)
    if step.after.momenta != expected_momenta:
        raise AssertionError("weighted-chain upper witness lost prefix-transfer construction")

    return WeightedChainUpperWitness1D(
        shift_parameter=shift,
        prefix_impulse_vector=tuple(impulses),
        final_momenta=step.after.momenta,
        final_scores=step.relative_scores_after,
    )


@dataclass(frozen=True)
class WeightedChainLeastActionSolution1D:
    before: ContactNetworkMomentum1D
    priority: tuple[int, ...]
    initial_scores: tuple[int, ...]
    coupling_gram: tuple[tuple[int, ...], ...]
    feasible_upper_impulse: tuple[int, ...]
    impulse_vector: tuple[int, ...]
    final_scores: tuple[int, ...]
    final_momenta: tuple[int, ...]
    increment_count: int

    @property
    def total_delivered_impulse(self) -> int:
        return sum(self.impulse_vector)


def solve_weighted_chain_least_action(
    state: ContactNetworkMomentum1D,
    priority: tuple[int, ...] | list[int] | None = None,
) -> WeightedChainLeastActionSolution1D:
    """Return the unique componentwise-least nonclosing impulse by unit updates."""
    _validate_weighted_chain(state)
    contact_count = len(state.contacts)
    order = weighted_chain_priority(contact_count, priority)
    initial_scores = contact_relative_scores(state)
    gram = contact_coupling_gram(state)

    for row in range(contact_count):
        if gram[row][row] <= 0:
            raise AssertionError("weighted path coupling lost positive diagonal")
        for col in range(contact_count):
            if row != col and gram[row][col] > 0:
                raise AssertionError("weighted path coupling lost Z-matrix sign pattern")

    upper = weighted_chain_feasible_upper_witness(state).prefix_impulse_vector
    impulses = [0] * contact_count
    scores = list(initial_scores)
    increments = 0
    maximum_increments = sum(upper)

    while True:
        violated = {index for index, score in enumerate(scores) if score < 0}
        if not violated:
            break
        chosen = next(index for index in order if index in violated)
        if impulses[chosen] >= upper[chosen]:
            raise AssertionError("violated contact reached the explicit feasible upper witness")
        impulses[chosen] += 1
        increments += 1
        for row in range(contact_count):
            scores[row] += gram[row][chosen]
        if increments > maximum_increments:
            raise AssertionError("weighted-chain least-action iteration exceeded finite upper bound")

    result = tuple(impulses)
    step = apply_contact_impulse_vector(state, result)
    if step.relative_scores_after != tuple(scores):
        raise AssertionError("incremental weighted-chain score ledger drifted from network oracle")
    if any(score < 0 for score in step.relative_scores_after):
        raise AssertionError("weighted-chain least-action solver terminated while contact was closing")
    if any(result[index] > upper[index] for index in range(contact_count)):
        raise AssertionError("least-action solution escaped explicit feasible upper witness")

    return WeightedChainLeastActionSolution1D(
        before=state,
        priority=order,
        initial_scores=initial_scores,
        coupling_gram=gram,
        feasible_upper_impulse=upper,
        impulse_vector=result,
        final_scores=step.relative_scores_after,
        final_momenta=step.after.momenta,
        increment_count=increments,
    )


def weighted_chain_candidate_is_feasible(
    state: ContactNetworkMomentum1D,
    impulse_vector: tuple[int, ...] | list[int],
) -> bool:
    """Check one non-negative candidate through the contact-network oracle."""
    _validate_weighted_chain(state)
    impulses = tuple(impulse_vector)
    if len(impulses) != len(state.contacts):
        raise ValueError("impulse_vector must match contact count")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in impulses
    ):
        raise ValueError("impulse_vector entries must be non-negative integers")
    return all(
        score >= 0
        for score in apply_contact_impulse_vector(state, impulses).relative_scores_after
    )
