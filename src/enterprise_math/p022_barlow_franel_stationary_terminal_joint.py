"""Joint fixed obstruction for double-stationary twin-terminal escape.

Two independent P022 reductions attach fixed rank-r rational data to the last
hard primitive-twin branch.

1. A double-stationary primitive source

       q^2 | F_r,   q | F'_r

   forces q to divide the numerator of the formal derivative F'_r.

2. Vanishing of the first twin terminal defect forces

       q | F_(2r-2),

   and the direct terminal-transfer theorem identifies this with divisibility
   of the fixed rational transfer C_r by q.

Consequently any primitive source satisfying both conditions must divide the
single fixed integer

    J_r = gcd(num(F'_r), num(C_r)).

This is strictly smaller than studying the stationary gcd or terminal gcd in
isolation: the common moving Franel factor F_r has disappeared.

Finite exact computation currently shows an especially strong pattern: for
3<=r<=1000 the odd part of J_r is always 1 or 5.  This is recorded only as a
pressure-test conjecture, not as a uniform theorem.  A proof that the odd part
of J_r divides 5 for every r>=3 would immediately exclude the joint obstruction
for every nontrivial primitive twin source, because its odd primitive valuation
prime is at least 2r+1>=13.

The Franel recurrence and formal derivative framework are prior art.  The two
fixed reductions are established by neighboring P022 modules; their joint gcd
and the resulting compression of the escape frontier are P022-local.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_franel_gessel_lucas_copy import copy_depth_obstruction, franel_formal_derivative
from .p022_barlow_franel_terminal_transfer import terminal_transfer
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_defect_difference import primitive_twin_terminal_cancellation_signature


def stationary_terminal_joint_gcd(rank: int) -> int:
    """J_r=gcd(num(F'_r),num(C_r))."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    derivative = franel_formal_derivative(rank)
    transfer = terminal_transfer(rank)
    return gcd(abs(derivative.numerator), abs(transfer.numerator))


def odd_part(value: int) -> int:
    """Return the positive odd part of a nonzero integer."""
    if isinstance(value, bool) or not isinstance(value, int) or value == 0:
        raise ValueError("value must be a nonzero integer")
    result = abs(value)
    while result % 2 == 0:
        result //= 2
    return result


def primitive_joint_escape_forces_fixed_gcd(rank: int, prime: int) -> int:
    """Double-stationary terminal cancellation forces q|J_r exactly."""
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")

    depth, derivative_residue, stationary = copy_depth_obstruction(rank, prime)
    if depth < 2 or derivative_residue != 0 or not stationary:
        raise ValueError("source is not double-stationary")
    signature = primitive_twin_terminal_cancellation_signature(rank, prime)
    if signature is None:
        raise ValueError("the first twin terminal defect has not cancelled")

    derivative = franel_formal_derivative(rank)
    transfer = terminal_transfer(rank)
    if derivative.denominator % prime == 0 or transfer.denominator % prime == 0:
        raise AssertionError("primitive q must be a unit on both fixed denominators")
    if derivative.numerator % prime:
        raise AssertionError("double-stationary source must divide num(F'_r)")
    if transfer.numerator % prime:
        raise AssertionError("terminal common zero must divide num(C_r)")

    joint = stationary_terminal_joint_gcd(rank)
    if joint % prime:
        raise AssertionError("joint fixed gcd lost the primitive obstruction")
    return joint


def bounded_joint_odd_part_divides_five(max_rank: int) -> bool:
    """Finite pressure test only; this is not the uniform theorem."""
    if isinstance(max_rank, bool) or not isinstance(max_rank, int) or max_rank < 3:
        raise ValueError("max_rank must be at least three")
    for rank in range(3, max_rank + 1):
        if 5 % odd_part(stationary_terminal_joint_gcd(rank)):
            return False
    return True
