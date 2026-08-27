#!/usr/bin/env python3
"""Exact finite checker for the c515 j=1 top×top canonical-suffix refinement.

The top short state is necessarily a product of the two smallest hard primes of
the full Rosser state. Therefore the long hard factor can use only larger hard
primes and, on the corrected j=1 depth-four family, at most two of them. The
checker upper-bounds the coupled reciprocal mass by fixed-point arithmetic and
proves a direct sharp-carry block bound < 29/50000 of L23.
"""

from fractions import Fraction as Q
from math import isqrt

K0 = 116_009_280_740_973_308
W = K0 + 1
Q23 = 223_092_870
L23 = Q23 * ((2 * K0) // Q23)
B_UP = 494_793_856_728_460
SCALE = 10**12


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def main() -> None:
    assert L23 == 232_018_561_402_828_200
    assert (B_UP - 1) ** 36 < W**31 < B_UP**36

    hard = [p for p in primes_upto(1439) if p >= 29]
    assert len(hard) == 219

    # Exact j=1 top short states. Since the block is above 15000, every state
    # is a two-prime product; identities and single hard primes do not occur.
    pairs: list[tuple[int, int, int]] = []
    for i, a in enumerate(hard):
        for b in hard[i + 1 :]:
            n = a * b
            if n > 18_455:
                break
            if (6 * n) ** 4 > 5**4 * W and n**4 <= W:
                pairs.append((a, b, n))
    assert len(pairs) == 185

    # Fixed-point upper reciprocals. suffix[b] is an upper bound, scaled by
    # SCALE, for sum_{p>b, p hard} 1/p.
    ceil_recip = {p: (SCALE + p - 1) // p for p in hard}
    suffix: dict[int, int] = {}
    running = 0
    for p in reversed(hard):
        suffix[p] = running
        running += ceil_recip[p]

    # If b2=a*b with a<b the two smallest hard primes, then b1 can contain at
    # most two primes, both >b. Repeated-prime expansion gives the safe mass
    # 1+S+S^2/2.
    coupled = Q(0)
    for _, b, _ in pairs:
        s = Q(suffix[b], SCALE)
        coupled += 1 + s + s * s / 2
    assert coupled < 236

    # q-binned Brun-Titchmarsh reciprocal-pair mass from the frozen support note.
    rlog = Q(1_997_873, 115_500_000)

    # Long-block lower endpoint is (5/6)B.  For each short suffix, BT gives
    # A(b2)/M0 < (2/5)*rlog*C_h(b2).  Use coupled<236, kappa<=73/80,
    # source prefactor 1/Delta with Delta=93/20, and B<B_UP.
    normalized = (
        Q(20, 93)
        * Q(73, 80)
        * Q(5 * B_UP, 6)
        / L23
        * Q(2, 5)
        * rlog
        * 236
    )
    assert normalized < Q(29, 50_000)

    print("P017 c515 j=1 top×top suffix-coupling certificate: PASS")
    print("top short pair states =", len(pairs))
    print("coupled hard reciprocal mass < 236")
    print("normalized upper ~=", float(normalized))
    print("certified < 29/50000 = 0.00058")


if __name__ == "__main__":
    main()
