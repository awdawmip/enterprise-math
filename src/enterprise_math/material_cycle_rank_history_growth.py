"""Exact cycle-rank growth of future-relevant hidden contact histories.

The balanced four-cycle bridge gives one cycle-rank-one component whose minimum
response fiber has ``2s+1`` body-invisible contact histories at impulse
denominator ``s``.  This module takes a direct product of ``beta>=1`` disjoint
copies to show that cycle rank can be the exact exponent of hidden material-state
growth.

For ``beta`` disjoint balanced four-cycles:

* body count ``V=4 beta``;
* contact count ``E=4 beta``;
* component count ``c=beta``;
* incidence cycle rank ``E-V+c=beta``.

Each component independently has minimum-total relation

    H_s = { j(t) : -s<=t<=s },     |H_s|=2s+1.

Because the network coupling is block diagonal, the global minimum-total
relation is the Cartesian product

    H_s^beta,

with exact cardinality

    (2s+1)^beta.

Every global history has the same total delivered impulse ``4 beta s``, the same
zero body after-state, the same zero contact-score after-state and the same zero
kinetic after-state in this constructed family.  Yet with the same toy
contact-local reservoir law used by ``material_cycle_reservoir_future``, one
further identical reload uniquely returns the componentwise complement history.
Thus all ``(2s+1)^beta`` hidden histories are future-distinguishable.

This is an existence/sharp-family result, not a universal counting theorem for
all graphs of cycle rank beta.  General affine-lattice/polytope counting belongs
to established lattice-point theory; the E001 value is the explicit material
state-complexity witness under precision refinement.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from .material_contact_network_cycle_kernel import contact_cycle_rank
from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
)
from .material_cycle_history_precision_bridge import (
    balanced_four_cycle_minimum_relation,
)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def disjoint_balanced_cycle_network(
    cycle_rank: int,
) -> ContactNetworkMomentum1D:
    """Return beta disjoint copies of the balanced four-cycle theorem state."""
    _positive("cycle_rank", cycle_rank)
    masses: list[int] = []
    momenta: list[int] = []
    contacts: list[ContactChannel1D] = []
    for block in range(cycle_rank):
        base = 4 * block
        masses.extend((1, 1, 1, 1))
        momenta.extend((2, -2, 2, -2))
        contacts.extend(
            (
                ContactChannel1D(base + 0, base + 1, 1),
                ContactChannel1D(base + 1, base + 2, -1),
                ContactChannel1D(base + 2, base + 3, 1),
                ContactChannel1D(base + 0, base + 3, 1),
            )
        )
    state = ContactNetworkMomentum1D(
        masses=tuple(masses),
        momenta=tuple(momenta),
        contacts=tuple(contacts),
    )
    if contact_cycle_rank(state) != cycle_rank:
        raise AssertionError("disjoint balanced-cycle construction lost exact cycle rank")
    return state


def disjoint_balanced_cycle_minimum_history_count(
    cycle_rank: int,
    denominator: int,
) -> int:
    _positive("cycle_rank", cycle_rank)
    _positive("denominator", denominator)
    return (2 * denominator + 1) ** cycle_rank


def disjoint_balanced_cycle_minimum_relation(
    cycle_rank: int,
    denominator: int,
) -> tuple[tuple[int, ...], ...]:
    """Return the exact Cartesian-product minimum contact-history relation."""
    _positive("cycle_rank", cycle_rank)
    _positive("denominator", denominator)
    local = balanced_four_cycle_minimum_relation(denominator)
    result = tuple(
        tuple(value for block in blocks for value in block)
        for blocks in product(local, repeat=cycle_rank)
    )
    expected = disjoint_balanced_cycle_minimum_history_count(
        cycle_rank, denominator
    )
    if len(result) != expected:
        raise AssertionError("cycle-rank product relation lost exact cardinality")
    return result


@dataclass(frozen=True)
class CycleRankHistoryGrowthReport:
    cycle_rank: int
    denominator: int
    body_count: int
    contact_count: int
    component_count: int
    minimum_total_impulse_numerator: int
    history_class_count: int
    common_body_after_numerators: tuple[int, ...]
    common_final_score_numerators: tuple[int, ...]
    common_kinetic_after_numerator: int
    all_histories_future_distinguishable_under_reservoir_reload: bool


def cycle_rank_history_growth_report(
    cycle_rank: int,
    denominator: int,
) -> CycleRankHistoryGrowthReport:
    """Verify the exact ``(2s+1)^beta`` hidden-history family."""
    _positive("cycle_rank", cycle_rank)
    _positive("denominator", denominator)
    beta = cycle_rank
    s = denominator
    state = disjoint_balanced_cycle_network(beta)
    relation = disjoint_balanced_cycle_minimum_relation(beta, s)
    scaled_state = ContactNetworkMomentum1D(
        masses=state.masses,
        momenta=tuple(s * value for value in state.momenta),
        contacts=state.contacts,
    )
    reference = relation[0]
    reference_step = apply_contact_impulse_vector(scaled_state, reference)
    if any(reference_step.after.momenta) or any(reference_step.relative_scores_after):
        raise AssertionError("cycle-rank reference failed zero body/score closure")
    expected_total = 4 * beta * s
    if sum(reference) != expected_total:
        raise AssertionError("cycle-rank reference lost minimum total impulse")

    # Exhaustive verification is intentionally performed by the executable
    # report only for the represented finite relation supplied by the caller.
    # Each block is independently known to be a minimum-total zero-score fiber.
    for history in relation:
        if sum(history) != expected_total:
            raise AssertionError("cycle-rank history changed total impulse")
        step = apply_contact_impulse_vector(scaled_state, history)
        if step.after.momenta != reference_step.after.momenta:
            raise AssertionError("cycle-rank history changed body after-state")
        if step.relative_scores_after != reference_step.relative_scores_after:
            raise AssertionError("cycle-rank history changed score after-state")

    kinetic_after = sum(value * value for value in reference_step.after.momenta)
    initial_capacity = 2 * s
    futures = {
        tuple(initial_capacity - value for value in history)
        for history in relation
    }
    if len(futures) != len(relation):
        raise AssertionError("cycle-rank reservoir future failed injective history recovery")
    local_set = set(balanced_four_cycle_minimum_relation(s))
    for future in futures:
        for block in range(beta):
            segment = future[4 * block : 4 * block + 4]
            if segment not in local_set:
                raise AssertionError("cycle-rank reservoir future left local minimum relation")

    return CycleRankHistoryGrowthReport(
        cycle_rank=beta,
        denominator=s,
        body_count=len(state.masses),
        contact_count=len(state.contacts),
        component_count=beta,
        minimum_total_impulse_numerator=expected_total,
        history_class_count=len(relation),
        common_body_after_numerators=reference_step.after.momenta,
        common_final_score_numerators=reference_step.relative_scores_after,
        common_kinetic_after_numerator=kinetic_after,
        all_histories_future_distinguishable_under_reservoir_reload=True,
    )
