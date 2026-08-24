"""Exact rational checks for the P017 / Iwaniec-Laborde a=6 P2 window.

This script verifies the algebraic parameter-compatibility claims in
`docs/P017_P2_IL_A6_MAXIMAL_LEGAL_WINDOW_20260824.md`.

It does not prove the analytic estimates in Iwaniec-Laborde 1981 and does not
claim an explicit all-K P2 theorem.
"""

from fractions import Fraction


def main() -> None:
    theta = Fraction(16, 35)
    d = 2 * theta - Fraction(5, 14)
    alpha = d / theta - 1

    assert d == Fraction(39, 70)
    assert alpha == Fraction(7, 32)

    # a=6, z=D^(1/6): exponent of z^2 is d/3.
    z2_exp = d / 3
    d1_exp = (3 * theta - 1) / 2
    assert z2_exp == Fraction(13, 70)
    assert d1_exp == Fraction(13, 70)
    assert z2_exp == d1_exp

    # Combining Lemma-4 and Lemma-6 exponent inequalities gives theta <= 16/35.
    # 3*(3 theta - 1)/2 <= 2 theta - 5/14.
    lhs = Fraction(3, 2) * (3 * theta - 1)
    rhs = 2 * theta - Fraction(5, 14)
    assert lhs == rhs == d

    # Weight relation b+c+1 = 6/((1+alpha) theta) = 6/d.
    bc_plus_one = Fraction(6, 1) / d
    assert bc_plus_one == Fraction(140, 13)
    assert bc_plus_one - 1 == Fraction(127, 13)

    # Negative boundary for the earlier theta=1/2, d=5/9, a=6 packet.
    theta_bad = Fraction(1, 2)
    d_bad = Fraction(5, 9)
    z2_bad = d_bad / 3
    d1_bad = (3 * theta_bad - 1) / 2
    assert z2_bad == Fraction(5, 27)
    assert d1_bad == Fraction(1, 4)
    assert z2_bad < d1_bad

    # A terminal x^(16/35) interval is asymptotically shorter than square width x^(1/2).
    assert theta < Fraction(1, 2)

    print("P017 P2 Iwaniec-Laborde a=6 parameter window: exact checks passed")
    print(f"theta_max={theta}, d={d}, alpha={alpha}, z^2 exponent={z2_exp}")


if __name__ == "__main__":
    main()
