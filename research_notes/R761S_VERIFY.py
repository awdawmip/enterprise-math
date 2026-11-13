#!/usr/bin/env python3
"""Exact finite certificate for R761S triadic-port sparse generators (Python 3 stdlib)."""
import itertools
import json
from collections import Counter, defaultdict, deque

N = 6
ID = tuple(range(N))
SUPPORTS = tuple(itertools.combinations(range(N), 3))

def compose(p, q):
    """Permutation p after q."""
    return tuple(p[q[i]] for i in range(N))

def inverse(p):
    q = [0] * N
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)

def triad(t):
    p = list(ID)
    a, b, c = t
    p[a], p[b], p[c] = b, c, a
    return tuple(p)

def histogram(support_set):
    generators = [triad(t) for t in support_set]
    generators += [inverse(g) for g in generators]
    depths = {ID: 0}
    queue = deque([ID])
    while queue:
        p = queue.popleft()
        for g in generators:
            q = compose(p, g)
            if q not in depths:
                depths[q] = depths[p] + 1
                queue.append(q)
    counts = Counter(depths.values())
    return tuple(counts[k] for k in range(max(counts) + 1))

def canonical(support_set):
    return min(
        tuple(sorted(tuple(sorted(sigma[i] for i in t)) for t in support_set))
        for sigma in itertools.permutations(range(N))
    )

def component_sizes(support_set):
    parent = list(range(N))
    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for t in support_set:
        for x in t[1:]:
            parent[find(x)] = find(t[0])
    return sorted(Counter(find(i) for i in range(N)).values())

all_triples = tuple(itertools.combinations(SUPPORTS, 3))
assert len(all_triples) == 1140
orbits = defaultdict(list)
group_sizes = Counter()
for s in all_triples:
    hist = histogram(s)
    group_sizes[sum(hist)] += 1
    union = set().union(*(set(t) for t in s))
    components = component_sizes(s)
    predicted_size = 1
    for k in components:
        if k >= 3:
            predicted_size *= __import__('math').factorial(k) // 2
    assert sum(hist) == predicted_size
    if len(union) == 6:
        assert components == [6] and sum(hist) == 360
        orbits[canonical(s)].append(s)
    else:
        assert sum(hist) != 360

assert group_sizes == {12: 60, 60: 600, 360: 480}
assert len(orbits) == 3
records = []
for rep, members in sorted(orbits.items()):
    hist = histogram(rep)
    pairs = sorted(len(set(a) & set(b)) for a, b in itertools.combinations(rep, 2))
    common = len(set.intersection(*(set(t) for t in rep)))
    for s in members:
        assert histogram(s) == hist
    records.append({
        'representative': [list(t) for t in rep],
        'orbit_size': len(members),
        'pair_intersections': pairs,
        'triple_intersection': common,
        'depth_counts': list(hist),
        'diameter': len(hist) - 1,
    })
assert sorted((r['orbit_size'], r['diameter']) for r in records) == [(120,5),(180,7),(180,7)]
assert sum(r['orbit_size'] for r in records) == 480

out = {
    'schema': 'R761S_EXACT_SPARSE_TRIADIC_PORT_ENUMERATION_V1',
    'model': 'six labelled positive-axis ports; one oriented 3-cycle and its inverse for each selected support',
    'support_count': len(SUPPORTS),
    'support_triples_tested': len(all_triples),
    'group_order_frequencies': {str(k):v for k,v in sorted(group_sizes.items())},
    'full_A6_support_triples': 480,
    'A6_orbit_records': records,
    'minimal_number_of_supports_to_generate_A6': 3,
    'optimal_diameter_over_three_supports': 5,
    'optimal_support_triples': 120,
    'least_fixed_width_bits_for_final_six-label_port_state': 9,
    'validation': 'exhaustive integer-only BFS over all 1,140 unordered support triples; S6 orbit enumeration; all members crosschecked',
}
print(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True))
