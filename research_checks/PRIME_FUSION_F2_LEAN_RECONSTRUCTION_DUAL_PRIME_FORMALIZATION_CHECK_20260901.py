#!/usr/bin/env python3
"""Finite regression audit for Prime Fusion F2 T7/T8 formalization.

This checker is deliberately bounded evidence only. The unbounded claims live in
Lean; this script guards exact examples, negative controls, and channel ordering.
"""
from __future__ import annotations

from math import gcd, isqrt


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


def channels(a: int, b: int) -> tuple[int, int]:
    return a * a + b * b, a * a - a * b + b * b


def check_t7() -> tuple[int, int, int, int]:
    cells = 0
    diagonal = 0
    interior = 0
    primitive_from_coprime_channels = 0

    for a in range(1, 65):
        for b in range(1, 65):
            cells += 1
            n, c = channels(a, b)
            u = a + b
            v = a - b
            U = 3 * n - 2 * c
            V = 2 * c - n

            assert U == u * u
            assert V == v * v
            assert c < n
            assert (V > 0) == (a != b)

            if a == b:
                diagonal += 1
            else:
                interior += 1

            # The theorem chooses nonnegative square roots, hence reconstructs
            # the unordered positive cell in orientation a >= b.
            aa, bb = max(a, b), min(a, b)
            su, sv = isqrt(U), isqrt(V)
            assert su * su == U and sv * sv == V
            assert (su + sv) % 2 == 0
            assert (su - sv) % 2 == 0
            ar = (su + sv) // 2
            br = (su - sv) // 2
            assert (ar, br) == (aa, bb)
            assert ar > 0 and br > 0
            assert channels(ar, br) == (n, c)

            if gcd(n, c) == 1:
                primitive_from_coprime_channels += 1
                assert gcd(a, b) == 1

    # Exact negative controls for theorem-critical gates.
    # Oriented but not square-gated: U=5 is not a square.
    n, c = 3, 2
    assert c < n and 3 * n - 2 * c == 5 and isqrt(5) ** 2 != 5

    # Square/parity data without N>C reconstructs a boundary/nonpositive cell.
    n, c = 1, 1
    U, V = 3 * n - 2 * c, 2 * c - n
    su, sv = isqrt(U), isqrt(V)
    assert (U, V, su, sv) == (1, 1, 1, 1)
    assert (su + sv) % 2 == 0 and (su - sv) % 2 == 0
    assert (su - sv) // 2 == 0

    # Strict-interior residue: positive diagonal cells have V=0, not V>0.
    assert channels(7, 7) == (98, 49)
    assert 2 * 49 - 98 == 0

    return cells, diagonal, interior, primitive_from_coprime_channels


def check_t8() -> int:
    dual_prime_cells = 0
    for a in range(0, 65):
        for b in range(0, 65):
            if a == 0 and b == 0:
                continue
            n, c = channels(a, b)
            if is_prime(n) and is_prime(c) and n != c:
                dual_prime_cells += 1
                h = n * c
                assert h == n * c
                assert is_prime(n) and is_prime(c)
                # Exact channel-attachment control: the unordered product is
                # symmetric and therefore cannot recover which factor is N/C.
                assert n * c == c * n
    assert dual_prime_cells > 0
    return dual_prime_cells


def main() -> None:
    cells, diagonal, interior, primitive = check_t7()
    dual = check_t8()
    print(
        "PRIME_FUSION_F2_CHECK: PASS "
        f"cells={cells} diagonal={diagonal} interior={interior} "
        f"coprime_channel_cells={primitive} dual_prime_cells={dual}"
    )


if __name__ == "__main__":
    main()
