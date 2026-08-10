"""Chinese-remainder decomposition of modular future precision and closure.

Let a positive modulus factor into pairwise-coprime prime powers

    M = product_j q_j,    q_j = p_j^e_j.

For any integer future observation matrix O, CRT gives

    (Z/MZ)^n ~= product_j (Z/q_j Z)^n,

and the modular observation map decomposes componentwise.  Therefore static
kernel/image counts multiply over the prime-power factors.

The same is true for an integer action-language row module.  At horizon h let
``L_h`` be the exact integer future row lattice.  Its modular image modulo M is
the CRT product of its images modulo all q_j.  Consequently

    modular row module at h over M is stable
      iff every prime-power component is stable at h.

Because every component plateau is permanent, the first exact stabilization
horizon satisfies

    h_M = max_j h_(q_j).

Thus independent prime-power precision refinements proceed in parallel.  The
generic composite-index bound ``Omega(I_0(M))`` equals the sum of prime-power
factor budgets and can be loose; CRT sharpens it to at most the maximum of the
component budgets.

CRT and finite abelian group decomposition are standard prior mathematics.  The
project value is the exact modular P023 precision/closure decomposition and its
parallel-refinement interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Sequence

from .integer_action_modular_closure import (
    ModularActionClosureReport,
    modular_action_closure_report,
)
from .integer_future_modular_precision import (
    ModularSmithPrecisionReport,
    modular_smith_precision_report,
)


@dataclass(frozen=True)
class PrimePowerFactor:
    prime: int
    exponent: int
    modulus: int


def prime_power_factorization(value: int) -> tuple[PrimePowerFactor, ...]:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("modulus must be an integer")
    if value <= 0:
        raise ValueError("modulus must be positive")
    if value == 1:
        return ()
    remaining = value
    prime = 2
    factors = []
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            power = 1
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
                power *= prime
            factors.append(
                PrimePowerFactor(
                    prime=prime,
                    exponent=exponent,
                    modulus=power,
                )
            )
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append(
            PrimePowerFactor(
                prime=remaining,
                exponent=1,
                modulus=remaining,
            )
        )
    if prod(factor.modulus for factor in factors) != value:
        raise AssertionError("prime-power factorization failed reconstruction")
    return tuple(factors)


@dataclass(frozen=True)
class ModularSmithCRTReport:
    modulus: int
    factors: tuple[PrimePowerFactor, ...]
    composite: ModularSmithPrecisionReport
    components: tuple[ModularSmithPrecisionReport, ...]
    product_kernel_size: int
    product_image_size: int


def modular_smith_crt_report(
    observation_matrix: Sequence[Sequence[int]],
    modulus: int,
) -> ModularSmithCRTReport:
    factors = prime_power_factorization(modulus)
    composite = modular_smith_precision_report(observation_matrix, modulus)
    components = tuple(
        modular_smith_precision_report(
            observation_matrix,
            factor.modulus,
        )
        for factor in factors
    )
    product_kernel = prod(report.kernel_size for report in components) if components else 1
    product_image = prod(report.image_size for report in components) if components else 1
    if product_kernel != composite.kernel_size:
        raise AssertionError("CRT kernel product disagreed with composite Smith count")
    if product_image != composite.image_size:
        raise AssertionError("CRT image product disagreed with composite Smith count")
    return ModularSmithCRTReport(
        modulus=modulus,
        factors=factors,
        composite=composite,
        components=components,
        product_kernel_size=product_kernel,
        product_image_size=product_image,
    )


@dataclass(frozen=True)
class ModularActionCRTReport:
    modulus: int
    factors: tuple[PrimePowerFactor, ...]
    composite: ModularActionClosureReport
    components: tuple[ModularActionClosureReport, ...]
    component_stabilization_horizons: tuple[int, ...]
    crt_stabilization_horizon: int
    component_refinement_budgets: tuple[int, ...]
    parallel_budget_bound: int

    @property
    def composite_horizon_matches_CRT_max(self) -> bool:
        return self.composite.exact_stabilization_horizon == self.crt_stabilization_horizon


def modular_action_crt_report(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    modulus: int,
) -> ModularActionCRTReport:
    factors = prime_power_factorization(modulus)
    composite = modular_action_closure_report(
        action_matrices,
        observation_rows,
        modulus,
    )
    components = tuple(
        modular_action_closure_report(
            action_matrices,
            observation_rows,
            factor.modulus,
        )
        for factor in factors
    )
    horizons = tuple(report.exact_stabilization_horizon for report in components)
    budgets = tuple(report.arithmetic_refinement_budget for report in components)
    crt_horizon = max(horizons, default=0)
    parallel_bound = max(budgets, default=0)
    if composite.exact_stabilization_horizon != crt_horizon:
        raise AssertionError("composite modular closure horizon disagreed with CRT maximum")
    if crt_horizon > parallel_bound:
        raise AssertionError("CRT component closure exceeded parallel arithmetic bound")
    if components:
        if prod(report.initial_kernel_size for report in components) != composite.initial_kernel_size:
            raise AssertionError("CRT initial modular kernel sizes failed to multiply")
        if prod(report.final_state_kernel_size for report in components) != composite.final_state_kernel_size:
            raise AssertionError("CRT final modular kernel sizes failed to multiply")
        if prod(report.final_observable_phase_count for report in components) != composite.final_observable_phase_count:
            raise AssertionError("CRT final modular image sizes failed to multiply")
    return ModularActionCRTReport(
        modulus=modulus,
        factors=factors,
        composite=composite,
        components=components,
        component_stabilization_horizons=horizons,
        crt_stabilization_horizon=crt_horizon,
        component_refinement_budgets=budgets,
        parallel_budget_bound=parallel_bound,
    )
