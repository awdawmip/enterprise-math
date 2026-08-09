"""Relation-subgroup generator radius for rank-one unit abc relations.

For ``1+b=c`` the compressed additive relation state is one-dimensional: a
common derivative value ``t`` lying in the intersection of the two raw block
image ideals.  Let ``D=lcm(A(b),A(c))`` be the primitive positive group step.
At ambient witness radius ``R``, accessible relation states correspond to
integer scale factors ``k`` for which ``t=kD`` is simultaneously accessible in
both blocks.

The subgroup generated at radius ``R`` is therefore

    gcd{k : kD accessible at radius R} * D Z.

The first radius where this gcd becomes one is a new exact scale between first
nonzero access and direct primitive-step access.  In the Sophie-type family
``1+2q=2q+1`` it has the closed form ``(q+1)/3`` for q>=5 Sophie primes.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .abc_block_floor_line import exact_absorption_floor_access
from .abc_block_mu import exact_minimum_nondegenerate_witness_radius
from .abc_block_value_quotient import block_derivative_access_value
from .abc_support import prime_factorization
from .abc_unit_relation import (
    raw_block_derivative_coefficients,
    raw_block_derivative_image_generator,
)


@dataclass(frozen=True)
class UnitRelationGeneratorRadius:
    b: int
    c: int
    common_group_step: int
    first_nonzero_radius: int
    generator_radius: int
    primitive_direct_radius: int
    scale_factors_at_generator_radius: tuple[int, ...]


def _is_prime(n: int) -> bool:
    return n > 1 and prime_factorization(n) == ((n, 1),)


def _target_bound(n: int, radius: int) -> int:
    return radius * sum(value for _prime, value in raw_block_derivative_coefficients(n))


def unit_relation_common_group_step(b: int, c: int) -> int:
    """Return the primitive positive common derivative-value group step."""
    if 1 + b != c:
        raise ValueError("require unit relation 1+b=c")
    if b <= 1:
        raise ValueError("require nontrivial b>1")
    return lcm(
        raw_block_derivative_image_generator(b),
        raw_block_derivative_image_generator(c),
    )


def accessible_unit_relation_scale_factors(
    b: int, c: int, radius: int
) -> tuple[int, ...]:
    """Return nonnegative ``k`` with common derivative target ``kD`` accessible by R."""
    if 1 + b != c:
        raise ValueError("require unit relation 1+b=c")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    D = unit_relation_common_group_step(b, c)
    max_target = min(_target_bound(b, radius), _target_bound(c, radius))
    max_scale = max_target // D
    accessible = []
    for k in range(max_scale + 1):
        target = k * D
        if (
            block_derivative_access_value(b, target).radius <= radius
            and block_derivative_access_value(c, target).radius <= radius
        ):
            accessible.append(k)
    return tuple(accessible)


def generated_scale_gcd(b: int, c: int, radius: int) -> int:
    """Return gcd of accessible scale factors; zero means only the zero state."""
    value = 0
    for scale in accessible_unit_relation_scale_factors(b, c, radius):
        value = gcd(value, scale)
    return value


def exact_unit_relation_generator_radius(b: int, c: int) -> UnitRelationGeneratorRadius:
    """Return first radius whose accessible relation states generate the full group."""
    if 1 + b != c:
        raise ValueError("require unit relation 1+b=c")
    triple = (1, b, c)
    mu = exact_minimum_nondegenerate_witness_radius(*triple).mu
    nu = exact_absorption_floor_access(*triple).nu
    D = unit_relation_common_group_step(b, c)
    for radius in range(mu, nu + 1):
        if generated_scale_gcd(b, c, radius) == 1:
            return UnitRelationGeneratorRadius(
                b=b,
                c=c,
                common_group_step=D,
                first_nonzero_radius=mu,
                generator_radius=radius,
                primitive_direct_radius=nu,
                scale_factors_at_generator_radius=accessible_unit_relation_scale_factors(
                    b, c, radius
                ),
            )
    raise AssertionError("direct primitive access at nu must generate the relation group")


def sophie_relation_generator_profile(q: int) -> dict[str, int | tuple[int, ...]]:
    """Return exact ``mu < rho_gen < nu`` profile for ``1+2q=2q+1``.

    Scope: q>=5, q prime, and 2q+1 prime.  Such q must satisfy q=5 mod 6.
    The formulas are

        mu = 2,
        rho_gen = (q+1)/3,
        nu = (q-1)/2.
    """
    if not _is_prime(q) or q < 5:
        raise ValueError("q must be a prime >=5")
    c = 2 * q + 1
    if not _is_prime(c):
        raise ValueError("2q+1 must also be prime")
    if q % 6 != 5:
        raise AssertionError("Sophie prime q>=5 must be 5 mod 6")
    exact = exact_unit_relation_generator_radius(2 * q, c)
    expected_mu = 2
    expected_rho = (q + 1) // 3
    expected_nu = (q - 1) // 2
    if (
        exact.first_nonzero_radius,
        exact.generator_radius,
        exact.primitive_direct_radius,
    ) != (expected_mu, expected_rho, expected_nu):
        raise AssertionError("exact unit solver disagrees with Sophie closed formulas")
    return {
        "q": q,
        "c": c,
        "mu": expected_mu,
        "generator_radius": expected_rho,
        "nu": expected_nu,
        "scale_factors_at_generator_radius": exact.scale_factors_at_generator_radius,
    }
