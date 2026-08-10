"""Divisibility lattice of modular future-observation precision.

For integer-valued future observations, modulus size is not the natural precision
order.  Divisibility is.

If ``M | N``, reduction ``Z/NZ -> Z/MZ`` is a ring homomorphism, so equality of
all future observations modulo N implies equality modulo M.  Hence mod-N
precision refines mod-M precision.

For two positive moduli M,N:

* observing modulo both M and N is exactly equivalent to observing modulo
  ``lcm(M,N)`` because integer differences vanish modulo both iff they vanish
  modulo the lcm;
* the greatest modulus that is a quotient/coarsening of both is ``gcd(M,N)``.

Thus modular precision levels form the positive-integer divisibility lattice:

    meet = gcd,    join = lcm.

The same order applies to action-language stabilization.  If ``M | N``, a
plateau modulo N projects to a plateau modulo M, so the first exact closure
horizon satisfies ``h_M <= h_N``.  Consequently

    h_lcm(M,N) = max(h_M, h_N),

which also follows prime-power componentwise from CRT.

This is standard modular arithmetic/lattice theory.  The project value is the
precision-order interpretation and the warning that numerical modulus magnitude
alone is not a refinement relation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm
from typing import Sequence

from .integer_action_modular_closure import modular_action_closure_report
from .integer_future_modular_precision import modular_observation_signature


def _modulus(value: int, *, name: str = "modulus") -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def modulus_refines(finer: int, coarser: int) -> bool:
    """Whether mod-finer precision canonically refines mod-coarser precision."""
    high = _modulus(finer, name="finer")
    low = _modulus(coarser, name="coarser")
    return high % low == 0


def modular_precision_meet(left: int, right: int) -> int:
    return gcd(
        _modulus(left, name="left"),
        _modulus(right, name="right"),
    )


def modular_precision_join(left: int, right: int) -> int:
    return lcm(
        _modulus(left, name="left"),
        _modulus(right, name="right"),
    )


def pair_equal_mod_both_iff_equal_mod_lcm(
    observation_matrix: Sequence[Sequence[int]],
    left_state: Sequence[int],
    right_state: Sequence[int],
    left_modulus: int,
    right_modulus: int,
) -> bool:
    """Exact equality-kernel statement for the modular precision join."""
    left_mod = _modulus(left_modulus, name="left_modulus")
    right_mod = _modulus(right_modulus, name="right_modulus")
    joined = lcm(left_mod, right_mod)
    equal_both = (
        modular_observation_signature(observation_matrix, left_state, left_mod)
        == modular_observation_signature(observation_matrix, right_state, left_mod)
        and modular_observation_signature(observation_matrix, left_state, right_mod)
        == modular_observation_signature(observation_matrix, right_state, right_mod)
    )
    equal_lcm = (
        modular_observation_signature(observation_matrix, left_state, joined)
        == modular_observation_signature(observation_matrix, right_state, joined)
    )
    if equal_both != equal_lcm:
        raise AssertionError("joint modular equality disagreed with lcm equality")
    return True


@dataclass(frozen=True)
class ModularActionPrecisionLatticeReport:
    left_modulus: int
    right_modulus: int
    meet_modulus: int
    join_modulus: int
    left_horizon: int
    right_horizon: int
    meet_horizon: int
    join_horizon: int

    @property
    def join_horizon_is_max(self) -> bool:
        return self.join_horizon == max(self.left_horizon, self.right_horizon)

    @property
    def meet_horizon_is_no_later_than_both(self) -> bool:
        return self.meet_horizon <= min(self.left_horizon, self.right_horizon)


def modular_action_precision_lattice_report(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    left_modulus: int,
    right_modulus: int,
) -> ModularActionPrecisionLatticeReport:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    meet = gcd(left, right)
    join = lcm(left, right)

    def horizon(modulus: int) -> int:
        return modular_action_closure_report(
            action_matrices,
            observation_rows,
            modulus,
        ).exact_stabilization_horizon

    left_h = horizon(left)
    right_h = horizon(right)
    meet_h = horizon(meet)
    join_h = horizon(join)
    if join_h != max(left_h, right_h):
        raise AssertionError("lcm modular closure horizon disagreed with maximum")
    if meet_h > min(left_h, right_h):
        raise AssertionError("gcd modular closure horizon was later than a refinement")
    return ModularActionPrecisionLatticeReport(
        left_modulus=left,
        right_modulus=right,
        meet_modulus=meet,
        join_modulus=join,
        left_horizon=left_h,
        right_horizon=right_h,
        meet_horizon=meet_h,
        join_horizon=join_h,
    )
