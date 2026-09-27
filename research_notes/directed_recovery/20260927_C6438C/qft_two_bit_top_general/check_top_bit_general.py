"""Predeclared highest-bit arbitrary-R checker; CODE ONLY until authorized.

The exact typed pair comparator is copied below from the pinned aligned
checker. No scientific import or execution was used to prepare this file.
"""
from copy import deepcopy
from pathlib import Path
import ast
import gzip
import hashlib
import json
import time
import traceback

from top_bit_general import (TopBitGeneralObserver, verify_top_bit_certificate,
    semantic_certificate, typed_two_power, DIRECT, DIRECT_PIN, PROOF_PIN, REVIEW_PIN,
    FLOOR_PIN, BASELINE_PIN, sha)
from direct_signed_gap import TypedFloorMoments
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
SOURCE_PIN = '33a46d5f3dacf61e83cedd75cb3424f2375485b3b58984429d5c9fc76b8c96d0'
ALIGNED_CHECKER = ROOT.parent/'sep27-qft-two-bit-aligned/check_aligned_two_bit.py'
ALIGNED_CHECKER_PIN = '6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969'
CASES = ((2,0,1,3),(3,1,2,3),(3,1,2,5),(4,2,3,6),(4,2,3,9),(3,1,2,11))
TARGETS = (ROOT/'TOP_BIT_GENERAL_RESULTS.json.gz', ROOT/'TOP_BIT_GENERAL_SUMMARY.json',
           ROOT/'TOP_BIT_GENERAL_FAILED_EXECUTION.json.gz')
SOURCE_NAMES = ('top_bit_general.py','check_top_bit_general.py','DESIGN.md')
LIVE = {'stage':'IMPORTED_NOT_STARTED','output':None,'guard':None,'observer':None,
        'brute_runner':None,'brute_digits':[],'brute_pairs':[],'brute_values':None,
        'replay_capture':[],'tamper_attempts':[],'current_tamper':None,
        'input_attempts':[],'current_input':None,'call_intervals':[]}


def typed_keys(item):
    if type(item) is dict:
        return {'object_entries': [{'key_type': type(key).__name__, 'key': key,
                                   'value': typed_keys(value)} for key, value in item.items()]}
    if type(item) in (tuple, list):
        return [typed_keys(x) for x in item]
    return item


def unfinished_runner(runner):
    return None if runner is None else deepcopy({
        'arithmetic_operations': runner.arithmetic.operations, 'arithmetic_stats': runner.arithmetic.stats,
        'signed_operations': runner.signed_operations, 'moment_nodes': runner.nodes,
        'window_weight_queries': runner.weight_queries, 'stats': runner.stats})


def interval(category, label, first):
    record = {'category': category, 'label': label, 'start': first, 'stop': len(CALLS)}
    LIVE['call_intervals'].append(record)
    return record


def typed_pair_histogram(g, ell, k, R):
    """One ordered-pair pass per tuple, all buckets together; no host reference."""
    runner = TypedFloorMoments()
    LIVE['brute_runner'] = runner
    length = typed_two_power(runner, g)
    low_scale = typed_two_power(runner, ell)
    high_scale = typed_two_power(runner, k)
    digit_rows, digits = [], []
    LIVE['brute_digits'] = digit_rows
    for x in range(length):
        first = len(runner.signed_operations)
        low_quotient, low_remainder = runner.floor_div(x, low_scale)
        _, low_bit = runner.floor_div(low_quotient, 2)
        high_quotient, high_remainder = runner.floor_div(x, high_scale)
        _, high_bit = runner.floor_div(high_quotient, 2)
        bit_sum = runner.add(low_bit, high_bit)
        _, parity = runner.floor_div(bit_sum, 2)
        assert low_bit in (0, 1) and high_bit in (0, 1) and parity in (0, 1)
        digits.append(parity)
        digit_rows.append({'label': x, 'low_quotient': low_quotient, 'low_remainder': low_remainder,
            'low_bit': low_bit, 'high_quotient': high_quotient, 'high_remainder': high_remainder,
            'high_bit': high_bit, 'bit_sum': bit_sum, 'parity': parity,
            'signed_operations_start': first, 'signed_operations_stop': len(runner.signed_operations)})
    buckets = [0 for _ in range(R)]
    pairs = []
    LIVE['brute_pairs'], LIVE['brute_values'] = pairs, buckets
    for x in range(length):
        for y in range(length):
            first = len(runner.signed_operations)
            difference = runner.sub(y, x)
            quotient, residue = runner.floor_div(difference, R)
            sign = 1 if digits[x] == digits[y] else -1
            before = buckets[residue]
            after = runner.add(before, sign)
            buckets[residue] = after
            pairs.append({'x': x, 'y': y, 'difference': difference, 'quotient': quotient,
                'residue': residue, 'sign': sign, 'bucket_before': before, 'bucket_after': after,
                'signed_operations_start': first, 'signed_operations_stop': len(runner.signed_operations)})
    return buckets, {'length': length, 'low_scale': low_scale, 'high_scale': high_scale,
                    'digit_observations': digit_rows, 'pair_observations': pairs,
                    'all_residue_buckets_from_one_pair_pass': True,
                    'actual_integer_evidence': runner.evidence()}


def cost(evidence):
    return {'arithmetic_stats': deepcopy(evidence['arithmetic_stats']),
            'typed_operations': len(evidence['arithmetic_operations']),
            'signed_operations': len(evidence['signed_operations']),
            'moment_nodes': len(evidence['moment_nodes']),
            'window_queries': len(evidence['window_weight_queries']),
            'moment_stats': deepcopy(evidence['stats'])}


def aggregate_cost(evidences):
    rows = [cost(e) for e in evidences]
    if not rows:
        return {'receipts': 0, 'sum': {}, 'max': {}}
    additive = ('adder_digit_replays', 'typed_operations', 'host_bit_wiring_operations',
                'host_bit_length_calls_in_arithmetic')
    total = {key: sum(row['arithmetic_stats'][key] for row in rows) for key in additive}
    for key in ('typed_operations', 'signed_operations', 'moment_nodes', 'window_queries'):
        # typed_operations is independently counted from the complete trace.
        value = sum(row[key] for row in rows)
        if key == 'typed_operations':
            assert total[key] == value
        total[key] = value
    for key in ('moment_requests', 'cache_hits'):
        total[key] = sum(row['moment_stats'][key] for row in rows)
    maxima = {key: max(row['moment_stats'][key] for row in rows)
              for key in ('max_recursion_depth', 'max_observed_integer_bits')}
    return {'receipts': len(rows), 'sum': total, 'max': maxima,
            'native_calls_counted_from_disjoint_process_intervals': True}


def verify_comparator_source():
    require_template = ALIGNED_CHECKER.read_bytes()
    assert hashlib.sha256(require_template).hexdigest() == ALIGNED_CHECKER_PIN
    old = require_template.decode('utf-8')
    new = Path(__file__).read_text(encoding='utf-8')
    def function(text, name):
        return ast.get_source_segment(text, next(node for node in ast.parse(text).body
            if isinstance(node, ast.FunctionDef) and node.name == name))
    old_function = function(old, 'typed_pair_histogram')
    assert old_function == function(new, 'typed_pair_histogram')
    return {'template_path':str(ALIGNED_CHECKER), 'template_sha256':ALIGNED_CHECKER_PIN,
        'function':'typed_pair_histogram', 'copied_function_sha256':
            hashlib.sha256(old_function.encode('utf-8')).hexdigest(),
        'exact_source_text_equal':True, 'historical_checker_imported_or_executed':False,
        'scope':'Comparator algorithm reused on six new tuples; no old 720-pair experiment rerun',
        'helper_source_sha256':{'direct':DIRECT_PIN,'floor':FLOOR_PIN,'baseline':BASELINE_PIN}}


def production_boundary_rejection(observer):
    """Invalid input changes no state; following ordinary grid requests reuse it.

    This is a zero-work subinterval inside the first production interval,
    never an additional global CALLS interval or an extra successful query.
    """
    attempted = (4,0,1,3,0,1)  # Valid bit order, but k is not g-1.
    before = observer.incomplete_snapshot()
    first = len(CALLS)
    try:
        observer.two_negative(*attempted[:5],stride=attempted[5])
    except ValueError as error:
        after = observer.incomplete_snapshot()
        assert after == before and len(CALLS) == first
        assert after['inflight_request'] is None and len(after['requests']) == 1
        return {'args':attempted,'rejected':True,'error':str(error),
            'before':before,'after':after,'state_and_paid_evidence_unchanged':True,
            'additional_native_calls':0,'additional_typed_operations':0,
            'native_subinterval':{'start':first,'stop':len(CALLS)},
            'cost_containment':'Snapshots overlap the first production receipt; do not charge again',
            'reuse_completed_by_original_grid':False}
    raise AssertionError('non-top request accepted after a valid prefix')


def input_rejections():
    cases = ((True,0,1,3,0,1),(1,0,1,3,0,1),(3,-1,2,3,0,1),
        (3,1,1,3,0,1),(3,1,3,3,0,1),(3,1,2,0,0,1),
        (3,1,2,3,-1,1),(3,1,2,3,3,1),(3,1,2,3,0,2),
        (3,False,2,3,0,1),(4,0,1,3,0,1),(3,1,2,True,0,1))
    records = []
    LIVE['input_attempts'] = records
    for args in cases:
        observer = TopBitGeneralObserver()
        LIVE.update(observer=observer,current_input={'args':args,'kind':'ordinary_pre_rejection'})
        first = len(CALLS)
        try:
            observer.two_negative(*args[:5],stride=args[5])
        except ValueError as error:
            assert not observer.runner.arithmetic.operations and not observer.requests
            assert observer.inflight is None and len(CALLS) == first
            records.append({'args':args,'rejected':True,'error':str(error),
                'actual_typed_operations':0,'call_interval':interval('input_pre_rejection',repr(args),first)})
        else:
            raise AssertionError('invalid top-bit input accepted')
    LIVE['current_input'] = None
    return records


def negative_checks(certificates):
    # Chosen structural entries exist for the predeclared tuples. Sentinel
    # edits affect evidence, not scientific input, except the one prefix test.
    changes = (
        ('segment_split',1,lambda c:c['requests'][0]['orientations'][0]['low_length'].__setitem__('n',999)),
        ('segment_high_head',1,lambda c:c['requests'][0]['orientations'][0]['high_head'].__setitem__('value',999)),
        ('polynomial_coefficient',1,lambda c:c['requests'][0]['coefficients']['low']['coefficients']['delta3'].__setitem__('value',999)),
        ('shifted_offset',1,lambda c:c['requests'][0]['orientations'][0]['segments'][0]['shifted_offset'].__setitem__('value',999)),
        ('exact_third',1,lambda c:c['requests'][0]['orientations'][0]['segments'][0]['exact_third'].__setitem__('denominator',2)),
        ('drop_half_modulus_orientation',3,lambda c:c['requests'][3]['orientations'].pop()),
        ('moment_table_output',1,lambda c:c['requests'][0]['orientations'][0]['segments'][0]['table_calls'][0]['outputs'].__setitem__('0,3',999)),
        ('raw_exponent',0,lambda c:c['requests'][0].__setitem__('raw_denominator_exponent',999)),
        ('signed_output',0,lambda c:c['requests'][0].__setitem__('value',999)),
        ('valid_prefix_then_invalid_non_top',1,lambda c:c['requests'][1]['inputs'].__setitem__('g',4)),
        ('source_early',0,lambda c:c.__setitem__('source_sha256','0'*64)),
        ('schema_early',0,lambda c:c.__setitem__('schema','UNRELATED')),
        ('bool_input_early',0,lambda c:c['requests'][0]['inputs'].__setitem__('g',True)),
        ('nonstring_key_early',0,lambda c:c['requests'][0].__setitem__(0,0)))
    attempts = []
    LIVE['tamper_attempts'] = attempts
    for name,index,change in changes:
        attempted = deepcopy(certificates[index])
        change(attempted)
        encoded = typed_keys(attempted)
        capture = []
        LIVE.update(replay_capture=capture,current_tamper={'name':name,
            'source_case_index':index,'typed_key_encoding':encoded})
        first = len(CALLS)
        try:
            verify_top_bit_certificate(attempted,replay_capture=capture)
        except ValueError as error:
            if name.endswith('_early'):
                assert not capture and len(CALLS) == first
                kind = 'EARLY_ZERO_WORK_REJECTION'
            else:
                assert len(capture) == 1 and capture[0]['actual_integer_evidence']['arithmetic_operations']
                if name == 'valid_prefix_then_invalid_non_top':
                    retained = capture[0]
                    assert retained['complete_certificate'] is False
                    assert retained['inflight_request'] is None
                    assert len(retained['requests']) == 1
                    assert retained['requests'][0] == certificates[index]['requests'][0]
                    # The invalid second request is rejected before mutation.
                    # This is a failed verification with paid valid prefix,
                    # not a numerical failure or terminal inflight observer.
                    assert len(retained['actual_integer_evidence']['signed_operations']) == retained['requests'][0]['signed_operations_stop']
                    kind = 'PAID_VALID_PREFIX_THEN_INPUT_REJECTION'
                else:
                    assert semantic_certificate(capture[0]) == semantic_certificate(certificates[index])
                    kind = 'COMPLETE_PAID_REPLAY_THEN_MISMATCH'
            attempts.append({'name':name,'source_case_index':index,'kind':kind,
                'rejected':True,'error':str(error),
                'attempted_certificate_typed_key_encoding':encoded,
                'actual_replay_certificates':capture,
                'call_interval':interval('negative_replay',name,first)})
        else:
            raise AssertionError('forged top-bit certificate accepted: '+name)
    LIVE['current_tamper'] = None
    return attempts


def coverage_checks(certificates):
    requests = [r for c in certificates for r in c['requests']]
    assert len(requests) == 37
    segments = []
    for req in requests:
        assert req['modulus_alignment_required'] is False
        assert req['route'] == 'TOP_BIT_TWO_PIECE_FLOOR_MOMENTS'
        assert req['raw_denominator_exponent'] == 2*req['inputs']['g']
        assert req['inputs']['k'] == req['inputs']['g']-1
        assert req['top_level_table_calls'] <= 8
        assert len(req['orientations']) == 2
        assert [o['orientation'] for o in req['orientations']] == ['nonnegative_difference','negative_difference_magnitude']
        if req['inputs']['r'] == 0:
            assert req['orientations'][0]['head']['value'] == 0
            assert req['orientations'][1]['head']['value'] == req['inputs']['R']
        for orientation in req['orientations']:
            assert orientation['multiplicity'] == 1
            if orientation['empty']:
                assert orientation['segments'] == [] and orientation['value'] == 0
                continue
            assert [s['piece'] for s in orientation['segments']] == ['low','high']
            for segment in orientation['segments']:
                segments.append(segment)
                assert len(segment['table_calls']) == (0 if segment['empty'] else 2)
                if segment['empty']:
                    assert segment['n'] == segment['value'] == 0
                else:
                    assert segment['n'] > 0
                    assert segment['displacement_lower_bound'] <= segment['head']['value'] < segment['displacement_exclusive_upper_bound']
                    assert segment['exact_third']['denominator'] == 3 and segment['exact_third']['remainder'] == 0
                    assert all(len(t['outputs']) == 10 for t in segment['table_calls'])
    assert any(r['value'] < 0 for r in requests)
    assert any(o['empty'] for r in requests for o in r['orientations'])
    assert any(s['empty'] for s in segments)
    assert {s['piece'] for s in segments if not s['empty']} == {'low','high'}
    assert any(s['piece']=='high' and s['head']['value']==s['displacement_lower_bound'] for s in segments if not s['empty'])
    # Actual typed comparator digits contain nonzero low remainders; no host
    # modulus/power is needed for coverage. Nonalignment is a fixed input fact,
    # not a route tested numerically by this algorithm.
    half = certificates[3]['requests'][3]['orientations']
    assert half[0]['head']['value'] == half[1]['head']['value'] == 3
    assert any(req['inputs']['R'] > req['L'] for req in requests)
    return {'requests':37,'segments':len(segments),
        'nonempty_segments':sum(not s['empty'] for s in segments),
        'top_level_table_calls':sum(r['top_level_table_calls'] for r in requests),
        'at_most_eight_tables_each':True,'both_polynomial_pieces_and_exact_third_seen':True,
        'negative_output_seen':True,'empty_segments_and_orientations_seen':True,
        'high_piece_exact_boundary_seen':True,'half_modulus_both_orientations_retained':True,
        'R_larger_than_L_seen':True,'alignment_test_or_order_discovery_performed':False}


def main():
    started = time.perf_counter()
    LIVE['stage'] = 'CHECK_STARTUP_GUARD'
    guard_path = ROOT/'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_bytes())
    assert guard.get('activity_allowed') is True and guard.get('persistence_allowed') is True
    assert guard.get('activity_id') == 'RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard.get('boundary') == 'startup' and guard.get('mode') == 'TASK_RESEARCH'
    assert guard.get('sync_debt_events') == []
    LIVE['guard'] = {'sha256':sha(guard_path),'receipt':guard}
    sources = {name:sha(ROOT/name) for name in SOURCE_NAMES}
    assert sources['top_bit_general.py'] == SOURCE_PIN
    assert sha(ROOT/'TOP_BIT_GENERAL_MODULUS.md') == PROOF_PIN
    assert sha(ROOT/'guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md') == REVIEW_PIN
    comparator_source = verify_comparator_source()
    output = {'status':'RUNNING','source_sha256':sources,'startup_guard':LIVE['guard'],
        'proof_sha256':PROOF_PIN,'proof_review_sha256':REVIEW_PIN,
        'comparator_source':comparator_source,'cases':[],
        'scope':'Highest selected bit, arbitrary supplied R; six new tuples and new typed pair comparators'}
    LIVE['output'] = output
    certificates = []
    for index,(g,ell,k,R) in enumerate(CASES):
        LIVE.update(stage='TOP_BIT_GENERAL_PRODUCTION',current_tuple=(g,ell,k,R),
            brute_runner=None,brute_digits=[],brute_pairs=[],brute_values=None,replay_capture=[])
        observer = TopBitGeneralObserver()
        LIVE['observer'] = observer
        first = len(CALLS)
        requests = []
        boundary = None
        for r in range(R):
            requests.append(observer.two_negative(g,ell,k,R,r))
            if index == 0 and r == 0:
                boundary = production_boundary_rejection(observer)
                output['production_boundary_rejection'] = boundary
        if boundary is not None:
            assert len(observer.requests) == R and observer.inflight is None
            boundary['reuse_completed_by_original_grid'] = True
        values = [r['value'] for r in requests]
        certificate = observer.export_certificate()
        production_interval = interval('production',repr((g,ell,k,R)),first)
        LIVE['stage'] = 'ONE_PASS_TYPED_PAIR_COMPARATOR'
        first = len(CALLS)
        expected,brute = typed_pair_histogram(g,ell,k,R)
        brute_interval = interval('typed_pair_comparator',repr((g,ell,k,R)),first)
        assert values == expected
        LIVE['stage'] = 'POSITIVE_FRESH_REPLAY'
        first = len(CALLS)
        verification = verify_top_bit_certificate(json.loads(json.dumps(certificate)),replay_capture=LIVE['replay_capture'])
        replay_interval = interval('positive_replay',repr((g,ell,k,R)),first)
        assert len(LIVE['replay_capture']) == 1
        assert semantic_certificate(certificate) == semantic_certificate(verification['replay_certificate'])
        output['cases'].append({'inputs':{'g':g,'ell':ell,'k':k,'R':R},'values':values,
            'all_residues_equal':True,'certificate':certificate,'typed_enumeration':brute,
            'verification':verification,'production_cost':cost(certificate['actual_integer_evidence']),
            'typed_enumeration_cost':cost(brute['actual_integer_evidence']),
            'positive_replay_cost':cost(verification['replay_certificate']['actual_integer_evidence']),
            'call_intervals':[production_interval,brute_interval,replay_interval]})
        certificates.append(certificate)
        print(json.dumps({'stage':'CASE_COMPLETE','tuple':(g,ell,k,R),'values':values,
            'typed_pairs':len(brute['pair_observations'])}),flush=True)
    output['coverage'] = coverage_checks(certificates)
    assert sum(len(c['typed_enumeration']['pair_observations']) for c in output['cases']) == 720
    assert any(row['low_remainder'] > 0 for c in output['cases'] for row in c['typed_enumeration']['digit_observations'])
    output['coverage']['actual_comparator_nonzero_low_remainder_seen'] = True
    LIVE['stage'] = 'INPUT_REJECTIONS'
    output['input_rejections'] = input_rejections()
    LIVE['stage'] = 'CERTIFICATE_TAMPER_REJECTIONS'
    output['negative_checks'] = negative_checks(certificates)
    assert sources == {name:sha(ROOT/name) for name in SOURCE_NAMES}
    assert sha(guard_path) == LIVE['guard']['sha256']
    assert sha(ROOT/'TOP_BIT_GENERAL_MODULUS.md') == PROOF_PIN
    assert sha(ROOT/'guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md') == REVIEW_PIN
    assert sha(DIRECT/'direct_signed_gap.py') == DIRECT_PIN
    assert verify_comparator_source() == comparator_source
    costs = {
        'production':aggregate_cost(c['actual_integer_evidence'] for c in certificates),
        'typed_pair_comparator':aggregate_cost(c['typed_enumeration']['actual_integer_evidence'] for c in output['cases']),
        'positive_replay':aggregate_cost(c['verification']['replay_certificate']['actual_integer_evidence'] for c in output['cases']),
        'negative_replay':aggregate_cost(c['actual_integer_evidence'] for r in output['negative_checks'] for c in r['actual_replay_certificates'])}
    frontier,native_by = 0,{}
    for row in LIVE['call_intervals']:
        assert row['start'] == frontier and row['stop'] >= frontier
        native_by[row['category']] = native_by.get(row['category'],0)+row['stop']-row['start']
        frontier = row['stop']
    assert frontier == len(CALLS) and sum(native_by.values()) == len(CALLS)
    output.update(status='PASS',cost_categories=costs,native_calls_by_category=native_by,
        call_intervals=deepcopy(LIVE['call_intervals']),actual_core_calls=deepcopy(CALLS),
        actual_core_call_count=len(CALLS),elapsed_seconds_before_serialization=time.perf_counter()-started,
        new_typed_pair_comparator_executions=6,historical_science_reexecuted=False)
    LIVE['stage'] = 'SERIALIZE_SUCCESS'
    raw = json.dumps(output,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[0].open('xb') as handle:
        handle.write(gzip.compress(raw,compresslevel=6,mtime=0))
    summary = {'status':'PASS','source_sha256':sources,'cases':6,'residue_equalities':37,
        'typed_pair_observations':720,'new_typed_pair_comparator_executions':6,
        'historical_science_reexecuted':False,'comparator_source':comparator_source,
        'input_rejections':len(output['input_rejections']),
        'valid_prefix_boundary_rejection_and_reuse':True,'negative_checks':len(output['negative_checks']),
        'negative_kinds':{kind:sum(r['kind']==kind for r in output['negative_checks'])
            for kind in sorted({r['kind'] for r in output['negative_checks']})},
        'coverage':output['coverage'],'cost_categories':costs,'native_calls_by_category':native_by,
        'actual_core_call_count':len(CALLS),'call_intervals':LIVE['call_intervals'],
        'values':[c['values'] for c in output['cases']],
        'per_case':[{'inputs':c['inputs'],'production':c['production_cost'],
            'typed_comparator':c['typed_enumeration_cost'],'positive_replay':c['positive_replay_cost']} for c in output['cases']],
        'raw_bytes':len(raw),'gzip_bytes':TARGETS[0].stat().st_size,
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'artifact_sha256':sha(TARGETS[0]),
        'elapsed_seconds_before_serialization':output['elapsed_seconds_before_serialization'],
        'comparison_is_timing_benchmark':False,'full_gram_integration_performed':False,
        'order_discovery_performed':False,'quantum_phase_propagation_performed':False,
        'host_cost_scope':'arithmetic wiring and bit-length counters; metadata/serialization/index bookkeeping excluded'}
    with TARGETS[1].open('x',encoding='utf-8') as handle:
        handle.write(json.dumps(summary,indent=2)+'\n')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary),flush=True)


def preserve_failure(error):
    # Available in-memory evidence only; no new scientific observer evaluation.
    fields = {
        'current_observer':lambda:None if LIVE['observer'] is None else LIVE['observer'].incomplete_snapshot(),
        'current_comparator_runner':lambda:unfinished_runner(LIVE['brute_runner']),
        'comparator_digit_observations':lambda:deepcopy(LIVE['brute_digits']),
        'comparator_pair_observations':lambda:deepcopy(LIVE['brute_pairs']),
        'comparator_values':lambda:deepcopy(LIVE['brute_values']),
        'completed_output':lambda:deepcopy(LIVE['output']),
        'replay_capture':lambda:deepcopy(LIVE['replay_capture']),
        'completed_tamper_attempts':lambda:deepcopy(LIVE['tamper_attempts']),
        'current_tamper':lambda:deepcopy(LIVE['current_tamper']),
        'completed_input_attempts':lambda:deepcopy(LIVE['input_attempts']),
        'current_input':lambda:deepcopy(LIVE['current_input'])}
    failure = {'status':'FAILED_EXECUTION','stage':LIVE['stage'],'error_type':type(error).__name__,
        'error':str(error),'traceback':traceback.format_exc(),'startup_guard':LIVE['guard'],
        'current_tuple':LIVE.get('current_tuple'),'source_sha256':{},'snapshot_errors':{},
        'actual_core_calls':deepcopy(CALLS),'call_intervals':deepcopy(LIVE['call_intervals']),
        'scope':'Available retained work; constructor/import failure before object return is not reconstructible'}
    for name in SOURCE_NAMES:
        try:
            failure['source_sha256'][name] = sha(ROOT/name)
        except BaseException as exc:
            failure['snapshot_errors']['source:'+name] = repr(exc)
    for name,collect in fields.items():
        try:
            failure[name] = collect()
        except BaseException as exc:
            failure['snapshot_errors'][name] = repr(exc)
    raw = json.dumps(failure,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[2].open('xb') as handle:
        handle.write(gzip.compress(raw,compresslevel=6,mtime=0))
    print(json.dumps({'status':'FAILED_EXECUTION','stage':LIVE['stage'],
        'path':str(TARGETS[2]),'payload_sha256':hashlib.sha256(raw).hexdigest()}),flush=True)


if __name__ == '__main__':
    if any(path.exists() for path in TARGETS):
        raise ValueError('existing success or failure evidence; refusing another run')
    try:
        main()
    except BaseException as error:
        preserve_failure(error)
        raise
