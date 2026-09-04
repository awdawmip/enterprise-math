#!/usr/bin/env python3
"""Exact finite checks for the V18 odd-simplex and commutator-jet frontier.

All theorem-level checks use ``fractions.Fraction``.  The action weights are
arbitrary positive rationals because the checked identities are structural and
do not depend on evaluating logarithms.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Callable, Dict


Scalar = Fraction
Field = Dict[int, Scalar]


def q(n: int, a: int) -> int:
    return n // a


def add(x: Field, y: Field) -> Field:
    return {n: x.get(n, Fraction(0)) + y.get(n, Fraction(0)) for n in set(x) | set(y)}


def sub(x: Field, y: Field) -> Field:
    return {n: x.get(n, Fraction(0)) - y.get(n, Fraction(0)) for n in set(x) | set(y)}


def scale(c: Scalar, x: Field) -> Field:
    return {n: c * value for n, value in x.items()}


def compose(left: Callable[[Field], Field], right: Callable[[Field], Field]) -> Callable[[Field], Field]:
    return lambda f: left(right(f))


def fixture() -> tuple[int, list[int], Dict[int, Scalar], Field]:
    n_top = 42
    actions = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 31, 37, 41]
    weights = {a: Fraction((3 * a + 5) % 11 + 1, (2 * a + 7) % 13 + 2) for a in actions}
    field = {n: Fraction(((17 * n * n + 5 * n + 11) % 53) - 26, 19) for n in range(n_top + 1)}
    return n_top, actions, weights, field


def cumulative_mass(n: int, actions: list[int], weights: Dict[int, Scalar]) -> Scalar:
    return sum((weights[a] for a in actions if a <= n), Fraction(0))


def adaptive_p(
    n: int,
    f: Field,
    actions: list[int],
    weights: Dict[int, Scalar],
) -> Scalar:
    mass = cumulative_mass(n, actions, weights)
    if mass == 0:
        return Fraction(0)
    return sum((weights[a] * f[q(n, a)] for a in actions if a <= n), Fraction(0)) / mass


def check_odd_simplex_graph_norm(
    n_top: int,
    actions: list[int],
    weights: Dict[int, Scalar],
    f: Field,
) -> None:
    def p_field(h: Field) -> Field:
        return {
            n: adaptive_p(n, h, actions, weights)
            for n in range(n_top + 1)
        }

    pf = p_field(f)
    p2f = p_field(pf)
    square = {n: f[n] ** 2 for n in range(n_top + 1)}
    psquare = p_field(square)
    p2square = p_field(psquare)
    residual = {n: f[n] + pf[n] for n in range(n_top + 1)}
    fe = {n: f[n] * residual[n] for n in range(n_top + 1)}
    pfe = p_field(fe)
    pe = p_field(residual)

    for n in range(2, n_top + 1):
        if cumulative_mass(n, actions, weights) == 0:
            continue

        e1 = f[n] ** 2 + 2 * f[n] * pf[n] + psquare[n]
        transported = adaptive_p(
            n,
            {
                m: (
                    f[m] ** 2
                    + 2 * f[m] * pf[m]
                    + psquare[m]
                )
                for m in range(n_top + 1)
            },
            actions,
            weights,
        )
        direct = f[n] ** 2 + 2 * f[n] * p2f[n] + p2square[n]
        odd = e1 + transported + direct

        assert e1 == psquare[n] - square[n] + 2 * fe[n]
        assert direct == 3 * square[n] + p2square[n] - 2 * fe[n] + 2 * f[n] * pe[n]
        assert odd == 2 * (square[n] + p2square[n] + pfe[n] + f[n] * pe[n])
        assert 4 * square[n] <= 3 * odd


def fixed_top_operators(
    n_top: int,
    actions: list[int],
    weights: Dict[int, Scalar],
):
    total = cumulative_mass(n_top, actions, weights)
    assert total > 0

    def s_op(f: Field) -> Field:
        return {
            n: cumulative_mass(n, actions, weights) * f[n] / total
            for n in range(n_top + 1)
        }

    def j_op(f: Field) -> Field:
        return {
            n: sum(
                (weights[a] * f[q(n, a)] for a in actions if a <= n),
                Fraction(0),
            )
            / total
            for n in range(n_top + 1)
        }

    return total, s_op, j_op


def commutator(left, right, f: Field) -> Field:
    return sub(left(right(f)), right(left(f)))


def iterated_ad(s_op, j_op, k: int, f: Field) -> Field:
    if k == 0:
        return j_op(f)

    def previous(h: Field) -> Field:
        return iterated_ad(s_op, j_op, k - 1, h)

    return commutator(s_op, previous, f)


def power(op, k: int, f: Field) -> Field:
    out = f
    for _ in range(k):
        out = op(out)
    return out


def check_commutator_jet(
    n_top: int,
    actions: list[int],
    weights: Dict[int, Scalar],
    f: Field,
) -> None:
    total, s_op, j_op = fixed_top_operators(n_top, actions, weights)
    first = commutator(s_op, j_op, f)

    for n in range(n_top + 1):
        mass_n = cumulative_mass(n, actions, weights)
        expected = sum(
            (
                weights[a]
                * (mass_n - cumulative_mass(q(n, a), actions, weights))
                * f[q(n, a)]
                for a in actions
                if a <= n
            ),
            Fraction(0),
        ) / total**2
        assert first[n] == expected

    for k in range(5):
        ad = iterated_ad(s_op, j_op, k, f)
        for n in range(n_top + 1):
            mass_n = cumulative_mass(n, actions, weights)
            expected = sum(
                (
                    weights[a]
                    * (mass_n - cumulative_mass(q(n, a), actions, weights)) ** k
                    * f[q(n, a)]
                    for a in actions
                    if a <= n
                ),
                Fraction(0),
            ) / total ** (k + 1)
            assert ad[n] == expected

    j2 = power(j_op, 2, f)
    defect = first[n_top] - j2[n_top]
    parity_fold = (
        sum(
            (
                weights[a] * weights[b] * f[q(n_top, a)]
                for a in actions
                for b in actions
                if a * b > n_top
            ),
            Fraction(0),
        )
        - sum(
            (
                weights[a] * weights[b] * f[q(n_top, a * b)]
                for a in actions
                for b in actions
                if a * b <= n_top
            ),
            Fraction(0),
        )
    ) / total**2
    assert defect == parity_fold

    h_field = add(s_op(f), j_op(f))
    jh = j_op(h_field)
    scalar_resolvent_rhs = h_field[n_top] - jh[n_top] - defect
    assert f[n_top] == scalar_resolvent_rhs


def mellin_entries(beta: Scalar) -> tuple[Scalar, Scalar, Scalar]:
    a = Fraction(1, 1) / (1 - beta) - 4 / (2 - beta) + 4 / (3 - beta)
    b = Fraction(1, 1) / (2 - beta)
    c = Fraction(4, 9) * (Fraction(1, 1) / (2 - beta) - Fraction(1, 1) / (3 - beta))
    return a, b, c


def delayed_multiplier(beta: Scalar, depth: int) -> Scalar:
    a, b, c = mellin_entries(beta)
    geometric = sum((a ** (depth - 1 - j) * b**j for j in range(depth)), Fraction(0))
    return a**depth + 9 * c * geometric


def check_delayed_design_points() -> None:
    assert delayed_multiplier(Fraction(1, 4), 1) == Fraction(4, 3)
    assert delayed_multiplier(Fraction(1, 4), 3) == Fraction(10429760, 12326391)
    assert delayed_multiplier(Fraction(1, 4), 3) < 1

    assert delayed_multiplier(Fraction(1, 3), 1) == Fraction(3, 2)
    assert delayed_multiplier(Fraction(1, 3), 4) == Fraction(567, 625)
    assert delayed_multiplier(Fraction(1, 3), 4) < 1

    a, b, c = mellin_entries(Fraction(1, 3))
    assert a == b == Fraction(3, 5)
    assert 9 * c == Fraction(9, 10)


def main() -> None:
    n_top, actions, weights, field = fixture()
    check_odd_simplex_graph_norm(n_top, actions, weights, field)
    check_commutator_jet(n_top, actions, weights, field)
    check_delayed_design_points()
    print("V18 odd-simplex graph norm and Volterra commutator jet: exact checks passed")


if __name__ == "__main__":
    main()
