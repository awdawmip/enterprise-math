"""Single declared shortcut fixture; only compile until coordinator execution."""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import json
import time
import traceback
from shortcut_two_bit import (ShortcutTwoBitObserver, verify_shortcut_certificate,
    semantic_certificate, PROOF, PROOF_PIN, DIRECT, DIRECT_PIN, ALIGNED, ALIGNED_PIN,
    SHORTCUT_PROOF, SHORTCUT_PIN, SHORTCUT_REVIEW, REVIEW_PIN, sha)
from stage45.brc_loop_recheck import CALLS
ROOT = Path(__file__).resolve().parent
CASES = ((2,0,1,1),(3,0,1,3),(3,1,2,2),(3,1,2,4),(4,1,3,6),(4,2,3,20))
TARGETS = (ROOT/'SHORTCUT_RESULTS.json.gz',ROOT/'SHORTCUT_SUMMARY.json',ROOT/'SHORTCUT_FAILED_EXECUTION.json.gz')
HISTORY_RAW_PIN = '61aee1882148519bd9738bacf6f107a39532aa98de6c128854edb98df334aba9'
HISTORY_GZIP_PIN = 'f6bf350f188d4252c60c897778561e3c4957d65774a25a12334b35261f0b7bd3'
HISTORY_SOURCE = {'aligned_two_bit.py':'a6fd6cf5bfe10829c1918c50a952de22e5e2bc6cd538011f37a3bffdff5acdb2',
    'check_aligned_two_bit.py':'6777057a9468b673c7d58a657467c65ae1c37bd353fd55b9eb86a743efdaa969',
    'DESIGN.md':'90605ff87a2a9f37576c57bb9f5363407c29778f87fef0c17aa6621713908876'}
HISTORY_GUARD_PIN = '1c9e45ed619a7480402d0719e283b06a52ca78a889bca6bd74c14ca8fbc4297f'
LIVE = {'stage':'IMPORTED_NOT_STARTED','output':None,'guard':None,'observer':None,
        'replay_capture':[],'tamper_attempts':[],'current_tamper':None,
        'input_attempts':[],'current_input':None,'call_intervals':[],'history':None}

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


def input_rejections():
    cases = ((True, 0, 1, 1, 0, 1), (1, 0, 1, 1, 0, 1), (3, -1, 2, 2, 0, 1),
             (3, 1, 1, 2, 0, 1), (3, 1, 3, 2, 0, 1), (3, 1, 2, 0, 0, 1),
             (3, 1, 2, 2, -1, 1), (3, 1, 2, 2, 2, 1), (3, 1, 2, 2, 0, 2),
             (3, False, 2, 2, 0, 1))
    records = []
    LIVE['input_attempts'] = records
    for args in cases:
        observer = ShortcutTwoBitObserver()
        LIVE.update(observer=observer, current_input={'args': args, 'kind': 'ordinary_pre_rejection'})
        first = len(CALLS)
        try:
            observer.two_negative(*args[:5], stride=args[5])
        except ValueError as error:
            assert not observer.runner.arithmetic.operations and not observer.requests
            assert len(CALLS) == first
            records.append({'args': args, 'kind': 'ordinary_pre_rejection', 'rejected': True,
                            'error': str(error), 'actual_typed_operations': 0,
                            'call_interval': interval('input_pre_rejection', repr(args), first)})
        else:
            raise AssertionError('invalid ordinary input accepted')
    for args in ((3, 1, 2, 3, 0), (4, 2, 3, 6, 1)):
        observer = ShortcutTwoBitObserver()
        LIVE.update(observer=observer, current_input={'args': args, 'kind': 'paid_unaligned_rejection'})
        first = len(CALLS)
        try:
            observer.two_negative(*args)
        except ValueError as error:
            receipt = observer.incomplete_snapshot()
            assert receipt['inflight_request']['alignment']['remainder'] > 0
            assert receipt['actual_integer_evidence']['arithmetic_operations'] and not observer.requests
            records.append({'args': args, 'kind': 'paid_unaligned_rejection', 'rejected': True,
                'error': str(error), 'incomplete_receipt': receipt,
                'call_interval': interval('paid_input_rejection', repr(args), first)})
            # A paid failure is terminal for this observer. The retained raw
            # trace is evidence, not an implicit resumable request prefix.
            reuse_args = (3, 1, 2, 2, 0)
            LIVE['current_input'] = {'args': reuse_args, 'kind': 'incomplete_observer_reuse'}
            reuse_first = len(CALLS)
            try:
                observer.two_negative(*reuse_args)
            except ValueError as reuse_error:
                assert observer.incomplete_snapshot() == receipt
                assert len(CALLS) == reuse_first
                records[-1]['reuse_rejection'] = {
                    'args': reuse_args, 'rejected': True, 'error': str(reuse_error),
                    'prior_inflight_and_all_evidence_unchanged': True,
                    'additional_typed_operations': 0,
                    'call_interval': interval('input_reuse_rejection', repr(args), reuse_first)}
            else:
                raise AssertionError('observer with paid incomplete work was reused')
        else:
            raise AssertionError('unaligned input accepted')
    LIVE['current_input'] = None
    return records


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


def load_history():
    """Read complete immutable historical bytes; no historical executor import."""
    compressed = (ALIGNED/'TWO_BIT_ALIGNED_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert hashlib.sha256(compressed).hexdigest() == HISTORY_GZIP_PIN
    assert hashlib.sha256(raw).hexdigest() == HISTORY_RAW_PIN
    history = json.loads(raw)
    assert history['status'] == 'PASS' and history['source_sha256'] == HISTORY_SOURCE
    for name, pin in HISTORY_SOURCE.items():
        assert sha(ALIGNED/name) == pin
    assert sha(ALIGNED/'STARTUP_GUARD.json') == HISTORY_GUARD_PIN == history['startup_guard']['sha256']
    assert json.loads((ALIGNED/'STARTUP_GUARD.json').read_bytes()) == history['startup_guard']['receipt']
    assert len(history['cases']) == len(CASES)
    total_pairs = 0
    for expected, case in zip(CASES, history['cases']):
        assert [case['inputs'][key] for key in ('g','ell','k','R')] == list(expected)
        cert, replay = case['certificate'], case['verification']['replay_certificate']
        assert semantic_certificate(cert) == semantic_certificate(replay)
        assert case['verification']['verified'] is True and case['all_residues_equal'] is True
        assert case['values'] == [r['value'] for r in cert['requests']]
        assert len(case['values']) == expected[3]
        assert cert['source_sha256'] == ALIGNED_PIN
        for path, key in ((DIRECT/'direct_signed_gap.py','direct_source_sha256'),
                          (PROOF,'two_bit_proof_sha256'),
                          (DIRECT.parent/'DIFFERENCE_AUTOCORRELATION.md','direct_proof_sha256'),
                          (ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py','floor_moment_source_sha256'),
                          (ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py','baseline_helper_source_sha256')):
            assert sha(path) == cert[key]
        native = cert['actual_integer_evidence']['native_source']
        for name, path in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
                           'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
                           'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
            assert sha(ROOT.parent/path) == native['files_sha256'][name]
        total_pairs += len(case['typed_enumeration']['pair_observations'])
    assert total_pairs == 720
    record = {'payload_sha256':HISTORY_RAW_PIN,'artifact_sha256':HISTORY_GZIP_PIN,
        'source_sha256':HISTORY_SOURCE,'raw_bytes':len(raw),'gzip_bytes':len(compressed),
        'whole_payload_read_and_hash_checked':True,'historical_pair_records':total_pairs,
        'historical_production_reexecuted':False,'historical_pair_comparator_reexecuted':False,
        'historical_fresh_replay_reexecuted':False,'guard_sha256':HISTORY_GUARD_PIN}
    LIVE['history'] = record
    return history, record


def negative_checks(certificates):
    changes = (
        ('zero_divisibility_reason',0,lambda c:c['requests'][0]['zero_test'].__setitem__('remainder',1)),
        ('zero_route_output',0,lambda c:c['requests'][0].__setitem__('value',1)),
        ('drop_half_modulus_orientation',4,lambda c:c['requests'][3]['orientations'].pop()),
        ('omitted_shifted_coefficient',1,lambda c:c['requests'][0]['orientations'][0]['branches'][0]['shifted'].__setitem__('observed_coefficient',1)),
        ('affine_canonical_length',5,lambda c:c['requests'][1]['orientations'][0]['branches'][0]['original'].__setitem__('n',999)),
        ('affine_typed_min_selection',4,lambda c:c['requests'][0]['orientations'][0]['branches'][0]['original']['q_selection']['selected'].__setitem__('value',999)),
        ('affine_exact_half',5,lambda c:c['requests'][1]['orientations'][0]['branches'][0]['original']['Tn']['exact_half'].__setitem__('value',999)),
        ('shifted_zero_tail',5,lambda c:c['requests'][13]['orientations'][0]['branches'][0]['shifted_zero_tail'].__setitem__('removed_zero_terms',0)),
        ('original_branch_sign',4,lambda c:c['requests'][1]['orientations'][0]['branches'][0].__setitem__('sign',-1)),
        ('fallback_table_offset',1,lambda c:c['requests'][0]['orientations'][0]['branches'][0]['original']['table_calls'][0]['inputs'].__setitem__('b',999)),
        ('signed_output',1,lambda c:c['requests'][0].__setitem__('value',999)),
        ('unaligned_input_paid_partial',2,lambda c:c['requests'][0]['inputs'].__setitem__('R',3)),
        ('source_early',0,lambda c:c.__setitem__('source_sha256','0'*64)),
        ('schema_early',0,lambda c:c.__setitem__('schema','UNRELATED')),
        ('bool_input_early',0,lambda c:c['requests'][0]['inputs'].__setitem__('g',True)),
        ('nonstring_key_early',0,lambda c:c['requests'][0].__setitem__(0,0)))
    attempts=[]
    LIVE['tamper_attempts']=attempts
    for name,index,change in changes:
        attempted=deepcopy(certificates[index])
        change(attempted)
        encoded=typed_keys(attempted)
        capture=[]
        LIVE.update(replay_capture=capture,current_tamper={'name':name,'source_case_index':index,'typed_key_encoding':encoded})
        first=len(CALLS)
        try:
            verify_shortcut_certificate(attempted,replay_capture=capture)
        except ValueError as error:
            if name.endswith('_early'):
                assert not capture and len(CALLS)==first
            else:
                assert len(capture)==1 and capture[0]['actual_integer_evidence']['arithmetic_operations']
                if name=='unaligned_input_paid_partial':
                    assert capture[0]['complete_certificate'] is False
                    assert capture[0]['inflight_request']['alignment']['remainder']>0
                    assert 'zero_test' not in capture[0]['inflight_request']
                else:
                    assert semantic_certificate(capture[0])==semantic_certificate(certificates[index])
            attempts.append({'name':name,'source_case_index':index,'rejected':True,'error':str(error),
                'attempted_certificate_typed_key_encoding':encoded,'actual_replay_certificates':capture,
                'call_interval':interval('negative_replay',name,first)})
        else:
            raise AssertionError('forged shortcut certificate accepted: '+name)
    LIVE['current_tamper']=None
    return attempts


def coverage_checks(certificates):
    requests=[r for c in certificates for r in c['requests']]
    assert len(requests)==36
    expected_routes={'RESIDUE_HISTOGRAM_CANCELLATION','HIGHEST_BIT_AFFINE','DIRECT_MOMENT_FALLBACK'}
    assert {r['route'] for r in requests}==expected_routes
    route_counts={key:sum(r['route']==key for r in requests) for key in sorted(expected_routes)}
    branches=[]; progressions=[]; omitted=[]
    for req in requests:
        assert req['alignment']['remainder']==0 and req['alignment_checked_before_zero_test'] is True
        assert req['raw_denominator_exponent']==2*req['inputs']['g']
        if req['route']=='RESIDUE_HISTOGRAM_CANCELLATION':
            assert req['zero_test']['remainder']==0 and req['value']==0
            assert req['orientations_evaluated'] is False and req['orientations']==[]
            assert req['single_progression_calls']==req['top_level_table_calls']==0
            continue
        assert req['zero_test']['remainder']>0 and req['orientations_evaluated'] is True
        assert len(req['orientations'])==2
        assert req['single_progression_calls']<=8 and req['top_level_table_calls']<=16
        if req['route']=='HIGHEST_BIT_AFFINE':
            assert req['coefficients'] is None and req['top_level_table_calls']==0
        for o in req['orientations']:
            assert o['multiplicity']==1
            for b in o['branches']:
                branches.append(b)
                progressions.append(b['original'])
                shift=b['shifted']
                if shift['execution']=='OMITTED_ZERO_COEFFICIENT':
                    omitted.append(shift)
                    assert b['shifted_weight']==shift['observed_coefficient']==0
                    assert shift['arithmetic_executed'] is False and shift['progression_called'] is False
                    assert 'value' not in shift and 'n' not in shift and 'signed_operations_start' not in shift
                else:
                    assert shift['execution']=='EVALUATED' and b['shifted_weight']>0
                    progressions.append(shift)
                assert b['original']['n']==b['expected_n']['value']
        if req['inputs']['r']==0:
            assert req['orientations'][0]['head']['value']==0
            assert req['orientations'][1]['head']['value']==req['inputs']['R']
    assert omitted and any(r['value']<0 for r in requests)
    assert any(o['empty'] for r in requests for o in r['orientations'])
    assert any(b.get('shifted_zero_tail',{}).get('removed_zero_terms')==1 for b in branches)
    assert any(b['original']['empty'] is False and b['shifted'].get('empty') is True for b in branches)
    affine=[p for p in progressions if p['strategy']=='HIGHEST_BIT_AFFINE']
    assert any(p['empty'] for p in affine)
    assert any(p.get('q')==0 for p in affine if not p['empty'])
    assert any(p.get('q')==p['n'] for p in affine if not p['empty'])
    assert any(p.get('junction_minus_head',{}).get('value')==0 for p in affine)
    assert {p['strategy'] for p in progressions}=={'HIGHEST_BIT_AFFINE','FROZEN_DIRECT_MOMENTS'}
    half=certificates[4]['requests'][3]['orientations']
    assert half[0]['head']['value']==half[1]['head']['value'] and len(half)==2
    return {'requests':36,'route_counts':route_counts,'private_progressions':len(progressions),
        'omitted_shifted_progressions':len(omitted),'affine_progressions':len(affine),
        'moment_progressions':sum(p['strategy']=='FROZEN_DIRECT_MOMENTS' for p in progressions),
        'top_level_tables':sum(len(p['table_calls']) for p in progressions),
        'negative_output_seen':True,'empty_orientation_and_affine_progression_seen':True,
        'affine_q_zero_full_and_junction_seen':True,'nonzero_shifted_M_tail_seen':True,
        'half_modulus_multiplicity_preserved':True}


def main():
    started=time.perf_counter()
    LIVE['stage']='CHECK_STARTUP_GUARD'
    guard_path=ROOT/'STARTUP_GUARD.json'
    guard=json.loads(guard_path.read_bytes())
    assert guard.get('activity_allowed') is True and guard.get('persistence_allowed') is True
    assert guard.get('activity_id')=='RA-CAAAC604CB513AEA8BBC1DFC'
    assert guard.get('boundary')=='startup' and guard.get('mode')=='TASK_RESEARCH'
    assert guard.get('sync_debt_events')==[]
    LIVE['guard']={'sha256':sha(guard_path),'receipt':guard}
    names=('shortcut_two_bit.py','check_shortcut_two_bit.py','DESIGN.md')
    sources={name:sha(ROOT/name) for name in names}
    assert sha(SHORTCUT_PROOF)==SHORTCUT_PIN and sha(SHORTCUT_REVIEW)==REVIEW_PIN
    LIVE['stage']='READ_FULL_IMMUTABLE_HISTORY'
    historical,history_record=load_history()
    output={'status':'RUNNING','source_sha256':sources,'startup_guard':LIVE['guard'],
        'history':history_record,'shortcut_proof_sha256':SHORTCUT_PIN,'shortcut_review_sha256':REVIEW_PIN,
        'cases':[],'scope':'Structural scalar shortcuts only, same aligned admission; no historical science rerun'}
    LIVE['output']=output
    certificates=[]
    for index,(g,ell,k,R) in enumerate(CASES):
        LIVE.update(stage='SHORTCUT_PRODUCTION',current_tuple=(g,ell,k,R),replay_capture=[])
        observer=ShortcutTwoBitObserver()
        LIVE['observer']=observer
        first=len(CALLS)
        records=[observer.two_negative(g,ell,k,R,r) for r in range(R)]
        cert=observer.export_certificate()
        production_interval=interval('production',repr((g,ell,k,R)),first)
        values=[r['value'] for r in records]
        old=historical['cases'][index]
        assert values==old['values']
        LIVE['stage']='POSITIVE_FRESH_REPLAY'
        first=len(CALLS)
        verification=verify_shortcut_certificate(json.loads(json.dumps(cert)),replay_capture=LIVE['replay_capture'])
        replay_interval=interval('positive_replay',repr((g,ell,k,R)),first)
        output['cases'].append({'inputs':{'g':g,'ell':ell,'k':k,'R':R},'values':values,
            'all_historical_residues_equal':True,'certificate':cert,'verification':verification,
            'production_cost':cost(cert['actual_integer_evidence']),
            'positive_replay_cost':cost(verification['replay_certificate']['actual_integer_evidence']),
            'history_reference':{'case_index':index,'certificate_pointer':f'cases/{index}/certificate',
                'values':old['values'],'historical_production_cost':old['production_cost'],
                'historical_comparator_cost':old['typed_enumeration_cost'],
                'historical_pairs_read':len(old['typed_enumeration']['pair_observations']),
                'historical_pair_comparator_reexecuted':False},
            'call_intervals':[production_interval,replay_interval]})
        certificates.append(cert)
        print(json.dumps({'stage':'CASE_COMPLETE','tuple':(g,ell,k,R),'values':values,
            'production_digits':cert['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']}),flush=True)
    output['coverage']=coverage_checks(certificates)
    LIVE['stage']='INPUT_REJECTIONS'
    output['input_rejections']=input_rejections()
    LIVE['stage']='CERTIFICATE_TAMPER_REJECTIONS'
    output['negative_checks']=negative_checks(certificates)
    assert sources=={name:sha(ROOT/name) for name in names}
    assert sha(guard_path)==LIVE['guard']['sha256']
    assert sha(SHORTCUT_PROOF)==SHORTCUT_PIN and sha(SHORTCUT_REVIEW)==REVIEW_PIN
    costs={'production':aggregate_cost(c['actual_integer_evidence'] for c in certificates),
        'positive_replay':aggregate_cost(c['verification']['replay_certificate']['actual_integer_evidence'] for c in output['cases']),
        'paid_input_rejection':aggregate_cost(r['incomplete_receipt']['actual_integer_evidence'] for r in output['input_rejections'] if 'incomplete_receipt' in r),
        'negative_replay':aggregate_cost(c['actual_integer_evidence'] for r in output['negative_checks'] for c in r['actual_replay_certificates'])}
    native_by={}; frontier=0
    for row in LIVE['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        native_by[row['category']]=native_by.get(row['category'],0)+row['stop']-row['start']
        frontier=row['stop']
    assert frontier==len(CALLS) and sum(native_by.values())==len(CALLS)
    output.update(status='PASS',cost_categories=costs,native_calls_by_category=native_by,
        call_intervals=deepcopy(LIVE['call_intervals']),actual_core_calls=deepcopy(CALLS),
        actual_core_call_count=len(CALLS),elapsed_seconds_before_serialization=time.perf_counter()-started,
        historical_digit_costs_not_in_new_cost_categories=True)
    LIVE['stage']='SERIALIZE_SUCCESS'
    raw=json.dumps(output,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[0].open('xb') as stream:
        stream.write(gzip.compress(raw,compresslevel=6,mtime=0))
    summary={'status':'PASS','source_sha256':sources,'cases':6,'residue_equalities':36,
        'historical_pairs_read':720,'new_pair_comparator_executions':0,'history':history_record,
        'input_rejections':len(output['input_rejections']),
        'incomplete_observer_reuse_rejections':sum('reuse_rejection' in r for r in output['input_rejections']),
        'negative_checks':len(output['negative_checks']),'coverage':output['coverage'],
        'cost_categories':costs,'native_calls_by_category':native_by,'actual_core_call_count':len(CALLS),
        'call_intervals':LIVE['call_intervals'],'values':[c['values'] for c in output['cases']],
        'per_case':[{'inputs':c['inputs'],'new_production':c['production_cost'],
                    'new_positive_replay':c['positive_replay_cost'],
                    'historical_production':c['history_reference']['historical_production_cost'],
                    'historical_comparator':c['history_reference']['historical_comparator_cost']} for c in output['cases']],
        'raw_bytes':len(raw),'gzip_bytes':TARGETS[0].stat().st_size,
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'artifact_sha256':sha(TARGETS[0]),
        'elapsed_seconds_before_serialization':output['elapsed_seconds_before_serialization'],
        'comparison_is_timing_benchmark':False,'full_gram_integration_performed':False,
        'order_discovery_performed':False,'host_cost_scope':'arithmetic wiring/bit-length counters; serialization/index bookkeeping excluded'}
    with TARGETS[1].open('x',encoding='utf-8') as stream:
        stream.write(json.dumps(summary,indent=2)+'\n')
    LIVE['stage']='COMPLETE'
    print(json.dumps(summary),flush=True)


def preserve_failure(error):
    observer=LIVE.get('observer')
    failure={'status':'FAILED_EXECUTION','stage':LIVE['stage'],'error_type':type(error).__name__,
        'error':str(error),'traceback':traceback.format_exc(),
        'source_sha256':{name:sha(ROOT/name) for name in ('shortcut_two_bit.py','check_shortcut_two_bit.py','DESIGN.md')},
        'startup_guard':LIVE['guard'],'history':LIVE['history'],'current_tuple':LIVE.get('current_tuple'),
        'completed_output':LIVE['output'],'current_observer':None if observer is None else observer.incomplete_snapshot(),
        'current_replay_capture':LIVE['replay_capture'],'completed_tamper_attempts':LIVE['tamper_attempts'],
        'current_tamper':LIVE['current_tamper'],'completed_input_attempts':LIVE['input_attempts'],
        'current_input':LIVE['current_input'],'call_intervals':LIVE['call_intervals'],'actual_core_calls':CALLS,
        'scope':'Incomplete retained typed work; no mathematical admission'}
    raw=json.dumps(failure,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[2].open('xb') as stream:
        stream.write(gzip.compress(raw,compresslevel=6,mtime=0))
    print(json.dumps({'status':'FAILED_EXECUTION','stage':LIVE['stage'],'path':str(TARGETS[2]),
        'payload_sha256':hashlib.sha256(raw).hexdigest()}),flush=True)


if __name__=='__main__':
    if any(path.exists() for path in TARGETS):
        raise ValueError('existing success or failure evidence; refusing another run')
    try:
        main()
    except BaseException as error:
        preserve_failure(error)
        raise

