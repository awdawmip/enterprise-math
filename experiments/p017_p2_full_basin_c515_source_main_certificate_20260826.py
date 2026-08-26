#!/usr/bin/env python3
"""Exact source-decimal main-coefficient certificate for b=93/20,c=103/20.

This uses exactly the same provenance convention as the frozen a6 root-edge
certificate: the 1981 printed optimum decimals are interpreted as prefix
intervals, B1 is reconstructed from the printed stationary point, and B2 is
eliminated by subtracting the published reference identity.  All logarithms
are enclosed by Fraction atanh series.

The terminal analysis split is taken at D^(c/6), so alpha=(6-c)/c and the
near-terminal quadratic defect vanishes.  The checker proves

    G_c > 19/250 = 0.076

and, at the Tier-A full-basin scale, the corresponding p.53 source main factor

    12 G_c / ((2c-b-1) log D) > 449/100000 = 0.00449.

The latter is a source-asymptotic bookkeeping scale before finite epsilon /
Mertens normalization errors are charged; it is not by itself a finite P2
certificate.
"""

from fractions import Fraction as Q

K0 = 116_009_280_740_973_308
W = K0 + 1


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


def log_bounds(x: Q, degree: int = 30) -> tuple[Q, Q]:
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


def log_int_bounds(n: int, degree: int = 30) -> tuple[Q, Q]:
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return Q(0), Q(0)
    log2 = log_bounds(Q(2), degree)
    k = n.bit_length() - 1
    reduced = Q(n, 1 << k)
    lr = log_bounds(reduced, degree)
    return k * log2[0] + lr[0], k * log2[1] + lr[1]


def source_interval() -> tuple[Q, Q]:
    # Iwaniec-Laborde printed reference prefixes.
    c0 = Q(51828, 10000), Q(51829, 10000)
    b0 = Q(48698, 10000), Q(48699, 10000)
    g0 = Q(177, 100000), Q(178, 100000)

    theta0 = Q(9, 20)
    d0 = Q(19, 35)
    alpha0 = Q(13, 63)
    root0 = Q(189, 38)
    small0 = Q(39, 38)
    factor0 = Q(21609, 23104)

    b1 = scale(
        Q(1, 2),
        add(
            scale(1 / factor0, add(c0, const(-root0))),
            scale(-Q(1, 6), log_bounds(alpha0)),
        ),
    )

    term01 = scale(-Q(1, 6), mul(c0, log_bounds(root0)))
    term02 = scale(
        -Q(1, 6),
        mul(add(const(Q(6)), scale(-1, c0)), log_bounds(small0)),
    )
    denominator0 = Q(3) * (3 * theta0 - 1)
    ratio0 = scale(
        1 / denominator0,
        add(scale(d0, c0), const(-6 * theta0)),
    )
    n0 = add(add(term01, term02), scale(-Q(2), square(ratio0)))

    # Finite-oriented rational terminal packet.
    c = Q(103, 20)
    b = Q(93, 20)
    assert b + c == Q(49, 5)
    assert c - b == Q(1, 2)

    # Split at the terminal horizon: 1/(1+alpha)=c/6.
    # Therefore 6/(1+alpha)=c and 6alpha/(1+alpha)=6-c,
    # and the quadratic terminal mismatch is exactly zero.
    nnew = add(
        scale(-c / 6, log_bounds(c)),
        scale(-(6 - c) / 6, log_bounds(6 - c)),
    )

    old_width = add(c0, scale(-1, b0))
    width_delta = add(const(c - b), scale(-1, old_width))

    gnew = add(
        add(g0, mul(b1, width_delta)),
        add(nnew, scale(-1, n0)),
    )

    assert gnew[0] > Q(19, 250)
    return gnew


def main() -> None:
    g = source_interval()

    c = Q(103, 20)
    b = Q(93, 20)
    denom = 2 * c - b - 1
    assert denom == Q(93, 20)

    # D=W^(10/9), so log D=(10/9) log W.  For a lower main scale,
    # use the certified G lower bound and an upper bound for log D.
    _, logw_hi = log_int_bounds(W)
    logd_hi = Q(10, 9) * logw_hi
    main_scale_lower = Q(12) * Q(19, 250) / (denom * logd_hi)

    assert main_scale_lower > Q(449, 100000)

    # Combining only the already-rigorous finite carry budgets:
    # lower base <0.00145 L and terminal T4 <0.00125 L.
    formal_reserve = Q(449, 100000) - Q(145, 100000) - Q(125, 100000)
    assert formal_reserve == Q(179, 100000)

    print("P017 c=103/20 source-main certificate: PASS")
    print("G interval lower ~=", float(g[0]))
    print("G interval upper ~=", float(g[1]))
    print("G > 19/250 = 0.076")
    print("source main scale > 0.00449 L")
    print("formal reserve after base+T4 > 0.00179 L")
    print("finite source epsilon/Mertens and T1-T3 are still uncharged")


if __name__ == "__main__":
    main()
