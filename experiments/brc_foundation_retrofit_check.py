"""Exact regression checks for the 2026-09-02 Weighted/Log BRC Foundation retrofit.

This experiment deliberately revisits three earlier research routes:

1. the unsieved support/thickness decomposition of arithmetic BRC;
2. the width-one neighboring-arm selector-flip reduction;
3. the oriented positive-axis holonomy cocycle.

The goal is not to manufacture a positive result.  It checks exactly which old
variables compress under the new Foundation layer and where the new positive
weighted carrier provably does *not* replace a signed path observable.

No floating logarithm is required.  Whenever a logarithmic identity is stated,
the checker verifies its positive-rational precursor exactly.
"""

from __future__ import annotations

from fractions import Fraction


LIMIT_N = 10_000
LIMIT_CENTER = 20_000


def factor_exponents(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    x = n
    exponents: list[int] = []
    p = 2
    while p * p <= x:
        exponent = 0
        while x % p == 0:
            exponent += 1
            x //= p
        if exponent:
            exponents.append(exponent)
        p = 3 if p == 2 else p + 2
    if x > 1:
        exponents.append(1)
    return tuple(exponents)


def omega(n: int) -> int:
    return len(factor_exponents(n))


def tau(n: int) -> int:
    result = 1
    for exponent in factor_exponents(n):
        result *= exponent + 1
    return result


def h1(n: int) -> Fraction:
    """H_1(n)=sum_{p^e || n} e/(e+1), exact."""
    return sum(
        (Fraction(exponent, exponent + 1) for exponent in factor_exponents(n)),
        Fraction(0, 1),
    )


def delta1(n: int) -> Fraction:
    return h1(n) - Fraction(omega(n), 2)


def thickness_ratio(n: int) -> Fraction:
    """Exact precursor of exp(Theta)=tau(n)/2^omega(n)."""
    return Fraction(tau(n), 2 ** omega(n))


def product_thickness_ratio(n: int) -> Fraction:
    result = Fraction(1, 1)
    for exponent in factor_exponents(n):
        result *= Fraction(exponent + 1, 2)
    return result


def old_brc_factorization(n: int) -> Fraction:
    """Old support/thickness form, with exp(Theta) kept as an exact ratio."""
    rank = omega(n)
    return (
        Fraction(1, 1)
        + Fraction(2**rank, 1)
        * thickness_ratio(n)
        * (Fraction(rank, 2) - 1 + delta1(n))
    )


def compressed_brc_factorization(n: int) -> Fraction:
    """Foundation-retrofitted exact form 1+tau(n)*(H_1(n)-1)."""
    return Fraction(1, 1) + tau(n) * (h1(n) - 1)


def check_two_scale_retyping() -> dict[str, int]:
    squarefree = 0
    non_squarefree = 0
    for n in range(2, LIMIT_N + 1):
        exponents = factor_exponents(n)
        ratio = thickness_ratio(n)
        assert ratio == product_thickness_ratio(n)

        # Theta = ln(tau/2^omega) is exactly the logarithmic difference between
        # full divisor multiplicity and the Boolean two-choice-per-prime skeleton.
        assert Fraction(tau(n), 1) == Fraction(2 ** omega(n), 1) * ratio

        is_squarefree = all(exponent == 1 for exponent in exponents)
        assert (ratio == 1) == is_squarefree
        if is_squarefree:
            squarefree += 1
        else:
            non_squarefree += 1

        # Old (omega,Theta,Delta_1) factorization collapses algebraically to
        # the two exact arithmetic coordinates (tau,H_1).
        assert old_brc_factorization(n) == compressed_brc_factorization(n)

    return {
        "checked_n": LIMIT_N - 1,
        "squarefree": squarefree,
        "non_squarefree": non_squarefree,
    }


def check_width_one_reduction() -> dict[str, object]:
    d_positive = 0
    multiplicity_reversals = 0
    multiplicity_ties = 0
    first_reversal: tuple[int, int, int, int, int] | None = None
    first_tie: tuple[int, int, int, int, Fraction] | None = None

    for center in range(3, LIMIT_CENTER + 1):
        left = center - 1
        right = center + 1
        rank_left = omega(left)
        rank_right = omega(right)
        d = rank_left - rank_right

        # Exact rational precursor of rho_d=2^d exp(D_Theta).
        if d >= 0:
            two_to_d = Fraction(2**d, 1)
        else:
            two_to_d = Fraction(1, 2 ** (-d))
        old_rho = (
            two_to_d
            * thickness_ratio(left)
            / thickness_ratio(right)
        )
        new_rho = Fraction(tau(left), tau(right))
        assert old_rho == new_rho

        if d <= 0:
            continue
        d_positive += 1

        # The old first flip test rho_d < 1 is exactly total multiplicity
        # reversal tau(left) < tau(right).
        assert (old_rho < 1) == (tau(left) < tau(right))
        assert (old_rho == 1) == (tau(left) == tau(right))

        if tau(left) < tau(right):
            multiplicity_reversals += 1
            if first_reversal is None:
                first_reversal = (
                    center,
                    left,
                    right,
                    tau(left),
                    tau(right),
                )

        if tau(left) == tau(right):
            multiplicity_ties += 1
            old_boundary = Fraction(d, 2) + delta1(left) - delta1(right)
            new_boundary = h1(left) - h1(right)
            assert old_boundary == new_boundary
            assert (old_boundary < 0) == (h1(left) < h1(right))
            if first_tie is None:
                first_tie = (
                    center,
                    left,
                    right,
                    tau(left),
                    new_boundary,
                )

    assert first_reversal is not None
    assert first_tie is not None
    return {
        "checked_centers": LIMIT_CENTER - 2,
        "d_positive": d_positive,
        "multiplicity_reversals": multiplicity_reversals,
        "multiplicity_ties": multiplicity_ties,
        "first_reversal": first_reversal,
        "first_tie": first_tie,
    }


Vector3 = tuple[int, int, int]


def incidence(x: Vector3, y: Vector3) -> int:
    a, b, c = x
    d, e, f = y
    return a * e + b * f + c * d - a * f - b * d - c * e


def omega2(path: tuple[Vector3, ...]) -> int:
    return sum(
        incidence(path[i], path[j])
        for i in range(len(path))
        for j in range(i + 1, len(path))
    )


def positive_power(base: int, exponent: int) -> Fraction:
    if exponent >= 0:
        return Fraction(base**exponent, 1)
    return Fraction(1, base ** (-exponent))


def cwm_recoalesce(weights: tuple[Fraction, ...]) -> tuple[int, Fraction, Fraction]:
    if not weights or any(weight <= 0 for weight in weights):
        raise ValueError("positive branch weights required")
    return len(weights), sum(weights, Fraction(0, 1)), max(weights)


def check_oriented_holonomy_boundary() -> dict[str, object]:
    e1 = (1, 0, 0)
    e2 = (0, 1, 0)
    e3 = (0, 0, 1)
    forward = (e1, e2, e3)
    reverse = (e3, e2, e1)

    forward_area = omega2(forward)
    reverse_area = omega2(reverse)
    assert forward_area == 1
    assert reverse_area == -1

    # Encode the signed path observable into positive weights only for the
    # purpose of testing what positive Weighted-BRC recoalescence can retain.
    lam = 2
    forward_weight = positive_power(lam, forward_area)
    reverse_weight = positive_power(lam, reverse_area)
    assert forward_weight == 2
    assert reverse_weight == Fraction(1, 2)

    aggregate = cwm_recoalesce((forward_weight, reverse_weight))
    reversed_aggregate = cwm_recoalesce((reverse_weight, forward_weight))
    assert aggregate == reversed_aggregate
    count, total, dominant = aggregate
    effective_multiplicity = total / dominant
    assert (count, total, dominant) == (2, Fraction(5, 2), Fraction(2, 1))
    assert effective_multiplicity == Fraction(5, 4)

    # Projective/gauge scaling changes W and M by a common factor but leaves E.
    gauge = Fraction(3, 1)
    gauged = (count, gauge * total, gauge * dominant)
    assert gauged[1] / gauged[2] == effective_multiplicity

    # The two underlying paths have opposite oriented holonomy, but the positive
    # recoalesced CWM state is unchanged when orientation is globally reversed.
    # Therefore signed orientation is not recoverable from positive CWM alone.
    assert forward_area != reverse_area
    assert aggregate == reversed_aggregate

    return {
        "forward_omega2": forward_area,
        "reverse_omega2": reverse_area,
        "cwm": aggregate,
        "effective_multiplicity": effective_multiplicity,
        "gauge_invariant_effective_multiplicity": gauged[1] / gauged[2],
    }


def main() -> None:
    two_scale = check_two_scale_retyping()
    width_one = check_width_one_reduction()
    holonomy = check_oriented_holonomy_boundary()

    print("BRC Foundation retrofit regression: PASS")
    print("two_scale", two_scale)
    print("width_one", width_one)
    print("holonomy", holonomy)


if __name__ == "__main__":
    main()
