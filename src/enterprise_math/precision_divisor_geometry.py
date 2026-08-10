"""Intrinsic exponent-grid geometry of one finite divisor lattice.

For ``lambda = prod p_i^a_i``, every positive divisor has one exponent vector
``0 <= e_i <= a_i``.  The Hasse graph that changes one exponent by one step is
therefore exactly the Cartesian product of finite paths of lengths ``a_i+1``.
This is standard divisor-lattice/graph mathematics.

R004's physical hypothesis under test is narrower: if a post-genesis precision
scale has equal active prime exponents, ``lambda=P^a`` with squarefree support
``P``, then the divisor graph is an axis-symmetric ``D=omega(lambda)`` grid of
side ``a+1``.  At ``lambda=1`` the canonical support is empty and the geometry
is one point, so the later value of ``D`` is not hidden in the precision-one
state itself.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import gcd, prod
from collections.abc import Sequence

from enterprise_math.precision_prime_axes import (
    divisor_from_exponent_coordinates,
    divisor_lattice_size,
    prime_axis_rank,
    prime_axis_support,
    prime_factorization,
)

ExponentState = tuple[int, ...]
ExponentEdge = frozenset[ExponentState]


@dataclass(frozen=True)
class DivisorGridProfile:
    scale: int
    dimension: int
    prime_support: tuple[int, ...]
    maximum_exponents: tuple[int, ...]
    shape: tuple[int, ...]
    vertex_count: int
    edge_count: int
    diameter: int
    uniform_exponent_level: int | None


def divisor_grid_profile(scale: int) -> DivisorGridProfile:
    factors = prime_factorization(scale)
    exponents = tuple(exponent for _, exponent in factors)
    shape = tuple(exponent + 1 for exponent in exponents)
    dimension = len(exponents)
    vertex_count = divisor_lattice_size(scale)
    edge_count = sum(
        exponent * prod(other + 1 for index, other in enumerate(exponents) if index != axis)
        for axis, exponent in enumerate(exponents)
    )
    uniform_level: int | None
    if not exponents:
        uniform_level = 0
    elif len(set(exponents)) == 1:
        uniform_level = exponents[0]
    else:
        uniform_level = None
    return DivisorGridProfile(
        scale=scale,
        dimension=dimension,
        prime_support=tuple(prime for prime, _ in factors),
        maximum_exponents=exponents,
        shape=shape,
        vertex_count=vertex_count,
        edge_count=edge_count,
        diameter=sum(exponents),
        uniform_exponent_level=uniform_level,
    )


def divisor_grid_states(scale: int) -> tuple[ExponentState, ...]:
    profile = divisor_grid_profile(scale)
    if not profile.maximum_exponents:
        return ((),)
    return tuple(
        product(*(range(exponent + 1) for exponent in profile.maximum_exponents))
    )


def divisor_grid_edges(scale: int) -> frozenset[ExponentEdge]:
    profile = divisor_grid_profile(scale)
    edges: set[ExponentEdge] = set()
    for state in divisor_grid_states(scale):
        for axis, maximum in enumerate(profile.maximum_exponents):
            if state[axis] >= maximum:
                continue
            target = list(state)
            target[axis] += 1
            edges.add(frozenset((state, tuple(target))))
    return frozenset(edges)


def divisor_grid_distance(
    left: ExponentState, right: ExponentState, scale: int
) -> int:
    profile = divisor_grid_profile(scale)
    if len(left) != profile.dimension or len(right) != profile.dimension:
        raise ValueError("exponent state dimension must match the divisor grid")
    for state in (left, right):
        if any(
            isinstance(value, bool)
            or not isinstance(value, int)
            or not 0 <= value <= maximum
            for value, maximum in zip(state, profile.maximum_exponents)
        ):
            raise ValueError("exponent coordinate outside divisor grid")
    return sum(abs(a - b) for a, b in zip(left, right))


def divisor_coordinate_value(state: ExponentState, scale: int) -> int:
    return divisor_from_exponent_coordinates(state, scale)


def equal_prime_exponent_geometry(scale: int) -> bool:
    profile = divisor_grid_profile(scale)
    return profile.uniform_exponent_level is not None


def isotropic_genesis_sequence(squarefree_support: int, levels: int) -> tuple[int, ...]:
    support_factors = prime_factorization(squarefree_support)
    if squarefree_support == 1:
        raise ValueError("genesis support must contain at least one prime")
    if any(exponent != 1 for _, exponent in support_factors):
        raise ValueError("genesis support must be squarefree")
    if isinstance(levels, bool) or not isinstance(levels, int) or levels < 0:
        raise ValueError("levels must be a non-negative integer")
    return tuple(squarefree_support**level for level in range(levels + 1))


def isotropic_profile_sequence(
    squarefree_support: int, levels: int
) -> tuple[DivisorGridProfile, ...]:
    return tuple(
        divisor_grid_profile(scale)
        for scale in isotropic_genesis_sequence(squarefree_support, levels)
    )


def coarsen_divisor_value(divisor: int, fine_scale: int, coarse_scale: int) -> int:
    if fine_scale % coarse_scale:
        raise ValueError("coarse scale must divide fine scale")
    if fine_scale % divisor:
        raise ValueError("divisor must divide the fine scale")
    return gcd(divisor, coarse_scale)


def coarsen_exponent_state(
    state: ExponentState, fine_scale: int, coarse_scale: int
) -> ExponentState:
    fine_profile = divisor_grid_profile(fine_scale)
    if len(state) != fine_profile.dimension:
        raise ValueError("state dimension must match fine divisor grid")
    divisor = divisor_coordinate_value(state, fine_scale)
    coarse_divisor = coarsen_divisor_value(divisor, fine_scale, coarse_scale)
    coarse_factors = prime_factorization(coarse_scale)
    coordinates: list[int] = []
    remaining = coarse_divisor
    for prime, maximum in coarse_factors:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent > maximum:
            raise AssertionError("coarsened exponent exceeds target grid")
        coordinates.append(exponent)
    if remaining != 1:
        raise AssertionError("coarsened divisor must use only coarse primes")
    return tuple(coordinates)


def coarsening_composes(
    state: ExponentState,
    finest_scale: int,
    middle_scale: int,
    coarse_scale: int,
) -> bool:
    if finest_scale % middle_scale or middle_scale % coarse_scale:
        raise ValueError("scales must form a descending divisor chain")
    direct = coarsen_exponent_state(state, finest_scale, coarse_scale)
    middle = coarsen_exponent_state(state, finest_scale, middle_scale)
    staged = coarsen_exponent_state(middle, middle_scale, coarse_scale)
    return direct == staged
