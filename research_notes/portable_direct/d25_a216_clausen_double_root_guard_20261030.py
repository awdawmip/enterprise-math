#!/usr/bin/env python3
"""Exact finite-field regression: A216 Clausen square and quadratic moment jet.
Finite checks are not an all-prime proof or native H0/B0 benchmark.
"""
from math import comb


def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, int(limit ** 0.5) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = b'\x00' * len(range(d*d, limit, d))
    return [p for p in range(7, limit) if sieve[p] and p % 6 == 1]


def check_prime(p):
    m = (p - 1) // 6
    x = pow(2, -1, p)
    # Finite Gauss polynomial: P_m(z) = _2F_1(-m,-2m;1;z) in F_p[z].
    pc = [(comb(m, n) * comb(2*m, n)) % p for n in range(m + 1)]
    square = [0] * (2*m + 1)
    for i, a in enumerate(pc):
        for j, b in enumerate(pc):
            square[i + j] = (square[i + j] + a * b) % p
    # Independent coefficient stream: _3F_2(1/2,1/3,2/3;1,1;z).
    hc = [1]
    for n in range(2*m):
        ratio_num = (2*n + 1) * (3*n + 1) * (3*n + 2)
        ratio_den = 18 * (n + 1)**3
        hc.append(hc[-1] * ratio_num * pow(ratio_den, -1, p) % p)
    assert square == hc, (p, "polynomial Clausen coefficient mismatch")
    pv = sum(a * pow(x, n, p) for n, a in enumerate(pc)) % p
    pd = sum(n * a * pow(x, n - 1, p) for n, a in enumerate(pc) if n) % p
    # Independently accumulate original A216 a_n and n^j a_n, n<p.
    terms = [0, 0, 0]
    term = 1
    for n in range(p):
        for j in range(3):
            terms[j] = (terms[j] + pow(n, j, p)*term) % p
        if n < p-1:
            term = term * (2*n+1)*(3*n+1)*(3*n+2) * pow(36*(n+1)**3, -1, p) % p
    assert terms[0] == pv**2 % p, (p, "S0")
    assert terms[1] == pv*pd % p, (p, "S1")
    if pv == 0:
        assert pd != 0, (p, "simple-root theorem contradicted")
        assert terms[2] == pd*pd*pow(2,-1,p)%p, (p, "S2")
    return (p, m, pv, pd, *terms)


def main():
    ps = primes_below(1500)
    samples = {p:check_prime(p) for p in ps}
    frozen = [p for p in ps if p % 24 in (13,19)]
    assert len(ps) == 115, len(ps)
    assert len(frozen) == 60, len(frozen)
    assert all(samples[p][2] == 0 and samples[p][3] != 0 for p in frozen)
    print("PASS_A216_FINITE_CLAUSEN_COEFFICIENTS_AND_SECOND_JET")
    print("ALL_P_1_MOD_6_UNDER_1500",len(ps),"FROZEN_TARGETS",len(frozen))
    for p in (13,19,373):
        print("p,m,P,Pprime,S0,S1,S2", *samples[p])


if __name__ == "__main__":
    main()
