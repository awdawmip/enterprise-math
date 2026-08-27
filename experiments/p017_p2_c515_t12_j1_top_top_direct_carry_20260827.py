#!/usr/bin/env python3
"""Exact finite checker for the c515 j=1 top-long/top-short direct carry block.

This certificate consumes the already-proved top-long support density <3/200,
recomputes the 185-state top short support, proves that every nontrivial P(23)
anchor divisor is excluded by the full Rosser level on the top x top block, and
checks that the resulting absolute sharp-carry contribution is < 10^-3 L23.

It is a block certificate only. It does not bound the full j=1 carrier or prove
a finite P2 theorem.
"""

from fractions import Fraction as Q
from math import isqrt

K0 = 116_009_280_740_973_308
W = K0 + 1
Q23 = 223_092_870
L23 = Q23 * ((2 * K0) // Q23)
B_UP = 494_793_856_728_460
N0_FLOOR = 18_455


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def main() -> None:
    # P(23)-anchored target interval.
    assert (2 * K0) // Q23 == 1_040_008_860
    assert L23 == 232_018_561_402_828_200
    assert 2 * K0 - L23 == 79_118_416 < Q23

    # Exact c515 top scales B=W^(31/36), N0=W^(1/4).
    assert (B_UP - 1) ** 36 < W**31 < B_UP**36
    assert N0_FLOOR**4 < W < (N0_FLOOR + 1) ** 4

    # Latest Brun-Titchmarsh support theorem:
    # A_M / ((5/6) B) < 3/200, hence A_M < B/80.
    bt_refined = Q(537_427_837, 36_960_000_000)
    assert bt_refined < Q(3, 200)
    assert Q(3, 200) * Q(5, 6) == Q(1, 80)

    # On top x top, m>(5/6)B and n>(5/6)N0, hence mn>(25/36)D.
    # The full Rosser condition is e*m*n<D.  Every nontrivial odd anchor
    # divisor e|P(23) has e>=3, but 3*(25/36)>1, so e=1 is forced.
    assert 3 * 25 > 36

    # Recompute the corrected j=1 short hard carrier:
    # identity + one prime 29..1439 + products of two distinct such primes.
    hard_primes = [p for p in primes_upto(1439) if p >= 29]
    assert len(hard_primes) == 219
    values = {1, *hard_primes}
    for i, p in enumerate(hard_primes):
        for q in hard_primes[i + 1 :]:
            pq = p * q
            if pq > N0_FLOOR:
                break
            values.add(pq)
    assert len(values) == 1115

    # Exact symbolic top block: (5/6) W^(1/4) < n <= W^(1/4).
    top_short = [
        n
        for n in values
        if (6 * n) ** 4 > 5**4 * W and n**4 <= W
    ]
    assert len(top_short) == 185

    # Residual ordered-pair kernel and source prefactor.
    kappa_max = Q(73, 80)
    Delta = Q(93, 20)

    # A_M < B/80 < B_UP/80 and |e(mn)|<1 for sharp carry.
    # Therefore the whole top x top block is bounded by
    # (1/Delta)*(73/80)*(B_UP/80)*185.
    normalized = (
        Q(1, 1) / Delta
        * kappa_max
        * Q(B_UP, 80)
        * len(top_short)
        / L23
    )
    assert normalized < Q(1, 1000)

    print("P017 c515 j=1 top x top direct-carry certificate: PASS")
    print("L23 =", L23)
    print("B <", B_UP)
    print("top short states =", len(top_short))
    print("top x top forces anchor e=1")
    print("normalized direct-carry upper ~=", float(normalized))
    print("certified < 1/1000")


if __name__ == "__main__":
    main()
