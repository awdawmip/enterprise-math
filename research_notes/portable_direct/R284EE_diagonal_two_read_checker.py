#!/usr/bin/env python3
"""R284EE exact classification of translated Port readings.

Run beside the frozen R284CO checker in research_notes/portable_direct.
All arithmetic is exact Python integer, over the full 16-bit source domain.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib, json
from R284CO_spectral_witness_checker import P, FROZEN_SHA, det, arcs, dist

SOURCE_COMMIT = 'acba2d8667903434aaa2a10720f43637fcc2421b'
SOURCE_BLOB = 'b46e0f682b58e47c27094b4bea6fa4e55119a3ee'
PAIR_SHA = '7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a'

def readouts():
    A = arcs()
    residues_hash = hashlib.sha256()
    values = []
    for upper in product((1, 2), repeat=4):
        top = sum((x - 1) << j for j, x in enumerate(upper))
        for lower in product((1, 2), repeat=12):
            z = det(lower, top) % P
            residues_hash.update(z.to_bytes(8, 'big'))
            values.append(max(dist(z, arc) for arc in A))
    assert len(values) == 65536 and len(A) == 64
    assert residues_hash.hexdigest() == FROZEN_SHA
    return values

def pairs_and_minimum(values, offset):
    tuples = sorted((values[i], values[i ^ offset], i) for i in range(65536))
    assert len({(a, b) for a, b, i in tuples}) == 65536
    best = 10**30
    winners = set()
    comparisons = 0
    for k, (a, b, i) in enumerate(tuples):
        j = k - 1
        while j >= 0 and a - tuples[j][0] <= best:
            a0, b0, other = tuples[j]
            comparisons += 1
            d = max(a - a0, abs(b - b0))
            pair = tuple(sorted((i, other)))
            if d < best:
                best, winners = d, {pair}
            elif d == best:
                winners.add(pair)
            j -= 1
    packed = b''.join(i.to_bytes(2, 'big') + j.to_bytes(2, 'big')
                      for i, j in sorted(winners))
    return {'minimum_Linf': best, 'minimizing_unordered_pairs': len(winners),
            'minimizers_sha256': hashlib.sha256(packed).hexdigest(),
            'example': list(min(winners)), 'candidate_comparisons': comparisons}

def close_pairs(values, cap=100):
    tuples = sorted((values[i], values[i ^ 65], i) for i in range(65536))
    out = []
    for k, (a, b, i) in enumerate(tuples):
        j = k - 1
        while j >= 0 and a - tuples[j][0] <= cap:
            aa, bb, other = tuples[j]
            d = abs(b - bb)
            if d <= cap:
                out.append((min(i, other), max(i, other), aa, a - aa,
                            min(b, bb), d))
            j -= 1
    return sorted(out)

def phase_atlas(close, width_limit=101):
    atlas = {}
    witness = {}
    for s in range(1, width_limit + 1):
        hit = bytearray(s)
        for i, j, lo1, d1, lo2, d2 in close:
            if d1 >= s or d2 >= s:
                continue
            for phase in range(s):
                if hit[phase]:
                    continue
                if (lo1 - phase) % s < s - d1 and (lo2 - phase) % s < s - d2:
                    hit[phase] = 1
                    if str(s) not in witness:
                        witness[str(s)] = [i, j, phase]
            if all(hit):
                break
        atlas[str(s)] = sum(hit)
    return atlas, witness

def direct_quantization_check(values, widths=(60, 61, 69, 72)):
    result = {}
    for width in widths:
        row = {}
        for mode, offsets in [('diagonal_two', (0, 65)),
                              ('joint_four', (0, 1, 64, 65))]:
            colliding_phases = 0
            for phase in range(width):
                seen = set()
                for i in range(65536):
                    key = tuple((values[i ^ q] - phase) // width for q in offsets)
                    if key in seen:
                        colliding_phases += 1
                        break
                    seen.add(key)
            row[mode] = colliding_phases
        result[str(width)] = row
    return result

def main():
    values = readouts()
    hist = Counter(Counter(values).values())
    results = {str(delta): pairs_and_minimum(values, delta) for delta in (1, 64, 65)}
    assert [results[str(x)]['minimum_Linf'] for x in (1, 64, 65)] == [14, 53, 60]
    assert results['65']['minimizing_unordered_pairs'] == 256
    assert results['65']['minimizers_sha256'] == PAIR_SHA
    close = close_pairs(values)
    assert len(close) == 11264
    atlas, witness = phase_atlas(close)
    assert all(atlas[str(s)] == 0 for s in range(1, 61))
    assert atlas['61'] == 3 and all(atlas[str(s)] == s for s in range(70, 102))
    direct = direct_quantization_check(values)
    assert all(direct[str(s)]['diagonal_two'] == atlas[str(s)] for s in (60,61,69,72))
    assert [direct[str(s)]['joint_four'] for s in (60,61,69,72)] == [0,0,1,0]
    cert = {
        'schema': 'R284EE_DIAGONAL_TWO_READ_EXACT_CLASSIFICATION_V1',
        'status': 'AUTHOR_EXACT_CHECKED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
        'frozen_source_commit': SOURCE_COMMIT,
        'frozen_source_blob_sha1': SOURCE_BLOB,
        'frozen_codeword_sha256': FROZEN_SHA,
        'source_states': 65536, 'arcs': 64, 'readout_values_distinct': len(set(values)),
        'single_read_multiplicity_histogram': {str(k): v for k, v in sorted(hist.items())},
        'two_read_offset_classification': results,
        'diagonal_two_read_phase_candidates_width_101': len(close),
        'diagonal_two_read_common_phase_collisions_width_1_to_101': atlas,
        'first_diagonal_shared_phase_collision': {'width':61,'pair_and_phase':witness['61']},
        'selected_direct_all_state_checks': direct,
        'scope': 'exact frozen Port auxiliary source and R/W translations only; no native X6 transfer',
        'review': 'NOT_REVIEWED'
    }
    out = Path(__file__).with_name('R284EE_diagonal_two_read_certificate.json')
    out.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'single':cert['single_read_multiplicity_histogram'],
      'pairs':results,'first_phase':cert['first_diagonal_shared_phase_collision'],
      'checks':direct},indent=2))
    return cert

if __name__ == '__main__':
    main()
