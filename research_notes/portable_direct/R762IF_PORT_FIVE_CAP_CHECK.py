"""Reproducible exact checks for the fixed-six-axis Port Euler cap-five lemma."""
from collections import Counter
from itertools import combinations
import json
import random

AXES = range(6)
PORTS = list(combinations(AXES, 2))
SUPPORTS = list(combinations(AXES, 3))
P_INDEX = {p: i for i, p in enumerate(PORTS)}
S_INDEX = {s: i for i, s in enumerate(SUPPORTS)}
EDGE_OPTIONS = {
    s: [tuple((P_INDEX[a], P_INDEX[b])) for a, b in combinations(list(combinations(s, 2)), 2)]
    for s in SUPPORTS
}


def rank(columns):
    pivots = {}
    for column in columns:
        x = column
        while x:
            bit = x.bit_length() - 1
            if bit in pivots:
                x ^= pivots[bit]
            else:
                pivots[bit] = x
                break
    return len(pivots)


def vector(event):
    s, u, v = event
    return (1 << u) ^ (1 << v) ^ (1 << (15 + S_INDEX[s]))


def valid(events, start):
    if not events:
        return False
    degrees = [0] * 15
    used = set()
    adjacency = [set() for _ in PORTS]
    for s, u, v in events:
        assert (u, v) in EDGE_OPTIONS[s] or (v, u) in EDGE_OPTIONS[s]
        degrees[u] ^= 1
        degrees[v] ^= 1
        adjacency[u].add(v)
        adjacency[v].add(u)
        used.update((u, v))
    seen = {start}
    stack = [start]
    while stack:
        for v in adjacency[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return not any(degrees) and used == seen


def five_cap(n):
    return n if n <= 5 else 4 + (n % 2)


def compress(events, start):
    """Convert one given connected Euler edge multigraph to its countwise cap-five witness."""
    assert valid(events, start)
    root = list(range(15))
    def find(x):
        while root[x] != x:
            x = root[x]
        return x
    tree, rest = [], []
    for event in events:
        u, v = event[1:]
        a, b = find(u), find(v)
        if a != b:
            root[a] = b
            tree.append(event)
        else:
            rest.append(event)
    pivots = {}
    for j, event in enumerate(rest):
        x, mask = vector(event), 1 << j
        while x:
            bit = x.bit_length() - 1
            if bit not in pivots:
                pivots[bit] = (x, mask)
                break
            y, oldmask = pivots[bit]
            x ^= y
            mask ^= oldmask
    target = 0
    for event in rest:
        target ^= vector(event)
    selected = 0
    while target:
        bit = target.bit_length() - 1
        y, mask = pivots[bit]
        target ^= y
        selected ^= mask
    core = tree + [event for j, event in enumerate(rest) if selected & (1 << j)]
    orig = Counter(e[0] for e in events)
    count = Counter(e[0] for e in core)
    first = {}
    for event in events:
        first.setdefault(event[0], event)
    reconstructed = list(core)
    for s in SUPPORTS:
        wanted = five_cap(orig[s])
        assert count[s] <= wanted and (wanted - count[s]) % 2 == 0
        for _ in range((wanted - count[s]) // 2):
            reconstructed.extend([first[s], first[s]])
    assert valid(reconstructed, start)
    assert all(sum(e[0] == s for e in reconstructed) == five_cap(orig[s]) for s in SUPPORTS)
    return len(tree), len(core) - len(tree), len(events), len(reconstructed)


def generated(seed, cycles=False):
    rng = random.Random(seed)
    start = P_INDEX[(0, 1)]
    active = {start}
    events = []
    for iteration in range(750):
        u = rng.choice(sorted(active))
        options = [(s, a, b) for s in SUPPORTS for a, b in EDGE_OPTIONS[s] if u in (a, b)]
        s, a, b = rng.choice(options)
        events.extend([(s, a, b), (s, a, b)])
        active.update((a, b))
        if cycles and iteration % 23 == 0:
            choices = [s for s in SUPPORTS if any(p in active for edge in EDGE_OPTIONS[s] for p in edge)]
            s = rng.choice(choices)
            for a, b in EDGE_OPTIONS[s]:
                events.append((s, a, b))
            active.update(x for edge in EDGE_OPTIONS[s] for x in edge)
    assert valid(events, start)
    return events, start


def main():
    columns = [vector((s, *edge)) for s in SUPPORTS for edge in EDGE_OPTIONS[s]]
    assert len(PORTS) == 15 and len(SUPPORTS) == 20 and len(columns) == 60
    assert rank(columns) == 34
    assert all(rank([vector((s, *edge)) for edge in EDGE_OPTIONS[s]]) == 3 for s in SUPPORTS)
    records = []
    for seed, cycles in [(7, False), (11, True), (29, True), (41, False)]:
        events, start = generated(seed, cycles)
        records.append({"seed": seed, "cycles": cycles, "sizes": compress(events, start)})
    print(json.dumps({"status": "PASS R762IF", "global_rank": 34,
                      "per_support_rank": 3, "tests": records}, ensure_ascii=False))


if __name__ == "__main__":
    main()
