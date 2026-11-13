#!/usr/bin/env python3
"""R121-LIT: exact rational-geometry count cross-check against Sturmian totients."""
import json
from math import gcd
from pathlib import Path
from check_r121 import patterns


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n+1))


def known_count(m):
    return 1 + sum((m-r)*phi(r) for r in range(1, m))


def run():
    observed = {}
    for m in range(2, 14):
        value = len(patterns(m))
        assert value == known_count(m), (m, value, known_count(m))
        observed[str(m)] = value
    return {"status": "R121_STURMIAN_COUNT_CROSSCHECK_PASS", "m_range": [2,13], "exact_cases": len(observed), "pattern_counts": observed, "enumeration_method": "fractional rational line arrangement", "formula_source": "OEIS A005598 / Mignosi 1991 / Berstel-Pocchiola 1993"}


if __name__ == "__main__":
    result=run()
    print(result['status'], result['exact_cases'], result['pattern_counts'])
    with Path(__file__).with_name('verification_r121_count.json').open('w') as f:
        json.dump(result, f, sort_keys=True, indent=2)
