#!/usr/bin/env python3
"""R762CD complete finite verification; Python 3.10+, standard library only.

Twelve Boolean atoms: 4 closure bits and 8 rooted gate bits.
These are model-law queries, not a physical TRIADIC_CLOSURE_E oracle.
"""
import json
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product

R = (1, 1, 3, 3)
W = (1, 1, 3, 3)
OPTIONS = [((0, 0),) + tuple((1, m) for m in range(1 << r)) for r in R]


def make_laws():
    laws = []
    for orbit_options in product(*OPTIONS):
        n = [0] * 4
        for (closed, mask), weight in zip(orbit_options, W):
            if closed:
                n[mask.bit_count()] += weight
        bits = tuple(c for c, _ in orbit_options) + tuple(
            (mask >> j) & 1
            for (_, mask), r in zip(orbit_options, R)
            for j in range(r)
        )
        sector = tuple(-1 if not c else mask.bit_count()
                       for c, mask in orbit_options)
        gates = tuple(mask for _, mask in orbit_options)
        laws.append((orbit_options, tuple(n), sector, gates, bits))
    assert len(laws) == 729
    assert len({x[4] for x in laws}) == 729
    return laws


def group(laws, index):
    groups = defaultdict(list)
    for i, law in enumerate(laws):
        groups[law[index]].append(i)
    return groups


def analyze(laws, groups):
    positive_sets = [
        frozenset(i for i, law in enumerate(laws) if law[4][j])
        for j in range(12)
    ]

    @lru_cache(None)
    def adaptive(ids):
        if len(ids) == 1:
            return 0
        best = 13
        for pos in positive_sets:
            yes = ids & pos
            if not yes or yes == ids:
                continue
            no = ids - yes
            best = min(best, 1 + max(adaptive(yes), adaptive(no)))
            # Proven information-theoretic lower bound for |ids| binary leaves
            if best == (len(ids) - 1).bit_length():
                break
        assert best <= 12
        return best

    def static(ids):
        for k in range(13):
            for coords in combinations(range(12), k):
                signatures = {
                    tuple(laws[i][4][j] for j in coords) for i in ids
                }
                if len(signatures) == len(ids):
                    assert len(set(signatures)) == len(ids)
                    return k, coords
        raise AssertionError("Twelve bits must identify the complete law")

    A_depths, N_depths, gains = [], [], []
    certificates = {}
    witness = {}
    for key, ids in groups.items():
        a = adaptive(frozenset(ids))
        n, coordinates = static(ids)
        assert a <= n
        A_depths.append(a)
        N_depths.append(n)
        gains.append(n - a)
        certificates[str(key)] = sum(1 << j for j in coordinates)
        if key in ((0, 3, 0, 0), (4, 3, 0, 0)):
            witness[str(key)] = {
                "fiber": len(ids), "adaptive": a, "nonadaptive": n
            }
    return {
        "adaptive_depth_histogram": dict(sorted(Counter(A_depths).items())),
        "nonadaptive_depth_histogram": dict(sorted(Counter(N_depths).items())),
        "adaptivity_gain_histogram": dict(sorted(Counter(gains).items())),
        "worst_adaptive": max(A_depths),
        "worst_nonadaptive": max(N_depths),
        "maximum_adaptivity_gain": max(gains),
        "recursive_subproblems": adaptive.cache_info().currsize,
        "witnesses": witness,
        "query_masks": certificates if len(groups) == 90 else None,
    }


def main():
    laws = make_laws()
    observers = {
        "A": group(laws, 1),
        "S": group(laws, 2),
        "E": group(laws, 3),
    }
    expected = {
        "A": (90, {1: 9, 2: 18, 4: 9, 6: 18, 9: 6,
                   12: 18, 18: 9, 36: 3}),
        "S": (225, {1: 81, 3: 108, 9: 36}),
        "E": (256, {1: 49, 2: 112, 4: 78, 8: 16, 16: 1}),
    }
    output = {}
    for key, classes in observers.items():
        histogram = dict(sorted(Counter(map(len, classes.values())).items()))
        count, expected_hist = expected[key]
        assert len(classes) == count and histogram == expected_hist
        assert sum(size * frequency for size, frequency
                   in histogram.items()) == 729
        census = analyze(laws, classes)
        output[key] = {
            "classes": count,
            "fiber_histogram": histogram,
            "max_fiber": max(histogram),
            "fixed_repair_bits": (max(histogram) - 1).bit_length(),
            **census,
        }
    assert [output[k]["fixed_repair_bits"] for k in "ASE"] == [6, 4, 4]
    assert [output[k]["worst_adaptive"] for k in "ASE"] == [6, 4, 4]
    assert [output[k]["worst_nonadaptive"] for k in "ASE"] == [6, 4, 4]
    assert output["A"]["witnesses"]["(0, 3, 0, 0)"] == {
        "fiber": 6, "adaptive": 3, "nonadaptive": 5
    }
    assert output["A"]["witnesses"]["(4, 3, 0, 0)"] == {
        "fiber": 12, "adaptive": 6, "nonadaptive": 6
    }
    assert output["A"]["adaptivity_gain_histogram"] == {
        0: 66, 1: 18, 2: 6
    }
    result = {
        "schema": "ENTERPRISE_MATH_R762CD_POLICY_FIBER_REPAIR_V1",
        "scope": "Conditional 729-law S6xC3 sign-only triadic model",
        "native_event_license_established": False,
        "law_count": 729,
        "root_count": list(R),
        "sign_orbit_weight": list(W),
        "atom_order": "C0,C1,C2,C3,g00,g10,g20,g21,g22,g30,g31,g32",
        "observers": output,
        "complete_J": {
            "classes": 729, "max_fiber": 1, "fixed_repair_bits": 0,
            "worst_adaptive": 0, "worst_nonadaptive": 0
        },
        "verification": "Complete exact enumeration and dynamic decision-tree minimax; exhaustive fixed-query search",
        "independent_review": "NOT_REVIEWED",
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
