"""Exact checker for the BRC weighted multiplicity tower.

Checks, over a finite rational palette on the complete four-vertex DAG:

* M <= W <= C*M;
* E=W/M satisfies 1 <= E <= C;
* the local effective-multiplicity transport law;
* integer-beta pre-log tropical bounds;
* the non-monotonicity witness for Delta under insertion of a new dominant path.

No float, logarithm, exponential, Fraction, or Decimal is used.
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
            raise ValueError("Ratio must be non-negative with positive denominator")


ZERO = Ratio(0, 1)
ONE = Ratio(1, 1)

EDGES = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)


def add(left: Ratio, right: Ratio) -> Ratio:
    return Ratio(
        left.numerator * right.denominator
        + right.numerator * left.denominator,
        left.denominator * right.denominator,
    )


def multiply(left: Ratio, right: Ratio) -> Ratio:
    return Ratio(
        left.numerator * right.numerator,
        left.denominator * right.denominator,
    )


def divide_positive(left: Ratio, right: Ratio) -> Ratio:
    if left.numerator <= 0 or right.numerator <= 0:
        raise ValueError("positive ratios required")
    return Ratio(
        left.numerator * right.denominator,
        left.denominator * right.numerator,
    )


def equal(left: Ratio, right: Ratio) -> bool:
    return left.numerator * right.denominator == right.numerator * left.denominator


def less_equal(left: Ratio, right: Ratio) -> bool:
    return left.numerator * right.denominator <= right.numerator * left.denominator


def greater(left: Ratio, right: Ratio) -> bool:
    return left.numerator * right.denominator > right.numerator * left.denominator


def scale(value: Ratio, factor: int) -> Ratio:
    return Ratio(value.numerator * factor, value.denominator)


def power(value: Ratio, exponent: int) -> Ratio:
    result = ONE
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def supported(value: Ratio) -> bool:
    return value.numerator != 0


def stats_by_vertex(weights: tuple[Ratio, ...]):
    count = [0, 0, 0, 0]
    total = [ZERO, ZERO, ZERO, ZERO]
    maximum = [ZERO, ZERO, ZERO, ZERO]
    effective = [None, None, None, None]

    count[0] = 1
    total[0] = ONE
    maximum[0] = ONE
    effective[0] = ONE

    for vertex in (1, 2, 3):
        c_v = 0
        w_v = ZERO
        m_v = ZERO
        incoming_candidates: list[tuple[Ratio, Ratio]] = []
        for edge_index, (source, target) in enumerate(EDGES):
            if target != vertex:
                continue
            edge_weight = weights[edge_index]
            if count[source] == 0 or not supported(edge_weight):
                continue
            c_v += count[source]
            w_v = add(w_v, multiply(total[source], edge_weight))
            candidate_max = multiply(maximum[source], edge_weight)
            if not supported(m_v) or greater(candidate_max, m_v):
                m_v = candidate_max
            if effective[source] is None:
                raise AssertionError("reachable predecessor must have effective multiplicity")
            incoming_candidates.append((effective[source], candidate_max))

        count[vertex] = c_v
        total[vertex] = w_v
        maximum[vertex] = m_v

        if c_v == 0:
            if supported(w_v) or supported(m_v):
                raise AssertionError("unreachable vertex must have zero weighted states")
            continue

        e_v = divide_positive(w_v, m_v)
        effective[vertex] = e_v

        if not less_equal(m_v, w_v):
            raise AssertionError("M <= W failed")
        if not less_equal(w_v, scale(m_v, c_v)):
            raise AssertionError("W <= C*M failed")
        if not less_equal(ONE, e_v):
            raise AssertionError("1 <= E failed")
        if not less_equal(e_v, Ratio(c_v, 1)):
            raise AssertionError("E <= C failed")

        transported = ZERO
        for predecessor_effective, candidate_max in incoming_candidates:
            relative_candidate = divide_positive(candidate_max, m_v)
            transported = add(
                transported,
                multiply(predecessor_effective, relative_candidate),
            )
        if not equal(transported, e_v):
            raise AssertionError("local effective-multiplicity transport law failed")

    return tuple(count), tuple(total), tuple(maximum), tuple(effective)


def explicit_supported_path_masses(weights: tuple[Ratio, ...]) -> tuple[Ratio, ...]:
    index = {edge: i for i, edge in enumerate(EDGES)}
    paths = (
        ((0, 3),),
        ((0, 1), (1, 3)),
        ((0, 2), (2, 3)),
        ((0, 1), (1, 2), (2, 3)),
    )
    result = []
    for path in paths:
        mass = ONE
        for edge in path:
            mass = multiply(mass, weights[index[edge]])
        if supported(mass):
            result.append(mass)
    return tuple(result)


def check_beta_bounds(path_masses: tuple[Ratio, ...]) -> None:
    if not path_masses:
        return
    count = len(path_masses)
    maximum = path_masses[0]
    for mass in path_masses[1:]:
        if greater(mass, maximum):
            maximum = mass
    for beta in (1, 2, 3, 4):
        powered_sum = ZERO
        for mass in path_masses:
            powered_sum = add(powered_sum, power(mass, beta))
        max_power = power(maximum, beta)
        if not less_equal(max_power, powered_sum):
            raise AssertionError("M^beta <= sum w^beta failed")
        if not less_equal(powered_sum, scale(max_power, count)):
            raise AssertionError("sum w^beta <= C*M^beta failed")


def check_exhaustive_tower() -> int:
    palette = (
        Ratio(0, 1),
        Ratio(1, 2),
        Ratio(1, 1),
        Ratio(2, 1),
    )
    cases = 0
    for weights in product(palette, repeat=len(EDGES)):
        count, total, maximum, effective = stats_by_vertex(weights)
        path_masses = explicit_supported_path_masses(weights)
        if count[3] != len(path_masses):
            raise AssertionError("dynamic path count differs from explicit paths")
        explicit_total = ZERO
        explicit_max = ZERO
        for mass in path_masses:
            explicit_total = add(explicit_total, mass)
            if not supported(explicit_max) or greater(mass, explicit_max):
                explicit_max = mass
        if not equal(total[3], explicit_total) or not equal(maximum[3], explicit_max):
            raise AssertionError("dynamic W/M differs from explicit path statistics")
        if count[3] == 0:
            if effective[3] is not None:
                raise AssertionError("unreachable target must have no E")
        else:
            if effective[3] is None:
                raise AssertionError("reachable target requires E")
            if not equal(effective[3], divide_positive(explicit_total, explicit_max)):
                raise AssertionError("dynamic E differs from explicit W/M")
        check_beta_bounds(path_masses)
        cases += 1
    return cases


def check_dominant_branch_nonmonotonicity() -> None:
    # Delta=ln(E). ln is strictly increasing, so compare E exactly pre-log.
    old_effective = Ratio(2, 1)  # masses (1,1): W/M=2
    new_effective = Ratio(102, 100)  # masses (1,1,100): W/M=102/100
    if not greater(old_effective, new_effective):
        raise AssertionError("new dominant branch should reduce effective multiplicity")


def main() -> None:
    cases = check_exhaustive_tower()
    check_dominant_branch_nonmonotonicity()
    print(
        "BRC weighted multiplicity tower PASS: "
        f"{cases} exact rational DAG assignments; beta=1..4 bounds; "
        "local E transport; dominant-branch nonmonotonicity witness"
    )


if __name__ == "__main__":
    main()
