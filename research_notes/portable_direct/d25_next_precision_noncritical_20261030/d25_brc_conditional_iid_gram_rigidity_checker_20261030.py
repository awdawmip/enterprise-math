#!/usr/bin/env python3
"""Exact positive-integer BRC checks for common-label / private-noise rigidity."""
import itertools
import json
from collections import Counter
from pathlib import Path

Y = (0, 1)
X = (0, 1, 2)
C = {0: 0, 1: 0, 2: 1}
B = (0, 1)
PRIVATE = ((2, 0), (1, 1), (0, 2))


def private_row(v, x, b):
    return v[b * len(X) + x]


def k1(v, x):
    return tuple(sum(private_row(v, x, b)[a] for b in B) for a in Y)


def k2(v, x, z):
    return tuple(sum(private_row(v, x, b)[a] * private_row(v, z, b)[c]
                     for b in B) for a in Y for c in Y)


def strong_lump(v, arity):
    groups = {}
    for xs in itertools.product(X, repeat=arity):
        obs = tuple(C[x] for x in xs)
        if arity == 1:
            row = k1(v, xs[0])
        else:
            row = k2(v, xs[0], xs[1])
        if obs in groups and groups[obs] != row:
            return False
        groups[obs] = row
    return True


def gram_defect(v, x, rep):
    return sum((k2(v, x, x)[a * 2 + a]
                + k2(v, rep, rep)[a * 2 + a]
                - 2 * k2(v, x, rep)[a * 2 + a]) for a in Y)


def level_lump(v):
    return all(private_row(v, 0, b) == private_row(v, 1, b) for b in B)


def exhaustive_iid():
    classes = Counter()
    evaluations = 0
    for v in itertools.product(PRIVATE, repeat=len(X) * len(B)):
        one = strong_lump(v, 1)
        two = strong_lump(v, 2)
        level = level_lump(v)
        defect = gram_defect(v, 1, 0)
        assert defect == sum((private_row(v, 1, b)[a] - private_row(v, 0, b)[a]) ** 2
                             for b in B for a in Y)
        assert (defect == 0) == level == two
        assert not two or one
        classes[(one, two, level)] += 1
        evaluations += 1
    assert evaluations == 3 ** 6 == 729
    assert sum(classes.values()) == 729
    assert classes[(True, True, True)] == 81
    return {"configurations": evaluations, "classifications": {
        "/".join(map(str, k)): val for k, val in sorted(classes.items())},
        "two_copy_safe": classes[(True, True, True)]}


STATES = ('a', 'b', 'c')
O = {'a': 0, 'b': 0, 'c': 1}


def single_private(x, shared):
    if x == 'c':
        return (4, 4)
    high = ((x == 'a') == (shared == 0))
    return (2, 6) if high else (6, 2)


def correlated_row(x, z, shared):
    """Output order (00,01,10,11), exactly 8 private pair paths per shared label."""
    if x == 'c' or z == 'c':
        vx, vz = single_private(x, shared), single_private(z, shared)
        return tuple(vx[a] * vz[b] // 8 for a in Y for b in Y)
    high_x = single_private(x, shared)[1] == 6
    high_z = single_private(z, shared)[1] == 6
    if high_x and high_z:
        return (0, 2, 2, 4)
    if not high_x and not high_z:
        return (4, 2, 2, 0)
    if high_x:
        return (2, 0, 4, 2)
    return (2, 4, 0, 2)


def correlated_example():
    for x, z, b in itertools.product(STATES, STATES, B):
        row = correlated_row(x, z, b)
        assert sum(row) == 8
        assert tuple(row[0 * 2 + t] + row[1 * 2 + t] for t in Y) == single_private(z, b)
        assert tuple(row[t * 2 + 0] + row[t * 2 + 1] for t in Y) == single_private(x, b)
        if x == 'c' or z == 'c':
            assert all(single_private(x, b)[a] * single_private(z, b)[c] % 8 == 0
                       for a in Y for c in Y)
        mixed = tuple(sum(correlated_row(x, z, bb)[i] for bb in B) for i in range(4))
        assert mixed == (4, 4, 4, 4)
    assert single_private('a', 0) != single_private('b', 0)
    assert tuple(sum(single_private(x, b)[a] for b in B) for a in Y) == (8, 8)
    return {
        "states": list(STATES), "observer": O, "branch_weights": [1, 1],
        "private_paths_per_shared_label_per_pair": 8,
        "all_pairs_mixed_kernel": [4, 4, 4, 4],
        "different_single_private_b0": {"a": list(single_private('a', 0)),
                                         "b": list(single_private('b', 0))},
        "example_joint_rows": {
            "aa_b0": list(correlated_row('a', 'a', 0)),
            "aa_b1": list(correlated_row('a', 'a', 1)),
            "ab_b0": list(correlated_row('a', 'b', 0)),
            "ab_b1": list(correlated_row('a', 'b', 1))},
        "pair_marginal_and_lumpability_assertions": 18
    }


def main():
    proof_check = exhaustive_iid()
    dependent = correlated_example()
    result = {
        "status": "PASS", "date": "2026-10-30", "type": "AUTHOR_EXACT_INTEGER_CHECK",
        "model": "auxiliary finite branch system; not native X6",
        "conditional_independence_enumeration": proof_check,
        "correlated_private_path_counterexample": dependent,
        "scope": "Finite enumeration only; mathematical generality supplied by separate Gram proof"}
    path = Path(__file__).with_name('d25_brc_conditional_iid_gram_rigidity_author_check_20261030.json')
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()