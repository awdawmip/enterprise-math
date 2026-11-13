#!/usr/bin/env python3
"""Exact native signed X6 G=25 shell, source scope P000 V5 signed Z^6."""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import comb, factorial
import json

DIM = 6
G = 25


def orbit_count(absolute):
    multiplicities = {a: absolute.count(a) for a in set(absolute)}
    count = factorial(DIM)
    for n in multiplicities.values():
        count //= factorial(n)
    return count * 2 ** sum(a != 0 for a in absolute)


def path_count(absolute):
    t = sum(absolute)
    count = factorial(t)
    for a in absolute:
        count //= factorial(a)
    return count


def exact_orbits():
    out = {}
    for a in combinations_with_replacement(range(6), DIM):
        if sum(x * x for x in a) != G:
            continue
        typ = tuple(sorted((x for x in a if x), reverse=True))
        n = orbit_count(a)
        m = path_count(a)
        out[typ] = (n, m, n * m)
    return out


def independent_dynamic_program():
    states = {(0, 0): (1, 1)}  # (G,T) -> (endpoint count, word count)
    for _ in range(DIM):
        nxt = defaultdict(lambda: (0, 0))
        for (g, t), (endpoints, words) in states.items():
            for a in range(6):
                if g + a*a > G:
                    break
                k = (g + a*a, t + a)
                e, w = nxt[k]
                sign_count = 1 if a == 0 else 2
                nxt[k] = (e + endpoints * sign_count,
                          w + words * sign_count * comb(t + a, a))
        states = dict(nxt)
    return {t: counts for (g, t), counts in states.items() if g == G}


def main():
    expected = {
        (5,): (12, 1, 12),
        (4, 3): (120, 35, 4200),
        (4, 2, 2, 1): (2880, 3780, 10886400),
        (3, 2, 2, 2, 2): (960, 415800, 399168000),
        (3, 3, 2, 1, 1, 1): (3840, 554400, 2128896000),
    }
    observed = exact_orbits()
    assert observed == expected, (observed, expected)
    dp = independent_dynamic_program()
    assert dp == {5: (12, 12), 7: (120, 4200),
                  9: (2880, 10886400), 11: (4800, 2528064000)}, dp
    assert sum(v[0] for v in observed.values()) == 7812
    assert sum(v[2] for v in observed.values()) == 2538954612
    assert sum(v[0] for k, v in observed.items() if len(k) <= 2) == 132
    assert sum(v[2] for k, v in observed.items() if len(k) <= 2) == 4212
    assert 1 + 35 + 35 + 1 == 72  # historical single positive two-axis sector
    print(json.dumps({"status": "PASS_EXACT_FINITE_G25_SHELL",
                      "dimension": DIM, "native_norm_square": G,
                      "orbit_types": len(observed),
                      "signed_native_endpoints": 7812,
                      "signed_primitive_minimal_BRC_words": 2538954612,
                      "length_distribution": {str(t): [n, w] for t, (n, w) in sorted(dp.items())},
                      "support_le_2": {"endpoints": 132, "words": 4212}},
                     ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
