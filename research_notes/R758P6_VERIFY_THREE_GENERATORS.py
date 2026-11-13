#!/usr/bin/env python3
"""R758P6: sparse 3-generator flat-area A7 candidate-frame theorem.
Exact integer and permutation arithmetic, standard library only.
"""
from collections import Counter, deque
from itertools import combinations
import json

I = tuple(range(7))

def mul(a, b):
    return tuple(a[b[k]] for k in range(7))

def inverse(a):
    return tuple(a.index(k) for k in range(7))

def transposition(i):
    p = list(I)
    p[0], p[i] = p[i], p[0]
    return tuple(p)
T = {i: transposition(i) for i in range(1, 7)}

def W(i, j):
    assert 1 <= i < j <= 6
    return ((i, 1), (j, 1), (i, -1), (j, -1),
            (i, 1), (j, -1), (i, -1), (j, 1))

def area_and_endpoint(word):
    x = [0] * 7
    pairs = list(combinations(range(1, 7), 2))
    A = {ij: 0 for ij in pairs}
    for axis, sign in word:
        for a in range(1, axis):
            A[a, axis] += x[a] * sign
        x[axis] += sign
    return tuple(x), tuple(A.values())

def frame(word):
    h = I
    for axis, sign in word:
        assert axis in T and sign in (-1, 1)
        h = mul(T[axis], h)
    return h

def word_inverse(word):
    return tuple((axis, -sign) for axis, sign in reversed(word))

def is_even(g):
    return sum(g[i] > g[j] for i in range(7) for j in range(i+1, 7)) % 2 == 0

def bfs(generators):
    steps = list(generators) + [inverse(g) for g in generators]
    distance = {I: 0}
    queue = deque((I,))
    while queue:
        g = queue.popleft()
        for h in steps:
            gh = mul(h, g)
            if gh not in distance:
                distance[gh] = distance[g] + 1
                queue.append(gh)
    return distance

def perfect_matchings(items):
    if not items:
        yield ()
        return
    a = items[0]
    for b in items[1:]:
        others = tuple(x for x in items[1:] if x != b)
        for rest in perfect_matchings(others):
            yield ((a, b),) + rest

def verify():
    pairs = ((1, 2), (3, 4), (5, 6))
    G = []
    all_witnesses = 0
    for i, j in combinations(range(1, 7), 2):
        w = W(i, j)
        assert area_and_endpoint(w) == ((0,)*7, (0,)*15)
        assert frame(w) == mul(T[j], T[i])
        wi = word_inverse(w)
        assert area_and_endpoint(wi) == ((0,)*7, (0,)*15)
        assert frame(wi) == inverse(frame(w))
        all_witnesses += 1
    for i, j in pairs:
        G.append(frame(W(i, j)))
    subgroups = [len(bfs(G[:k])) for k in (1, 2, 3)]
    assert subgroups == [3, 60, 2520]
    distances = bfs(G)
    histogram = dict(sorted(Counter(distances.values()).items()))
    assert histogram == {0:1,1:6,2:24,3:96,4:312,5:714,6:967,7:358,8:36,9:6}
    assert len(distances) == 2520 and all(is_even(g) for g in distances)
    assert max(distances.values()) == 9
    assert sum(histogram.values()) == 2520
    matchings = list(perfect_matchings(tuple(range(1, 7))))
    assert len(matchings) == 15
    for m in matchings:
        metric = bfs([frame(W(i,j)) for i,j in m])
        assert len(metric) == 2520
        assert Counter(metric.values()) == Counter(histogram)
    result = {
        'schema': 'R758P6_SPARSE_FLAT_A7_EXACT_V1',
        'frozen_science': 'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'candidate_frame_labels': 7,
        'native_space_dimensions': 6,
        'canonical_Wij_witnesses_rechecked': all_witnesses,
        'selected_generators': [[i,j] for i,j in pairs],
        'single_generator_subgroup_orders': subgroups,
        'generated_subgroup': 'A7',
        'subgroup_order': len(distances),
        'minimal_canonical_Wij_generator_count': 3,
        'perfect_matching_generator_bases_verified': len(matchings),
        'full_S6_invariant_nonempty_Wij_library_size': 15,
        'symmetric_word_metric_diameter': max(distances.values()),
        'histogram': {str(k): v for k,v in histogram.items()},
        'max_primitive_steps_for_any_frame': 8*max(distances.values()),
        'full_native_triadic_event': 'UNRESOLVED',
        'result': 'PASS'
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__ == '__main__':
    verify()
