"""Pure saved-record I/O review; never imports or runs scientific arithmetic.

All arithmetic cursor methods consume recorded outputs. Host work is hashes,
strict equality, sign encoding, address/coverage checks and cost accounting.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import gzip
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT.parent/'sep27-qft-gap-direct/guard_review/read_direct_result.py'
HELPER_PIN = '4b7e7d1bf7e4b7575d6b202f680acbac62861e16551aa4971ba7b74848571098'
RAW_PIN = '61aee1882148519bd9738bacf6f107a39532aa98de6c128854edb98df334aba9'
GZIP_PIN = 'f6bf350f188d4252c60c897778561e3c4957d65774a25a12334b35261f0b7bd3'
SOURCE_PINS = {
    'aligned_two_bit.py': 'a6fd6cf5bfe10829c1918c50a952de22e5e2bc6cd538011f37a3bffdff5acdb2',
    'check_aligned_two_bit.py': '6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969',
    'DESIGN.md': '90605ff87a2a9f37576c57bb9f5363407c29778f87fef0c17aa6621713908876'}
DEPENDENCIES = {
    'direct_source_sha256': ('sep27-qft-gap-direct/direct_gap/direct_signed_gap.py', '3ab2515c1b9df35d01c9605f21d8f8fe56bd044effe489063192c0a5c56a8521'),
    'direct_proof_sha256': ('sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md', 'c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf'),
    'two_bit_proof_sha256': ('sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md', '9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26'),
    'floor_moment_source_sha256': ('sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py', '633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2'),
    'baseline_helper_source_sha256': ('sep27-qft-signedgap/signed_gap/signed_gap.py', '86ea28956fa7ac9c41fb38a8c63f4ba00b0377f3264b5a525c46c5335faff90a')}
CASES = ((2,0,1,1), (3,0,1,3), (3,1,2,2), (3,1,2,4), (4,1,3,6), (4,2,3,20))
SCHEMA = 'BRC_ALIGNED_TWO_BIT_STRETCH_V1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


assert digest(HELPER.read_bytes()) == HELPER_PIN
spec = importlib.util.spec_from_file_location('pinned_direct_io_review', HELPER)
io = importlib.util.module_from_spec(spec)
spec.loader.exec_module(io)
same = io.same


def signed_typed_links(evidence):
    """Bind saved signed results to saved typed output fields, not evaluation."""
    typed = evidence['arithmetic_operations']
    same([j for op in evidence['signed_operations'] for j in op['typed_operation_indices']],
         list(range(len(typed))))
    for operation in evidence['signed_operations']:
        steps = [typed[j] for j in operation['typed_operation_indices']]
        at = 0
        def take(kind, left, right):
            nonlocal at
            row = steps[at]
            at += 1
            assert row['operation'] == kind
            t = row['trace']
            if kind == 'divide':
                same([t['value'], t['modulus']], [left, right])
                return t['quotient'], t['remainder']
            same([t['left'], t['right']], [left, right])
            if kind == 'add':
                assert t['carry'] == 0
                return t['low']
            if kind == 'multiply':
                return t['value']
            assert kind == 'compare'
            return t['relation'], t['low_difference']
        x, y = operation['inputs']
        if operation['operation'] == 'signed_add':
            if (x < 0) == (y < 0):
                mag = take('add', abs(x), abs(y))
                result = -mag if x < 0 else mag
            else:
                relation, mag = take('compare', abs(x), abs(y))
                if relation < 0:
                    _, mag = take('compare', abs(y), abs(x))
                    result = -mag if y < 0 else mag
                else:
                    result = -mag if x < 0 else mag
        elif operation['operation'] == 'signed_multiply':
            mag = take('multiply', abs(x), abs(y))
            result = -mag if (x < 0) != (y < 0) else mag
        else:
            assert operation['operation'] == 'signed_euclidean_division' and y > 0
            quotient, remainder = take('divide', abs(x), y)
            if x < 0:
                if remainder:
                    quotient = take('add', quotient, 1)
                    _, remainder = take('compare', y, remainder)
                quotient = -quotient
            result = [quotient, remainder]
        same(result, operation['result'])
        assert at == len(steps)
    assert len(typed) == evidence['arithmetic_stats']['typed_operations']


def inspect_evidence(evidence, native, partial=False):
    signed_typed_links(evidence)
    assert evidence['window_weight_queries'] == []
    if not partial:
        same(evidence['native_source'], native)
        assert evidence['source_sha256'] == DEPENDENCIES['floor_moment_source_sha256'][1]
    view = dict(evidence)
    view['native_source'] = native
    counted = io.trace_accounting(view)
    return {'signed_operations': len(evidence['signed_operations']),
            'typed_operations': len(evidence['arithmetic_operations']),
            'moment_nodes': len(evidence['moment_nodes']),
            'all_signed_to_typed_and_native_cell_links_checked': True,
            'recounted_cost': counted}


class Cursor(io.RecordedCursor):
    def power(self, exponent, expected):
        value = 1
        for _ in range(exponent):
            value = self.add(value, value)
        same(value, expected)
        return value

    def division(self, record, x, m):
        same([record['numerator'], record['denominator']], [x, m])
        assert record['signed_operations_start'] == self.i
        q, rem = self.div(x, m)
        same([q, rem], [record['quotient'], record['remainder']])
        assert record['signed_operations_stop'] == self.i
        return q, rem

    def coefficients(self, req):
        H, P = req['H'], req['P']
        four = self.recorded(req['coefficient_helpers']['four_H'], lambda: self.mul(4, H))
        eight = self.recorded(req['coefficient_helpers']['eight_H'], lambda: self.mul(8, H))
        checks = (
            ('n', lambda: self.mul(H, P)), ('q', lambda: self.mul(self.sub(four, 2), P)),
            ('dq', lambda: self.add(4, 0)), ('q2', lambda: self.mul(-4, P)),
            ('d', lambda: self.sub(1, four)), ('ddelta', lambda: self.sub(eight, 4)),
            ('dqdelta', lambda: self.add(-8, 0)), ('q2delta', lambda: self.mul(8, P)),
            ('qdelta', lambda: self.mul(self.sub(8, eight), P)),
            ('delta', lambda: self.mul(self.sub(2, four), P)))
        for key, operation in checks:
            self.recorded(req['coefficients'][key], operation)

    def length(self, record, head, step, limit):
        same([record['head'], record['step'], record['limit']], [head, step, limit])
        d = self.recorded(record['last_minus_head'], lambda: self.sub(self.sub(limit, 1), head))
        if d < 0:
            assert record['empty'] is True and record['n'] == 0
            same(self.recorded(record['zero'], lambda: self.add(0, 0)), 0)
        else:
            assert record['empty'] is False
            q, _ = self.division(record['division'], d, step)
            n = self.recorded(record['length_addition'], lambda: self.add(q, 1))
            same(n, record['n'])
        return record['n']

    def branch(self, branch, label, head, step, expected, req, remainder):
        assert branch['label'] == label and branch['signed_operations_start'] == self.i
        same([branch['head'], branch['step'], branch['expected_n']], [head, step, expected])
        _, parity = self.division(branch['parity'], head['value'], 2)
        assert parity in (0, 1)
        sign = -1 if parity else 1
        same(branch['sign'], sign)
        small = {'inputs': {'R': step}, 'L': req['M'], 'U': req['U'], 'P': req['P'],
                 'coefficients': req['coefficients']}
        original = self.progression(branch['original'], head, label+':original', small)
        difference = self.recorded(branch['canonical_count_difference'],
            lambda: self.sub(branch['original']['n'], expected['value']))
        assert difference == 0
        shifted_head = branch['shifted']['head']
        self.recorded(shifted_head, lambda: self.add(head['value'], 1))
        shifted = self.progression(branch['shifted'], shifted_head, label+':shifted', small)
        tail = branch['shifted_zero_tail']
        removed = self.recorded(tail['count_difference'],
            lambda: self.sub(branch['original']['n'], branch['shifted']['n']))
        same(removed, tail['removed_zero_terms'])
        assert removed in (0, 1)
        if removed:
            assert branch['original']['n'] > 0
            last = self.recorded(tail['last_index'], lambda: self.sub(branch['original']['n'], 1))
            last_z = self.recorded(tail['last_original_z'], lambda: self.add(head['value'], self.mul(step, last)))
            shifted_last = self.recorded(tail['shifted_last'], lambda: self.add(last_z, 1))
            assert self.recorded(tail['boundary_difference'], lambda: self.sub(shifted_last, req['M'])) == 0
        weight = self.recorded(branch['original_weight'], lambda: self.sub(req['V'], remainder))
        same(branch['shifted_weight'], remainder)
        first = self.recorded(branch['original_product'], lambda: self.mul(weight, original))
        second = self.recorded(branch['shifted_product'], lambda: self.mul(remainder, shifted))
        unsigned = self.recorded(branch['unsigned_difference'], lambda: self.sub(first, second))
        answer = self.recorded(branch['signed_result'], lambda: self.mul(sign, unsigned))
        same(answer, branch['value'])
        assert branch['sign_is_original_z_not_shifted_z'] is True
        assert branch['signed_operations_stop'] == self.i
        return answer

    def orientation(self, orientation, label, req):
        assert orientation['orientation'] == label and orientation['multiplicity'] == 1
        assert orientation['signed_operations_start'] == self.i
        b = orientation['head']['value']
        length = self.length(orientation['original_length'], b, req['inputs']['R'], req['L'])
        if orientation['original_length']['empty']:
            assert orientation['empty'] is True and not orientation['branches']
            answer = self.recorded(orientation['zero'], lambda: self.add(0, 0))
        else:
            assert orientation['empty'] is False
            z0, t = self.division(orientation['compressed_head'], b, req['V'])
            same(t, orientation['constant_low_remainder'])
            branches = orientation['branches']
            first_head = branches[0]['head']
            self.recorded(first_head, lambda: self.add(z0, 0))
            if req['h_parity']['remainder'] == 0:
                assert len(branches) == 1
                expected = branches[0]['expected_n']
                self.recorded(expected, lambda: self.add(length, 0))
                specs = [('even_step', first_head, req['h'], expected)]
            else:
                assert req['h_parity']['remainder'] == 1 and len(branches) == 2
                split = orientation['parity_split']
                step = self.recorded(split['twice_h'], lambda: self.add(req['h'], req['h']))
                n1 = self.recorded(split['n_plus_one'], lambda: self.add(length, 1))
                ne, _ = self.division(split['even_count'], n1, 2)
                no, _ = self.division(split['odd_count'], length, 2)
                even, odd = branches[0]['expected_n'], branches[1]['expected_n']
                self.recorded(even, lambda: self.add(ne, 0))
                self.recorded(odd, lambda: self.add(no, 0))
                second_head = branches[1]['head']
                self.recorded(second_head, lambda: self.add(z0, req['h']))
                specs = [('even_j', first_head, step, even), ('odd_j', second_head, step, odd)]
            values = [self.branch(branch, label+':'+part, head, step, expected, req, t)
                      for branch, (part, head, step, expected) in zip(branches, specs)]
            answer = self.recorded(orientation['total'], lambda: self.total(values))
        same(answer, orientation['value'])
        assert orientation['signed_operations_stop'] == self.i
        return answer


def inspect_certificate(cert, native):
    assert cert['schema'] == SCHEMA and cert['source_sha256'] == SOURCE_PINS['aligned_two_bit.py']
    for key, (_, pin) in DEPENDENCIES.items():
        assert cert[key] == pin
    e = cert['actual_integer_evidence']
    result = inspect_evidence(e, native)
    c = Cursor(e)
    for index, req in enumerate(cert['requests']):
        inp = req['inputs']
        assert all(type(v) is int for v in inp.values())
        assert set(inp) == {'g', 'ell', 'k', 'R', 'r', 'stride'}
        assert inp['g'] >= 2 and 0 <= inp['ell'] < inp['k'] < inp['g']
        assert inp['R'] >= 1 and inp['r'] == index and inp['stride'] == 1
        assert req['signed_operations_start'] == c.i
        c.power(inp['ell'], req['V'])
        h, rem = c.division(req['alignment'], inp['R'], req['V'])
        same(h, req['h']); assert rem == 0
        c.division(req['h_parity'], h, 2)
        c.power(inp['g']-inp['ell'], req['M'])
        c.power(inp['k']-inp['ell'], req['U'])
        same(c.add(req['U'], req['U']), req['P'])
        c.power(inp['g']-inp['k']-1, req['H'])
        same(c.mul(req['V'], req['M']), req['L'])
        assert req['scales_operations_stop'] == c.i
        c.coefficients(req)
        assert len(req['orientations']) == 2
        pos, neg = req['orientations']
        c.recorded(pos['head'], lambda: c.add(inp['r'], 0))
        c.recorded(neg['head'], lambda: c.sub(inp['R'], inp['r']))
        p = c.orientation(pos, 'nonnegative_difference', req)
        n = c.orientation(neg, 'negative_difference_magnitude', req)
        value = c.recorded(req['final_addition'], lambda: c.add(p, n))
        same(value, req['value'])
        assert req['signed_operations_stop'] == c.i
        assert req['raw_denominator_exponent'] == 2*inp['g']
        assert req['compressed_length_is_not_normalization'] is True and req['negative_values_are_valid'] is True
        progressions = [b[k] for o in req['orientations'] for b in o['branches'] for k in ('original', 'shifted')]
        assert len(progressions) == req['single_progression_calls'] <= 8
        assert sum(len(p['table_calls']) for p in progressions) == req['top_level_table_calls'] <= 16
    assert c.i == len(c.ops)
    result.update(requests=len(cert['requests']), top_level_tables=c.seen_tables,
                  empty_progressions=c.empty_progressions)
    return result


def inspect_partial(cert, native):
    assert cert['schema'] == 'INCOMPLETE_'+SCHEMA and cert['complete_certificate'] is False
    assert cert['source_sha256'] == SOURCE_PINS['aligned_two_bit.py'] and cert['requests'] == []
    e, req = cert['actual_integer_evidence'], cert['inflight_request']
    result = inspect_evidence(e, native, partial=True)
    assert e['moment_nodes'] == [] and req['signed_operations_start'] == 0
    c = Cursor(e)
    c.power(req['inputs']['ell'], req['V'])
    _, rem = c.division(req['alignment'], req['inputs']['R'], req['V'])
    assert rem > 0 and c.i == len(c.ops)
    result['paid_unaligned_rejection'] = True
    return result


def inspect_comparator(case, native):
    inp, brute = case['inputs'], case['typed_enumeration']
    e = brute['actual_integer_evidence']
    result = inspect_evidence(e, native)
    assert not e['moment_nodes'] and brute['all_residue_buckets_from_one_pair_pass'] is True
    c = Cursor(e)
    c.power(inp['g'], brute['length'])
    c.power(inp['ell'], brute['low_scale'])
    c.power(inp['k'], brute['high_scale'])
    digits = []
    assert len(brute['digit_observations']) == brute['length']
    for x, row in enumerate(brute['digit_observations']):
        assert row['label'] == x and row['signed_operations_start'] == c.i
        lq, lr = c.div(x, brute['low_scale'])
        _, lb = c.div(lq, 2)
        hq, hr = c.div(x, brute['high_scale'])
        _, hb = c.div(hq, 2)
        bs = c.add(lb, hb)
        _, parity = c.div(bs, 2)
        same([lq,lr,lb,hq,hr,hb,bs,parity], [row[k] for k in
            ('low_quotient','low_remainder','low_bit','high_quotient','high_remainder','high_bit','bit_sum','parity')])
        assert lb in (0,1) and hb in (0,1) and parity in (0,1)
        assert row['signed_operations_stop'] == c.i
        digits.append(parity)
    buckets = [0 for _ in range(inp['R'])]
    addresses = [(x,y) for x in range(brute['length']) for y in range(brute['length'])]
    same([(r['x'],r['y']) for r in brute['pair_observations']], addresses)
    for row in brute['pair_observations']:
        assert row['signed_operations_start'] == c.i
        difference = c.sub(row['y'], row['x'])
        quotient, residue = c.div(difference, inp['R'])
        same([difference,quotient,residue], [row['difference'],row['quotient'],row['residue']])
        assert type(residue) is int and 0 <= residue < inp['R']
        sign = 1 if digits[row['x']] == digits[row['y']] else -1
        same(sign, row['sign']); same(buckets[residue], row['bucket_before'])
        after = c.add(buckets[residue], sign)
        same(after, row['bucket_after'])
        buckets[residue] = after
        assert row['signed_operations_stop'] == c.i
    assert c.i == len(c.ops)
    same(buckets, case['values'])
    same(buckets, [r['value'] for r in case['certificate']['requests']])
    result.update(labels=len(digits), ordered_pairs=len(addresses), all_buckets_bound_to_recorded_updates=True)
    return result


def decode_keys(item):
    if type(item) is dict:
        assert set(item) == {'object_entries'}
        out = {}
        for entry in item['object_entries']:
            key = entry['key']
            assert type(key).__name__ == entry['key_type'] and key not in out
            out[key] = decode_keys(entry['value'])
        return out
    if type(item) is list:
        return [decode_keys(x) for x in item]
    return item


def costs(evidences):
    keys = ('adder_digit_replays','typed_operations','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
    total = {k:sum(e['arithmetic_stats'][k] for e in evidences) for k in keys}
    for name, field in (('signed_operations','signed_operations'),('moment_nodes','moment_nodes'),('window_queries','window_weight_queries')):
        total[name] = sum(len(e[field]) for e in evidences)
    for k in ('moment_requests','cache_hits'):
        total[k] = sum(e['stats'][k] for e in evidences)
    return {'receipts':len(evidences),'sum':total,
        'max':{k:max(e['stats'][k] for e in evidences) for k in ('max_recursion_depth','max_observed_integer_bits')},
        'native_calls_counted_from_disjoint_process_intervals':True}


def main():
    data, summary = io.load(ROOT, 'TWO_BIT_ALIGNED', RAW_PIN, GZIP_PIN)
    same(data['source_sha256'], SOURCE_PINS)
    for _, (rel, pin) in DEPENDENCIES.items():
        assert digest((ROOT.parent/rel).read_bytes()) == pin
    guard_bytes = (ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guard_bytes) == data['startup_guard']['sha256']
    same(json.loads(guard_bytes), data['startup_guard']['receipt'])
    guard = data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events'] == []
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC'
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    assert native['native_adder']['input_columns'] == 8 and native['native_adder']['positive_BRC_input_states'] == 12
    native_paths = {
        'lazy_modular': 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular': 'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks': 'sep26-shor-general/completion/typed_integer_prechecks.py'}
    for name, rel in native_paths.items():
        assert digest((ROOT.parent/rel).read_bytes()) == native['files_sha256'][name]
    groups = {k:[] for k in ('production','typed_pair_comparator','positive_replay','paid_input_rejection','negative_replay')}
    reviewed = []
    for index, case in enumerate(data['cases']):
        same(tuple(case['inputs'][k] for k in ('g','ell','k','R')), CASES[index])
        cert, verification = case['certificate'], case['verification']
        assert case['all_residues_equal'] is True and verification['verified'] is True
        assert verification['requests_replayed'] == len(cert['requests'])
        replay = verification['replay_certificate']
        assert io.semantic(cert) == io.semantic(replay)
        review = {'inputs':case['inputs'], 'values':case['values'],
            'production':inspect_certificate(cert,native),
            'typed_comparator':inspect_comparator(case,native),
            'positive_replay':inspect_certificate(replay,native)}
        reviewed.append(review)
        for category, evidence in (('production',cert['actual_integer_evidence']),
                ('typed_pair_comparator',case['typed_enumeration']['actual_integer_evidence']),
                ('positive_replay',replay['actual_integer_evidence'])):
            groups[category].append(evidence)
    assert len(reviewed) == 6 and sum(r['production']['requests'] for r in reviewed) == 36
    assert sum(r['typed_comparator']['ordered_pairs'] for r in reviewed) == 720
    input_reviews = []
    for record in data['input_rejections']:
        assert record['rejected'] is True
        if record['kind'] == 'ordinary_pre_rejection':
            assert record['actual_typed_operations'] == 0 and 'incomplete_receipt' not in record
            review = {'kind':record['kind'],'args':record['args'],'no_work_recorded':True}
        else:
            assert record['kind'] == 'paid_unaligned_rejection'
            review = inspect_partial(record['incomplete_receipt'],native)
            groups['paid_input_rejection'].append(record['incomplete_receipt']['actual_integer_evidence'])
            reuse = record['reuse_rejection']
            assert reuse['rejected'] is True and reuse['prior_inflight_and_all_evidence_unchanged'] is True
            assert reuse['additional_typed_operations'] == 0
            assert reuse['call_interval']['start'] == reuse['call_interval']['stop']
            review.update(args=record['args'],reuse_negative=deepcopy(reuse))
        input_reviews.append(review)
    assert len(input_reviews) == 12 and len(groups['paid_input_rejection']) == 2
    negative_reviews = []
    expected_names = ['drop_half_modulus_orientation','compressed_length','shifted_zero_tail',
        'original_branch_sign','compressed_step_parity','original_raw_exponent','signed_output',
        'unaligned_input_paid_partial','source_early','schema_early','bool_input_early','nonstring_key_early']
    same([n['name'] for n in data['negative_checks']],expected_names)
    for record in data['negative_checks']:
        assert record['rejected'] is True
        attempted = decode_keys(record['attempted_certificate_typed_key_encoding'])
        capture = record['actual_replay_certificates']
        if record['name'].endswith('_early'):
            assert capture == [] and record['call_interval']['start'] == record['call_interval']['stop']
            result = {'type':'early','paid_receipts':0}
        else:
            assert len(capture) == 1
            replay = capture[0]
            groups['negative_replay'].append(replay['actual_integer_evidence'])
            if record['name'] == 'unaligned_input_paid_partial':
                result = inspect_partial(replay,native)
                same(replay['inflight_request']['inputs'],attempted['requests'][0]['inputs'])
                result['type'] = 'paid_partial'
            else:
                honest = data['cases'][record['source_case_index']]['certificate']
                assert io.semantic(replay) == io.semantic(honest)
                assert io.semantic(replay) != io.semantic(attempted)
                result = inspect_certificate(replay,native)
                result['type'] = 'paid_full'
            result['paid_receipts'] = 1
        result.update(name=record['name'],error=record['error'])
        negative_reviews.append(result)
    calculated = {name:costs(es) for name,es in groups.items()}
    same(calculated,data['cost_categories']); same(calculated,summary['cost_categories'])
    frontier = 0
    call_categories = Counter()
    for interval in data['call_intervals']:
        assert interval['start'] == frontier and interval['stop'] >= frontier
        frontier = interval['stop']
        call_categories[interval['category']] += interval['stop']-interval['start']
    same(dict(call_categories),data['native_calls_by_category'])
    same(data['call_intervals'],summary['call_intervals'])
    assert frontier == len(data['actual_core_calls']) == data['actual_core_call_count'] == 1
    assert data['actual_core_calls'][0]['states'] == 12
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for es in groups.values() for e in es) == 1
    totals = {k:sum(row['sum'][k] for row in calculated.values()) for k in calculated['production']['sum']}
    assert totals['adder_digit_replays'] == 255115
    result = {'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW',
        'scope':'Shared-context metadata-only peer review; no science import, arithmetic recomputation or experiment',
        'reader_sha256':digest(Path(__file__).read_bytes()),'pure_io_helper_sha256':HELPER_PIN,
        'source_sha256':SOURCE_PINS,'dependencies':{k:{'path':p,'sha256':h} for k,(p,h) in DEPENDENCIES.items()},
        'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':summary['raw_bytes'],'gzip_bytes':summary['gzip_bytes'],
        'startup_guard_sha256':digest(guard_bytes),'native_source':native,'cases':reviewed,
        'input_rejections':input_reviews,'negative_checks':negative_reviews,'cost_categories':calculated,
        'total_current_run_cost':totals,'native_calls_by_category':dict(call_categories),
        'actual_core_calls':data['actual_core_calls'],'declared_coverage':data['coverage'],
        'unexpected_failure_artifact_present':(ROOT/'TWO_BIT_ALIGNED_FAILED_EXECUTION.json.gz').exists(),
        'scientific_execution_performed':False,'comparison_is_timing_benchmark':False,
        'limits':['Native arithmetic results are linked to saved source-bound cell observations, not scientifically recomputed.',
                  'Moment table outputs and node links are bound to complete fresh replay; no new recurrence evaluation.',
                  'Reuse no-work snapshot equality was executed by the frozen checker; the saved receipt retains its assertion and original snapshot.',
                  'This is aligned supplied-modulus scalar counting, not a Gram/sampling/order-discovery test.']}
    out = Path(__file__).parent/'ALIGNED_RECORD_REVIEW.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'total':totals,'sha256':digest(out.read_bytes())}))


if __name__ == '__main__':
    main()
