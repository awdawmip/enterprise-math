"""Divisor re-entry ladder for a primitive twin Franel source.

Let r be a nontrivial twin-prime center.  The source A-coordinate is flanked by
new central-binomial prime generators

    p_- = 2r-1,   p_+ = 2r+1.

Odd multiples of either source prime create later composite odd boundaries.
A particularly clean family occurs when the multiplier is 2d-1 and d divides
r (right source) or r-1 (left source).

Right gate.  If d|r and r>2d, put

    N_d^+ = (2d-1)r+d,
    2N_d^+-1 = (2d-1)(2r+1).

The factorization d|N_d^+ makes every denominator integer-basis index strictly
below r.  The exact high A-support is therefore

    -e_r + e_(r+1) + e_(N_d^+-1).

Left gate.  If d|(r-1) and r-1>2d, put

    N_d^- = (2d-1)r-d+1,
    2N_d^--1 = (2d-1)(2r-1).

Again the denominator support lies below r, and the exact high A-support is

    +e_r + e_(N_d^--1).

For a q-adic primitive source, all coordinates below r vanish and F_(r+1) is a
q-unit.  If q is beyond the half-segment horizon, p-Lucas reduces adjacent
zero/nonzero behavior at N_d^+-1,N_d^+ (or N_d^--1,N_d^-) to the single-digit
zero alphabet.  A vanishing defect then transports the positive source depth
to one new zero.

The transported zero excludes an open interval of possible q values:

    right: ((2d-2)r+d-1,  2dr+d),
    left:  ((2d-2)r-d+1, 2dr-d+2).

Thus any already-established lower bound beyond the left endpoint upgrades to
the right endpoint.  Taking d=2 on whichever of r,r-1 is even gives the 4r
scale; every nontrivial twin center has 3|r, so d=3 on the right gives the
universal 6r scale.  Additional small divisors of r or r-1 continue the ladder.

The central-binomial prime-generation recurrence is established P022
infrastructure.  This file records the exact divisor-family support theorem and
its linear escape intervals.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
)
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


def _require_gate(rank: int, divisor: int) -> None:
    if rank < 6 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin-prime center")
    if isinstance(divisor, bool) or not isinstance(divisor, int) or divisor < 2:
        raise ValueError("divisor must be an integer at least two")


def right_divisor_reentry_segment(rank: int, divisor: int) -> int:
    _require_gate(rank, divisor)
    if rank % divisor:
        raise ValueError("right divisor gate requires d|r")
    if rank <= 2 * divisor:
        raise ValueError("right divisor gate requires r>2d")
    return (2 * divisor - 1) * rank + divisor


def left_divisor_reentry_segment(rank: int, divisor: int) -> int:
    _require_gate(rank, divisor)
    if (rank - 1) % divisor:
        raise ValueError("left divisor gate requires d|(r-1)")
    if rank - 1 <= 2 * divisor:
        raise ValueError("left divisor gate requires r-1>2d")
    return (2 * divisor - 1) * rank - divisor + 1


def right_divisor_high_support(
    rank: int,
    divisor: int,
) -> tuple[tuple[int, int], ...]:
    """Exact support at indices >=r for the right d-gate."""
    segment = right_divisor_reentry_segment(rank, divisor)
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, -1), (rank + 1, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("right divisor re-entry escaped the clean high support")
    return high


def left_divisor_high_support(
    rank: int,
    divisor: int,
) -> tuple[tuple[int, int], ...]:
    """Exact support at indices >=r for the left d-gate."""
    segment = left_divisor_reentry_segment(rank, divisor)
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("left divisor re-entry escaped the clean high support")
    return high


def right_divisor_forbidden_interval(rank: int, divisor: int) -> tuple[int, int]:
    """Open q-interval excluded by a vanishing clean right gate."""
    right_divisor_reentry_segment(rank, divisor)
    return (
        (2 * divisor - 2) * rank + divisor - 1,
        2 * divisor * rank + divisor,
    )


def left_divisor_forbidden_interval(rank: int, divisor: int) -> tuple[int, int]:
    """Open q-interval excluded by a vanishing clean left gate."""
    left_divisor_reentry_segment(rank, divisor)
    return (
        (2 * divisor - 2) * rank - divisor + 1,
        2 * divisor * rank - divisor + 2,
    )


def available_divisor_gates(
    rank: int,
    max_divisor: int,
) -> tuple[tuple[int, str, tuple[int, int]], ...]:
    """List every clean divisor gate available up to ``max_divisor``."""
    if max_divisor < 2:
        raise ValueError("max_divisor must be at least two")
    output = []
    for divisor in range(2, max_divisor + 1):
        if rank % divisor == 0 and rank > 2 * divisor:
            output.append(
                (
                    divisor,
                    "right",
                    right_divisor_forbidden_interval(rank, divisor),
                )
            )
        if (rank - 1) % divisor == 0 and rank - 1 > 2 * divisor:
            output.append(
                (
                    divisor,
                    "left",
                    left_divisor_forbidden_interval(rank, divisor),
                )
            )
    return tuple(output)


def formal_divisor_barrier_ladder(
    rank: int,
    initial_strict_lower_bound: int,
    max_divisor: int,
) -> tuple[tuple[int, str, int, int], ...]:
    """Propagate a strict q lower bound through all currently usable gates.

    This is an arithmetic consequence of the divisor intervals only.  Each
    returned tuple is ``(d,side,old_bound,new_bound)``.  It assumes the
    corresponding defect vanishes and upgrades whenever the current strict
    lower bound is already at or beyond the forbidden interval's left edge.
    """
    _require_gate(rank, 2)
    if initial_strict_lower_bound < 0:
        raise ValueError("initial bound must be non-negative")
    gates = available_divisor_gates(rank, max_divisor)
    bound = initial_strict_lower_bound
    used: list[tuple[int, str, int, int]] = []
    progress = True
    while progress:
        progress = False
        for divisor, side, interval in gates:
            lower, upper = interval
            if upper <= bound or lower > bound:
                continue
            old = bound
            bound = upper
            used.append((divisor, side, old, bound))
            progress = True
            break
    return tuple(used)
