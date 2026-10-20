#!/usr/bin/env python3
"""Exact checker for the native Enterprise seven-cell star Poisson/localization law."""

from __future__ import annotations

import math


def shell_base(r: int) -> int:
    return 3 * r * (r - 1) // 2 + 1


def label(r: int, t: int, sigma: int) -> int:
    return shell_base(r) + t + sigma * r


def coord_from_n(n: int):
    if n < 1:
        raise ValueError
    r = max(1, int((math.sqrt(1 + 8 * n / 3) - 1) / 2))
    while 3 * r * (r + 1) // 2 < n:
        r += 1
    while r > 1 and 3 * (r - 1) * r // 2 >= n:
        r -= 1
    j = n - shell_base(r)
    sigma, t = divmod(j, r)
    if sigma == 0:
        addr = (r - t, t, 0)
    elif sigma == 1:
        addr = (0, r - t, t)
    elif sigma == 2:
        addr = (t, 0, r - t)
    else:
        raise AssertionError
    return r, t, sigma, addr


def reverse_label(addr) -> int:
    a, b, c = addr
    r = a + b + c
    if c == 0 and a > 0:
        sigma, t = 0, b
    elif a == 0 and b > 0:
        sigma, t = 1, c
    elif b == 0 and c > 0:
        sigma, t = 2, a
    else:
        raise ValueError(addr)
    return shell_base(r) + (r - 1 - t) + sigma * r


def neighbor_labels(r: int, t: int, sigma: int):
    n = label(r, t, sigma)
    offsets = (
        3 * r + sigma,
        6 * r + 4 + 2 * sigma,
        3 * r + 1 + sigma,
        -3 * r + 3 - sigma,
        -6 * r + 8 - 2 * sigma,
        -3 * r + 2 - sigma,
    )
    return n, [n + d for d in offsets]


def local_recover(n: int, nbr):
    pairs = ((0, 3), (1, 4), (2, 5))
    curv = [nbr[i] + nbr[j] - 2 * n for i, j in pairs]
    gaps = [abs(nbr[i] - nbr[j]) for i, j in pairs]
    assert sorted(curv) == [3, 3, 12]
    high = curv.index(12)
    g3 = gaps[high]
    r = (g3 + 4) // 12
    sigma = ((g3 + 4) % 12) // 4
    t = n - shell_base(r) - sigma * r
    return r, t, sigma, tuple(sorted(gaps)), tuple(sorted(curv))


def main() -> None:
    tested = 0
    for r in range(6, 501):
        for sigma in range(3):
            for t in range(2, r - 2):
                n, nbr = neighbor_labels(r, t, sigma)
                assert sum(nbr) - 6 * n == 18
                rr, tt, ss, gaps, curv = local_recover(n, nbr)
                assert (rr, tt, ss) == (r, t, sigma)
                g1, g2, g3 = gaps
                assert g2 == g1 + 2
                assert g3 == g1 + g2

                # Reverse-traversal ablation on the same geometric cells.
                _, _, _, addr = coord_from_n(n)
                rn = reverse_label(addr)
                rnbr = []
                for m in nbr:
                    _, _, _, a = coord_from_n(m)
                    rnbr.append(reverse_label(a))
                assert sum(rnbr) - 6 * rn == 18
                rpairs = ((0, 3), (1, 4), (2, 5))
                rcurv = sorted(rnbr[i] + rnbr[j] - 2 * rn for i, j in rpairs)
                rgaps = sorted(abs(rnbr[i] - rnbr[j]) for i, j in rpairs)
                assert rcurv == [3, 3, 12]
                assert rgaps == list(gaps)
                tested += 1

    print("SEVEN_CELL_STAR_POISSON=18")
    print("OPPOSITE_PAIR_HESSIAN_SPECTRUM=3,3,12")
    print("LOCAL_COORDINATE_RECOVERY=PASS")
    print("REVERSE_TRAVERSAL_ABLATION=PASS")
    print(f"TESTED_INTERNAL_STARS={tested}")


if __name__ == "__main__":
    main()
