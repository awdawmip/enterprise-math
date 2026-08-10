"""Agreement-state Smith profile for two integer dynamic models.

The final future-output difference module D of two corresponding linear models
is itself an integer observation module on the common initial state x.

    D x = 0

means every generated output-difference row vanishes, equivalently the two models
produce identical outputs for x under every literal action word.

Thus the Smith profile of D classifies the model-agreement fiber:

* ``n-rank_Q(D)`` free exact agreement directions;
* Smith factors describe modular agreement residues;
* modulo M, the number of initial states in ``(Z/MZ)^n`` on which the models
  agree for all words is

      M^(n-r) * product_i gcd(d_i,M).

The models are modularly indistinguishable on **all** states iff this kernel size
is ``M^n``, which is the same condition captured by the dynamic difference
content.  This module refines the global yes/no separation result into an exact
state-fiber size/profile.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_dynamic_model_separation import (
    _paired_models,
    dynamic_difference_module_basis,
    row_module_content,
)
from .integer_future_modular_precision import modular_smith_precision_report
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class DynamicModelAgreementProfile:
    state_dimension: int
    difference_basis: Matrix
    difference_content: int
    difference_rank: int
    exact_agreement_free_rank: int
    difference_smith_factors: tuple[int, ...]

    @property
    def exactly_equivalent_on_all_states(self) -> bool:
        return not self.difference_basis


@dataclass(frozen=True)
class DynamicModelModularAgreementReport:
    modulus: int
    state_dimension: int
    agreement_state_count: int
    total_state_count: int
    disagreement_state_count: int
    difference_rank: int
    difference_smith_factors: tuple[int, ...]

    @property
    def all_states_agree(self) -> bool:
        return self.agreement_state_count == self.total_state_count

    @property
    def only_zero_fraction_statement(self) -> bool:
        # Placeholder semantic guard: counts are exact integers; callers should
        # not infer probability without a separately declared state measure.
        return True


def dynamic_model_agreement_profile(
    left_actions: Sequence[Sequence[Sequence[int]]],
    left_observations: Sequence[Sequence[int]],
    right_actions: Sequence[Sequence[Sequence[int]]],
    right_observations: Sequence[Sequence[int]],
) -> DynamicModelAgreementProfile:
    left, left_rows, right, right_rows = _paired_models(
        left_actions,
        left_observations,
        right_actions,
        right_observations,
    )
    del left, right, right_rows
    dimension = len(left_rows[0])
    basis = dynamic_difference_module_basis(
        left_actions,
        left_observations,
        right_actions,
        right_observations,
    )
    if not basis:
        return DynamicModelAgreementProfile(
            state_dimension=dimension,
            difference_basis=(),
            difference_content=0,
            difference_rank=0,
            exact_agreement_free_rank=dimension,
            difference_smith_factors=(),
        )
    profile = integer_smith_precision_profile(basis)
    return DynamicModelAgreementProfile(
        state_dimension=dimension,
        difference_basis=basis,
        difference_content=row_module_content(basis),
        difference_rank=profile.rational_rank,
        exact_agreement_free_rank=profile.hidden_free_rank,
        difference_smith_factors=profile.smith_invariant_factors,
    )


def dynamic_model_modular_agreement_report(
    left_actions: Sequence[Sequence[Sequence[int]]],
    left_observations: Sequence[Sequence[int]],
    right_actions: Sequence[Sequence[Sequence[int]]],
    right_observations: Sequence[Sequence[int]],
    modulus: int,
) -> DynamicModelModularAgreementReport:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    exact = dynamic_model_agreement_profile(
        left_actions,
        left_observations,
        right_actions,
        right_observations,
    )
    total = modulus ** exact.state_dimension
    if not exact.difference_basis:
        return DynamicModelModularAgreementReport(
            modulus=modulus,
            state_dimension=exact.state_dimension,
            agreement_state_count=total,
            total_state_count=total,
            disagreement_state_count=0,
            difference_rank=0,
            difference_smith_factors=(),
        )
    modular = modular_smith_precision_report(
        exact.difference_basis,
        modulus,
    )
    return DynamicModelModularAgreementReport(
        modulus=modulus,
        state_dimension=exact.state_dimension,
        agreement_state_count=modular.kernel_size,
        total_state_count=total,
        disagreement_state_count=total - modular.kernel_size,
        difference_rank=exact.difference_rank,
        difference_smith_factors=exact.difference_smith_factors,
    )
