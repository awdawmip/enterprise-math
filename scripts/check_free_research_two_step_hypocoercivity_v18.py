#!/usr/bin/env python3
"""Exact finite checks for the V18 two-step hypocoercive block."""

from __future__ import annotations

from fractions import Fraction


State = tuple[Fraction, Fraction]


def transition(gamma: Fraction, s: Fraction, state: State) -> State:
    root, standard = state
    return (
        (1 - 2 * s) ** 2 * root,
        4 * gamma * s * (1 - s) * root + s * standard,
    )


def terminal_energy(gamma: Fraction, state: State) -> Fraction:
    root, standard = state
    return root + standard / gamma


def mellin_entries(beta: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    a = (
        1 / (1 - beta)
        - 4 / (2 - beta)
        + 4 / (3 - beta)
    )
    b = 1 / (2 - beta)
    d = 4 * (1 / (2 - beta) - 1 / (3 - beta))
    return a, b, d


def check_one_step_balance() -> None:
    for gamma in (
        Fraction(1, 9),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(1),
    ):
        for numerator in range(11):
            s = Fraction(numerator, 10)
            for root in (Fraction(0), Fraction(1), Fraction(7, 3)):
                for standard in (Fraction(0), Fraction(2), Fraction(5, 4)):
                    state = (root, standard)
                    output = transition(gamma, s, state)
                    assert terminal_energy(gamma, output) == (
                        root + s * standard / gamma
                    )
                    assert (
                        terminal_energy(gamma, state)
                        - terminal_energy(gamma, output)
                        == (1 - s) * standard / gamma
                    )


def check_two_step_identity() -> None:
    for gamma in (
        Fraction(1, 9),
        Fraction(1, 4),
        Fraction(1),
    ):
        for first_numerator in range(11):
            for second_numerator in range(11):
                s1 = Fraction(first_numerator, 10)
                s2 = Fraction(second_numerator, 10)
                for root in (Fraction(0), Fraction(1), Fraction(7, 3)):
                    for standard in (Fraction(0), Fraction(2), Fraction(5, 4)):
                        state = (root, standard)
                        output = transition(
                            gamma,
                            s2,
                            transition(gamma, s1, state),
                        )
                        expected = (
                            (1 - 4 * (1 - s2) * s1 * (1 - s1)) * root
                            + s1 * s2 * standard / gamma
                        )
                        assert terminal_energy(gamma, output) == expected
                        defect = (
                            4 * (1 - s2) * s1 * (1 - s1) * root
                            + (1 - s1 * s2) * standard / gamma
                        )
                        assert (
                            terminal_energy(gamma, state)
                            - terminal_energy(gamma, output)
                            == defect
                        )
                        assert defect >= 0


def check_ideal_average() -> None:
    # E[1 - 4(1-s2)s1(1-s1)] for independent uniform s1,s2.
    root_coefficient = 1 - 4 * Fraction(1, 2) * Fraction(1, 6)
    standard_coefficient = Fraction(1, 2) ** 2
    assert root_coefficient == Fraction(2, 3)
    assert standard_coefficient == Fraction(1, 4)


def check_beta_one_sixth() -> None:
    beta = Fraction(1, 6)
    a, b, d = mellin_entries(beta)
    assert a == Fraction(402, 935)
    assert b == Fraction(6, 11)
    assert d == Fraction(144, 187)

    root_coefficient = a**2 + d * (a + b)
    standard_coefficient = b**2
    assert root_coefficient == Fraction(48132, 51425)
    assert 1 - root_coefficient == Fraction(3293, 51425)
    assert standard_coefficient == Fraction(36, 121)
    assert standard_coefficient < root_coefficient < 1


def check_two_step_critical_polynomial() -> None:
    # The polynomial is zero exactly at the two-step critical exponent.
    # Rational sign checks place the first root between 19/100 and 1/5.
    def polynomial(beta: Fraction) -> Fraction:
        return (
            beta**5
            - 9 * beta**4
            + 30 * beta**3
            - 44 * beta**2
            + 28 * beta
            - 4
        )

    assert polynomial(Fraction(19, 100)) < 0
    assert polynomial(Fraction(1, 5)) > 0


def main() -> None:
    check_one_step_balance()
    check_two_step_identity()
    check_ideal_average()
    check_beta_one_sixth()
    check_two_step_critical_polynomial()
    print("V18 two-step hypocoercivity: exact checks passed")


if __name__ == "__main__":
    main()
