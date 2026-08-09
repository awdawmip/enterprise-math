"""Exact block derivative-value quotient for P025 witness cost languages.

A fine arithmetic-derivative witness has one coordinate per prime in
``supp(abc)``.  For the future language consisting of

* relation additivity,
* arithmetic Wronskian magnitude / absorption redundancy, and
* minimum global L-infinity witness radius,

prime-coordinate identity inside each integer block is unnecessary once the
block access response is retained.

Write ``t_n=d_x(n)``.  A primitive relation ``a+b=c`` requires

    t_a + t_b = t_c,

and the Wronskian is

    W = a*t_b - b*t_a.

Each block value ``t_n`` lies in its derivative image ideal ``A(n) Z``.  Its
minimum prime-coordinate cost is an independent block access problem.  Hence
the fine witness Pareto problem descends exactly to a rank-two lattice of
``(t_a,t_b)`` equipped with three block access functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_block_access_apery import exact_block_access_radius
from .abc_support import abc_support_state, multiplicity_residual
from .abc_unit_relation import (
    raw_block_derivative_coefficients,
    raw_block_derivative_image_generator,
)
from .abc_witness_absorption import certified_absorption_pareto_frontier


@dataclass(frozen=True)
class BlockAccessValue:
    integer_block: int
    target: int
    image_generator: int
    primitive_row: tuple[int, ...]
    reduced_target: int
    radius: int


@dataclass(frozen=True)
class BlockValueWitnessState:
    a: int
    b: int
    c: int
    derivative_values: tuple[int, int, int]
    block_radii: tuple[int, int, int]
    global_radius: int
    wronskian: int
    residual_product: int
    absorption_redundancy: int


def _positive_gcd(values: tuple[int, ...]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def block_derivative_access_value(n: int, target: int) -> BlockAccessValue:
    """Return exact minimum prime-coordinate radius for one raw derivative target."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("integer block must be positive")
    if isinstance(target, bool) or not isinstance(target, int):
        raise ValueError("target must be an integer")
    if n == 1:
        if target != 0:
            raise ValueError("the unit block has derivative image {0}")
        return BlockAccessValue(
            integer_block=1,
            target=0,
            image_generator=0,
            primitive_row=(),
            reduced_target=0,
            radius=0,
        )

    coefficients = raw_block_derivative_coefficients(n)
    values = tuple(value for _prime, value in coefficients)
    generator = raw_block_derivative_image_generator(n)
    if target % generator:
        raise ValueError("target lies outside the block derivative image")
    primitive_row = tuple(value // generator for value in values)
    if _positive_gcd(primitive_row) != 1:
        raise AssertionError("raw derivative row failed primitive normalization")
    reduced_target = target // generator
    radius = exact_block_access_radius(primitive_row, abs(reduced_target))
    return BlockAccessValue(
        integer_block=n,
        target=target,
        image_generator=generator,
        primitive_row=primitive_row,
        reduced_target=reduced_target,
        radius=radius,
    )


def block_value_witness_state(
    a: int, b: int, c: int, derivative_a: int, derivative_b: int
) -> BlockValueWitnessState:
    """Evaluate one exact compressed additive witness state.

    The third derivative value is forced to ``derivative_a+derivative_b``.
    Each block value is checked against its exact image ideal and assigned its
    minimum independent prime-coordinate access radius.
    """
    abc_support_state(a, b, c)
    derivative_c = derivative_a + derivative_b
    access_a = block_derivative_access_value(a, derivative_a)
    access_b = block_derivative_access_value(b, derivative_b)
    access_c = block_derivative_access_value(c, derivative_c)
    wronskian = a * derivative_b - b * derivative_a
    if wronskian == 0:
        raise ValueError("compressed witness is Wronskian-degenerate")
    residual = (
        multiplicity_residual(a)
        * multiplicity_residual(b)
        * multiplicity_residual(c)
    )
    if abs(wronskian) % residual:
        raise AssertionError("additive block-value witness violated Pasten residual divisibility")
    eta = abs(wronskian) // residual
    radii = (access_a.radius, access_b.radius, access_c.radius)
    return BlockValueWitnessState(
        a=a,
        b=b,
        c=c,
        derivative_values=(derivative_a, derivative_b, derivative_c),
        block_radii=radii,
        global_radius=max(radii),
        wronskian=wronskian,
        residual_product=residual,
        absorption_redundancy=eta,
    )


def block_value_lattice_membership(
    a: int, b: int, c: int, derivative_a: int, derivative_b: int
) -> bool:
    """Return whether ``(t_a,t_b)`` lies in the exact compressed additive lattice."""
    abc_support_state(a, b, c)
    targets = (derivative_a, derivative_b, derivative_a + derivative_b)
    for n, target in zip((a, b, c), targets, strict=True):
        if n == 1:
            if target != 0:
                return False
            continue
        generator = raw_block_derivative_image_generator(n)
        if target % generator:
            return False
    return True


def _pareto_pairs(pairs: set[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
    result = []
    for pair in pairs:
        if any(
            other != pair
            and other[0] <= pair[0]
            and other[1] <= pair[1]
            for other in pairs
        ):
            continue
        result.append(pair)
    return tuple(sorted(result))


def bounded_block_value_pareto_frontier(
    a: int, b: int, c: int, max_radius: int
) -> tuple[tuple[int, int], ...]:
    """Enumerate compressed witness costs through an exact finite radius bound.

    This is a small-state executable oracle.  The theorem that prime-coordinate
    Pareto minima descend to block values is proved in prose; this routine is a
    regression tool for examples and bounded comparisons.
    """
    abc_support_state(a, b, c)
    if isinstance(max_radius, bool) or not isinstance(max_radius, int) or max_radius < 1:
        raise ValueError("max_radius must be a positive integer")

    def candidates(n: int) -> tuple[int, ...]:
        if n == 1:
            return (0,)
        coefficients = raw_block_derivative_coefficients(n)
        bound = max_radius * sum(abs(value) for _prime, value in coefficients)
        generator = raw_block_derivative_image_generator(n)
        multiple_bound = bound // generator
        return tuple(generator * multiple for multiple in range(-multiple_bound, multiple_bound + 1))

    values_a = candidates(a)
    values_b = candidates(b)
    pairs: set[tuple[int, int]] = set()
    for t_a in values_a:
        for t_b in values_b:
            if not block_value_lattice_membership(a, b, c, t_a, t_b):
                continue
            try:
                state = block_value_witness_state(a, b, c, t_a, t_b)
            except ValueError:
                continue
            if state.global_radius <= max_radius:
                pairs.add((state.global_radius, state.absorption_redundancy))
    return _pareto_pairs(pairs)


def fine_and_block_pareto_agree_on_reference_examples() -> bool:
    """Cross-check the compressed and fine exact frontiers on small P025 examples."""
    examples = (
        ((2, 3, 5), 3),
        ((2, 7, 9), 6),
        ((5, 7, 12), 3),
    )
    for triple, bound in examples:
        fine = certified_absorption_pareto_frontier(*triple, max_bound=bound)
        compressed = bounded_block_value_pareto_frontier(*triple, max_radius=bound)
        if fine != compressed:
            raise AssertionError(
                f"fine/block Pareto mismatch for {triple}: {fine} != {compressed}"
            )
    return True
