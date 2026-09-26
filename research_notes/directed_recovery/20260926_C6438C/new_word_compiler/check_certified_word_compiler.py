"""Bounded actual-word fixtures, cursor continuation, and certificate tampering.

This executes no ideal reference and no unbounded/explosive word search.
"""
from __future__ import annotations
import copy
import gzip
import json
from fractions import Fraction as F
from pathlib import Path

import certified_word_compiler as compiler
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent


def rejects(action):
    try:
        action()
    except (ValueError, KeyError, TypeError):
        return True
    raise AssertionError('tampered input was accepted')


def main():
    start = len(CALLS)
    seeds = ((('neg', 0),), compiler.QUARTER_WORD)
    empty = compiler.compile_phase(2, F(1, 1 << 40), seeds=seeds,
                                    pair_budget=0, observer_start_bits=3)
    assert empty['status'] == 'PARTIAL' and len(CALLS) == start
    first = compiler.compile_phase(2, F(1, 1 << 40), seeds=seeds,
        cursor=empty['cursor'], pair_budget=1, observer_start_bits=3)
    assert first['status'] == 'PARTIAL'
    assert first['events'][0]['status'] == 'SKIPPED_NEGATIVE_DETERMINANT'
    assert len(CALLS) == start
    quarter = compiler.compile_phase(2, F(1, 1 << 40), seeds=seeds,
        cursor=first['cursor'], pair_budget=2, observer_start_bits=3)
    assert quarter['status'] == 'CERTIFIED'
    assert quarter['certificate']['error_observer']['frobenius_squared_upper'] == '0'
    quarter_replay = compiler.verify_phase_record(quarter)

    old_seeds = compiler.load_legacy_seed_words(max_m=3)
    phase3 = compiler.compile_phase(3, F(1, 64), seeds=old_seeds[3],
                                    pair_budget=1, observer_start_bits=18)
    assert phase3['status'] == 'CERTIFIED'
    phase3_replay = compiler.verify_phase_record(phase3)

    # A deep phase at deliberately shallow observer depth exercises the exact
    # closed-zero endpoint extension. It is an observer, not new gate synthesis.
    shallow = compiler.isolate_target(12, 3)
    assert shallow['lower'] == '0' and F(shallow['upper']) > 0

    bank0 = compiler.compile_phase_bank(3, F(1, 16), seed_words=old_seeds,
        pair_budget=0, observer_start_bits=18)
    assert bank0['status'] == 'PARTIAL' and bank0['phases'] == {}
    bank1 = compiler.compile_phase_bank(3, F(1, 16), seed_words=old_seeds,
        cursor=bank0['cursor'], pair_budget=1, observer_start_bits=18)
    assert bank1['status'] == 'PARTIAL' and set(bank1['phases']) == {'2'}
    bank2 = compiler.compile_phase_bank(3, F(1, 16), seed_words=old_seeds,
        cursor=bank1['cursor'], pair_budget=1, observer_start_bits=18)
    assert bank2['status'] == 'CERTIFIED' and set(bank2['phases']) == {'2', '3'}
    assert F(bank2['occurrence_weighted_error_bound']) == F(1, 32)

    bad_word = copy.deepcopy(phase3)
    bad_word['word'] = []
    bad_bound = copy.deepcopy(phase3)
    bad_bound['operator_error_bound'] = '0'
    bad_column = copy.deepcopy(phase3['certificate'])
    bad_column['actual_columns']['complete_basis_columns'][0]['numerators'][0] += 1
    bad_margin = copy.deepcopy(phase3['certificate'])
    bad_margin['error_observer']['strict_margin'] = '1'
    bad_bank_cursor = copy.deepcopy(bank1['cursor'])
    bad_bank_cursor['phases']['2']['word'] = []
    negatives = {
        'record_word_substitution': rejects(lambda: compiler.verify_phase_record(bad_word)),
        'unsupported_smaller_error': rejects(lambda: compiler.verify_phase_record(bad_bound)),
        'column_tampering_full_replay': rejects(lambda: compiler.verify_certificate(bad_column)),
        'strict_margin_tampering_full_replay': rejects(lambda: compiler.verify_certificate(bad_margin)),
        'completed_cursor_word_substitution': rejects(lambda: compiler.compile_phase_bank(
            3, F(1, 16), seed_words=old_seeds, cursor=bad_bank_cursor,
            pair_budget=0, observer_start_bits=18)),
        'cursor_target_substitution': rejects(lambda: compiler.compile_phase(
            3, F(1, 64), seeds=seeds, cursor=empty['cursor'], pair_budget=0)),
    }
    assert len(compiler.ALPHABET) == 62
    assert compiler.unrank_word(0) == ()
    assert compiler.unrank_word(1) == (compiler.ALPHABET[0],)
    assert compiler.unrank_word(62) == (compiler.ALPHABET[-1],)
    assert compiler.unrank_word(63) == (compiler.ALPHABET[0], compiler.ALPHABET[0])
    schedule, stage, offset = [], 0, 0
    for _ in range(10):
        schedule.append([stage, offset, 3+stage-offset])
        stage, offset = compiler.advance(stage, offset)
    assert schedule == [[0,0,3],[1,0,4],[1,1,3],[2,0,5],[2,1,4],
                        [2,2,3],[3,0,6],[3,1,5],[3,2,4],[3,3,3]]
    report = {'schema': 'FIXED_WORD_COMPILER_BOUNDED_CHECKS_V1',
        'status': 'AUTHOR_ACTUAL_BOUNDED_EXECUTION_NOT_ADMITTED',
        'activity': compiler.ACTIVITY, 'source': compiler.source_binding(),
        'fixtures': {'m2_quarter': quarter, 'm3_native_legacy_seed': phase3},
        'replays': [quarter_replay, phase3_replay],
        'closed_zero_observer_m12_b3': shallow,
        'bank_zero_budget': bank0, 'bank_partial': bank1, 'bank_resumed': bank2,
        'negative_controls': negatives, 'first_ten_dovetail_pairs': schedule,
        'actual_core_call_count': len(CALLS)-start,
        'actual_core_calls': CALLS[start:],
        'scope': 'm2 exact and one m3 seeded word; bounded cursor/resume and negative controls',
        'ideal_reference_execution': False, 'unbounded_search_executed': False,
        'legacy_target32_vector64_modified': False}
    raw = compiler.packed(report)
    path = ROOT / 'CERTIFIED_WORD_COMPILER_CHECKS.json.gz'
    path.write_bytes(gzip.compress(raw, mtime=0))
    summary = {'status': report['status'], 'artifact': path.name,
        'payload_sha256': compiler.digest(report),
        'm2_error_squared_upper': quarter['certificate']['error_observer']['frobenius_squared_upper'],
        'm3_error_squared_upper': phase3['certificate']['error_observer']['frobenius_squared_upper'],
        'm3_tolerance': phase3['operator_error_bound'],
        'm3_word_length': len(phase3['word']), 'bank_resume_status': bank2['status'],
        'negative_controls': negatives, 'actual_core_call_count': len(CALLS)-start}
    (ROOT / 'CERTIFIED_WORD_COMPILER_SUMMARY.json').write_text(
        json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
