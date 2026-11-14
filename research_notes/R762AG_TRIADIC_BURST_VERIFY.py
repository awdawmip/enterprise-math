#!/usr/bin/env python3
"""R762AG: independent exact checks for a conditional three-port star.

Exhaust all six distinct source-blind I/O events, compare explicit physical
token-location transitions with matching/permutation equations, and verify
three-residue positive BRC counts by recurrence versus binomial expansion.
Standard-library only; exact integers. Run: python R762AG_TRIADIC_BURST_VERIFY.py
"""
import json
from collections import Counter
from itertools import permutations
from math import comb

PORTS = (0, 1, 2)
SYMBOLS = tuple((kind, i) for kind in ("I", "O") for i in PORTS)
THREE_CYCLES = {(1, 2, 0), (2, 0, 1)}

def matching_maps(word, capacity):
    ti, to, occupancy = {}, {}, 0
    for instant, (kind, port) in enumerate(word):
        if kind == "I":
            ti[port] = instant
            occupancy += 1
        else:
            to[port] = instant
            occupancy -= 1
        if not (0 <= occupancy <= capacity):
            return set()
    if occupancy != 0 or any(ti[i] > to[i] for i in PORTS):
        return set()
    return {
        p for p in permutations(PORTS)
        if all(p[i] != i and ti[i] < to[p[i]] for i in PORTS)
    }

def physical_maps(word, capacity):
    """Independent explicit state: outer token holders, hub tokens, source destinations."""
    states = {(PORTS, (), (-1, -1, -1))}
    for kind, port in word:
        nxt = set()
        for outer, hub, destinations in states:
            if kind == "I":
                source = outer[port]
                if source is None or len(hub) >= capacity:
                    continue
                update = list(outer)
                update[port] = None
                nxt.add((tuple(update), hub + (source,), destinations))
            else:
                if outer[port] is not None:
                    continue
                for index, source in enumerate(hub):
                    if source == port:
                        continue
                    update = list(outer)
                    update[port] = source
                    dest = list(destinations)
                    dest[source] = port
                    nxt.add((
                        tuple(update), hub[:index] + hub[index + 1:], tuple(dest)
                    ))
        states = nxt
        if not states:
            break
    return {
        d for outer, hub, d in states
        if not hub and all(v is not None for v in outer)
        and all(v >= 0 for v in d)
    }

def weighted_recurrence(k, u, v):
    masses = [1, 0, 0]
    for _ in range(k):
        nxt = [0, 0, 0]
        for r, weight in enumerate(masses):
            nxt[(r + 1) % 3] += weight * u
            nxt[(r - 1) % 3] += weight * v
        masses = nxt
    return masses

def weighted_binomial(k, u, v):
    return [
        sum(
            comb(k, j) * u**j * v**(k - j)
            for j in range(k + 1)
            if (2 * j - k) % 3 == r
        )
        for r in PORTS
    ]

def run():
    all_words = list(permutations(SYMBOLS))
    assert len(all_words) == 720
    capacity_results = {}
    for capacity in (1, 2, 3):
        histogram = Counter()
        for word in all_words:
            direct = physical_maps(word, capacity)
            matching = matching_maps(word, capacity)
            assert direct == matching, (capacity, word, direct, matching)
            if not direct:
                continue
            histogram[len(direct)] += 1
            if len(direct) == 2:
                assert capacity == 3
                assert all(kind == "I" for kind, _ in word[:3])
                assert all(kind == "O" for kind, _ in word[3:])
                assert direct == THREE_CYCLES
            else:
                assert len(direct) == 1
        capacity_results[str(capacity)] = {
            "realizable_logs": sum(histogram.values()),
            "fiber_histogram": {str(k): v for k, v in sorted(histogram.items())},
            "named_physical_histories": sum(k * v for k, v in histogram.items())
        }
    assert capacity_results["1"]["realizable_logs"] == 0
    assert capacity_results["2"]["fiber_histogram"] == {"1": 24}
    assert capacity_results["3"]["fiber_histogram"] == {"1": 24, "2": 36}

    rows = []
    for h in range(15):
        exact = weighted_recurrence(h, 1, 1)
        expected = [
            (2**h + 2 * (-1)**h) // 3,
            (2**h - (-1)**h) // 3,
            (2**h - (-1)**h) // 3,
        ]
        assert exact == expected
        assert sum(exact) == 2**h
        for u, v in ((1, 1), (2, 3), (3, 1)):
            assert weighted_recurrence(h, u, v) == weighted_binomial(h, u, v)
        rows.append({"h": h, "residue_history_counts": exact})

    return {
        "schema": "R762AG_TRIADIC_BURST_C3_EVIDENCE_V1",
        "status": "AUTHOR_SIDE_CONDITIONAL_NOT_REVIEWED_NOT_NATIVE_ADMITTED",
        "frozen_science": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "parent": "R762AF PR2389 7db9d11653d34d264aaec846ae6a91f6972cde86",
        "exact_enumeration": "3 capacities times all 720 I/O word permutations = 2160 independent comparisons",
        "two_independent_methods": [
            "explicit labeled-token state propagation",
            "time-inequality/permutation matching"
        ],
        "capacity_results": capacity_results,
        "residue_checks": rows,
        "weighted_scope": "h=0..14; (u,v)=(1,1),(2,3),(3,1); exact integer recurrence vs binomial sum"
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
