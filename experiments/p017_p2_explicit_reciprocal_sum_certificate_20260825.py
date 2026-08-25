#!/usr/bin/env python3
"""Exact arithmetic certificate for the explicit reciprocal-sum application window.

This checks the rational exponent margins, the clean constant budget, and the
exact comparison (6/5)^350 < 10^31. It does not replace Patel's analytic
Kuzmin-Landau / second-derivative lemmas and does not prove the full sieve.
"""

from fractions import Fraction as Q


def main() -> None:
    rho = Q(6, 5)
    theta = Q(4999, 10000)
    d = Q(4, 7)
    eta = Q(1, 70)
    mu = Q(16, 35)
    nu = Q(4, 35)

    # Lower-frequency application margin.
    lower_margin = 1 - 2 * nu - Q(5, 3) * mu
    assert lower_margin == Q(1, 105) > 0

    # Geometric block loss rho^2 from n1*n2 and rho^(4/3) from the m-lemma.
    # Raising X^(1/105) >= rho^(10/3) to the third power gives
    # X^(1/35) >= rho^10, equivalently X >= rho^350.
    assert 6**350 < 5**350 * 10**31

    # Upper-frequency application margin.
    tmax_exp = d + 1 + eta - theta - nu
    upper_margin = 3 * mu - tmax_exp
    assert tmax_exp == Q(68007, 70000)
    assert upper_margin == Q(3999, 10000) > 0

    # It is enough that X^upper_margin >= 16*rho = 96/5.
    # X=10^4 already clears this by exact integer arithmetic after raising
    # to the denominator 10000.
    assert (10**4) ** 3999 >= (Q(96, 5)) ** 10000

    # High-frequency normalized constant proof, using pi>3 and sqrt(5)>11/5.
    # Curvature contribution: 4*(2/5+4)*(6/11) = 48/5 = 9.6.
    curvature_constant = 4 * (Q(2, 5) + 4) * Q(6, 11)
    assert curvature_constant == Q(48, 5)

    # Remaining normalized piece is < 4.8, hence total < 14.4 < 15.
    residual_upper = Q(24, 5)
    assert curvature_constant + residual_upper == Q(72, 5) < 15

    print("P017 explicit reciprocal-sum certificate: PASS")
    print("lower exponent margin =", lower_margin, "~=", float(lower_margin))
    print("upper exponent margin =", upper_margin, "~=", float(upper_margin))
    print("(6/5)^350 < 10^31: verified exactly")
    print("clean reciprocal-sum constant = 15")


if __name__ == "__main__":
    main()
