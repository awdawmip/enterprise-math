"""Read saved bytes, recording links and costs; never import scientific modules."""
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'signed_gap'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def same(left, right):
    assert canonical(left) == canonical(right)


def semantic(certificate):
    certificate = deepcopy(certificate)
    count = certificate['actual_integer_evidence']['arithmetic_stats']['native_kernel_calls_delta']
    assert type(count) is int and count >= 0
    certificate['actual_integer_evidence']['arithmetic_stats']['native_kernel_calls_delta'] = 0
    return canonical(certificate)


def load_result(stem):
    compressed = (DATA / (stem + '_RESULTS.json.gz')).read_bytes()
    raw = gzip.decompress(compressed)
    summary = json.loads((DATA / (stem + '_SUMMARY.json')).read_bytes())
    assert digest(raw) == summary['payload_sha256']
    assert digest(compressed) == summary['artifact_sha256']
    assert len(raw) == summary['raw_bytes'] and len(compressed) == summary['gzip_bytes']
    data = json.loads(raw)
    assert data['status'] == summary['status'] == 'PASS'
    same(data['source_sha256'], summary['source_sha256'])
    for name, pin in data['source_sha256'].items():
        assert digest((DATA / name).read_bytes()) == pin
    return data, summary


def op_link(op, kind, inputs, result=None, check_result=False):
    assert op['operation'] == kind
    same(op['inputs'], inputs)
    if check_result:
        same(op['result'], result)


def inspect_certificate(cert):
    """Validate links between already recorded numbers; do not recompute counts."""
    evidence = cert['actual_integer_evidence']
    ops = evidence['signed_operations']
    typed = evidence['arithmetic_operations']
    indices = [idx for op in ops for idx in op['typed_operation_indices']]
    same(indices, list(range(len(typed))))
    assert len(typed) == evidence['arithmetic_stats']['typed_operations']
    previous = 0
    for request_index, req in enumerate(cert['requests']):
        inp = req['inputs']
        assert all(type(x) is int for x in inp.values())
        assert inp['stride'] == 1 and inp['r'] == request_index
        start, scale, interval, outer, stop = (req[k] for k in (
            'signed_operations_start', 'scale_operations_stop',
            'interval_operations_start', 'outer_operations_start', 'signed_operations_stop'))
        assert start == previous and start <= scale <= interval < outer < stop <= len(ops)
        assert req['negative_values_are_valid'] is True
        assert req['raw_denominator_exponent'] == 2 * inp['g']

        # Scale construction: inspect the recorded chain rather than compute powers.
        position = start
        for exponent, saved in ((inp['k'], req['U']), (inp['g'] - inp['k'] - 1, req['H'])):
            value = 1
            for _ in range(exponent):
                op_link(ops[position], 'signed_add', [value, value])
                value = ops[position]['result']
                position += 1
            same(value, saved)
        op_link(ops[position], 'signed_multiply', [2, req['U']])
        twice_u = ops[position]['result']
        position += 1
        op_link(ops[position], 'signed_multiply', [twice_u, req['H']], req['L'], True)
        assert position + 1 == scale

        qi = req['window_query_index']
        assert qi == request_index
        query = evidence['window_weight_queries'][qi]
        same(query['inputs'], {'H': req['H'], 'V': req['U'], 'P': 2,
                               'R': inp['R'], 'r': inp['r'], 'd': 0})
        assert query['signed_operations_start'] == scale
        assert query['signed_operations_stop'] == interval
        same(query['value'], req['weights']['J_zero'])
        same(ops[interval - 1]['result'], query['value'])

        # All 13 outer interval-count recording edges, with only sign/routing wiring.
        part = ops[interval:outer]
        assert len(part) == 13
        op_link(part[0], 'signed_euclidean_division', [req['L'], inp['R']])
        v, u = part[0]['result']
        op_link(part[1], 'signed_euclidean_division', [inp['r'], inp['R']])
        _, rho = part[1]['result']
        op_link(part[2], 'signed_add', [u, -rho])
        op_link(part[3], 'signed_add', [inp['R'], -rho])
        op_link(part[4], 'signed_add', [u, -part[3]['result']])
        op_link(part[5], 'signed_multiply', [v, v])
        op_link(part[6], 'signed_multiply', [inp['R'], part[5]['result']])
        op_link(part[7], 'signed_multiply', [v, u])
        op_link(part[8], 'signed_multiply', [2, part[7]['result']])
        value = 0
        terms = (part[6]['result'], part[8]['result'],
                 part[2]['result'] if part[2]['result'] > 0 else 0,
                 part[4]['result'] if part[4]['result'] > 0 else 0)
        for op, term in zip(part[9:], terms):
            op_link(op, 'signed_add', [value, term])
            value = op['result']
        same(value, req['weights']['total_unsigned'])
        assert outer + 2 == stop
        op_link(ops[outer], 'signed_multiply', [4, req['weights']['J_zero']], req['four_J_zero'], True)
        op_link(ops[outer + 1], 'signed_add', [req['four_J_zero'], -value], req['value'], True)
        previous = stop
    assert previous == len(ops)
    assert len(evidence['window_weight_queries']) == len(cert['requests'])
    for node in evidence['moment_nodes']:
        assert 0 <= node['signed_operations_start'] <= node['signed_operations_stop'] <= len(ops)
    return {'requests': len(cert['requests']), 'signed_operations': len(ops),
            'typed_operations': len(typed), 'moment_nodes': len(evidence['moment_nodes'])}


def aggregate(certificates):
    evidences = [c['actual_integer_evidence'] for c in certificates]
    metrics = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
               'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
    return {'certificates': len(evidences),
        'arithmetic': {key: sum(e['arithmetic_stats'][key] for e in evidences) for key in metrics},
        'signed_operations': sum(len(e['signed_operations']) for e in evidences),
        'moment_nodes': sum(len(e['moment_nodes']) for e in evidences),
        'outer_window_queries': sum(len(e['window_weight_queries']) for e in evidences)}


def main():
    data, summary = load_result('ONE_WINDOW')
    old, old_summary = load_result('SIGNED_GAP')
    assert data['baseline']['reexecuted'] is False
    assert data['baseline']['whole_payload_read_and_hash_checked'] is True
    assert data['baseline']['payload_sha256'] == old_summary['payload_sha256']
    assert data['baseline']['artifact_sha256'] == old_summary['artifact_sha256']
    guard_raw = (ROOT / 'STARTUP_GUARD.json').read_bytes()
    assert digest(guard_raw) == data['startup_guard']['sha256']
    same(json.loads(guard_raw), data['startup_guard']['receipt'])
    guard = data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['sync_debt_events'] == [] and guard['required_action'] == 'CONTINUE_ACTIVITY'
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert data['actual_core_call_count'] == summary['actual_core_call_count'] == len(data['actual_core_calls']) == 1
    cases = []
    productions, positives, negatives = [], [], []
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    native_paths = {
        'lazy_modular': 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular': 'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks': 'sep26-shor-general/completion/typed_integer_prechecks.py'}
    for name, path in native_paths.items():
        assert digest((ROOT.parent / path).read_bytes()) == native['files_sha256'][name]
    for index, (case, prior) in enumerate(zip(data['cases'], old['cases'])):
        same(case['inputs'], prior['inputs'])
        same(case['values'], prior['values'])
        assert case['all_residues_equal'] is True and prior['all_residues_equal'] is True
        cert, replay = case['certificate'], case['verification']['replay_certificate']
        assert semantic(cert) == semantic(replay)
        assert case['verification']['verified'] is True
        assert case['verification']['requests_replayed'] == len(cert['requests']) == case['inputs']['R']
        same(case['values'], [r['value'] for r in cert['requests']])
        same(cert['actual_integer_evidence']['native_source'], native)
        same(replay['actual_integer_evidence']['native_source'], native)
        production_links = inspect_certificate(cert)
        replay_links = inspect_certificate(replay)
        same(production_links, replay_links)
        base = case['baseline_reference']
        assert base['case_index'] == index
        assert base['certificate_pointer'] == f'cases/{index}/certificate'
        assert base['typed_enumeration_pointer'] == f'cases/{index}/typed_enumeration'
        same(base['values'], prior['values'])
        same(base['recorded_production_arithmetic_stats'], prior['certificate']['actual_integer_evidence']['arithmetic_stats'])
        same(case['new_production_arithmetic_stats'], cert['actual_integer_evidence']['arithmetic_stats'])
        assert semantic(prior['certificate']) == semantic(prior['verification']['replay_certificate'])
        brute = prior['typed_enumeration']
        assert base['recorded_pair_count'] == len(brute['pair_observations'])
        buckets = [0] * case['inputs']['R']
        for pair in brute['pair_observations']:
            idx = pair['residue']
            same(buckets[idx], pair['bucket_before'])
            buckets[idx] = pair['bucket_after']
            same(brute['actual_integer_evidence']['signed_operations'][pair['signed_operations_stop'] - 1]['result'], pair['bucket_after'])
        same(buckets, case['values'])
        cases.append({'inputs': case['inputs'], 'values': case['values'],
            'recorded_historical_pairs': base['recorded_pair_count'], 'recorded_links': production_links})
        productions.append(cert)
        positives.append(replay)
    assert len(cases) == len(data['cases']) == len(old['cases']) == summary['cases'] == 9
    assert sum(len(c['values']) for c in cases) == summary['residue_equalities'] == 31
    negative_rows = []
    expected_names = ('value', 'window_weight', 'interval_weight', 'identity', 'boolean_input', 'source')
    same([n['name'] for n in data['negative_checks']], list(expected_names))
    for item in data['negative_checks']:
        assert item['rejected'] is True
        assert semantic(item['attempted_certificate']) != semantic(productions[0])
        captures = item['actual_replay_certificates']
        if item['name'] in expected_names[:4]:
            assert len(captures) == 1 and item['error'] == 'one-window certificate does not replay'
            assert semantic(captures[0]) == semantic(productions[0])
            inspect_certificate(captures[0])
            negatives.extend(captures)
        else:
            assert captures == []
        negative_rows.append({'name': item['name'], 'error': item['error'], 'complete_fresh_replays': len(captures)})
    resources = {'production': aggregate(productions), 'positive_replay': aggregate(positives),
                 'negative_replay': aggregate(negatives),
                 'historical_production': aggregate([c['certificate'] for c in old['cases']])}
    for key, field in (('production', 'fresh_production_adder_digit_replays'),
                       ('positive_replay', 'positive_replay_adder_digit_replays'),
                       ('negative_replay', 'negative_replay_adder_digit_replays'),
                       ('historical_production', 'historical_three_window_production_adder_digit_replays')):
        assert resources[key]['arithmetic']['adder_digit_replays'] == summary[field]
    reported = json.loads((DATA / 'ONE_WINDOW_READBACK.json').read_bytes())
    for key in ('production', 'positive_replay', 'negative_replay'):
        same(resources[key]['arithmetic'], reported[key]['arithmetic_totals'])
    output = {'status': 'PASS_COMPLETE_SAVED_RECORD_REVIEW',
        'scope': 'full bytes, strict saved replay equality, operation links and resource metadata; no native import or scientific execution',
        'reader_sha256': digest(Path(__file__).read_bytes()),
        'source_sha256': data['source_sha256'],
        'payload_sha256': summary['payload_sha256'], 'raw_bytes': summary['raw_bytes'],
        'gzip_sha256': summary['artifact_sha256'], 'gzip_bytes': summary['gzip_bytes'],
        'baseline_payload_sha256': old_summary['payload_sha256'],
        'baseline_raw_bytes': old_summary['raw_bytes'],
        'guard_sha256': digest(guard_raw), 'native_source': native,
        'cases': cases, 'negative_replays': negative_rows, 'resources': resources,
        'actual_core_calls': data['actual_core_calls'],
        'current_run_total_adder_digit_replays': sum(resources[k]['arithmetic']['adder_digit_replays']
            for k in ('production', 'positive_replay', 'negative_replay')),
        'new_failure_artifact_present': (DATA / 'ONE_WINDOW_FAILED_EXECUTION.json.gz').exists(),
        'comparison_is_timing_benchmark': False,
        'scientific_arithmetic_recomputed_by_reader': False}
    target = ROOT / 'guard_review/ONE_WINDOW_RECORD_REVIEW.json'
    with target.open('x', encoding='utf-8') as stream:
        json.dump(output, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'status': output['status'], 'reader_sha256': output['reader_sha256'],
        'record_sha256': digest(target.read_bytes()), 'cases': len(cases),
        'resources': resources, 'current_run_total_digits': output['current_run_total_adder_digit_replays']}))


if __name__ == '__main__':
    main()
