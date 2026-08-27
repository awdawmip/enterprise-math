#!/usr/bin/env python3
"""Exact finite checker collapsing all corrected c515 T1-T2 shells j>=2.

The j=2 square-divisor bound extends to higher least-prime valuations.  The
later-prime multiplicity is at most 9-j, and r^{-j} is bounded by
1447^{-(j-2)} r^{-2}.  The combined j=2..8 residual penalty remains below
3/25000 of L23.
"""

from fractions import Fraction as Q

L23 = 232_018_561_402_828_200
RCOUNT = 47_735
S2 = Q(423, 5_000_000)  # frozen upper bound for sum_r 1/r^2


def main() -> None:
    # For valuation j, 5(j+1+k)<54, hence k<=9-j for j=2..8.
    for j in range(2, 9):
        kmax = 9 - j
        assert 5 * (j + 1 + kmax) < 54
        assert 5 * (j + 1 + kmax + 1) >= 54

    # Sum the r^{-j} tails through the j=2 square-reciprocal envelope.
    valuation_factor = sum(
        Q(9 - j, 1447 ** (j - 2)) for j in range(2, 9)
    )
    plus_one_multiplicity = sum(9 - j for j in range(2, 9))
    assert plus_one_multiplicity == 28

    hit_density = S2 * valuation_factor + Q(RCOUNT * 28, L23)
    normalized = Q(20, 93) * Q(73, 80) * hit_density
    assert normalized < Q(3, 25_000)

    print("P017 c515 T1-T2 high-valuation direct-collapse certificate: PASS")
    print("valuation shells j=2..8 all included")
    print("normalized upper ~=", float(normalized))
    print("certified < 3/25000 = 0.00012")


if __name__ == "__main__":
    main()
