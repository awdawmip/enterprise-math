"""Pure saved-record inspection; no native modules or scientific arithmetic.

The imported helper is the frozen prior I/O reviewer, not an observer/runner.
Arithmetic below is resource accounting, range routing or record indexing.
Scientific integer results are linked to saved operations, not recomputed.
"""
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'endpoint_gap'
OLD = ROOT.parent / 'sep27-qft-signedgap/signed_gap'
HELPER = OLD.parent / 'guard_review/read_one_window_review.py'
HELPER_PIN = '4ec7a4318006427895f6234d413778372c545482e6f5bf371f96ea6d82c87f6a'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


assert digest(HELPER.read_bytes()) == HELPER_PIN
spec = importlib.util.spec_from_file_location('prior_io_review', HELPER)
prior_io = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior_io)
same, semantic, op_link, aggregate = (prior_io.same, prior_io.semantic,
                                    prior_io.op_link, prior_io.aggregate)


def load(data_dir, stem):
    compressed = (data_dir / (stem + '_RESULTS.json.gz')).read_bytes()
    raw = gzip.decompress(compressed)
    summary = json.loads((data_dir / (stem + '_SUMMARY.json')).read_bytes())
    assert digest(raw) == summary['payload_sha256']
    assert digest(compressed) == summary['artifact_sha256']
    assert len(raw) == summary['raw_bytes'] and len(compressed) == summary['gzip_bytes']
    data = json.loads(raw)
    assert data['status'] == summary['status'] == 'PASS'
    same(data['source_sha256'], summary['source_sha256'])
    for name, pin in data['source_sha256'].items():
        assert digest((data_dir / name).read_bytes()) == pin
    return data, summary


def interval_links(ops, receipt, length, R, r, start):
    same(receipt['inputs'], {'length': length, 'R': R, 'r': r})
    assert receipt['signed_operations_start'] == start
    stop = receipt['signed_operations_stop']
    part = ops[start:stop]
    assert len(part) == 13
    op_link(part[0], 'signed_euclidean_division', [length, R])
    v, u = part[0]['result']
    op_link(part[1], 'signed_euclidean_division', [r, R])
    _, rho = part[1]['result']
    op_link(part[2], 'signed_add', [u, -rho])
    op_link(part[3], 'signed_add', [R, -rho])
    op_link(part[4], 'signed_add', [u, -part[3]['result']])
    op_link(part[5], 'signed_multiply', [v, v])
    op_link(part[6], 'signed_multiply', [R, part[5]['result']])
    op_link(part[7], 'signed_multiply', [v, u])
    op_link(part[8], 'signed_multiply', [2, part[7]['result']])
    value = 0
    for op, term in zip(part[9:], (part[6]['result'], part[8]['result'],
            part[2]['result'] if part[2]['result'] > 0 else 0,
            part[4]['result'] if part[4]['result'] > 0 else 0)):
        op_link(op, 'signed_add', [value, term])
        value = op['result']
    same(value, receipt['value'])
    return stop


def inspect(cert):
    e = cert['actual_integer_evidence']
    ops, typed = e['signed_operations'], e['arithmetic_operations']
    same([j for op in ops for j in op['typed_operation_indices']], list(range(len(typed))))
    assert len(typed) == e['arithmetic_stats']['typed_operations']
    counts = {'highest_bit': 0, 'lowest_odd_modulus': 0,
              'lowest_even_modulus': 0, 'interior_one_window': 0}
    prev = intervals = 0
    nested = []
    for request_index, req in enumerate(cert['requests']):
        inp = req['inputs']
        assert set(inp) == {'g', 'k', 'R', 'r', 'stride'}
        assert all(type(x) is int for x in inp.values())
        g, k, R, r = (inp[x] for x in ('g', 'k', 'R', 'r'))
        assert g >= 1 and 0 <= k < g and R >= 1 and 0 <= r < R
        assert inp['stride'] == 1 and r == request_index
        assert req['negative_values_are_valid'] is True
        assert req['raw_denominator_exponent'] == 2 * g
        pos = req['signed_operations_start']
        assert pos == prev
        stop = req['signed_operations_stop']
        if k == g - 1:
            branch = 'highest_bit'
        elif k == 0:
            branch = 'lowest_even_modulus' if req['modulus_parity'] == 0 else 'lowest_odd_modulus'
        else:
            branch = 'interior_one_window'
        assert req['branch'] == branch
        same(req['identity'], cert['identities'][branch])
        counts[branch] += 1
        if branch == 'interior_one_window':
            sub = req['frozen_one_window_request']
            same(sub['inputs'], inp)
            same(sub['value'], req['value'])
            assert sub['signed_operations_start'] == pos and sub['signed_operations_stop'] == stop
            assert sub['raw_denominator_exponent'] == req['raw_denominator_exponent']
            assert req['fallback_request_index'] == len(nested)
            same(req['window_query_indices'], [sub['window_query_index']])
            nested.append(sub)
            prev = stop
            continue

        assert req['window_query_indices'] == []
        if k == 0 and k != g - 1:
            op_link(ops[pos], 'signed_euclidean_division', [R, 2],
                    [req['modulus_half'], req['modulus_parity']], True)
            op_link(ops[pos + 1], 'signed_euclidean_division', [r, 2],
                    [req['residue_half'], req['residue_parity']], True)
            assert req['modulus_parity'] in (0, 1) and req['residue_parity'] in (0, 1)
            pos += 2
        half = 1
        for _ in range(g - 1):
            op_link(ops[pos], 'signed_add', [half, half])
            half = ops[pos]['result']
            pos += 1
        same(half, req['H'])
        op_link(ops[pos], 'signed_add', [half, half], req['L'], True)
        pos += 1
        assert pos == req['scale_operations_stop']
        if branch == 'lowest_odd_modulus':
            saved = req['half_residue']
            assert saved['signed_operations_start'] == pos
            if req['residue_parity']:
                assert saved['even_residue_reuses_recorded_division'] is False
                op_link(ops[pos], 'signed_add', [r, R], saved['numerator'], True)
                op_link(ops[pos + 1], 'signed_euclidean_division',
                        [saved['numerator'], 2], [saved['value'], 0], True)
                pos += 2
            else:
                assert saved['even_residue_reuses_recorded_division'] is True
                same(saved['numerator'], r)
                same(saved['value'], req['residue_half'])
            assert saved['signed_operations_stop'] == pos
            assert 0 <= saved['value'] < R
            residue = saved['value']
        else:
            residue = r
        receipts = req['interval_receipts']
        if branch == 'lowest_even_modulus':
            assert len(receipts) == 1
        else:
            assert len(receipts) == 2
            pos = interval_links(ops, receipts[0], half, R, residue, pos)
        pos = interval_links(ops, receipts[-1], req['L'], R, r, pos)
        intervals += len(receipts)
        assert pos == req['outer_operations_start']
        if branch == 'lowest_even_modulus':
            op_link(ops[pos], 'signed_multiply', [2, req['residue_parity']], req['parity_twice'], True)
            op_link(ops[pos + 1], 'signed_add', [1, -req['parity_twice']], req['sign'], True)
            op_link(ops[pos + 2], 'signed_multiply', [req['sign'], receipts[0]['value']], req['value'], True)
            assert pos + 3 == stop
        else:
            op_link(ops[pos], 'signed_multiply', [4, receipts[0]['value']], req['four_J_zero'], True)
            op_link(ops[pos + 1], 'signed_add', [req['four_J_zero'], -receipts[-1]['value']], req['value'], True)
            assert pos + 2 == stop
        prev = stop
    assert prev == len(ops)
    # The declared grid uses single-branch certificates; this is a review limit,
    # not an assumption in the production dispatcher's sequential API.
    if nested:
        assert len(nested) == len(cert['requests'])
        prior_io.inspect_certificate({'requests': nested, 'actual_integer_evidence': e})
    else:
        assert not e['window_weight_queries'] and not e['moment_nodes']
    return {'branch_counts': counts, 'endpoint_interval_receipts': intervals,
            'signed_operations': len(ops), 'typed_operations': len(typed),
            'window_queries': len(e['window_weight_queries']), 'moment_nodes': len(e['moment_nodes'])}


def main():
    data, summary = load(DATA, 'ENDPOINT')
    old, old_summary = load(OLD, 'ONE_WINDOW')
    assert data['history']['one_window_reexecuted'] is False
    assert data['history']['three_window_or_exhaustive_reexecuted'] is False
    assert data['history']['whole_payload_read_and_hash_checked'] is True
    assert data['history']['artifact_sha256'] == old_summary['artifact_sha256']
    assert data['history']['payload_sha256'] == old_summary['payload_sha256']
    guard_bytes = (ROOT / 'STARTUP_GUARD.json').read_bytes()
    assert digest(guard_bytes) == data['startup_guard']['sha256']
    same(json.loads(guard_bytes), data['startup_guard']['receipt'])
    guard = data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['sync_debt_events'] == [] and guard['required_action'] == 'CONTINUE_ACTIVITY'
    assert digest((ROOT / 'ENDPOINT_IDENTITIES.md').read_bytes()) == data['endpoint_proof_sha256']
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    for name, path in {
        'lazy_modular': 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular': 'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks': 'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent / path).read_bytes()) == native['files_sha256'][name]
    productions, positives, negatives, cases = [], [], [], []
    for i, (case, prior) in enumerate(zip(data['cases'], old['cases'])):
        same(case['inputs'], prior['inputs'])
        same(case['values'], prior['values'])
        assert case['all_residues_equal'] is True
        cert, replay = case['certificate'], case['verification']['replay_certificate']
        assert semantic(cert) == semantic(replay)
        assert case['verification']['verified'] is True
        assert case['verification']['requests_replayed'] == len(cert['requests']) == case['inputs']['R']
        assert cert['source_sha256'] == data['source_sha256']['endpoint_signed_gap.py']
        assert cert['one_window_source_sha256'] == old['source_sha256']['one_window_signed_gap.py']
        same(cert['actual_integer_evidence']['native_source'], native)
        same(replay['actual_integer_evidence']['native_source'], native)
        same(case['values'], [r['value'] for r in cert['requests']])
        links = inspect(cert)
        same(links, inspect(replay))
        base = case['history_reference']
        assert base['case_index'] == i and base['certificate_pointer'] == f'cases/{i}/certificate'
        same(base['values'], prior['values'])
        same(base['recorded_three_window_reference'], prior['baseline_reference'])
        same(base['recorded_one_window_production_arithmetic_stats'], prior['certificate']['actual_integer_evidence']['arithmetic_stats'])
        same(case['new_production_arithmetic_stats'], cert['actual_integer_evidence']['arithmetic_stats'])
        if case['branch'] == 'interior_one_window':
            same([r['frozen_one_window_request'] for r in cert['requests']], prior['certificate']['requests'])
            assert semantic({'actual_integer_evidence': cert['actual_integer_evidence']}) == semantic({'actual_integer_evidence': prior['certificate']['actual_integer_evidence']})
        cases.append({'inputs': case['inputs'], 'branch': case['branch'], 'values': case['values'], 'record_links': links})
        productions.append(cert)
        positives.append(replay)
    assert len(cases) == len(data['cases']) == len(old['cases']) == summary['cases'] == 9
    assert sum(len(c['values']) for c in cases) == summary['residue_equalities'] == 31
    names = ['wrong_branch', 'wrong_half_residue', 'wrong_parity_sign', 'altered_interval',
             'boolean_input', 'wrong_source', 'altered_fallback', 'wrong_denominator']
    same([r['name'] for r in data['negative_checks']], names)
    negative_rows = []
    for row in data['negative_checks']:
        assert row['rejected'] is True
        original = productions[row['source_case_index']]
        assert semantic(row['attempted_certificate']) != semantic(original)
        captured = row['actual_replay_certificates']
        if row['name'] not in ('boolean_input', 'wrong_source'):
            assert len(captured) == 1 and row['error'] == 'endpoint certificate does not replay'
            assert semantic(captured[0]) == semantic(original)
            inspect(captured[0])
            negatives.extend(captured)
        else:
            assert captured == []
        negative_rows.append({'name': row['name'], 'error': row['error'], 'complete_paid_replays': len(captured)})
    assert len(data['input_rejections']) == summary['input_rejections'] == 8
    assert all(row['rejected'] is True for row in data['input_rejections'])
    assert len(data['negative_checks']) == summary['negative_checks'] == 8
    assert data['actual_core_call_count'] == summary['actual_core_call_count'] == len(data['actual_core_calls']) == 1
    resources = {'production': aggregate(productions), 'positive_replay': aggregate(positives),
                 'negative_replay': aggregate(negatives),
                 'historical_one_window_production': aggregate([c['certificate'] for c in old['cases']])}
    for category, field in (('production', 'fresh_production_adder_digit_replays'),
            ('positive_replay', 'positive_replay_adder_digit_replays'),
            ('negative_replay', 'negative_replay_adder_digit_replays'),
            ('historical_one_window_production', 'historical_one_window_production_adder_digit_replays')):
        assert resources[category]['arithmetic']['adder_digit_replays'] == summary[field]
    by_branch = {branch: aggregate([c for c in productions if c['requests'][0]['branch'] == branch])
                 for branch in summary['branch_counts']}
    for branch, count in summary['branch_counts'].items():
        assert sum(c['record_links']['branch_counts'][branch] for c in cases) == count
    output = {'status': 'PASS_COMPLETE_SAVED_RECORD_REVIEW',
        'admission': 'SHARED_CONTEXT_AUTHOR_REVIEW_NOT_FORMAL_ADMISSION',
        'scope': 'full saved payload, strict complete replay equality, operation links and cost metadata; no native execution',
        'reader_sha256': digest(Path(__file__).read_bytes()), 'prior_io_helper_sha256': HELPER_PIN,
        'source_sha256': data['source_sha256'], 'payload_sha256': summary['payload_sha256'],
        'raw_bytes': summary['raw_bytes'], 'artifact_sha256': summary['artifact_sha256'],
        'gzip_bytes': summary['gzip_bytes'], 'baseline_payload_sha256': old_summary['payload_sha256'],
        'baseline_raw_bytes': old_summary['raw_bytes'], 'guard_sha256': digest(guard_bytes),
        'native_source': native, 'cases': cases, 'negative_checks': negative_rows,
        'input_rejections': data['input_rejections'], 'resources': resources, 'production_by_branch': by_branch,
        'current_run_total_adder_digit_replays': sum(resources[k]['arithmetic']['adder_digit_replays']
            for k in ('production', 'positive_replay', 'negative_replay')),
        'actual_core_calls': data['actual_core_calls'],
        'unexpected_failure_artifact_present': (DATA / 'ENDPOINT_FAILED_EXECUTION.json.gz').exists(),
        'scientific_arithmetic_recomputed': False, 'timing_benchmark': False,
        'coverage_limits': ['all declared certificates single branch; mixed branch shared runner not executed',
                            'R=1 only interior execution; endpoint R=1 symbolic proof only']}
    target = ROOT / 'guard_review/ENDPOINT_RECORD_REVIEW.json'
    with target.open('x', encoding='utf-8') as stream:
        json.dump(output, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'status': output['status'], 'reader_sha256': output['reader_sha256'],
        'review_sha256': digest(target.read_bytes()), 'resources': resources,
        'by_branch': by_branch, 'total_current_digits': output['current_run_total_adder_digit_replays']}))


if __name__ == '__main__':
    main()
