#!/usr/bin/env python3
"""Exact-rational source-decimal certificate for the a6 root-complete main term.

This is the same Laborde/Iwaniec source-decimal reconstruction as the frozen
a6 five-ninth package, but the W1/W2 analysis split is moved to the physical
root endpoint D^(c/a)=x^(1/2).  Thus alpha=1/9, 6/(1+alpha)=c=27/5,
6*alpha/(1+alpha)=6-c=3/5, and the terminal quadratic defect vanishes.

The certificate proves G_root>287/2500 and G_root-G_old>0.  It does not make
Mertens/PNT finite errors explicit at the Tier-A splice.
"""

from fractions import Fraction as Q


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(c, a):
    if c >= 0:
        return c*a[0], c*a[1]
    return c*a[1], c*a[0]


def mul(a, b):
    vals = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(vals), max(vals)


def square(a):
    lo, hi = a
    if lo <= 0 <= hi:
        return Q(0), max(lo*lo, hi*hi)
    return min(lo*lo, hi*hi), max(lo*lo, hi*hi)


def const(x):
    return x, x


def log_bounds(x: Q, degree: int = 30):
    z = (x - 1)/(x + 1)
    partial = sum(
        2*z**(2*k + 1)/Q(2*k + 1) for k in range(degree + 1)
    )
    tail = 2*abs(z)**(2*degree + 3) / (
        Q(2*degree + 3)*(1-z*z)
    )
    if z >= 0:
        return partial, partial + tail
    return partial - tail, partial


def common_reference():
    c0 = Q(51828,10000), Q(51829,10000)
    b0 = Q(48698,10000), Q(48699,10000)
    g0 = Q(177,100000), Q(178,100000)
    theta0 = Q(9,20)
    d0 = Q(19,35)
    alpha0 = d0/theta0 - 1
    root0 = Q(6)/(1+alpha0)
    small0 = Q(6)*alpha0/(1+alpha0)
    factor0 = (
        Q(3)*(3*theta0-1)/(Q(2)*(1+alpha0)*theta0)
    )**2

    b1 = scale(
        Q(1,2),
        add(
            scale(1/factor0, add(c0, const(-root0))),
            scale(-Q(1,6), log_bounds(alpha0)),
        ),
    )

    term01 = scale(-Q(1,6), mul(c0, log_bounds(root0)))
    term02 = scale(
        -Q(1,6),
        mul(add(const(Q(6)), scale(-1,c0)), log_bounds(small0)),
    )
    denominator0 = Q(3)*(3*theta0-1)
    ratio0 = scale(
        1/denominator0,
        add(scale(d0,c0), const(-6*theta0)),
    )
    n0 = add(add(term01, term02), scale(-Q(2), square(ratio0)))
    return c0, b0, g0, b1, n0


def n_term(theta: Q):
    d = Q(5,9)
    c = Q(27,5)
    alpha = d/theta - 1
    root = Q(6)/(1+alpha)
    small = Q(6)*alpha/(1+alpha)
    delta1 = d/3
    n = add(
        scale(-c/6, log_bounds(root)),
        scale(-(6-c)/6, log_bounds(small)),
    )
    ratio = (c*d/6-theta)/delta1
    n = add(n, const(-2*ratio*ratio))
    return alpha, root, small, n


def main() -> None:
    c0, b0, g0, b1, n0 = common_reference()
    b = Q(22,5)
    c = Q(27,5)

    old_theta = Q(4999,10000)
    old_alpha, old_root, old_small, n_old = n_term(old_theta)
    assert old_alpha == Q(5009,44991)
    assert old_root == Q(134973,25000)
    assert old_small == Q(15027,25000)

    # Root-complete split: theta_split=1/2, alpha=1/9.
    root_theta = Q(1,2)
    alpha, root, small, n_root = n_term(root_theta)
    assert alpha == Q(1,9)
    assert root == c == Q(27,5)
    assert small == 6-c == Q(3,5)
    # cd/6=1/2 exactly, so the quadratic terminal defect is zero.
    assert c*Q(5,9)/6 == root_theta

    old_width = add(c0, scale(-1,b0))
    width_delta = add(const(c-b), scale(-1,old_width))
    g_root = add(
        add(g0, mul(b1, width_delta)),
        add(n_root, scale(-1,n0)),
    )

    assert g_root[0] > Q(287,2500)

    # The improvement over the previous theta=4999/10000 split is independent
    # of the reconstructed B1/B2/reference constants: it is n_root-n_old.
    improvement = add(n_root, scale(-1,n_old))
    assert improvement[0] > 0
    assert improvement[0] > Q(4033, 10_000_000_000)  # 4.033e-7

    print("P017 a6 root-complete main certificate: PASS")
    print("G_root lower =", float(g_root[0]))
    print("G_root upper =", float(g_root[1]))
    print("certified G_root > 287/2500 = 0.1148")
    print("G_root-G_old in [", float(improvement[0]), ",", float(improvement[1]), "]")


if __name__ == "__main__":
    main()
