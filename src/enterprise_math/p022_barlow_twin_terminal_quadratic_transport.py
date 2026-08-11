"""Secondary quadratic transport after a primitive twin terminal collision.

Let q be primitive for the Franel sequence at a nontrivial twin center r and
put

    t = 2r-2.

If the first terminal defect D_(2r-1) vanishes, then

    z_t=z_r>0,  z_(t+1)=0,

where z_n=v_q(F_n).  Complete escape through the whole twin blackout forces
2t-1=4r-5 to be prime; otherwise the direct row D_t sees the isolated zero at
t.

Now use that prime in a second neighboring-product re-entry:

    Q = 2(t-1)^2 = 2(2r-3)^2,
    2Q-1 = (2t-1)(2t-3).

The canonical central-binomial relation at Q has, at indices >=r, exactly

    +e_t - e_u + e_(Q-1),

where u=t-1 if 2t-3 is composite and u=t-2 if 2t-3 is prime.  In the first
case u is adjacent to the terminal zero t.  In the second case u lies in the
original twin blackout and u=2 mod 3, so it cannot itself be a hidden
nontrivial twin center.  Hence under complete blackout escape z_u=0 and

    v_q(D_Q)=z_Q-z_t-z_(Q-1).

If this secondary defect also vanishes, Q must be a q-zero.  Existing P022
transport gives q>7r+3, hence Q<q^2 and its base-q expansion has two digits

    Q=a q+b,  0<=a<2r,  0<=b<q.

There are then two genuinely different branches.

* If F_a is a q-unit, p-Lucas forces b to be a single-digit q-zero.  Since
  b-1 is not a zero digit, F_(Q-1) is a q-unit and the defect equality sharpens
  to z_Q=z_t=z_r.  Reflection places b in the symmetric primitive band
  r<=b<=q-1-r.
* If F_a is a q-zero, the common high digit can make both Q and Q-1 divisible
  by q.  Global nonadjacency must not be used here.  The unresolved branch is
  therefore an explicit high-digit zero a in Z_q intersect [r,2r).

This corrects the tempting but false shortcut that consecutive Franel terms
can never share a prime divisor outside the single-digit horizon.  The clean
quadratic A-support and the digit dichotomy are P022-local; p-Lucas and
Jarvis--Verrill reflection are prior art.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import (
    franel_lucas_residue,
    franel_residue,
)
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_twin_defect_difference import (
    primitive_twin_first_defect_incidence,
    primitive_twin_terminal_cancellation_signature,
)


def terminal_secondary_index(rank: int) -> int:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 6:
        raise ValueError("rank must be an integer at least six")
    return 2 * (2 * rank - 3) ** 2


def terminal_secondary_interference_index(rank: int) -> int:
    """The sole nonexplicit high coordinate u below t in the Q relation."""
    t = 2 * rank - 2
    return t - 2 if _is_prime(2 * t - 3) else t - 1


def terminal_secondary_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """Exact A-support at indices >=r of Q=2(2r-3)^2."""
    t = 2 * rank - 2
    if not _is_prime(2 * rank - 1) or not _is_prime(2 * rank + 1):
        raise ValueError("rank must be a nontrivial twin-prime center")
    if not _is_prime(2 * t - 1):
        raise ValueError("the terminal boundary 4r-5 must be prime")
    segment = terminal_secondary_index(rank)
    u = terminal_secondary_interference_index(rank)
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((u, -1), (t, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("secondary quadratic high support escaped the clean form")
    return high


def terminal_secondary_complete_escape_identity(
    rank: int,
    prime: int,
) -> tuple[int, int, int, int, int]:
    """Return (Q,D_Q,z_Q,z_(Q-1),z_t) under complete twin-blackout escape."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared rank")
    signature = primitive_twin_terminal_cancellation_signature(rank, prime)
    if signature is None:
        raise ValueError("the first twin terminal defect has not cancelled")
    if primitive_twin_first_defect_incidence(rank, prime) is not None:
        raise ValueError("an earlier twin-blackout defect already captures the row")

    t = 2 * rank - 2
    if not _is_prime(2 * t - 1):
        raise AssertionError("complete blackout escape forces 4r-5 to be prime")
    terminal_secondary_high_support(rank)
    u = terminal_secondary_interference_index(rank)
    z_u = p_adic_valuation(triple_moment_factor(u), prime)
    if z_u:
        if u == t - 1:
            raise AssertionError("the isolated terminal zero cannot have an adjacent zero")
        # Here u=t-2 lies inside the original blackout.  It is 2 mod 3 and
        # therefore not a nontrivial twin center; a zero there would already
        # create a direct/successor defect incidence.
        if u % 3 != 2:
            raise AssertionError("t-2 residue class changed")
        raise AssertionError("a non-twin blackout zero would already be visible")

    segment = terminal_secondary_index(rank)
    z_q = p_adic_valuation(triple_moment_factor(segment), prime)
    z_previous = p_adic_valuation(triple_moment_factor(segment - 1), prime)
    z_t = p_adic_valuation(triple_moment_factor(t), prime)
    actual = franel_defect_valuation(segment, prime)
    predicted = z_q - z_t - z_previous
    if actual != predicted:
        raise AssertionError("secondary quadratic defect identity failed")
    return segment, actual, z_q, z_previous, z_t


def terminal_secondary_digit_dichotomy(
    rank: int,
    prime: int,
) -> tuple[str, int, int, int, int]:
    """Classify a vanishing secondary quadratic defect by its base-q digits.

    Returns `(branch,a,b,z_Q,z_t)`, where branch is `remainder-zero` or
    `quotient-zero`.  The terminal row, every earlier blackout row, and D_Q are
    required to vanish.  The seven-rank barrier is used only as a size
    hypothesis here; callers may establish it by the dedicated transport
    theorem.
    """
    segment, value, z_q, z_previous, z_t = terminal_secondary_complete_escape_identity(
        rank, prime
    )
    if value != 0:
        raise ValueError("the secondary quadratic row already captures the valuation")
    if prime <= 7 * rank + 3:
        raise ValueError("the seven-rank escape barrier must be established first")
    if segment >= prime * prime:
        raise AssertionError("q>7r+3 must place the secondary index below q^2")
    a, b = divmod(segment, prime)
    if not 0 <= a < 2 * rank:
        raise AssertionError("secondary quotient digit must lie below 2r")
    if franel_lucas_residue(segment, prime) != 0 or z_q <= 0:
        raise AssertionError("vanishing secondary defect must force q|F_Q")

    quotient_zero = franel_residue(a, prime) == 0
    remainder_zero = franel_residue(b, prime) == 0
    if not quotient_zero and not remainder_zero:
        raise AssertionError("p-Lucas requires a zero digit in the transported index")

    if quotient_zero:
        if a < rank:
            raise AssertionError("primitive rank forbids a preprimitive zero quotient")
        return "quotient-zero", a, b, z_q, z_t

    # The quotient is a q-unit, so the remainder must carry the zero.
    if not remainder_zero or b < rank:
        raise AssertionError("unit quotient forces a primitive-or-later zero remainder")
    if b == 0:
        raise AssertionError("F_0 is a unit")
    if franel_residue(b - 1, prime) == 0:
        raise AssertionError("single-digit Franel zeros cannot be adjacent")
    if franel_lucas_residue(segment - 1, prime) == 0 or z_previous != 0:
        raise AssertionError("unit quotient and b-1 unit force F_(Q-1) to be a q-unit")
    if z_q != z_t:
        raise AssertionError("vanishing defect must transport the terminal depth exactly")
    mirror = prime - 1 - b
    if mirror < rank:
        raise AssertionError("reflection would create a zero before the primitive rank")
    return "remainder-zero", a, b, z_q, z_t
