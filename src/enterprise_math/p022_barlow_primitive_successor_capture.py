"""Primitive Franel events enter the defect lattice within one step.

Let p be a primitive prime divisor of the Franel sequence at rank r:

    p | F_r,   p does not divide F_j for 1 <= j < r,

and put z=v_p(F_r)>0.

There are two automatic defect-capture mechanisms.

1. If 2r-1 is composite, D_r exists and the existing primitive-defect theorem
   gives v_p(D_r)=+z.
2. If 2r-1 is prime but 2r+1 is composite, D_(r+1) exists.  In the canonical
   central-binomial relation for A_(r+1), the coefficient of A_r is exactly
   one and every other Franel index is <r.  Also F_(r+1) is a p-unit because
   primitive Franel zeros cannot be adjacent.  Hence

       v_p(D_(r+1))=-z.

Therefore a primitive Franel event is captured at r or r+1 unless both
2r-1 and 2r+1 are prime.  The latter is exactly the condition that r is the
center of an odd twin-prime pair.  For r>2 such a center must satisfy
r=0 (mod 3).  Hence every primitive event at r>2 with r not divisible by
three is automatically captured within one defect step.

Twin-prime terminology and elementary prime-factor bounds are classical.  The
P022 content is the exact interaction with the canonical Franel defect basis.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)
from .p022_barlow_primitive_defect_criterion import (
    is_primitive_franel_divisor,
    primitive_defect_pivot,
)


def _require_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")


def primitive_capture_location(rank: int) -> int | None:
    """Return r, r+1, or None for the immediate twin-prime deferral case."""
    _require_rank(rank)
    if not _is_prime(2 * rank - 1):
        return rank
    if not _is_prime(2 * rank + 1):
        return rank + 1
    return None


def mod3_forced_capture_location(rank: int) -> int | None:
    """Return the defect column forced by rank mod 3 alone, when available.

    For r>2:

    - r=2 mod 3 forces 2r-1 to be a composite multiple of three, so D_r
      captures any primitive event at r;
    - r=1 mod 3 forces 2r+1 to be a composite multiple of three.  If D_r does
      not already exist, D_(r+1) is therefore forced to exist;
    - r=0 mod 3 has no such divisibility obstruction, so this helper returns
      None even when a particular r happens to be captured for another reason.

    Rank 2 is the exceptional center of the twin primes 3 and 5 and is not
    covered by the r>2 statement.
    """
    _require_rank(rank)
    if rank <= 2 or rank % 3 == 0:
        return None
    if rank % 3 == 2:
        if (2 * rank - 1) % 3 != 0 or 2 * rank - 1 <= 3:
            raise AssertionError("r=2 mod 3 must force a composite current boundary")
        if _is_prime(2 * rank - 1):
            raise AssertionError("forced current boundary cannot be prime")
        return rank
    if (2 * rank + 1) % 3 != 0 or 2 * rank + 1 <= 3:
        raise AssertionError("r=1 mod 3 must force a composite successor boundary")
    if _is_prime(2 * rank + 1):
        raise AssertionError("forced successor boundary cannot be prime")
    return rank if not _is_prime(2 * rank - 1) else rank + 1


def twin_prime_deferral_requires_rank_multiple_of_three(rank: int) -> bool:
    """Certify that every twin-prime deferral center r>2 lies in 3Z."""
    _require_rank(rank)
    if not is_twin_prime_deferral_center(rank):
        raise ValueError("rank is not a twin-prime deferral center")
    if rank == 2:
        return True
    if rank % 3 != 0:
        raise AssertionError("an odd twin-prime center above 3 must be 0 mod 3")
    return True


def is_twin_prime_deferral_center(rank: int) -> bool:
    _require_rank(rank)
    return _is_prime(2 * rank - 1) and _is_prime(2 * rank + 1)


def successor_relation_previous_exponent(rank: int) -> int:
    """For composite 2r+1, certify alpha_r=1 and all other indices <r."""
    _require_rank(rank)
    successor = rank + 1
    if _is_prime(2 * rank + 1):
        raise ValueError("successor odd boundary must be composite")
    exponents = composite_A_relation_exponents(successor)
    exponent_map = dict(exponents)
    if exponent_map.get(rank) != 1:
        raise AssertionError("successor relation must contain A_r exactly once")
    if any(index >= rank for index, _ in exponents if index != rank):
        raise AssertionError("all other successor relation indices must be below r")
    return 1


def primitive_successor_capture_valuation(rank: int, prime: int) -> int:
    """If r is prime-boundary and r+1 composite-boundary, return -v_p(F_r)."""
    _require_rank(rank)
    if not _is_prime(2 * rank - 1):
        raise ValueError("this helper is for a prime odd boundary at r")
    if _is_prime(2 * rank + 1):
        raise ValueError("successor odd boundary must be composite")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    successor_relation_previous_exponent(rank)

    depth = p_adic_valuation(triple_moment_factor(rank), prime)
    if depth <= 0:
        raise AssertionError("primitive Franel depth must be positive")
    if p_adic_valuation(triple_moment_factor(rank + 1), prime) != 0:
        raise AssertionError("primitive Franel zero cannot persist to the adjacent term")

    actual = franel_defect_valuation(rank + 1, prime)
    expected = -depth
    if actual != expected:
        raise AssertionError(
            "successor defect must capture the primitive event with negative depth"
        )
    return actual


def primitive_event_capture_valuation(
    rank: int,
    prime: int,
) -> tuple[int | None, int | None]:
    """Return (capture column, valuation), or (None,None) at twin-prime deferral."""
    _require_rank(rank)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    location = primitive_capture_location(rank)
    if location is None:
        return None, None
    if location == rank:
        return rank, primitive_defect_pivot(rank, prime)
    return rank + 1, primitive_successor_capture_valuation(rank, prime)


def primitive_event_is_captured_within_one_step(rank: int, prime: int) -> bool:
    """True exactly when the two neighboring odd boundaries are not both prime."""
    location, valuation = primitive_event_capture_valuation(rank, prime)
    if location is None:
        if not is_twin_prime_deferral_center(rank):
            raise AssertionError("only twin-prime centers may defer immediate capture")
        return False
    if valuation == 0:
        raise AssertionError("captured primitive event must give a nonzero valuation")
    return True
