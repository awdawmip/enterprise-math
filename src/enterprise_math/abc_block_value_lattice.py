"""Determinantal invariants of the P025 block derivative-value lattice.

For a primitive relation ``a+b=c``, let ``A,B,C`` be the positive generators
of the raw derivative images of the three non-unit blocks (zero for a unit
block).  The compressed additive witness lattice consists of

    u in A Z,  v in B Z,  u+v in C Z.

Writing ``u=A*x``, ``v=B*y`` gives the relation row ``(A,B,-C)``.  The
Wronskian functional is ``(-b*A, a*B, 0)`` on ``(x,y,z)``.  The standard gcd of
2x2 minors therefore gives the positive Wronskian image generator

    gcd(c*A*B, b*A*C, a*B*C) / gcd(A,B,C).

This recovers the earlier absorption-floor formulas using only block image
ideals and the abc relation values.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_absorption_block import minimum_absorption_redundancy_block_formula
from .abc_support import abc_support_state, multiplicity_residual
from .abc_unit_relation import raw_block_derivative_image_generator


@dataclass(frozen=True)
class BlockValueLatticeInvariants:
    abc: tuple[int, int, int]
    block_image_generators: tuple[int, int, int]
    relation_content: int
    wronskian_minor_generators: tuple[int, int, int]
    wronskian_image_generator: int
    residual_product: int
    absorption_floor: int
    lattice_index_in_z2: int | None


def _block_generator(n: int) -> int:
    if n == 1:
        return 0
    return raw_block_derivative_image_generator(n)


def block_value_lattice_invariants(a: int, b: int, c: int) -> BlockValueLatticeInvariants:
    """Return exact compressed-lattice and Wronskian-image invariants."""
    abc_support_state(a, b, c)
    A, B, C = (_block_generator(n) for n in (a, b, c))
    G = gcd(A, B, C)
    if G <= 0:
        raise AssertionError("primitive abc relation must have at least two non-unit blocks")

    numerators = (c * A * B, b * A * C, a * B * C)
    minors = tuple(value // G for value in numerators)
    if any(value % G for value in numerators):
        raise AssertionError("relation content must divide every compressed minor")
    D = gcd(*minors)
    if D <= 0:
        raise AssertionError("Wronskian image must be nonzero on a primitive abc relation")

    residual = (
        multiplicity_residual(a)
        * multiplicity_residual(b)
        * multiplicity_residual(c)
    )
    if D % residual:
        raise AssertionError("compressed Wronskian image must contain Pasten residual product")
    eta = D // residual
    previous = minimum_absorption_redundancy_block_formula(a, b, c)
    if eta != previous:
        raise AssertionError("compressed lattice floor disagrees with prior block formula")

    lattice_index: int | None
    if A > 0 and B > 0 and C > 0:
        # In x,y coordinates the congruence A*x+B*y == 0 mod C has image
        # subgroup of size C/G, so its kernel has index C/G in Z^2.  Scaling
        # x,y to u=A*x,v=B*y multiplies the index by A*B.
        lattice_index = A * B * C // G
    else:
        lattice_index = None

    return BlockValueLatticeInvariants(
        abc=(a, b, c),
        block_image_generators=(A, B, C),
        relation_content=G,
        wronskian_minor_generators=minors,
        wronskian_image_generator=D,
        residual_product=residual,
        absorption_floor=eta,
        lattice_index_in_z2=lattice_index,
    )


def block_value_wronskian_image_generator(a: int, b: int, c: int) -> int:
    """Return the positive generator of Wronskian values on the compressed lattice."""
    return block_value_lattice_invariants(a, b, c).wronskian_image_generator


def block_value_absorption_floor(a: int, b: int, c: int) -> int:
    """Return ``eta_min`` from only abc values and block derivative image ideals."""
    return block_value_lattice_invariants(a, b, c).absorption_floor
