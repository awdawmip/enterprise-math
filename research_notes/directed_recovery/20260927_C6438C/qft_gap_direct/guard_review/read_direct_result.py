"""Saved-record review only: stdlib I/O, recording-edge checks and cost sums.

No scientific module is imported. Saved arithmetic outputs are read, never
recomputed. Native adder cells are matched to the saved source-bound columns.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'direct_gap'
OLD = ROOT.parent / 'sep27-qft-signedgap/signed_gap'
SOURCE_PINS = {
    'direct_signed_gap.py': '3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521',
    'check_direct_signed_gap.py': 'be69a1937c9ab1e04ad4fe6f650c412c5cad5def247b2d40f97042b926e5ce6f'}
RAW_PIN = '48780f175bc4bcf673345ee8c0b9e0240cc1c2a0e166037720c5fc06b8483157'
GZIP_PIN = '3ac0ebc17112afb9f068e39c1ebb91afd8f6e3f6aeb3d6cd46044d0733b26354'
HISTORY_RAW_PIN = '37ec0d4b7939a70d9157239bfebec7c88a387ff6a2f046a2701f87641d5d78f9'
HISTORY_GZIP_PIN = 'd465513608449d40b081a6ae62acff51f75ef5990f7bc911cec632a5b705e3de'
DEGREES = {f'{p},{e}' for e in range(4) for p in range(4-e)}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def same(a, b):
    assert canonical(a) == canonical(b)


def semantic(cert):
    cert = deepcopy(cert)
    stats = cert['actual_integer_evidence']['arithmetic_stats']
    assert type(stats['native_kernel_calls_delta']) is int and stats['native_kernel_calls_delta'] >= 0
    stats['native_kernel_calls_delta'] = 0
    return canonical(cert)


def load(directory, stem, raw_pin, gzip_pin):
    compressed = (directory / f'{stem}_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    summary = json.loads((directory / f'{stem}_SUMMARY.json').read_bytes())
    assert digest(raw) == raw_pin == summary['payload_sha256']
    assert digest(compressed) == gzip_pin == summary['artifact_sha256']
    assert len(raw) == summary['raw_bytes'] and len(compressed) == summary['gzip_bytes']
    data = json.loads(raw)
    assert data['status'] == summary['status'] == 'PASS'
    same(data['source_sha256'], summary['source_sha256'])
    for name, pin in data['source_sha256'].items():
        assert digest((directory / name).read_bytes()) == pin
    return data, summary


def trace_accounting(evidence):
    """Recount retained cells/host metadata, without executing their arithmetic."""
    total = Counter(adder_digit_replays=0, host_bit_wiring_operations=0,
                    host_bit_length_calls_in_arithmetic=0)
    columns = evidence['native_source']['native_adder']['columns']
    assert len(columns) == 8
    def visit(item):
        if type(item) is dict:
            if {'cells', 'low', 'carry'} <= set(item):
                cells = item['cells']
                assert len(cells) == item['width']
                for bit, cell in enumerate(cells):
                    assert len(cell) == 4 and cell[0] == bit
                    assert type(cell[1]) is int and 0 <= cell[1] < len(columns)
                    same(cell[2:], columns[cell[1]])
                if cells:
                    same(item['carry'], cells[-1][3])
                total['adder_digit_replays'] += len(cells)
                total['host_bit_wiring_operations'] += 10*len(cells)
                return
            kind = item.get('operation')
            if kind == 'BRC_UNSIGNED_COMPARE':
                total['host_bit_wiring_operations'] += 3
                total['host_bit_length_calls_in_arithmetic'] += 2
            elif kind == 'BRC_UNSIGNED_SHIFT_ADD':
                total['host_bit_wiring_operations'] += 3*len(item['steps'])
                total['host_bit_length_calls_in_arithmetic'] += 3
            elif kind == 'BRC_UNSIGNED_LONG_DIVISION':
                total['host_bit_wiring_operations'] += 6*len(item['steps'])
                total['host_bit_length_calls_in_arithmetic'] += 1
            for child in item.values():
                visit(child)
        elif type(item) is list:
            for child in item:
                visit(child)
    for operation in evidence['arithmetic_operations']:
        assert operation['operation'] in ('add', 'compare', 'multiply', 'divide')
        visit(operation['trace'])
        if operation['operation'] == 'add':
            total['host_bit_length_calls_in_arithmetic'] += 2
    for key, count in total.items():
        assert count == evidence['arithmetic_stats'][key]
    return dict(total)


class RecordedCursor:
    """A cursor over already saved outputs, not an arithmetic evaluator."""
    def __init__(self, evidence):
        self.evidence = evidence
        self.ops = evidence['signed_operations']
        self.i = 0
        self.node_map = {}
        self.seen_tables = 0
        self.empty_progressions = 0
        nodes = evidence['moment_nodes']
        for index, node in enumerate(nodes):
            key = tuple(node['parameters'])
            assert key not in self.node_map and len(key) == 4
            assert set(node['moments']) == DEGREES
            assert 0 <= node['signed_operations_start'] <= node['signed_operations_stop'] <= len(self.ops)
            assert node['branch'] in ('empty', 'normalize_signed_coefficients',
                'normalized_constant_zero', 'normalized_zero_height', 'transpose_lattice')
            if node['child'] is not None:
                child_index, child = self.node_map[tuple(node['child'])]
                assert child_index < index
                assert child['signed_operations_stop'] <= node['signed_operations_stop']
            self.node_map[key] = (index, node)
        assert evidence['stats']['moment_requests'] == len(nodes) + evidence['stats']['cache_hits']

    def take(self, kind, inputs):
        op = self.ops[self.i]
        assert op['operation'] == kind
        same(op['inputs'], inputs)
        self.i += 1
        return op['result']

    def add(self, x, y):
        return self.take('signed_add', [x, y])

    def sub(self, x, y):
        return self.take('signed_add', [x, -y])

    def mul(self, x, y):
        return self.take('signed_multiply', [x, y])

    def div(self, x, y):
        return self.take('signed_euclidean_division', [x, y])

    def total(self, terms):
        value = 0
        for term in terms:
            value = self.add(value, term)
        return value

    def recorded(self, record, operation):
        assert record['signed_operations_start'] == self.i
        value = operation()
        same(value, record['value'])
        assert record['signed_operations_stop'] == self.i
        return value

    def exact(self, record, numerator, denominator):
        same(record['numerator'], numerator)
        same(record['denominator'], denominator)
        assert record['signed_operation_index'] == record['signed_operations_start'] == self.i
        value, remainder = self.div(numerator, denominator)
        assert remainder == record['remainder'] == 0
        same(value, record['value'])
        assert record['signed_operations_stop'] == self.i
        return value

    def table(self, record, n, P, R, b):
        same(record['inputs'], {'n': n, 'm': P, 'a': R, 'b': b})
        assert record['signed_operations_start'] == self.i
        stop = record['signed_operations_stop']
        assert self.i <= stop <= len(self.ops)
        index, node = self.node_map[(n, P, R, b)]
        same(record['outputs'], node['moments'])
        new_indices = record['new_moment_node_indices']
        if new_indices:
            same(new_indices, list(range(new_indices[0], new_indices[-1]+1)))
            assert new_indices[-1] == index
            for j in new_indices:
                part = self.evidence['moment_nodes'][j]
                assert self.i <= part['signed_operations_start'] <= part['signed_operations_stop'] <= stop
            assert node['signed_operations_start'] == self.i and node['signed_operations_stop'] == stop
        else:
            assert self.i == stop and node['signed_operations_stop'] <= stop
        before, after = record['stats_before'], record['stats_after']
        assert after['moment_requests'] - before['moment_requests'] == len(new_indices) + after['cache_hits'] - before['cache_hits']
        assert after['max_recursion_depth'] >= before['max_recursion_depth']
        assert after['max_observed_integer_bits'] >= before['max_observed_integer_bits']
        self.i = stop
        self.seen_tables += 1
        return record['outputs']

    def progression(self, record, head, orientation, req):
        same(record['head'], head)
        assert record['orientation'] == orientation and record['multiplicity'] == 1
        assert record['signed_operations_start'] == self.i
        R, L, U, P, b = req['inputs']['R'], req['L'], req['U'], req['P'], head['value']
        same(record['step'], R)
        z = self.recorded(record['last_minus_head'], lambda: self.sub(self.sub(L, 1), b))
        if z < 0:
            assert record['empty'] is True and record['n'] == 0 and record['table_calls'] == []
            answer = self.recorded(record['zero'], lambda: self.add(0, 0))
            self.empty_progressions += 1
        else:
            assert record['empty'] is False
            length = record['length_receipt']
            assert length['signed_operations_start'] == self.i
            q, remainder = self.div(z, R)
            n = self.add(q, 1)
            same([q, remainder, n], [length['quotient'], length['remainder'], length['value']])
            same(n, record['n'])
            assert length['signed_operations_stop'] == self.i
            assert len(record['table_calls']) == 2
            M = self.table(record['table_calls'][0], n, P, R, b)
            shifted = self.recorded(record['shifted_offset'], lambda: self.add(b, U))
            Mp = self.table(record['table_calls'][1], n, P, R, shifted)
            delta = {}
            for key in ('0,1', '1,1', '0,2', '1,2', '0,3'):
                delta[key] = self.recorded(record['deltas'][key], lambda key=key: self.sub(Mp[key], M[key]))
            D01, D11, D02, D12, D03 = [delta[k] for k in ('0,1', '1,1', '0,2', '1,2', '0,3')]
            nums, exact = record['division_numerators'], record['exact_divisions']
            numerator = self.recorded(nums['qdelta'], lambda: self.sub(D02, D01))
            qdelta = self.exact(exact['qdelta'], numerator, 2)
            numerator = self.recorded(nums['jqdelta'], lambda: self.sub(D12, D11))
            jqdelta = self.exact(exact['jqdelta'], numerator, 2)
            numerator = self.recorded(nums['q2delta'], lambda: self.total((self.mul(2, D03), self.mul(-3, D02), D01)))
            q2delta = self.exact(exact['q2delta'], numerator, 6)
            weighted = record['weighted_sums']
            d = self.recorded(weighted['d'], lambda: self.add(self.mul(b, n), self.mul(R, M['1,0'])))
            dq = self.recorded(weighted['dq'], lambda: self.add(self.mul(b, M['0,1']), self.mul(R, M['1,1'])))
            dd = self.recorded(weighted['ddelta'], lambda: self.add(self.mul(b, D01), self.mul(R, D11)))
            dqd = self.recorded(weighted['dqdelta'], lambda: self.add(self.mul(b, qdelta), self.mul(R, jqdelta)))
            factors = {'n': n, 'q': M['0,1'], 'dq': dq, 'q2': M['0,2'], 'd': d,
                'ddelta': dd, 'dqdelta': dqd, 'q2delta': q2delta, 'qdelta': qdelta, 'delta': D01}
            same(factors, record['term_factors'])
            names = ('n', 'q', 'dq', 'q2', 'd', 'ddelta', 'dqdelta', 'q2delta', 'qdelta', 'delta')
            terms = [self.recorded(record['terms'][name], lambda name=name:
                self.mul(req['coefficients'][name]['value'], factors[name])) for name in names]
            answer = self.recorded(record['sumA'], lambda: self.total(terms))
        same(answer, record['value'])
        assert record['signed_operations_stop'] == self.i
        return answer


def inspect(cert):
    evidence = cert['actual_integer_evidence']
    assert evidence['window_weight_queries'] == []
    ops, typed = evidence['signed_operations'], evidence['arithmetic_operations']
    same([idx for op in ops for idx in op['typed_operation_indices']], list(range(len(typed))))
    assert len(typed) == evidence['arithmetic_stats']['typed_operations']
    recounted = trace_accounting(evidence)
    c = RecordedCursor(evidence)
    for index, req in enumerate(cert['requests']):
        inp = req['inputs']
        assert set(inp) == {'g', 'k', 'R', 'r', 'stride'}
        assert all(type(x) is int for x in inp.values()) and inp['stride'] == 1 and inp['r'] == index
        assert inp['g'] >= 1 and 0 <= inp['k'] < inp['g'] and inp['R'] >= 1
        assert req['endpoint_shortcuts_used'] is False and req['negative_values_are_valid'] is True
        assert req['raw_denominator_exponent'] == 2*inp['g']
        assert req['signed_operations_start'] == req['scales_operations_start'] == c.i
        for exponent, saved in ((inp['k'], req['U']), (inp['g']-inp['k']-1, req['H'])):
            value = 1
            for _ in range(exponent):
                value = c.add(value, value)
            same(value, saved)
        same(c.add(req['U'], req['U']), req['P'])
        same(c.mul(req['H'], req['P']), req['L'])
        assert req['scales_operations_stop'] == c.i
        H, P = req['H'], req['P']
        helper, coefficients = req['coefficient_helpers'], req['coefficients']
        four_H = c.recorded(helper['four_H'], lambda: c.mul(4, H))
        eight_H = c.recorded(helper['eight_H'], lambda: c.mul(8, H))
        checks = (
            ('n', lambda: c.mul(H, P)), ('q', lambda: c.mul(c.sub(four_H, 2), P)),
            ('dq', lambda: c.add(4, 0)), ('q2', lambda: c.mul(-4, P)),
            ('d', lambda: c.sub(1, four_H)), ('ddelta', lambda: c.sub(eight_H, 4)),
            ('dqdelta', lambda: c.add(-8, 0)), ('q2delta', lambda: c.mul(8, P)),
            ('qdelta', lambda: c.mul(c.sub(8, eight_H), P)),
            ('delta', lambda: c.mul(c.sub(2, four_H), P)))
        for name, operation in checks:
            c.recorded(coefficients[name], operation)
        assert len(req['progressions']) == 2
        positive, negative = req['progressions']
        c.recorded(positive['head'], lambda: c.add(inp['r'], 0))
        p = c.progression(positive, positive['head'], 'nonnegative_difference', req)
        c.recorded(negative['head'], lambda: c.sub(inp['R'], inp['r']))
        n = c.progression(negative, negative['head'], 'negative_difference_magnitude', req)
        answer = c.recorded(req['final_addition'], lambda: c.add(p, n))
        same(answer, req['value'])
        assert req['signed_operations_stop'] == c.i
    assert c.i == len(ops)
    return {'requests': len(cert['requests']), 'signed_operations': len(ops),
        'typed_operations': len(typed), 'moment_nodes': len(evidence['moment_nodes']),
        'top_level_table_calls': c.seen_tables, 'empty_progressions': c.empty_progressions,
        'all_retained_native_adder_cells_bound': True, 'recounted_cost': recounted}


def aggregate(certificates):
    es = [c['actual_integer_evidence'] for c in certificates]
    keys = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
            'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
    return {'certificates': len(es),
        'arithmetic': {k: sum(e['arithmetic_stats'][k] for e in es) for k in keys},
        'signed_operations': sum(len(e['signed_operations']) for e in es),
        'moment_nodes': sum(len(e['moment_nodes']) for e in es),
        'moment_requests': sum(e['stats']['moment_requests'] for e in es),
        'cache_hits': sum(e['stats']['cache_hits'] for e in es)}


def main():
    data, summary = load(DATA, 'DIRECT', RAW_PIN, GZIP_PIN)
    old, old_summary = load(OLD, 'ONE_WINDOW', HISTORY_RAW_PIN, HISTORY_GZIP_PIN)
    same(data['source_sha256'], SOURCE_PINS)
    assert digest((ROOT/'DIFFERENCE_AUTOCORRELATION.md').read_bytes()) == data['direct_proof_sha256']
    guard_bytes = (ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guard_bytes) == data['startup_guard']['sha256']
    same(json.loads(guard_bytes), data['startup_guard']['receipt'])
    guard = data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['sync_debt_events'] == [] and guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC'
    history = data['history']
    assert history['whole_payload_read_and_hash_checked'] is True
    assert history['one_window_reexecuted'] is False and history['three_window_or_exhaustive_reexecuted'] is False
    assert history['payload_sha256'] == HISTORY_RAW_PIN and history['artifact_sha256'] == HISTORY_GZIP_PIN
    assert history['source_commit'] == '56b191519b036c6890cae328c3b3812fbc1debb7'
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    for key, path in {
        'lazy_modular': 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular': 'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks': 'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/path).read_bytes()) == native['files_sha256'][key]
    productions, positives, negatives, cases = [], [], [], []
    for index, (case, prior) in enumerate(zip(data['cases'], old['cases'])):
        same(case['inputs'], prior['inputs'])
        same(case['values'], prior['values'])
        cert, replay = case['certificate'], case['verification']['replay_certificate']
        assert cert['source_sha256'] == SOURCE_PINS['direct_signed_gap.py']
        assert cert['direct_proof_sha256'] == data['direct_proof_sha256']
        assert digest((OLD/'signed_gap.py').read_bytes()) == cert['baseline_helper_source_sha256']
        assert digest((ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py').read_bytes()) == cert['floor_moment_source_sha256']
        assert cert['signed_gap_proof_sha256'] == prior['certificate']['signed_gap_proof_sha256']
        assert semantic(cert) == semantic(replay)
        assert case['verification']['verified'] is True and case['all_residues_equal'] is True
        assert case['verification']['requests_replayed'] == len(cert['requests']) == case['inputs']['R']
        same(case['verification']['replay_arithmetic_stats'], replay['actual_integer_evidence']['arithmetic_stats'])
        same(case['values'], [r['value'] for r in cert['requests']])
        same(cert['actual_integer_evidence']['native_source'], native)
        same(replay['actual_integer_evidence']['native_source'], native)
        links = inspect(cert)
        same(links, inspect(replay))
        ref = case['history_reference']
        assert ref['case_index'] == index and ref['certificate_pointer'] == f'cases/{index}/certificate'
        same(ref['values'], prior['values'])
        same(ref['recorded_three_window_reference'], prior['baseline_reference'])
        same(ref['recorded_one_window_production_arithmetic_stats'], prior['certificate']['actual_integer_evidence']['arithmetic_stats'])
        same(case['new_production_arithmetic_stats'], cert['actual_integer_evidence']['arithmetic_stats'])
        assert semantic(prior['certificate']) == semantic(prior['verification']['replay_certificate'])
        cases.append({'inputs': case['inputs'], 'values': case['values'], 'record_links': links,
            'production_digits': cert['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'],
            'historical_one_window_digits': prior['certificate']['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']})
        productions.append(cert)
        positives.append(replay)
    assert len(cases) == len(data['cases']) == len(old['cases']) == summary['cases'] == 9
    assert sum(len(c['values']) for c in cases) == summary['residue_equalities'] == 31
    assert sum(c['record_links']['top_level_table_calls'] for c in cases) == summary['top_level_table_calls'] == 118
    assert sum(c['record_links']['empty_progressions'] for c in cases) == summary['empty_progressions'] == 3
    half = productions[5]['requests'][1]['progressions']
    assert len(half) == 2 and half[0]['head']['value'] == half[1]['head']['value']
    assert all(p['multiplicity'] == 1 and p['empty'] is False for p in half)
    expected_names = ['drop_half_modulus_orientation', 'wrong_length', 'wrong_table_offset',
        'wrong_delta', 'wrong_exact_division', 'wrong_output', 'wrong_source', 'boolean_input', 'wrong_schema']
    same([r['name'] for r in data['negative_checks']], expected_names)
    negative_rows = []
    for row in data['negative_checks']:
        original = productions[row['source_case_index']]
        assert row['rejected'] is True and semantic(row['attempted_certificate']) != semantic(original)
        captures = row['actual_replay_certificates']
        if row['name'] in expected_names[:6]:
            assert len(captures) == 1 and row['error'] == 'direct certificate does not replay'
            assert semantic(captures[0]) == semantic(original)
            inspect(captures[0])
            negatives.extend(captures)
        else:
            assert captures == []
        negative_rows.append({'name': row['name'], 'error': row['error'], 'paid_complete_replays': len(captures)})
    assert len(negatives) == 6 and len(data['negative_checks']) == summary['negative_checks'] == 9
    expected_inputs = [(True,0,3,0,1),(0,0,3,0,1),(2,-1,3,0,1),(2,2,3,0,1),
                       (2,0,0,0,1),(2,0,3,-1,1),(2,0,3,3,1),(2,0,3,0,2)]
    assert len(data['input_rejections']) == summary['input_rejections'] == len(expected_inputs)
    for row, values in zip(data['input_rejections'], expected_inputs):
        same(row['inputs'], dict(zip(('g','k','R','r','stride'), values)))
        assert row['rejected'] is True and type(row['error']) is str
    resources = {'production': aggregate(productions), 'positive_replay': aggregate(positives),
        'negative_replay': aggregate(negatives),
        'historical_one_window_production': aggregate([c['certificate'] for c in old['cases']])}
    for category, field in (
        ('production','fresh_production_adder_digit_replays'), ('positive_replay','positive_replay_adder_digit_replays'),
        ('negative_replay','negative_replay_adder_digit_replays'),
        ('historical_one_window_production','historical_one_window_production_adder_digit_replays')):
        assert resources[category]['arithmetic']['adder_digit_replays'] == summary[field]
    actual_total = sum(resources[k]['arithmetic']['adder_digit_replays']
                       for k in ('production','positive_replay','negative_replay'))
    native_total = sum(resources[k]['arithmetic']['native_kernel_calls_delta']
                       for k in ('production','positive_replay','negative_replay'))
    assert actual_total == 191601
    assert native_total == len(data['actual_core_calls']) == data['actual_core_call_count'] == summary['actual_core_call_count'] == 1
    assert data['actual_core_calls'][0]['states'] == 12 and data['actual_core_calls'][0]['entrypoint'] == 'recurrent_mass_power'
    output = {'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW',
        'scope':'full saved bytes, strict replay semantics, recording links, native-column cell binding and resource metadata; no scientific execution',
        'admission':'SHARED_CONTEXT_AUTHOR_REVIEW_NOT_FORMAL_ADMISSION',
        'reader_sha256':digest(Path(__file__).read_bytes()), 'source_sha256':SOURCE_PINS,
        'payload_sha256':RAW_PIN,'raw_bytes':summary['raw_bytes'], 'artifact_sha256':GZIP_PIN,'gzip_bytes':summary['gzip_bytes'],
        'history_payload_sha256':HISTORY_RAW_PIN,'history_raw_bytes':old_summary['raw_bytes'],
        'guard_sha256':digest(guard_bytes),'native_source':native,'cases':cases,
        'negative_checks':negative_rows,'input_rejections':data['input_rejections'],'resources':resources,
        'current_run_total_adder_digit_replays':actual_total,'actual_core_calls':data['actual_core_calls'],
        'unexpected_failure_artifact_present':(DATA/'DIRECT_FAILED_EXECUTION.json.gz').exists(),
        'scientific_arithmetic_recomputed':False,'comparison_is_timing_benchmark':False,
        'coverage_limits':['bounded one-negative-bit stride-one scalar observer only',
            'moment recurrence outputs are bound to saved fresh replay, not scientifically recomputed by this reader',
            'one primitive construction call is not total arithmetic cost',
            'historical one-window production is read, not a matched timing rerun']}
    target = ROOT/'guard_review/DIRECT_RECORD_REVIEW.json'
    with target.open('x',encoding='utf-8') as stream:
        json.dump(output,stream,indent=2)
        stream.write('\n')
    print(json.dumps({'status':output['status'],'reader_sha256':output['reader_sha256'],
        'review_sha256':digest(target.read_bytes()),'resources':resources,
        'current_run_total_digits':actual_total,'top_tables':118,'empty_progressions':3}))


if __name__ == '__main__':
    main()
