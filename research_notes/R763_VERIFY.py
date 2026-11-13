#!/usr/bin/env python3
"""R763 exact-length saturation of directed 3-cycle alphabets on six labelled ports.
Finite exhaustive integer-permutation certificate; stdlib only.
"""
import itertools
import json
from collections import Counter, defaultdict

N = 6
IDENTITY = tuple(range(N))
SUPPORTS = tuple(itertools.combinations(range(N), 3))


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def positive_cycle(s):
    a, b, c = s
    p = list(IDENTITY)
    p[a], p[b], p[c] = b, c, a
    return tuple(p)


def inverse(p):
    q = [0] * N
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q)


def sign_even(p):
    return sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N)) % 2 == 0


EVEN = tuple(p for p in itertools.permutations(range(N)) if sign_even(p))
assert len(EVEN) == 360 and EVEN[0] == IDENTITY
INDEX = {p: i for i, p in enumerate(EVEN)}
CYCLES = tuple(g for s in SUPPORTS for g in (positive_cycle(s), inverse(positive_cycle(s))))
T = tuple(tuple(INDEX[compose(p, g)] for p in EVEN) for g in CYCLES)


def incidence(family):
    ss = tuple(set(SUPPORTS[i]) for i in family)
    return (tuple(sorted(len(a & b) for a, b in itertools.combinations(ss, 2))),
            len(set.intersection(*ss)))


def full_run(family, bits):
    moves = [T[2 * i + bit] for i, bit in zip(family, bits)]
    current, seen = {0}, {0}
    diameter, saturation = None, None
    sizes = [1]
    for n in range(1, 25):
        current = {move[p] for move in moves for p in current}
        seen |= current
        sizes.append(len(current))
        if len(seen) == 360 and diameter is None:
            diameter = n
        if len(current) == 360:
            saturation = n
            break
    assert diameter is not None and saturation is not None
    assert len(current) == 360
    return diameter, saturation, sizes


size_counts = Counter()
saturation_counts = Counter()
diameter_saturation = Counter()
by_incidence = Counter()
example = {}
for family in itertools.combinations(range(20), 3):
    union = set().union(*(SUPPORTS[i] for i in family))
    for bits in itertools.product((0, 1), repeat=3):
        if len(union) == 6:
            d, s, sizes = full_run(family, bits)
            size_counts[360] += 1
            saturation_counts[s] += 1
            diameter_saturation[(d, s)] += 1
            by_incidence[(incidence(family), s)] += 1
            if tuple(SUPPORTS[i] for i in family) == ((0, 1, 2), (0, 3, 4), (1, 3, 5)) and bits in ((0, 0, 0), (0, 1, 0)):
                example[str(bits)] = {'shortest_diameter': d, 'saturation_index': s,
                                      'exact_length_reachable_sizes': sizes}
        else:
            moves = [T[2 * i + bit] for i, bit in zip(family, bits)]
            seen, frontier = {0}, {0}
            while frontier:
                new = {move[p] for move in moves for p in frontier} - seen
                seen |= new
                frontier = new
            assert len(seen) in (12, 60)
            size_counts[len(seen)] += 1

assert size_counts == {12: 480, 60: 4800, 360: 3840}
assert saturation_counts == {8: 720, 9: 720, 10: 960, 12: 720, 13: 720}
assert diameter_saturation == {(7, 8): 720, (8, 10): 240, (9, 9): 720,
                               (9, 12): 720, (9, 13): 720, (10, 10): 720}
assert example['(0, 0, 0)']['exact_length_reachable_sizes'] == [1,3,9,25,66,153,283,348,360]
assert example['(0, 1, 0)']['saturation_index'] == 10
assert sum(size_counts.values()) == 9120

# Independent direct word enumeration for 7/8 steps of the optimal generator triple.
G = [positive_cycle(s) for s in ((0, 1, 2), (0, 3, 4), (1, 3, 5))]
for length, expected in ((7, 348), (8, 360)):
    words = set()
    for choices in itertools.product(range(3), repeat=length):
        cur = IDENTITY
        for k in choices:
            cur = compose(cur, G[k])
        words.add(cur)
    assert len(words) == expected

# Explicit coprime identity lengths: g^3 and (g*h)^5, intersection-one supports.
assert compose(G[0], compose(G[0], G[0])) == IDENTITY
pair = compose(G[0], G[1])
q = IDENTITY
for _ in range(5):
    q = compose(q, pair)
assert q == IDENTITY

result = {
    'schema': 'R763_DIRECTED_TRIAD_EXACT_LENGTH_SATURATION_V1',
    'scope': 'conditional repeatable six-label A6 candidate, not certified native triadic force',
    'support_families': 1140,
    'directed_alphabets': 9120,
    'generated_group_orders': {str(k): size_counts[k] for k in sorted(size_counts)},
    'A6_alphabets': 3840,
    'saturation_index_distribution': {str(k): saturation_counts[k] for k in sorted(saturation_counts)},
    'shortest_diameter_vs_saturation_index': [
        {'diameter': d, 'saturation_index': s, 'alphabets': count}
        for (d, s), count in sorted(diameter_saturation.items())
    ],
    'saturation_by_support_incidence': [
        {'pair_intersections': list(sig[0]), 'triple_intersection': sig[1],
         'saturation_index': s, 'alphabets': count}
        for (sig, s), count in sorted(by_incidence.items())
    ],
    'minimum_saturation_index': min(saturation_counts),
    'maximum_saturation_index': max(saturation_counts),
    'optimal_example_supports': [[0,1,2],[0,3,4],[1,3,5]],
    'example_orientations': example,
    'direct_word_crosscheck_lengths': {'7':348, '8':360},
    'identity_loop_lengths_verified': [3, 10],
    'validation': 'Exhaustive 9120 event alphabets, tuple permutation index, every exact-length reachable set until full; independent direct 3^7 and 3^8 word enumeration for the optimal example.'
}
print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
