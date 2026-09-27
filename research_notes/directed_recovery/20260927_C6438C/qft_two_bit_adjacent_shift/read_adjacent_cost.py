"""Complete author readback of saved adjacent-bit evidence; stdlib I/O only.

No scientific module is imported, no scalar answer is recomputed, and no
experiment is repeated. Cursor operations consume already recorded outputs.
"""
from pathlib import Path
from collections import Counter
import ast, gzip, hashlib, importlib.util, json

ROOT = Path(__file__).resolve().parent
HELPER = ROOT.parent/'sep27-qft-two-bit-top-general/read_top_general_cost.py'
HELPER_PIN = 'a96696eb187d6c6251934f9b1651f5abc1b8d2db5a5357ea051960b8e4489f5a'
RAW_PIN = 'a084a16fa26a9a2143729620ba3f2fdc1331579ae16087a5f3ddcce199a96d82'
GZIP_PIN = '385295e9a5581ce762761f24d0d5c25e32f9bc06d645f32fbaecbdffd75b8294'
SCHEMA = 'BRC_ADJACENT_BITS_SHIFTED_SINGLE_BIT_V1'
assert hashlib.sha256(HELPER.read_bytes()).hexdigest() == HELPER_PIN
spec = importlib.util.spec_from_file_location('frozen_saved_readback', HELPER)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
digest, same = old.digest, old.same


class AdjacentCursor(old.RecordedCursor):
    def power(self, exponent):
        value = 1
        for _ in range(exponent):
            value = self.add(value, value)
        return value

    def coefficients(self, req):
        H, P = req['H'], req['P']
        h = req['coefficient_helpers']
        four = self.recorded(h['four_H'], lambda: self.mul(4, H))
        eight = self.recorded(h['eight_H'], lambda: self.mul(8, H))
        functions = (
            ('n', lambda: self.mul(H, P)),
            ('q', lambda: self.mul(self.sub(four, 2), P)),
            ('dq', lambda: self.add(4, 0)),
            ('q2', lambda: self.mul(-4, P)),
            ('d', lambda: self.sub(1, four)),
            ('ddelta', lambda: self.sub(eight, 4)),
            ('dqdelta', lambda: self.add(-8, 0)),
            ('q2delta', lambda: self.mul(8, P)),
            ('qdelta', lambda: self.mul(self.sub(8, eight), P)),
            ('delta', lambda: self.mul(self.sub(2, four), P)))
        for key, fn in functions:
            self.recorded(req['coefficients'][key], fn)

    def adjacent_progression(self, rec, head, orientation, req):
        assert rec['signed_operations_start'] == self.i
        assert rec['orientation'] == orientation and rec['multiplicity'] == 1
        base = rec['single_bit_progression']
        value = self.progression(base, head, orientation, req)
        same([rec['empty'], rec['n']], [base['empty'], base['n']])
        if base['empty']:
            assert rec['correction'] is None and value == 0
        else:
            correction = rec['correction']
            assert correction['signed_operations_start'] == self.i
            b, n, V, P, R = head['value'], rec['n'], req['V'], req['P'], req['inputs']['R']
            cc = req['correction_coefficients']
            offset = self.recorded(correction['offsets'][0], lambda: self.add(b, cc['threeV']['value']))
            ta = self.table(correction['table_calls'][0], n, P, R, offset)
            offset = self.recorded(correction['offsets'][1], lambda: self.add(b, V))
            tb = self.table(correction['table_calls'][1], n, P, R, offset)
            wa = self.recorded(correction['weighted_floors'][0],
                lambda: self.add(self.mul(b, ta['0,1']), self.mul(R, ta['1,1'])))
            wb = self.recorded(correction['weighted_floors'][1],
                lambda: self.add(self.mul(b, tb['0,1']), self.mul(R, tb['1,1'])))
            displacement = base['weighted_sums']['d']['value']
            same(displacement, correction['reused_single_bit_displacement_sum'])
            functions = (
                ('linear_d', lambda: self.mul(-2, displacement)),
                ('weighted_floor_difference', lambda: self.mul(4, self.sub(wa, wb))),
                ('floor_sum', lambda: self.mul(cc['fourV']['value'], self.add(ta['0,1'], tb['0,1']))),
                ('floor_square_difference', lambda: self.mul(cc['eightV']['value'], self.sub(tb['0,2'], ta['0,2']))))
            terms = [self.recorded(correction['terms'][key], fn) for key, fn in functions]
            delta = self.recorded(correction['sum'], lambda: self.total(terms))
            assert correction['signed_operations_stop'] == self.i
            value = self.recorded(rec['combined'], lambda: self.add(value, delta))
        same(rec['value'], value)
        assert rec['signed_operations_stop'] == self.i
        return value

    def requests(self, cert):
        for req in cert['requests']:
            assert req['signed_operations_start'] == req['scales_operations_start'] == self.i
            inp = req['inputs']
            assert set(inp) == {'g', 'ell', 'k', 'R', 'r', 'stride'}
            assert all(type(v) is int for v in inp.values())
            g, ell, k, R, r = [inp[key] for key in ('g', 'ell', 'k', 'R', 'r')]
            assert g >= 2 and 0 <= ell and k == ell+1 and k < g
            assert R >= 1 and 0 <= r < R and inp['stride'] == 1
            V = self.power(ell); U = self.add(V, V); P = self.add(U, U)
            H = self.power(g-k-1); L = self.mul(H, P)
            same([V, U, P, H, L], [req[key] for key in ('V', 'U', 'P', 'H', 'L')])
            assert req['scales_operations_stop'] == self.i
            self.coefficients(req)
            cc = req['correction_coefficients']
            self.recorded(cc['threeV'], lambda: self.add(U, V))
            self.recorded(cc['fourV'], lambda: self.mul(4, V))
            self.recorded(cc['eightV'], lambda: self.mul(8, V))
            assert len(req['progressions']) == 2
            a, b = req['progressions']; head = a['single_bit_progression']['head']
            self.recorded(head, lambda: self.add(r, 0))
            pos = self.adjacent_progression(a, head, 'nonnegative_difference', req)
            head = b['single_bit_progression']['head']
            self.recorded(head, lambda: self.sub(R, r))
            neg = self.adjacent_progression(b, head, 'negative_difference_magnitude', req)
            result = self.recorded(req['final_addition'], lambda: self.add(pos, neg))
            same(result, req['value'])
            assert req['signed_operations_stop'] == self.i
            assert req['complete'] is True and req['negative_values_are_valid'] is True
            assert req['raw_denominator_exponent'] == 2*g
        assert self.i == len(self.ops)


def inspect(cert, native):
    old.inspect_evidence(cert['actual_integer_evidence'], native)
    AdjacentCursor(cert['actual_integer_evidence']).requests(cert)


def inspect_partial(cert, original, native):
    assert cert['schema'] == 'INCOMPLETE_'+SCHEMA and cert['complete_certificate'] is False
    assert cert['inflight'] is None and cert['failed'] is False and len(cert['requests']) == 1
    assert cert['source_sha256'] == original['source_sha256']
    same(cert['requests'], original['requests'][:1]); inspect(cert, native)
    e = cert['actual_integer_evidence']; full = original['actual_integer_evidence']
    same(e['signed_operations'], full['signed_operations'][:len(e['signed_operations'])])
    same(e['arithmetic_operations'], full['arithmetic_operations'][:len(e['arithmetic_operations'])])
    same(e['moment_nodes'], full['moment_nodes'][:len(e['moment_nodes'])])


def source_pins(cert):
    targets = {
        'source_sha256': ROOT/'adjacent_shift.py',
        'adjacent_proof_sha256': ROOT/'ADJACENT_SHIFT_REDUCTION.md',
        'direct_source_sha256': ROOT.parent/'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
        'direct_proof_sha256': ROOT.parent/'sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md',
        'floor_moment_source_sha256': ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
        'baseline_helper_source_sha256': ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py',
        'signed_gap_proof_sha256': ROOT.parent/'sep27-qft-boundary/gram_structure/SIGNED_GAPS_REFINEMENT.md'}
    for key, path in targets.items():
        assert digest(path.read_bytes()) == cert[key], (key, str(path))
    return {k: {'path': str(p), 'sha256': cert[k]} for k, p in targets.items()}


def hotspots(cert):
    e = cert['actual_integer_evidence']; ops = e['signed_operations']
    labels = ['routing_and_final']*len(ops)
    def mark(name, start, stop):
        assert 0 <= start <= stop <= len(labels)
        labels[start:stop] = [name]*(stop-start)
    for req in cert['requests']:
        mark('scales', req['scales_operations_start'], req['scales_operations_stop'])
        stop = req['correction_coefficients']['threeV']['signed_operations_start']
        mark('base_coefficients', req['scales_operations_stop'], stop)
        stop2 = req['correction_coefficients']['eightV']['signed_operations_stop']
        mark('correction_coefficients', stop, stop2)
        for p in req['progressions']:
            base = p['single_bit_progression']
            mark('empty_base' if base['empty'] else 'base_outer', base['signed_operations_start'], base['signed_operations_stop'])
            for t in base['table_calls']:
                mark('base_moment_tables', t['signed_operations_start'], t['signed_operations_stop'])
            c = p['correction']
            if c is not None:
                mark('correction_outer', c['signed_operations_start'], c['signed_operations_stop'])
                for t in c['table_calls']:
                    mark('correction_moment_tables', t['signed_operations_start'], t['signed_operations_stop'])
    out = {key: Counter(signed_operations=0, typed_operations=0, adder_digit_replays=0) for key in set(labels)}
    for label, op in zip(labels, ops):
        out[label]['signed_operations'] += 1
        out[label]['typed_operations'] += len(op['typed_operation_indices'])
        out[label]['adder_digit_replays'] += sum(old.raw_digit_count(e['arithmetic_operations'][j]['trace']) for j in op['typed_operation_indices'])
    assert sum(x['adder_digit_replays'] for x in out.values()) == e['arithmetic_stats']['adder_digit_replays']
    return {key: dict(out[key]) for key in sorted(out)}


def main():
    target = ROOT/'ADJACENT_COST_READBACK.json'
    if target.exists():
        raise FileExistsError('Frozen author readback already exists')
    compressed = (ROOT/'ADJACENT_SHIFT_RESULTS.json.gz').read_bytes(); raw = gzip.decompress(compressed)
    assert digest(raw) == RAW_PIN and digest(compressed) == GZIP_PIN
    data = json.loads(raw); summary = json.loads((ROOT/'ADJACENT_SHIFT_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASS'
    assert summary['payload_sha256'] == RAW_PIN and summary['artifact_sha256'] == GZIP_PIN
    assert summary['raw_bytes'] == len(raw) and summary['gzip_bytes'] == len(compressed)
    same(data['source_sha256'], summary['source_sha256'])
    for name, pin in data['source_sha256'].items():
        assert digest((ROOT/name).read_bytes()) == pin
    guardraw = (ROOT/'STARTUP_GUARD.json').read_bytes(); guard = json.loads(guardraw)
    assert digest(guardraw) == data['startup_guard']['sha256']; same(guard, data['startup_guard']['receipt'])
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC' and guard['sync_debt_events'] == []
    assert guard['mode'] == 'TASK_RESEARCH' and guard['boundary'] == 'startup'
    comp = data['comparator_source']; same(comp, summary['comparator_source'])
    template = Path(comp['template_path']).read_bytes(); assert digest(template) == comp['template_sha256']
    def function(text):
        node = next(n for n in ast.parse(text).body if isinstance(n, ast.FunctionDef) and n.name == 'typed_pair_histogram')
        return ast.get_source_segment(text, node)
    body = function(template.decode('utf-8-sig'))
    assert body == function((ROOT/'check_adjacent_shift.py').read_text(encoding='utf-8-sig'))
    assert digest(body.encode()) == comp['copied_function_sha256']
    assert comp['exact_source_text_equal'] is True and comp['historical_checker_imported_or_executed'] is False
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    for key, path in {'lazy_modular': 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular': 'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks': 'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/path).read_bytes()) == native['files_sha256'][key]
    groups = {k: [] for k in ('production', 'typed_pair_comparator', 'positive_replay', 'negative_replay')}
    cases = []; pairs_total = 0; coverage = Counter(); combined_hotspots = {}
    for case in data['cases']:
        cert = case['certificate']; replay = case['verification']['replay_certificate']; brute = case['typed_enumeration']
        assert cert['schema'] == SCHEMA and cert['source_sha256'] == data['source_sha256']['adjacent_shift.py']
        pins = source_pins(cert); assert old.semantic(cert) == old.semantic(replay)
        same(case['inputs'], {key: cert['requests'][0]['inputs'][key] for key in ('g', 'ell', 'k', 'R')})
        assert [r['inputs']['r'] for r in cert['requests']] == list(range(case['inputs']['R']))
        for c, category, field in ((cert, 'production', 'production_cost'), (replay, 'positive_replay', 'positive_replay_cost')):
            inspect(c, native); groups[category].append(c['actual_integer_evidence'])
            same(old.cost_record(c['actual_integer_evidence']), case[field])
        e = brute['actual_integer_evidence']; old.inspect_evidence(e, native)
        groups['typed_pair_comparator'].append(e); same(old.cost_record(e), case['typed_enumeration_cost'])
        values, pairs = old.inspect_pairs(brute, case['inputs']); pairs_total += pairs
        same(values, case['values']); same(values, [r['value'] for r in cert['requests']])
        assert case['all_residues_equal'] is True and case['verification']['verified'] is True
        assert case['verification']['requests_replayed'] == case['inputs']['R']
        same(case['verification']['replay_arithmetic_stats'], replay['actual_integer_evidence']['arithmetic_stats'])
        hs = hotspots(cert)
        for key, counts in hs.items():
            combined_hotspots.setdefault(key, Counter()).update(counts)
        counts = Counter()
        for req in cert['requests']:
            counts['requests'] += 1; tables = 0
            for p in req['progressions']:
                counts['orientations'] += 1; counts['empty_orientations'] += int(p['empty'])
                tables += len(p['single_bit_progression']['table_calls'])
                if p['correction'] is not None:
                    counts['corrections'] += 1; tables += len(p['correction']['table_calls'])
            assert tables <= 8; counts['top_level_tables'] += tables
        coverage.update(counts)
        cases.append({'inputs': case['inputs'], 'values': values, 'typed_pairs_read': pairs,
            'production_digits': case['production_cost']['arithmetic_stats']['adder_digit_replays'],
            'typed_comparator_digits': case['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays'],
            'positive_replay_digits': case['positive_replay_cost']['arithmetic_stats']['adder_digit_replays'],
            'structural_counts': dict(counts), 'production_hotspots': hs})
    assert len(cases) == 6 and pairs_total == 1152 and coverage['requests'] == 37
    assert coverage['top_level_tables'] == data['coverage']['top_level_table_calls'] == 268
    same(data['coverage'], summary['coverage'])
    assert all(c['inputs']['k'] < c['inputs']['g']-1 for c in cases)
    boundary = data['production_boundary_rejection']
    assert boundary['rejected'] is True and boundary['reuse_completed_by_original_grid'] is True
    assert boundary['state_and_paid_evidence_unchanged'] is True
    same(boundary['before'], boundary['after']); inspect_partial(boundary['before'], data['cases'][0]['certificate'], native)
    assert boundary['additional_native_calls'] == boundary['additional_typed_operations'] == 0
    assert boundary['native_subinterval']['start'] == boundary['native_subinterval']['stop']
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations'] == 0
        assert row['call_interval']['start'] == row['call_interval']['stop']
    assert len(data['input_rejections']) == 12
    negatives = []; kinds = Counter()
    for row in data['negative_checks']:
        assert row['rejected'] is True
        original = data['cases'][row['source_case_index']]['certificate']
        attempted = old.decode_keys(row['attempted_certificate_typed_key_encoding'])
        assert row['attempted_certificate_typed_key_encoding'] != old.encode_keys(original)
        captures = row['actual_replay_certificates']; kinds[row['kind']] += 1
        if row['name'].endswith('_early'):
            assert not captures and row['call_interval']['start'] == row['call_interval']['stop']
            if row['name'] == 'bool_input_early': assert type(attempted['requests'][0]['inputs']['g']) is bool
            if row['name'] == 'nonstring_key_early': assert 0 in attempted['requests'][0]
        else:
            assert len(captures) == 1; capture = captures[0]
            if row['name'] == 'valid_prefix_then_invalid_nonadjacent':
                inspect_partial(capture, original, native)
            else:
                assert old.semantic(capture) == old.semantic(original); inspect(capture, native)
            groups['negative_replay'].append(capture['actual_integer_evidence'])
        negatives.append({'name': row['name'], 'kind': row['kind'], 'error': row['error'],
            'receipts': len(captures), 'digits': sum(c['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'] for c in captures)})
    assert len(negatives) == 14 and len(groups['negative_replay']) == 10
    same(dict(kinds), summary['negative_kinds'])
    costs = {key: old.costs(rows) for key, rows in groups.items()}
    same(costs, data['cost_categories']); same(costs, summary['cost_categories'])
    frontier = 0; native_by = Counter()
    for row in data['call_intervals']:
        assert row['start'] == frontier and row['stop'] >= frontier
        native_by[row['category']] += row['stop']-row['start']; frontier = row['stop']
    assert frontier == len(data['actual_core_calls']) == summary['actual_core_call_count'] == 1
    same(dict(native_by), data['native_calls_by_category']); same(dict(native_by), summary['native_calls_by_category'])
    same(data['call_intervals'], summary['call_intervals'])
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for rows in groups.values() for e in rows) == 1
    call = data['actual_core_calls'][0]
    assert call['states'] == 12 and call['depth'] == 1 and call['entrypoint'] == 'recurrent_mass_power'
    assert data['new_typed_pair_comparator_executions'] == 6 and data['historical_science_reexecuted'] is False
    log = (ROOT/'run.log').read_bytes()
    lines = [json.loads(line) for line in log.decode('utf-8-sig').splitlines() if line.strip().startswith('{')]
    assert len([line for line in lines if line.get('stage') == 'CASE_COMPLETE']) == 6
    same(lines[-1], summary)
    result = {'status': 'PASS_FULL_AUTHOR_SAVED_EVIDENCE_READBACK', 'scientific_execution_performed': False,
        'reader_sha256': digest(Path(__file__).read_bytes()), 'pure_io_helper_sha256': HELPER_PIN,
        'source_sha256': data['source_sha256'], 'proof_and_helper_pins': pins, 'comparator_source': comp,
        'payload_sha256': RAW_PIN, 'artifact_sha256': GZIP_PIN, 'raw_bytes': len(raw), 'gzip_bytes': len(compressed),
        'summary_sha256': digest((ROOT/'ADJACENT_SHIFT_SUMMARY.json').read_bytes()),
        'log_sha256': digest(log), 'guard_sha256': digest(guardraw), 'case_rows': cases, 'cost_categories': costs,
        'all_disjoint_current_streams_read': sum(len(rows) for rows in groups.values()),
        'current_total_adder_digits': sum(c['sum']['adder_digit_replays'] for c in costs.values()),
        'typed_pair_records_read': pairs_total, 'structural_counts': dict(coverage),
        'production_hotspots': {key: dict(value) for key, value in sorted(combined_hotspots.items())},
        'negative_checks': negatives, 'negative_kinds': dict(kinds), 'input_rejections': 12,
        'boundary_before_after_equal': True, 'boundary_cost_counted_once_inside_first_production': True,
        'native_source': native, 'actual_core_calls': data['actual_core_calls'], 'native_calls_by_category': dict(native_by),
        'elapsed_seconds_before_serialization': data['elapsed_seconds_before_serialization'],
        'production_below_typed_comparator_cases': sum(c['production_digits'] < c['typed_comparator_digits'] for c in cases),
        'failure_artifact_present': (ROOT/'ADJACENT_SHIFT_FAILED_EXECUTION.json.gz').exists(),
        'scope': 'Saved outer base/correction expressions and links, signed-to-typed outputs, actual native cells, 1152 pair updates, complete/partial replay and disjoint cost accounting. No scientific recomputation.',
        'admission': 'AUTHOR_SHARED_CONTEXT_READBACK_NOT_FORMAL_ADMISSION'}
    with target.open('x', encoding='utf-8') as handle:
        handle.write(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'reader_sha256': result['reader_sha256'],
        'record_sha256': digest(target.read_bytes()), 'streams': result['all_disjoint_current_streams_read'],
        'digits': result['current_total_adder_digits'], 'production_hotspots': result['production_hotspots']}))


if __name__ == '__main__':
    main()
