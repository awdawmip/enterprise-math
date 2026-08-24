"""Exact arithmetic checks for the closed-form P017 / IL a=4 packet.

No analytic remainder estimate is reproved here.  The script checks the exact
parameter geometry and the elementary integer inequality used for the positive
main-term certificate.
"""

from fractions import Fraction as Q


def main() -> None:
    theta = Q(49, 100)
    d = Q(4, 7)
    a = Q(4)
    b = Q(5, 2)
    c = Q(7, 2)
    eps = Q(1, 50)

    assert Q(3, 7) < theta < Q(1, 2)
    assert Q(1) <= b < c <= a
    assert b + c + 1 == a / d == Q(7)

    lower_break = d * b / a
    upper_break = d * c / a
    assert lower_break == Q(5, 14)
    assert upper_break == Q(1, 2)
    assert lower_break < theta < upper_break

    lemma4_max = 2 * theta - Q(5, 14) - 2 * eps
    assert lemma4_max == Q(102, 175)
    assert d == Q(100, 175)
    assert lemma4_max - d == Q(2, 175)

    z_exp = d / a
    z2_exp = 2 * z_exp
    d1_exp = (3 * theta - 1) / 2 - 2 * eps
    w_exp = upper_break
    assert z_exp == Q(1, 7)
    assert z2_exp == Q(2, 7)
    assert d1_exp == Q(39, 200)
    assert d1_exp < z2_exp < theta < w_exp < Q(3, 2) * theta

    R = 4 * (w_exp - theta) / (3 * theta - 1)
    assert R == Q(4, 47)

    # Closed-form main brace ratio is > log(2)/8 because this rational exceeds 2.
    numerator = 3**7 * 10**16
    denominator = 19 * 7**21
    assert numerator > 2 * denominator

    # log(2)>1/2 then gives the rational net lower bound below.
    rational_margin = Q(1, 8) - Q(16, 2209)
    assert rational_margin == Q(2081, 17672)
    assert rational_margin > 0

    print("P017 P2 a=4 closed-form packet: exact checks passed")
    print("Lemma-4 exponent slack =", lemma4_max - d)
    print("high-tail R =", R)
    print("elementary net lower bound >", rational_margin, "=", float(rational_margin))


if __name__ == "__main__":
    main()
