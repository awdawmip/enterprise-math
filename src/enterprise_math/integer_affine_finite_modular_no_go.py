"""Finite modular tests cannot certify exact integer affine reachability.

For any finite nonempty set of tested positive moduli ``M_i``, let

    D = lcm(M_i),
    q = D+1.

Use the same scalar integer map ``A=(q)`` and compare two targets

    b_reach = q,
    b_bad   = q + D.

Exact integer world:

* ``q x=q`` is reachable, with solution x=1;
* ``q x=q+D`` is unreachable because ``0<D<q`` and q does not divide q+D.

For every tested modulus M_i, however, ``M_i | D`` and therefore

    b_bad == b_reach (mod M_i).

Since A is identical, the two modular equations have exactly the same solution
set modulo every tested modulus, state by state.  Thus no finite family of
modular precision tests can certify exact integer IMAGE reachability without an
additional bound or exact arithmetic access.

A new modulus not dividing D can break the mimic.  The construction is the
IMAGE-side analogue of the finite-modular free-hidden-state/deep-torsion no-go.

This is elementary congruence arithmetic expressed as a precision-identifiability
boundary; no probabilistic or physical claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)


def _moduli(values: Sequence[int]) -> tuple[int, ...]:
    result = tuple(values)
    if not result:
        raise ValueError("at least one tested modulus is required")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("tested moduli must be integers")
        if value <= 0:
            raise ValueError("tested moduli must be positive")
    return result


def finite_modular_reachable_unreachable_pair(
    tested_moduli: Sequence[int],
) -> tuple[int, int, int, int]:
    moduli = _moduli(tested_moduli)
    depth = 1
    for modulus in moduli:
        depth = lcm(depth, modulus)
    coefficient = depth + 1
    reachable_target = coefficient
    unreachable_target = coefficient + depth
    return coefficient, reachable_target, unreachable_target, depth


@dataclass(frozen=True)
class FiniteModularImageNoGoReport:
    tested_moduli: tuple[int, ...]
    lcm_depth: int
    coefficient: int
    reachable_target: int
    unreachable_target: int
    reachable_exact: bool
    unreachable_exact: bool
    modular_solution_sets_identical: bool


def finite_modular_image_no_go_report(
    tested_moduli: Sequence[int],
) -> FiniteModularImageNoGoReport:
    moduli = _moduli(tested_moduli)
    coefficient, reachable_target, unreachable_target, depth = (
        finite_modular_reachable_unreachable_pair(moduli)
    )
    matrix = ((coefficient,),)
    reachable_exact = integrally_reachable(matrix, (reachable_target,))
    unreachable_exact = integrally_reachable(matrix, (unreachable_target,))
    if not reachable_exact or unreachable_exact:
        raise AssertionError("finite modular IMAGE no-go exact boundary failed")

    identical = True
    for modulus in moduli:
        if (reachable_target - unreachable_target) % modulus != 0:
            identical = False
            break
        if modularly_reachable(matrix, (reachable_target,), modulus) != modularly_reachable(
            matrix,
            (unreachable_target,),
            modulus,
        ):
            identical = False
            break
        # Because coefficient and target are congruent equation data, bounded
        # statewise equality is automatic.  Check every residue explicitly here.
        for state in range(modulus):
            left = (coefficient * state - reachable_target) % modulus == 0
            right = (coefficient * state - unreachable_target) % modulus == 0
            if left != right:
                identical = False
                break
        if not identical:
            break
    if not identical:
        raise AssertionError("finite tested modular solution sets were not identical")

    return FiniteModularImageNoGoReport(
        tested_moduli=moduli,
        lcm_depth=depth,
        coefficient=coefficient,
        reachable_target=reachable_target,
        unreachable_target=unreachable_target,
        reachable_exact=reachable_exact,
        unreachable_exact=unreachable_exact,
        modular_solution_sets_identical=identical,
    )
