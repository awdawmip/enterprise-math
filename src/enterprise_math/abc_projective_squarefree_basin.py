"""Pointwise squarefree-safe basin for the P025 projective activation bit.

For a primitive non-unit triple a+b=c, projective activation ``sigma_proj>=1``
requires at least two nonsquarefree components, one of which must be c.
Equivalently, if c is squarefree or if both a and b are squarefree, then
``sigma_proj<1``.

The proof is elementary and pointwise; no de Bruijn counting is used.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_projective_activation import projective_activation_state
from .abc_projective_orientation import raw_derivative_mass
from .abc_support import abc_support_state, radical


@dataclass(frozen=True)
class SquarefreeBasinState:
    abc: tuple[int, int, int]
    squarefree: tuple[bool, bool, bool]
    nonsquarefree_count: int
    forced_subunit_by_structure: bool
    actually_activated: bool


def is_squarefree_integer(n: int) -> bool:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return radical(n) == n


def squarefree_basin_state(a: int, b: int, c: int) -> SquarefreeBasinState:
    """Return the exact pointwise squarefree safety classification for a,b>1."""
    abc_support_state(a, b, c)
    if a <= 1 or b <= 1:
        raise ValueError("squarefree-safe theorem here is scoped to non-unit triples")
    flags = tuple(is_squarefree_integer(n) for n in (a, b, c))
    count = sum(not flag for flag in flags)
    forced = flags[2] or (flags[0] and flags[1])
    activation = projective_activation_state(a, b, c).activated
    if forced and activation:
        raise AssertionError("squarefree structural safe basin unexpectedly activated")
    if activation:
        if flags[2] or (flags[0] and flags[1]) or count < 2:
            raise AssertionError("activated non-unit state violated squarefree necessity")
    return SquarefreeBasinState(
        abc=(a, b, c),
        squarefree=flags,
        nonsquarefree_count=count,
        forced_subunit_by_structure=forced,
        actually_activated=activation,
    )


def squarefree_pair_derivative_dominates_sum(a: int, b: int) -> bool:
    """Verify ``(ab)' >= a+b`` for coprime squarefree a,b>1.

    For squarefree n, ``n'=n*sum_{p|n}1/p >=1``; more directly
    ``a'/a>=1/a`` and ``b'/b>=1/b``.  Leibniz then gives
    ``(ab)'=b*a'+a*b'>=a+b``.
    """
    if a <= 1 or b <= 1:
        raise ValueError("require a,b>1")
    if not is_squarefree_integer(a) or not is_squarefree_integer(b):
        raise ValueError("require squarefree inputs")
    from math import gcd
    if gcd(a, b) != 1:
        raise ValueError("require coprime inputs")
    derivative = b * raw_derivative_mass(a) + a * raw_derivative_mass(b)
    if derivative < a + b:
        raise AssertionError("squarefree product derivative lost additive lower bound")
    return True
