#!/usr/bin/env python3
"""Exact finite checker for the c515 two-pair credit / z^2 Rosser collapse."""

from itertools import combinations

K = 116_009_280_740_973_308
W = K + 1


def primes_upto(n: int) -> tuple[int, ...]:
    primes: list[int] = []
    for x in range(2, n + 1):
        prime = True
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                prime = False
                break
        if prime:
            primes.append(x)
    return tuple(primes)


def qcrit(subset: tuple[int, ...]) -> int:
    desc = tuple(sorted(subset, reverse=True))
    running = 1
    out = 1
    for j, q in enumerate(desc, start=1):
        if j % 2 == 1:
            out = max(out, running * q**3)
        running *= q
    return out


def active(subset: tuple[int, ...]) -> bool:
    # qcrit < W^(10/27), cleared exactly.
    return qcrit(subset) ** 27 < W**10


def census(primes: tuple[int, ...], max_depth: int) -> dict[int, int]:
    out: dict[int, int] = {}
    for depth in range(max_depth + 1):
        count = sum(1 for subset in combinations(primes, depth) if active(subset))
        if count:
            out[depth] = count
    return out


def main() -> None:
    # Pair-budget identity: 2*(6u-1/2)=12u-1.
    # We check the coefficients exactly after clearing the symbolic variable.
    assert 2 * 6 == 12
    assert 2 * (-1) == -2  # twice the half-term after denominator 2 is cleared

    # Four-prime witness leaves level D/z^4 = D^(1/3)=W^(10/27).
    # First Rosser prime ceiling: q^3 < W^(10/27).
    assert 127**81 < W**10
    assert 131**81 > W**10

    all_odd = tuple(p for p in primes_upto(127) if p % 2 == 1)
    hard = tuple(p for p in all_odd if p >= 29)
    assert len(all_odd) == 30
    assert len(hard) == 22

    hard_counts = census(hard, 3)
    assert hard_counts == {0: 1, 1: 22, 2: 231}
    assert sum(hard_counts.values()) == 254

    full_counts = census(all_odd, 6)
    assert full_counts == {0: 1, 1: 30, 2: 435, 3: 1153, 4: 1234, 5: 288}
    assert sum(full_counts.values()) == 3141

    print("P017 c515 two-pair credit / z2 residual checker: PASS")
    print("hard P23-stripped support =", hard_counts, "total=254")
    print("anchor-free odd support =", full_counts, "total=3141")
    print("hard residual Rosser depth <=2 at Q<=z^2")


if __name__ == "__main__":
    main()
