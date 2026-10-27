#!/usr/bin/env python3
"""R45 exact p-adic source-labelled reflected-weight obstruction.

Stdlib integers, modular units and exact Fraction. No native CM/Frobenius
or canonical Source execution claimed.
"""
from fractions import Fraction
from math import isqrt


def primes_6m1(limit=997):
    for p in range(19, limit + 1):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def residue(value: Fraction, modulus: int):
    assert value.denominator % modulus != 0
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def pfree_prefix(p):
    modulus = p * p
    fs = [1] * (4 * p)
    for n in range(1, 4 * p):
        fs[n] = fs[n - 1] * (n // p if n % p == 0 else n) % modulus
    return fs


def regularized_tau(p, k, fs):
    """p^{-e}tau from p-free factorials, valid mod p^2 for k<p."""
    modulus = p * p
    b = 3 * pow(32, -1, modulus) % modulus
    return (pow(b, k, modulus) * fs[k] * fs[4 * k]
            * pow(fs[2 * k] * fs[3 * k] % modulus, -1, modulus)) % modulus


def source_pair_ratio(p, k, fs):
    modulus = p * p
    v = regularized_tau(p, k, fs) * regularized_tau(p, p - k, fs) % modulus
    num = (8 * k + 1) * (8 * (p - k) + 1)
    den = (6 * k + 1) * (6 * (p - k) + 1)
    assert den % p
    return v * num * pow(den, -1, modulus) % modulus


def direct_fraction_pair_ratio(p, k):
    """Independent original w/s exact-Q values for small primes."""
    from math import factorial

    def w(i):
        return Fraction((6 * i + 1) * factorial(2 * i) * factorial(3 * i),
                        factorial(i)**5 * 216**i)

    def s(i):
        return Fraction((8 * i + 1) * factorial(4 * i),
                        factorial(i)**4 * 2304**i)

    return s(k) * s(p - k) / (w(k) * w(p - k))


def check():
    nprimes = instances = raw = 0
    samples = []
    lo1, lo2 = Fraction(27, 80), Fraction(765, 2288)
    assert lo1 - lo2 == Fraction(9, 2860)
    for p in primes_6m1():
        fs = pfree_prefix(p)
        p2 = p * p
        b = 3 * pow(32, -1, p2) % p2
        qp = (pow(b, p - 1, p2) - 1) // p
        qp2 = ((pow(3, p - 1, p2) - 1) // p
               - 5 * ((pow(2, p - 1, p2) - 1) // p)) % p
        assert qp == qp2
        out = []
        for k, base, jet in ((1, lo1, Fraction(187, 210)),
                             (2, lo2, Fraction(267, 308))):
            actual = source_pair_ratio(p, k, fs)
            expected = residue(base, p2) * (1 + p * (qp + residue(jet, p2))) % p2
            assert actual == expected, (p, k, actual, expected)
            assert actual % p == residue(base, p)
            if p <= 43:
                exact = direct_fraction_pair_ratio(p, k)
                assert residue(exact, p2) == actual
                raw += 1
            out.append(actual)
            instances += 1
        assert (out[0] - out[1]) % p == residue(Fraction(9, 2860), p)
        assert out[0] % p != out[1] % p
        if p in (19, 31, 37, 181, 373, 733, 997):
            samples.append((p, out[0], out[1], (out[0] - out[1]) % p))
        nprimes += 1

    print(f"R45 PASS: {nprimes} primes p≡1 (mod 6), 19≤p≤997; "
          f"{instances} reflected pair jet checks; {raw} independent raw Fraction checks")
    print("Examples (p, E1 mod p², E2 mod p², difference mod p):")
    for row in samples:
        print(" ", row)


if __name__ == "__main__":
    check()
