#!/usr/bin/env python3
"""R284DG: sharp quadratic two-bit winner-label code on frozen R284CO Port model.

Requires R284CO_spectral_witness_checker.py in the same directory. Standard
library only; all distance and code operations use exact integers/GF(2).
"""
import hashlib
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from R284CO_spectral_witness_checker import FROZEN_SHA, arcs, dist, words

# Label bit x_i = (L >> i) & 1. Two degree-2 GF(2) polynomials.
F0_MONOMIAL_MASKS = (0, 1, 4, 3, 9, 34, 24)
F1_MONOMIAL_MASKS = (0, 1, 4, 8, 16, 9, 40)
CLIQUE = (1, 8, 62, 63)


def evaluate(label, monomials):
    return sum((label & mask) == mask for mask in monomials) % 2


def code(label):
    return evaluate(label, F0_MONOMIAL_MASKS) | (evaluate(label, F1_MONOMIAL_MASKS) << 1)


def build_certificate():
    X, A = words(), arcs()  # words() checks 65536 distinct and pinned SHA256.
    by_distance = defaultdict(list)
    winner = []
    for i, x in enumerate(X):
        distances = [dist(x, a) for a in A]
        D = max(distances)
        labels = [j for j, d in enumerate(distances) if d == D]
        assert len(labels) == 1, (i, labels)
        winner.append((D, labels[0]))
        by_distance[D].append(i)

    conflicts = set()
    pair_count = 0
    for ids in by_distance.values():
        for i, j in combinations(ids, 2):
            pair_count += 1
            u, v = winner[i][1], winner[j][1]
            assert u != v
            conflicts.add(tuple(sorted((u, v))))
    assert (len(by_distance), pair_count, len(conflicts)) == (65139, 420, 84)
    assert all(tuple(sorted(pair)) in conflicts for pair in combinations(CLIQUE, 2))

    colors = [code(u) for u in range(64)]
    assert len(set(colors)) == 4
    assert all(colors[u] != colors[v] for u, v in conflicts)
    assert len({(d, colors[label]) for d, label in winner}) == len(X)
    assert max(mask.bit_count() for mask in F0_MONOMIAL_MASKS + F1_MONOMIAL_MASKS) == 2

    # The K4 forces rank two for an affine code. All 63 choose 2 rank-two
    # mask pairs are tested; affine offsets never affect color equality.
    tested = 0
    affine_solutions = 0
    for a in range(1, 64):
        for b in range(a + 1, 64):
            tested += 1
            if all((((u & a).bit_count() & 1, (u & b).bit_count() & 1) !=
                    ((v & a).bit_count() & 1, (v & b).bit_count() & 1))
                   for u, v in conflicts):
                affine_solutions += 1
    assert (tested, affine_solutions) == (1953, 0)

    graph_bytes = json.dumps(sorted(conflicts), separators=(',', ':')).encode()
    palette_bytes = bytes(colors)
    return {
        'schema': 'R284DG_SHARP_QUADRATIC_TWO_BIT_WINNER_LABEL_CODE_V1',
        'frozen_source': 'R284CO_spectral_witness_checker.py',
        'frozen_word_sha256': FROZEN_SHA,
        'frozen_sites': len(X),
        'frozen_arcs': len(A),
        'exact_direct_distance_evaluations': len(X) * len(A),
        'unique_winner_sites': len(X),
        'distinct_farthest_values': len(by_distance),
        'colliding_unordered_site_pairs': pair_count,
        'distinct_conflict_edges': len(conflicts),
        'conflict_edges_sha256': hashlib.sha256(graph_bytes).hexdigest(),
        'K4_lower_bound_labels': list(CLIQUE),
        'minimum_color_count': 4,
        'minimum_Gf2_polynomial_degree_of_any_two_output_bit_label_encoder': 2,
        'all_affine_rank_two_mask_pairs_tested': tested,
        'successful_affine_rank_two_mask_pairs': affine_solutions,
        'f0_monomial_masks': list(F0_MONOMIAL_MASKS),
        'f1_monomial_masks': list(F1_MONOMIAL_MASKS),
        'total_anf_monomial_occurrences': len(F0_MONOMIAL_MASKS) + len(F1_MONOMIAL_MASKS),
        'code_lookup_64_labels': colors,
        'code_lookup_sha256': hashlib.sha256(palette_bytes).hexdigest(),
        'code_color_histogram': {str(k): v for k, v in sorted(Counter(colors).items())},
        'all_65536_observations_injective': True,
        'project_review': 'NOT_REVIEWED',
        'scope': 'Exact finite frozen 34-bit Port auxiliary observer; no native X6 operational-fidelity transfer',
    }


def main():
    result = build_certificate()
    path = Path(__file__).with_name('R284DG_quadratic_label_residual_certificate.json')
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in (
        'frozen_sites', 'distinct_conflict_edges',
        'minimum_Gf2_polynomial_degree_of_any_two_output_bit_label_encoder',
        'total_anf_monomial_occurrences', 'conflict_edges_sha256',
        'code_lookup_sha256'
    )}, indent=2))


if __name__ == '__main__':
    main()
