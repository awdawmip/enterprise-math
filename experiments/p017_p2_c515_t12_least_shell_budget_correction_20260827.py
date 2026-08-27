#!/usr/bin/env python3
"""Exact checker for the corrected c515 least-shell / one-pair budget."""

from fractions import Fraction as F
from itertools import combinations

K = 116_009_280_740_973_308
W = K + 1


def primes_upto(n: int) -> list[int]:
    ps: list[int] = []
    for x in range(2, n + 1):
        ok = True
        for p in ps:
            if p * p > x:
                break
            if x % p == 0:
                ok = False
                break
        if ok:
            ps.append(x)
    return ps


def iroot(a: int, n: int) -> int:
    lo, hi = 0, 1
    while hi**n <= a:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**n <= a:
            lo = mid
        else:
            hi = mid
    return lo


def qcrit(vals: tuple[int, ...]) -> int:
    qs = tuple(sorted(vals, reverse=True))
    running = 1
    out = 1
    for j, q in enumerate(qs, start=1):
        if j % 2 == 1:
            out = max(out, running * q**3)
        running *= q
    return out


def main() -> None:
    U = F(113, 240)
    mid = U / 2
    umax = F(73, 240)
    assert mid == F(113, 480)

    # Correct pair budget after least-prime-shell cost.
    # On the lower half C(u)=6u-1/2 exactly.
    # On the upper half C(u)-(6u-1/2)=12u-113/40 >=0.
    assert 12 * mid - F(113, 40) == 0
    assert 12 * umax - F(113, 40) == F(33, 40) > 0

    # Explicit obstruction to the superseded two-pair claim at u=1/6.
    u0 = F(1, 6)
    base = 12 * u0 - 1
    least = F(1, 2)
    pair_max = 6 * u0 - F(1, 2)
    assert base == 1
    assert least == pair_max == F(1, 2)
    assert base - least == pair_max < 2 * pair_max

    # Worst corrected residual level Q*=floor(W^(5/9)).
    qstar = iroot(W**5, 9)
    assert qstar == 3_021_855_833
    assert qstar**9 <= W**5 < (qstar + 1) ** 9

    # z cutoff: hard alphabet after P23 is primes 29..1439.
    hard = tuple(p for p in primes_upto(1439) if p >= 29)
    assert len(hard) == 219

    # Five hard primes are impossible; test the minimal five-prime packet.
    minimal5 = tuple(hard[:5])
    assert qcrit(minimal5) ** 9 > W**5

    # Exact depth census. For depth 0,1,2 all choices are supported.
    c0 = 1
    c1 = len(hard)
    c2 = c1 * (c1 - 1) // 2

    # For depth 3, use increasing a<b<c and condition c*b*a^3 <= qstar.
    # Depth 4 has the same top-three condition and any fourth hard prime below a.
    c3 = 0
    c4 = 0
    for ia, a in enumerate(hard):
        for ib in range(ia + 1, len(hard)):
            b = hard[ib]
            for ic in range(ib + 1, len(hard)):
                c = hard[ic]
                if c * b * a**3 > qstar:
                    break
                c3 += 1
                c4 += ia

    assert (c0, c1, c2, c3, c4) == (1, 219, 23871, 18808, 31126)
    assert c0 + c1 + c2 + c3 + c4 == 74025

    print("P017 c515 least-shell budget correction checker: PASS")
    print("correct residual credit = one maximal pair after least shell")
    print("Q_res <= D^(1/2), floor Q* =", qstar)
    print("P23-stripped hard Rosser census =", (c0, c1, c2, c3, c4))
    print("total hard states = 74025; hard depth <=4")


if __name__ == "__main__":
    main()
