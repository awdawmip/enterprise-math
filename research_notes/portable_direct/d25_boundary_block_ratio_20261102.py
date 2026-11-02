#!/usr/bin/env python3
"""Exact integer checks for the D25 normalized PF-boundary block quotient.

Only prime-indexed integer modular arithmetic is used. This is an author-side
portable certificate, not native H0/B0 execution or Source admission.
"""

from math import factorial


def primes_through(limit: int):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for a in range(2, int(limit**0.5) + 1):
        if sieve[a]:
            sieve[a * a : limit + 1 : a] = b"\x00" * ((limit - a * a) // a + 1)
    return [p for p in range(5, limit + 1) if sieve[p]]


def normalized_endpoint_units(p: int, mod: int):
    """Compute c_{A,p-1}/p^3, c_{B,p-1}/p^3 modulo `mod`.

    Formulas use original factorial streams with the p-power in each numerator
    stripped exactly; k=p-1 implies n< p^2 for n<=4k (p>=5).
    """
    k = p - 1
    nmax = 4 * k
    marks = {k, 2 * k, 3 * k, 4 * k}
    unit = 1
    fac = {}
    for j in range(1, nmax + 1):
        if j % p:
            unit = unit * j % mod
        if j in marks:
            fac[j] = unit * factorial(j // p) % mod
    a = fac[2 * k] * fac[3 * k] % mod
    a = a * pow(pow(fac[k], 5, mod) * pow(108, k, mod) % mod, -1, mod) % mod
    b = fac[4 * k] * pow(pow(fac[k], 4, mod) * pow(256, k, mod) % mod, -1, mod) % mod
    return a, b


def independent_pochhammer_units(p: int, mod: int):
    """Independent representation using numerator linear-factor products."""
    k = p - 1
    a = b = 1
    pa = pb = 0
    for j in range(k):
        for value in (2 * j + 1, 3 * j + 1, 3 * j + 2):
            if value % p == 0:
                value //= p
                pa += 1
            a = a * value % mod
        for value in (4 * j + 1, 2 * j + 1, 4 * j + 3):
            if value % p == 0:
                value //= p
                pb += 1
            b = b * value % mod
    assert (pa, pb) == (3, 3)
    fk = factorial(k) % mod
    a = a * pow(pow(18, k, mod) * pow(fk, 3, mod) % mod, -1, mod) % mod
    b = b * pow(pow(32, k, mod) * pow(fk, 3, mod) % mod, -1, mod) % mod
    return a, b


def compute_prime(p: int):
    mod = p**4
    ua, ub = normalized_endpoint_units(p, mod)
    assert (ua, ub) == independent_pochhammer_units(p, mod)
    assert ua % p == ub % p == p - 1

    end_a = ((2 * p - 1) * (3 * p - 2) * (3 * p - 1) * pow(18, -1, mod)) % mod
    end_b = ((4 * p - 3) * (2 * p - 1) * (4 * p - 1) * pow(32, -1, mod)) % mod
    ea = (-ua * end_a * pow(2, -p, mod)) % mod
    eb = (-ub * end_b * pow(9, -p, mod)) % mod
    ratio = ea * pow(eb, -1, mod) % mod

    base = (16 * pow(3, -1, mod) * pow(32 * pow(3, -1, mod), p - 1, mod)) % mod
    w1 = w3 = 1
    for j in range(1, p):
        w1 = w1 * (p + j) % mod
        w3 = w3 * (3 * p + j) % mod
    block = w1 * pow(w3, -1, mod) % mod
    assert ratio == base * block % mod

    h2 = sum(pow(j * j, -1, p**2) for j in range(1, p)) % (p**2)
    assert h2 % p == 0
    expected_block = (1 + 5 * p * p * h2) % mod
    assert block == expected_block
    assert ratio % (p**3) == base % (p**3)

    q2 = (pow(2, p - 1) - 1) // p
    q3 = (pow(3, p - 1) - 1) // p
    fifth_digit = ((q3 - 5 * q2) * pow(6, -1, p)) % p
    assert ((3 * ea - 16 * eb) % (p * p)) == p * fifth_digit

    return {
        "p": p,
        "EA_mod_p2": ea % (p**2),
        "EB_mod_p2": eb % (p**2),
        "first_defect_digit": fifth_digit,
        "next_block_digit": ((block - 1) // p**3) % p,
        "harmonic_prediction": (5 * (h2 // p)) % p,
    }


def main():
    tests = primes_through(3000)
    results = [compute_prime(p) for p in tests]
    print("D25 normalized PF-boundary exact block relation / harmonic correction")
    print(f"primes_checked={len(tests)} domain=5<=p<=3000 all prime residues")
    print("independent_representation=factorial_unit_vs_linear_pochhammer: PASS")
    print("exact_block_ratio_mod_p4: PASS")
    print("universal_ratio_mod_p3: PASS")
    print("seventh_digit_harmonic_residual_mod_p4: PASS")
    print("fifth_digit_Fermat_quotient_mod_p2: PASS")
    for v in results:
        if v["p"] in (5, 7, 13, 19, 37, 373, 1171):
            print("certificate:", v)


if __name__ == "__main__":
    main()
