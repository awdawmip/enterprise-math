#!/usr/bin/env python3
"""Exact A3 sign-twisted S4 one-root quotient-descent regression.

Finite verification only. The all-radius theorem is proved in the accompanying
2026-11-13 Driver research note, not inferred from this finite enumeration.
"""
from itertools import permutations

E = (0, 1, 2, 3)
H = (1, 0, 2, 3)  # (12), zero-based coordinate permutation


def permutation_sign(g):
    inversions = sum(g[i] > g[j] for i in range(4) for j in range(i + 1, 4))
    return -1 if inversions % 2 else 1


def action(g, x):
    """R_g = sgn(g) P_g, using (P_g x)[g(i)] = x[i]."""
    result = [0] * 4
    sign = permutation_sign(g)
    for i, coordinate in enumerate(x):
        result[g[i]] = sign * coordinate
    return tuple(result)


def centralizes_h(g):
    return set((g[2], g[3])) == {2, 3}


def equivalent_singleton_images(g, radius):
    x = (0, 0, radius, -radius)
    left = action(g, action(H, x))
    right = action(g, x)
    return left in {right, action(H, right)}


def main():
    universe = list(permutations(E))
    assert len(universe) == 24
    centralizer = {g for g in universe if centralizes_h(g)}
    assert len(centralizer) == 4
    evaluations = 0
    for radius in range(1, 5):
        passes = {g for g in universe if equivalent_singleton_images(g, radius)}
        assert passes == centralizer, (radius, passes ^ centralizer)
        evaluations += len(universe)
        print(f"radius={radius}: passes={len(passes)} rejects={len(universe)-len(passes)}")
    assert evaluations == 96
    print("A3_SINGLE_BINARY_PROBE=PASS; EXACT_EVALUATIONS=96; CENTRALIZER_SIZE=4")


if __name__ == "__main__":
    main()
