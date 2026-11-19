#!/usr/bin/env python3
"""Exact finite check for R40 weighted observed-trace classification.

Weights are nonnegative integers counting distinct transitions; output and
transition matrices are exact. No claim of native X6 physics is made.
"""
from itertools import product
from collections import Counter
import json


def symbols(labels, outputs):
    return tuple((a, v) for a in labels for v in outputs)


def count(machine, start, word):
    """Number of transition paths producing observed word from start."""
    weights, observations, labels = machine
    n = len(observations)
    row = [int(j == start) for j in range(n)]
    for event, next_output in word:
        new = [0] * n
        for i in range(n):
            for j in range(n):
                if observations[j] == next_output:
                    new[j] += row[i] * weights[event][i][j]
        row = new
    return sum(row)


def profiles(machine, horizon, alphabet):
    # Profiles at every depth, each a tuple of (word,count) ordered by length.
    words = [()]
    by_depth = [words[:]]
    for h in range(1, horizon + 1):
        words = [w + (a,) for w in words for a in alphabet]
        by_depth.append(words)
    result = []
    for s in range(len(machine[1])):
        levels = []
        part = []
        for depth_words in by_depth:
            part.extend(count(machine, s, w) for w in depth_words)
            levels.append(tuple(part))
        result.append((machine[1][s], levels))
    return result


def six_state_example():
    # p=0, q=1, u=2, v=3, t1=4, t2=5. Two paths for p-ab,
    # one for q-ab, though the Boolean observed languages are identical.
    n = 6
    matrices = {a: [[0] * n for _ in range(n)] for a in ("a", "b")}
    for a, i, j in (("a", 0, 2), ("a", 1, 3),
                    ("b", 2, 4), ("b", 2, 5), ("b", 3, 4)):
        matrices[a][i][j] += 1
    machine = (matrices, (0,) * n, ("a", "b"))
    words = [(), (("a", 0),), (("b", 0),),
             (("a", 0), ("a", 0)), (("a", 0), ("b", 0)),
             (("b", 0), ("a", 0)), (("b", 0), ("b", 0))]
    p, q = [{w: count(machine, s, w) for w in words} for s in (0, 1)]
    assert all((p[w] > 0) == (q[w] > 0) for w in words)
    assert p[(("a", 0), ("b", 0))] == 2
    assert q[(("a", 0), ("b", 0))] == 1
    assert p[(("a", 0),)] == q[(("a", 0),)] == 1
    return {"states": 6, "support_equal_all_lengths": True,
            "first_weight_difference": ["a:0", "b:0"],
            "paths_p_ab": 2, "paths_q_ab": 1,
            "equal_initial_and_one_step_counts": True}


def run():
    n = 2
    all_machines = []
    for entries in product((0, 1, 2), repeat=4):
        matrix = (entries[:2], entries[2:])
        for obs in product((0, 1), repeat=n):
            all_machines.append(({"a": matrix}, obs, ("a",)))
    assert len(all_machines) == 324
    alphabet = symbols(("a",), (0, 1))
    # Theorem gives N-1=3 for two states on each side.
    # Verify against all words to depth 6, a strictly stronger finite check.
    profiles_all = [p for machine in all_machines for p in profiles(machine, 6, alphabet)]
    assert len(profiles_all) == 648
    pair_count = 0
    same_through_3 = 0
    full_check_equal = 0
    first_difference = Counter()
    for output_a, aa in profiles_all:
        for output_b, bb in profiles_all:
            pair_count += 1
            if output_a != output_b:
                first_difference[0] += 1
                continue
            if aa[3] == bb[3]:
                same_through_3 += 1
                assert aa[6] == bb[6], "difference after cutoff"
                full_check_equal += 1
                continue
            d = next(d for d in range(1, 4) if aa[d] != bb[d])
            first_difference[d] += 1
    assert pair_count == 648 ** 2
    assert pair_count == sum(first_difference.values()) + full_check_equal
    return {
        "result": "PASS",
        "scope": "all pairs of 324 two-state, one-event, binary-readout, transition-weight 0/1/2 machines and both starts; observed alphabet (event, destination output); compare exact counts through depth 6",
        "machines": len(all_machines),
        "rooted_states": len(profiles_all),
        "ordered_pairs": pair_count,
        "cutoff_for_two_plus_two_states": 3,
        "confirmatory_depth": 6,
        "equal_through_cutoff_and_confirmatory_depth": full_check_equal,
        "first_difference_depths": {str(d): first_difference[d] for d in sorted(first_difference)},
        "example": six_state_example(),
        "general_theorem_proof": "Symbolic rational reachable-row-span argument; finite testing does not prove arbitrary size"
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False, sort_keys=True))
