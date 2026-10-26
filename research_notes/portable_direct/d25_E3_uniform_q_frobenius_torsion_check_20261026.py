#!/usr/bin/env python3
"""Exact finite-field checks for the D25 original E3 uniform geometric q-Frobenius theorem.
Portable author-only; NOT a native H0/B0 [X]U experiment or a formal CM theorem checker.
"""
from fractions import Fraction


def pair_mul(x, y):
    return (x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def pair_pow(x, k):
    ans = (1, 0)
    for _ in range(k):
        ans = pair_mul(ans, x)
    return ans


def check_CM_j_identity():
    t = (Fraction(1, 2), Fraction(-1, 4))
    a = (9-8*t[0], -8*t[1])
    lhs = pair_mul(pair_pow(t, 3), (1-t[0], -t[1]))
    j = (2417472, 1707264)
    assert pair_mul(j, lhs) == tuple(27*z for z in pair_pow(a, 3))
    jj = pair_mul(j, j)
    assert (jj[0]-4834944*j[0]+14670139392,
            jj[1]-4834944*j[1]) == (0, 0)


def count_E3(p):
    assert p >= 13 and p % 24 in (13, 19)
    inv4, inv27 = pow(4, -1, p), pow(27, -1, p)
    t = ((2*inv4)%p, -inv4%p)
    c = (t[0]*inv27%p, t[1]*inv27%p)

    def mul(a, b):
        return ((a[0]*b[0]+2*a[1]*b[1])%p,
                (a[0]*b[1]+a[1]*b[0])%p)

    assert pow(2, (p-1)//2, p) == p-1
    assert pow((-6)%p, (p-1)//2, p) == p-1
    assert p % 3 == 1
    chi = [0]+[1 if pow(n, (p-1)//2, p)==1 else -1
               for n in range(1, p)]
    S = 0
    for a in range(p):
        for b in range(p):
            x = (a, b)
            d = ((a+c[0])%p, (b+c[1])%p)
            d2 = mul(d, d)
            x3 = mul(mul(x, x), x)
            D = ((d2[0]+4*x3[0])%p, (d2[1]+4*x3[1])%p)
            norm = (D[0]*D[0]-2*D[1]*D[1])%p
            S += chi[norm]
    points = p*p+1+S
    trace = p*p+1-points
    assert S == -2*p and points == (p-1)**2 and trace == 2*p
    return (p, p*p, S, points, trace)


if __name__ == "__main__":
    check_CM_j_identity()
    print("EXACT Q(sqrt2) j, H_-24: PASS")
    for p in (13, 19, 37, 43, 61, 67, 211, 373):
        print("p q signed_character_sum points trace", *count_E3(p))
    print("PASS: exhausted every F_(p²) x coordinate in listed eight fibers")
