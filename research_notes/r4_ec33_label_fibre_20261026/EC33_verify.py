#!/usr/bin/env python3
"""EC33: exact labelled positive-source BRC refutation of scalar-observer fidelity.

Run with Python 3 standard library. This tests the specifically declared positive
branch carrier, not a P000 heartbeat update or any phase/signed amplitude model.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

LABELS = ('R', 'B')


def transitions_u(state: int, label: str):
    assert state == 0 and label in LABELS
    return ((0, 1),)


def transitions_v(H: int, state: int, label: str):
    assert H >= 1 and 0 <= state <= H and label in LABELS
    if state < H:
        return ((state + 1, 1),)
    return ((H, 2),) if label == 'R' else ()


def weight_for_labels(H: int, labels: tuple[str, ...], model: str) -> int:
    counts = {0: 1}
    for lab in labels:
        nxt = defaultdict(int)
        for s, multiplicity in counts.items():
            edges = transitions_u(s, lab) if model == 'U' else transitions_v(H, s, lab)
            for t, source_multiplicity in edges:
                nxt[t] += multiplicity * source_multiplicity
        counts = nxt
    return sum(counts.values())


def observer_histogram(H: int, n: int, model: str):
    return {''.join(w): weight_for_labels(H, w, model) for w in product(LABELS, repeat=n)}


def total_by_step_dp(H: int, n: int, model: str) -> int:
    counts = {0: 1}
    for _ in range(n):
        nxt = defaultdict(int)
        for s, multiplicity in counts.items():
            for lab in LABELS:
                edges = transitions_u(s, lab) if model == 'U' else transitions_v(H, s, lab)
                for t, source_multiplicity in edges:
                    nxt[t] += multiplicity * source_multiplicity
        counts = nxt
    return sum(counts.values())


def total_variation(h1, h2):
    a, b = sum(h1.values()), sum(h2.values())
    assert a > 0 and b > 0 and h1.keys() == h2.keys()
    return sum((abs(Fraction(h1[w], a) - Fraction(h2[w], b)) for w in h1), Fraction(0)) / 2


def verify():
    all_cases = []
    compared = 0
    dp_checks = 0
    total_checks = 0
    tv_checks = 0
    for H in range(1, 9):
        for n in range(H + 5):
            U = observer_histogram(H, n, 'U')
            V = observer_histogram(H, n, 'V')
            assert len(U) == 2 ** n
            assert all(x == 1 for x in U.values())
            expected = (lambda w: 1) if n <= H else (lambda w: 2 ** (n - H) if w[H:] == 'R' * (n - H) else 0)
            for word, val in V.items():
                assert val == expected(word)
                compared += 1
            assert sum(V.values()) == sum(U.values()) == 2 ** n
            assert total_by_step_dp(H, n, 'U') == 2 ** n
            assert total_by_step_dp(H, n, 'V') == 2 ** n
            dp_checks += 2
            total_checks += 1
            if n <= H:
                assert V == U
                assert total_variation(U, V) == 0
            else:
                assert V != U
                assert V['R' * H + 'B' + 'R' * (n - H - 1)] == 0
                expected_tv = Fraction(2 ** (n - H) - 1, 2 ** (n - H))
                assert total_variation(U, V) == expected_tv
                tv_checks += 1
        n = H + 1
        assert weight_for_labels(H, tuple('R' * H + 'B'), 'U') == 1
        assert weight_for_labels(H, tuple('R' * H + 'B'), 'V') == 0
        assert weight_for_labels(H, tuple('R' * n), 'U') == 1
        assert weight_for_labels(H, tuple('R' * n), 'V') == 2
        all_cases.append({
            'H': H,
            'dimensions_U_V': [1, H + 1],
            'sharp_refined_alphabet_cutoff': H + 1,
            'first_label_witness': 'R' * H + 'B',
            'witness_counts_U_V': [1, 0],
            'equal_total_source_count_at_every_depth': '2^n (proven by row sums)',
            'label_total_variation_for_n_gt_H': '1 - 2^(H-n) (proven exactly)',
            'last_checked_depth': H + 4,
            'last_checked_tv_fraction': f'{2**4-1}/{2**4}'
        })
    return {
        'schema': 'EM_R4_EC33_LABEL_FIBRE_VERIFICATION_V1',
        'status': 'PASS',
        'input_semantics': 'positive ordered branch BRC, one operation A, observed source labels R/B, distinguishable microscopic red alternatives represented as multiplicity 2',
        'source': 'EC32 R4 exact finite-state rational reachable-span theorem; this verification enumerates refined labels and independently sums state transitions',
        'native_heartbeat_executed': False,
        'H_range': '1..8',
        'label_words_checked': compared,
        'independent_unlabelled_DP_checks': dp_checks,
        'aggregate_source_counts_checked': total_checks,
        'nonzero_exact_TV_checks': tv_checks,
        'examples': all_cases,
        'universal_proofs_in_note': True,
        'next_question': 'Native X6 source-labelled transition and ports: do labels form a globally coherent finite refined alphabet, and can a source-fibre-preserving simulation or finite labelled Hankel certificate be established?'
    }


if __name__ == '__main__':
    res = verify()
    out = Path(__file__).with_name('EC33_REPORT.json')
    out.write_text(json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': res['status'], 'label_words_checked': res['label_words_checked'], 'independent_unlabelled_DP_checks': res['independent_unlabelled_DP_checks'], 'tv_checks': res['nonzero_exact_TV_checks']}, ensure_ascii=False))
