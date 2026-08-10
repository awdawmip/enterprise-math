"""Close the dangerous q=3r-1 twin-escape boundary by a later defect.

Let r be a nontrivial twin-prime deferral center and let q=3r-1 be prime.
Suppose q is primitive for the Franel sequence at rank r.  Earlier P022 work
shows that if all first-reentry defects through T=2r-1 vanish, then every
positive Franel q-depth strictly inside the blackout must lie at another
nontrivial twin-prime center and z_(T-1)=z_r, z_T=0.

At the exact reflection boundary q=3r-1 this is much more rigid.
Jarvis--Verrill reflection maps d to q-1-d=3r-2-d.  Any interior zero d in
r+2..2r-4 would have a reflected zero in the same interval.  Complete escape
would force both to be twin centers, hence both divisible by three, while their
sum is 3r-2=1 (mod 3), impossible.  The remaining interior endpoint 2r-3
reflects to r+1 and is excluded by recurrence nonadjacency.  Primitivity rules
out all zero digits below r, and reflection then rules out all zero digits above
2r-2.  Therefore complete first-reentry escape forces the entire q-zero digit
alphabet to be exactly

    Z_q = {r, 2r-2}.

This removes the earlier need to prove that q cannot divide F_((q+1)/3).
Even if such a boundary primitive zero exists, it cannot stay hidden.
Indeed D_q always exists because

    2q-1 = 3(2r-1)

is composite.  The canonical A-relation at segment q has high support

    A_r^(+1) A_((q-1)/2)^(+1) A_((q+1)/2)^(-1) A_(q-1)^(+1),

with all remaining indices below r.  Under Z_q={r,2r-2}, only A_r carries
positive q-depth; p-Lucas also gives q not dividing F_q.  Consequently

    v_q(D_q) = -v_q(F_r) != 0.

Thus every primitive event on the boundary q=3r-1 is captured no later than
segment q: either an earlier first-reentry defect is already nonzero, or D_q
captures it with the exact negative primitive depth.

Franel reflection, recurrence nonadjacency, and p-Lucas are prior art.  The
P022 contribution is the interaction with the deleted-edge twin kernel and the
canonical central-binomial defect relation at q.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_franel_zero_geometry import (
    zero_digits_are_nonadjacent,
    zero_digits_are_reflection_symmetric,
)
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_twin_defect_difference import (
    primitive_twin_first_defect_incidence,
    twin_blackout_target,
    twin_zero_local_visibility,
)


def boundary_prime(rank: int) -> int:
    """Return q=3r-1 after certifying the prime reflection boundary."""
    twin_blackout_target(rank)  # validates the twin-center hypothesis
    prime = 3 * rank - 1
    if not _is_prime(prime):
        raise ValueError("3r-1 must be prime")
    if rank % 3:
        raise AssertionError("every nontrivial twin center is divisible by three")
    if rank % 2:
        raise AssertionError("primality of 3r-1 forces the twin center to be even")
    return prime


def boundary_reflection(index: int, rank: int) -> int:
    prime = boundary_prime(rank)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must be a q-digit")
    return prime - 1 - index


def boundary_reflected_interior_pair_cannot_both_be_twin(rank: int, index: int) -> bool:
    """Mod-3 obstruction for a reflected pair strictly inside the blackout."""
    target = twin_blackout_target(rank)
    prime = boundary_prime(rank)
    if not rank + 2 <= index <= target - 3:
        raise ValueError("index must lie in r+2..T-3")
    reflected = boundary_reflection(index, rank)
    if not rank + 2 <= reflected <= target - 3:
        raise AssertionError("boundary reflection must preserve the strict interior")
    if index + reflected != prime - 1 or (prime - 1) % 3 != 1:
        raise AssertionError("boundary reflected-pair arithmetic changed")

    left_twin = twin_zero_local_visibility(index) == (False, False)
    right_twin = twin_zero_local_visibility(reflected) == (False, False)
    if left_twin and right_twin:
        if index % 3 or reflected % 3:
            raise AssertionError("nontrivial twin centers must be divisible by three")
        raise AssertionError("two twin centers cannot sum to 1 modulo three")
    return True


def boundary_escape_zero_support_from_kernel(
    rank: int, zero_digits: tuple[int, ...]
) -> tuple[int, int]:
    """Under complete first-reentry kernel hypotheses, force Z_q={r,2r-2}.

    ``zero_digits`` is an abstract q-digit zero alphabet satisfying the same
    reflection, nonadjacency, primitivity, and deleted-edge hiding conditions
    as an escaping primitive Franel row.  This helper isolates the finite
    combinatorial proof without evaluating any Franel number.
    """
    target = twin_blackout_target(rank)
    prime = boundary_prime(rank)
    if not zero_digits or tuple(sorted(set(zero_digits))) != zero_digits:
        raise ValueError("zero_digits must be a nonempty increasing tuple")
    if zero_digits[0] != rank:
        raise ValueError("rank must be the first positive zero digit")
    if any(not 1 <= digit < prime for digit in zero_digits):
        raise ValueError("all zero digits must lie in 1..q-1")
    zero_set = set(zero_digits)
    if {prime - 1 - digit for digit in zero_set} != zero_set:
        raise ValueError("zero alphabet must be reflection symmetric")
    if any(digit + 1 in zero_set for digit in zero_set):
        raise ValueError("adjacent positive zero digits are forbidden")
    if target - 1 not in zero_set:
        raise AssertionError("reflection of the primitive rank must be T-1")

    for digit in zero_digits:
        if digit < rank:
            raise AssertionError("primitivity forbids a zero below rank")
        if digit > target - 1:
            reflected = prime - 1 - digit
            if reflected >= rank:
                raise AssertionError("a zero above T-1 must reflect below rank")
            raise AssertionError("reflection contradicts primitive first zero")
        if digit in (rank, target - 1):
            continue
        if digit == rank + 1:
            raise AssertionError("adjacent zero after the primitive rank is impossible")
        if digit == target - 2:
            if boundary_reflection(digit, rank) != rank + 1:
                raise AssertionError("terminal-neighbor reflection identity changed")
            raise AssertionError("T-2 would reflect to the forbidden zero r+1")
        if twin_zero_local_visibility(digit) != (False, False):
            raise ValueError("complete escape requires every interior zero to be a twin center")
        reflected = boundary_reflection(digit, rank)
        if reflected not in zero_set:
            raise AssertionError("reflection partner missing")
        if twin_zero_local_visibility(reflected) != (False, False):
            raise ValueError("reflection partner must also be hidden by deleted edges")
        boundary_reflected_interior_pair_cannot_both_be_twin(rank, digit)
        raise AssertionError("strict interior zero survived the mod-3 obstruction")

    expected = (rank, target - 1)
    if zero_digits != expected:
        raise AssertionError("boundary complete escape must have exactly two zero digits")
    return expected


def boundary_q_relation_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """High part of the canonical A-relation for the guaranteed capture D_q."""
    prime = boundary_prime(rank)
    if 2 * prime - 1 != 3 * (2 * rank - 1):
        raise AssertionError("2q-1 boundary factorization changed")
    if _is_prime(2 * prime - 1):
        raise AssertionError("D_q must exist because 2q-1 is composite")
    middle = (prime + 1) // 2
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(prime)
        if index >= rank
    )
    expected = (
        (rank, 1),
        (middle - 1, 1),
        (middle, -1),
        (prime - 1, 1),
    )
    if high != expected:
        raise AssertionError("boundary D_q relation escaped the four-term high support")
    return high


def boundary_primitive_capture_no_later_than_q(rank: int, prime: int) -> tuple[int, int]:
    """Exact conditional theorem for an actual primitive boundary Franel row.

    Returns the first nonzero first-reentry defect when one exists.  Otherwise
    certifies the two-zero alphabet and returns the guaranteed later capture
    ``(q,-v_q(F_r))``.
    """
    expected_prime = boundary_prime(rank)
    if prime != expected_prime:
        raise ValueError("prime must equal the reflection boundary q=3r-1")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("q must be primitive for the Franel sequence at rank r")

    earlier = primitive_twin_first_defect_incidence(rank, prime)
    if earlier is not None:
        return earlier

    zero_digits_are_reflection_symmetric(prime)
    zero_digits_are_nonadjacent(prime)
    zeros = franel_zero_digits(prime)
    boundary_escape_zero_support_from_kernel(rank, zeros)
    boundary_q_relation_high_support(rank)

    depth = p_adic_valuation(triple_moment_factor(rank), prime)
    if depth <= 0:
        raise AssertionError("primitive depth must be positive")
    actual = franel_defect_valuation(prime, prime)
    if actual != -depth:
        raise AssertionError("boundary D_q must capture exactly the negative primitive depth")
    return prime, actual
