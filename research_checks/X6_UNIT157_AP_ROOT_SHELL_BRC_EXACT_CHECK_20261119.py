#!/usr/bin/env python3
"""Reproducible exact integer check for X6 Unit157.

Frozen semantics: A_p roots e_i-e_j and signed-native axes +/-e_i.
Independent reconstructed algorithms; does NOT invoke historical test modules.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb
import json


def check(actual, expected, label):
    if actual != expected:
        raise ValueError(f"{label}: actual={actual!r}; expected={expected!r}")


def radius(x):
    check(sum(x), 0, "zero-sum")
    return sum(t for t in x if t > 0)


def root_dp(n, m):
    d = {(0,) * n: 1}
    for k in range(1, m + 1):
        e = defaultdict(int)
        for x, v in d.items():
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    y = list(x)
                    y[i] += 1
                    y[j] -= 1
                    y = tuple(y)
                    if radius(y) == k:
                        e[y] += v
        d = dict(e)
    return d


@lru_cache(None)
def native_dp(x):
    if all(v == 0 for v in x):
        return 1
    total = 0
    for i, v in enumerate(x):
        if v:
            y = list(x)
            y[i] -= 1 if v > 0 else -1
            total += native_dp(tuple(y))
    return total


def surj(m, a):
    return sum((-1)**j * comb(a, j) * (a-j)**m for j in range(a+1))


def weighted(n, m):
    if m == 0:
        return 1
    return sum(comb(n, a) * comb(n-a, b) * surj(m, a) * surj(m, b)
               for a in range(1, min(n, m)+1)
               for b in range(1, min(n-a, m)+1))


def frozen_shell(p, m):
    if m == 0:
        return 1
    return sum(comb(p, j)**2 * comb(m-j+p-1, p-1)
               for j in range(min(p, m)+1))


def run():
    rows = []
    checks = 0
    for p in range(1, 6):
        for m in range(5):
            d = root_dp(p+1, m)
            check(len(d), frozen_shell(p, m), "frozen shell")
            ways = sum(d.values())
            check(ways, weighted(p+1, m), "surjection shell")
            factor = comb(2*m, m)
            native_sum = 0
            for x, w in d.items():
                actual = native_dp(x)
                check(actual, factor*w, "native endpoint shuffle")
                native_sum += actual
                checks += 1
            check(native_sum, factor*ways, "native weighted shell")
            rows.append({"p":p, "m":m, "endpoints":len(d),
                         "root_words":ways, "native_words":native_sum,
                         "shuffle_factor":factor})
    return {"schema":"X6_UNIT157_ROOT_SHELL_BRC_RECHECK_V1",
            "rows": rows, "checked_endpoints": checks,
            "original_historical_tests_run": False}


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, separators=(",", ":")))
