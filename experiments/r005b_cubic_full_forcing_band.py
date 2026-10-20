#!/usr/bin/env python3
"""Exact finite certificate for the R005-B cubic full-forcing band.

The certificate combines:

1. a lower-band closure endpoint supplied as an input (currently 5,848,035
   from Supplement 15's prime-gap prefix/external transfer), and
2. an integer scan of the upper closing inequality

       (F_3(k)+G) * floor(sqrt(k^3)) <= (k+1)^3-1.

The scan uses no primality oracle because G is an external uniform prime-gap cap.
For the conservative R005-A upper premise G=1328, the last k not automatically
closed is 783,190.
"""

from __future__ import annotations

import argparse
import json
from math import isqrt


def factor_horizon_cubic(k: int) -> int:
    return isqrt((k + 1) ** 3 - 1)


def upper_closed(k: int, gap_cap: int) -> bool:
    u = (k + 1) ** 3 - 1
    s = isqrt(k**3)
    f = factor_horizon_cubic(k)
    return (f + gap_cap) * s <= u


def last_not_closed(k_limit: int, gap_cap: int) -> int:
    last = 0
    for k in range(1, k_limit + 1):
        if not upper_closed(k, gap_cap):
            last = k
    return last


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k-limit", type=int, default=5_848_035)
    parser.add_argument("--upper-gap-cap", type=int, default=1328)
    parser.add_argument("--assert-current-certificate", action="store_true")
    args = parser.parse_args()

    last = last_not_closed(args.k_limit, args.upper_gap_cap)
    result = {
        "k_limit": args.k_limit,
        "upper_gap_cap": args.upper_gap_cap,
        "last_k_not_closed_by_cap": last,
        "certified_upper_closed_start": last + 1,
        "certified_full_band_if_lower_closed_through_k_limit": [last + 1, args.k_limit],
    }

    if args.assert_current_certificate:
        assert args.k_limit == 5_848_035
        assert args.upper_gap_cap == 1328
        assert last == 783_190
        result["certificate"] = "PASS"

    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
