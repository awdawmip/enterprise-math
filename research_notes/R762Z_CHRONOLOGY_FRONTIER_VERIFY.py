#!/usr/bin/env python3
"""Exact resource/preemption DP for labelled cyclic PASS macros with fixed first-start order.
No external dependencies. Validation is complete on the declared finite domains.
"""
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

INF = 10 ** 9


def optimal_interruptions(q, roots, initial_inventory):
    """Minimum interruptions among all legal edge shuffles.

    Each C_r uses edges r->r+1,...,r+q-1->r (mod q).
    First starts must be in listed order. A switch from an incomplete
    previous macro to another macro costs one; completed switches cost zero.
    """
    roots = tuple(roots)
    initial_inventory = tuple(initial_inventory)
    k = len(roots)
    assert q >= 2 and k >= 1 and len(initial_inventory) == q
    assert min(initial_inventory) >= 0
    assert all(0 <= r < q for r in roots)

    @lru_cache(maxsize=None)
    def solve(progress, last_macro):
        if all(p == q for p in progress):
            return 0
        first_not_started = sum(p > 0 for p in progress)
        stocks = list(initial_inventory)
        for root, p in zip(roots, progress):
            # A partly executed simple cycle has moved one token from its
            # root to the current location, regardless of the step count.
            if 0 < p < q:
                stocks[root] -= 1
                stocks[(root + p) % q] += 1
        answer = INF
        for i, p in enumerate(progress):
            if p == q or (p == 0 and i != first_not_started):
                continue
            tail = (roots[i] + p) % q
            if stocks[tail] < 1:
                continue
            following = list(progress)
            following[i] += 1
            interruption = int(
                last_macro >= 0 and i != last_macro
                and progress[last_macro] < q
            )
            answer = min(
                answer, interruption + solve(tuple(following), i)
            )
        return answer

    return solve((0,) * k, -1)


def other_root_run_count(word):
    a = word[0]
    bset = set(word) - {a}
    assert len(bset) <= 1
    if not bset:
        return 0
    b = next(iter(bset))
    return sum(
        value == b and (i == 0 or word[i - 1] != b)
        for i, value in enumerate(word)
    )


def validate():
    by_q = []
    total = 0
    for q in (2, 3, 4, 5):
        count = 0
        # Rotation symmetry fixes the first root at 0; test every
        # second root B=1,...,q-1 and every listed root word of length <=7.
        for second in range(1, q):
            for k in range(1, 8):
                for tail in product((0, second), repeat=k - 1):
                    word = (0,) + tail
                    initial = (1,) + (0,) * (q - 1)
                    got = optimal_interruptions(q, word, initial)
                    expect = other_root_run_count(word)
                    assert got == expect, (q, word, got, expect)
                    count += 1
        by_q.append({"q": q, "cases": count, "all_assertions_passed": True})
        total += count

    # Two distinct words have the same source histogram and identical
    # final nonnegative PASS counts (each macro traverses every edge once).
    q = 3
    aabb = (0, 0, 1, 1)
    abab = (0, 1, 0, 1)
    one_seed = (1, 0, 0)
    counterexample = {
        "q": 3,
        "word_aabb": list(aabb),
        "word_abab": list(abab),
        "one_seed_min_interruptions": {
            "aabb": optimal_interruptions(q, aabb, one_seed),
            "abab": optimal_interruptions(q, abab, one_seed),
        },
        "two_seeds_min_interruptions": {
            "aabb": optimal_interruptions(q, aabb, (1, 1, 0)),
            "abab": optimal_interruptions(q, abab, (1, 1, 0)),
        },
        "terminal_pass_per_edge": 4,
        "source_root_counts": {"0": 2, "1": 2},
    }
    assert counterexample["one_seed_min_interruptions"] == {"aabb": 1, "abab": 2}
    assert counterexample["two_seeds_min_interruptions"] == {"aabb": 0, "abab": 0}

    alternating = []
    for m in range(1, 6):
        word = (0, 1) * m
        actual = optimal_interruptions(3, word, one_seed)
        assert actual == m
        alternating.append({
            "m": m, "macro_count": 2 * m, "chronological_min_interruptions": actual,
            "unrestricted_first_start_min_interruptions": 1,
            "chronology_penalty": actual - 1,
        })

    return {
        "schema": "R762Z_EXACT_CHRONOLOGICAL_TWO_ROOT_VALIDATION_V1",
        "date": "2026-11-14",
        "method": "complete integer dynamic programming of legal macro shuffles with first-start order, progress vector and exact port stocks",
        "domain": "q=2..5, two distinct named roots, all words of length 1..7 beginning with 0, every second-root offset; K=1; plus stated counterexample and alternating m=1..5",
        "finite_tests": by_q,
        "finite_total": total,
        "counterexample": counterexample,
        "alternating": alternating,
        "result": "ALL_ASSERTIONS_PASSED",
        "mathematical_review": "NOT_REVIEWED",
        "native_force_admission": "NOT_TESTED",
    }


if __name__ == "__main__":
    result = validate()
    out = Path(__file__).with_name("R762Z_CHRONOLOGY_FRONTIER_EVIDENCE.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
