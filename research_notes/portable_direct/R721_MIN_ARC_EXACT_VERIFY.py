"""R721: exhaustive finite minimum-arc certificate, standard-library Python.
Five accessible axes, root 012; nine R719q repair arcs are required.
Each target is one of six V17 ordered frames at lengths 4,5,6.
"""
from itertools import combinations
from functools import lru_cache
from json import dumps

S, AXES = '012', '01234'
FRAMES = ('012', '021', '102', '120', '201', '210')
TRIADS = [''.join(t) for t in combinations(AXES, 3)]
ARCS = sorted(f'{u}>{v}' for u in TRIADS for v in TRIADS
              if len(set(u) & set(v)) == 2)
REPAIR = set()
for a in S:
    x = ''.join(sorted((set(S) - {a}) | {'3'}))
    y = ''.join(sorted((set(S) - {a}) | {'4'}))
    REPAIR.update((f'{S}>{x}', f'{x}>{y}', f'{y}>{S}'))
OPTIONAL = sorted(set(ARCS) - REPAIR)
INDEX = {e:i for i,e in enumerate(OPTIONAL)}
ADJ = {u:[v for v in TRIADS if f'{u}>{v}' in ARCS] for u in TRIADS}
assert len(TRIADS) == 10 and len(ARCS) == 60
assert len(REPAIR) == 9 and len(OPTIONAL) == 51


def move(frame, triad):
    outgoing = next(c for c in frame if c not in triad)
    incoming = next(c for c in triad if c not in frame)
    return frame.replace(outgoing, incoming)

BUCKETS = {(m,h):set() for m in (4,5,6) for h in FRAMES}
COUNTS = {(m,h):0 for m in (4,5,6) for h in FRAMES}


def walk(m, prev, cur, first, frame, edge_mask, depth):
    if depth == m:
        if cur == S and prev != first:
            BUCKETS[m,frame].add(edge_mask)
            COUNTS[m,frame] += 1
        return
    for nxt in ADJ[cur]:
        if nxt == prev:
            continue
        edge = f'{cur}>{nxt}'
        add = 0 if edge in REPAIR else 1 << INDEX[edge]
        walk(m, cur, nxt, nxt if first is None else first,
             move(frame,nxt), edge_mask | add, depth+1)

for length in (4,5,6):
    walk(length, None, S, None, S, 0, 0)
assert all(BUCKETS.values())
GROUPS = [tuple(sorted(v)) for v in BUCKETS.values()]


def exact_search(budget):
    seen = set()
    def dfs(mask):
        if mask in seen:
            return False
        seen.add(mask)
        best = None
        for group in GROUPS:
            if any((mask & w) == w for w in group):
                continue
            options = [w for w in group if (mask | w).bit_count() <= budget]
            if not options:
                return False
            if best is None or len(options) < len(best):
                best = options
        if best is None:
            return True
        return any(dfs(mask | w) for w in best)
    possible = dfs(0)
    return {'possible':possible, 'visited_masks':len(seen)}

LOWER, UPPER = exact_search(8), exact_search(9)
assert not LOWER['possible'] and UPPER['possible']
EXAMPLE = ('''012>013 012>023 012>123 012>124 013>014 013>123
014>012 014>024 023>024 023>123 024>012 024>014
123>124 123>234 124>012 124>014 124>024 234>024''').split()
assert len(EXAMPLE) == len(set(EXAMPLE)) == 18
assert REPAIR.issubset(EXAMPLE)
example_mask = sum(1 << INDEX[e] for e in EXAMPLE if e not in REPAIR)
assert example_mask.bit_count() == 9
assert all(any((example_mask & w)==w for w in group) for group in GROUPS)
result = {
 'schema':'R721_FIVE_AXIS_CNB_MINIMUM_DIRECTED_ARCS',
 'status':'R721_18_ARCS_SHARP_EXACT_PASS',
 'domain':{'triads':10,'all_directed_arcs':60,'mandatory_arcs':9,
           'optional_arcs':51,'targets':18},
 'full_graph_raw_path_counts':{str(m):{h:COUNTS[m,h] for h in FRAMES}
                               for m in (4,5,6)},
 'distinct_optional_witness_masks':{str(m):{h:len(BUCKETS[m,h]) for h in FRAMES}
                                    for m in (4,5,6)},
 'eight_or_fewer_optional_arcs':LOWER,
 'nine_optional_arcs':UPPER,
 'minimum_directed_arcs_with_R719q_repair_triangles':18,
 'example_directed_arcs':EXAMPLE,
 'unbounded_length_step':'R719q identity-root-triangle insertion by +3'
}
print(dumps(result,ensure_ascii=False,indent=2))
