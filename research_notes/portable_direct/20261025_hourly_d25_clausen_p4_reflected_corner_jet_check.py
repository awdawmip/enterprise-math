#!/usr/bin/env python3
"""Clausen p^4 reflected-corner author checks; no native CM experiment."""
from math import isqrt, factorial

def primes_1mod6(bound):
    out = []
    for p in range(7, bound + 1, 6):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            out.append(p)
    return out

def sequences(p):
    M = p**4
    r = [1]
    for n in range(p - 1):
        r.append(r[-1]*(6*n + 1)*(3*n + 1)
                 *pow(36*(n + 1)**2, -1, M) % M)
    a = 1
    W = 0
    for n in range(p):
        W = (W + (6*n + 1)*a) % M
        if n + 1 < p:
            a = (a*(2*n + 1)*(3*n + 1)*(3*n + 2)
                 *pow(36*(n + 1)**3, -1, M)) % M
    return r, W

def reflected_jet(p):
    m = (p - 1)//6
    M = p*p
    numerator = 1
    for i in range(p - 1):
        if i != m:
            numerator = numerator*(6*i + 1) % M
        if i != 2*m:
            numerator = numerator*(3*i + 1) % M
    denominator = pow(36, p - 1, M)*pow(factorial(p - 1), 2, M) % M
    s1 = numerator*pow(denominator, -1, M) % M
    rho, L = 1, 0
    s = [0]
    for h in range(1, 2*m + 1):
        s.append(s1*rho*(1+p*L) % M)
        if h < 2*m:
            rho = rho*36*h*h*pow((6*h+5)*(3*h+2), -1, M) % M
            L = (L - 2*pow(h, -1, p)
                 + 6*pow(6*h+5, -1, p)
                 + 3*pow(3*h+2, -1, p)) % p
    return s1, s

def check(p, with_double_sum):
    m, M = (p - 1)//6, p**4
    r, W = sequences(p)
    s1, s = reflected_jet(p)
    assert s1 == (r[p-1]//p**2) % p**2
    for h in range(1, 2*m + 1):
        assert r[p-h] % p**2 == 0
        assert (r[p-h]//p**2) % p**2 == s[h], (p, h)
    V, H, C, A_part, B_part = 0, 0, 0, 0, 0
    for j in range(1, 2*m + 1):
        V = (V+s[j]) % p**2
        H = (H+j*s[j]) % p**2
        term = 2*r[j]*((6*j+1+6*p)*V-6*H)
        C = (C+term) % p**2
        if j <= m:
            A_part = (A_part+term) % p**2
        else:
            B_part = (B_part+term) % p**2
    R = sum(r) % M
    D = sum(n*v for n, v in enumerate(r)) % M
    assert (R*(R+12*D)-p*p*C-W) % M == 0, (p, "Clausen")
    if with_double_sum:
        Q = sum((6*(j+k)+1)*r[j]*r[k]
                for j in range(p) for k in range(p-j, p)) % M
        assert Q == p*p*C % M, (p, "independent_Q")
    return p, C % p, (C - C % p)//p, A_part, B_part

if __name__ == "__main__":
    cases = primes_1mod6(300) + [373, 1327, 19963]
    for p in cases:
        if p in (13, 19, 373, 1327, 19963):
            print(check(p, p <= 300))
        else:
            check(p, p <= 300)
    print("PASS:", len(cases), "p ≡ 1 (mod 6) primes; independent Q double sums for",
          len([p for p in cases if p <= 300]), "primes.")
    print("AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_NATIVE_CM")
