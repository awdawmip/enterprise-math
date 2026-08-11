"""Minimal two-digit saturation in the simple secondary-terminal branch.

Assume a primitive Franel prime q occurs simply at a nontrivial twin rank r,
the first terminal defect cancels, every earlier twin-blackout defect remains
zero, the seven-rank escape barrier has been crossed, and the secondary
quadratic defect at

    Q=2(2r-3)^2

also vanishes.  Write Q=a*q+b.

The secondary transport theorem leaves a quotient-zero branch a in Z_q.  If
this high digit is itself a simple q-zero, the two-digit valuation calculus
becomes decisive.  Since q>7r+3>2r-3, q cannot divide the integer Q itself, so
b is nonzero.

For a unit low digit b, a simple high zero makes F_Q have exact q-depth one,
while Q-1 still contains the same high zero digit and hence has depth at least
one.  This makes

    v_q(D_Q)=v_q(F_Q)-1-v_q(F_(Q-1)) < 0,

contradicting continued escape.  Therefore b must also lie in Z_q.  Then b-1
is a unit, F_(Q-1) has exact depth one, and Delaygue's zero-digit lower bound
writes

    v_q(F_Q)=2+epsilon_q(Q).

The vanishing defect forces epsilon_q(Q)=0.  Thus the only simple-high-digit
continuation is exact minimal saturation:

    b in Z_q,
    v_q(F_Q)=2,
    v_q(F_(Q-1))=1,
    epsilon_q(Q)=0.

The p-adic digit lower bound is prior art (Delaygue/Gorodetsky) and the p^2
copy law is prior art (Straub).  Their use to classify the secondary Barlow
transport is P022-local.
"""

from __future__ import annotations

from .p022_barlow_franel_two_digit_excess import simple_high_zero_transport_residual
from .p022_barlow_franel_zero_digit_depth import excess_decomposition
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_twin_terminal_quadratic_transport import (
    terminal_secondary_digit_dichotomy,
    terminal_secondary_index,
)


def simple_secondary_quotient_zero_saturation(
    rank: int,
    prime: int,
) -> tuple[int, int, int, int, int]:
    """Return (a,b,z_Q,z_(Q-1),epsilon_Q) in the simple quotient-zero branch."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared rank")
    if p_adic_valuation(triple_moment_factor(rank), prime) != 1:
        raise ValueError("primitive source must have exact q-adic depth one")

    branch, high, low, z_q, z_t = terminal_secondary_digit_dichotomy(rank, prime)
    if branch != "quotient-zero":
        raise ValueError("secondary transport is not in the quotient-zero branch")
    if z_t != 1:
        raise AssertionError("simple source and terminal cancellation must give z_t=1")
    if p_adic_valuation(triple_moment_factor(high), prime) != 1:
        raise ValueError("high transported zero must have exact q-adic depth one")

    segment = terminal_secondary_index(rank)
    if low == 0:
        # q>7r+3>2r-3, so q cannot divide 2(2r-3)^2 as an ordinary integer.
        raise AssertionError("secondary quadratic index cannot be zero modulo q")

    local_branch, residual, excess = simple_high_zero_transport_residual(
        high,
        low,
        prime,
    )
    if residual != 0:
        raise AssertionError("vanishing secondary defect requires zero local residual")
    if local_branch != "two-zero" or excess != 0:
        raise AssertionError("continued simple escape must be minimally saturated two-zero transport")

    previous_depth = p_adic_valuation(triple_moment_factor(segment - 1), prime)
    valuation, baseline, checked_excess = excess_decomposition(segment, prime)
    if baseline != 2 or checked_excess != 0 or valuation != 2:
        raise AssertionError("secondary two-zero term must saturate the Delaygue depth-two baseline")
    if previous_depth != 1 or z_q != 2:
        raise AssertionError("secondary predecessor/transported depths must be 1 and 2")
    return high, low, z_q, previous_depth, checked_excess
