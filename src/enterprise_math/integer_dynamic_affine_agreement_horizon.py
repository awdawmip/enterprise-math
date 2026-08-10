"""Horizon filtration of exact/modular agreement states for affine models.

At each future horizon h, the homogeneous dynamic-difference compiler gives an
augmented row module ``D_h``.  Split its basis rows into variable coefficients
and constants:

    A_h x = -c_h.

The agreement set can refine in two mathematically different ways:

* FIBER refinement: the linear kernel of A_h shrinks;
* IMAGE consistency loss: ``-c_h`` leaves the exact/modular image and the affine
  agreement coset becomes empty, even if the linear kernel size/rank is unchanged.

This module tracks both axes over horizon.  A sharp scalar example has h0
constraint ``2x+2=0 mod4`` (two solutions) and h1 adds ``2x=0 mod4`` (same
linear kernel size, but no common affine solution).
"""

from __future__ import annotations

from dataclasses import dataclass

from .integer_dynamic_affine_agreement import (
    affine_equation_integer_solvable,
    affine_equation_modular_solvable,
    split_affine_difference_basis,
)
from .integer_dynamic_affine_model_separation import (
    homogeneous_affine_action_family,
    homogeneous_affine_observation_rows,
)
from .integer_dynamic_model_separation_horizon import (
    dynamic_model_separation_horizon_report,
)
from .integer_future_modular_precision import modular_smith_precision_report
from .integer_future_smith_precision import integer_smith_precision_profile


@dataclass(frozen=True)
class AffineAgreementHorizonStep:
    horizon: int
    solvable: bool
    linear_rank: int
    exact_agreement_free_rank: int | None
    linear_smith_factors: tuple[int, ...]
    modular_agreement_state_count: int | None
    modular_total_state_count: int | None


@dataclass(frozen=True)
class AffineAgreementHorizonReport:
    state_dimension: int
    modulus: int | None
    steps: tuple[AffineAgreementHorizonStep, ...]

    @property
    def first_empty_agreement_horizon(self) -> int | None:
        return next((step.horizon for step in self.steps if not step.solvable), None)


def dynamic_affine_agreement_horizon_report(
    left_actions,
    left_observation_rows,
    left_observation_offset,
    right_actions,
    right_observation_rows,
    right_observation_offset,
    *,
    modulus: int | None = None,
) -> AffineAgreementHorizonReport:
    if modulus is not None:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("modulus must be an integer")
        if modulus <= 0:
            raise ValueError("modulus must be positive")

    left_homogeneous_actions = homogeneous_affine_action_family(left_actions)
    right_homogeneous_actions = homogeneous_affine_action_family(right_actions)
    left_homogeneous_obs = homogeneous_affine_observation_rows(
        left_observation_rows,
        left_observation_offset,
    )
    right_homogeneous_obs = homogeneous_affine_observation_rows(
        right_observation_rows,
        right_observation_offset,
    )
    dynamic = dynamic_model_separation_horizon_report(
        left_homogeneous_actions,
        left_homogeneous_obs,
        right_homogeneous_actions,
        right_homogeneous_obs,
    )
    state_dimension = dynamic.state_dimension - 1
    total = modulus ** state_dimension if modulus is not None else None
    steps = []

    for dynamic_step in dynamic.steps:
        basis = dynamic_step.difference_basis
        if not basis:
            steps.append(
                AffineAgreementHorizonStep(
                    horizon=dynamic_step.horizon,
                    solvable=True,
                    linear_rank=0,
                    exact_agreement_free_rank=state_dimension,
                    linear_smith_factors=(),
                    modular_agreement_state_count=total,
                    modular_total_state_count=total,
                )
            )
            continue

        linear, constants = split_affine_difference_basis(basis)
        profile = integer_smith_precision_profile(linear)
        if modulus is None:
            solvable = affine_equation_integer_solvable(linear, constants)
            agreement_count = None
        else:
            solvable = affine_equation_modular_solvable(
                linear,
                constants,
                modulus,
            )
            agreement_count = (
                modular_smith_precision_report(linear, modulus).kernel_size
                if solvable
                else 0
            )
        steps.append(
            AffineAgreementHorizonStep(
                horizon=dynamic_step.horizon,
                solvable=solvable,
                linear_rank=profile.rational_rank,
                exact_agreement_free_rank=(
                    profile.hidden_free_rank if solvable else None
                ),
                linear_smith_factors=profile.smith_invariant_factors,
                modular_agreement_state_count=agreement_count,
                modular_total_state_count=total,
            )
        )

    return AffineAgreementHorizonReport(
        state_dimension=state_dimension,
        modulus=modulus,
        steps=tuple(steps),
    )
