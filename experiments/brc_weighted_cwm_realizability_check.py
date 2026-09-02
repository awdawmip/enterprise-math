"""Exact checker for the positive-path CWM realizability correction.

For count c and positive rational path masses, the realizable CWM triples are:

* (0,0,0);
* c=1 with W=M>0;
* c>=2 with 0<M<W<=cM.

The checker enumerates small rational mass multisets, tests the characterization,
constructs witnesses for every bounded rational triple in the theorem region,
and confirms closure under CWM recoalescence/product composition.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Ratio:
    numerator: int
    denominator: int = 1

    def __post_init__(self) -> None:
        if self.numerator < 0 or self.denominator <= 0:
            raise ValueError("invalid ratio")


def add(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)


def multiply(a: Ratio, b: Ratio) -> Ratio:
    return Ratio(a.numerator * b.numerator, a.denominator * b.denominator)


def equal(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator == b.numerator * a.denominator


def less(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator < b.numerator * a.denominator


def less_equal(a: Ratio, b: Ratio) -> bool:
    return a.numerator * b.denominator <= b.numerator * a.denominator


def max_ratio(values: tuple[Ratio, ...]) -> Ratio:
    result = values[0]
    for value in values[1:]:
        if less(result, value):
            result = value
    return result


def scale(value: Ratio, factor: int) -> Ratio:
    return Ratio(value.numerator * factor, value.denominator)


def divide_by_integer(value: Ratio, divisor: int) -> Ratio:
    if divisor <= 0:
        raise ValueError("positive divisor required")
    return Ratio(value.numerator, value.denominator * divisor)


def subtract_positive(a: Ratio, b: Ratio) -> Ratio:
    numerator = a.numerator * b.denominator - b.numerator * a.denominator
    if numerator <= 0:
        raise ValueError("strictly positive difference required")
    return Ratio(numerator, a.denominator * b.denominator)


ZERO = Ratio(0, 1)


@dataclass(frozen=True)
class CWM:
    count: int
    total: Ratio
    maximum: Ratio


def from_masses(masses: tuple[Ratio, ...]) -> CWM:
    if not masses:
        return CWM(0, ZERO, ZERO)
    if any(mass.numerator <= 0 for mass in masses):
        raise ValueError("supported path masses must be strictly positive")
    total = ZERO
    for mass in masses:
        total = add(total, mass)
    return CWM(len(masses), total, max_ratio(masses))


def in_exact_realizable_locus(value: CWM) -> bool:
    if value.count == 0:
        return value.total.numerator == 0 and value.maximum.numerator == 0
    if value.total.numerator <= 0 or value.maximum.numerator <= 0:
        return False
    if value.count == 1:
        return equal(value.total, value.maximum)
    return (
        less(value.maximum, value.total)
        and less_equal(value.total, scale(value.maximum, value.count))
    )


def construct_masses(value: CWM) -> tuple[Ratio, ...]:
    if not in_exact_realizable_locus(value):
        raise ValueError("triple is outside exact realizability locus")
    if value.count == 0:
        return ()
    if value.count == 1:
        return (value.maximum,)
    remainder = subtract_positive(value.total, value.maximum)
    each = divide_by_integer(remainder, value.count - 1)
    if not less_equal(each, value.maximum):
        raise AssertionError("sufficiency construction exceeded declared maximum")
    result = (value.maximum,) + (each,) * (value.count - 1)
    if from_masses(result) != value:
        reconstructed = from_masses(result)
        if (
            reconstructed.count != value.count
            or not equal(reconstructed.total, value.total)
            or not equal(reconstructed.maximum, value.maximum)
        ):
            raise AssertionError("sufficiency construction failed")
    return result


def cwm_add(a: CWM, b: CWM) -> CWM:
    if a.count == 0:
        return b
    if b.count == 0:
        return a
    return CWM(
        a.count + b.count,
        add(a.total, b.total),
        max_ratio((a.maximum, b.maximum)),
    )


def cwm_multiply(a: CWM, b: CWM) -> CWM:
    if a.count == 0 or b.count == 0:
        return CWM(0, ZERO, ZERO)
    return CWM(
        a.count * b.count,
        multiply(a.total, b.total),
        multiply(a.maximum, b.maximum),
    )


def check_mass_multisets() -> int:
    palette = (Ratio(1, 2), Ratio(1, 1), Ratio(3, 2), Ratio(2, 1))
    checked = 1  # empty family
    if not in_exact_realizable_locus(from_masses(())):
        raise AssertionError("empty family must be realizable")
    for count in range(1, 5):
        for masses in product(palette, repeat=count):
            value = from_masses(tuple(masses))
            if not in_exact_realizable_locus(value):
                raise AssertionError("positive mass family violated exact characterization")
            checked += 1
    return checked


def check_constructive_sufficiency() -> int:
    candidates = 0
    palette = (
        Ratio(1, 2),
        Ratio(1, 1),
        Ratio(3, 2),
        Ratio(2, 1),
        Ratio(5, 2),
        Ratio(3, 1),
        Ratio(4, 1),
        Ratio(5, 1),
        Ratio(6, 1),
    )
    for count in range(1, 5):
        for total, maximum in product(palette, repeat=2):
            value = CWM(count, total, maximum)
            if not in_exact_realizable_locus(value):
                continue
            masses = construct_masses(value)
            reconstructed = from_masses(masses)
            if (
                reconstructed.count != value.count
                or not equal(reconstructed.total, value.total)
                or not equal(reconstructed.maximum, value.maximum)
            ):
                raise AssertionError("constructed positive masses do not realize candidate")
            candidates += 1
    return candidates


def check_strict_envelope_gap() -> None:
    envelope_only = CWM(2, Ratio(1, 1), Ratio(1, 1))
    weak_envelope = (
        envelope_only.count >= 1
        and less_equal(envelope_only.maximum, envelope_only.total)
        and less_equal(
            envelope_only.total,
            scale(envelope_only.maximum, envelope_only.count),
        )
    )
    if not weak_envelope:
        raise AssertionError("counterexample must lie in weak algebraic envelope")
    if in_exact_realizable_locus(envelope_only):
        raise AssertionError("(2,1,1) must not be positive-path realizable")


def check_closure() -> int:
    families = (
        (),
        (Ratio(1, 1),),
        (Ratio(1, 2), Ratio(1, 1)),
        (Ratio(1, 1), Ratio(1, 1)),
        (Ratio(1, 2), Ratio(3, 2), Ratio(2, 1)),
    )
    states = tuple(from_masses(family) for family in families)
    checks = 0
    for left, right in product(states, repeat=2):
        added = cwm_add(left, right)
        multiplied = cwm_multiply(left, right)
        if not in_exact_realizable_locus(added):
            raise AssertionError("realizability locus not closed under recoalescence")
        if not in_exact_realizable_locus(multiplied):
            raise AssertionError("realizability locus not closed under product composition")
        checks += 1
    return checks


def main() -> None:
    multisets = check_mass_multisets()
    candidates = check_constructive_sufficiency()
    check_strict_envelope_gap()
    closure = check_closure()
    print(
        "BRC CWM realizability correction PASS: "
        f"{multisets} positive mass families; {candidates} constructive triples; "
        f"{closure} closure pairs; strict H\\R witness confirmed"
    )


if __name__ == "__main__":
    main()
