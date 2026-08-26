#!/usr/bin/env python3
"""Exact checker for the odd-sector central-fiber saturation theorem."""

from __future__ import annotations

from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def legendre(a: int, q: int) -> int:
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def packet_value(s: int, j: int, m: int) -> int:
    return 2 * s * m * m + 2 * j * m + 1


def root_union(s: int, q: int) -> set[int]:
    h = (s - 1) // 2
    out: set[int] = set()
    for j in range(-h, h + 1):
        for m in range(q):
            if packet_value(s, j, m) % q == 0:
                out.add(m)
    return out


def omega_formula(s: int, q: int) -> int:
    h = (s - 1) // 2
    return s + sum(legendre(j * j - 2 * s, q) for j in range(-h, h + 1))


def saturated_primes(s: int) -> list[int]:
    out = []
    for q in range(3, 2 * s + 2):
        if not is_prime(q):
            continue
        if root_union(s, q) == set(range(1, q)):
            out.append(q)
    return out


def main() -> None:
    # Automatic saturation for every odd prime q<=s.
    for s in range(1, 40, 2):
        for q in range(3, s + 1):
            if is_prime(q):
                assert root_union(s, q) == set(range(1, q)), (s, q)

    # For q>s with q not dividing 2s, roots are lane-disjoint and omega formula is exact.
    for s in range(1, 30, 2):
        h = (s - 1) // 2
        for q in range(s + 1, 2 * s + 2):
            if not is_prime(q) or (2 * s) % q == 0:
                continue
            lane_roots = []
            for j in range(-h, h + 1):
                roots = {m for m in range(q) if packet_value(s, j, m) % q == 0}
                lane_roots.append(roots)
            for i in range(len(lane_roots)):
                for j in range(i + 1, len(lane_roots)):
                    assert not (lane_roots[i] & lane_roots[j])
            union = set().union(*lane_roots)
            assert len(union) == omega_formula(s, q), (s, q, len(union), omega_formula(s, q))

    # No q>2s+1 can saturate by root-slot count. Pressure check a finite range.
    for s in range(1, 20, 2):
        for q in range(2 * s + 2, 5 * s + 20):
            if is_prime(q):
                assert root_union(s, q) != set(range(1, q)), (s, q)

    expected = {
        1: [3],
        3: [3, 5, 7],
        5: [3, 5, 7],
        7: [3, 5, 7],
        9: [3, 5, 7, 11, 13],
        11: [3, 5, 7, 11],
        13: [3, 5, 7, 11, 13],
    }
    for s, exp in expected.items():
        assert saturated_primes(s) == exp, (s, saturated_primes(s), exp)

    # Native s=3 root profile.
    s = 3
    for q in (5, 7, 11, 13, 17, 19):
        if q > s:
            assert len(root_union(s, q)) == omega_formula(s, q)
    assert saturated_primes(3) == [3, 5, 7]
    assert 3 * 5 * 7 == 105

    print("AUTOMATIC_PRIMORIAL_CORE_Q_LE_S=PASS")
    print("LARGE_PRIME_OMEGA_PROFILE=PASS")
    print("NO_SATURATION_ABOVE_2S_PLUS_1=PASS")
    print("SMALL_S_GATE_TABLE=PASS")
    print("NATIVE_S3_GATE_105=PASS")


if __name__ == "__main__":
    main()
