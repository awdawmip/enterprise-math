#!/usr/bin/env python3
"""R719: exact six-axis two-tag BRC source observer (pure integers)."""
from collections import Counter, defaultdict
from itertools import combinations
from json import dumps

V = tuple(range(6))
PAIRS = tuple(combinations(V, 2))
TRIPLES = tuple(combinations(V, 3))
A, B = 0, 1
W = (2, 3, 4, 5)
STAR = tuple(t for t in TRIPLES if A in t or B in t)
EXTERIOR = tuple(t for t in TRIPLES if A not in t and B not in t)
STAR_IDX = {t: i for i, t in enumerate(STAR)}
EDGE = tuple(combinations(W, 2))
assert len(STAR) == 16 and len(EXTERIOR) == 4


def ledger(triples):
    return tuple(sum(set(e).issubset(t) for t in triples) for e in PAIRS)


def state(mask, frozen=()):
    return frozenset(t for i, t in enumerate(STAR) if (mask >> i) & 1) | frozenset(frozen)


def recovery(h0, after, probe_p, probe_q):
    """Reconstruct six-axis h1 from a two-axis transition with two a-tag probes."""
    outside = frozenset(t for t in h0 if t in EXTERIOR)
    d_out = ledger(outside)
    q = {e: after[i] - d_out[i] for i, e in enumerate(PAIRS)}
    s = {e: q[e] for e in EDGE}
    y = {}
    degree = {}
    for i in W:
        total = sum(s[tuple(sorted((i, j)))] for j in W if j != i)
        twice_y = q[(A, i)] + q[(B, i)] - total
        assert twice_y % 2 == 0
        y[i] = twice_y // 2
        degree[i] = q[(A, i)] - y[i]
        assert y[i] in (0, 1)
    i, j, k, ell = W
    p, z = probe_p, probe_q
    x = {(i, j): p, (i, k): z}
    x[(i, ell)] = degree[i] - p - z
    twice_x_jk = degree[i] + degree[j] + degree[k] - degree[ell]
    assert twice_x_jk % 2 == 0
    x[(j, k)] = twice_x_jk // 2 - p - z
    x[(j, ell)] = degree[j] - p - x[(j, k)]
    x[(k, ell)] = degree[k] - z - x[(j, k)]
    assert all(v in (0, 1) for v in x.values())
    assert all(s[e] - x[e] in (0, 1) for e in EDGE)
    h1 = set(outside)
    h1.update((A, B, i) for i in W if y[i])
    h1.update((A,) + e for e in EDGE if x[e])
    h1.update((B,) + e for e in EDGE if s[e] - x[e])
    assert ledger(h1) == after
    return frozenset(h1)


def compute():
    pair_contrib = tuple(tuple(i for i, e in enumerate(PAIRS)
                               if set(e).issubset(t)) for t in STAR)
    ledgers = [None] * (1 << 16)
    ledgers[0] = (0,) * len(PAIRS)
    fibers = defaultdict(list)
    for mask in range(1 << 16):
        if mask:
            bit = mask & -mask
            col = bit.bit_length() - 1
            prev = list(ledgers[mask ^ bit])
            for row in pair_contrib[col]:
                prev[row] += 1
            ledgers[mask] = tuple(prev)
        fibers[ledgers[mask]].append(mask)
    hist = Counter(map(len, fibers.values()))
    assert hist == {1: 64096, 2: 672, 3: 32}
    diff = set()
    for fiber in fibers.values():
        for u, v in combinations(fiber, 2):
            diff.add(u ^ v)
    assert len(diff) == 3
    assert {x.bit_count() for x in diff} == {8}
    pair_count = sum(k * (k - 1) // 2 * count for k, count in hist.items())
    assert pair_count == 768
    good_two_queries = []
    for ij in combinations(range(16), 2):
        query = sum(1 << i for i in ij)
        if all(query & different for different in diff):
            good_two_queries.append(ij)
    assert len(good_two_queries) == 48
    assert all(
        STAR[i][0] in (A, B) and STAR[j][0] in (A, B)
        and STAR[i][1:] != STAR[j][1:]
        and len(set(STAR[i][1:]) & set(STAR[j][1:])) == 1
        and A not in STAR[i][1:] and B not in STAR[i][1:]
        and A not in STAR[j][1:] and B not in STAR[j][1:]
        for i, j in good_two_queries
    )
    probes = ((A, W[0], W[1]), (A, W[0], W[2]))
    probe_idx = tuple(STAR_IDX[t] for t in probes)
    cases = 0
    for outside in ((), EXTERIOR, (EXTERIOR[0], EXTERIOR[-1])):
        d_exterior = ledger(outside)
        for mask in range(1 << 16):
            h = state(mask, outside)
            d = tuple(x + y for x, y in zip(d_exterior, ledgers[mask]))
            ans = recovery(state(0, outside), d,
                           (mask >> probe_idx[0]) & 1,
                           (mask >> probe_idx[1]) & 1)
            assert ans == h
            cases += 1
    largest = next(f for f in fibers.values() if len(f) == 3)
    assert len({ledgers[m] for m in largest}) == 1
    assert len({((m >> probe_idx[0]) & 1,
                 (m >> probe_idx[1]) & 1) for m in largest}) == 3
    return {
        "n_axes": 6,
        "known_axis_tags": [0, 1],
        "triple_membership_bits": 20,
        "two_star_variable_bits": 16,
        "frozen_exterior_bits": 4,
        "pair_ledger_coordinates": 15,
        "enumerated_states": 1 << 16,
        "distinct_pair_ledgers": len(fibers),
        "fiber_histogram": dict(sorted(hist.items())),
        "colliding_unordered_state_pairs": pair_count,
        "distinct_collision_supports": len(diff),
        "minimal_collision_distance": min(x.bit_count() for x in diff),
        "optimal_worst_case_extra_fixed_membership_queries": 2,
        "optimal_worst_case_extra_adaptive_membership_queries": 2,
        "number_of_optimal_fixed_two_query_sets": len(good_two_queries),
        "sample_fixed_queries": ["".join(map(str, t)) for t in probes],
        "decoder_cases": cases,
        "arithmetic": "exact Python integers; full enumeration of 2^16 Boolean two-star states",
        "native_status": "candidate source observer; native X6 event admissibility unverified",
    }


if __name__ == "__main__":
    result = compute()
    print(dumps(result, ensure_ascii=False, indent=2))
    print("R719_BRC_TWO_AXIS_LOCAL_LEDGER_EXACT_PASS")
