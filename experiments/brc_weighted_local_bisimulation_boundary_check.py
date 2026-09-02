"""Exact counterexample: local weighted bisimulation is not necessary for CWM future equivalence.

The example relocates a factor 2 from a downstream transfer into an incoming
edge. Complete path masses and therefore future CWM semantics stay unchanged,
while one-step transition aggregates by future class change.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Ratio:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.numerator < 0 or self.denominator <= 0:
            raise ValueError("invalid ratio")


def add_ratio(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)


def mul_ratio(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.numerator, a.denominator * b.denominator)


def equal_ratio(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator == b.numerator * a.denominator


def max_ratio(a: Ratio, b: Ratio) -> Ratio:
    if a.numerator * b.denominator >= b.numerator * a.denominator:
        return a
    return b


ZERO_R = Ratio(0, 1)
ONE_R = Ratio(1, 1)


@dataclass(frozen=True)
class CWM:
    count: int
    total: Ratio
    maximum: Ratio


ZERO = CWM(0, ZERO_R, ZERO_R)
ONE = CWM(1, ONE_R, ONE_R)


def plus(a: CWM, b: CWM) -> CWM:
    return CWM(a.count + b.count, add_ratio(a.total, b.total), max_ratio(a.maximum, b.maximum))


def times(a: CWM, b: CWM) -> CWM:
    return CWM(a.count * b.count, mul_ratio(a.total, b.total), mul_ratio(a.maximum, b.maximum))


def equal(a: CWM, b: CWM) -> bool:
    return a.count == b.count and equal_ratio(a.total, b.total) and equal_ratio(a.maximum, b.maximum)


def edge(weight: int) -> CWM:
    if weight == 0:
        return ZERO
    ratio = Ratio(weight, 1)
    return CWM(1, ratio, ratio)


def main() -> None:
    # Future transfer values to one sink t.
    future_a1 = ONE
    future_a2 = ONE
    future_b = edge(2)  # B -> t has downstream factor 2.

    if not equal(future_a1, future_a2):
        raise AssertionError("A1 and A2 must define one future class")
    if equal(future_a1, future_b):
        raise AssertionError("B must be a distinct future class")

    # x -> A1 weight 1; x -> B weight 1.
    future_x = plus(times(edge(1), future_a1), times(edge(1), future_b))

    # y -> A1 weight 1; y -> A2 weight 2.
    future_y = plus(times(edge(1), future_a1), times(edge(2), future_a2))

    expected = CWM(2, Ratio(3, 1), Ratio(2, 1))
    if not equal(future_x, expected) or not equal(future_y, expected):
        raise AssertionError("factor relocation must preserve complete CWM future semantics")

    # One-step aggregate lifted edge carriers into future classes A={A1,A2}, B={B}.
    x_to_a = edge(1)
    x_to_b = edge(1)
    y_to_a = plus(edge(1), edge(2))
    y_to_b = ZERO

    if equal(x_to_a, y_to_a) or equal(x_to_b, y_to_b):
        raise AssertionError("local block transition summaries must differ")

    # Exact factor-relocation identity 1*2 == 2*1.
    if not equal_ratio(mul_ratio(Ratio(1), Ratio(2)), mul_ratio(Ratio(2), Ratio(1))):
        raise AssertionError("factor relocation identity failed")

    print(
        "BRC weighted local-bisimulation boundary PASS: "
        "future_x=future_y=(2,3,2) while local future-class transitions differ"
    )


if __name__ == "__main__":
    main()
