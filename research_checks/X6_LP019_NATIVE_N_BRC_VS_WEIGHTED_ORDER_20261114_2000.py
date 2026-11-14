#!/usr/bin/env python3
"""Exact two-shortest-word X6 N-BRC versus signed-weight discriminator.

This is a new bounded test, not a rerun of a historical R063 native benchmark.
"""
from itertools import combinations, permutations, product
from math import factorial


def positive_shortest_mass(d):
    magnitudes = [abs(c) for c in d]
    n = sum(magnitudes)
    numerator = factorial(n)
    for c in magnitudes:
        numerator //= factorial(c)
    return numerator


def run():
    tested = 0
    for i, j in combinations(range(6), 2):
        for sign_i, sign_j in product((-1, +1), repeat=2):
            d = [0] * 6
            d[i], d[j] = sign_i, sign_j
            letters = ((i, sign_i), (j, sign_j))
            words = tuple(permutations(letters))
            assert len(words) == len(set(words)) == 2
            # Weights require an explicitly chosen order character,
            # not merely opposite displacement signs.
            weights = tuple(+1 if w[0][0] < w[1][0] else -1 for w in words)
            assert set(weights) == {-1, +1}
            assert sum(weights) == 0
            assert positive_shortest_mass(d) == len(words) == 2
            reverse = [-x for x in d]
            assert positive_shortest_mass(reverse) == 2
            assert positive_shortest_mass(d) + positive_shortest_mass(reverse) == 4
            tested += 1
    assert tested == 60
    print("PASS_X6_LP019_NATIVE_N_BRC_VS_EXPLICIT_SIGNED_ORDER_WEIGHT", tested)


if __name__ == "__main__":
    run()
