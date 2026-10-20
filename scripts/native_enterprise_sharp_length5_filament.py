#!/usr/bin/env python3
"""Verify the sharp length-five cap and two explicit chiral nine-prime filaments."""

from __future__ import annotations

import math


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def chain_values(r: int, h: int, L: int):
    t = h + (r + 1) // 2
    n = shell_base(r) + r + t
    p0 = n - 6 * r + 6
    values = [p0]
    for s in range(r, r + L + 3):
        d = 3 * s - 4 if s % 2 == 0 else 3 * s - 5
        values.append(values[-1] + d)
    return values


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def mod5_survivors(L: int):
    out = []
    for rmod10 in range(10):
        r = 100 + rmod10
        for hmod5 in range(5):
            vals = chain_values(r, hmod5, L)
            if all(v % 5 != 0 for v in vals):
                out.append((rmod10, hmod5))
    return out


def curvature_vector(vals):
    assert len(vals) == 9
    c = vals[4]
    return tuple(vals[4-j] - 2*c + vals[4+j] for j in range(1,5))


def main() -> None:
    expected_counts = {1:15, 2:10, 3:7, 4:4, 5:2, 6:0}
    for L, expected in expected_counts.items():
        got = mod5_survivors(L)
        assert len(got) == expected, (L,got)

    assert mod5_survivors(5) == [(3,4),(8,1)]
    assert mod5_survivors(6) == []

    even_vals = [
        171283421,171315481,171347543,171379609,171411677,
        171443749,171475823,171507901,171539981,
    ]
    odd_vals = [
        17434825207,17435148641,17435472079,17435795519,17436118963,
        17436442409,17436765859,17437089311,17437412767,
    ]

    assert chain_values(10688,-2474,5) == even_vals
    assert chain_values(107813,7624,5) == odd_vals

    for packet in (even_vals, odd_vals):
        assert all(is_prime_trial(v) for v in packet)

    assert curvature_vector(even_vals) == (4,12,28,48)
    assert curvature_vector(odd_vals) == (2,12,26,48)

    print("MOD5_LENGTH_COUNTS=15,10,7,4,2,0")
    print("SHARP_MAX_FILAMENT_LENGTH=5")
    print("EVEN_CHIRAL_PACKET=PASS")
    print("ODD_CHIRAL_PACKET=PASS")
    print("MULTISCALE_CURVATURES=(4,12,28,48)/(2,12,26,48)")


if __name__ == "__main__":
    main()
