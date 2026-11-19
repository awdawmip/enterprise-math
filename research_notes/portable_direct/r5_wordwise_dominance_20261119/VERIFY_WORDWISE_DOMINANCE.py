#!/usr/bin/env python3
"""Exact finite verification of future-word existential support deletion.

Standard-library Python 3. All transformations, supports and queries are exact.
"""
from collections import deque
from itertools import product
import json


def image_set(action, Y):
    result = 0
    for y in range(len(action)):
        if Y & (1 << y):
            result |= 1 << action[y]
    return result


def dominates(labels, x, Y):
    return any((labels[x] & ~labels[y]) == 0
               for y in range(len(labels)) if Y & (1 << y))


def bfs_certificate(actions, labels, x, Y):
    """Exact decision plus shortest counterexample word."""
    queue = deque([(x, Y, ())])
    visited = {(x, Y)}
    while queue:
        x0, yset, word = queue.popleft()
        if not dominates(labels, x0, yset):
            return (False, word, len(visited))
        for a_idx, action in enumerate(actions):
            nx, ny = action[x0], image_set(action, yset)
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, word + (a_idx,)))
    return (True, None, len(visited))


def transformation_monoid(actions, n):
    """All distinct total transformations T_w, including identity."""
    identity = tuple(range(n))
    found = {identity}
    queue = deque([identity])
    while queue:
        f = queue.popleft()
        for action in actions:
            g = tuple(action[f[i]] for i in range(n))
            if g not in found:
                found.add(g)
                queue.append(g)
    return found


def independent_query_oracle(monoid, labels, x, Y):
    """Directly compare every Q-observation, not the dominance predicate."""
    ys = [i for i in range(len(labels)) if Y & (1 << i)]
    sources = [x] + ys
    num_queries = 1 << max(1, max(labels).bit_length())
    for f in monoid:
        for Q in range(num_queries):
            before = any((labels[f[z]] & Q) == Q for z in sources)
            after = any((labels[f[z]] & Q) == Q for z in ys)
            if before != after:
                return False
    return True


def fixed_witness_missing(monoid, labels, x, Y):
    ys = [i for i in range(len(labels)) if Y & (1 << i)]
    return not any(all((labels[f[x]] & ~labels[f[y]]) == 0
                       for f in monoid) for y in ys)


def exhaustive_three_state():
    n = 3
    all_actions = list(product(range(n), repeat=n))
    subsets = [s for s in range(1, 1 << n) if s.bit_count() >= 2]
    checks = safe = unsafe = failures_after_one = 0
    max_bfs = max_monoid = 0
    for a in all_actions:
        for b in all_actions:
            actions = (a, b)
            monoid = transformation_monoid(actions, n)
            max_monoid = max(max_monoid, len(monoid))
            for labels in product((0, 1), repeat=n):
                for S in subsets:
                    for x in range(n):
                        if not (S & (1 << x)):
                            continue
                        Y = S & ~(1 << x)
                        actual, witness, visited = bfs_certificate(actions, labels, x, Y)
                        expected = independent_query_oracle(monoid, labels, x, Y)
                        assert actual == expected, (actions, labels, S, x)
                        checks += 1
                        safe += int(actual)
                        unsafe += int(not actual)
                        max_bfs = max(max_bfs, visited)
                        if witness is not None and len(witness) > 1:
                            failures_after_one += 1
    assert checks == 27 * 27 * 8 * 9
    return dict(n=3, actions=2, observation_bits=1,
                exhaustive_configs=checks, safe_cases=safe,
                unsafe_cases=unsafe,
                unsafe_shortest_word_length_gt_one=failures_after_one,
                max_bfs_states_seen=max_bfs,
                max_transformation_monoid_size=max_monoid)


def four_state_secondary():
    n = 4
    checked = safe = unsafe = 0
    max_monoid = 0
    for seed in range(128):
        a = tuple((seed // (4 ** i)) % 4 for i in range(n))
        b = tuple(((seed * 37 + 19) // (4 ** i)) % 4 for i in range(n))
        labels = tuple(((seed * 11 + 7) // (4 ** i)) % 4 for i in range(n))
        monoid = transformation_monoid((a, b), n)
        max_monoid = max(max_monoid, len(monoid))
        for Y in range(1, 1 << n):
            for x in range(n):
                if Y & (1 << x):
                    continue
                actual, _, _ = bfs_certificate((a, b), labels, x, Y)
                assert actual == independent_query_oracle(monoid, labels, x, Y)
                checked += 1
                safe += int(actual)
                unsafe += int(not actual)
    return dict(n=4, actions=2, observation_bits=2,
                deterministic_instances=128, input_checks=checked,
                safe_cases=safe, unsafe_cases=unsafe,
                max_monoid_size=max_monoid)


def targeted_five_state():
    # Response indices: x=0, y1=1, y2=2, good=3, bad=4
    a = (3, 4, 3, 3, 4)
    b = (3, 3, 4, 3, 4)
    labels = (1, 1, 1, 1, 0)
    monoid = transformation_monoid((a, b), 5)
    Y = (1 << 1) | (1 << 2)
    admissible, bad_word, states_seen = bfs_certificate((a, b), labels, 0, Y)
    assert admissible and bad_word is None
    assert independent_query_oracle(monoid, labels, 0, Y)
    assert fixed_witness_missing(monoid, labels, 0, Y)
    assert not independent_query_oracle(monoid, labels, 0, 1 << 1)
    assert not independent_query_oracle(monoid, labels, 0, 1 << 2)
    return dict(n=5, actions=2, labels=labels, transitions_a=a,
                transitions_b=b, initial_x=0, initial_Y=[1, 2],
                full_set_redundant=True, each_fixed_witness_inadequate=True,
                reachable_pair_states=states_seen,
                transformation_monoid_size=len(monoid))


if __name__ == "__main__":
    result = {
        "schema": "EM_R5_WORDWISE_DOMINANCE_FINITE_CHECK_V1",
        "scope": "FINITE_DETERMINISTIC_RESPONSE_AUTOMATA_AND_EXISTENTIAL_MASK_QUERIES",
        "theoretical_bfs_state_bound": "N*2^N",
        "n3_complete": exhaustive_three_state(),
        "n4_deterministic_sweep": four_state_secondary(),
        "n5_counterexample": targeted_five_state(),
        "independent_checker": "BFS_PAIR_PRODUCT_VS_COMPLETE_TRANSFORMATION_MONOID",
        "result": "PASS"
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
