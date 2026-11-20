#!/usr/bin/env python3
"""Exact dependency-free projective certificates for EC49FVH.

Construct primitive integer phase polynomials H_{h,k}(x) after removing
only the x=1 boundary factor, then check no roots in P^1(F_p).
"""
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path

U = F(4822040484, 8132285009)
GAMMA = F(141024, 1653649)
A = [F(0), F(640, 637), F(-3, 637)]
B = [1 - U, U * (1-GAMMA), U * GAMMA]


def trim(z):
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return z


def add(a, b):
    z = [F(0)] * max(len(a), len(b))
    for j, v in enumerate(a):
        z[j] += v
    for j, v in enumerate(b):
        z[j] += v
    return trim(z)


def mul(a, b):
    z = [F(0)] * (len(a) + len(b) - 1)
    for j, v in enumerate(a):
        for i, w in enumerate(b):
            z[i+j] += v*w
    return trim(z)


def scale(a, c):
    return trim([v*c for v in a])


def eval_poly(a, x):
    y = F(0)
    for c in reversed(a):
        y = y*x+c
    return y


def div_x_minus_one(a):
    q = [F(0)] * (len(a)-1)
    q[-1] = a[-1]
    for i in range(len(q)-2, -1, -1):
        q[i] = a[i+1] + q[i+1]
    assert a[0] + q[0] == 0, "expected boundary factor missing"
    return trim(q)


def primitive_integer(a):
    denominator = 1
    for c in a:
        denominator = lcm(denominator, c.denominator)
    z = [int(c*denominator) for c in a]
    content = 0
    for c in z:
        content = gcd(content, abs(c))
    assert content != 0
    z = [v//content for v in z]
    if z[-1] < 0:
        z = [-v for v in z]
    return z


def phase_polynomial(h, k):
    # f(z)=z^h(1-z)^(k-h), Q=(f(a)-f(b))/(a-b).
    aa = [[F(1)]]
    bb = [[F(1)]]
    for _ in range(k):
        aa.append(mul(aa[-1], A))
        bb.append(mul(bb[-1], B))
    q = [F(0)]
    for i in range(h, k+1):
        c = (-1)**(i-h)*comb(k-h, i-h)
        term = [F(0)]
        for j in range(i):
            term = add(term, mul(aa[i-1-j], bb[j]))
        q = add(q, scale(term, c))
    # Each (1-a),(1-b) has a factor (1-x), and (a-b)
    # has exactly one. Thus (x-1)^(k-h-1) divides Q.
    for _ in range(k-h-1):
        q = div_x_minus_one(q)
    return primitive_integer(q)


def primes_to(n):
    for p in range(2, n+1):
        if all(p % q for q in range(2, int(p**0.5)+1)):
            yield p


def eval_mod(coeff, x, p):
    v = 0
    for c in reversed(coeff):
        v = (v*x+c) % p
    return v


def certificate(coeff):
    for p in primes_to(307):
        # Nonzero leading coefficient excludes projective infinity.
        if coeff[-1] % p and all(eval_mod(coeff, z, p) != 0 for z in range(p)):
            return p
    raise AssertionError("No searched projective-prime obstruction")


def main():
    assert 0 < eval_poly(A, F(7, 20)) < eval_poly(B, F(7, 20)) < 1
    report = []
    for k in range(2, 26):
        for h in range(1, k):
            if gcd(h, k) != 1:
                continue
            coeff = phase_polynomial(h, k)
            p = certificate(coeff)
            assert coeff[-1] % p
            assert all(eval_mod(coeff, z, p) != 0 for z in range(p))
            # Exact independent sample crosscheck, not the theorem proof.
            for x in [F(1, 7), F(7, 20), F(9, 10)]:
                a, b = eval_poly(A, x), eval_poly(B, x)
                f = lambda z: z**h * (1-z)**(k-h)
                q = (f(a)-f(b))/(a-b)
                assert q != 0
                assert eval_poly(coeff, x) != 0
            report.append((h, k, len(coeff)-1, p))
    assert len(report) == 199
    # The half-phase binary quadratic reduces mod 5 to m^2+2d^2,
    # which is anisotropic on nonzero pairs in F_5.
    assert all((m*m+2*d*d) % 5 != 0 for m in range(5)
               for d in range(5) if (m, d) != (0, 0))
    with Path(__file__).with_name("EC49FVH_PHASE_CERTIFICATES.csv").open(
            "w", encoding="utf-8") as fh:
        fh.write("h,k,degree,prime\n")
        for h, k, deg, p in report:
            fh.write(f"{h},{k},{deg},{p}\n")
    for k in range(2, 26):
        block = [(h, p, deg) for h, kk, deg, p in report if kk == k]
        print(f"k={k:2d} : " + " ; ".join(
            f"h={h}:p={p},deg={deg}" for h, p, deg in block))
    print("CERTIFIED: 199/199 reduced phases h/k with 2<=k<=25; all rational x in (0,1) excluded")
    print("Certificate semantics: no roots in P^1(F_p), including denominator-divisible x; ALL PASS")


if __name__ == "__main__":
    main()
