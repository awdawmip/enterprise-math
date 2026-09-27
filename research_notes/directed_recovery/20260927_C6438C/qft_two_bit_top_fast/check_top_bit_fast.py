"""Declared point/setup optimization checker; no run until source review."""
from copy import deepcopy
from pathlib import Path
import gzip,hashlib,json,time,traceback
from top_bit_fast import (TopBitFastObserver,verify_top_bit_fast_certificate,semantic_certificate,
    BASE_ROOT,BASE_PIN,OPT_PROOF_PIN,DIRECT,DIRECT_PIN,PROOF_PIN,REVIEW_PIN,sha)
from stage45.brc_loop_recheck import CALLS
ROOT=Path(__file__).resolve().parent
SOURCE_PIN='8c73aa1ad2f195b9d8f440112dac7b08cacbc1e544e65850a754dc38f2fa48e8'
SOURCE_NAMES=('top_bit_fast.py','check_top_bit_fast.py','DESIGN.md','POINT_AND_SETUP_REUSE.md')
CASES=((2,0,1,3),(3,1,2,3),(3,1,2,5),(4,2,3,6),(4,2,3,9),(3,1,2,11))
MIXED_CACHE_REQUESTS=((1,0),(0,0),(1,1),(2,0))
HISTORY_GZIP_PIN='ba39feafb35e6d902c1ba1de8c7e64aba581eca7d02e429064c389f6d79e9dc0'
HISTORY_RAW_PIN='4f6fae5355d3a809b765af17c6be7b2ac709cf63ec2e6fbd4e5b81a35cf79dc9'
HISTORY_GUARD_PIN='fd9b5bf7a1b9680a23e3f4ea2ac0f0dce5d3ce362936635044c9324c3aa99f1b'
HISTORY_SOURCE={'top_bit_general.py':BASE_PIN,
    'check_top_bit_general.py':'2b9b04fa1670af5c857eac4ba0810fe6a3c9e45d14f62a6f4371d1bd7ebefc9c',
    'DESIGN.md':'228c00ba4a2a29dc645e2d126b586183d7e6539a40396adf7719db4cdabc0ad3'}
TARGETS=(ROOT/'TOP_BIT_FAST_RESULTS.json.gz',ROOT/'TOP_BIT_FAST_SUMMARY.json',ROOT/'TOP_BIT_FAST_FAILED_EXECUTION.json.gz')
LIVE={'stage':'IMPORTED_NOT_STARTED','output':None,'guard':None,'observer':None,
    'replay_capture':[],'tamper_attempts':[],'current_tamper':None,'input_attempts':[],
    'current_input':None,'call_intervals':[],'history':None}

def typed_keys(item):
    if type(item) is dict:
        return {'object_entries': [{'key_type': type(key).__name__, 'key': key,
                                   'value': typed_keys(value)} for key, value in item.items()]}
    if type(item) in (tuple, list):
        return [typed_keys(x) for x in item]
    return item

def interval(category, label, first):
    record = {'category': category, 'label': label, 'start': first, 'stop': len(CALLS)}
    LIVE['call_intervals'].append(record)
    return record

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
        observer = TopBitFastObserver()
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

def load_history():
    compressed=(BASE_ROOT/'TOP_BIT_GENERAL_RESULTS.json.gz').read_bytes()
    raw=gzip.decompress(compressed)
    assert hashlib.sha256(compressed).hexdigest()==HISTORY_GZIP_PIN
    assert hashlib.sha256(raw).hexdigest()==HISTORY_RAW_PIN
    data=json.loads(raw)
    assert data['status']=='PASS' and data['source_sha256']==HISTORY_SOURCE
    for name,pin in HISTORY_SOURCE.items():
        assert sha(BASE_ROOT/name)==pin
    assert sha(BASE_ROOT/'STARTUP_GUARD.json')==HISTORY_GUARD_PIN==data['startup_guard']['sha256']
    assert json.loads((BASE_ROOT/'STARTUP_GUARD.json').read_bytes())==data['startup_guard']['receipt']
    assert len(data['cases'])==6
    pairs=0
    for expected,case in zip(CASES,data['cases']):
        assert [case['inputs'][k] for k in ('g','ell','k','R')]==list(expected)
        cert=case['certificate']
        assert semantic_certificate(cert)==semantic_certificate(case['verification']['replay_certificate'])
        assert case['verification']['verified'] and case['all_residues_equal']
        assert cert['source_sha256']==BASE_PIN
        assert case['values']==[r['value'] for r in cert['requests']]
        assert len(case['values'])==expected[3]
        for path,key in ((DIRECT/'direct_signed_gap.py','direct_source_sha256'),
            (BASE_ROOT/'TOP_BIT_GENERAL_MODULUS.md','proof_sha256'),
            (BASE_ROOT/'guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md','proof_review_sha256'),
            (DIRECT.parent/'DIFFERENCE_AUTOCORRELATION.md','direct_proof_sha256'),
            (ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py','floor_moment_source_sha256'),
            (ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py','baseline_helper_source_sha256')):
            assert sha(path)==cert[key]
        native=cert['actual_integer_evidence']['native_source']
        for name,path in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
            'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
            'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
            assert sha(ROOT.parent/path)==native['files_sha256'][name]
        pairs+=len(case['typed_enumeration']['pair_observations'])
    assert pairs==720
    receipt={'payload_sha256':HISTORY_RAW_PIN,'artifact_sha256':HISTORY_GZIP_PIN,
        'source_sha256':HISTORY_SOURCE,'raw_bytes':len(raw),'gzip_bytes':len(compressed),
        'whole_payload_read_and_hash_checked':True,'historical_pair_records':pairs,
        'historical_pair_comparator_reexecuted':False,'historical_production_reexecuted':False,
        'guard_sha256':HISTORY_GUARD_PIN}
    LIVE['history']=receipt
    return data,receipt


def segments(certificate):
    return [s for q in certificate['requests'] for o in q['orientations'] for s in o['segments']]


def selected_segment(certificate,route):
    return next(s for s in segments(certificate) if s['route']==route)


def negative_checks(certificates):
    changes=(
        ('setup_scale',1,lambda c:c['setups'][0]['V'].__setitem__('value',999)),
        ('setup_input',1,lambda c:c['setups'][0]['inputs'].__setitem__('g',99)),
        ('setup_index',1,lambda c:c['requests'][1].__setitem__('setup_index',99)),
        ('setup_hit',1,lambda c:c['requests'][1].__setitem__('setup_cache_hit',False)),
        ('setup_complete',1,lambda c:c['setups'][0].__setitem__('complete',False)),
        ('coefficient_value',1,lambda c:c['setups'][0]['coefficients']['low']['coefficients']['n'].__setitem__('value',999)),
        ('coefficient_reference',3,lambda c:selected_segment(c,'FLOOR_MOMENTS')['coefficient_reference'].__setitem__('piece','INVALID')),
        ('point_parity',0,lambda c:selected_segment(c,'SINGLE_DISPLACEMENT')['parity'].__setitem__('remainder',999)),
        ('point_alpha',0,lambda c:selected_segment(c,'SINGLE_DISPLACEMENT').__setitem__('alpha',99)),
        ('point_result',0,lambda c:selected_segment(c,'SINGLE_DISPLACEMENT')['result'].__setitem__('value',999)),
        ('table_output',1,lambda c:selected_segment(c,'FLOOR_MOMENTS')['table_calls'][0]['outputs'].__setitem__('0,3',999)),
        ('half_modulus_orientation',3,lambda c:c['requests'][3]['orientations'].pop()),
        ('raw_exponent',0,lambda c:c['requests'][0].__setitem__('raw_denominator_exponent',999)),
        ('valid_prefix_then_invalid_non_top',1,lambda c:c['requests'][1]['inputs'].__setitem__('g',4)),
        ('source_early',0,lambda c:c.__setitem__('source_sha256','0'*64)),
        ('schema_early',0,lambda c:c.__setitem__('schema','UNRELATED')),
        ('bool_input_early',0,lambda c:c['requests'][0]['inputs'].__setitem__('g',True)),
        ('nonstring_key_early',0,lambda c:c['requests'][0].__setitem__(0,0)))
    attempts=[]
    LIVE['tamper_attempts']=attempts
    for name,index,change in changes:
        attempted=deepcopy(certificates[index])
        change(attempted)
        assert attempted!=certificates[index]
        encoded=typed_keys(attempted)
        capture=[]
        LIVE.update(replay_capture=capture,current_tamper={'name':name,'source_case_index':index,'typed_key_encoding':encoded})
        first=len(CALLS)
        try:
            verify_top_bit_fast_certificate(attempted,replay_capture=capture)
        except ValueError as error:
            if name.endswith('_early'):
                assert not capture and len(CALLS)==first
                kind='EARLY_ZERO_WORK_REJECTION'
            else:
                assert len(capture)==1 and capture[0]['actual_integer_evidence']['arithmetic_operations']
                if name=='valid_prefix_then_invalid_non_top':
                    retained=capture[0]
                    assert retained['complete_certificate'] is False and retained['inflight_request'] is None
                    assert len(retained['requests'])==1 and retained['requests'][0]==certificates[index]['requests'][0]
                    assert len(retained['setups'])==1 and retained['setups'][0]['complete'] is True
                    assert len(retained['actual_integer_evidence']['signed_operations'])==retained['requests'][0]['signed_operations_stop']
                    kind='PAID_VALID_PREFIX_THEN_INPUT_REJECTION'
                else:
                    assert semantic_certificate(capture[0])==semantic_certificate(certificates[index])
                    kind='COMPLETE_PAID_REPLAY_THEN_MISMATCH'
            attempts.append({'name':name,'source_case_index':index,'kind':kind,'rejected':True,'error':str(error),
                'attempted_certificate_typed_key_encoding':encoded,'actual_replay_certificates':capture,
                'call_interval':interval('negative_replay',name,first)})
        else:
            raise AssertionError('forged fast certificate accepted: '+name)
    LIVE['current_tamper']=None
    return attempts


def coverage_checks(certificates):
    requests=[r for c in certificates for r in c['requests']]
    assert len(requests)==37
    for cert in certificates:
        assert len(cert['setups'])==1 and cert['setups'][0]['complete'] is True
        assert cert['requests'][0]['setup_cache_hit'] is False
        assert all(r['setup_cache_hit'] is True for r in cert['requests'][1:])
        assert all(r['setup_index']==0 for r in cert['requests'])
        for record in cert['setups'][0]['coefficients'].values():
            assert record['complete'] is True
    rows=[s for c in certificates for s in segments(c)]
    for req in requests:
        assert req['raw_denominator_exponent']==2*req['inputs']['g']
        assert req['top_level_table_calls']<=8 and len(req['orientations'])==2
        if req['inputs']['r']==0:
            assert [o['head']['value'] for o in req['orientations']]==[0,req['inputs']['R']]
    for s in rows:
        if s['route']=='EMPTY':
            assert s['n']==s['value']==0 and s['table_calls']==[]
        elif s['route']=='SINGLE_DISPLACEMENT':
            assert s['n']==1 and s['table_calls']==[]
            assert s['parity']['remainder'] in (0,1)
            assert s['alpha']==(-3 if s['piece']=='low' else 1)
            assert 'coefficient_reference' not in s
        else:
            assert s['route']=='FLOOR_MOMENTS' and s['n']>=2 and len(s['table_calls'])==2
            assert s['exact_third']['denominator']==3 and s['exact_third']['remainder']==0
            assert s['coefficient_reference']['piece']==s['piece']
    assert {s['route'] for s in rows}=={'EMPTY','SINGLE_DISPLACEMENT','FLOOR_MOMENTS'}
    assert {s['piece'] for s in rows if s['route']=='SINGLE_DISPLACEMENT'}=={'low','high'}
    assert {s['parity']['remainder'] for s in rows if s['route']=='SINGLE_DISPLACEMENT'}=={0,1}
    assert any(s['compressed_displacement']['remainder']>0 for s in rows if s['route']=='SINGLE_DISPLACEMENT')
    assert any(s['coefficient_reference']['cache_hit'] for s in rows if s['route']=='FLOOR_MOMENTS')
    assert any(not c['setups'][0]['coefficients'] for c in certificates)
    assert any(r['value']<0 for r in requests)
    half=certificates[3]['requests'][3]['orientations']
    assert half[0]['head']['value']==half[1]['head']['value']==3
    return {'requests':37,'segments':len(rows),
        'route_counts':{route:sum(s['route']==route for s in rows) for route in sorted({s['route'] for s in rows})},
        'top_level_table_calls':sum(r['top_level_table_calls'] for r in requests),
        'setup_misses':6,'setup_hits':31,
        'coefficient_constructions':sum(len(c['setups'][0]['coefficients']) for c in certificates),
        'singleton_both_pieces_parities_nonzero_remainders':True,'empty_and_moment_routes':True,
        'unused_coefficients_not_built':True,'half_modulus_orientations_retained':True}


def main():
    started=time.perf_counter()
    LIVE['stage']='CHECK_STARTUP_GUARD'
    guard=json.loads((ROOT/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['mode']=='TASK_RESEARCH' and guard['boundary']=='startup'
    LIVE['guard']={'sha256':sha(ROOT/'STARTUP_GUARD.json'),'receipt':guard}
    sources={name:sha(ROOT/name) for name in SOURCE_NAMES}
    assert sources['top_bit_fast.py']==SOURCE_PIN and sources['POINT_AND_SETUP_REUSE.md']==OPT_PROOF_PIN
    LIVE['stage']='READ_COMPLETE_HISTORY'
    history,history_receipt=load_history()
    output={'status':'RUNNING','source_sha256':sources,'startup_guard':LIVE['guard'],
        'historical_evidence_reuse':history_receipt,'cases':[]}
    LIVE['output']=output
    certificates=[]
    for index,(g,ell,k,R) in enumerate(CASES):
        LIVE.update(stage='PRODUCTION',current_tuple=(g,ell,k,R))
        first=len(CALLS)
        observer=TopBitFastObserver()
        LIVE['observer']=observer
        boundary=None
        for residue in range(R):
            observer.two_negative(g,ell,k,R,residue)
            if index==0 and residue==0:
                boundary=production_boundary_rejection(observer)
                output['production_boundary_rejection']=boundary
        if boundary is not None:
            boundary['reuse_completed_by_original_grid']=True
        cert=observer.export_certificate()
        production_interval=interval('production',repr((g,ell,k,R)),first)
        values=[r['value'] for r in cert['requests']]
        assert values==history['cases'][index]['values']
        LIVE['stage']='POSITIVE_REPLAY'
        first=len(CALLS)
        LIVE['replay_capture']=[]
        verification=verify_top_bit_fast_certificate(json.loads(json.dumps(cert)),replay_capture=LIVE['replay_capture'])
        assert len(LIVE['replay_capture'])==1
        assert semantic_certificate(cert)==semantic_certificate(verification['replay_certificate'])
        replay_interval=interval('positive_replay',repr((g,ell,k,R)),first)
        output['cases'].append({'inputs':{'g':g,'ell':ell,'k':k,'R':R},'values':values,
            'all_residues_equal_saved_typed_comparator':True,'certificate':cert,'verification':verification,
            'production_cost':cost(cert['actual_integer_evidence']),
            'positive_replay_cost':cost(verification['replay_certificate']['actual_integer_evidence']),
            'historical_production_cost':history['cases'][index]['production_cost'],
            'historical_typed_comparator_cost':history['cases'][index]['typed_enumeration_cost'],
            'call_intervals':[production_interval,replay_interval]})
        certificates.append(cert)
        print(json.dumps({'stage':'CASE_COMPLETE','tuple':(g,ell,k,R),'values':values}),flush=True)
    output['coverage']=coverage_checks(certificates)
    LIVE['stage']='MIXED_SETUP_CACHE_CONTROL'
    first=len(CALLS)
    mixed=TopBitFastObserver()
    LIVE['observer']=mixed
    for index,residue in MIXED_CACHE_REQUESTS:
        g,ell,k,R=CASES[index]
        row=mixed.two_negative(g,ell,k,R,residue)
        assert row['value']==history['cases'][index]['values'][residue]
    mixed_cert=mixed.export_certificate()
    assert len(mixed_cert['setups'])==2
    assert [r['setup_index'] for r in mixed_cert['requests']]==[0,1,0,0]
    assert [r['setup_cache_hit'] for r in mixed_cert['requests']]==[False,False,True,True]
    mixed_interval=interval('cache_control','mixed_g_and_R',first)
    first=len(CALLS)
    LIVE['replay_capture']=[]
    mixed_verification=verify_top_bit_fast_certificate(mixed_cert,replay_capture=LIVE['replay_capture'])
    assert len(LIVE['replay_capture'])==1
    output['mixed_cache_control']={'requests_from_historical_grid':MIXED_CACHE_REQUESTS,'certificate':mixed_cert,
        'verification':mixed_verification,'call_intervals':[mixed_interval,interval('cache_control_replay','mixed_g_and_R',first)],
        'scope':'Four additional accepted queries test switching setup keys and R; separately charged'}
    LIVE['stage']='INPUT_REJECTIONS'
    output['input_rejections']=input_rejections()
    LIVE['stage']='TAMPER_REJECTIONS'
    output['negative_checks']=negative_checks(certificates)
    costs={
        'production':aggregate_cost(c['actual_integer_evidence'] for c in certificates),
        'positive_replay':aggregate_cost(c['verification']['replay_certificate']['actual_integer_evidence'] for c in output['cases']),
        'cache_control':aggregate_cost([mixed_cert['actual_integer_evidence']]),
        'cache_control_replay':aggregate_cost([mixed_verification['replay_certificate']['actual_integer_evidence']]),
        'negative_replay':aggregate_cost(c['actual_integer_evidence'] for row in output['negative_checks'] for c in row['actual_replay_certificates'])}
    frontier=0
    native_by={}
    for row in LIVE['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        native_by[row['category']]=native_by.get(row['category'],0)+row['stop']-row['start']
        frontier=row['stop']
    assert frontier==len(CALLS)
    assert sources=={name:sha(ROOT/name) for name in SOURCE_NAMES}
    assert sha(ROOT/'STARTUP_GUARD.json')==LIVE['guard']['sha256']
    assert sha(BASE_ROOT/'TOP_BIT_GENERAL_RESULTS.json.gz')==HISTORY_GZIP_PIN
    for name,pin in HISTORY_SOURCE.items():
        assert sha(BASE_ROOT/name)==pin
    output.update(status='PASS',cost_categories=costs,native_calls_by_category=native_by,
        call_intervals=deepcopy(LIVE['call_intervals']),actual_core_calls=deepcopy(CALLS),
        actual_core_call_count=len(CALLS),elapsed_seconds_before_serialization=time.perf_counter()-started,
        new_typed_pair_comparator_executions=0,historical_science_reexecuted=False)
    LIVE['stage']='SERIALIZE_SUCCESS'
    raw=json.dumps(output,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[0].open('xb') as handle:
        handle.write(gzip.compress(raw,compresslevel=6,mtime=0))
    summary={'status':'PASS','source_sha256':sources,'cases':6,'residue_equalities':37,
        'additional_cache_control_accepted_queries':4,'historical_typed_pair_observations':720,
        'new_typed_pair_comparator_executions':0,'input_rejections':12,'negative_checks':18,
        'negative_kinds':{kind:sum(r['kind']==kind for r in output['negative_checks']) for kind in sorted({r['kind'] for r in output['negative_checks']})},
        'coverage':output['coverage'],'cost_categories':costs,'native_calls_by_category':native_by,
        'actual_core_call_count':len(CALLS),'call_intervals':LIVE['call_intervals'],
        'per_case':[{'inputs':c['inputs'],'values':c['values'],'production':c['production_cost'],
            'historical_production':c['historical_production_cost'],'historical_comparator':c['historical_typed_comparator_cost']} for c in output['cases']],
        'raw_bytes':len(raw),'gzip_bytes':TARGETS[0].stat().st_size,'payload_sha256':hashlib.sha256(raw).hexdigest(),
        'artifact_sha256':sha(TARGETS[0]),'elapsed_seconds_before_serialization':output['elapsed_seconds_before_serialization'],
        'comparison_is_timing_benchmark':False,'full_shor_sampling_performed':False}
    with TARGETS[1].open('x',encoding='utf-8') as handle:
        handle.write(json.dumps(summary,indent=2)+'\n')
    LIVE['stage']='COMPLETE'
    print(json.dumps(summary),flush=True)


def preserve_failure(error):
    fields={'current_observer':lambda:None if LIVE['observer'] is None else LIVE['observer'].incomplete_snapshot(),
        'completed_output':lambda:deepcopy(LIVE['output']),'replay_capture':lambda:deepcopy(LIVE['replay_capture']),
        'completed_tamper_attempts':lambda:deepcopy(LIVE['tamper_attempts']),'current_tamper':lambda:deepcopy(LIVE['current_tamper']),
        'completed_input_attempts':lambda:deepcopy(LIVE['input_attempts']),'current_input':lambda:deepcopy(LIVE['current_input'])}
    failure={'status':'FAILED_EXECUTION','stage':LIVE['stage'],'error_type':type(error).__name__,'error':str(error),
        'traceback':traceback.format_exc(),'startup_guard':LIVE['guard'],'history':LIVE['history'],
        'current_tuple':LIVE.get('current_tuple'),'source_sha256':{},'snapshot_errors':{},
        'actual_core_calls':deepcopy(CALLS),'call_intervals':deepcopy(LIVE['call_intervals'])}
    for name in SOURCE_NAMES:
        try: failure['source_sha256'][name]=sha(ROOT/name)
        except BaseException as exc: failure['snapshot_errors']['source:'+name]=repr(exc)
    for name,collect in fields.items():
        try: failure[name]=collect()
        except BaseException as exc: failure['snapshot_errors'][name]=repr(exc)
    raw=json.dumps(failure,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[2].open('xb') as handle:
        handle.write(gzip.compress(raw,compresslevel=6,mtime=0))
    print(json.dumps({'status':'FAILED_EXECUTION','path':str(TARGETS[2]),'payload_sha256':hashlib.sha256(raw).hexdigest()}),flush=True)


if __name__=='__main__':
    if any(path.exists() for path in TARGETS):
        raise ValueError('existing success or failure evidence; refusing another run')
    try: main()
    except BaseException as error:
        preserve_failure(error)
        raise
