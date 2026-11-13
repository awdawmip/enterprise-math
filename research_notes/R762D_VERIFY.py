#!/usr/bin/env python3
"""R762D: directed single-chirality triple generators of S6; exact BFS certificate."""
import itertools
import json
from collections import Counter, deque

N = 6
IDENTITY = tuple(range(N))
SUPPORTS = tuple(itertools.combinations(range(N), 3))


def compose(p, q):
    """Permutation p after q, with image tuples."""
    return tuple(p[q[i]] for i in range(N))


def inverse(p):
    q = [0] * N
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def triad(support):
    a, b, c = support
    p = list(IDENTITY)
    p[a], p[b], p[c] = b, c, a
    return tuple(p)


def histogram(generators):
    distance = {IDENTITY: 0}
    queue = deque([IDENTITY])
    while queue:
        g = queue.popleft()
        for t in generators:
            next_g = compose(g, t)
            if next_g not in distance:
                distance[next_g] = distance[g] + 1
                queue.append(next_g)
    count = Counter(distance.values())
    return tuple(count[i] for i in range(max(count) + 1))


def signature(supports):
    intersections = tuple(sorted(len(set(a) & set(b)) for a, b in itertools.combinations(supports, 2)))
    triple_common = len(set.intersection(*(set(s) for s in supports)))
    return intersections, triple_common


ORIENTATIONS = {s: (triad(s), inverse(triad(s))) for s in SUPPORTS}
counts = Counter()
by_incidence = Counter()
example = {}
all_supports = tuple(itertools.combinations(SUPPORTS, 3))
assert len(SUPPORTS) == 20
assert len(all_supports) == 1140

for support_family in all_supports:
    sig = signature(support_family)
    union_size = len(set.union(*(set(s) for s in support_family)))
    for bits in itertools.product((0, 1), repeat=3):
        gens = tuple(ORIENTATIONS[s][b] for s, b in zip(support_family, bits))
        hist = histogram(gens)
        order = sum(hist)
        diameter = len(hist) - 1
        counts[order] += 1
        if union_size == 6:
            assert order == 360
            by_incidence[(sig, diameter)] += 1
        else:
            assert order in (12, 60)
        if support_family == ((0, 1, 2), (0, 3, 4), (1, 3, 5)) and bits in ((0, 0, 0), (0, 1, 0)):
            example[str(bits)] = dict(diameter=diameter, depth_histogram=hist, order=order)

assert sum(counts.values()) == 9120
assert counts == {12: 480, 60: 4800, 360: 3840}, counts
by_diameter = Counter()
for (sig, diam), count in by_incidence.items():
    by_diameter[diam] += count
assert by_diameter == {7: 720, 8: 240, 9: 2160, 10: 720}, by_diameter
assert len(by_incidence) == 5, by_incidence
assert example['(0, 0, 0)'] == {'diameter': 7, 'depth_histogram': (1,3,9,24,63,135,115,10), 'order': 360}
assert example['(0, 1, 0)'] == {'diameter': 8, 'depth_histogram': (1,3,9,24,61,124,117,19,2), 'order': 360}

output = {
    'schema': 'R762D_SINGLE_CHIRALITY_TRIAD_MONOID_EXACT_V1',
    'scope': 'candidate six-port labelled permutation monoid, not native physical triad admission',
    'ports': 6,
    'support_types': len(SUPPORTS),
    'three_support_sets': len(all_supports),
    'orientation_alphabets_enumerated': sum(counts.values()),
    'group_size_frequencies': {str(k): counts[k] for k in sorted(counts)},
    'full_A6_directed_alphabets': counts[360],
    'directed_A6_diameter_frequencies': {str(k): by_diameter[k] for k in sorted(by_diameter)},
    'full_A6_by_incidence_and_diameter': [
        {'pair_intersections': list(sig[0]), 'triple_intersection': sig[1], 'diameter': d, 'directed_alphabets': n}
        for (sig, d), n in sorted(by_incidence.items())
    ],
    'optimal_three_supports': [[0,1,2], [0,3,4], [1,3,5]],
    'example_orientation_bit_0_forward_1_reverse': example,
    'minimal_directed_event_types_for_A6': 3,
    'sharp_optimal_directed_event_diameter': min(by_diameter),
    'validation': 'complete exact integer tuple-permutation BFS for all 1,140 sets times 8 chirality choices; each finite generated monoid fully explored',
}
print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
