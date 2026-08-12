"""Direct terminal transfer for a primitive Franel zero.

Let the Franel recurrence be

    (n+1)^2 y_(n+1)=(7n^2+7n+2)y_n+8n^2 y_(n-1).

For r>=2 define C_r by starting the same recurrence at

    y_(r-1)=1,  y_r=0

and propagating to y_(2r-2).  Thus C_r is a fixed rational depending only on r.

If q is a primitive Franel prime at rank r, then q>=2r+1.  Every denominator
(n+1)^2 used between r and 2r-3 is therefore a q-adic unit, while F_(r-1) is a
q-unit by primitivity.  Normalizing the real Franel solution modulo q by
F_(r-1) gives exactly the transfer solution above.  Hence

    F_(2r-2) / F_(r-1) = C_r                         (mod q),

and terminal common-zero status is equivalent to C_r=0 mod q.  This removes
the moving prime q entirely and is valid throughout the full primitive range,
not only in the large-midpoint window.

The transfer is the same obstruction as the fixed half-integer gap continuant
R_r, up to an explicit small-prime scale:

    R_r = lambda_r C_r,

    lambda_r = (-8)^(r-1) ((2r-2)!)^2
               / (2^(r+6) (r!)^2 r^2).

All numerator/denominator prime factors of lambda_r are <=2r-2 (apart from 2),
so every primitive q>=2r+1 sees lambda_r as a q-adic unit.  Thus C_r and R_r
have exactly the same primitive large-prime zero obstruction, while C_r gives
the direct recurrence interpretation for every primitive q.

The Franel recurrence and two-solution/Casoratian formalism are prior art.  The
P022 contribution is the terminal normalization, its exact primitive-zero
criterion, and the bridge to the previously isolated fixed continuant.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, gcd

from .p022_barlow_franel_gap_continuant import eliminated_gap_transfer
from .p022_barlow_low_order_identifiability import triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor


def terminal_transfer(rank: int) -> Fraction:
    """Return C_r from state (y_(r-1),y_r)=(1,0)."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    previous = Fraction(1, 1)
    current = Fraction(0, 1)
    for n in range(rank, 2 * rank - 2):
        following = Fraction(
            (7 * n * n + 7 * n + 2) * current + 8 * n * n * previous,
            (n + 1) ** 2,
        )
        previous, current = current, following
    return current


def terminal_transfer_scale(rank: int) -> Fraction:
    """lambda_r with R_r=lambda_r*C_r."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")
    return Fraction(
        (-8) ** (rank - 1) * factorial(2 * rank - 2) ** 2,
        2 ** (rank + 6) * factorial(rank) ** 2 * rank**2,
    )


def terminal_transfer_matches_gap_continuant(rank: int) -> bool:
    """Exact characteristic-zero bridge R_r=lambda_r*C_r."""
    transfer = terminal_transfer(rank)
    predicted = terminal_transfer_scale(rank) * transfer
    actual = Fraction(eliminated_gap_transfer(rank), 1)
    if predicted != actual:
        raise AssertionError("direct terminal transfer and fixed gap continuant disagree")
    return True


def _fraction_mod(value: Fraction, prime: int) -> int:
    denominator = value.denominator % prime
    if gcd(denominator, prime) != 1:
        raise ValueError("transfer denominator is not a unit modulo the prime")
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def primitive_terminal_transfer_residue(rank: int, prime: int) -> tuple[int, int]:
    """Return actual/predicted F_(2r-2)/F_(r-1) modulo a primitive q."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    if prime < 2 * rank + 1:
        raise AssertionError("odd primitive Franel prime violates the reflection size bound")
    previous = triple_moment_factor(rank - 1) % prime
    if previous == 0:
        raise AssertionError("primitivity makes F_(r-1) a q-unit")
    terminal = triple_moment_factor(2 * rank - 2) % prime
    actual = terminal * pow(previous, -1, prime) % prime
    predicted = _fraction_mod(terminal_transfer(rank), prime)
    if actual != predicted:
        raise AssertionError("primitive terminal value disagrees with direct transfer")
    return actual, predicted


def primitive_terminal_zero_iff_transfer_zero(rank: int, prime: int) -> bool:
    """Certify q|F_(2r-2) iff q divides the rational transfer C_r."""
    actual, predicted = primitive_terminal_transfer_residue(rank, prime)
    if (actual == 0) != (predicted == 0):
        raise AssertionError("transfer residue must preserve terminal zero status")
    return actual == 0


def terminal_transfer_fixed_gcd(rank: int) -> int:
    """gcd(F_r,num(C_r)), the fixed terminal common-zero obstruction."""
    transfer = terminal_transfer(rank)
    return gcd(triple_moment_factor(rank), abs(transfer.numerator))


def terminal_transfer_large_common_primes(rank: int) -> tuple[int, ...]:
    """Prime factors >rank of gcd(F_r,num(C_r)); finite diagnostic helper."""
    value = terminal_transfer_fixed_gcd(rank)
    factors = []
    remaining = value
    candidate = 2
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            if candidate > rank:
                factors.append(candidate)
            while remaining % candidate == 0:
                remaining //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1 and remaining > rank:
        factors.append(remaining)
    return tuple(factors)
