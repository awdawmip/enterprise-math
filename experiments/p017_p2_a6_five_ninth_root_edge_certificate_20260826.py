#!/usr/bin/env python3
"""Exact-rational certificate for the P017 a=6 five-ninth root-edge package.

The main-term enclosure uses the decimal prefixes printed by Iwaniec-Laborde
(1981) as rational intervals, then eliminates B2 by subtracting the reference
identity.  All logarithms are enclosed by the atanh series with an explicit
rational tail.  The parameter and trivial-pair power bookkeeping is exact.
"""

from fractions import Fraction as Q


def add(a: tuple[Q, Q], b: tuple[Q, Q]) -> tuple[Q, Q]:
    return a[0] + b[0], a[1] + b[1]


def scale(c: Q, a: tuple[Q, Q]) -> tuple[Q, Q]:
    if c >= 0:
        return c * a[0], c * a[1]
    return c * a[1], c * a[0]


def mul(a: tuple[Q, Q], b: tuple[Q, Q]) -> tuple[Q, Q]:
    vals = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(vals), max(vals)


def square(a: tuple[Q, Q]) -> tuple[Q, Q]:
    lo, hi = a
    if lo <= 0 <= hi:
        return Q(0), max(lo * lo, hi * hi)
    return min(lo * lo, hi * hi), max(lo * lo, hi * hi)


def const(x: Q) -> tuple[Q, Q]:
    return x, x


def log_bounds(x: Q, degree: int) -> tuple[Q, Q]:
    if x <= 0:
        raise ValueError("x must be positive")
    z = (x - 1) / (x + 1)
    partial = Q(0)
    for k in range(degree + 1):
        partial += 2 * z ** (2 * k + 1) / (2 * k + 1)
    tail = 2 * abs(z) ** (2 * degree + 3) / (
        (2 * degree + 3) * (1 - z * z)
    )
    if z >= 0:
        return partial, partial + tail
    return partial - tail, partial


def source_decimal_main_interval() -> tuple[Q, Q]:
    degree = 30

    # Printed 1981 prefixes.
    c0 = Q(51828, 10000), Q(51829, 10000)
    b0 = Q(48698, 10000), Q(48699, 10000)
    g0 = Q(177, 100000), Q(178, 100000)

    theta0 = Q(9, 20)
    d0 = Q(19, 35)
    alpha0 = d0 / theta0 - 1
    assert alpha0 == Q(13, 63)

    root0 = Q(6) / (1 + alpha0)
    small0 = Q(6) * alpha0 / (1 + alpha0)
    factor0 = (
        Q(3) * (3 * theta0 - 1) / (Q(2) * (1 + alpha0) * theta0)
    ) ** 2
    assert root0 == Q(189, 38)
    assert small0 == Q(39, 38)
    assert factor0 == Q(21609, 23104)

    # First-order reconstruction of B1, with interval c0 and log(alpha0).
    b1 = scale(
        Q(1, 2),
        add(
            scale(1 / factor0, add(c0, const(-root0))),
            scale(-Q(1, 6), log_bounds(alpha0, degree)),
        ),
    )

    # Reference nonconstant N0(c0).
    term01 = scale(-Q(1, 6), mul(c0, log_bounds(root0, degree)))
    term02 = scale(
        -Q(1, 6),
        mul(add(const(Q(6)), scale(-1, c0)), log_bounds(small0, degree)),
    )
    denominator0 = Q(3) * (3 * theta0 - 1)
    ratio0 = scale(
        1 / denominator0,
        add(scale(d0, c0), const(-6 * theta0)),
    )
    n0 = add(add(term01, term02), scale(-Q(2), square(ratio0)))

    # New root-edge packet.
    theta = Q(4999, 10000)
    d = Q(5, 9)
    a = Q(6)
    b = Q(22, 5)
    c = Q(27, 5)

    assert b + c + 1 == a / d
    assert 3 < b < c < a
    assert d * c / a == Q(1, 2)
    assert d * b / a == Q(11, 27)
    assert d / a == Q(5, 54)

    alpha = d / theta - 1
    assert alpha == Q(5009, 44991)
    root = Q(6) / (1 + alpha)
    small = Q(6) * alpha / (1 + alpha)
    assert root == Q(134973, 25000)
    assert small == Q(15027, 25000)

    delta1 = d / 3
    assert delta1 == Q(5, 27)

    nstar = add(
        scale(-c / 6, log_bounds(root, degree)),
        scale(-(6 - c) / 6, log_bounds(small, degree)),
    )
    ratio_star = (c * d / 6 - theta) / delta1
    nstar = add(nstar, const(-2 * ratio_star * ratio_star))

    old_width = add(c0, scale(-1, b0))
    width_delta = add(const(c - b), scale(-1, old_width))

    gstar = add(
        add(g0, mul(b1, width_delta)),
        add(nstar, scale(-1, n0)),
    )

    # Safe rational lower bound.
    assert gstar[0] > Q(287, 2500)
    return gstar


def trivial_pair_certificate() -> None:
    theta = Q(4999, 10000)
    d = Q(5, 9)
    eps = Q(1, 200)
    mu = Q(31, 72)
    nu = Q(1, 8)

    assert mu + nu == d

    a2_margin = theta - 6 * eps - mu
    a3_margin = 1 - (mu + 2 * nu)
    a4_margin = Q(5, 2) * theta - Q(1, 2) - 4 * eps - (mu + 2 * nu)

    assert a2_margin == Q(3541, 90000) > 0
    assert a3_margin == Q(23, 72) > 0
    assert a4_margin == Q(1771, 36000) > 0

    diag_square_exponent = mu - theta + 3 * eps
    off_square_exponent = 2 * (d - theta) + (1 - theta) / 2 + 3 * eps - mu

    assert diag_square_exponent == -Q(4891, 90000)
    assert off_square_exponent == -Q(1951, 36000)

    diag_saving = -diag_square_exponent / 2
    off_saving = -off_square_exponent / 2
    assert diag_saving == Q(4891, 180000)
    assert off_saving == Q(1951, 72000)
    assert off_saving < diag_saving

    print("A2 margin =", a2_margin, "~=", float(a2_margin))
    print("A3 margin =", a3_margin, "~=", float(a3_margin))
    print("A4 margin =", a4_margin, "~=", float(a4_margin))
    print("diag saving =", diag_saving, "~=", float(diag_saving))
    print("off saving =", off_saving, "~=", float(off_saving))


def main() -> None:
    gstar = source_decimal_main_interval()
    print("P017 a=6 five-ninth root-edge certificate: PASS")
    print("source-decimal G interval:")
    print(" lower =", gstar[0], "~=", float(gstar[0]))
    print(" upper =", gstar[1], "~=", float(gstar[1]))
    print("certified G > 287/2500 =", float(Q(287, 2500)))
    trivial_pair_certificate()


if __name__ == "__main__":
    main()
