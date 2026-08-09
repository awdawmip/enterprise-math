"""Repair-bit polynomial of the two-sided Barlow coordination quotient.

Every coordination-history fiber has size 2^r, where r=E+B is the exact
orientation-plus-side repair dimension. Record

    R_N(z)=sum_r a_(N,r) z^r.

This is a complete re-encoding of the P011 fiber-size profile because all fiber
sizes are powers of two. A finite weighted walk recursion in 0<=a<=b computes
it exactly. The lowest and highest nonzero coefficients also have closed forms.
"""

from __future__ import annotations

from collections import defaultdict
from math import comb

from .p022_barlow_excursion_repair import absolute_history_count_with_excursions
from .p022_barlow_two_sided_repair import total_two_sided_repair_bit_load

ChamberState = tuple[int, int]
RepairPolynomial = tuple[int, ...]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def chamber_successors(state: ChamberState) -> tuple[ChamberState, ...]:
    a, b = state
    if a < 0 or b < a:
        raise ValueError("state must satisfy 0<=a<=b")
    a_next = (1,) if a == 0 else (a - 1, a + 1)
    b_next = (1,) if b == 0 else (b - 1, b + 1)
    return tuple(sorted({tuple(sorted((x, y))) for x in a_next for y in b_next}))


def transition_repair_bits(previous: ChamberState, current: ChamberState) -> int:
    if current not in chamber_successors(previous):
        raise ValueError("current is not a legal chamber successor")
    zeros = int(previous[0] == 0) + int(previous[1] == 0)
    split = int(previous[0] == previous[1] and current[0] != current[1])
    return zeros + split


def repair_polynomial_coefficients(length: int) -> RepairPolynomial:
    _require_natural("length", length)
    state_polynomials: dict[ChamberState, dict[int, int]] = {(0, 0): {0: 1}}
    for _ in range(length):
        nxt: dict[ChamberState, dict[int, int]] = defaultdict(dict)
        for state, polynomial in state_polynomials.items():
            for successor in chamber_successors(state):
                cost = transition_repair_bits(state, successor)
                target = nxt[successor]
                for repair, count in polynomial.items():
                    target[repair + cost] = target.get(repair + cost, 0) + count
        state_polynomials = dict(nxt)
    total: dict[int, int] = {}
    for polynomial in state_polynomials.values():
        for repair, count in polynomial.items():
            total[repair] = total.get(repair, 0) + count
    degree = max(total, default=0)
    return tuple(total.get(power, 0) for power in range(degree + 1))


def evaluate_repair_polynomial(coefficients: RepairPolynomial, value: int) -> int:
    if not isinstance(coefficients, tuple) or not coefficients:
        raise ValueError("coefficients must be a nonempty tuple")
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    return sum(c * value**r for r, c in enumerate(coefficients))


def repair_polynomial_derivative_at_two(coefficients: RepairPolynomial) -> int:
    return sum(r * c * 2 ** (r - 1) for r, c in enumerate(coefficients) if r)


def coordination_history_image_size(length: int) -> int:
    return sum(repair_polynomial_coefficients(length))


def coordination_history_image_size_closed(length: int) -> int:
    _require_natural("length", length)
    if length % 2 == 0:
        m = length // 2
        catalan = comb(2 * m, m) // (m + 1)
        return (2 * m + 1) * catalan * catalan
    m = (length - 1) // 2
    catalan = comb(2 * (m + 1), m + 1) // (m + 2)
    return ((m + 2) * catalan * catalan) // 2


def minimum_repair_coefficient_closed(length: int) -> int:
    """Coefficient a_(N,2) for N>=1.

    Repair dimension two means the two absolute channels coincide and form one
    common excursion, with no later split/departure event. Hence the number is
    exactly the one-sided absolute-history count with one excursion.
    """
    _require_natural("length", length)
    if length == 0:
        return 1
    return absolute_history_count_with_excursions(length, 1)


def maximum_repair_coefficient_closed(length: int) -> int:
    """Coefficient a_(N,N+1) at the sharp largest fiber for N>=1.

    Internal maximizers use only A=(0,0), B=(1,1), C=(0,2). From B, a complete
    two-step return to B has two choices: B-A-B or B-C-B. For even N=2m, make
    m-1 such choices and finish B->C. For odd N=2m+1>=3, make m-1 choices and
    finish with one of B-A-B, B-C-B, B-C-D where D=(1,3).
    """
    _require_natural("length", length)
    if length == 0:
        return 1
    if length == 1:
        return 1
    if length % 2 == 0:
        m = length // 2
        return 2 ** (m - 1)
    m = (length - 1) // 2
    return 3 * (2 ** (m - 1))


def maximum_fiber_microscopic_mass_fraction(length: int) -> tuple[int, int]:
    """Reduced exact fraction of microscopic windows in maximum-size fibers."""
    _require_natural("length", length)
    if length == 0:
        return 1, 1
    numerator = maximum_repair_coefficient_closed(length) * 2 ** (length + 1)
    denominator = 4 ** length
    while numerator % 2 == 0 and denominator % 2 == 0:
        numerator //= 2
        denominator //= 2
    return numerator, denominator


def microscopic_domain_from_repair_polynomial(length: int) -> int:
    coefficients = repair_polynomial_coefficients(length)
    value = evaluate_repair_polynomial(coefficients, 2)
    if value != 4 ** length:
        raise AssertionError("repair polynomial must reconstruct microscopic domain")
    return value


def collision_coefficients_from_repair_polynomial(
    coefficients: RepairPolynomial,
) -> tuple[int, ...]:
    maximum_repair = max((r for r, c in enumerate(coefficients) if c), default=0)
    maximum_fiber = 2 ** maximum_repair
    return tuple(
        sum(
            count * comb(2**r, order)
            for r, count in enumerate(coefficients)
            if count and 2**r >= order
        )
        for order in range(1, maximum_fiber + 1)
    )


def total_repair_load_from_polynomial(length: int) -> int:
    coefficients = repair_polynomial_coefficients(length)
    load = 2 * repair_polynomial_derivative_at_two(coefficients)
    expected = total_two_sided_repair_bit_load(length)
    if load != expected:
        raise AssertionError("repair-polynomial derivative must match event count")
    return load
