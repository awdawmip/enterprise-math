#!/usr/bin/env python3
"""
Independent exact-integer audit for
RS-PRIME-FUSION-T4-T7-T8-FINAL-EXACT-CLOSURE.

No source checker or withheld proof is used.

Audit ranges:
  * T4 SNF/cyclicity: 0 <= a,b <= 64, (a,b)!=(0,0)
  * T4 pointed compatibility: 1 <= a,b <= 64, gcd(a,b)=1
  * T4 explicit kernel equivalence: 1 <= a,b <= 12, gcd(a,b)=1,
    -16 <= x,y <= 16
  * T7 all idempotents: 1 <= H <= 1000
  * T7 cell witness table: positive primitive 1 <= a,b <= 40, H<=1000
  * T8 positive cells: 1 <= a,b <= 100
"""

from math import gcd, isqrt

T4_CELL_MAX = 64
T4_KERNEL_CELL_MAX = 12
T4_KERNEL_XY = 16
T7_H_MAX = 1000
T7_CELL_MAX = 40
T8_CELL_MAX = 100


def n_channel(a: int, b: int) -> int:
    return a * a + b * b


def c_channel(a: int, b: int) -> int:
    return a * a - a * b + b * b


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def factorization(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def is_squarefree_semiprime(n: int) -> bool:
    fac = factorization(n)
    return len(fac) == 2 and all(exp == 1 for exp in fac.values())


def gaussian_snf(a: int, b: int) -> tuple[int, int]:
    # Multiplication by a+b*i on basis (1,i):
    # [[a,-b],[b,a]], determinant N.
    d1 = gcd(abs(a), abs(b))
    det = n_channel(a, b)
    assert d1 > 0 and det % d1 == 0
    d2 = det // d1
    assert d2 % d1 == 0
    return d1, d2


def eisenstein_snf(a: int, b: int) -> tuple[int, int]:
    # Multiplication by a+b*w on basis (1,w), w^2+w+1=0:
    # [[a,-b],[b,a-b]], determinant C.
    d1 = gcd(gcd(abs(a), abs(b)), abs(a - b))
    det = c_channel(a, b)
    assert d1 > 0 and det % d1 == 0
    d2 = det // d1
    assert d2 % d1 == 0
    return d1, d2


def gaussian_ideal_contains(a: int, b: int, x: int, y: int) -> bool:
    n = n_channel(a, b)
    return (a * x + b * y) % n == 0 and (a * y - b * x) % n == 0


def eisenstein_ideal_contains(a: int, b: int, x: int, y: int) -> bool:
    c = c_channel(a, b)
    return ((a - b) * x + b * y) % c == 0 and (a * y - b * x) % c == 0


def split_from_idempotent(h: int, e: int) -> tuple[int, int]:
    return gcd(e, h), gcd(e - 1, h)


def reconstructed_pair(n: int, c: int):
    u = 3 * n - 2 * c
    v = 2 * c - n
    if not (is_square(u) and is_square(v)):
        return None
    x, y = isqrt(u), isqrt(v)
    if (x - y) % 2:
        return None
    return (x + y) // 2, (x - y) // 2


def audit_t4() -> dict:
    snf_cases = 0
    primitive_cases = 0
    nonprimitive_cases = 0
    pointed_cases = 0
    kernel_tests = 0

    for a in range(T4_CELL_MAX + 1):
        for b in range(T4_CELL_MAX + 1):
            if a == 0 and b == 0:
                continue
            d = gcd(a, b)
            g1, g2 = gaussian_snf(a, b)
            e1, e2 = eisenstein_snf(a, b)
            assert g1 == d and e1 == d
            assert g1 * g2 == n_channel(a, b)
            assert e1 * e2 == c_channel(a, b)
            # Additive quotient cyclic iff first Smith invariant is 1.
            assert (g1 == 1) == (d == 1)
            assert (e1 == 1) == (d == 1)
            snf_cases += 1
            if d == 1:
                primitive_cases += 1
            else:
                nonprimitive_cases += 1

    # Exact nonprimitive control requested by the packet.
    assert gaussian_snf(2, 2) == (2, 4)
    assert eisenstein_snf(2, 2) == (2, 2)

    for a in range(1, T4_CELL_MAX + 1):
        for b in range(1, T4_CELL_MAX + 1):
            if gcd(a, b) != 1:
                continue
            n = n_channel(a, b)
            c = c_channel(a, b)
            h = n * c
            assert gcd(b, n) == gcd(b, c) == gcd(b, h) == 1
            assert gcd(n, c) == 1

            s_n = (-a * pow(b, -1, n)) % n
            s_c = (-a * pow(b, -1, c)) % c
            r = (-a * pow(b, -1, h)) % h

            assert (s_n * s_n + 1) % n == 0
            assert (s_c * s_c + s_c + 1) % c == 0
            assert r % n == s_n
            assert r % c == s_c
            assert ((r * r + 1) * (r * r + r + 1)) % h == 0
            assert gcd(h, r * r + 1) == n
            assert gcd(h, r * r + r + 1) == c
            pointed_cases += 1

            if a <= T4_KERNEL_CELL_MAX and b <= T4_KERNEL_CELL_MAX:
                for x in range(-T4_KERNEL_XY, T4_KERNEL_XY + 1):
                    for y in range(-T4_KERNEL_XY, T4_KERNEL_XY + 1):
                        ker_n = (x + y * s_n) % n == 0
                        ker_c = (x + y * s_c) % c == 0
                        assert ker_n == gaussian_ideal_contains(a, b, x, y)
                        assert ker_c == eisenstein_ideal_contains(a, b, x, y)
                        kernel_tests += 2

    # Primitive diagonal boundary: C=1 is harmless for the unpointed collapse.
    a = b = 1
    assert n_channel(a, b) == 2 and c_channel(a, b) == 1
    assert gaussian_snf(a, b) == (1, 2)
    assert eisenstein_snf(a, b) == (1, 1)

    return {
        "snf_cases": snf_cases,
        "primitive_snf_cases": primitive_cases,
        "nonprimitive_snf_cases": nonprimitive_cases,
        "pointed_primitive_positive_cases": pointed_cases,
        "explicit_kernel_equivalences_checked": kernel_tests,
        "nonprimitive_control_(2,2)": {
            "gaussian_snf": gaussian_snf(2, 2),
            "eisenstein_snf": eisenstein_snf(2, 2),
        },
    }


def audit_t7() -> dict:
    positive_pairs = set()
    interior_pairs = set()
    for a in range(1, T7_CELL_MAX + 1):
        for b in range(1, T7_CELL_MAX + 1):
            if gcd(a, b) != 1:
                continue
            n = n_channel(a, b)
            c = c_channel(a, b)
            if n * c <= T7_H_MAX:
                positive_pairs.add((n, c))
                if a != b:
                    interior_pairs.add((n, c))

    idempotents = 0
    source_gate_true = 0
    minimal_gate_true = 0
    reconstruction_checks = 0
    swap_checks = 0

    for h in range(1, T7_H_MAX + 1):
        for e in range(h):
            if (e * e - e) % h:
                continue
            idempotents += 1
            n, c = split_from_idempotent(h, e)
            assert n * c == h
            assert gcd(n, c) == 1

            u = 3 * n - 2 * c
            v = 2 * c - n
            squares = is_square(u) and is_square(v)

            # Source/interior version: C<N<2C + two squares.
            source_gate = c < n < 2 * c and squares
            assert source_gate == ((n, c) in interior_pairs)
            if source_gate:
                source_gate_true += 1

            # Stronger positive version: N>C + two squares.
            # V square already forces N<=2C; equality is the positive diagonal.
            minimal_gate = n > c and squares
            assert minimal_gate == ((n, c) in positive_pairs)
            if minimal_gate:
                minimal_gate_true += 1
                pair = reconstructed_pair(n, c)
                assert pair is not None
                a, b = pair
                assert a >= b > 0
                assert gcd(a, b) == 1
                assert n_channel(a, b) == n
                assert c_channel(a, b) == c
                assert (isqrt(u) & 1) == (isqrt(v) & 1)
                reconstruction_checks += 1

            e_swap = (1 - e) % h
            n_swap, c_swap = split_from_idempotent(h, e_swap)
            assert (n_swap, c_swap) == (c, n)
            swap_checks += 1

    # Arithmetically legal idempotent split, inside C<N<2C, but square gate fails.
    assert (21 * 21 - 21) % 28 == 0
    assert split_from_idempotent(28, 21) == (7, 4)
    assert (3 * 7 - 2 * 4, 2 * 4 - 7) == (13, 1)
    assert not is_square(13)

    # Two squares alone are not enough for a positive cell: N>C is essential.
    assert (15 * 15 - 15) % 35 == 0
    assert split_from_idempotent(35, 15) == (5, 7)
    assert (3 * 5 - 2 * 7, 2 * 7 - 5) == (1, 9)
    assert reconstructed_pair(5, 7) == (2, -1)

    # Valid oriented split and channel-swap control.
    assert (10 * 10 - 10) % 15 == 0
    assert split_from_idempotent(15, 10) == (5, 3)
    assert reconstructed_pair(5, 3) == (2, 1)
    assert split_from_idempotent(15, (1 - 10) % 15) == (3, 5)

    return {
        "H_range": [1, T7_H_MAX],
        "idempotents_checked": idempotents,
        "source_interior_gate_hits": source_gate_true,
        "stronger_positive_gate_hits": minimal_gate_true,
        "successful_reconstructions": reconstruction_checks,
        "channel_swap_checks": swap_checks,
        "controls": {
            "square_gate_fail": {"H": 28, "e": 21, "N": 7, "C": 4, "U": 13, "V": 1},
            "positivity_fail_if_N_gt_C_removed": {"H": 35, "e": 15, "N": 5, "C": 7, "U": 1, "V": 9},
            "valid_and_swapped": {"H": 15, "e": 10, "N": 5, "C": 3, "cell": (2, 1)},
        },
    }


def audit_t8() -> dict:
    cells = 0
    eligible = 0
    dual = 0
    semiprime_equivalence_checks = 0

    for a in range(1, T8_CELL_MAX + 1):
        for b in range(1, T8_CELL_MAX + 1):
            cells += 1
            n = n_channel(a, b)
            c = c_channel(a, b)
            h = n * c
            if n <= 1 or c <= 1:
                continue
            eligible += 1
            dual_prime = is_prime(n) and is_prime(c)
            sf_semiprime = is_squarefree_semiprime(h)
            assert dual_prime == sf_semiprime
            semiprime_equivalence_checks += 1
            if dual_prime:
                dual += 1
                assert n != c
                assert gcd(n, c) == 1
                assert gcd(a, b) == 1

    # Positive dual-prime control.
    assert (n_channel(1, 2), c_channel(1, 2)) == (5, 3)
    assert is_squarefree_semiprime(15)

    # Prime-power/composite channel control.
    assert (n_channel(3, 4), c_channel(3, 4)) == (25, 13)
    assert not is_prime(25) and is_prime(13)
    assert not is_squarefree_semiprime(25 * 13)
    # Z/25Z is not a field: 5 is a nonzero zero-divisor.
    assert 5 % 25 != 0 and (5 * 5) % 25 == 0

    # Composite non-prime-power control.
    assert (n_channel(1, 3), c_channel(1, 3)) == (10, 7)
    assert not is_prime(10) and is_prime(7)
    assert not is_squarefree_semiprime(70)

    return {
        "positive_cell_box": [1, T8_CELL_MAX],
        "cells_checked": cells,
        "eligible_NC_gt_1": eligible,
        "dual_prime_cells": dual,
        "squarefree_semiprime_equivalence_checks": semiprime_equivalence_checks,
        "controls": {
            "dual_prime": {"cell": (1, 2), "N": 5, "C": 3, "H": 15},
            "prime_power": {"cell": (3, 4), "N": 25, "C": 13, "H": 325},
            "composite": {"cell": (1, 3), "N": 10, "C": 7, "H": 70},
        },
    }


def main() -> None:
    t4 = audit_t4()
    t7 = audit_t7()
    t8 = audit_t8()

    print("PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_CHECKER: PASS")
    print("T4", t4)
    print("T7", t7)
    print("T8", t8)


if __name__ == "__main__":
    main()
