"""Exact unavoidable core of a monotone future-action preservation family.

Fix one precision level and let ``P(S)`` mean that action subset ``S`` preserves
the full declared future precision.  ``P`` is monotone upward.

An action ``a`` belongs to **every** preserving subset iff

    P(E \ {a}) is false,

where ``E`` is the full action family.

Proof: if the maximal subset omitting ``a`` already fails, every smaller subset
omitting ``a`` fails by monotonicity.  Conversely, if ``E\{a}`` preserves, it is
a preserving witness that omits ``a``.

Thus the intersection of all preserving subsets — the unavoidable action core —
is computed by only one leave-one-out preservation test per action, with no
``2^k`` subset enumeration.

The core is a unique least preserving action family exactly when the core itself
preserves full precision.  If the core fails, no least subset exists; preserving
capabilities must then rely on alternative/contextual action combinations.

This statement holds independently at STATE_KERNEL and INTEGER_MODULE levels.
It is standard monotone-set-family logic; the project value is an exact cheap
front-end test before any global action-capability search.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_subset_preserves,
)


def _mode(value: str) -> str:
    if value not in (STATE_KERNEL, INTEGER_MODULE):
        raise ValueError("mode must be STATE_KERNEL or INTEGER_MODULE")
    return value


@dataclass(frozen=True)
class ActionCapabilityCoreReport:
    mode: str
    action_count: int
    unavoidable_core: tuple[int, ...]
    optional_actions: tuple[int, ...]
    core_preserves_full_precision: bool
    unique_least_subset: tuple[int, ...] | None
    leave_one_out_tests: int

    @property
    def has_unique_least_subset(self) -> bool:
        return self.unique_least_subset is not None

    @property
    def least_subset_nonexistence_certified(self) -> bool:
        return not self.core_preserves_full_precision


def action_capability_unavoidable_core(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    *,
    mode: str = INTEGER_MODULE,
) -> ActionCapabilityCoreReport:
    actions = tuple(action_matrices)
    if not actions:
        raise ValueError("at least one action is required")
    selected_mode = _mode(mode)
    all_indices = tuple(range(len(actions)))

    if not action_subset_preserves(
        actions,
        observation_rows,
        all_indices,
        mode=selected_mode,
    ):
        raise AssertionError("full action family failed to preserve its own precision")

    unavoidable = []
    for action in all_indices:
        retained = tuple(index for index in all_indices if index != action)
        if not action_subset_preserves(
            actions,
            observation_rows,
            retained,
            mode=selected_mode,
        ):
            unavoidable.append(action)

    core = tuple(unavoidable)
    core_preserves = action_subset_preserves(
        actions,
        observation_rows,
        core,
        mode=selected_mode,
    )
    optional = tuple(index for index in all_indices if index not in set(core))
    return ActionCapabilityCoreReport(
        mode=selected_mode,
        action_count=len(actions),
        unavoidable_core=core,
        optional_actions=optional,
        core_preserves_full_precision=core_preserves,
        unique_least_subset=core if core_preserves else None,
        leave_one_out_tests=len(actions),
    )
