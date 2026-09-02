"""Exact checker for one-state multi-loop cyclic Weighted-BRC closure.

The checker validates the CWM loop-power law, separates max-path and total-mass
stability thresholds, checks exact rational geometric closure, and routes the
stable recurrent surplus through the existing BRC LN runtime.

All stability decisions use integer cross multiplication; no float/log/exp is
used for the cyclic classification.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from enterprise_math.brc_logarithm import brc_ln_decimal_readout, ln
from enterprise_math.exact_arithmetic import division


@dataclass(frozen=True)
class Ratio:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.numerator < 0 or self.denominator <= 0:
            raise ValueError("Ratio must be non-negative with positive denominator")


def add(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(
        a.numerator * b.denominator + b.numerator * a.denominator,
        a.denominator * b.denominator,
    )


def multiply(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.numerator, a.denominator * b.denominator)


def equal(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator == b.numerator * a.denominator


def less(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator < b.numerator * a.denominator


def less_equal(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator <= b.numerator * a.denominator


def greater(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator > b.numerator * a.denominator


def max_ratio(values: tuple[Ratio, ...]) -> Ratio:
    if not values:
        raise ValueError("nonempty values required")
    result = values[0]
    for value in values[1:]:
        if greater(value, result):
            result = value
    return result


def power(value: Ratio, exponent: int) -> Ratio:
    result = Ratio(1, 1)
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def sum_ratios(values: tuple[Ratio, ...]) -> Ratio:
    result = Ratio(0, 1)
    for value in values:
        result = add(result, value)
    return result


def divide_positive(a: Ratio, b: Ratio) -> Ratio:
    if a.numerator <= 0 or b.numerator <= 0:
        raise ValueError("positive ratios required")
    return Ratio(a.numerator * b.denominator, a.denominator * b.numerator)


def geometric_closure_factor(s: Ratio) -> Ratio:
    """Return exact 1/(1-s), requiring 0<=s<1."""
    if not less(s, Ratio(1, 1)):
        raise ValueError("geometric closure requires s<1")
    difference_numerator = s.denominator - s.numerator
    if difference_numerator <= 0:
        raise AssertionError("positive one-minus-s numerator required")
    return Ratio(s.denominator, difference_numerator)


def explicit_loop_words(weights: tuple[Ratio, ...], length: int) -> tuple[int, Ratio, Ratio]:
    if not weights:
        raise ValueError("at least one positive loop required")
    if any(weight.numerator <= 0 for weight in weights):
        raise ValueError("loop weights must be positive")
    if length == 0:
        one = Ratio(1, 1)
        return (1, one, one)
    count = 0
    total = Ratio(0, 1)
    maximum = Ratio(0, 1)
    for word in product(weights, repeat=length):
        mass = Ratio(1, 1)
        for weight in word:
            mass = multiply(mass, weight)
        total = add(total, mass)
        if count == 0 or greater(mass, maximum):
            maximum = mass
        count += 1
    return count, total, maximum


def check_n_turn_power_law() -> int:
    palettes = (
        (Ratio(1, 4),),
        (Ratio(1, 4), Ratio(1, 8)),
        (Ratio(1, 5), Ratio(1, 5)),
        (Ratio(1, 2), Ratio(1, 3), Ratio(1, 6)),
    )
    checks = 0
    for weights in palettes:
        k = len(weights)
        s = sum_ratios(weights)
        q = max_ratio(weights)
        for length in range(0, 6):
            count, total, maximum = explicit_loop_words(weights, length)
            if count != k**length:
                raise AssertionError("loop-word count power law failed")
            if not equal(total, power(s, length)):
                raise AssertionError("loop total-mass power law failed")
            if not equal(maximum, power(q, length)):
                raise AssertionError("loop max-mass power law failed")
            checks += 1
    return checks


def phase(weights: tuple[Ratio, ...]) -> str:
    s = sum_ratios(weights)
    q = max_ratio(weights)
    one = Ratio(1, 1)
    if less(s, one):
        if not less(q, one):
            raise AssertionError("S<1 must imply Q<1")
        return "SUMMABLE"
    if less_equal(q, one):
        return "MULTIPLICITY_DIVERGENT"
    return "AMPLIFYING_DIVERGENT"


def check_phase_classification() -> None:
    if phase((Ratio(1, 4), Ratio(1, 8))) != "SUMMABLE":
        raise AssertionError("3/8 total loop mass should be summable")
    if phase((Ratio(3, 5), Ratio(3, 5))) != "MULTIPLICITY_DIVERGENT":
        raise AssertionError("two 3/5 loops must be multiplicity-driven divergent")
    if phase((Ratio(1, 2), Ratio(1, 2))) != "MULTIPLICITY_DIVERGENT":
        raise AssertionError("S=1 is critical divergent")
    if phase((Ratio(6, 5),)) != "AMPLIFYING_DIVERGENT":
        raise AssertionError("single 6/5 loop must amplify")

    # Minimal witness: each individual loop contracts, but total loop family expands.
    weights = (Ratio(3, 5), Ratio(3, 5))
    q = max_ratio(weights)
    s = sum_ratios(weights)
    if not less(q, Ratio(1)) or not greater(s, Ratio(1)):
        raise AssertionError("multiplicity divergence witness malformed")
    # At every fixed length n, max mass decays while summed mass grows.
    for length in range(1, 6):
        if not less(power(q, length), Ratio(1)):
            raise AssertionError("dominant loop word should contract")
        if not greater(power(s, length), Ratio(1)):
            raise AssertionError("summed loop-word mass should grow")


def check_equal_loop_threshold() -> int:
    candidate_q = (
        Ratio(1, 10),
        Ratio(1, 5),
        Ratio(1, 4),
        Ratio(1, 3),
        Ratio(1, 2),
        Ratio(3, 5),
    )
    checks = 0
    for k in range(1, 6):
        for q in candidate_q:
            s = Ratio(k * q.numerator, q.denominator)
            stable_by_sum = less(s, Ratio(1))
            stable_by_cross_product = k * q.numerator < q.denominator
            if stable_by_sum != stable_by_cross_product:
                raise AssertionError("equal-loop kq<1 criterion failed")
            checks += 1
    return checks


def check_exact_closure_and_tail() -> None:
    loops = (Ratio(1, 4), Ratio(1, 8))
    s = sum_ratios(loops)
    if not equal(s, Ratio(3, 8)):
        raise AssertionError("loop aggregate S should be 3/8")
    closure = geometric_closure_factor(s)
    if not equal(closure, Ratio(8, 5)):
        raise AssertionError("1/(1-3/8) must be 8/5")

    # Tail path masses 1/2 and 1/4: W0=3/4, M0=1/2, E0=3/2.
    w0 = Ratio(3, 4)
    m0 = Ratio(1, 2)
    e0 = divide_positive(w0, m0)
    if not equal(e0, Ratio(3, 2)):
        raise AssertionError("tail effective multiplicity should be 3/2")

    w_total = multiply(w0, closure)
    m_total = m0
    e_total = divide_positive(w_total, m_total)
    if not equal(w_total, Ratio(6, 5)):
        raise AssertionError("closed tail total mass should be 6/5")
    if not equal(e_total, multiply(e0, closure)):
        raise AssertionError("E_total=E0/(1-S) failed")
    if not equal(e_total, Ratio(12, 5)):
        raise AssertionError("closed effective multiplicity should be 12/5")

    # The stable recurrent closure surplus Gamma=ln(8/5) is materialized by the
    # already-merged BRC LN interval runtime, not by floating logarithms here.
    gamma_expr = ln(division(closure.numerator, closure.denominator))
    gamma_text = brc_ln_decimal_readout(gamma_expr, 6).text
    if gamma_text != "0.470003":
        raise AssertionError(f"unexpected BRC LN closure surplus: {gamma_text}")


def check_equal_loop_log_surplus_materialization() -> None:
    # Two equal loops have S/Q=2 exactly, so their one-step multiplicity surplus is ln 2.
    weights = (Ratio(1, 5), Ratio(1, 5))
    s = sum_ratios(weights)
    q = max_ratio(weights)
    effective = divide_positive(s, q)
    if not equal(effective, Ratio(2, 1)):
        raise AssertionError("equal two-loop effective multiplicity must be 2")
    text = brc_ln_decimal_readout(
        ln(division(effective.numerator, effective.denominator)),
        6,
    ).text
    if text != "0.693147":
        raise AssertionError("two-loop multiplicity surplus must materialize as ln 2")


def main() -> None:
    power_checks = check_n_turn_power_law()
    check_phase_classification()
    equal_threshold_checks = check_equal_loop_threshold()
    check_exact_closure_and_tail()
    check_equal_loop_log_surplus_materialization()
    print(
        "BRC cyclic log-multiplicity closure PASS: "
        f"{power_checks} loop-power checks; {equal_threshold_checks} equal-loop thresholds; "
        "multiplicity divergence and exact BRC-LN closure surplus confirmed"
    )


if __name__ == "__main__":
    main()
