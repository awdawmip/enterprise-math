"""Casoratian and last-hit form of the large-prime Franel terminal problem.

The universal midpoint companions H and K solve the same second-order integer
recurrence with initial data (0,1) and (2,-1).  Their Casoratian is

    H_d K_(d+1) - H_(d+1) K_d
      = -2 (-8)^d ((2d-1)!!)^4.

Hence for an odd prime q>2d-1 the two branches cannot both vanish at d.
The residue class q mod8 therefore selects a unique algebraic branch, not just
a convenient representation.

For q>4r-3, put m=(q-1)/2 and offsets

    d=m-(2r-2),  e=m-r.

If q is primitive at rank r, then e is the largest positive left-half hit of
the selected companion.  Terminal cancellation additionally forces d to be a
hit.  Thus the unresolved large-prime arithmetic core is exactly a last-hit
gap problem for one fixed integer recurrence, with

    e-d=r-2,  q=4e-2d+5.
"""

from __future__ import annotations

from .p022_barlow_franel_integer_companion import (
    midpoint_integer_companion,
    odd_double_factorial,
)
from .p022_barlow_franel_lucas_rank import franel_rank_of_apparition
from .p022_barlow_franel_universal_companion import (
    companion_kind,
    nonforced_midpoint_integer_companion,
    terminal_companion_offsets,
    universal_companion_value,
    universal_left_zero_offsets,
)
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor


def universal_companion_casoratian(offset: int) -> int:
    """Exact H/K Casoratian at offset d."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    left = (
        midpoint_integer_companion(offset)
        * nonforced_midpoint_integer_companion(offset + 1)
        - midpoint_integer_companion(offset + 1)
        * nonforced_midpoint_integer_companion(offset)
    )
    expected = -2 * (-8) ** offset * odd_double_factorial(offset) ** 4
    if left != expected:
        raise AssertionError("universal companion Casoratian changed")
    return left


def companion_branch_zero_is_unique(prime: int, offset: int) -> bool:
    """For p>2d-1, H_d and K_d cannot both vanish modulo p."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    if prime <= 2 * offset - 1:
        raise ValueError("prime must exceed all Casoratian odd factors")
    determinant = universal_companion_casoratian(offset)
    if determinant % prime == 0:
        raise AssertionError("Casoratian must be a p-unit in the declared range")
    h_zero = midpoint_integer_companion(offset) % prime == 0
    k_zero = nonforced_midpoint_integer_companion(offset) % prime == 0
    if h_zero and k_zero:
        raise AssertionError("the two companion branches cannot vanish together")
    return True


def rank_from_universal_companion(prime: int) -> int | None:
    """Recover the Franel rank as the last left companion hit."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    middle = (prime - 1) // 2
    offsets = universal_left_zero_offsets(prime)
    if offsets:
        predicted = middle - max(offsets)
    elif companion_kind(prime) == "H":
        predicted = middle
    else:
        predicted = None
    actual = franel_rank_of_apparition(prime)
    if predicted != actual:
        raise AssertionError("last companion hit must equal the Franel first zero")
    return predicted


def primitive_terminal_last_hit_signature(rank: int, prime: int) -> tuple[int, int, str]:
    """Exact last-hit signature of a primitive terminal common zero."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    d, e = terminal_companion_offsets(rank, prime)
    if triple_moment_factor(2 * rank - 2) % prime:
        raise ValueError("terminal Franel term must also vanish modulo prime")
    offsets = universal_left_zero_offsets(prime)
    if not offsets or max(offsets) != e:
        raise AssertionError("primitive rank must be the largest left companion hit")
    if d not in offsets:
        raise AssertionError("terminal cancellation must be another companion hit")
    if rank_from_universal_companion(prime) != rank:
        raise AssertionError("last-hit rank reconstruction changed")
    if e - d != rank - 2 or prime != 4 * e - 2 * d + 5:
        raise AssertionError("last-hit affine geometry changed")
    companion_branch_zero_is_unique(prime, d)
    companion_branch_zero_is_unique(prime, e)
    return d, e, companion_kind(prime)


def twin_terminal_offset_mod3_obstruction(rank: int, prime: int) -> int:
    """A dangerous large-prime terminal offset is never 0 modulo three."""
    d, _ = terminal_companion_offsets(rank, prime)
    if rank % 3:
        raise ValueError("rank must be a nontrivial twin-center multiple of three")
    if prime != 4 * rank + 2 * d - 3:
        raise AssertionError("terminal offset prime identity changed")
    if d % 3 == 0:
        if prime % 3:
            raise AssertionError("d=0 mod3 must make q divisible by three")
        if prime > 3:
            raise ValueError("prime q cannot arise from a terminal offset divisible by three")
    return d % 3
