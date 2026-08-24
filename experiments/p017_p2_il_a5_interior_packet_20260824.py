"""Exact rational checks for the robust P017 / Iwaniec-Laborde a=5 packet.

This checks parameter geometry only.  The analytic Iwaniec-Laborde lemmas and
the numerical Jurkat-Richert main integral remain external/analytic inputs.
"""

from fractions import Fraction as Q


def main() -> None:
    theta = Q(49, 100)
    a = Q(5)
    d = Q(3, 5)
    b = Q(3)
    c = Q(13, 3)
    eps = Q(1, 100)

    assert Q(3, 7) < theta < Q(1, 2)
    assert Q(1) <= b < c <= a
    assert b + c + 1 == a / d == Q(25, 3)

    lower_break = d * b / a
    upper_break = d * c / a
    assert lower_break == Q(9, 25)
    assert upper_break == Q(13, 25)
    assert lower_break < theta < upper_break

    # Lemma-4 product-level room after the displayed epsilon losses.
    lemma4_max = 2 * theta - Q(5, 14) - 2 * eps
    assert lemma4_max == Q(211, 350)
    assert d == Q(210, 350)
    assert lemma4_max - d == Q(1, 350)

    # A concrete admissible exponent split M*N=D.
    m_exp = theta - eps
    n_exp = d - m_exp
    assert m_exp == Q(12, 25)  # 0.48
    assert n_exp == Q(3, 25)   # 0.12
    assert n_exp < theta - Q(5, 14) - eps
    assert m_exp + n_exp == d

    # Lemma-6 order chain.
    z_exp = d / a
    z2_exp = 2 * z_exp
    d1_exp = (3 * theta - 1) / 2 - 2 * eps
    w_exp = upper_break
    assert z_exp == Q(3, 25)
    assert z2_exp == Q(6, 25)
    assert d1_exp == Q(43, 200)
    assert d1_exp < z2_exp < theta < w_exp < Q(3, 2) * theta

    # The high-tail normalized ratio simplifies exactly.
    R = 4 * (w_exp - theta) / (3 * theta - 1)
    assert R == Q(12, 47)

    print("P017 P2 a=5 interior packet: exact rational checks passed")
    print(
        f"theta={theta}, d={d}, a={a}, b={b}, c={c}, "
        f"lemma4_slack={lemma4_max-d}, tail_R={R}"
    )


if __name__ == "__main__":
    main()
