"""Full saved evidence readback; stdlib I/O only, no scientific imports.

The recorded cursor and cell-accounting routines are copied from the frozen
pure-I/O direct result reader. They consume recorded values; they do not run
scientific arithmetic or evaluate an ordinary numerical reference.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import gzip, hashlib, json
ROOT = Path(__file__).resolve().parent
DEGREES = {f'{p},{e}' for e in range(4) for p in range(4-e)}
RAW_PIN = '61aee1882148519bd9738bacf6f107a39532aa98de6c128854edb98df334aba9'
GZIP_PIN = 'f6bf350f188d4252c60c897778561e3c4957d65774a25a12334b35261f0b7bd3'
SCHEMA = 'BRC_ALIGNED_TWO_BIT_STRETCH_V1'

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


class AlignedCursor(RecordedCursor):
    def power(self, exponent):
        value = 1
        for _ in range(exponent):
            value = self.add(value, value)
        return value

    def division(self, record, x, m):
        same([record['numerator'], record['denominator']], [x, m])
        assert record['signed_operations_start'] == self.i
        q, r = self.div(x, m)
        same([q, r], [record['quotient'], record['remainder']])
        assert record['signed_operations_stop'] == self.i
        return q, r

    def length(self, record, head, step, limit):
        same([record['head'], record['step'], record['limit']], [head, step, limit])
        z = self.recorded(record['last_minus_head'], lambda: self.sub(self.sub(limit, 1), head))
        if z < 0:
            assert record['empty'] is True and record['n'] == 0
            assert self.recorded(record['zero'], lambda: self.add(0, 0)) == 0
        else:
            assert record['empty'] is False
            q, _ = self.division(record['division'], z, step)
            same(self.recorded(record['length_addition'], lambda: self.add(q, 1)), record['n'])
        return record['n']

    def coefficients(self, request):
        H, P = request['H'], request['P']
        helper, coefficients = request['coefficient_helpers'], request['coefficients']
        four_H = self.recorded(helper['four_H'], lambda: self.mul(4, H))
        eight_H = self.recorded(helper['eight_H'], lambda: self.mul(8, H))
        checks = (
            ('n', lambda: self.mul(H, P)), ('q', lambda: self.mul(self.sub(four_H, 2), P)),
            ('dq', lambda: self.add(4, 0)), ('q2', lambda: self.mul(-4, P)),
            ('d', lambda: self.sub(1, four_H)), ('ddelta', lambda: self.sub(eight_H, 4)),
            ('dqdelta', lambda: self.add(-8, 0)), ('q2delta', lambda: self.mul(8, P)),
            ('qdelta', lambda: self.mul(self.sub(8, eight_H), P)),
            ('delta', lambda: self.mul(self.sub(2, four_H), P)))
        for name, operation in checks:
            self.recorded(coefficients[name], operation)

    def branch(self, b, label, head, step, expected, req, remainder):
        same([b['label'], b['head'], b['step'], b['expected_n']], [label, head, step, expected])
        assert b['signed_operations_start'] == self.i
        _, parity = self.division(b['parity'], head['value'], 2)
        sign = -1 if parity else 1
        same(sign, b['sign'])
        fake_req = {'inputs': {'R': step}, 'L': req['M'], 'U': req['U'],
                    'P': req['P'], 'coefficients': req['coefficients']}
        original = self.progression(b['original'], head, label+':original', fake_req)
        assert self.recorded(b['canonical_count_difference'],
                            lambda: self.sub(b['original']['n'], expected['value'])) == 0
        shifted_head = b['shifted']['head']
        self.recorded(shifted_head, lambda: self.add(head['value'], 1))
        shifted = self.progression(b['shifted'], shifted_head, label+':shifted', fake_req)
        tail = b['shifted_zero_tail']
        removed = self.recorded(tail['count_difference'],
                               lambda: self.sub(b['original']['n'], b['shifted']['n']))
        assert removed == tail['removed_zero_terms'] and removed in (0, 1)
        if removed:
            idx = self.recorded(tail['last_index'], lambda: self.sub(b['original']['n'], 1))
            last = self.recorded(tail['last_original_z'], lambda: self.add(head['value'], self.mul(step, idx)))
            end = self.recorded(tail['shifted_last'], lambda: self.add(last, 1))
            assert self.recorded(tail['boundary_difference'], lambda: self.sub(end, req['M'])) == 0
        weight = self.recorded(b['original_weight'], lambda: self.sub(req['V'], remainder))
        same(remainder, b['shifted_weight'])
        first = self.recorded(b['original_product'], lambda: self.mul(weight, original))
        second = self.recorded(b['shifted_product'], lambda: self.mul(remainder, shifted))
        diff = self.recorded(b['unsigned_difference'], lambda: self.sub(first, second))
        answer = self.recorded(b['signed_result'], lambda: self.mul(sign, diff))
        same(answer, b['value'])
        assert b['sign_is_original_z_not_shifted_z'] is True
        assert b['signed_operations_stop'] == self.i
        return answer

    def orientation(self, record, label, req):
        assert record['orientation'] == label and record['multiplicity'] == 1
        assert record['signed_operations_start'] == self.i
        inp = req['inputs']
        n = self.length(record['original_length'], record['head']['value'], inp['R'], req['L'])
        if not n:
            assert record['empty'] is True and record['branches'] == []
            answer = self.recorded(record['zero'], lambda: self.add(0, 0))
        else:
            assert record['empty'] is False
            z0, t = self.division(record['compressed_head'], record['head']['value'], req['V'])
            same(t, record['constant_low_remainder'])
            head0 = record['branches'][0]['head']
            self.recorded(head0, lambda: self.add(z0, 0))
            h = req['h']
            if req['h_parity']['remainder'] == 0:
                expected = record['branches'][0]['expected_n']
                self.recorded(expected, lambda: self.add(n, 0))
                specs = [('even_step', head0, h, expected)]
            else:
                split = record['parity_split']
                step = self.recorded(split['twice_h'], lambda: self.add(h, h))
                plus = self.recorded(split['n_plus_one'], lambda: self.add(n, 1))
                even_n, _ = self.division(split['even_count'], plus, 2)
                odd_n, _ = self.division(split['odd_count'], n, 2)
                even, odd = [b['expected_n'] for b in record['branches']]
                self.recorded(even, lambda: self.add(even_n, 0))
                self.recorded(odd, lambda: self.add(odd_n, 0))
                head1 = record['branches'][1]['head']
                self.recorded(head1, lambda: self.add(z0, h))
                specs = [('even_j', head0, step, even), ('odd_j', head1, step, odd)]
            assert len(record['branches']) == len(specs)
            values = [self.branch(b, label+':'+name, head, step, expected, req, t)
                      for b, (name, head, step, expected) in zip(record['branches'], specs)]
            answer = self.recorded(record['total'], lambda: self.total(values))
        same(answer, record['value'])
        assert record['signed_operations_stop'] == self.i
        return answer

    def requests(self, cert):
        for index, req in enumerate(cert['requests']):
            inp = req['inputs']
            assert inp['r'] == index and req['signed_operations_start'] == self.i
            same(self.power(inp['ell']), req['V'])
            h, remainder = self.division(req['alignment'], inp['R'], req['V'])
            assert remainder == 0 and h == req['h']
            self.division(req['h_parity'], h, 2)
            same(self.power(inp['g']-inp['ell']), req['M'])
            same(self.power(inp['k']-inp['ell']), req['U'])
            same(self.add(req['U'], req['U']), req['P'])
            same(self.power(inp['g']-inp['k']-1), req['H'])
            same(self.mul(req['V'], req['M']), req['L'])
            assert req['scales_operations_stop'] == self.i
            self.coefficients(req)
            pos, neg = req['orientations']
            # Both heads are recorded before either orientation executes.
            self.recorded(pos['head'], lambda: self.add(inp['r'], 0))
            self.recorded(neg['head'], lambda: self.sub(inp['R'], inp['r']))
            x = self.orientation(pos, 'nonnegative_difference', req)
            y = self.orientation(neg, 'negative_difference_magnitude', req)
            answer = self.recorded(req['final_addition'], lambda: self.add(x, y))
            same(answer, req['value'])
            assert req['signed_operations_stop'] == self.i
            assert req['raw_denominator_exponent'] == 2*inp['g']
            assert req['compressed_length_is_not_normalization'] is True
        assert self.i == len(self.ops)


def inspect_pairs(record, inputs):
    c = AlignedCursor(record['actual_integer_evidence'])
    same(c.power(inputs['g']), record['length'])
    low, high = record['low_scale'], record['high_scale']
    same(c.power(inputs['ell']), low)
    same(c.power(inputs['k']), high)
    rows = record['digit_observations']
    assert len(rows) == record['length']
    for x, row in enumerate(rows):
        assert row['label'] == x and row['signed_operations_start'] == c.i
        lq, lr = c.div(x, low)
        _, lb = c.div(lq, 2)
        hq, hr = c.div(x, high)
        _, hb = c.div(hq, 2)
        summed = c.add(lb, hb)
        _, parity = c.div(summed, 2)
        same([lq, lr, lb, hq, hr, hb, summed, parity], [row[k] for k in
             ('low_quotient','low_remainder','low_bit','high_quotient','high_remainder','high_bit','bit_sum','parity')])
        assert row['signed_operations_stop'] == c.i
    buckets = [0 for _ in range(inputs['R'])]
    pairs = iter(record['pair_observations'])
    count = 0
    for x in range(record['length']):
        for y in range(record['length']):
            row = next(pairs)
            assert row['x'] == x and row['y'] == y and row['signed_operations_start'] == c.i
            diff = c.sub(y, x)
            quotient, residue = c.div(diff, inputs['R'])
            sign = 1 if rows[x]['parity'] == rows[y]['parity'] else -1
            same([diff, quotient, residue, sign], [row[k] for k in ('difference','quotient','residue','sign')])
            same(row['bucket_before'], buckets[residue])
            buckets[residue] = c.add(buckets[residue], sign)
            same(buckets[residue], row['bucket_after'])
            assert row['signed_operations_stop'] == c.i
            count += 1
    assert next(pairs, None) is None and c.i == len(c.ops)
    assert record['all_residue_buckets_from_one_pair_pass'] is True
    return buckets, count


def inspect_evidence(evidence, native):
    ops, typed = evidence['signed_operations'], evidence['arithmetic_operations']
    same([idx for op in ops for idx in op['typed_operation_indices']], list(range(len(typed))))
    assert len(typed) == evidence['arithmetic_stats']['typed_operations']
    if 'native_source' in evidence:
        same(evidence['native_source'], native)
    assert not evidence['window_weight_queries']
    recounted = trace_accounting({**evidence, 'native_source': native})
    return recounted


def costs(evidences):
    rows = list(evidences)
    keys = ('adder_digit_replays','typed_operations','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
    total = {key: sum(r['arithmetic_stats'][key] for r in rows) for key in keys}
    total.update(signed_operations=sum(len(r['signed_operations']) for r in rows),
                 moment_nodes=sum(len(r['moment_nodes']) for r in rows),
                 window_queries=sum(len(r['window_weight_queries']) for r in rows),
                 moment_requests=sum(r['stats']['moment_requests'] for r in rows),
                 cache_hits=sum(r['stats']['cache_hits'] for r in rows))
    maxima = {key: max(r['stats'][key] for r in rows) for key in ('max_recursion_depth','max_observed_integer_bits')}
    return {'receipts':len(rows),'sum':total,'max':maxima,
            'native_calls_counted_from_disjoint_process_intervals':True}


def incomplete(cert, native):
    assert cert['schema'] == 'INCOMPLETE_'+SCHEMA and cert['complete_certificate'] is False
    assert cert['requests'] == []
    evidence = cert['actual_integer_evidence']
    inspect_evidence(evidence, native)
    c = AlignedCursor(evidence)
    req = cert['inflight_request']
    assert req['signed_operations_start'] == 0
    same(c.power(req['inputs']['ell']), req['V'])
    _, remainder = c.division(req['alignment'], req['inputs']['R'], req['V'])
    assert remainder > 0 and c.i == len(c.ops)


def main():
    compressed = (ROOT/'TWO_BIT_ALIGNED_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert digest(raw) == RAW_PIN and digest(compressed) == GZIP_PIN
    data, summary = json.loads(raw), json.loads((ROOT/'TWO_BIT_ALIGNED_SUMMARY.json').read_bytes())
    assert len(raw) == summary['raw_bytes'] and len(compressed) == summary['gzip_bytes']
    assert data['status'] == summary['status'] == 'PASS'
    same(data['source_sha256'], summary['source_sha256'])
    for name, pin in data['source_sha256'].items():
        assert digest((ROOT/name).read_bytes()) == pin
    guard = (ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guard) == data['startup_guard']['sha256']
    same(json.loads(guard), data['startup_guard']['receipt'])
    assert data['startup_guard']['receipt']['activity_allowed'] is True
    assert data['startup_guard']['receipt']['persistence_allowed'] is True
    assert data['startup_guard']['receipt']['sync_debt_events'] == []
    assert digest((ROOT.parent/'sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md').read_bytes()) == data['two_bit_proof_sha256']
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    for key, path in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
                      'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
                      'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/path).read_bytes()) == native['files_sha256'][key]
    groups = {k:[] for k in ('production','typed_pair_comparator','positive_replay','paid_input_rejection','negative_replay')}
    case_rows, pairs, tables, progressions = [], 0, 0, 0
    for case in data['cases']:
        cert, replay = case['certificate'], case['verification']['replay_certificate']
        assert cert['schema'] == SCHEMA and cert['source_sha256'] == data['source_sha256']['aligned_two_bit.py']
        for key, path in {'direct_source_sha256':'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
                          'direct_proof_sha256':'sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md',
                          'two_bit_proof_sha256':'sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md',
                          'floor_moment_source_sha256':'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
                          'baseline_helper_source_sha256':'sep27-qft-signedgap/signed_gap/signed_gap.py'}.items():
            assert digest((ROOT.parent/path).read_bytes()) == cert[key]
        assert semantic(cert) == semantic(replay)
        for item in (cert, replay):
            inspect_evidence(item['actual_integer_evidence'], native)
            AlignedCursor(item['actual_integer_evidence']).requests(item)
        assert case['verification']['verified'] is True
        comparator = case['typed_enumeration']
        inspect_evidence(comparator['actual_integer_evidence'], native)
        values, count = inspect_pairs(comparator, case['inputs'])
        same(values, case['values'])
        same(values, [r['value'] for r in cert['requests']])
        pairs += count
        tables += sum(r['top_level_table_calls'] for r in cert['requests'])
        progressions += sum(r['single_progression_calls'] for r in cert['requests'])
        for name, e in (('production',cert['actual_integer_evidence']),
                        ('typed_pair_comparator',comparator['actual_integer_evidence']),
                        ('positive_replay',replay['actual_integer_evidence'])):
            groups[name].append(e)
        case_rows.append({'inputs':case['inputs'],'values':values,'typed_pair_observations':count,
                          'production_digits':cert['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'],
                          'comparator_digits':comparator['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']})
    assert pairs == summary['typed_pair_observations'] == 720
    assert tables == summary['top_level_table_calls'] == 332
    assert progressions == summary['single_progression_calls'] == 236
    negatives=[]
    for row in data['negative_checks']:
        assert row['rejected'] is True
        captures=row['actual_replay_certificates']
        if row['name'].endswith('_early'):
            assert captures == []
        else:
            assert len(captures) == 1
            capture=captures[0]
            if row['name']=='unaligned_input_paid_partial':
                incomplete(capture,native)
            else:
                assert semantic(capture)==semantic(data['cases'][row['source_case_index']]['certificate'])
                inspect_evidence(capture['actual_integer_evidence'],native)
                AlignedCursor(capture['actual_integer_evidence']).requests(capture)
            groups['negative_replay'].append(capture['actual_integer_evidence'])
        negatives.append({'name':row['name'],'error':row['error'],'retained_replays':len(captures),
                          'retained_complete': bool(captures) and captures[0]['schema']==SCHEMA})
    assert len(negatives)==12 and len(groups['negative_replay'])==8
    for row in data['input_rejections']:
        assert row['rejected'] is True
        if row['kind']=='ordinary_pre_rejection':
            assert row['actual_typed_operations']==0
        else:
            incomplete(row['incomplete_receipt'],native)
            groups['paid_input_rejection'].append(row['incomplete_receipt']['actual_integer_evidence'])
            reuse=row['reuse_rejection']
            assert reuse['rejected'] is True and reuse['prior_inflight_and_all_evidence_unchanged'] is True
            assert reuse['additional_typed_operations']==0
    assert len(data['input_rejections'])==12 and len(groups['paid_input_rejection'])==2
    categorized={key:costs(rows) for key,rows in groups.items()}
    same(categorized,data['cost_categories']); same(categorized,summary['cost_categories'])
    frontier=0; native_by=Counter()
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        native_by[row['category']]+=row['stop']-row['start']
        frontier=row['stop']
    assert frontier==len(data['actual_core_calls'])==summary['actual_core_call_count']==1
    same(dict(native_by),summary['native_calls_by_category'])
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for es in groups.values() for e in es)==1
    total_digits=sum(c['sum']['adder_digit_replays'] for c in categorized.values())
    assert total_digits==255115
    result={'status':'PASS_FULL_AUTHOR_SAVED_EVIDENCE_READBACK','scientific_execution_performed':False,
            'reader_sha256':digest(Path(__file__).read_bytes()),'source_sha256':data['source_sha256'],
            'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':len(raw),'gzip_bytes':len(compressed),
            'summary_sha256':digest((ROOT/'TWO_BIT_ALIGNED_SUMMARY.json').read_bytes()),
            'log_sha256':digest((ROOT/'TWO_BIT_ALIGNED_EXECUTION_LOG.txt').read_bytes()),
            'guard_sha256':digest(guard),'case_rows':case_rows,'cost_categories':categorized,
            'all_scientific_receipts_read':sum(len(v) for v in groups.values()),'total_adder_digit_replays':total_digits,
            'typed_pair_observations':pairs,'single_progression_calls':progressions,'top_level_table_calls':tables,
            'negative_checks':negatives,'input_rejections':12,'unchanged_reuse_rejections':2,
            'native_source':native,'actual_core_calls':data['actual_core_calls'],
            'native_calls_by_category':dict(native_by),'elapsed_seconds_before_serialization':summary['elapsed_seconds_before_serialization'],
            'failure_artifact_present':(ROOT/'TWO_BIT_ALIGNED_FAILED_EXECUTION.json.gz').exists(),
            'coverage':'All outer production/replay recording edges, all pair/digit bucket chains, native-column cells and cost counts; saved moment outputs, not new moment evaluation.',
            'limitation':'Author shared-context readback, not formal independent admission; bounded scalar observer only; no timing speed claim.'}
    target=ROOT/'ALIGNED_COST_READBACK.json'
    with target.open('x',encoding='utf-8') as stream:
        stream.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'reader_sha256':result['reader_sha256'],
                      'record_sha256':digest(target.read_bytes()),'receipts':result['all_scientific_receipts_read'],
                      'total_digits':total_digits,'production_digits':categorized['production']['sum']['adder_digit_replays'],
                      'typed_comparator_digits':categorized['typed_pair_comparator']['sum']['adder_digit_replays']}))


if __name__ == '__main__':
    main()

