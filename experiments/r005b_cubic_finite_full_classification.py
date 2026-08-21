#!/usr/bin/env python3
"""Exact finite cubic full-forcing classification certificate for R005-B.

This artifact performs two independent upper-band checks:

1. direct prime-sieve classification for k<=5501;
2. scale-dependent maximal-record-gap closure for 5502<=k<=5,848,035.

It consumes Supplement 15's lower-band closure as a separate premise.  The
record-gap staircase is frozen from the Prime Gap List project's confirmed
maximal-gap table as consulted on 2026-08-10; it is external computational data,
not an Enterprise Math theorem.
"""

from __future__ import annotations

import argparse
import bisect
import json
from math import isqrt


# (gap start, maximal gap size from this start onward until the next record).
# Only records needed through F_3(5,848,035) are retained; the next record start
# 20,678,048,297 lies beyond the endpoint horizon 14,142,137,522.
RECORD_GAPS = [
    (2, 1), (3, 2), (7, 4), (23, 6), (89, 8), (113, 14),
    (523, 18), (887, 20), (1129, 22), (1327, 34), (9551, 36),
    (15683, 44), (19609, 52), (31397, 72), (155921, 86),
    (360653, 96), (370261, 112), (492113, 114), (1349533, 118),
    (1357201, 132), (2010733, 148), (4652353, 154),
    (17051707, 180), (20831323, 210), (47326693, 220),
    (122164747, 222), (189695659, 234), (191912783, 248),
    (387096133, 250), (436273009, 282), (1294268491, 288),
    (1453168141, 292), (2300942549, 320), (3842610773, 336),
    (4302407359, 354), (10726904659, 382), (20678048297, 384),
]

EXPECTED_EXCEPTIONS = {
    23: [109],
    64: [509],
    120: [1303, 1307],
    138: [1621],
    1005: [31859],
}


def factor_horizon(k: int) -> int:
    return isqrt((k + 1) ** 3 - 1)


def lower_root(k: int) -> int:
    return isqrt(k**3)


def sieve_primes(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if not sieve[p]:
            continue
        start = p * p
        count = (limit - start) // p + 1
        sieve[start : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def record_gap_cap(x: int) -> int:
    starts = [item[0] for item in RECORD_GAPS]
    i = bisect.bisect_right(starts, x) - 1
    if i < 0:
        return 0
    return RECORD_GAPS[i][1]


def upper_closed_by_cap(k: int, gap_cap: int) -> bool:
    f = factor_horizon(k)
    s = lower_root(k)
    u = (k + 1) ** 3 - 1
    return (f + gap_cap) * s <= u


def direct_upper_exceptions(k_limit: int) -> dict[int, list[int]]:
    max_f = factor_horizon(k_limit)
    # A small buffer guarantees one successor prime beyond the last horizon.
    primes = sieve_primes(max_f + 10_000)
    result: dict[int, list[int]] = {}
    for k in range(2, k_limit + 1):
        a = k**3
        u = (k + 1) ** 3 - 1
        f = factor_horizon(k)
        s = lower_root(k)
        q_index = bisect.bisect_right(primes, s) - 1
        r_index = bisect.bisect_right(primes, f)
        q_max = primes[q_index]
        r = primes[r_index]
        if not (q_max * f > a and q_max * r > u):
            continue
        lo = max(a // f, u // r) + 1
        left = bisect.bisect_left(primes, lo)
        right = bisect.bisect_right(primes, s)
        result[k] = primes[left:right]
    return result


def last_record_cap_uncertified(k_limit: int) -> int:
    last = 0
    for k in range(2, k_limit + 1):
        f = factor_horizon(k)
        if not upper_closed_by_cap(k, record_gap_cap(f)):
            last = k
    return last


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k-limit", type=int, default=5_848_035)
    parser.add_argument("--direct-limit", type=int, default=5_501)
    parser.add_argument("--assert-current-certificate", action="store_true")
    args = parser.parse_args()

    exceptions = direct_upper_exceptions(args.direct_limit)
    last_cap_uncertified = last_record_cap_uncertified(args.k_limit)
    endpoint_f = factor_horizon(args.k_limit)
    result = {
        "k_limit": args.k_limit,
        "direct_limit": args.direct_limit,
        "endpoint_factor_horizon": endpoint_f,
        "last_record_cap_uncertified_k": last_cap_uncertified,
        "direct_upper_nonforcing_exceptions": exceptions,
    }

    if args.assert_current_certificate:
        assert args.k_limit == 5_848_035
        assert args.direct_limit == 5_501
        assert endpoint_f == 14_142_137_522
        assert last_cap_uncertified == 5_501
        assert exceptions == EXPECTED_EXCEPTIONS
        result["certificate"] = "PASS"

    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
