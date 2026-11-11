#!/usr/bin/env python3
"""R716 exact six-axis BRC pair-degree radius and Pasch-midpoint census (stdlib)."""
import itertools
import json
from collections import Counter
from math import comb
from pathlib import Path

V = range(6)
TRIPLES = tuple(itertools.combinations(V, 3))
PAIRS = tuple(itertools.combinations(V, 2))
TINDEX = {t: i for i, t in enumerate(TRIPLES)}
PINDEX = {p: i for i, p in enumerate(PAIRS)}
assert len(TRIPLES) == 20 and len(PAIRS) == 15
WEIGHTS = tuple(sum(5 ** PINDEX[e] for e in itertools.combinations(t, 2)) for t in TRIPLES)

def ledger(mask):
    return sum(w for i, w in enumerate(WEIGHTS) if (mask >> i) & 1)

def matchings(vertices):
    if not vertices:
        yield ()
        return
    v = vertices[0]
    for i in range(1, len(vertices)):
        for tail in matchings(vertices[1:i] + vertices[i+1:]):
            yield ((v, vertices[i]),) + tail

def trade(matching):
    support = a = b = 0
    for choices in itertools.product((0, 1), repeat=3):
        t = tuple(matching[j][choices[j]] for j in range(3))
        bit = 1 << TINDEX[tuple(sorted(t))]
        support |= bit
        if sum(choices) % 2 == 0:
            a |= bit
        else:
            b |= bit
    return support, a, b

def run():
    trades = tuple(trade(m) for m in matchings(tuple(V)))
    assert len(trades) == len(set(t[0] for t in trades)) == 15
    for support, a, b in trades:
        assert support.bit_count() == 8 and a.bit_count() == b.bit_count() == 4
        assert (a & b) == 0 and (a | b) == support and ledger(a) == ledger(b)

    groups = {}
    gray_ledger = 0
    previous = 0
    collision_count = 0
    minimum_distance = 21
    diff_supports = set()
    for k in range(1 << 20):
        mask = k ^ (k >> 1)
        if k:
            bit = (mask ^ previous).bit_length() - 1
            gray_ledger += WEIGHTS[bit] if (mask >> bit) & 1 else -WEIGHTS[bit]
        previous = mask
        existing = groups.get(gray_ledger)
        if existing is None:
            groups[gray_ledger] = [mask]
            continue
        for old in existing:
            delta = mask ^ old
            collision_count += 1
            minimum_distance = min(minimum_distance, delta.bit_count())
            diff_supports.add(delta)
        existing.append(mask)

    distribution = Counter(d.bit_count() for d in diff_supports)
    assert len(groups) == 995085
    assert collision_count == 65286
    assert minimum_distance == 8
    assert distribution == Counter({8: 15, 12: 15, 20: 1})
    assert set(t[0] for t in trades) == set(d for d in diff_supports if d.bit_count() == 8)

    incidence = Counter()
    for h0 in range(1 << 20):
        midpoint_count = sum((((h0 ^ a) & support).bit_count() == 4)
                             for support, a, b in trades)
        incidence[midpoint_count] += 1
    ambiguous = sum(count for hits, count in incidence.items() if hits)
    assert sum(incidence.values()) == 1 << 20
    assert sum(hits * count for hits, count in incidence.items()) == 15 * comb(8, 4) * (1 << 12)

    support, a, b = trades[0]
    coordinates = [i for i in range(20) if (support >> i) & 1]
    midpoint = next(sum(1 << i for i in subset)
                    for subset in itertools.combinations(coordinates, 4)
                    if ((sum(1 << i for i in subset) ^ a) & support).bit_count() == 4)
    assert (midpoint ^ a).bit_count() == (midpoint ^ b).bit_count() == 4
    for h0 in (0, (1 << 20) - 1, midpoint):
        seen = set()
        for d in range(4):
            for subset in itertools.combinations(range(20), d):
                h = h0
                for j in subset:
                    h ^= 1 << j
                v = ledger(h)
                assert v not in seen
                seen.add(v)
        assert len(seen) == 1351

    report = {
        "schema": "R716_TEMPORAL_LEDGER_EXACT_V1",
        "source_population": 1048576,
        "triples": 20,
        "pairs": 15,
        "ledger_fibers": len(groups),
        "colliding_pairs": collision_count,
        "difference_support_sizes": {str(i): v for i, v in sorted(distribution.items())},
        "minimum_nonzero_fiber_distance": minimum_distance,
        "radius_3_ball_size": sum(comb(20, k) for k in range(4)),
        "radius_4_ball_size": sum(comb(20, k) for k in range(5)),
        "pasch_supports": len(trades),
        "midpoint_incidence_distribution": {str(i): v for i, v in sorted(incidence.items())},
        "radius4_ambiguous_centers": ambiguous,
        "radius4_unambiguous_centers": incidence[0],
        "total_midpoint_trade_incidence": sum(i * v for i, v in incidence.items()),
        "sharpness_example": {
            "H0_triples": ["".join(map(str, TRIPLES[i])) for i in range(20) if (midpoint >> i) & 1],
            "A_triples": ["".join(map(str, TRIPLES[i])) for i in range(20) if (a >> i) & 1],
            "B_triples": ["".join(map(str, TRIPLES[i])) for i in range(20) if (b >> i) & 1],
            "distance_H0_A": (midpoint ^ a).bit_count(),
            "distance_H0_B": (midpoint ^ b).bit_count(),
            "A_and_B_have_same_ledger": ledger(a) == ledger(b)
        },
        "verification": "R716_BRC_TEMPORAL_LEDGER_RADIUS3_EXACT_PASS"
    }
    Path(__file__).with_name("R716_BRC_TEMPORAL_LEDGER_RESULTS.json").write_text(
        json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(report["verification"])
    print(json.dumps({
        "minimum_nonzero_fiber_distance": minimum_distance,
        "radius4_ambiguous_centers": ambiguous,
        "radius4_unambiguous_centers": incidence[0],
        "midpoint_incidence_distribution": report["midpoint_incidence_distribution"]
    }, ensure_ascii=False))

if __name__ == "__main__":
    run()
