"""Block-access compilation of Pasten's small arithmetic-derivative problem.

Pasten's relation-adapted derivations are prime-coordinate integer vectors with
L-infinity norm.  The P025 block-value quotient proves that their minimum
nondegenerate norm is equivalently the minimum, over the rank-at-most-two block
relation lattice, of the maximum of three exact one-block access costs.

This module also records an exact integer Wronskian-capacity inequality.  For
one integer block define

    C(n) = sum_{p|n} v_p(n) * rad(n)/p.

For a primitive abc witness of radius r and normalized absorption redundancy
eta=|W|/M, the (a,b) Wronskian capacity gives

    r * (rad(a) C(b) + rad(b) C(a)) >= eta * m(c).

The nonnegative difference is an integer capacity slack.  These identities are
elementary re-accountings of the arithmetic-Wronskian route; no claim is made
that the small-derivative objective or abc connection is new.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_absorption_block import normalized_block_derivative_coefficients
from .abc_block_mu import (
    compressed_additive_states_at_radius,
    degenerate_scaling_parameter,
    exact_minimum_nondegenerate_witness_radius,
)
from .abc_support import abc_support_state, multiplicity_residual, radical


@dataclass(frozen=True)
class CompressedEscapeCount:
    abc: tuple[int, int, int]
    radius: int
    additive_state_count: int
    degenerate_state_count: int
    nondegenerate_state_count: int
    escaped: bool


@dataclass(frozen=True)
class CapacityPressure:
    abc: tuple[int, int, int]
    block_capacities: tuple[int, int, int]
    pair_capacity_ab: int
    multiplicity_residual_c: int
    mu: int
    mu_capacity_lower_bound: int
    exact_c_upper_capacity: int


def normalized_block_capacity(n: int) -> int:
    """Return ``C(n)=sum v_p(n)*rad(n)/p``; define ``C(1)=0``."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return sum(value for _prime, value in normalized_block_derivative_coefficients(n))


def pair_capacity_ab(a: int, b: int, c: int) -> int:
    """Return exact integer normalized Wronskian capacity for the (a,b) pair."""
    abc_support_state(a, b, c)
    return radical(a) * normalized_block_capacity(b) + radical(b) * normalized_block_capacity(a)


def witness_capacity_slack(
    a: int,
    b: int,
    c: int,
    radius: int,
    absorption_redundancy: int,
) -> int:
    """Return ``chi=r*K_ab-eta*m(c)`` and assert nonnegativity.

    This is valid for an actual nondegenerate witness with the supplied radius
    and absorption redundancy.  The function only checks the universal
    arithmetic inequality; it does not certify that such a witness exists.
    """
    if isinstance(radius, bool) or not isinstance(radius, int) or radius <= 0:
        raise ValueError("radius must be a positive integer")
    if (
        isinstance(absorption_redundancy, bool)
        or not isinstance(absorption_redundancy, int)
        or absorption_redundancy <= 0
    ):
        raise ValueError("absorption redundancy must be a positive integer")
    capacity = pair_capacity_ab(a, b, c)
    slack = radius * capacity - absorption_redundancy * multiplicity_residual(c)
    if slack < 0:
        raise ValueError("supplied witness costs violate exact Wronskian capacity")
    return slack


def compressed_escape_count(a: int, b: int, c: int, radius: int) -> CompressedEscapeCount:
    """Count additive compressed states and exact Wronskian-degenerate states."""
    states = compressed_additive_states_at_radius(a, b, c, radius)
    degenerate = sum(
        degenerate_scaling_parameter(a, b, c, u, v) is not None
        for u, v, _w in states
    )
    nondegenerate = len(states) - degenerate
    return CompressedEscapeCount(
        abc=(a, b, c),
        radius=radius,
        additive_state_count=len(states),
        degenerate_state_count=degenerate,
        nondegenerate_state_count=nondegenerate,
        escaped=nondegenerate > 0,
    )


def capacity_pressure(a: int, b: int, c: int) -> CapacityPressure:
    """Return exact capacity lower bound on Pasten's minimum derivative norm ``mu``."""
    abc_support_state(a, b, c)
    capacities = tuple(normalized_block_capacity(n) for n in (a, b, c))
    K = pair_capacity_ab(a, b, c)
    if K <= 0:
        raise AssertionError("primitive abc with c>2 must have positive (a,b) capacity")
    residual_c = multiplicity_residual(c)
    lower = (residual_c + K - 1) // K
    mu = exact_minimum_nondegenerate_witness_radius(a, b, c).mu
    if mu < lower:
        raise AssertionError("exact mu violated Wronskian capacity lower bound")
    c_upper = mu * radical(c) * K
    if c > c_upper:
        raise AssertionError("minimum derivative norm violated exact abc capacity inequality")
    return CapacityPressure(
        abc=(a, b, c),
        block_capacities=capacities,
        pair_capacity_ab=K,
        multiplicity_residual_c=residual_c,
        mu=mu,
        mu_capacity_lower_bound=lower,
        exact_c_upper_capacity=c_upper,
    )


def rational_small_derivative_bound_holds(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> bool:
    """Decide ``mu < c^(numerator/denominator)`` with integer powers only."""
    if (
        isinstance(numerator, bool)
        or not isinstance(numerator, int)
        or isinstance(denominator, bool)
        or not isinstance(denominator, int)
        or not 0 < numerator < denominator
    ):
        raise ValueError("require integers 0 < numerator < denominator")
    mu = exact_minimum_nondegenerate_witness_radius(a, b, c).mu
    return mu**denominator < c**numerator


def minimum_escape_radius_by_counts(a: int, b: int, c: int) -> int:
    """Recover exact ``mu`` as first radius where compressed count escapes degeneracy."""
    exact = exact_minimum_nondegenerate_witness_radius(a, b, c).mu
    for radius in range(1, exact + 1):
        if compressed_escape_count(a, b, c, radius).escaped:
            if radius != exact:
                raise AssertionError("compressed counting escape disagrees with exact mu")
            return radius
    raise AssertionError("exact mu must eventually produce a nondegenerate compressed state")
