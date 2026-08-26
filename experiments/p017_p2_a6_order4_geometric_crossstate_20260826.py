#!/usr/bin/env python3
"""Exact-rational certificate for the P017 a6 order-4 geometric B-spline package.

Checks parameter identities, source-Lemma-4 margins, explicit-cutoff structural
powers, the elementary pi>3 block-tail constant, the exact Tier-A splice tail
inequality, and the reciprocal-sum frequency-window exponents.

This does not propagate constants through the full Cauchy quadruple sum or
Rosser/Iwaniec factorization.
"""

from fractions import Fraction as Q


K0 = 116_009_280_740_973_308
X0 = K0 * K0


def main() -> None:
    theta = Q(4999, 10000)
    d = Q(5, 9)
    eps = Q(1, 200)
    p = 4
    eta = Q(1, 40)
    rho = Q(6, 5)

    mu = Q(161777, 360000)
    nu = Q(4247, 40000)

    assert mu + nu == d

    # Original source-Lemma-4 admissibility margins.
    a2 = theta - 6 * eps - mu
    a3 = 1 - (mu + 2 * nu)
    a4 = Q(5, 2) * theta - Q(1, 2) - 4 * eps - (mu + 2 * nu)

    assert a2 == Q(7387, 360000) > 0
    assert a3 == Q(121777, 360000) > 0
    assert a4 == Q(24487, 360000) > 0

    # Explicit-cutoff structural powers inherited from the frozen B-spline replay.
    diag = (theta - eta - mu) / 2
    off = (
        mu
        - 2 * (d - theta)
        - (1 - theta) / 2
        - Q(5, 2) * eta
    ) / 2
    tail = (p - 1) * eta - (d - theta)

    assert diag == Q(9187, 720000) > 0
    assert off == diag
    assert tail == Q(1741, 90000) > diag

    # Ratio-6/5 geometric block, M,N>=1000.
    # C_4 = 512/(3*pi^4) < 512/243 from pi>3.
    c4_upper = Q(512, 243)
    block_tail_constant = c4_upper * (rho - 1 + Q(1, 1000)) ** 2
    assert block_tail_constant == Q(35912, 421875)
    assert block_tail_constant < Q(86, 1000)

    # Exact splice inequality:
    # block_tail_constant * X0^(-1741/90000) < 19/1000.
    ratio = block_tail_constant / Q(19, 1000)
    assert ratio > 1
    assert ratio.numerator**90000 < (
        ratio.denominator**90000 * X0**1741
    )

    # Existing explicit reciprocal-sum lemma frequency window.
    lower_exp = 1 - 2 * nu - Q(5, 3) * mu
    upper_margin = 3 * mu - (d + 1 + eta - theta - nu)

    assert lower_exp == Q(41777, 1080000) > 0
    assert upper_margin == Q(67259, 180000) > 0
    assert Q(10, 3) / lower_exp == Q(3600000, 41777)

    # Tier-A splice is overwhelmingly beyond the lower frequency threshold:
    # X0^lower_exp >= rho^(10/3).
    # Clear denominators 3, 1080000: X0^41777 >= rho^3600000.
    assert X0**41777 * 5**3600000 >= 6**3600000

    print("P017 a6 order-4 geometric cross-state certificate: PASS")
    print("mu =", mu, "~=", float(mu))
    print("nu =", nu, "~=", float(nu))
    print("delta_diag = delta_off =", diag, "~=", float(diag))
    print("delta_tail =", tail, "~=", float(tail))
    print("block tail constant <", block_tail_constant, "~=", float(block_tail_constant))
    print("splice block tail / y < 19/1000")
    print("reciprocal lower exponent =", lower_exp, "~=", float(lower_exp))
    print("reciprocal upper margin =", upper_margin, "~=", float(upper_margin))


if __name__ == "__main__":
    main()
