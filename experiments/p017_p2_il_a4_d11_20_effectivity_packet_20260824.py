"""Exact checks for the P017 / Iwaniec-Laborde d=11/20 effectivity packet.

The script checks parameter geometry, the exact rational main-term lower-bound
certificate, and the safe power exponent eta=1/180.  It does not make the
multiplicative constants in the analytic remainder estimates explicit.
"""

from fractions import Fraction as Q


def main() -> None:
    theta = Q(49, 100)
    d = Q(11, 20)
    a = Q(4)
    b = Q(29, 11)
    c = Q(40, 11)
    eps = Q(1, 28)
    eta = Q(1, 180)

    assert Q(3, 7) < theta < Q(1, 2)
    assert Q(1) < b < c < a
    assert b + c + 1 == a / d == Q(80, 11)

    lower_break = d * b / a
    upper_break = d * c / a
    assert lower_break == Q(29, 80)
    assert upper_break == Q(1, 2)
    assert lower_break < theta < upper_break

    lemma4_max = 2 * theta - Q(5, 14) - 2 * eps
    assert lemma4_max == Q(193, 350) == Q(386, 700)
    assert d == Q(385, 700)
    assert lemma4_max - d == Q(1, 700)

    m_exp = theta - eps
    n_exp = d - m_exp
    n_max = theta - Q(5, 14) - eps
    assert m_exp == Q(159, 350)
    assert n_exp == Q(67, 700)
    assert n_max == Q(68, 700)
    assert n_max - n_exp == Q(1, 700)
    assert m_exp + n_exp == d

    assert eta < eps / 6
    assert eta == Q(1, 180)

    z_exp = d / a
    z2_exp = 2 * z_exp
    d1_exp = (3 * theta - 1) / 2 - 2 * eps
    w_exp = upper_break
    assert z_exp == Q(11, 80)
    assert z2_exp == Q(11, 40)
    assert d1_exp == Q(229, 1400)
    assert d1_exp < z2_exp < theta < w_exp < Q(3, 2) * theta

    tail = 4 * (w_exp - theta) / (3 * theta - 1)
    assert tail == Q(4, 47)

    r0_num = 3**10 * 224**2 * 55**11
    r0_den = 392**11
    assert Q(r0_num, r0_den) > Q(6, 5)

    # B/C = log(R0)/11 > log(6/5)/11 > 1/66.
    # Therefore S = 2 B/C - (4/47)^2 > 1/33 - 16/2209.
    margin = Q(1, 33) - Q(16, 2209)
    assert margin == Q(1681, 72897)
    assert margin > Q(23, 1000)

    print("P017 P2 d=11/20 effectivity packet: exact checks passed")
    print("lemma4 product slack =", lemma4_max - d)
    print("safe eta =", eta)
    print("certified net main margin >", margin, "=", float(margin))


if __name__ == "__main__":
    main()
