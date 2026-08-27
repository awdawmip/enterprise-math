#!/usr/bin/env python3
"""Exact finite checker for the c515 P(23) anchor activation automaton.

For a fixed P(23)-stripped beta-2 hard modulus b, the anchor support depends only
on parity omega(b) and T=Q/b.  This checker enumerates the 256 anchor divisors,
computes their exact activation thresholds, and certifies the shallow geometric
block consequences used by the j=1 route.
"""

ANCHOR = (23, 19, 17, 13, 11, 7, 5, 3)  # descending


def activation_threshold(mask: int, hard_parity: int) -> tuple[int, int]:
    aa = [ANCHOR[i] for i in range(8) if (mask >> i) & 1]
    e = 1
    for a in aa:
        e *= a
    crit = e  # full level e<T
    prefix = 1
    for ell, a in enumerate(aa, start=1):
        # Global Rosser position is omega(b)+ell.
        if (hard_parity + ell) % 2 == 1:
            crit = max(crit, prefix * a**3)
        prefix *= a
    return crit, e


def active_count(hard_parity: int, n: int) -> int:
    # T=(6/5)^n. Strict activation crit<T is checked by integers.
    return sum(
        crit * 5**n < 6**n
        for crit, _ in (
            activation_threshold(mask, hard_parity) for mask in range(256)
        )
    )


def main() -> None:
    rows = {
        parity: sorted(
            activation_threshold(mask, parity) + (mask,) for mask in range(256)
        )
        for parity in (0, 1)
    }

    # Even hard depth: the first nontrivial anchor is e=3 and activates only at T>27.
    assert rows[0][0][:2] == (1, 1)
    assert rows[0][1][:2] == (27, 3)

    # Odd hard depth: single anchor primes activate at their own level thresholds.
    assert rows[1][0][:2] == (1, 1)
    assert [row[:2] for row in rows[1][1:9]] == [
        (3, 3), (5, 5), (7, 7), (11, 11),
        (13, 13), (17, 17), (19, 19), (23, 23),
    ]
    # The first two-anchor odd-parity state is delayed to T>135.
    assert rows[1][9][0] == 135

    # Geometric blocks have T<=(6/5)^(i+j+2).
    # All parities force e=1 on the first five block diagonals i+j<=4.
    for depth in range(0, 5):
        n = depth + 2
        assert active_count(0, n) == 1
        assert active_count(1, n) == 1

    # Through i+j<=16, even hard depth still forces e=1.
    for depth in range(0, 17):
        assert active_count(0, depth + 2) == 1

    # Through the same range, odd hard depth can use at most the identity plus
    # the eight single anchor primes; no two-prime anchor has yet activated.
    for depth in range(0, 17):
        assert active_count(1, depth + 2) <= 9

    print("P017 c515 P23 anchor activation automaton: PASS")
    print("first even-parity nontrivial threshold = 27")
    print("first odd-parity two-anchor threshold = 135")
    print("depth 0..4: both parities force e=1")
    print("depth 0..16: even parity e=1; odd parity <=9 labels")
    print("depth counts (d, even, odd):")
    for depth in range(0, 20):
        print(depth, active_count(0, depth + 2), active_count(1, depth + 2))


if __name__ == "__main__":
    main()
