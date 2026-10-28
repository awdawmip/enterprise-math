#!/usr/bin/env python3
"""Exact finite-field verification of author lemmas GH-55 through GH-57.

This script runs ordinary Python arithmetic, not any Enterprise Math native
experiment, Source CLAIM, formal proof checker, or independent review.
"""
from math import comb, factorial


def primes_below(limit):
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"
    for d in range(2, int(limit ** 0.5) + 1):
        if sieve[d]:
            sieve[d * d:limit:d] = b"\x00" * (((limit - 1 - d * d) // d) + 1)
    return [p for p in range(11, limit) if sieve[p] and p % 8 == 3]


def f_coefficients(p):
    m = (p - 3) // 8
    out = [1]
    for r in range(m):
        # (-m)_{r+1}^2 / ((2m+2)_{r+1} (r+1)!)
        num = ((m - r) ** 2) % p
        den = ((2 * m + 2 + r) * (r + 1)) % p
        assert den, (p, r)
        out.append(out[-1] * num * pow(den, -1, p) % p)
    return out


def legendre_polynomial_in_z(p, m):
    """z^m P_{2m}(sqrt((z-1)/z)), from a Q-polynomial identity."""
    coef = [0] * (m + 1)
    q = -pow(4, -1, p)
    for k in range(m + 1):
        weight = comb(2 * m, 2 * k) * comb(2 * k, k) * pow(q, k, p) % p
        d = m - k
        for j in range(d + 1):
            coef[j] = (coef[j] + weight * comb(d, j) * (-1 if (d-j) % 2 else 1)) % p
    return coef


def legendre_even_value_and_t_derivative(p, m, t_squared):
    """Return P_{2m}(t) and t P'_{2m}(t) in F_p from even coefficients."""
    facts = [1]
    for k in range(1, 4 * m + 1):
        facts.append(facts[-1] * k % p)
    leading_denom = pow(4, m, p)
    P = 0
    tP = 0
    for j in range(m + 1):
        denom = (leading_denom * facts[m-j] * facts[m+j] * facts[2*j]) % p
        assert denom != 0
        c = facts[2*m+2*j] * pow(denom, -1, p) % p
        if (m-j) % 2:
            c = (-c) % p
        monomial = c * pow(t_squared, j, p) % p
        P = (P + monomial) % p
        tP = (tP + 2 * j * monomial) % p
    return P, tP


def check_prime(p, full_coefficients=False):
    m = (p - 3) // 8
    assert 8*m+3 == p
    fc = f_coefficients(p)
    D = comb(3*m+1, m) % p
    assert D != 0
    if full_coefficients:
        H = legendre_polynomial_in_z(p, m)
        assert H[-1] == 1, (p, "monic")
        assert H == [(D * c) % p for c in fc], (p, "polynomial")
        for z in (0, 1, 2, 9, p-1):
            assert sum(H[r] * pow(z, r, p) for r in range(m+1)) % p == \
                   D * sum(fc[r] * pow(z, r, p) for r in range(m+1)) % p

    z = 9 % p
    F = sum(fc[r] * pow(z, r, p) for r in range(m+1)) % p
    G = sum((16*r+5) * fc[r] * pow(z, r, p) for r in range(m+1)) % p
    G_prime = sum(r * (16*r+5) * fc[r] * pow(z, r-1, p) for r in range(1, m+1)) % p
    G_second = sum(r * (r-1) * (16*r+5) * fc[r] * pow(z, r-2, p)
                   for r in range(2, m+1)) % p
    F_prime = sum(r * fc[r] * pow(z, r-1, p) for r in range(1, m+1)) % p
    F_second = sum(r * (r-1) * fc[r] * pow(z, r-2, p)
                   for r in range(2, m+1)) % p
    H_prime = (F_prime * G + F * G_prime) % p
    H_second = (F_second * G + 2 * F_prime * G_prime + F * G_second) % p
    # GH-57: exact conditional port-discriminating second jets.
    if F == 0:
        assert (16 * H_second + 5 * H_prime) % p == 0, (p, "F-port jet")
    if G == 0:
        assert (48 * H_second + 7 * H_prime) % p == 0, (p, "G-port jet")
    if F == 0 or G == 0:
        assert H_prime != 0, (p, "simple port zero")
    assert (288 * G_prime + 16 * G + F) % p == 0, (p, "local_jet")

    t_sq = 8 * pow(9, -1, p) % p
    P, tP = legendre_even_value_and_t_derivative(p, m, t_sq)
    assert (D * F - pow(9, m, p) * P) % p == 0, (p, "F Legendre")
    assert (D * G - pow(9, m, p) * (tP - P)) % p == 0, (p, "G derivative")
    if G == 0:
        assert (288 * G_prime + F) % p == 0
    if F == 0:
        assert (18 * G_prime + G) % p == 0
    return (p, m, F, G, G_prime, P, tP)


def main():
    smaller = primes_below(2000)
    larger = primes_below(10000)
    for p in smaller:
        check_prime(p, full_coefficients=True)
    samples = [check_prime(p) for p in larger]
    split11 = [v for v in samples if v[0] % 24 == 11]
    inert19 = [v for v in samples if v[0] % 24 == 19]
    assert all(v[2] != 0 and v[3] == 0 for v in split11)
    assert all(v[2] == 0 and v[3] != 0 for v in inert19)
    print(f"PASS_GH55_UNIFORM_LEGENDRE_COEFFICIENTS {len(smaller)} primes p<2000")
    print(f"PASS_GH55_F_G_LEGENDRE_SPECIAL_VALUES {len(larger)} primes p<10000")
    print(f"PASS_GH56_LOCAL_PICARD_FUCHS_JET {len(larger)} primes p<10000")
    print(f"PASS_GH57_CHANNEL_TYPED_SECOND_JET {len(larger)} observed root cases p<10000")
    print(f"OBSERVATION_ONLY_CLASS11_G_ZERO {len(split11)}/{len(split11)}")
    print(f"OBSERVATION_ONLY_CLASS19_F_ZERO {len(inert19)}/{len(inert19)}")
    print("WITNESSES(p,m,F,G,Gprime,P,tP):", [v for v in samples if v[0] in (11,19,43,59,67,83)])


if __name__ == "__main__":
    main()
