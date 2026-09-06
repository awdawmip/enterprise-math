#!/usr/bin/env python3
"""
Independent salvage verifier for enterprise-math PR #1330.

Scope:
- exact checks for RSA-270 residue fibers;
- corrected local-modulus theorem boundary;
- exact mod-72 linear-coordinate image law;
- profile moment and odd-multiplier profile identities;
- V/multiplier-Fermat certificates;
- counterexample to the claimed simple 3-adic "one bit per digit" law;
- demonstration that the 62-point torsion check is a formal identity and is
  not candidate-discriminating without independently observed torsion data.

This is a research verification checkpoint, not a factorization program.
"""

from __future__ import annotations

import cmath
import math
from math import gcd, isqrt, lcm

RSA270 = int(
    "2331085303444075445276376569106805241456198124803054490429486119684959182451"
    "3578286788836931857711641821391926857265831491306067262691135402760979316634"
    "1626693946596196427744273886601876896313468704059066746903123910748277606548"
    "649151920812699309766587514735456594993207"
)


def units(m: int):
    return [a for a in range(m) if gcd(a, m) == 1]


def admissible_sums(N: int, m: int, branch: str | None = None):
    """
    Local factor-residue model:
      a*b = N (mod L), L=lcm(m,6);
    optional branch H1: a,b=1 mod3; H2: a,b=2 mod3.
    Return induced S=a+b (mod m).
    """
    L = lcm(m, 6)
    out = set()
    for a in units(L):
        b = (N * pow(a, -1, L)) % L
        if branch == "H1" and not (a % 3 == 1 and b % 3 == 1):
            continue
        if branch == "H2" and not (a % 3 == 2 and b % 3 == 2):
            continue
        out.add((a + b) % m)
    return sorted(out)


def divisors(n: int):
    ds = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)


def profile_coeffs_semiprime(p: int, q: int):
    N = p * q
    S = p + q
    a = (N + 3) // 2
    b = (S + 2) // 2
    coeff = {}
    for s in (a, a, b, b):
        for j in range(s - 1):
            e = 2 - s + 2 * j
            coeff[e] = coeff.get(e, 0) + 1
    return coeff


def profile_indices(T: int):
    return sorted((d + T // d + 2) // 2 for d in divisors(T))


def predicted_multiplier_indices(k: int, p: int, q: int):
    """Odd k, gcd(k,pq)=1: exact divisor-pair decomposition, with multiplicity."""
    N = p * q
    out = []
    for a in divisors(k):
        b = k // a
        out.extend([(a + b * N + 2) // 2] * 2)
        out.extend([(a * p + b * q + 2) // 2] * 2)
    return sorted(out)


def pair_and_sum_counts_prime_power(N: int, prime: int, t: int, branch_mod3=None):
    m = prime**t
    sums = set()
    count = 0
    for a in units(m):
        b = (N * pow(a, -1, m)) % m
        if branch_mod3 is not None:
            if a % 3 != branch_mod3 or b % 3 != branch_mod3:
                continue
        count += 1
        sums.add((a + b) % m)
    return count, len(sums)


def torsion_formal_check(N: int, S: int, mmax: int = 64, tol: float = 1e-7):
    """
    Compare two algebraically equivalent presentations of the same formal profile.
    Passing this check does NOT show that S factors N.
    """
    assert N % 2 == 1 and S % 2 == 0
    for m in range(3, mmax + 1):
        w = cmath.exp(2j * math.pi / m)
        r0 = ((N + 3) // 2) % m
        r1 = ((S + 2) // 2) % m

        def g(r: int):
            th = 2 * math.pi / m
            return math.sin(((r - 1) % m) * th) / math.sin(th)

        e1 = ((S - N - 1) // 2) % m
        B = (w**e1) * (1 - w ** ((N + 1) % m)) + (1 - w ** (S % m))
        lhs = 2 * (w ** (((2 - S) // 2) % m)) * B / (1 - w * w)
        rhs = 2 * g(r0) + 2 * g(r1)
        if abs(lhs - rhs) > tol:
            return False
    return True


def main():
    expected_residues = {
        3: 1, 6: 1, 8: 7, 9: 1, 16: 7, 18: 1,
        24: 7, 27: 19, 36: 19, 72: 55, 144: 55,
    }
    assert {m: RSA270 % m for m in expected_residues} == expected_residues
    assert admissible_sums(RSA270, 72, None) == [16, 56]
    assert admissible_sums(RSA270, 72, "H2") == [16]
    assert admissible_sums(RSA270, 72, "H1") == [56]
    assert admissible_sums(RSA270, 144, "H2") == [16, 88]
    assert admissible_sums(RSA270, 144, "H1") == [56, 128]

    assert admissible_sums(RSA270, 8, "H2") == [0]
    assert len(admissible_sums(RSA270, 16, "H2")) == 2
    assert admissible_sums(RSA270, 9, "H2") == [7]
    assert len(admissible_sums(RSA270, 27, "H2")) == 2
    for r in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        if RSA270 % r == 0:
            continue
        image = {(a + (RSA270 % r) * pow(a, -1, r)) % r for a in range(1, r)}
        assert len(image) >= 2

    F = {
        (a, (RSA270 * pow(a, -1, 72)) % 72)
        for a in units(72)
        if a % 6 == 5 and ((RSA270 * pow(a, -1, 72)) % 72) % 6 == 5
    }
    parameterized = {((5 + 6 * k) % 72, (11 - 6 * k) % 72) for k in range(12)}
    assert F == parameterized and len(F) == 12
    assert {((q - p) % 72) for p, q in F} == {6, 18, 30, 42, 54, 66}
    for a in range(72):
        for b in range(72):
            image = {(a * p + b * q) % 72 for p, q in F}
            assert len(image) == 12 // gcd(12, a - b)

    for p, q in ((5, 7), (11, 13), (17, 23), (29, 31), (59, 61)):
        N, S = p * q, p + q
        P = profile_coeffs_semiprime(p, q)
        for r in range(1, 7):
            observed = sum(c**r for c in P.values())
            predicted = 2 ** (r - 1) * ((N + 1) + (2**r - 1) * S)
            assert observed == predicted

    for p, q in ((5, 7), (11, 13), (17, 23)):
        N = p * q
        for k in (3, 5, 9, 15, 25, 35):
            if k % 2 == 1 and gcd(k, N) == 1:
                assert profile_indices(k * N) == predicted_multiplier_indices(k, p, q)
                for a in divisors(k):
                    b = k // a
                    La = (a * p + b * q - 2) // 2
                    Lb = (b * p + a * q - 2) // 2
                    assert La + Lb == ((a + b) * (p + q) - 4) // 2
                    assert La - Lb == (a - b) * (p - q) // 2

    for p, q in ((5, 7), (11, 13), (17, 23), (29, 31)):
        N = p * q
        for ell in (2, 3, 5, 7, 11, 13):
            x = ell * p + q
            y = abs(ell * p - q)
            assert x * x - 4 * ell * N == y * y
            assert {x + y, x - y} == {2 * ell * p, 2 * q}
        for l1, l2 in ((2, 3), (3, 5), (5, 11)):
            x1, x2 = l1 * p + q, l2 * p + q
            assert (x1 - x2) * (l1 * x2 - l2 * x1) == (l1 - l2) ** 2 * N

    observed_3adic = [
        pair_and_sum_counts_prime_power(RSA270, 3, t, branch_mod3=2)
        for t in range(1, 8)
    ]
    assert observed_3adic == [
        (1, 1), (3, 1), (9, 2), (27, 4), (81, 11), (243, 31), (729, 92)
    ]
    assert observed_3adic[4][1] == 11

    wrong_candidates = ((35, 100), (35, 156), (143, 168), (391, 184), (899, 204))
    for N, S in wrong_candidates:
        A = S // 2
        discriminant_square = (isqrt(A * A - N) ** 2 == A * A - N) if A * A >= N else False
        assert not discriminant_square
        assert torsion_formal_check(N, S)

    print("PASS: corrected RSA-270 residue branches")
    print("PASS: local H2 mod-72 maximality boundary checks")
    print("PASS: mod-72 factor-fiber parameterization and |image|=12/gcd(12,a-b)")
    print("PASS: profile moment law r=1..6")
    print("PASS: odd composite-multiplier profile decomposition")
    print("PASS: V/multiplier-Fermat and Pluecker identities")
    print("PASS: 3-adic simple-doubling claim falsified at 3^5 (11 S-classes)")
    print("PASS: torsion formal identity accepts deliberately wrong S candidates")
    print("No RSA-270 factor obtained.")


if __name__ == "__main__":
    main()
