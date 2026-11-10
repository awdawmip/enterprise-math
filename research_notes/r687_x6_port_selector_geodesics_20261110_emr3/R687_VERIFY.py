#!/usr/bin/env python3
"""R687 exact finite certificate for A(6,3), X6 selector cost, and BRC path counts."""
from itertools import permutations, combinations
from collections import Counter, defaultdict, deque
from functools import lru_cache
from pathlib import Path
import json

ROOT = (0, 1, 2)
WORDS = tuple(permutations(range(6), 3))

def neighbors(w, n=6):
    for i in range(len(w)):
        for x in range(n):
            if x not in w:
                yield w[:i] + (x,) + w[i + 1:]

def formula(x, y):
    pos = {a: i for i, a in enumerate(x)}
    edges = {i: pos[y[i]] for i in range(len(x))
             if x[i] != y[i] and y[i] in pos}
    seen = set()
    cycles = 0
    for i in edges:
        path = set()
        j = i
        while j in edges and j not in path and j not in seen:
            path.add(j)
            j = edges[j]
        if j in path:
            cycles += 1
        seen.update(path)
    return sum(a != b for a, b in zip(x, y)) + cycles

def bfs(root, n=6):
    distance = {root: 0}
    count = {root: 1}
    queue = deque([root])
    while queue:
        x = queue.popleft()
        for y in neighbors(x, n):
            if y not in distance:
                distance[y] = distance[x] + 1
                count[y] = 0
                queue.append(y)
            if distance[y] == distance[x] + 1:
                count[y] += count[x]
    return distance, count

def best_fixed_request_word(requests):
    """Just-in-time SWITCHes: choose which occupied slot to evict only on a miss."""
    states = {frozenset(ROOT): (0, 1)}
    for axis in requests:
        nxt = {}
        for active, (cost, multiplicity) in states.items():
            candidates = [(active, cost, multiplicity)] if axis in active else [
                (frozenset((active - {evicted}) | {axis}),
                 cost + 1, multiplicity) for evicted in active]
            for new_active, new_cost, new_mult in candidates:
                old = nxt.get(new_active)
                if old is None or new_cost < old[0]:
                    nxt[new_active] = (new_cost, new_mult)
                elif new_cost == old[0]:
                    nxt[new_active] = (new_cost, old[1] + new_mult)
        states = nxt
    best = min(v[0] for v in states.values())
    return best, sum(v[1] for v in states.values() if v[0] == best)

def free_event_cost(support):
    @lru_cache(None)
    def rec(remaining, active):
        if not remaining:
            return 0
        best = 10**9
        for axis in remaining:
            if axis in active:
                value = 1 + rec(remaining - (axis,), active)
                best = min(best, value)
            else:
                for evicted in active:
                    new_active = tuple(sorted(set(active) - {evicted} | {axis}))
                    value = 2 + rec(remaining - (axis,), new_active)
                    best = min(best, value)
        return best
    return rec(tuple(sorted(support)), ROOT)

def verify():
    assert len(WORDS) == 120 and all(len(tuple(neighbors(w))) == 9 for w in WORDS)
    assert sum(len(tuple(neighbors(w))) for w in WORDS) == 1080
    base_d, base_words = bfs(ROOT)
    assert len(base_d) == 120
    shells = dict(sorted(Counter(base_d.values()).items()))
    assert shells == {0: 1, 1: 9, 2: 36, 3: 63, 4: 11}
    assert max(base_d.values()) == 4
    assert base_d[(1, 2, 0)] == 4
    all_pairs = 0
    for x in WORDS:
        d, _ = bfs(x)
        for y in WORDS:
            assert d[y] == formula(x, y), (x, y, d[y], formula(x, y))
            all_pairs += 1
    assert all_pairs == 14400
    hist = {}
    for distance in range(5):
        hist[str(distance)] = dict(sorted(Counter(
            base_words[w] for w in WORDS if base_d[w] == distance).items()))
        hist[str(distance)] = {str(k): v for k, v in hist[str(distance)].items()}
    expected_hist = {
        "0": {"1": 1}, "1": {"1": 9},
        "2": {"1": 18, "2": 18},
        "3": {"1": 18, "3": 36, "6": 9},
        "4": {"9": 2, "20": 9}}
    assert hist == expected_hist, hist
    assert sum(base_words[w] for w in WORDS if base_d[w] == 4) == 198
    triads = tuple(combinations(range(6), 3))
    assert len(triads) == 20
    for w in WORDS:
        for other in triads:
            if len(set(w) & set(other)) != 2:
                continue
            out = next(iter(set(w) - set(other)))
            inc = next(iter(set(other) - set(w)))
            transported = tuple(inc if x == out else x for x in w)
            assert transported in set(neighbors(w))
            assert tuple(sorted(transported)) == other

    switch_cost_hist = Counter()
    word_mass_by_cost = Counter()
    for requests in permutations(range(6)):
        switch_cost, word_mass = best_fixed_request_word(requests)
        expected = 3 if requests[0] in ROOT else 4
        assert switch_cost == expected
        switch_cost_hist[switch_cost] += 1
        word_mass_by_cost[switch_cost] += word_mass
    assert switch_cost_hist == {3: 360, 4: 360}
    assert word_mass_by_cost == {3: 3240, 4: 9720}

    support_checks = 0
    for mask in range(64):
        support = {i for i in range(6) if mask & (1 << i)}
        exact = free_event_cost(frozenset(support))
        assert exact == len(support) + len(support - set(ROOT))
        support_checks += 1
    assert support_checks == 64

    delta = (-1, 0, 0, 1, 0, 0)
    assert sum(v * v for v in delta) == 2
    p = Path(__file__).with_name("R687_EVIDENCE.json")
    if p.exists():
        record = json.loads(p.read_text(encoding="utf-8"))
        assert record["vertices"] == len(WORDS)
        assert record["shells"] == {str(k): v for k, v in shells.items()}
        assert record["root_geodesic_mass_hist"] == expected_hist
        assert record["length4_word_mass"] == 198
        assert record["all_pairs_checks"] == all_pairs
        assert record["positive_all_six_fixed_path_min_switches"] == {
            str(k): v for k, v in switch_cost_hist.items()}
        assert record["just_in_time_optimal_BRC_hist"] == {
            str(k): v for k, v in word_mass_by_cost.items()}
    for n, k in ((4, 2), (4, 3), (5, 3), (7, 3), (7, 4)):
        words = list(permutations(range(n), k))
        for x in words[:min(len(words), 20)]:
            ds, _ = bfs(x, n)
            assert all(ds[y] == formula(x, y) for y in words)
    print("R687_ARRANGEMENT_GRAPH_EXACT_PASS")
    print("shells", shells, "all_pair_checks", all_pairs)
    print("fixed_path_switch_hist", dict(switch_cost_hist))
    print("just_in_time_BRC_mass", dict(word_mass_by_cost))

if __name__ == "__main__":
    verify()
