#!/usr/bin/env python3
"""R762KH — exact finite connected-parity proof and graph-construction verifier.
Native Python standard library only. No sampling is used in the finite theorem.
"""
from collections import Counter
from itertools import combinations, product
from math import comb
import json

AX = tuple(range(6))
MISSING = ((0, 1), (2, 3), (4, 5))
PORTS = tuple(p for p in combinations(AX, 2) if p not in MISSING)
PI = {p: i for i, p in enumerate(PORTS)}
COLORS = tuple(combinations(AX, 3))
EDGE = {
    s: tuple(combinations([PI[p] for p in combinations(s, 2) if p in PI], 2))
    for s in COLORS
}
FORCED = tuple(s for s in COLORS if len(EDGE[s]) == 1)
FLEX = tuple(s for s in COLORS if len(EDGE[s]) == 3)
assert (len(PORTS), len(COLORS), len(FORCED), len(FLEX)) == (12, 20, 12, 8)


def boundary(e):
    return (1 << e[0]) ^ (1 << e[1])


def force_components():
    parent = list(range(len(PORTS)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for s in FORCED:
        a, b = EDGE[s][0]
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    grouping = {}
    for i in range(len(PORTS)):
        r = find(i)
        if r not in grouping:
            grouping[r] = len(grouping)
    comp = {i: grouping[find(i)] for i in range(len(PORTS))}
    assert Counter(comp.values()) == {0: 4, 1: 4, 2: 4}
    return comp


COMP = force_components()
PAIRTYPES = {(0, 1): 1, (0, 2): 2, (1, 2): 4}


def typebit(e):
    pair = tuple(sorted((COMP[e[0]], COMP[e[1]])))
    return PAIRTYPES[pair]


assert all({typebit(e) for e in EDGE[s]} == {1, 2, 4} for s in FLEX)


def local_choices(s, multiplicity):
    """Exact unordered 1- or 2-event multisets and their parity/type signatures."""
    if multiplicity == 1:
        rows = [(j,) for j in range(3)]
    elif multiplicity == 2:
        rows = [(j, j) for j in range(3)] + list(combinations(range(3), 2))
    else:
        raise ValueError("the finite DP uses minimal 1/2 flexible counts")
    result = []
    for inds in rows:
        b, types = 0, 0
        for j in inds:
            e = EDGE[s][j]
            b ^= boundary(e)
            types |= typebit(e)
        result.append((b, types, inds))
    assert len(result) == (3 if multiplicity == 1 else 6)
    return tuple(result)


CHOICES = {(s, n): local_choices(s, n) for s in FLEX for n in (1, 2)}
FORCED_TARGETS = {}
for mask in range(1 << len(FORCED)):
    b = 0
    for i, s in enumerate(FORCED):
        if (mask >> i) & 1:
            b ^= boundary(EDGE[s][0])
    FORCED_TARGETS[mask] = b
TARGETS = frozenset(FORCED_TARGETS.values())
assert (len(FORCED_TARGETS), len(TARGETS)) == (4096, 512)


def connected_types(t):
    # Any two different edges of a three-component K3 connect A,B,C.
    return t.bit_count() >= 2


def state_dp(upgraded, retain_witness=False):
    """Exact state: (degree-boundary XOR, OR of cross-component pair types)."""
    if retain_witness:
        states = {(0, 0): ()}
    else:
        states = {(0, 0)}
    for i, s in enumerate(FLEX):
        opts = CHOICES[(s, 2 if (upgraded >> i) & 1 else 1)]
        if retain_witness:
            nxt = {}
            for (v, typ), witness in states.items():
                for bv, bt, inds in opts:
                    nxt.setdefault((v ^ bv, typ | bt), witness + (inds,))
            states = nxt
        else:
            states = {(v ^ bv, typ | bt)
                      for v, typ in states for bv, bt, _ in opts}
    return states


def check_event_graph(events, inventory):
    degree = [0] * len(PORTS)
    parent = list(range(len(PORTS)))
    used = Counter()
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for s, e in events:
        assert e in EDGE[s], (s, e)
        used[s] += 1
        u, v = e
        degree[u] += 1
        degree[v] += 1
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
    assert used == Counter(inventory)
    assert all(d > 0 and d % 2 == 0 for d in degree)
    assert len({find(j) for j in range(len(PORTS))}) == 1
    assert len(events) == sum(inventory.values())


def sample_full_graph(upgraded, forced_mask, witness):
    counts = {s: (1 if (forced_mask >> i) & 1 else 2)
              for i, s in enumerate(FORCED)}
    counts.update({s: (2 if (upgraded >> i) & 1 else 1)
                   for i, s in enumerate(FLEX)})
    events = [(s, EDGE[s][0]) for s in FORCED for _ in range(counts[s])]
    for s, indices in zip(FLEX, witness):
        for i in indices:
            events.append((s, EDGE[s][i]))
    check_event_graph(events, counts)


def extended_local(s, n, indices):
    """Lift any 2-event triangle witness to arbitrary n>=2, preserving
    the required GF(2) boundary and connectedness among forced components.
    """
    assert n >= len(indices)
    if len(indices) == 1:
        assert n == 1
        return [EDGE[s][indices[0]]]
    i, j = indices
    if n % 2 == 0:
        base = [EDGE[s][i], EDGE[s][j]]
    elif i == j:
        base = list(EDGE[s])
    else:
        k = next(k for k in range(3) if k not in (i, j))
        base = [EDGE[s][k], EDGE[s][i], EDGE[s][i]]
    assert len(base) <= n and (n - len(base)) % 2 == 0
    out = base + [EDGE[s][0], EDGE[s][0]] * ((n - len(base)) // 2)
    assert len(out) == n
    return out


def verify_extended_graph(upgraded, forced_mask, witness):
    forced = {s: (3 if (forced_mask >> i) & 1 else 4)
              for i, s in enumerate(FORCED)}
    flexible = {s: (3 + (i % 2) if (upgraded >> i) & 1 else 1)
                for i, s in enumerate(FLEX)}
    inventory = forced | flexible
    events = [(s, EDGE[s][0]) for s in FORCED for _ in range(inventory[s])]
    for s, indices in zip(FLEX, witness):
        for e in extended_local(s, inventory[s], indices):
            events.append((s, e))
    check_event_graph(events, inventory)


def direct_all_singleton_reach():
    reached = set()
    for row in product(range(3), repeat=8):
        b = 0
        for s, i in zip(FLEX, row):
            b ^= boundary(EDGE[s][i])
        reached.add(b)
    assert len(reached) == 1881
    return reached


def run():
    base = direct_all_singleton_reach()
    assert 4010 not in base and len(base & TARGETS) == 465
    histogram = {}
    for upgraded in range(1 << len(FLEX)):
        states = state_dp(upgraded)
        matching = {v for v, typ in states if connected_types(typ)} & TARGETS
        parity = {v for v, _ in states} & TARGETS
        assert parity == matching
        count = len(matching)
        histogram.setdefault(upgraded.bit_count(), Counter())[count] += 1
        if upgraded.bit_count() >= 3:
            assert count == 512, (upgraded, count)
    expected = {
        0: Counter({465: 1}), 1: Counter({495: 8}),
        2: Counter({508: 28}), 3: Counter({512: 56}),
        4: Counter({512: 70}), 5: Counter({512: 56}),
        6: Counter({512: 28}), 7: Counter({512: 8}),
        8: Counter({512: 1})}
    assert histogram == expected

    # Reconstruct complete exact graphs for all 4096 forced oddness patterns,
    # using the same 3 upgraded flexible supports.
    sample_upgraded = 0b00000111
    records = state_dp(sample_upgraded, retain_witness=True)
    by_target = {}
    for (bv, typ), witness in records.items():
        if connected_types(typ) and bv in TARGETS:
            by_target.setdefault(bv, witness)
    assert len(by_target) == 512
    for mask, target in FORCED_TARGETS.items():
        sample_full_graph(sample_upgraded, mask, by_target[target])
    for forced_mask in range(16):
        verify_extended_graph(
            sample_upgraded, forced_mask,
            by_target[FORCED_TARGETS[forced_mask]])

    num42 = comb(20, 5) * comb(15, 7)
    assert num42 == 99768240
    output = {
        "schema": "R762KH_THREE_INACTIVE_UPGRADE_THRESHOLD_V1",
        "research_date": "2026-11-23",
        "model": "unsigned six-axis Port-Euler observer; inactive ports 01,23,45",
        "task_frozen_source": "awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json",
        "active_ports": ["".join(map(str, p)) for p in PORTS],
        "forced_colors": ["".join(map(str, s)) for s in FORCED],
        "flexible_colors": ["".join(map(str, s)) for s in FLEX],
        "forced_components": 3,
        "forced_parity_masks": len(FORCED_TARGETS),
        "distinct_forced_parity_targets": len(TARGETS),
        "flexible_upgrade_patterns_exactly_checked": 256,
        "all_singleton_flexible_selections_checked": 3**8,
        "all_singleton_distinct_parities": len(base),
        "reachable_forced_parity_targets_by_number_of_upgraded_flexible_colors":
            {str(k): dict(v) for k, v in sorted(histogram.items())},
        "necessary_and_sufficient_universal_threshold_upgraded_flexible_colors": 3,
        "forced_masks_with_constructed_connected_graph_for_fixed_three_upgrades": 4096,
        "verified_arbitrary_positive_extended_graphs": 16,
        "m3_all_42_event_targets_per_perfect_matching": num42,
        "number_of_named_perfect_matchings": 15,
        "m3_all_42_event_targets_all_perfect_matchings": 15*num42,
        "m3_marked_44_to_42_pairs_all_perfect_matchings": 15*5*num42,
        "independent_review": "NOT_REVIEWED",
        "model_scope": "auxiliary unsigned only; native signed P000/BRC lift remains open",
        "failed_assertions": 0
    }
    return output


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
