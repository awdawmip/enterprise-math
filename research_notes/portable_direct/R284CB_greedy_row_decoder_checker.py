#!/usr/bin/env python3
"""Exact R284CB checker for the greedy first-row decoder of frozen R284BZ.

Standalone stdlib-only reproducible certificate. All core arithmetic is exact.
Finite domain: 4096 lower blocks, 16 upper rows, three integer error samples.
"""
from bisect import bisect_left, bisect_right
from fractions import Fraction
from hashlib import sha256
from itertools import product
from json import dumps
from pathlib import Path

P = 17179869143
D0, D3, Z1, Z2, Z3 = 1120832, 1651128, 390139, 394465, 1497639
R = Fraction(59, 2)


def block_record(L):
    u1, a11, x, y, u2, w, a22, z, u3, g, h, r = L
    t, s = 6 - a11, 13 - a22
    U = t * s - x * w
    V = -r * U - z * (t * h + x * g) - y * (w * h + s * g)
    p1, p2 = s * u1 + x * u2, t * u2 + w * u1
    q1 = -r * p1 - u1 * z * h + x * z * u3 + y * (u2 * h + s * u3)
    q2 = -r * p2 + t * z * u3 + u1 * z * g + y * (w * u3 - u2 * g)
    q3 = U * u3 + p1 * g + p2 * h
    ks = (U * D3 + V, p1 * D3 + q1, p2 * D3 + q2, q3)
    base = (D0 * ks[0] - Z1 * ks[1] - Z2 * ks[2] - Z3 * ks[3] - sum(ks)) % P
    return base, ks


def codeword(rec, bits):
    base, ks = rec
    return (base - sum(ks[j] for j in range(4) if (bits >> j) & 1)) % P


def greedy_from_lift(delta, ks):
    bits, residual = 0, delta
    for j in range(4):
        subordinate = sum(ks[j + 1:])
        bit = int(2 * residual > ks[j] + subordinate)
        bits |= bit << j
        residual -= bit * ks[j]
    return (bits, residual) if abs(residual) < R else (None, residual)


def lift(base, observed, span):
    delta = (base - observed) % P
    if delta > span + R:
        delta -= P
    return delta if -R <= delta <= span + R else None


def prepare_index(records):
    sorted_base = sorted((base, i) for i, (base, _) in enumerate(records))
    ext = sorted((base + shift, i) for base, i in sorted_base for shift in (-P, 0, P))
    return ext, [base for base, _ in ext], max(sum(k) for _, k in records)


def grouped_greedy(observed, records, index):
    ext, bases, max_span = index
    query = observed % P
    start = bisect_left(bases, query - R)
    stop = bisect_right(bases, query + max_span + R)
    candidates = set()
    for i in range(start, stop):
        block_id = ext[i][1]
        base, ks = records[block_id]
        delta = lift(base, query, sum(ks))
        if delta is None:
            continue
        bits, residual = greedy_from_lift(delta, ks)
        if bits is not None:
            candidates.add((block_id, bits))
    return sorted(candidates)


def verify():
    lower = list(product((1, 2), repeat=12))
    records = [block_record(L) for L in lower]
    margins = [(
        ks[0] - sum(ks[1:]),
        ks[1] - sum(ks[2:]),
        ks[2] - ks[3],
        ks[3],
    ) for _, ks in records]
    minimum = [min(m[i] for m in margins) for i in range(4)]
    maximum = [max(m[i] for m in margins) for i in range(4)]
    assert minimum == [3301944, 1650972, 8255510, 59], minimum
    assert all(all(x >= 59 for x in row) for row in margins)
    index = prepare_index(records)
    ordered = []
    digest = sha256()
    correct_block_tests = 0
    for top in product((1, 2), repeat=4):
        high = sum((top[j] - 1) << j for j in range(4))
        for i, rec in enumerate(records):
            val = codeword(rec, high)
            digest.update(val.to_bytes(8, 'big'))
            ordered.append((val, i, high))
            for err in (-29, 0, 29):
                observed = (val + err) % P
                delta = lift(rec[0], observed, sum(rec[1]))
                assert delta is not None
                bits, residual = greedy_from_lift(delta, rec[1])
                assert (bits, residual) == (high, -err)
                correct_block_tests += 1
    ordered.sort()
    gaps = [b[0] - a[0] for a, b in zip(ordered, ordered[1:])]
    gaps.append(P + ordered[0][0] - ordered[-1][0])
    assert len({x[0] for x in ordered}) == 65536
    assert min(gaps) == 59 and gaps.count(59) == 64
    assert digest.hexdigest() == 'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'
    full_index_tests = 0
    for val, i, high in ordered[::131]:
        for err in (-29, 0, 29, Fraction(117, 4), -Fraction(117, 4)):
            candidates = grouped_greedy((val + err) % P, records, index)
            assert candidates == [(i, high)], (i, high, err, candidates)
            full_index_tests += 1
    return {
        'schema': 'EM_R284CB_GREEDY_PORT_DECODER_V1',
        'predecessor': 'R284CA_4096_BLOCK_SHARP_NOISE_DECODER_20261120.md',
        'prime': P,
        'fixed_diagonal_controls': [6, 13],
        'remaining_controls': [D0, D3, Z1, Z2, Z3],
        'lower_blocks_exhausted': len(records),
        'full_matrices_exhausted': len(ordered),
        'cofactor_superincreasing_min_margins': minimum,
        'cofactor_superincreasing_max_margins': maximum,
        'global_minimum_circular_gap': min(gaps),
        'gap59_multiplicity': gaps.count(59),
        'correct_block_decoding_tests': correct_block_tests,
        'selected_full_index_decoding_tests': full_index_tests,
        'rowmajor_be64_sha256': digest.hexdigest(),
        'uniform_guarantee': 'for every real observation error |epsilon|<29.5, unique decoding for all 65536 matrices',
        'indexed_lower_blocks': 4096,
        'maximum_lower_blocks_per_circle_query': 128,
        'complete_top_row_subset_enumerations_per_lower_block': 0,
        'greedy_bit_thresholds_per_lower_block': 4,
        'full_center_checks_per_lower_block': 1,
        'review': 'NOT_REVIEWED'
    }


if __name__ == '__main__':
    result = verify()
    destination = Path(__file__).with_name('R284CB_greedy_row_decoder_verification.json')
    destination.write_text(dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(dumps(result, indent=2, sort_keys=True))
