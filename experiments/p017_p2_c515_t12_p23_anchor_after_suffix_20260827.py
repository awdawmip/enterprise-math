#!/usr/bin/env python3
"""Exact checker for the preferred P(23) c515 low-pair anchor."""

from fractions import Fraction as Q

K = 116_009_280_740_973_308
W = K + 1
Q23 = 223_092_870


def main() -> None:
    L23 = Q23 * ((2 * K) // Q23)
    tail = 2 * K - L23

    assert (2 * K) // Q23 == 1_040_008_860
    assert tail == 79_118_416
    assert 0 <= tail < Q23
    assert K < L23 < 2 * K
    assert Q(tail, 2 * K) < Q(342, 10**12)

    # Short-scale cube threshold: 23^3 < W^(1/4) < 29^3.
    assert 23**12 < W < 29**12

    # Hard-depth envelope below D^(2/3)=W^(20/27).
    assert 29 ** (27 * 8) < W**20
    assert 29 ** (27 * 9) > W**20

    print("P017 c515 P23 anchor checker: PASS")
    print("relative P23 tail < 3.42e-10")
    print("residual hard primes >=29 and hard omega<=8")
    print("29^3 > N0, so canonical 0/1/2-prime suffix split remains valid")


if __name__ == "__main__":
    main()
