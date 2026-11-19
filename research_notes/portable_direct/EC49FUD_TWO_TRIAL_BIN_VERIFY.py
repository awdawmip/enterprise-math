#!/usr/bin/env python3
"""Exact Fraction regression for EC49FUD; the analytic inequalities are in the paper."""
from fractions import Fraction as F

E = F(1048576, 18958647)
m = F(1469, 64)
L, U = F(951, 1280), F(3, 4)
W = U - L
a = F(2807259, 163840)
b = F(41217719, 2359296)
t = F(45529434409, 2630615040)
q_infty = F(23700188425, 45529434409)


def q(e):
    return F(575) * (41217719 * e - 2359296) / (
        45529434409 * e - 2630615040
    )


def p(e, x):
    return x * (1 - e * m * (U - x * W / 2)) / (1 - e * a)


def r(e, x):
    return p(e, x) + q(e) * (1 - p(e, x))


def d1(e, x):
    return (1 - p(e, x)) ** 2 - (1 - r(e, x)) ** 2


def d2(e, x):
    return r(e, x) ** 2 - p(e, x) ** 2


def slope_bound(x):
    c = a - m * W * x / 2
    return (a - c) / (b - t) * (b * t) / (a * c)


def switching_poly(x):
    return (1826870798324832 * x * x
            + 19595036598849125 * x
            - 7973962424326116)


def main():
    assert W == F(9, 1280)
    assert a == m * (L + U) / 2
    assert b > t > a > m * L > 0
    assert (b - t) / (m * W / 2) == F(3965947, 1965522)
    assert q(E) == F(3310244525, 8132285009)
    assert q_infty > q(E)
    assert (1 - q_infty) / (2 - q_infty) == F(
        21829245984, 67358680393
    )
    assert slope_bound(F(1, 2)) == F(
        9383097168495465355, 36678362354402067936
    )
    assert slope_bound(F(1, 2)) < (1 - q_infty) / (2 - q_infty)
    assert F(9383097168495465355, 18295894360889780544) < 1
    assert switching_poly(0) < 0 < switching_poly(F(1, 2))
    assert switching_poly(F(39256, 100000)) < 0
    assert switching_poly(F(39257, 100000)) > 0

    def endpoint_p(x):
        return x * (141024 * x + 1512625) / 1653649

    def endpoint_r(x):
        return (411225984 * x * x + 4410814500 * x
                + 3310244525) / 8132285009

    sample_x = [F(0), F(1, 8), F(1, 4), F(2, 5),
                F(1, 2), F(3, 4), F(1)]
    sample_e = [F(-10**6), F(-100), F(-1), F(0), E]
    for x in sample_x:
        assert p(E, x) == endpoint_p(x)
        assert r(E, x) == endpoint_r(x)
        assert p(E, x) + r(E, x) - 1 == (
            switching_poly(x) / F(13447944972847841)
        )
        for e in sample_e:
            pe, re = p(e, x), r(e, x)
            assert 0 <= pe <= re <= 1
            assert d1(e, x) - d2(e, x) == 2 * (re - pe) * (1 - pe - re)
            if e != E and x <= F(1, 2):
                assert d1(e, x) >= d1(E, x)
            if e != E:
                assert d2(e, x) >= d2(E, x)

    x = F(1, 4)
    assert p(E, x) == F(1547881, 6614596)
    assert r(E, x) == F(4438649774, 8132285009)
    assert (1 - d1(E, x)) / 2 == F(
        1792706378557916871129377139144871,
        5787111167767792608343351627560992
    )
    assert p(E, x) + r(E, x) < 1
    print("EC49FUD: exact Fraction identities and regression PASS")
    print("quarter-width two-trial minimax risk:", (1 - d1(E, x)) / 2)


if __name__ == "__main__":
    main()
