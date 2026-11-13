#!/usr/bin/env python3
"""Exact six-axis 3-uniform BRC shadow-fiber enumeration and independent IE count."""
import json
from collections import Counter
from itertools import combinations

V = range(6)
EDGES = tuple(combinations(V, 2))
TRIADS = tuple(combinations(V, 3))
EDGE_INDEX = {e: j for j, e in enumerate(EDGES)}
TRIAD_EDGE_MASK = tuple(sum(1 << EDGE_INDEX[e] for e in combinations(t, 2)) for t in TRIADS)

# Enumerate every source-preserving 20-bit triple-license H; derive its 15-bit pair shadow.
shadow = [0] * (1 << len(TRIADS))
fiber = [0] * (1 << len(EDGES))
for h in range(len(shadow)):
    if h:
        low_bit = h & -h
        shadow[h] = shadow[h ^ low_bit] | TRIAD_EDGE_MASK[low_bit.bit_length() - 1]
    fiber[shadow[h]] += 1

nonempty = [(g, n) for g, n in enumerate(fiber) if n]
counts = Counter(n for _, n in nonempty)
max_count = max(fiber)
max_shadows = [g for g, n in nonempty if n == max_count]
assert max_shadows == [(1 << 15) - 1]
assert len(nonempty) == 6115
assert sum(n * m for n, m in counts.items()) == 1 << 20
assert counts[1] == 2713

# Second computation via edge-avoidance inclusion-exclusion; no 20-bit H enumeration here.
# For each forbidden pair-set S, i3(S) counts triples using none of the forbidden pairs.
ie = 0
for forbidden in range(1 << 15):
    allowed_triads = sum((forbidden & mask) == 0 for mask in TRIAD_EDGE_MASK)
    term = 1 << allowed_triads
    ie += -term if forbidden.bit_count() & 1 else term
assert ie == max_count == 477965
assert (1 << 18) < max_count < (1 << 19)

# A concrete distinct-fiber pair with identical complete shadow, but different source 012.
all_h = (1 << 20) - 1
missing_012 = all_h ^ (1 << TRIADS.index((0, 1, 2)))
assert shadow[all_h] == shadow[missing_012] == (1 << 15) - 1
assert bool(all_h & 1) and not bool(missing_012 & 1)

# Exact rank / unrank for the most ambiguous known shadow, using source-mask order.
rank_check = {}
rank = 0
wanted = {0, 12345, max_count - 1}
for h, g in enumerate(shadow):
    if g == (1 << 15) - 1:
        if rank in wanted:
            rank_check[str(rank)] = h
        rank += 1
assert rank == max_count
assert len(rank_check) == len(wanted)
assert all(shadow[h] == (1 << 15) - 1 for h in rank_check.values())

out = {
    'schema': 'EM_R712_X6_TRIAD_BRC_SHADOW_FIBER_EXACT_V1',
    'domain': {'vertex_count': 6, 'unordered_pair_count': 15, 'unordered_triad_count': 20},
    'total_hypergraph_licenses': 1 << 20,
    'distinct_pair_shadows': len(nonempty),
    'max_fiber_count': max_count,
    'unique_max_shadow_edge_mask': max_shadows[0],
    'worst_case_additional_bits_given_shadow': (max_count - 1).bit_length(),
    'complete_shadow_probability_under_uniform_triad_masks': f'{max_count}/{1<<20}',
    'single_preimage_shadows': counts[1],
    'fiber_size_distribution': {str(k): v for k, v in sorted(counts.items())},
    'independent_edge_inclusion_exclusion_count': ie,
    'complete_shadow_distinct_license_example': [all_h, missing_012],
    'rank_unrank_samples_on_complete_shadow': rank_check,
    'verification': 'EXACT_INTEGER_TWO_METHOD_PASS',
    'status': 'AUTHOR_SIDE_FINITE_PROOF_AND_EXACT_ENUMERATION',
}
print('R712_SHADOW_FIBER_EXACT_PASS', len(nonempty), max_count,
      out['worst_case_additional_bits_given_shadow'], counts[1], ie)
with open('R712_SHADOW_FIBER_RESULTS.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
    f.write('\n')
