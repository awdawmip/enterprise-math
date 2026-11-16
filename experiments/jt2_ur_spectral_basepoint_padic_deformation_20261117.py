#!/usr/bin/env python3
"""Exact finite crosscheck of the JT2 spectral basepoint p-adic deformation.

Scope: all p<=2000 with p % 6 == 1 for the coefficientwise theorem;
CM-port quotient for p % 24 in (13, 19); direct norm convolution for
the 15 CM-class primes p<=300. No external packages, no floating point.
Tests are evidence for the separate general algebraic proof, not a
universal verification of the open UR vanishing conjecture.
"""
from math import comb


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for a in range(2, int(n**0.5) + 1):
        if sieve[a]:
            for k in range(a * a, n + 1, a):
                sieve[k] = False
    return [a for a, ok in enumerate(sieve) if ok]


def inv(a, modulus):
    return pow(a % modulus, -1, modulus)


def verify_prime(p):
    m = (p - 1) // 6
    mod = p * p
    c0 = ((-1) ** m * comb(2 * m, m) * inv(4**m, mod)) % mod
    # c_j = [Y^j] Q_m(Y); f_j = [Y^j] H_m(-1/9,Y)
    c, f, T = [c0], [1], [0]
    for j in range(m):
        c.append(c[-1] * (j - m) * (2 * m + 2 * j + 1)
                 * inv((j + 1) * (2 * j + 1), mod) % mod)
        f.append(f[-1] * (6 * j + 1) * (3 * j + 1)
                 * inv(9 * (2 * j + 1) * (j + 1), mod) % mod)
        T.append((T[-1] + inv((m - j) * (2 * m + 2 * j + 1), p)) % p)

    # D holds coefficientwise in Z_(p)[Y]/p^2.
    pinv18 = p * inv(18, mod)
    for j in range(m + 1):
        assert (c[j] - c0 * f[j] - pinv18 * c[j] * T[j]) % mod == 0, (p, j)

    half_mod = inv(2, mod)
    q = sum(c[j] * pow(half_mod, j, mod) for j in range(m + 1)) % mod
    fhalf = sum(f[j] * pow(half_mod, j, mod) for j in range(m + 1)) % mod
    z = sum(c[j] * T[j] * pow(half_mod, j, mod)
            for j in range(m + 1)) % p
    assert (q - c0 * fhalf - pinv18 * z) % mod == 0, p

    if p % 24 not in (13, 19):
        return False, False

    # The inherited CM0 premise is independently checked here for
    # the finite sample; it is not assumed in a symbolic proof.
    assert q % p == 0 and fhalf % p == 0, p
    u = q // p
    v = fhalf // p
    assert (u - c0 * v - z * inv(18, p)) % p == 0, p

    if p > 300:
        return True, False

    # Independent quadratic convolution (rather than the spectral
    # reduction) for the small-sample original norm integral.
    d = sum(j * c[j] * pow(half_mod, j - 1, mod)
            for j in range(1, m + 1)) % p
    s = sum(c[j] * pow(2, -(m + j), p) * inv(2 * m + 2 * j + 1, p)
            for j in range(m + 1)) % p
    norm = sum(c[i] * c[j] * pow(2, -(i + j), p)
               * inv(2 * (i + j) + 1, p)
               for i in range(m + 1) for j in range(m + 1)) % p
    old_residual = (18 * u * d - 2 * norm - 3) % p
    new_residual = (18 * c0 * v * d - 2 * c[-1] * s - 3) % p
    assert old_residual == new_residual == 0, (p, old_residual, new_residual)
    return True, True


def main():
    tested = cm = norm_tests = 0
    for p in primes_up_to(2000):
        if p % 6 != 1:
            continue
        tested += 1
        in_cm, ran_norm = verify_prime(p)
        cm += int(in_cm)
        norm_tests += int(ran_norm)
    assert (tested, cm, norm_tests) == (148, 77, 15)
    print(f"PASS: coefficientwise={tested}; CM quotient={cm}; "
          f"independent norm/residual={norm_tests}")


if __name__ == "__main__":
    main()
