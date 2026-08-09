"""Exact projective Wronskian efficiency and first-witness overhead split.

For a primitive abc witness x define the homogeneous ratio

    ||x||_inf / eta(x) = M ||x||_inf / |W(x)|.

Scaling x by a nonzero integer preserves this ratio.  The real relation slice
``alpha*x=0, ||x||_inf<=1`` is a rational polytope, so a rational maximizer of
``|W|`` can be scaled to an integer witness.  Hence the best integer projective
ratio equals the reciprocal real operator norm.

For abc, LP duality gives

    max |W| = min(P_ab, P_ac, P_bc),

where ``U_n=sum n*v_p(n)/p`` and

    P_ab = a*U_b + b*U_a

with cyclic analogues.  Equivalently

    sigma_proj = M / min(Pairs)
               = max(m_c/K_ab, m_b/K_ac, m_a/K_bc).

This module also factors the effective first-witness overhead into (i) failure
of the first witness to attain the projective capacity optimum and (ii) its
absorption level remaining above ``eta_min``.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_block_mu import exact_minimum_nondegenerate_witness_radius
from .abc_block_pareto_profile import minimum_absorption_at_radius
from .abc_block_value_lattice import block_value_absorption_floor
from .abc_small_derivative_block import normalized_block_capacity
from .abc_support import abc_support_state, multiplicity_residual


@dataclass(frozen=True)
class ProjectiveWronskianEfficiency:
    abc: tuple[int, int, int]
    raw_block_capacities: tuple[int, int, int]
    pair_capacities: tuple[int, int, int]
    wronskian_operator_norm: int
    residual_product: int
    sigma_projective: Fraction


@dataclass(frozen=True)
class EffectiveOverheadDecomposition:
    abc: tuple[int, int, int]
    mu: int
    eta_at_mu: int
    eta_min: int
    sigma_projective: Fraction
    first_witness_projective_ratio: Fraction
    effective_mu: Fraction
    projective_alignment_factor: Fraction
    absorption_level_factor: Fraction
    total_effective_overhead_factor: Fraction


def raw_block_capacity(n: int) -> int:
    """Return ``U_n=sum n*v_p(n)/p = m(n) C(n)``."""
    return multiplicity_residual(n) * normalized_block_capacity(n)


def projective_wronskian_efficiency(
    a: int, b: int, c: int
) -> ProjectiveWronskianEfficiency:
    """Return the exact homogeneous minimum ``inf ||x||/eta(x)``.

    The three pair capacities are exact support-function values from the three
    equivalent Wronskian expressions.  Their minimum is the restricted
    L-infinity-to-absolute-value operator norm of W on the real additive
    relation hyperplane.
    """
    abc_support_state(a, b, c)
    U_a, U_b, U_c = (raw_block_capacity(n) for n in (a, b, c))
    P_ab = a * U_b + b * U_a
    P_ac = a * U_c + c * U_a
    P_bc = b * U_c + c * U_b
    operator_norm = min(P_ab, P_ac, P_bc)
    if operator_norm <= 0:
        raise AssertionError("nontrivial primitive abc must have positive Wronskian capacity")
    M = multiplicity_residual(a) * multiplicity_residual(b) * multiplicity_residual(c)
    return ProjectiveWronskianEfficiency(
        abc=(a, b, c),
        raw_block_capacities=(U_a, U_b, U_c),
        pair_capacities=(P_ab, P_ac, P_bc),
        wronskian_operator_norm=operator_norm,
        residual_product=M,
        sigma_projective=Fraction(M, operator_norm),
    )


def effective_overhead_decomposition(
    a: int, b: int, c: int
) -> EffectiveOverheadDecomposition:
    """Factor ``(mu/eta_min)/sigma_proj`` into two exact nonnegative losses."""
    efficiency = projective_wronskian_efficiency(a, b, c)
    mu = exact_minimum_nondegenerate_witness_radius(a, b, c).mu
    eta_mu = minimum_absorption_at_radius(a, b, c, mu)
    if eta_mu is None:
        raise AssertionError("mu radius must contain a nondegenerate witness")
    eta_min = block_value_absorption_floor(a, b, c)
    if eta_mu < eta_min:
        raise AssertionError("first-witness absorption cannot lie below global floor")

    first_ratio = Fraction(mu, eta_mu)
    effective_mu = Fraction(mu, eta_min)
    sigma = efficiency.sigma_projective
    if first_ratio < sigma:
        raise AssertionError("integer first witness beat the projective real optimum")

    alignment = first_ratio / sigma
    absorption = Fraction(eta_mu, eta_min)
    total = effective_mu / sigma
    if alignment < 1 or absorption < 1 or total < 1:
        raise AssertionError("effective overhead factors must be at least one")
    if alignment * absorption != total:
        raise AssertionError("effective overhead factorization failed")

    return EffectiveOverheadDecomposition(
        abc=(a, b, c),
        mu=mu,
        eta_at_mu=eta_mu,
        eta_min=eta_min,
        sigma_projective=sigma,
        first_witness_projective_ratio=first_ratio,
        effective_mu=effective_mu,
        projective_alignment_factor=alignment,
        absorption_level_factor=absorption,
        total_effective_overhead_factor=total,
    )
