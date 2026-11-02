#!/usr/bin/env python3
"""Original 216 / finite Clausen / frozen-reflected precision check (author only)."""
from math import isqrt


def primes(n):
    s = bytearray(b'\1') * (n + 1)
    s[:2] = b'\0\0'
    for k in range(2, isqrt(n) + 1):
        if s[k]:
            s[k*k::k] = b'\0' * ((n-k*k)//k+1)
    return [p for p in range(13, n+1) if s[p] and p % 24 in (13, 19)]


def sums(p, mod, keep=False):
    B = A = 1
    M = N = W = 0
    arr = []
    for k in range(p):
        if keep:
            arr.append(B)
        M = (M + B) % mod
        N = (N + k*B) % mod
        W = (W + (6*k+1)*A) % mod
        if k+1 < p:
            B = B*(6*k+1)*(3*k+1)*pow(36*(k+1)**2, -1, mod) % mod
            A = A*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3, -1, mod) % mod
    return M, N, W, arr


def detailed(p):
    m = p**5
    M, N, W, arr = sums(p, m, keep=True)
    h = (M + 12*N) % m
    Q = (M*h-W) % m
    assert M % p == Q % (p*p) == 0
    R = Q//(p*p)
    D = (((M//p)*h - 1) % p**4)//p
    E = ((W-M*h) % m)//(p*p)
    assert (D-R) % p**3 == ((W-p) % m)//(p*p)
    assert (E+R) % p**3 == 0
    if p <= 373:
        direct = sum((6*(i+j)+1)*arr[i]*arr[j]
                     for i in range(p) for j in range(p-i, p)) % m
        assert direct == Q
    r = (p-1)//6
    v = pow(10, -1, p)
    V = J = frozen = 0
    for i in range(1, r+1):
        if i > 1:
            s = i-1
            v = v*36*s*s*pow((6*s+5)*(3*s+2), -1, p) % p
        V = (V+v) % p
        J = (J+i*v) % p
        frozen = (frozen+2*arr[i]*((6*i+1)*V-6*J)) % p
    assert R % p == frozen
    digits = lambda x: [(x//p**j) % p for j in range(3)]
    return p, digits(R), digits(D), digits((D-R) % p**3)


def main():
    checked = primes(10000)
    next_digits = []
    for p in checked:
        _, _, W, _ = sums(p, p**4)
        assert (W-p) % p**3 == 0
        next_digits.append(((W-p) % p**4)//p**3)
    assert all(next_digits)  # Finite scan only, not a universal theorem.
    print('TARGET SCAN PASS', len(checked), 'p<=10000; v_p(W-p)=3')
    for p in (13, 19, 37, 43, 181, 373, 1171):
        print('DETAIL', detailed(p))


if __name__ == '__main__':
    main()
