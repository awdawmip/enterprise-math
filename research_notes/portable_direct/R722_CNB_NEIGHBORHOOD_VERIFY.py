"""R722: exact 14-arc radius-two barrier around R721b, native V17 CNB path model.
Independent observers: all-path edge-mask catalog and typed-frame propagation.
Reproduce: python R722_CNB_NEIGHBORHOOD_VERIFY.py
No floating point, classical pi, or unrelated physical propagator.
"""
import itertools
import json
from collections import Counter, defaultdict
from math import comb

ROOT = "012"
VERTICES = ["".join(v) for v in itertools.combinations("01234", 3)]
FRAMES = {"".join(p) for p in itertools.permutations(ROOT)}
ARCS = tuple((u, v) for u in VERTICES for v in VERTICES
             if len(set(u) & set(v)) == 2)
ARC_IDS = {e: i for i, e in enumerate(ARCS)}
BASE_TEXT = """012>024 012>123 012>124 013>012 013>023
023>012 023>013 024>023 024>124 123>013
123>023 123>134 124>123 124>134 134>013"""
BASE = frozenset(tuple(e.split(">")) for e in BASE_TEXT.split())
OUT = frozenset(ARCS) - BASE
NEIGHBORS = {u: tuple(v for x, v in ARCS if x == u) for u in VERTICES}
assert len(BASE) == 15 and len(ARCS) == 60 and len(OUT) == 45

def advance(frame, destination):
    missing = [x for x in frame if x not in destination]
    entering = [x for x in destination if x not in frame]
    assert len(missing) == len(entering) == 1
    return frame.replace(missing[0], entering[0])

def catalog(length):
    by_frame = defaultdict(set)
    def visit(previous, current, first, frame, depth, mask):
        if depth == length:
            if current == ROOT and previous != first:
                by_frame[frame].add(mask)
            return
        for dest in NEIGHBORS[current]:
            if dest != previous:
                visit(current, dest, dest if first is None else first,
                      advance(frame, dest), depth + 1,
                      mask | (1 << ARC_IDS[(current, dest)]))
    visit(None, ROOT, None, ROOT, 0, 0)
    assert set(by_frame) == FRAMES
    return {h: tuple(sorted(by_frame[h])) for h in sorted(FRAMES)}

C4, C5 = catalog(4), catalog(5)

def by_catalog(mask, options):
    return frozenset(h for h, masks in options.items()
                     if any((p & mask) == p for p in masks))

def by_propagation(edges, length):
    outgoing = defaultdict(list)
    for u, v in edges:
        outgoing[u].append(v)
    states = {(ROOT, v, advance(ROOT, v), v) for v in outgoing[ROOT]}
    for _ in range(2, length + 1):
        new_states = set()
        for previous, current, frame, first in states:
            for dest in outgoing[current]:
                if dest != previous:
                    new_states.add((current, dest, advance(frame, dest), first))
        states = new_states
    return frozenset(frame for previous, current, frame, first in states
                     if current == ROOT and previous != first)

def mask_of(edges):
    mask = 0
    for arc in edges:
        mask |= 1 << ARC_IDS[arc]
    return mask

def verify():
    assert all(by_catalog(mask_of(BASE), c) == FRAMES for c in (C4, C5))
    counts = {}
    dual_checked = 0
    examples = []
    for k in (1, 2, 3):
        count = Counter()
        for deleted in itertools.combinations(sorted(BASE), k):
            retained = BASE.difference(deleted)
            for added in itertools.combinations(sorted(OUT), k - 1):
                candidate = retained.union(added)
                assert len(candidate) == 14
                mask = mask_of(candidate)
                support4 = by_catalog(mask, C4)
                if support4 != FRAMES:
                    count["fails_at_4"] += 1
                    continue
                support5 = by_catalog(mask, C5)
                assert by_propagation(candidate, 4) == support4
                assert by_propagation(candidate, 5) == support5
                dual_checked += 1
                if support5 != FRAMES:
                    count["passes_4_fails_5"] += 1
                    if len(examples) < 5:
                        examples.append({
                            "deleted": sorted(">".join(e) for e in deleted),
                            "added": sorted(">".join(e) for e in added),
                            "missing_at_5": sorted(FRAMES - support5)
                        })
                else:
                    count["passes_4_and_5"] += 1
        assert sum(count.values()) == comb(15, k) * comb(45, k - 1)
        assert count["passes_4_and_5"] == 0
        counts[str(k)] = {
            "candidate_count": comb(15, k) * comb(45, k - 1),
            "fails_at_4": count["fails_at_4"],
            "passes_4_fails_5": count["passes_4_fails_5"],
            "passes_4_and_5": count["passes_4_and_5"]
        }
    assert dual_checked == 65
    assert sum(v["candidate_count"] for v in counts.values()) == 455190
    result = {
        "schema": "R722_CNB_15_ARC_RADIUS_TWO_EXACT_V1",
        "status": "R722_LOCAL_LOWER_BOUND_EXACT_PASS",
        "source": "R721b, ab1faa492bec4e7f56a81dc8bba09d96b0d6cffc",
        "root": ROOT, "axes": "01234",
        "possible_directed_arcs": 60,
        "base_arcs": sorted(">".join(e) for e in BASE),
        "claim": "Every 14-arc set obtained by deleting k=1,2,3 base arcs and adding k-1 new arcs fails six-state reachability at length 4 or 5.",
        "path_catalog_distinct_masks": {
            "length_4": {h: len(C4[h]) for h in sorted(FRAMES)},
            "length_5": {h: len(C5[h]) for h in sorted(FRAMES)}
        },
        "classification": counts,
        "total_candidates": 455190,
        "cross_checked_by_independent_propagation": dual_checked,
        "examples": examples,
        "remaining": "Global 14-or-fewer directed-arc constructions and native Link/Port admissibility are open."
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == "__main__":
    verify()
