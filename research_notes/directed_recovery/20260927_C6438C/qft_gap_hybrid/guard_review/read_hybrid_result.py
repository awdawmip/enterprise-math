"""Full saved-record inspection only; imports two pinned I/O reviewers.

No observer/native scientific module is imported or executed. Numerical
arithmetic outputs are read from saved records, not recomputed.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'hybrid_gap'
SOURCES = {
    'hybrid_signed_gap.py':'7daf2e04be83ed9a9124c1a2bcc79ae2cc8feb5334c4b675ed19f7a2bc918fb8',
    'check_hybrid_signed_gap.py':'ed54ddc3ffb9735e1610ae363b69cd58d426adb4b9c1d0cc6ba85fcf11de1da7'}
IO_HELPERS = {
    'direct':(ROOT.parent/'sep27-qft-gap-direct/guard_review/read_direct_result.py',
              '4b7e7d1bf7e4b7575d6b202f680acbac62861e16551aa4971ba7b74848571098'),
    'endpoint':(ROOT.parent/'sep27-qft-gap-shortcuts/guard_review/read_endpoint_result.py',
                'e230a560c28cf5416d72a653aa8add0bcd5005a880f1a5f3ab10c74a5ae70b4c')}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load_io(name):
    path, pin = IO_HELPERS[name]
    assert digest(path.read_bytes()) == pin
    spec = importlib.util.spec_from_file_location('saved_io_'+name,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


direct, endpoint = load_io('direct'), load_io('endpoint')
same, canonical = direct.same, direct.canonical


def streams(cert):
    return {'routing':cert['routing_integer_evidence'],
        'endpoint':cert['endpoint_certificate']['actual_integer_evidence'],
        'direct':cert['direct_certificate']['actual_integer_evidence']}


def semantic(cert):
    c=deepcopy(cert)
    for e in streams(c).values():
        n=e['arithmetic_stats']['native_kernel_calls_delta']
        assert type(n) is int and n>=0
        e['arithmetic_stats']['native_kernel_calls_delta']=0
    return canonical(c)


def saved_cost(cert):
    result={}
    for name,e in streams(cert).items():
        result[name]={'arithmetic_stats':e['arithmetic_stats'],
            'signed_operations':len(e['signed_operations']), 'moment_nodes':len(e['moment_nodes']),
            'moment_stats':e['stats'],'window_queries':len(e['window_weight_queries'])}
    result['arithmetic_totals']={k:sum(e['arithmetic_stats'][k] for e in streams(cert).values())
                                 for k in result['routing']['arithmetic_stats']}
    return result


def inspect(cert,native):
    assert cert['schema']=='BRC_STRUCTURAL_HYBRID_SIGNED_GAP_V1'
    assert cert['source_sha256']==SOURCES['hybrid_signed_gap.py']
    es=streams(cert)
    for e in es.values():
        same(e['native_source'],native)
        same([j for op in e['signed_operations'] for j in op['typed_operation_indices']],
             list(range(len(e['arithmetic_operations']))))
        assert len(e['arithmetic_operations'])==e['arithmetic_stats']['typed_operations']
        direct.trace_accounting(e)
    routing=es['routing']
    assert routing['moment_nodes']==[] and routing['window_weight_queries']==[]
    assert routing['stats']['moment_requests']==routing['stats']['cache_hits']==0
    cursor=direct.RecordedCursor(routing)
    seen={'endpoint':0,'direct':0}
    counts={'endpoint':0,'interior_direct':0,'interior_divisible_zero':0}
    for index,req in enumerate(cert['requests']):
        inp=req['inputs']
        assert set(inp)=={'g','k','R','r','stride'} and all(type(v) is int for v in inp.values())
        assert inp['stride']==1 and inp['r']==index
        assert req['raw_denominator_exponent']==2*inp['g'] and req['negative_values_are_valid'] is True
        assert req['routing_operations_start']==cursor.i
        counts[req['branch']]+=1
        if inp['k']==0 or inp['k']==inp['g']-1:
            assert req['branch']==req['nested_kind']=='endpoint'
            assert req['divisibility'] is None and req['zero_proof'] is None
            assert req['endpoint_branch']==req['nested_request']['branch']!='interior_one_window'
        else:
            div=req['divisibility']
            assert div['scale_operations_start']==cursor.i
            U=1
            for _ in range(inp['k']):
                U=cursor.add(U,U)
            same(U,div['U'])
            assert div['scale_operations_stop']==div['division_signed_operation_index']==cursor.i
            same(div['R'],inp['R'])
            q,remainder=cursor.div(U,inp['R'])
            same([q,remainder],[div['quotient'],div['remainder']])
            assert req['endpoint_branch'] is None
            if remainder==0:
                assert req['branch']=='interior_divisible_zero'
                assert req['nested_kind'] is req['nested_request_index'] is req['nested_request'] is None
                proof=req['zero_proof']
                assert proof['identity']=='R divides U: every signed residue histogram is zero'
                assert proof['division_signed_operation_index']==div['division_signed_operation_index']
                assert proof['zero_signed_operation_index']==cursor.i
                zero=cursor.sub(U,U)
                assert type(zero) is int and zero==0
                same([zero,zero],[req['value'],proof['value']])
            else:
                assert remainder>0 and req['branch']=='interior_direct' and req['nested_kind']=='direct'
                assert req['zero_proof'] is None
        assert req['routing_operations_stop']==cursor.i
        kind=req['nested_kind']
        if kind is not None:
            index=req['nested_request_index']
            assert index==seen[kind]
            nested=cert[kind+'_certificate']['requests'][index]
            same(nested,req['nested_request'])
            same(nested['inputs'],inp)
            same(nested['value'],req['value'])
            seen[kind]+=1
    assert cursor.i==len(routing['signed_operations'])
    for name,count in seen.items():
        assert count==len(cert[name+'_certificate']['requests'])
    # Each declared tuple uses one route; these pinned readers verify that scope.
    e_links=endpoint.inspect(cert['endpoint_certificate'])
    d_links=direct.inspect(cert['direct_certificate'])
    return {'branch_counts':counts,'routing_signed_operations':cursor.i,
        'endpoint_links':e_links,'direct_links':d_links,
        'all_three_streams_native_cells_and_costs_checked':True}


def aggregate(certs):
    result={}
    for name in ('routing','endpoint','direct'):
        result[name]=direct.aggregate([{'actual_integer_evidence':streams(c)[name]} for c in certs])
    result['arithmetic_totals']={k:sum(result[n]['arithmetic'][k] for n in ('routing','endpoint','direct'))
                                 for k in result['routing']['arithmetic']}
    return result


def main():
    data,summary=direct.load(DATA,'HYBRID',
        '76efccc284001219b2ecde3523557f66e55e828125e4132a83814f25df80398b',
        '036242b07b480d05937b6a72ffc375dc33eea48283647964ca020b78bdb3f962')
    old,old_summary=direct.load(ROOT.parent/'sep27-qft-gap-direct/direct_gap','DIRECT',direct.RAW_PIN,direct.GZIP_PIN)
    same(data['source_sha256'],SOURCES)
    for name,path in {
        'endpoint_signed_gap.py':ROOT.parent/'sep27-qft-gap-shortcuts/endpoint_gap/endpoint_signed_gap.py',
        'direct_signed_gap.py':ROOT.parent/'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
        'signed_gap.py':ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py',
        'typed_floor_moments.py':ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
        'DESIGN.md':ROOT/'DESIGN.md'}.items():
        assert digest(path.read_bytes())==data['dependency_sha256'][name]
    guard_bytes=(ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guard_bytes)==data['startup_guard']['sha256']
    same(json.loads(guard_bytes),data['startup_guard']['receipt'])
    guard=data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC'
    assert data['history']['whole_payload_read_and_hash_checked'] is True and data['history']['historical_science_reexecuted'] is False
    assert data['history']['payload_sha256']==direct.RAW_PIN and data['history']['artifact_sha256']==direct.GZIP_PIN
    native=streams(data['cases'][0]['certificate'])['routing']['native_source']
    for key,path in {
        'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/path).read_bytes())==native['files_sha256'][key]
    productions,positives,negatives,cases=[],[],[],[]
    for i,(case,prior) in enumerate(zip(data['cases'],old['cases'])):
        same(case['inputs'],prior['inputs']);same(case['values'],prior['values'])
        assert case['all_residues_equal'] is True
        cert,replay=case['certificate'],case['verification']['replay_certificate']
        same(cert['dependency_sha256'],data['dependency_sha256'])
        assert cert['endpoint_certificate']['source_sha256']==data['dependency_sha256']['endpoint_signed_gap.py']
        assert cert['direct_certificate']['source_sha256']==data['dependency_sha256']['direct_signed_gap.py']
        assert semantic(cert)==semantic(replay) and case['verification']['verified'] is True
        assert case['verification']['requests_replayed']==len(cert['requests'])==case['inputs']['R']
        same(case['values'],[r['value'] for r in cert['requests']])
        links=inspect(cert,native);same(links,inspect(replay,native))
        same(links['branch_counts'],case['branch_counts'])
        same(saved_cost(cert),case['production_cost']);same(saved_cost(replay),case['positive_replay_cost'])
        same({name:e['arithmetic_stats'] for name,e in streams(replay).items()},case['verification']['replay_arithmetic_stats'])
        assert saved_cost(cert)['arithmetic_totals']['native_kernel_calls_delta']==case['production_native_core_calls_delta']
        assert saved_cost(replay)['arithmetic_totals']['native_kernel_calls_delta']==case['replay_native_core_calls_delta']
        ref=case['history_reference']
        assert ref['case_index']==i and ref['certificate_pointer']==f'cases/{i}/certificate'
        same(ref['values'],prior['values']);same(ref['recorded_pure_direct_stats'],prior['new_production_arithmetic_stats'])
        cases.append({'inputs':case['inputs'],'values':case['values'],'record_links':links,
            'production_cost':saved_cost(cert),'historical_pure_direct_stats':ref['recorded_pure_direct_stats']})
        productions.append(cert);positives.append(replay)
    assert len(cases)==len(data['cases'])==len(old['cases'])==summary['cases']==9
    assert sum(len(c['values']) for c in cases)==summary['residue_equalities']==31
    counts={k:sum(c['record_links']['branch_counts'][k] for c in cases) for k in data['branch_counts']}
    same(counts,{'endpoint':20,'interior_direct':10,'interior_divisible_zero':1});same(counts,data['branch_counts']);same(counts,summary['branch_counts'])
    expected_names=['wrong_schema','wrong_source','wrong_dependency','boolean_input','false_direct_branch',
        'wrong_zero_quotient','wrong_zero_remainder','wrong_zero_U','missing_zero_proof','boolean_zero_output',
        'wrong_zero_subtraction','wrong_routing_division','wrong_endpoint_nested_value','wrong_direct_nested_value','wrong_nested_provenance']
    same([r['name'] for r in data['negative_checks']],expected_names)
    negative_rows=[]
    for i,row in enumerate(data['negative_checks']):
        original=productions[row['case_index']]
        assert row['rejected'] is True and semantic(row['attempted_certificate'])!=semantic(original)
        captures=row['actual_replay_certificates']
        if i>=4:
            assert len(captures)==1 and row['error']=='hybrid certificate does not strictly replay'
            assert semantic(captures[0])==semantic(original)
            inspect(captures[0],native);negatives.extend(captures)
        else:
            assert captures==[]
        same([saved_cost(c) for c in captures],row['replay_costs'])
        assert row['native_core_calls_delta']==sum(saved_cost(c)['arithmetic_totals']['native_kernel_calls_delta'] for c in captures)
        negative_rows.append({'name':row['name'],'error':row['error'],'complete_paid_replays':len(captures)})
    assert len(data['negative_checks'])==summary['negative_checks']==15
    assert len(negatives)==summary['paid_negative_replays']==11
    assert len(data['input_rejections'])==summary['input_rejections']==8
    same(data['input_rejections'],old['input_rejections'])
    resources={'production':aggregate(productions),'positive_replay':aggregate(positives),'negative_replay':aggregate(negatives)}
    for name in resources:
        same(resources[name]['arithmetic_totals'],summary[name+'_totals'])
    total={k:sum(r['arithmetic_totals'][k] for r in resources.values()) for k in resources['production']['arithmetic_totals']}
    assert total['adder_digit_replays']==84535
    assert resources['production']['routing']['arithmetic']['adder_digit_replays']==193
    assert total['native_kernel_calls_delta']==data['actual_core_call_count']==summary['actual_core_call_count']==len(data['actual_core_calls'])==1
    assert data['actual_core_calls'][0]['states']==12
    output={'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW','admission':'SHARED_CONTEXT_AUTHOR_REVIEW_NOT_FORMAL_ADMISSION',
        'scope':'whole payload and saved fresh replay equality; all three runner recording links and native-cell/cost accounting; no scientific execution',
        'reader_sha256':digest(Path(__file__).read_bytes()),'io_helper_sha256':{k:v[1] for k,v in IO_HELPERS.items()},
        'source_sha256':SOURCES,'dependency_sha256':data['dependency_sha256'],
        'payload_sha256':summary['payload_sha256'],'raw_bytes':summary['raw_bytes'],
        'artifact_sha256':summary['artifact_sha256'],'gzip_bytes':summary['gzip_bytes'],
        'history_payload_sha256':old_summary['payload_sha256'],'guard_sha256':digest(guard_bytes),
        'native_source':native,'cases':cases,'branch_counts':counts,'input_rejections':data['input_rejections'],
        'negative_checks':negative_rows,'resources':resources,'current_run_total_arithmetic':total,
        'actual_core_calls':data['actual_core_calls'],
        'unexpected_failure_artifact_present':(DATA/'HYBRID_FAILED_EXECUTION.json.gz').exists(),
        'scientific_arithmetic_recomputed':False,'comparison_is_timing_benchmark':False,
        'coverage_limits':['each declared certificate uses one route; no mixed-route single-observer execution claimed',
            'zero-route executed R=1; nontrivial R-divides-U cases remain symbolic coverage',
            'native outputs and moment values bound to saved fresh replay, not scientifically recomputed']}
    target=ROOT/'guard_review/HYBRID_RECORD_REVIEW.json'
    with target.open('x',encoding='utf-8') as stream:
        json.dump(output,stream,indent=2);stream.write('\n')
    print(json.dumps({'status':output['status'],'reader_sha256':output['reader_sha256'],
        'review_sha256':digest(target.read_bytes()),'branch_counts':counts,'total':total,
        'production_runner_digits':{k:resources['production'][k]['arithmetic']['adder_digit_replays'] for k in ('routing','endpoint','direct')}}))


if __name__=='__main__':
    main()
