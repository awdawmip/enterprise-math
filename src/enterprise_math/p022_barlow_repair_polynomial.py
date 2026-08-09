"""Repair-bit polynomial of the two-sided Barlow coordination quotient.

Every coordination-history fiber has size 2^r, where r=E+B is the exact
orientation-plus-side repair dimension.  Record how many quotient histories
have each repair dimension:

    R_N(z)=sum_r a_(N,r) z^r.

This polynomial is a complete re-encoding of the P011 fiber-size profile because
fiber sizes are powers of two.  A finite weighted walk recursion in the chamber
0<=a<=b computes it exactly.
"""

from __future__ import annotations

from collections import defaultdict
from math import comb

from .p022_barlow_two_sided_repair import total_two_sided_repair_bit_load

ChamberState = tuple[int, int]
RepairPolynomial = tuple[int, ...]  # coefficient index = repair-bit count


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def chamber_successors(state: ChamberState) -> tuple[ChamberState, ...]:
    """Distinct unordered absolute successors of ``0<=a<=b``."""
    a, b = state
    if a < 0 or b < a:
        raise ValueError("state must satisfy 0<=a<=b")
    a_next = (1,) if a == 0 else (a - 1, a + 1)
    b_next = (1,) if b == 0 else (b - 1, b + 1)
    return tuple(
        sorted(
            {
                tuple(sorted((left, right)))
                for left in a_next
                for right in b_next
            }
        )
    )


def transition_repair_bits(previous: ChamberState, current: ChamberState) -> int:
    """One-step repair event count: zero departures plus diagonal split."""
    if current not in chamber_successors(previous):
        raise ValueError("current is not a legal chamber successor")
    zero_departures = int(previous[0] == 0) + int(previous[1] == 0)
    split = int(previous[0] == previous[1] and current[0] != current[1])
    return zero_departures + split


def repair_polynomial_coefficients(length: int) -> RepairPolynomial:
    """Exact coefficient vector ``a_(N,r)`` by weighted chamber recursion."""
    _require_natural("length", length)
    # state -> {repair_bits: quotient-history count}
    state_polynomials: dict[ChamberState, dict[int, int]] = {(0, 0): {0: 1}}

    for _ in range(length):
        next_polynomials: dict[ChamberState, dict[int, int]] = defaultdict(dict)
        for state, polynomial in state_polynomials.items():
            for successor in chamber_successors(state):
                cost = transition_repair_bits(state, successor)
                target = next_polynomials[successor]
                for repair_bits, count in polynomial.items():
                    key = repair_bits + cost
                    target[key] = target.get(key, 0) + count
        state_polynomials = dict(next_polynomials)

    total: dict[int, int] = {}
    for polynomial in state_polynomials.values():
        for repair_bits, count in polynomial.items():
            total[repair_bits] = total.get(repair_bits, 0) + count

    if not total:
        return (1,)
    degree = max(total)
    return tuple(total.get(power, 0) for power in range(degree + 1))


def evaluate_repair_polynomial(coefficients: RepairPolynomial, value: int) -> int:
    """Integer evaluation of ``sum_r a_r value^r``."""
    if not isinstance(coefficients, tuple) or not coefficients:
        raise ValueError("coefficients must be a nonempty tuple")
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    return sum(coefficient * (value ** power) for power, coefficient in enumerate(coefficients))


def repair_polynomial_derivative_at_two(coefficients: RepairPolynomial) -> int:
    """Return ``R'_N(2)`` exactly."""
    return sum(
        power * coefficient * (2 ** (power - 1))
        for power, coefficient in enumerate(coefficients)
        if power
    )


def coordination_history_image_size(length: int) -> int:
    """Number of represented coordination histories ``R_N(1)``."""
    return sum(repair_polynomial_coefficients(length))


def coordination_history_image_size_closed(length: int) -> int:
    """Closed free-endpoint type-C2 chamber count.

    The unordered absolute-pair path ``0<=a<=b`` maps after the shift
    ``(a,b)->(a+1,b+3)`` to a lock-step walk in the strict chamber
    ``0<x1<x2`` starting at ``(1,3)``.  The resulting free-endpoint count is a
    classical Weyl-chamber/Narayana-Catalan sequence.

    For N=2m:
        I_N=(2m+1) Catalan(m)^2.

    For N=2m+1:
        I_N=(m+2) Catalan(m+1)^2 / 2.
    """
    _require_natural("length", length)
    if length % 2 == 0:
        half = length // 2
        catalan = comb(2 * half, half) // (half + 1)
        return (2 * half + 1) * catalan * catalan

    half = (length - 1) // 2
    next_index = half + 1
    catalan = comb(2 * next_index, next_index) // (next_index + 1)
    numerator = (half + 2) * catalan * catalan
    if numerator % 2:
        raise AssertionError("odd Barlow chamber count must be integral")
    return numerator // 2


def microscopic_domain_from_repair_polynomial(length: int) -> int:
    """``R_N(2)=4^N`` exact reconstruction of all microscopic word pairs."""
    coefficients = repair_polynomial_coefficients(length)
    value = evaluate_repair_polynomial(coefficients, 2)
    if value != 4 ** length:
        raise AssertionError("repair polynomial must reconstruct microscopic domain")
    return value


def collision_coefficients_from_repair_polynomial(
    coefficients: RepairPolynomial,
) -> tuple[int, ...]:
    """P011 collision coefficients from the bit-dimension profile.

    There are ``a_r`` fibers of size ``2^r``. Hence

        J_k=sum_r a_r C(2^r,k).
    """
    maximum_repair = max(
        (power for power, count in enumerate(coefficients) if count),
        default=0,
    )
    maximum_fiber = 2 ** maximum_repair
    return tuple(
        sum(
            history_count * comb(2 ** repair_bits, order)
            for repair_bits, history_count in enumerate(coefficients)
            if history_count and 2 ** repair_bits >= order
        )
        for order in range(1, maximum_fiber + 1)
    )


def total_repair_load_from_polynomial(length: int) -> int:
    """``2 R'_N(2)`` equals total repair bits over microscopic windows."""
    coefficients = repair_polynomial_coefficients(length)
    load = 2 * repair_polynomial_derivative_at_two(coefficients)
    expected = total_two_sided_repair_bit_load(length)
    if load != expected:
        raise AssertionError("repair-polynomial derivative must match event count")
    return load
