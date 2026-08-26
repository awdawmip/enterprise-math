#!/usr/bin/env python3
"""Exact checker for the C3 bouquet = unfolded central filament identity."""

from __future__ import annotations


def eps(r: int) -> int:
    return r & 1


def shell_start(r: int) -> int:
    return 1 + 3 * r * (r - 1) // 2


def N(r: int, t: int, sigma: int) -> int:
    return shell_start(r) + t + sigma * r


def F3(H: int, r: int) -> int:
    return H + (3 * r * r + eps(r)) // 2


def bouquet(m: int) -> tuple[int, int, int]:
    return (6 * m * m - 2 * m + 1, 6 * m * m + 1, 6 * m * m + 2 * m + 1)


def root_set(poly, q: int) -> set[int]:
    return {m for m in range(q) if poly(m) % q == 0}


def main() -> None:
    for m in range(1, 1000):
        r = 2 * m
        t = m
        c = F3(1, r)
        vals = (N(r, t, 0), N(r, t, 1), N(r, t, 2))
        assert c == 6 * m * m + 1
        assert vals == (c - r, c, c + r)
        assert vals == bouquet(m)

        p = vals[0] * vals[1] * vals[2]
        assert p == c * (c * c - r * r)
        assert p == 216 * m**6 + 84 * m**4 + 14 * m**2 + 1

    # Reconstruct the exact 3/5/7 nonzero-residue saturation gate.
    fm = lambda m: 6*m*m - 2*m + 1
    f0 = lambda m: 6*m*m + 1
    fp = lambda m: 6*m*m + 2*m + 1

    roots3 = [root_set(f, 3) for f in (fm, f0, fp)]
    roots5 = [root_set(f, 5) for f in (fm, f0, fp)]
    roots7 = [root_set(f, 7) for f in (fm, f0, fp)]

    assert roots3 == [{2}, set(), {1}]
    assert roots5 == [{1}, {2, 3}, {4}]
    assert roots7 == [{2, 3}, {1, 6}, {4, 5}]

    for q, roots in ((3, roots3), (5, roots5), (7, roots7)):
        covered = set().union(*roots)
        assert covered == set(range(1, q))

    # Cross-route coherence.
    B = 3
    breaker = 5
    k_star = 2 * breaker - 1
    assert k_star == 9
    M9 = (k_star - 2) * (k_star - 4)
    assert M9 == 35
    assert B * M9 == 105
    assert 3 * 5 * 7 == 105
    assert B * (k_star - 2) * (k_star - 4) == 105
    assert (105 + 1) // 2 == 53
    assert 105 + 1 == 2 * 53

    print("C3_BOUQUET_EQUALS_UNFOLDED_H0_EVEN_FILAMENT=PASS")
    print("BOUQUET_PRODUCT_CUBIC_NORM=PASS")
    print("MOD_3_5_7_NONZERO_SATURATION=PASS")
    print("COHERENCE_105_EQUALS_B_TIMES_M9=PASS")
    print("TERMINAL_EXCEPTION_53_EQUALS_106_OVER_2=PASS")


if __name__ == "__main__":
    main()
