#!/usr/bin/env python3
"""Deterministic post-10^10 cubic horizontal cursor certificate.

The frozen reference block checks every prime-q database-overflow state for

    10^10 < k <= 10^10 + 2000

using only the published 12-base strong-pseudoprime bound for primality.
No BPSW/probabilistic fallback is used.
"""

from __future__ import annotations

import argparse
import json

from enterprise_math.prime_cubic_horizontal_cursor import verify_cursor_block


BOUNDARY_K = 10_000_000_000
COVERAGE_LIMIT = 10**20
FROZEN_OFFSET = 2000
FROZEN_STATS = {
    "states": 161_846,
    "distinct_q_primes": 236,
    "max_search_offset": 523,
    "min_slack": 29_999_993_957,
    "max_cofactor_prime": 100_000_039_890_003_978_139,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offset", type=int, default=FROZEN_OFFSET)
    parser.add_argument("--assert-frozen", action="store_true")
    args = parser.parse_args()

    if args.offset < 1:
        raise SystemExit("offset must be positive")

    stats = verify_cursor_block(
        BOUNDARY_K + 1,
        BOUNDARY_K + args.offset,
        coverage_limit=COVERAGE_LIMIT,
    )
    report = {
        "boundary_k": BOUNDARY_K,
        "last_k": BOUNDARY_K + args.offset,
        "coverage_limit": COVERAGE_LIMIT,
        **stats,
    }

    if args.assert_frozen:
        if args.offset != FROZEN_OFFSET:
            raise AssertionError("--assert-frozen requires --offset 2000")
        for key, value in FROZEN_STATS.items():
            if stats[key] != value:
                raise AssertionError((key, stats[key], value))

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
