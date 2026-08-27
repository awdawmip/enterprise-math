#!/usr/bin/env python3
"""Exact-rational regression checker for the c=103/20 second-Buchstab pair-shell reduction.

Checks the source exponents, the ordered-pair kernel, its piecewise form and
maximum under the ordering r<p, and a finite synthetic reindexing identity for
T1+T2.  This is regression evidence, not a finite P2 theorem.
"""

from fractions import Fraction as Q


def kappa(u: Q, t: Q) -> Q:
    U = Q(113, 240)
    s0 = Q(1, 6)
    return Q(1, 2) + 6 * max(Q(0), min(u, U - t) - s0)


def parameter_checks() -> None:
    U = Q(113, 240)
    s0 = Q(1, 6)
    ustar = U - s0

    assert ustar == Q(73, 240)
    assert Q(10, 9) * ustar == Q(73, 216)
    assert Q(31, 40) > ustar

    # Piece 1 can occur only if u<t<=U-u, hence 2u<U.
    # Therefore 6u-1/2 < 3U-1/2 = 73/80.
    assert 3 * U - Q(1, 2) == Q(73, 80)

    # Piece 2: t>max(u,U-u).  The smallest possible t approaches U/2,
    # so 93/40-6t is < 93/40-3U = 73/80.
    assert Q(93, 40) - 3 * U == Q(73, 80)

    # Piece 3 is exactly 1/2.
    assert Q(1, 2) < Q(73, 80)


def piecewise_checks() -> None:
    U = Q(113, 240)
    s0 = Q(1, 6)
    ustar = Q(73, 240)

    # Samples in each legal ordered region.
    samples = [
        (Q(1, 5), Q(11, 50)),   # t <= U-u
        (Q(1, 5), Q(3, 10)),    # U-u < t < ustar
        (Q(1, 4), Q(7, 25)),    # u>U/2; second branch
        (Q(1, 5), Q(1, 3)),     # t >= ustar
    ]
    for u, t in samples:
        assert s0 <= u < t < Q(31, 40)
        actual = kappa(u, t)
        if t <= U - u:
            expected = 6 * u - Q(1, 2)
        elif t < ustar and min(u, U - t) > s0:
            # In this branch ordering ensures min(u,U-t)=U-t when u<=U/2;
            # for u>U/2 and t>u, U-t<u as well.
            expected = Q(93, 40) - 6 * t
        else:
            expected = Q(1, 2)
        assert actual == expected
        assert actual <= Q(73, 80)


def synthetic_reindex() -> None:
    # Synthetic ordered primes represented only by their log_D exponents.
    # Each state has a least-prime exponent u and a set of larger-prime exponents.
    U = Q(113, 240)
    s0 = Q(1, 6)
    t1_hi = Q(31, 40)

    states = [
        (Q(1, 5), (Q(11, 50), Q(3, 10))),
        (Q(1, 4), (Q(7, 25), Q(2, 5))),
        (Q(9, 50), (Q(1, 3),)),
    ]

    # Direct T1+T2 by summing over every divisor prime p above z.
    direct = Q(0)
    for u, larger in states:
        all_primes = (u,) + larger
        for idx, t in enumerate(all_primes):
            if t < t1_hi:
                direct += Q(1, 2)
            # For T2, q_p is the least exponent remaining after deleting p.
            remaining = all_primes[:idx] + all_primes[idx + 1 :]
            sigma = min(remaining) if remaining else Q(10)
            length = min(t, U - t, sigma) - s0
            if length > 0:
                direct += 6 * length

    # Reindexed form: least-prime shells plus ordered pairs (least r, larger p).
    reindexed = Q(0)
    for u, larger in states:
        # least-shell coefficient T1 + T2
        if u < t1_hi:
            reindexed += Q(1, 2)
        length = min(u, U - u) - s0
        if length > 0:
            reindexed += 6 * length

        for t in larger:
            if t < t1_hi:
                reindexed += kappa(u, t)

    assert direct == reindexed


def main() -> None:
    parameter_checks()
    piecewise_checks()
    synthetic_reindex()
    print("P017 c515 second-Buchstab pair-shell checker: PASS")
    print("ordered-pair kernel kappa <= 73/80 under 1/6 <= u < t")
    print("dangerous first anchor u < 73/240 = W-exponent 73/216")


if __name__ == "__main__":
    main()
