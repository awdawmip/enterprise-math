"""Administrative inspection of saved bytes; no native import or science rerun."""
from pathlib import Path
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'trace_bank'


def strict(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False,
                      allow_nan=False).encode()


def sha(x):
    return hashlib.sha256(x).hexdigest()


blob = (SOURCE / 'SO_TRACE_BANK_RESULTS.json.gz').read_bytes()
raw = gzip.decompress(blob)
data = json.loads(raw)
summary = json.loads((SOURCE / 'SO_TRACE_BANK_SUMMARY.json').read_bytes())
cost = json.loads((SOURCE / 'SO_TRACE_COST_ACCOUNTING.json').read_bytes())
assert (sha(blob), len(blob)) == (summary['gzip_sha256'], summary['gzip_bytes'])
assert (sha(raw), len(raw)) == (summary['raw_sha256'], summary['raw_bytes'])
assert data['source_hashes'] == summary['source_hashes'] == cost['source_hashes']
for name, expected in data['source_hashes'].items():
    assert sha((SOURCE / name).read_bytes()) == expected
assert sha((SOURCE / 'extract_so_trace_cost.py').read_bytes()) == cost['extractor_sha256']
assert data['status'] == summary['status'] == 'PASSED'
assert len(data['actual_core_calls']) == data['core_call_count'] == summary['core_call_count'] == 722
start = data['initial_native_bank_admission_call_interval'][0]
banks = [(name, data[name]) for name in ('encoded_bank', 'complete_bank', 'restored_bank')]
banks += [('special:' + item['case'], item['bank']) for item in data['special_words']]
negatives = []
for item in data['negative_controls']:
    assert item['rejected'] is True
    a, b = item['call_interval']
    assert b - a == item['actual_core_calls']
    ev = item['failed_fresh_replay_evidence']
    if ev is not None:
        assert item['type'] == 'TraceReplayError'
        assert ev['setup']['call_interval'] == [a, b]
        assert ev['setup']['core_call_count'] == item['actual_core_calls']
        expected = data['special_words'][1]['bank'] if item['case'] == 'reflection_false_half_trace_two' else data['encoded_bank']
        assert strict(ev['logical']) == strict(expected['logical'])
        banks.append(('failed_replay:' + item['case'], ev))
    negatives.append({'case': item['case'], 'type': item['type'], 'calls': item['actual_core_calls'],
                      'complete_fresh_replay_attached': ev is not None})
rows = []
for label, bank in banks:
    logical, setup = bank['logical'], bank['setup']
    assert sha(strict(logical)) == bank['binding_sha256']
    assert logical['source']['trace_bank_sha256'] == data['source_hashes']['so_trace_certificates.py']
    a, b = setup['call_interval']
    assert b - a == setup['core_call_count'] == len(setup['actual_core_calls'])
    assert strict(setup['actual_core_calls']) == strict(data['actual_core_calls'][a-start:b-start])
    word_counts = []
    for key, word in logical['words'].items():
        assert word['full_dimension'] == 61 and word['phase_index'] == int(key)
        forward, inverse = word['complete_forward_columns'], word['complete_inverse_columns']
        assert len(forward) == len(inverse) == 61
        assert all(len(col) == 61 for col in forward + inverse)
        assert all(forward[j][i] == inverse[i][j] for i in range(61) for j in range(61))
        orientation = word['orientation']
        positions = [j for j, gate in enumerate(orientation['normalized_word']) if gate[0] in ('neg', 'swap')]
        assert positions == orientation['negative_determinant_letter_positions']
        assert orientation['negative_letter_parity'] == len(positions) & 1
        assert orientation['determinant'] == (-1 if len(positions) & 1 else 1)
        assert orientation['primitive_sha256'] == sha(strict(logical['primitive_orientation']))
        ops = word['observer_operations']
        assert len(ops) == word['actual_unique_observer_expressions']
        assert all(op['states'] <= 5 and op['depth'] == 2 for op in ops)
        if orientation['determinant'] == 1:
            assert word['expression_reference_count'] == 122
            assert len(word['trace_nodes']) == 121
            assert word['diagonal_node_indices'] == list(range(61))
            for node in word['trace_nodes']:
                assert node['value'] == ops[node['expression_index']]['signed_observation']
            assert word['clipping_margin']['value'] == ops[word['clipping_margin']['expression_index']]['signed_observation']
        else:
            assert word['s'] == '4' and word['bound_is_exact'] is True
            assert word['bound_method'] == 'DET_MINUS_ONE_EXACT'
            assert not ops and not word['trace_nodes']
        word_counts.append(len(ops))
    assert sum(word_counts) == setup['core_call_count']
    assert setup['stored_complete_column_scalar_entries'] == len(logical['words']) * 2 * 61 * 61
    assert setup['logical_serialized_bytes'] == len(strict(logical))
    rows.append({'label': label, 'words': len(word_counts), 'calls': setup['core_call_count'],
                 'unique_observer_counts': word_counts, 'interval': [a, b],
                 'full_saved_call_records_match_global_slice': True})
intervals = sorted(x['interval'] for x in rows if x['interval'][0] != x['interval'][1])
assert all(b <= c for (a, b), (c, d) in zip(intervals, intervals[1:]))
assert len(rows) == cost['whole_checker']['bank_invocations_with_saved_evidence'] == 17
assert sum(x['words'] for x in rows) == cost['whole_checker']['replayed_word_count'] == 43
assert sum(x['calls'] for x in rows) == cost['whole_checker']['bank_construction_or_fresh_replay_calls'] == 478
assert len(negatives) == summary['negative_controls'] == 23
assert sum(x['complete_fresh_replay_attached'] for x in negatives) == 11
assert sum(x['calls'] == 0 for x in negatives) == 13
assert strict(data['encoded_bank']['logical']) == strict(data['restored_bank']['logical'])
for key, word in data['encoded_bank']['logical']['words'].items():
    assert word['s'] == data['complete_bank']['logical']['words'][key]['s']
    assert strict(word['complete_forward_columns']) == strict(data['complete_bank']['logical']['words'][key]['complete_forward_columns'])
assert data['warm_reuse'] == cost['warm_reuse'] == summary['warm_reuse']
report = {'scope': 'Read-only raw evidence and metadata; no native/scientific rerun',
          'source_hashes': data['source_hashes'], 'raw_sha256': sha(raw), 'gzip_sha256': sha(blob),
          'raw_bytes': len(raw), 'gzip_bytes': len(blob), 'bank_invocations': rows,
          'negative_controls': negatives, 'whole_checker': cost['whole_checker'],
          'strict_logical_bindings_and_full_call_slices_verified': True,
          'full_and_codec_columns_and_bounds_equal': True,
          'table_instance_counts_per_program': [len(p['factory_tables']) for p in data['program_admissions']],
          'warm_reuse': data['warm_reuse']}
(ROOT / 'SO_TRACE_METADATA_REVIEW.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'raw_sha256': sha(raw), 'bank_invocations': len(rows),
                  'calls_total': data['core_call_count'], 'bank_observers': sum(x['calls'] for x in rows),
                  'negative_controls': len(negatives), 'status': 'SAVED_EVIDENCE_ADMIN_CHECKS_PASS'}))
