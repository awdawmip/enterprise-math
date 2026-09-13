#!/usr/bin/env python3
"""
Verification for the odd-prime-power character BRC atlas.

Checks:
1. primitive-character normalized profile projector for l=3,5,7,11;
2. exactly l product-compatible lifts per l-adic level;
3. mixed-radix RSA-270 Coppersmith cutoff depths.

Researcher-ID: EM-DIRECT-66DE45
No RSA factor is used or produced.
"""
import cmath
import math
import random


def divisors(n):
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
        d += 1
    return sorted(out)


def prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root_prime_power(l, e):
    m = l ** e
    phi = (l - 1) * l ** (e - 1)
    pf = prime_factors(phi)
    for g in range(2, m):
        if math.gcd(g, m) == 1 and all(pow(g, phi // q, m) != 1 for q in pf):
            return g
    raise AssertionError("primitive root not found")


def character(l, e):
    m = l ** e
    phi = (l - 1) * l ** (e - 1)
    gen = primitive_root_prime_power(l, e)
    dlog = {}
    x = 1
    for j in range(phi):
        dlog[x] = j
        x = (x * gen) % m
    assert len(dlog) == phi

    xi = cmath.exp(2j * math.pi / phi)

    def chi(a):
        r = a % m
        if math.gcd(r, m) != 1:
            return 0j
        return xi ** dlog[r]

    return m, gen, chi


def projector_case(n, l, e):
    m, _, chi = character(l, e)
    T = m * n

    # Apply Pi_chi to D(zeta) P_T(zeta) using the monomial projector lemma.
    lhs = 0j
    for d in divisors(T):
        comp = T // d
        assert (d + comp) % 2 == 0
        t = ((d + comp) // 2) % m
        lhs += 0.5 * (chi(t) - chi(-t))

    A = sum(chi(d) for d in divisors(n))
    rhs = 2 * A / chi(2)
    assert abs(lhs - rhs) < 1e-8, (n, l, e, lhs, rhs)


def check_projector():
    ns = [5, 7, 11, 25, 35, 55, 77, 105]
    count = 0
    for l in (3, 5, 7, 11):
        for e in (1, 2, 3):
            for n in ns:
                projector_case(n, l, e)
                count += 1
    assert count == 96
    return count


def check_lift_counts():
    rng = random.Random(20260908)
    count = 0
    for l in (3, 5, 7, 11):
        for e in (2, 3, 4):
            n = l ** (e - 1)
            m = l ** e
            for _ in range(100):
                p0 = rng.randrange(1, n)
                while p0 % l == 0:
                    p0 = rng.randrange(1, n)
                q0 = rng.randrange(1, n)
                while q0 % l == 0:
                    q0 = rng.randrange(1, n)

                ip = rng.randrange(l)
                iq = rng.randrange(l)
                p = p0 + ip * n
                q = q0 + iq * n
                N = p * q

                solutions = []
                for i in range(l):
                    for j in range(l):
                        if ((p0 + i * n) * (q0 + j * n) - N) % m == 0:
                            solutions.append((i, j))

                assert len(solutions) == l, (l, e, p0, q0, len(solutions))
                count += 1
    return count


RSA270 = int(
    "2331085303444075445276376569106805241456198124803054490429486119684959182451"
    "3578286788836931857711641821391926857265831491306067262691135402760979316634"
    "1626693946596196427744273886601876896313468704059066746903123910748277606548"
    "649151920812699309766587514735456594993207"
)


def equal_depth_cutoff(primes):
    base = math.prod(primes)
    E = 0
    while (2 * base ** E) ** 4 <= RSA270:
        E += 1
    assert E == 0 or (2 * base ** (E - 1)) ** 4 <= RSA270
    return E, math.log2(2 * base ** E)


def check_cutoffs():
    expected = {
        (3,): 141,
        (3, 5): 58,
        (3, 5, 7): 34,
        (3, 5, 7, 11): 22,
    }
    out = {}
    for primes, E_expected in expected.items():
        E, bits = equal_depth_cutoff(primes)
        assert E == E_expected, (primes, E, E_expected)
        out[primes] = (E, bits, 2 ** len(primes))
    return out


def check_cartier_digits():
    for l in (3, 5, 7, 11):
        h = (l - 1) // 2
        for e in range(1, 6):
            c = (l ** e - 1) // 2
            digits = []
            x = c
            for _ in range(e):
                digits.append(x % l)
                x //= l
            assert digits == [h] * e
            assert x == 0


def main():
    print("projector cases:", check_projector(), "PASS")
    print("l-adic lift states:", check_lift_counts(), "PASS")
    check_cartier_digits()
    print("Cartier repeated middle-digit identity: PASS")
    cuts = check_cutoffs()
    for primes, row in cuts.items():
        print(primes, row)
    print("ALL PASS")


if __name__ == "__main__":
    main()
