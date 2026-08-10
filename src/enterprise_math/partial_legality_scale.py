"""Operation-generated coarse scales from legality-sensitive partial translations.

This module is a P008/P018 specialization of the FQ-006 partial-operation
quotient semantics.  It does not reimplement the generic partial quotient engine.

Fine state is ``N_0``.  A negative step ``-u`` is legal only when the current
state is at least ``u``.  Positive steps are total.

Three exact regimes are exposed.

1. A single partial decrement by ``d`` generates the block quotient
   ``q_d(n)=floor(n/d)`` from legality alone: ``q_d(n)`` is exactly the maximum
   number of repeated ``-d`` actions that remain legal.

2. A one-sided family of decrements ``-U`` generates basin boundaries at the
   additive monoid ``<U>``.  Two states are legality-equivalent iff no reachable
   decrement sum lies strictly between them.  Thus basin widths are consecutive
   gaps in ``<U>``; for finite positive ``U`` they are eventually the gcd grain
   after the numerical-semigroup boundary layer.

3. If both ``+u`` and partial ``-u`` are available for every ``u in U``, the
   legality quotient is exactly ``q_g`` where ``g=gcd(U)``.  A Bezout word with
   net displacement ``-g`` can be ordered so that its minimum prefix displacement
   is ``-g``; repeated copies are legal exactly from states ``n >= k*g``.
   Hence the signed future language distinguishes exactly the block levels
   ``floor(n/g)``.

The generic partial-algebra/strong-congruence machinery is prior mathematics.
The project-specific role of this module is the reverse bridge
``operation legality -> basin geometry -> scalar scale when representable``.
"""

from __future__ import annotations

from collections.abc import Iterable
from math import gcd


def _positive_steps(steps: Iterable[int]) -> tuple[int, ...]:
    values = tuple(sorted(set(steps)))
    if not values:
        raise ValueError("at least one positive step is required")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("steps must be positive integers")
    return values


def action_gcd(steps: Iterable[int]) -> int:
    """Positive gcd grain of a nonempty positive step family."""
    values = _positive_steps(steps)
    grain = 0
    for value in values:
        grain = gcd(grain, value)
    return grain


def reachable_decrement_sums(
    steps: Iterable[int], cutoff: int
) -> tuple[int, ...]:
    """Elements of the additive monoid ``<steps>`` not exceeding ``cutoff``."""
    values = _positive_steps(steps)
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")

    reached = {0}
    frontier = [0]
    while frontier:
        total = frontier.pop()
        for step in values:
            nxt = total + step
            if nxt <= cutoff and nxt not in reached:
                reached.add(nxt)
                frontier.append(nxt)
    return tuple(sorted(reached))


def single_decrement_level(n: int, step: int) -> int:
    """Legality quotient for repeated partial decrement ``n -> n-step``."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if isinstance(step, bool) or not isinstance(step, int) or step <= 0:
        raise ValueError("step must be a positive integer")
    return n // step


def one_sided_legality_rank(n: int, steps: Iterable[int]) -> int:
    """Canonical class index for the decrement-only legality quotient.

    The signature at ``n`` is the set of reachable decrement totals at most
    ``n``.  Since these signatures are nested as ``n`` grows, the class index is
    the number of positive reachable totals not exceeding ``n``.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return len(reachable_decrement_sums(steps, n)) - 1


def one_sided_basin_boundaries(
    steps: Iterable[int], cutoff: int
) -> tuple[int, ...]:
    """Legality-basin lower boundaries through ``cutoff``.

    The boundaries are exactly the reachable additive-monoid sums.
    """
    return reachable_decrement_sums(steps, cutoff)


def one_sided_complete_basin_widths(
    steps: Iterable[int], cutoff: int
) -> tuple[int, ...]:
    """Widths between consecutive legality boundaries through ``cutoff``."""
    boundaries = one_sided_basin_boundaries(steps, cutoff)
    return tuple(
        right - left for left, right in zip(boundaries, boundaries[1:])
    )


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def bezout_coefficients(
    steps: Iterable[int],
) -> tuple[tuple[int, ...], tuple[int, ...], int]:
    """Return sorted steps, coefficients and their positive gcd.

    The coefficients ``c_i`` satisfy ``sum(c_i * step_i) == gcd(steps)``.
    """
    values = _positive_steps(steps)
    coefficients = [1]
    grain = values[0]
    for value in values[1:]:
        next_grain, left, right = _extended_gcd(grain, value)
        coefficients = [coefficient * left for coefficient in coefficients]
        coefficients.append(right)
        grain = next_grain
    if sum(c * u for c, u in zip(coefficients, values)) != grain:
        raise AssertionError("Bezout reconstruction failed")
    return values, tuple(coefficients), grain


def signed_gcd_probe_word(steps: Iterable[int]) -> tuple[int, ...]:
    """Construct a signed word whose net and minimum prefix are both ``-g``.

    Positive entries are total increments.  Negative entries are partial
    decrements.  Therefore the returned word is legal at ``n`` exactly when
    ``n >= g``, and ``k`` repeated copies are legal exactly when ``n >= k*g``.
    """
    values, coefficients, grain = bezout_coefficients(steps)

    target_coefficients = tuple(-coefficient for coefficient in coefficients)

    positive_part: list[int] = []
    negative_part: list[int] = []
    for value, coefficient in zip(values, target_coefficients):
        if coefficient > 0:
            positive_part.extend([value] * coefficient)
        elif coefficient < 0:
            negative_part.extend([-value] * (-coefficient))

    word = tuple(positive_part + negative_part)
    if not word or sum(word) != -grain:
        raise AssertionError("signed gcd probe must have net displacement -g")

    displacement = 0
    minimum = 0
    for signed_step in word:
        displacement += signed_step
        minimum = min(minimum, displacement)
    if minimum != -grain:
        raise AssertionError("signed gcd probe must have minimum prefix -g")
    return word


def signed_word_is_legal(n: int, word: Iterable[int]) -> bool:
    """Whether every prefix of a signed translation word remains in ``N_0``."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    current = n
    for signed_step in word:
        if isinstance(signed_step, bool) or not isinstance(signed_step, int):
            raise ValueError("word steps must be integers")
        current += signed_step
        if current < 0:
            return False
    return True


def signed_legality_level(n: int, steps: Iterable[int]) -> int:
    """Exact operation-generated block level for the two-sided step family."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return n // action_gcd(steps)
