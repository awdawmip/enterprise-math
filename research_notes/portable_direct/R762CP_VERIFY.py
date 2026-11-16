#!/usr/bin/env python3
"""R762CP: exact integer census of binary source-marked K4 triad swaps.

Scientific scope: conditional candidate event law, not the native event licence.
No third-party dependencies. Run: python3 R762CP_VERIFY.py > R762CP_EVIDENCE.json
"""
import itertools
import json
from collections import Counter, defaultdict

EDGES = tuple(itertools.combinations(range(4), 2))
ALL = frozenset(range(6))
STATES = tuple(sorted({
    min(tuple(t), tuple(sorted(ALL-set(t))))
    for t in itertools.combinations(range(6), 3)
}))
INDEX = {s: i for i, s in enumerate(STATES)}
assert len(STATES) == 10

def canonical(a):
    a = tuple(sorted(a))
    b = tuple(sorted(ALL - set(a)))
    return min(a, b)

def kind(a):
    deg = [sum(vertex in EDGES[e] for e in a) for vertex in range(4)]
    return "F" if (3 in deg or 0 in deg) else "P"

def transition(mask):
    t = [[0]*10 for _ in STATES]
    for i, a in enumerate(STATES):
        for x in a:
            for y in ALL-set(a):
                if ((mask >> x) & 1) == ((mask >> y) & 1):
                    t[i][INDEX[canonical((set(a)-{x})|{y})]] += 1
    return t

def connected(t):
    unseen = set(range(10))
    parts = []
    while unseen:
        root = unseen.pop()
        group, todo = {root}, [root]
        while todo:
            i = todo.pop()
            for j in list(unseen):
                if t[i][j]:
                    unseen.remove(j)
                    group.add(j)
                    todo.append(j)
        parts.append(tuple(sorted(group)))
    return tuple(sorted(parts, key=lambda b: (len(b), b)))

def observer_blocks(t):
    d = defaultdict(list)
    for i, a in enumerate(STATES):
        counts = tuple(sum(t[i][j] for j, b in enumerate(STATES)
                           if kind(b) == label) for label in ("F","P"))
        d[(kind(a),)+counts].append(i)
    return tuple(tuple(block) for key, block in
                 sorted(d.items(), key=lambda x: (x[0][0],len(x[1]),x[1][0])))

def quotient(t, blocks):
    q = [[sum(t[b[0]][j] for j in c) for c in blocks] for b in blocks]
    for i, b in enumerate(blocks):
        for state in b:
            for j, c in enumerate(blocks):
                assert sum(t[state][v] for v in c) == q[i][j]
    return q

def shape(mask):
    m = mask.bit_count()
    if m in (0,6): return "0_or_6"
    if m in (1,5): return "1_or_5"
    if m in (2,4):
        selected = [i for i in range(6) if bool(mask & (1<<i)) == (m==2)]
        return "2_or_4_opposite" if set(EDGES[selected[0]]).isdisjoint(
            EDGES[selected[1]]) else "2_or_4_adjacent"
    selected = tuple(i for i in range(6) if mask & (1<<i))
    return "3_F" if kind(selected) == "F" else "3_P"

def edge_map(p):
    return tuple(EDGES.index(tuple(sorted((p[a],p[b])))) for a,b in EDGES)

def transform_mask(mask, em):
    return sum(1<<em[i] for i in range(6) if mask & (1<<i))

def run():
    expected = {
        "0_or_6": (2, (10,), (9,)),
        "1_or_5": (3, (10,), (6,)),
        "2_or_4_opposite": (3, (4,6), (3,5)),
        "2_or_4_adjacent": (4, (4,6), (3,5)),
        "3_F": (3, (1,9), (0,4)),
        "3_P": (4, (1,9), (0,4)),
    }
    reps = {"0_or_6":0, "1_or_5":1, "2_or_4_adjacent":3,
            "2_or_4_opposite":12, "3_F":7, "3_P":19}
    census = Counter()
    details = {}
    representatives = {}
    for mask in range(64):
        t = transition(mask)
        group = shape(mask)
        blocks = observer_blocks(t)
        q = quotient(t,blocks)
        expected_count, components, degrees = expected[group]
        assert len(blocks) == expected_count
        assert tuple(sorted(len(c) for c in connected(t))) == components
        assert tuple(sorted(set(map(sum,t)))) == degrees
        assert t == transition(mask ^ 63)  # global source-mark reversal
        assert all(t[i][i] == 0 and
                   all(t[i][j] == t[j][i] and t[i][j] in (0,1)
                       for j in range(10)) for i in range(10))
        census[group] += 1
        details[str(mask)] = {
            "type":group,
            "future_classes":len(blocks),
            "components":list(components),
            "degrees":list(degrees),
        }
        if mask == reps[group]:
            representatives[group] = {
                "mark_mask":mask,
                "plus_edges":[i for i in range(6) if mask & (1<<i)],
                "blocks":[{"type":kind(STATES[b[0]]), "size":len(b),
                           "states":[list(STATES[i]) for i in b]}
                          for b in blocks],
                "quotient":q,
            }
    assert dict(census) == {"0_or_6":2,"1_or_5":12,
                           "2_or_4_adjacent":24,"2_or_4_opposite":6,
                           "3_F":8,"3_P":12}

    # Entire 24-element K4 skeleton, each of the 64 marked configurations.
    for p in itertools.permutations(range(4)):
        em = edge_map(p)
        relabel = [INDEX[canonical(em[e] for e in a)] for a in STATES]
        for mask in range(64):
            t1 = transition(mask)
            t2 = transition(transform_mask(mask,em))
            assert all(t1[i][j] == t2[relabel[i]][relabel[j]]
                       for i in range(10) for j in range(10))

    hist = Counter(v["future_classes"] for v in details.values())
    assert dict(hist) == {2:2,3:26,4:36}
    return {
        "schema":"R762CP_EXACT_SIGN_MATCHED_BRC_V1",
        "scope":"Conditional source-mark-matched candidate events, NOT native TRIADIC_CLOSURE_E licence",
        "review":"NOT_REVIEWED",
        "edge_order":[list(e) for e in EDGES],
        "ten_canonical_states":[list(a) for a in STATES],
        "64_assignments":details,
        "S4_permutations":24,
        "S4_marked_cases_checked":24*64,
        "six_classes":dict(census),
        "BRC_class_histogram":{str(k):v for k,v in sorted(hist.items())},
        "representatives":representatives,
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
