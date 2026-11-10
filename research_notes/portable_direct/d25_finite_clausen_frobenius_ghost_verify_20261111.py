#!/usr/bin/env python3
"""Exact F_p polynomial verifier for D25 Clausen-Frobenius ghost repair.
Original-class native H0/B0/Source operations are not called.
"""
from math import comb, isqrt


def primes(n):
    s = bytearray(b"\x01") * (n + 1)
    s[:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i*i:n+1:i] = b"\x00" * ((n - i*i) // i + 1)
    return [i for i in range(5,n+1) if s[i]]


def validate(p):
    eps = int(p % 6 == 5)
    b = p//3
    d = (p-1)//6 if not eps else (2*p-1)//3
    A = (p-1)//6 if not eps else (5*p-1)//6
    B = (p-1)//3 if not eps else (2*p-1)//3
    assert d == min(A,B) and 2*d == b + eps*p
    # Two Gauss-coefficient sources: modular recurrence and independent binomials.
    c = [1]
    for k in range(d):
        c.append(c[-1]*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,p)%p)
    assert c == [comb(A,k)*comb(B,k)%p for k in range(d+1)]
    f = [1]
    for k in range(b):
        f.append(f[-1]*(2*k+1)*(3*k+1)*(3*k+2)*
                 pow(18*(k+1)**3,-1,p)%p)
    h = [0]*(2*d+1)
    for i,a in enumerate(c):
        for j,v in enumerate(c):
            h[i+j] = (h[i+j] + a*v)%p
    expected = f + [0]*(len(h)-len(f))
    if eps:
        for k,a in enumerate(f):
            expected[p+k] = (-a)%p
    assert h == expected, f"coefficient failure p={p}"
    x = pow(2,-1,p)
    g = sum(a*pow(x,k,p) for k,a in enumerate(c))%p
    dg = sum(k*a*pow(x,k-1,p) for k,a in enumerate(c) if k)%p
    F = sum(a*pow(x,k,p) for k,a in enumerate(f))%p
    W = sum((6*k+1)*a*pow(x,k,p) for k,a in enumerate(f))%p
    denom = pow((1-eps*x)%p,-1,p)
    assert F == g*g*denom%p
    assert W == g*(g+12*x*dg)*denom%p
    return len(h), W, h[p] if eps else 0


def main():
    large=[1009,1013,1571,1997]
    ps=primes(1000)+[p for p in large if all(p%i for i in range(2,isqrt(p)+1))]
    total=0
    for p in ps:
        count, w, ghost=validate(p)
        total+=count
        if p in (5,7,11,13,157,373,1013,1997):
            print(f"p={p}, W_modp={w}, ghost_xp={ghost}, checked={count}")
    print(f"PASS {len(ps)} primes, {total} exact coefficients")


if __name__ == "__main__":
    main()
