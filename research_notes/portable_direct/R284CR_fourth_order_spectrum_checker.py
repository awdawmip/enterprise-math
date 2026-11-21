#!/usr/bin/env python3
"""R284CR: Exact fourth Port spectrum and its unique minimum 248-site core.
Place beside R284CO_spectral_witness_checker.py and R284CO/CP/CQ certificates.
"""
import hashlib
import heapq
import json
from collections import Counter
from pathlib import Path
from R284CO_spectral_witness_checker import P, D, Z, SELECT, FROZEN_SHA, words, arcs, dist


def compute():
    X, A = words(), arcs()  # words() checks frozen SHA-256 and 65,536 distinct sites.
    heaps = [[] for _ in range(64)]
    for index, x in enumerate(X):
        for j, value in enumerate(sorted(dist(x, arc) for arc in A)):
            pair = (value, index)
            if len(heaps[j]) < 5:
                heapq.heappush(heaps[j], pair)
            elif pair > heaps[j][0]:
                heapq.heapreplace(heaps[j], pair)
    rows = [sorted(h, reverse=True) for h in heaps]
    assert all(len(row) == 5 for row in rows)
    assert all(row[2][0] > row[3][0] > row[4][0] for row in rows[1:])
    prior = {X[index] for row in rows[1:] for _, index in row[:3]}
    fourth = [X[row[3][1]] for row in rows[1:]]
    fourth_set = set(fourth)
    core = prior | fourth_set
    assert len(prior) == 186 and len(fourth_set) == 62 and not (prior & fourth_set)
    assert len(core) == 248
    assert Counter(fourth).most_common(1) == [(3347474639, 2)]
    assert fourth[4] == fourth[17] == 3347474639
    assert all(sorted((sorted(dist(x, a) for a in A)[j] for x in core), reverse=True)[:4]
               == [value for value, _ in rows[j][:4]] for j in range(1, 64))
    with open('R284CO_spectral_witness_certificate.json', encoding='utf-8') as f:
        co = json.load(f)
    with open('R284CP_127_sweep_witness_certificate.json', encoding='utf-8') as f:
        cp = json.load(f)
    with open('R284CQ_third_spectrum_certificate.json', encoding='utf-8') as f:
        cq = json.load(f)
    assert [row[0][0] for row in rows] == co['U_all_64']
    assert [X[row[0][1]] for row in rows[1:]] == co['winner_residue_k2_to_k64']
    assert [X[row[1][1]] for row in rows[1:]] == cp['unique_runner_up_residues_k2_to_k64']
    assert [row[2][0] for row in rows[1:]] == cq['third_values_k2_to_k64']
    assert [X[row[2][1]] for row in rows[1:]] == cq['third_witness_residues_k2_to_k64']
    digest = hashlib.sha256(b''.join(x.to_bytes(8,'big') for x in sorted(core))).hexdigest()
    return {
        'schema': 'R284CR_FOURTH_ORDER_PORT_SPECTRUM_V1',
        'status': 'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'pins': {'P': P, 'D': list(D), 'Z': list(Z), 'SELECT': list(SELECT), 'frozen_sha256': FROZEN_SHA},
        'counts': {'population': len(X), 'arc_count': len(A), 'exact_site_arc_distances': len(X)*len(A),
                   'top3_core': len(prior), 'fourth_unique_sites': len(fourth_set),
                   'fourth_overlap_top3': len(fourth_set & prior), 'minimum_top4_core': len(core)},
        'fourth_values_k2_to_k64': [row[3][0] for row in rows[1:]],
        'fourth_witness_residues_k2_to_k64': fourth,
        'fourth_witness_indices_k2_to_k64': [row[3][1] for row in rows[1:]],
        'third_to_fourth_gap_k2_to_k64': [row[2][0]-row[3][0] for row in rows[1:]],
        'fourth_to_fifth_gap_k2_to_k64': [row[3][0]-row[4][0] for row in rows[1:]],
        'fourth_witness_duplicate': {'ranks': [6,19], 'residue': 3347474639},
        'minimum_third_to_fourth_gap': min(row[2][0]-row[3][0] for row in rows[1:]),
        'minimum_fourth_to_fifth_gap': min(row[3][0]-row[4][0] for row in rows[1:]),
        'core_sorted_sha256_u64be': digest,
        'verification': {'full_population': True, 'top_four_reproduced_on_248_site_core': True,
                         'all_fourth_witnesses_unique_at_their_level': True,
                         'crosschecked_existing_top_three_certificates': True,
                         'independent_review': 'NOT_REVIEWED'}
    }


if __name__ == '__main__':
    record = compute()
    Path('R284CR_fourth_order_spectrum_certificate.json').write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'core':record['counts']['minimum_top4_core'],
                      'gap34':record['minimum_third_to_fourth_gap'],
                      'gap45':record['minimum_fourth_to_fifth_gap'],
                      'core_sha256':record['core_sorted_sha256_u64be']}))
