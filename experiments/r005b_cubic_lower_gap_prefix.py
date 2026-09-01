#!/usr/bin/env python3
"""Exact prefix certificate for cubic cube-root-supercritical prime gaps.

The certificate scans every consecutive prime gap with left endpoint below the
chosen limit and reports those satisfying

    gap^3 > 27 * left_prime.

This is the scale-free necessary condition for a cubic lower cofactor-gap e=1
failure derived in R005-B.  The default full checkpoint limit 190,000,000 is
just above ceil(1724^3/27), the cutoff used with the 2026 Prime Gap List
external gap cap.

The sieve uses only Python's standard library and a bytearray.  No floating
point value is used in the certificate predicate.
"""

from __future__ import annotations

import argparse
import json
from math import isqrt


def scan_supercritical_gaps(limit: int) -> tuple[int, list[tuple[int, int, int]]]:
    if limit < 3:
        return 0, []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if not sieve[p]:
            continue
        start = p * p
        count = (limit - start) // p + 1
        sieve[start : limit + 1 : p] = b"\x00" * count

    prime_count = 0
    previous = None
    hits: list[tuple[int, int, int]] = []
    for n in range(2, limit + 1):
        if not sieve[n]:
            continue
        prime_count += 1
        if previous is not None:
            gap = n - previous
            if gap**3 > 27 * previous:
                hits.append((previous, n, gap))
        previous = n
    return prime_count, hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=190_000_000)
    parser.add_argument(
        "--assert-current-certificate",
        action="store_true",
        help="assert the frozen R005-B 190,000,000-prefix certificate",
    )
    args = parser.parse_args()

    prime_count, hits = scan_supercritical_gaps(args.limit)
    result = {
        "limit": args.limit,
        "prime_count": prime_count,
        "cube_root_supercritical_gaps": hits,
    }

    if args.assert_current_certificate:
        if args.limit != 190_000_000:
            raise SystemExit("--assert-current-certificate requires --limit 190000000")
        assert prime_count == 10_555_473
        assert hits == [(1327, 1361, 34)]
        result["certificate"] = "PASS"

    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
