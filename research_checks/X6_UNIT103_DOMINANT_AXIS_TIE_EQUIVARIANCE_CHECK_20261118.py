#!/usr/bin/env python3
"""Exact finite S3-covariance certificate for the X6 signed slice axis-selector boundary.

This is a new bounded checker, not a replay of frozen native benchmarks.
"""
from itertools import permutations, product
import json

AXES = (0, 1, 2)
PERMS = tuple(permutations(AXES))


def permute(d, p):
    """Coordinate j after action comes from old coordinate p[j]."""
    return tuple(d[p[j]] for j in AXES)


def tied_signed_directions(d):
    m = max(map(abs, d))
    if m == 0:
        return ()
    return tuple((i, 1 if d[i] > 0 else -1) for i in AXES if abs(d[i]) == m)


def rename_signed_directions(directions, p):
    return tuple(sorted((p.index(i), sign) for i, sign in directions))


def count_minimal_words(d):
    from math import factorial
    n = sum(map(abs, d))
    ans = factorial(n)
    for x in d:
        ans //= factorial(abs(x))
    return ans


def require(predicate, message):
    if not predicate:
        raise RuntimeError(message)


def main():
    counts = {"zero": 0, "unique": 0, "two_way_tie": 0, "three_way_tie": 0}
    equivariance_checks = 0
    reversal_checks = 0
    for d in product(range(-2, 3), repeat=3):
        a = tied_signed_directions(d)
        k = len(a)
        counts[{0:"zero", 1:"unique", 2:"two_way_tie", 3:"three_way_tie"}[k]] += 1
        for p in PERMS:
            b = tied_signed_directions(permute(d, p))
            require(tuple(sorted(b)) == rename_signed_directions(a, p),
                    f"S3 covariance failed: {d}, {p}")
            equivariance_checks += 1
        reverse = tied_signed_directions(tuple(-x for x in d))
        require(reverse == tuple((i, -sign) for i, sign in a),
                f"reversal covariance failed: {d}")
        reversal_checks += 1
    witness = (1, 1, 0)
    swap = (1, 0, 2)
    require(permute(witness, swap) == witness, "wrong stabilizer witness")
    require(tied_signed_directions(witness) == ((0, 1), (1, 1)),
            "wrong two-axis signed candidates")
    require(count_minimal_words(witness) == 2, "wrong tied path count")
    # A single-valued equivariant selector would be fixed by the stabilizer swap,
    # but neither allowed maximizer index 0 nor 1 is fixed by that swap.
    require(all(swap.index(i) != i for i in (0, 1)), "witness has a fixed candidate")
    require(tied_signed_directions((0, 0, 0)) == (), "zero has a direction")
    print(json.dumps({
        "schema":"X6_UNIT103_DOMINANT_AXIS_TIE_EQUIVARIANCE_FINITE_V1",
        "domain":"signed triples [-2,2]^3",
        "counts":counts,
        "s3_permutation_count":len(PERMS),
        "equivariance_checks":equivariance_checks,
        "reversal_checks":reversal_checks,
        "stabilizer_witness":{"d":witness,"swap":swap,"candidate_signed_axes":tied_signed_directions(witness),"shortest_path_multiplicity":2},
        "theorem":"no globally S3-equivariant single-valued dominant-axis selector on nonzero signed triples",
        "finite_check_status":"PASS",
    },sort_keys=True,separators=(",",":")))


if __name__ == "__main__":
    main()
