#!/usr/bin/env python3
"""R718: exact integer verification of typed-axis star-local BRC pair-degree recovery.

Self-contained six-axis candidate Boolean triad model; no physical/native-event inference.
No external dependencies, no random or floating-point arithmetic.
"""
import json
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path

V = tuple(range(6))
TRIPLES = tuple(combinations(V, 3))
PAIRS = tuple(combinations(V, 2))
TI = {t: n for n, t in enumerate(TRIPLES)}
PI = {p: n for n, p in enumerate(PAIRS)}
STARS = {i: tuple(k for k, t in enumerate(TRIPLES) if i in t) for i in V}


def mask(*texts):
    return sum(1 << TI[tuple(int(c) for c in t)] for t in texts)


def ledger(h):
    d = [0] * len(PAIRS)
    for t in TRIPLES:
        if h & (1 << TI[t]):
            for e in combinations(t, 2):
                d[PI[e]] += 1
    return tuple(d)


def decode_star(h0, d1, axis):
    """Exact decoder; ValueError is an algebraic or Boolean feasibility failure."""
    d0 = ledger(h0)
    h1 = h0
    delta = {}
    other = tuple(j for j in V if j != axis)
    for j, k in combinations(other, 2):
        diff = d1[PI[j, k]] - d0[PI[j, k]]
        t = tuple(sorted((axis, j, k)))
        b = TI[t]
        old = (h0 >> b) & 1
        if old + diff not in (0, 1):
            raise ValueError("Non-Boolean axis-star transition")
        delta[j, k] = diff
        if diff:
            h1 ^= 1 << b
    for j in other:
        expected = sum(delta[tuple(sorted((j, k)))] for k in other if k != j)
        if d1[PI[tuple(sorted((axis, j)))]] - d0[PI[tuple(sorted((axis, j)))]] != expected:
            raise ValueError("Five-star consistency constraints fail")
    assert ledger(h1) == tuple(d1)
    return h1


def permute(h, p):
    return sum(1 << TI[tuple(sorted(p[k] for k in t))] for t in TRIPLES if h & (1 << TI[t]))


def run():
    assert len(TRIPLES) == 20 and len(PAIRS) == 15
    # Exhaust all 2^10 possible membership-change supports for each tagged axis.
    support_tags = Counter()
    for axis in V:
        s = STARS[axis]
        assert len(s) == 10
        for bits in range(1 << 10):
            support = sum(1 << idx for j, idx in enumerate(s) if (bits >> j) & 1)
            support_tags[support] += 1

    tag_hist = Counter(support_tags.values())
    assert dict(tag_hist) == {1: 5748, 2: 165, 3: 20, 6: 1}
    assert sum(k * n for k, n in tag_hist.items()) == 6 * (1 << 10)
    assert len(support_tags) == 5934

    h0 = mask("024", "035", "124", "135")
    h1 = mask("025", "034", "124", "135")
    h2 = mask("024", "035", "125", "134")
    assert h0 != h1 and h0 != h2 and h1 != h2
    assert (h0 ^ h1).bit_count() == (h0 ^ h2).bit_count() == 4
    assert all(0 in TRIPLES[idx] for idx in range(20) if ((h0 ^ h1) >> idx) & 1)
    assert all(1 in TRIPLES[idx] for idx in range(20) if ((h0 ^ h2) >> idx) & 1)
    assert ledger(h1) == ledger(h2)
    assert decode_star(h0, ledger(h1), 0) == h1
    assert decode_star(h0, ledger(h2), 1) == h2

    no_tag_ambiguity = {
        "H0": ["024", "035", "124", "135"],
        "axis0_H1": ["025", "034", "124", "135"],
        "axis1_H2": ["024", "035", "125", "134"],
        "D_H1_equals_D_H2": list(ledger(h1)),
        "D_H0": list(ledger(h0)),
        "both_four_changes": True,
    }

    base_masks = (0, (1 << 20) - 1, h0, h1, h2, 0x5A5A5, 0x369CF, 0xC03AD)
    checks = 0
    for base in base_masks:
        for axis in V:
            for bits in range(1 << 10):
                change = sum(1 << idx for j, idx in enumerate(STARS[axis]) if (bits >> j) & 1)
                target = base ^ change
                assert decode_star(base, ledger(target), axis) == target
                checks += 1

    for p in permutations(V):
        g0, g1, g2 = [permute(x, p) for x in (h0, h1, h2)]
        assert ledger(g1) == ledger(g2)
        assert decode_star(g0, ledger(g1), p[0]) == g1
        assert decode_star(g0, ledger(g2), p[1]) == g2

    # An algebraically impossible proposed ledger must be rejected.
    invalid = list(ledger(h1))
    invalid[PI[tuple(sorted((0, 1)))]] += 1
    try:
        decode_star(h0, invalid, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Inconsistent star ledger wrongly accepted")

    results = {
        "result": "R718_BRC_TAGGED_AXIS_STAR_LEDGER_EXACT_PASS",
        "model": "Boolean six-axis triad source states, exact integer pair-degrees",
        "frozen_scientific_input": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "triad_count": 20,
        "pair_ledger_entries": 15,
        "single_axis_star_triad_count": 10,
        "tagged_axis_transition_supports": 6144,
        "distinct_axis_local_transition_supports": 5934,
        "tag_multiplicity_histogram": {str(k): v for k, v in sorted(tag_hist.items())},
        "exhaustive_tagged_updates_on_8_fixed_baselines": checks,
        "complete_axis_permutation_witness_tests": 720,
        "unknown_tag_collision_witness": no_tag_ambiguity,
        "general_n_proof": "Direct pair-degree delta identity for pairs disjoint from tagged axis",
        "native_X6_V29_V39_correspondence": "OPEN; not asserted by this candidate test",
    }
    out = Path(__file__).with_name("R718_BRC_AXIS_STAR_LEDGER_RESULTS.json")
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(results["result"], "supports=5934", "cases=" + str(checks), "S6=720")
    return results


if __name__ == "__main__":
    run()
