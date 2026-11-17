#!/usr/bin/env python3
"""R762DB: exact positive N-BRC adaptive sample-tree checker.

Python 3 stdlib only. Every named microbranch is one entry in 'steps'.
Repeated increments retain their independent microbranch identities.
"""
import json
from collections import Counter
from itertools import permutations, product
from functools import reduce
from math import gcd


def brc_counts(elements, mul, identity, steps, h):
    out = [{x: int(x == identity) for x in elements}]
    for _ in range(h):
        nxt = {x: 0 for x in elements}
        for x in elements:
            for a in steps:
                nxt[mul(x, a)] += out[-1][x]
        out.append(nxt)
    return out


def cgcd(values):
    return reduce(gcd, values, 0)


def simulate(elements, mul, inv, identity, steps, horizon, policy):
    """Independently enumerate named microbranch words and exact leaf counts."""
    D = len(steps)
    C = brc_counts(elements, mul, identity, steps, horizon)
    actual = Counter()
    for word in product(steps, repeat=horizon):
        history = []
        states = [identity]
        for a in word:
            states.append(mul(states[-1], a))
        while True:
            t = policy(tuple(history), horizon)
            if t is None:
                break
            assert 0 < t <= horizon and (not history or t > history[-1][0])
            history.append((t, states[t]))
        actual[tuple(history)] += 1
    predicted = {}
    for leaf in actual:
        previous_t, previous_x, weight = 0, identity, 1
        for t, x in leaf:
            increment = mul(inv(previous_x), x)
            weight *= C[t - previous_t][increment]
            previous_t, previous_x = t, x
        predicted[leaf] = weight * D ** (horizon - previous_t)
    assert actual == Counter(predicted), (horizon, policy.__name__)
    assert sum(actual.values()) == D ** horizon
    g = cgcd(actual.values())
    return {"leaves": len(actual), "numerator_gcd": g,
            "minimum_uniform_seeds": D ** horizon // g,
            "paths": D ** horizon}


def policies():
    def marked(x):
        return x == 1 or x == (1, 0, 2)

    def final_only(hist, H):
        return H if not hist else None

    def first_last(hist, H):
        return 1 if not hist else H if len(hist) == 1 else None

    def fixed_three(hist, H):
        return (1 if not hist else 3 if len(hist) == 1 else H if len(hist) == 2 else None)

    def adaptive_optional(hist, H):
        if not hist:
            return 1
        if len(hist) == 1:
            return 3 if marked(hist[0][1]) else H
        return H if hist[-1][0] != H else None

    def adaptive_early(hist, H):
        if not hist:
            return 1
        return H if len(hist) == 1 and not marked(hist[0][1]) else None

    def optional_by_first(hist, H):
        if not hist:
            return 1
        if len(hist) == 1:
            return 2 if marked(hist[0][1]) else H
        return H if hist[-1][0] != H else None

    def adaptive_twice(hist, H):
        if not hist:
            return 1
        if len(hist) == 1:
            return 3
        if len(hist) == 2:
            return 4 if hist[-1][1] == hist[0][1] else H
        return H if hist[-1][0] != H else None

    return [final_only, first_last, fixed_three, adaptive_optional,
            adaptive_early, optional_by_first, adaptive_twice]


def c3():
    elems = tuple(range(3))
    return elems, lambda x, y: (x + y) % 3, lambda x: (-x) % 3, 0


def s3():
    elems = tuple(permutations(range(3)))
    ident = (0, 1, 2)
    def mul(x, y):
        return tuple(x[y[i]] for i in range(3))
    def inv(x):
        return tuple(x.index(i) for i in range(3))
    return elems, mul, inv, ident


def run():
    results = []
    checked_words = 0
    checked_leaf_equalities = 0
    for name, setup in (("C3", c3()), ("S3", s3())):
        elements, mul, inv, identity = setup
        if name == "C3":
            families = [(p, q, (1,) * p + (2,) * q)
                        for p in (1, 2, 3) for q in (1, 2, 3)]
        else:
            u, v = (1, 0, 2), (1, 2, 0)
            families = [(p, q, (u,) * p + (v,) * q)
                        for p in (1, 2) for q in (1, 2)]
        for p, q, steps in families:
            for H in (4, 5, 6):
                for policy in policies():
                    res = simulate(elements, mul, inv, identity, steps, H, policy)
                    checked_words += res["paths"]
                    checked_leaf_equalities += res["leaves"]
                    results.append((name, p, q, H, policy.__name__, res))
    demo_rows = [r for r in results if r[:4] == ("C3", 1, 2, 6)]
    demo = {r[4]: r[5] for r in demo_rows}
    assert demo["first_last"]["minimum_uniform_seeds"] == 81
    assert demo["fixed_three"]["minimum_uniform_seeds"] == 243
    assert demo["adaptive_optional"]["minimum_uniform_seeds"] == 243
    assert demo["adaptive_optional"]["numerator_gcd"] == 3
    assert demo["adaptive_optional"]["leaves"] == 12
    for name,p,q,H,policy_name,res in results:
        if policy_name == "adaptive_optional":
            base = next(z[5] for z in results
                        if z[:4] == (name,p,q,H) and z[4] == "first_last")
            assert res["minimum_uniform_seeds"] % base["minimum_uniform_seeds"] == 0
    report = {
        "schema": "EM_R762DB_EXACT_ADAPTIVE_POSITIVE_BRC_EVIDENCE_V1",
        "task_id": "RS-X6-TRIADIC-CLOSURE-DYNAMICS",
        "scientific_scope": "conditional finite-group positive integer named-microbranch N-BRC; no native TRIADIC_CLOSURE_E event admission",
        "arithmetic": "exact nonnegative arbitrary-precision integers; direct enumeration of D^h named microbranch paths",
        "group_families": {"C3": "p,q=1..3; step +1 count p, step -1 count q",
                           "S3": "p,q=1..2; two named permutations with right-product"},
        "horizons": [4, 5, 6],
        "adaptive_policy_count": len(policies()),
        "configuration_count": len(results),
        "enumerated_microbranch_paths": checked_words,
        "observed_leaf_numerators_compared": checked_leaf_equalities,
        "all_checks": "PASS",
        "distinguished_C3_p1_q2_H6": demo,
        "identity": "Each adaptive leaf has exact numerator D^(H-t_leaf) * product C_gap(x_previous^-1*x_current)",
        "minimum_seeds": "D^H/gcd of adaptive leaf numerators",
        "independent_review": "NOT_REVIEWED"
    }
    print(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False))
    return report


if __name__ == '__main__':
    run()
