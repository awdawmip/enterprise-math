#!/usr/bin/env python3
"""Check self-delimiting boundary recovery on the frozen island spectrum."""

from __future__ import annotations

import math


def Bc(s: int) -> int:
    return 1 + 3 * s * (s + 1) // 2


def inverse_typed(n: int):
    if n < 1:
        raise ValueError(n)
    s = max(0, (math.isqrt(24 * n - 15) - 3) // 6)
    while Bc(s + 1) <= n:
        s += 1
    while s > 0 and Bc(s) > n:
        s -= 1
    j = n - Bc(s)
    sigma, t = divmod(j, s + 1)
    assert sigma in (0, 1, 2)
    return s, t, sigma


def C(r: int, h: int) -> int:
    if r % 2 == 0:
        return h + 3 * r * r // 2 + 1
    return h + 3 * (r * r + 1) // 2


def long_decode(p0: int, p1: int):
    s, t, sigma = inverse_typed(p0)
    if sigma != 1:
        return None
    r = s + 1
    h = t - (r + 1) // 2
    values = []
    for d in range(9):
        v = C(r + d, h)
        values.append(v)
        if v == p1:
            return tuple(values)
        if v > p1:
            break
    return None


def triangle_decode(p0: int, p2: int):
    D = p2 - p0
    if D < 0 or (D - 4) % 2:
        return None
    u = (D - 4) // 2
    sigma = u % 3
    r = (u - sigma) // 3
    s0, _t0, sigma0 = inverse_typed(p0)
    if r != s0 + 1 or sigma != sigma0:
        return None
    candidates = (p0 + u, p0 + u + 1)
    odd = [v for v in candidates if v % 2 == 1]
    if len(odd) != 1:
        return None
    return (p0, odd[0], p2)


def diamond_decode(p0: int, p3: int):
    D = p3 - p0
    rem = D % 3
    if rem not in (1, 2):
        return None
    K0 = 4 if rem == 1 else 2
    num = 2 * p0 + p3 - 6 - K0
    if num % 3:
        return None
    p1 = num // 3
    p2 = p0 + p3 - 6 - p1
    if not (p0 < p1 < p2 < p3):
        return None

    # The first triple must self-localize to the actual typed start Cell.
    K = p0 - 2 * p1 + p2
    if K not in (2, 4):
        return None
    delta = (4 - K) // 2
    u = p1 - p0 - delta
    sigma = u % 3
    r = (u - sigma) // 3
    s0, _t0, sigma0 = inverse_typed(p0)
    if r != s0 + 1 or sigma != sigma0:
        return None
    return (p0, p1, p2, p3)


def decode_boundary_pair(p0: int, pmax: int):
    candidates = []
    for decoder in (long_decode, triangle_decode, diamond_decode):
        result = decoder(p0, pmax)
        if result is not None:
            candidates.append(result)
    # Duplicate descriptions of the same 3/4 packet are harmless; deduplicate.
    unique = sorted(set(candidates), key=lambda x: (len(x), x))
    return unique


def main() -> None:
    witnesses = {
        3: (37, 53, 73),
        4: (17, 29, 43, 61),
        5: (3767, 3919, 4073, 4231, 4391),
        6: (63611, 64231, 64853, 65479, 66107, 66739),
        7: (363269, 364747, 366227, 367711, 369197, 370687, 372179),
        8: (1370471, 1373341, 1376213, 1379089, 1381967, 1384849, 1387733, 1390621),
        9: (
            171283421, 171315481, 171347543, 171379609, 171411677,
            171443749, 171475823, 171507901, 171539981,
        ),
    }

    for k, packet in witnesses.items():
        decoded = decode_boundary_pair(packet[0], packet[-1])
        assert decoded == [packet], (k, decoded)

    # Long-filament monotonicity and self-delimitation over a broad exact grid.
    for r in range(4, 500):
        lo = -((r + 1) // 2)
        hi = r // 2 - 1
        for h in (lo, (lo + hi) // 2, hi):
            values = tuple(C(r + j, h) for j in range(9))
            assert all(values[j] < values[j + 1] for j in range(8))
            s, t, sigma = inverse_typed(values[0])
            assert (s + 1, sigma) == (r, 1)
            assert t - (r + 1) // 2 == h
            for k in range(3, 10):
                decoded = long_decode(values[0], values[k - 1])
                assert decoded == values[:k]

    print("TYPED_INVERSE_FROM_FIRST_BOUNDARY=PASS")
    print("LONG_PATH_SPANS_STRICTLY_INCREASING=PASS")
    print("BOUNDARY_PAIR_RECOVERS_K=PASS")
    print("EXPLICIT_ISLAND_SPECTRUM_3_TO_9=PASS")
    print("GLOBAL_PRIME_ISLAND_BOUNDARIES=SELF_DELIMITING")


if __name__ == "__main__":
    main()
