#!/usr/bin/env python3
"""Independent blind checker for RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION.

This script is reconstructed only from the frozen statement packet
NATIVE_FILAMENT_POSTAUDIT_HYPERBOLA_JOUKOWSKI_BLIND_PACKET_20260825.md.
It intentionally does not import repository theorem/checker code.
"""
from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def primes_upto(n: int):
    return [p for p in range(2, n + 1) if is_prime(p)]


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    z = pow(a, (p - 1) // 2, p)
    assert z in (1, p - 1)
    return 1 if z == 1 else -1


def inv(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def lam(s: int, a: int, p: int) -> int:
    return (-s * a - inv(2 * a, p)) % p


def h1_pressure():
    checks = 0
    for p in (5, 7, 13):
        for B in range(1, p):
            for d0 in range(p):
                for d1 in range(p):
                    if d0 == d1:
                        continue
                    ds = (d0, d1)
                    for i in (0, 1):
                        C = 2 * (ds[i] - ds[1 - i]) % p
                        for u in range(p):
                            for v in range(p):
                                if u == v:
                                    continue
                                x = (-B * (u + v) * inv(2, p)) % p
                                y = (B * u * v * inv(2, p) - ds[i]) % p
                                for w in range(p):
                                    on_third = (
                                        y
                                        + w * x
                                        + B * w * w * inv(2, p)
                                        + ds[1 - i]
                                    ) % p == 0
                                    hyper = B * (w - u) * (w - v) % p == C
                                    assert on_third == hyper
                                    checks += 1

    for p in (5, 7, 13):
        for B in range(1, p):
            for C in range(1, p):
                for x in range(p):
                    for y in range(p):
                        in_R = B * (y * y - x * x) % p == C
                        a, b = (y - x) % p, (y + x) % p
                        in_H = B * a * b % p == C
                        assert in_R == in_H
                        xx = (b - a) * inv(2, p) % p
                        yy = (a + b) * inv(2, p) % p
                        assert (xx, yy) == (x, y)

    p, B, C = 5, 1, 1
    H = {(a, b) for a in range(p) for b in range(p) if B * a * b % p == C}
    diag = {(a, b) for (a, b) in H if a == b}
    assert diag == {(1, 1), (4, 4)}
    assert len(H - diag) == 2
    return checks, sorted(diag)


def orbit_count_R(p: int, B: int, C: int):
    R = {
        (x, y)
        for x in range(p)
        for y in range(p)
        if B * (y * y - x * x) % p == C % p
    }
    seen = set()
    orbits = 0
    for x, y in R:
        if (x, y) in seen:
            continue
        orb = {
            (sx * x % p, sy * y % p)
            for sx in (1, -1)
            for sy in (1, -1)
        }
        orb &= R
        seen |= orb
        orbits += 1
    return len(R), orbits


def h2_pressure():
    log = {}
    for p in (5, 7, 13, 53):
        rows = set()
        for C in range(1, p):
            B = 1
            nR, nO = orbit_count_R(p, B, C)
            formula = (p + 1 + chi(B * C, p) + chi(-B * C, p)) // 4
            assert nR == p - 1
            assert nO == formula
            rows.add((chi(B * C, p), chi(-B * C, p), nO))
        for B in range(1, min(p, 8)):
            for C in range(1, min(p, 8)):
                nR, nO = orbit_count_R(p, B, C)
                formula = (p + 1 + chi(B * C, p) + chi(-B * C, p)) // 4
                assert nR == p - 1 and nO == formula
        log[p] = sorted(rows)
    for p in primes_upto(101):
        if p % 2 == 0:
            continue
        if p - 1 > 4:
            assert (p - 1 + 3) // 4 > 1
    return log


def j1_pressure():
    cases = 0
    for s in range(3, 16, 2):
        J = {j for j in range(-(s - 1) // 2, (s - 1) // 2 + 1)}
        for p in primes_upto(101):
            if p == 2 or (2 * s) % p == 0:
                continue
            image = {lam(s, a, p) for a in range(1, p)}
            c = inv(2 * s, p)
            expected = (p + chi(c, p)) // 2
            assert len(image) == expected
            Jmod = {j % p for j in J}
            saturation = all(lam(s, a, p) in Jmod for a in range(1, p))
            assert saturation == image.issubset(Jmod)
            cases += 1

    s, p = 5, 5
    image = {lam(s, a, p) for a in range(1, p)}
    assert len(image) == p - 1
    return cases


def j2_pressure():
    lower = []
    upper = []
    for s in range(3, 102, 2):
        q = 2 * s - 1
        if is_prime(q):
            J = {j % q for j in range(-(s - 1) // 2, (s - 1) // 2 + 1)}
            sat = {lam(s, a, q) for a in range(1, q)}.issubset(J)
            lower.append((s, q, sat))
        q = 2 * s + 1
        if is_prime(q):
            J = {j % q for j in range(-(s - 1) // 2, (s - 1) // 2 + 1)}
            sat = {lam(s, a, q) for a in range(1, q)}.issubset(J)
            upper.append((s, q, sat))
    assert [(s, q) for s, q, sat in lower if sat] == [(3, 5)]
    assert [(s, q) for s, q, sat in upper if sat] == [(3, 7)]
    for s, q, sat in lower:
        if sat:
            assert 25 % q == 0
    for s, q, sat in upper:
        if sat:
            assert 7 % q == 0
    return lower, upper


def c1_c2_pressure():
    solutions = []
    for qb in (3, 5):
        k = 2 * qb - 1
        for s in range(3, 20, 2):
            if k - 4 == 2 * s - 1 and k - 2 == 2 * s + 1:
                solutions.append((s, qb, k))
    assert solutions == [(3, 5, 9)]
    M9 = (9 - 4) * (9 - 2)
    assert M9 == 35
    assert 3 * M9 == 105
    assert 3 * M9 + 1 == 106 == 2 * 53

    for m in range(-20, 21):
        vals = [2 * 3 * m * m + 2 * j * m + 1 for j in (-1, 0, 1)]
        assert vals == [
            6 * m * m - 2 * m + 1,
            6 * m * m + 1,
            6 * m * m + 2 * m + 1,
        ]
    return solutions


def main():
    h1_checks, h1_diag = h1_pressure()
    h2 = h2_pressure()
    j1_cases = j1_pressure()
    lower, upper = j2_pressure()
    c1 = c1_c2_pressure()
    print("PASS independent blind checker")
    print(f"H1a exhaustive representative checks: {h1_checks}")
    print(f"H1 distinct-tangent diagonal omission witness F5: {h1_diag}")
    print(f"H2 orbit classes: {h2}")
    print(f"J1 image-size/saturation cases: {j1_cases}")
    print(
        f"J2 lower prime cases: {len(lower)}; "
        f"saturating: {[(s, q) for s, q, z in lower if z]}"
    )
    print(
        f"J2 upper prime cases: {len(upper)}; "
        f"saturating: {[(s, q) for s, q, z in upper if z]}"
    )
    print(f"C1 solutions under odd qb<=5 and odd s>=3: {c1}")
    print(
        "Boundary guards: q=2 excluded; q|s excluded from J1b inverse; "
        "nonprime extremals excluded by J2 hypotheses."
    )


if __name__ == "__main__":
    main()
