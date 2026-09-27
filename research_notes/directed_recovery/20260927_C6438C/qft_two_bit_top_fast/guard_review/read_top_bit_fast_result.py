"""Full saved-record I/O peer review; no scientific imports or evaluation.

Cursor methods only consume saved arithmetic outputs. Host arithmetic is for
source/index/coverage checks and resource-accounting metadata.
"""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json

ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'sep27-qft-two-bit-top-general/guard_review/read_top_bit_general_result.py'
HELPER_PIN='ee6baa8d58826eab8a583997ffa516bb38f1d5535705b4a817737cb2e7876312'
RAW_PIN='db60ed6dd188c5936585c0d1a4dbffa83652baca0dd2551182148d2c8457038a'
GZIP_PIN='7cea2d841376650734622fe7d29b529a8f46cd195a4dc87b63993d9e995fc507'
GUARD_PIN='f8ff9c3877cfc3dd22ad91bbc05a3927105769a60ac541b74ffe31bcc77647ae'
SOURCE_PINS={
    'top_bit_fast.py':'8c73aa1ad2f195b9d8f440112dac7b08cacbc1e544e65850a754dc38f2fa48e8',
    'check_top_bit_fast.py':'76dc68753c07e9eedd64183c4a2875fde709ef6f1f0f59dd32b6ce39eee8dc21',
    'DESIGN.md':'87e0d3416e24030a6e76f9b418d9cdb1aa9ffba9175e63fbff4ce622521ed275',
    'POINT_AND_SETUP_REUSE.md':'e4c0f33e1fd6c8d62d3604eb37db41b937ba999e536b61cfeac6e1300c9690e6'}
SCHEMA='BRC_TOP_BIT_POINT_AND_SETUP_REUSE_V1'
def digest(raw): return hashlib.sha256(raw).hexdigest()
assert digest(HELPER.read_bytes())==HELPER_PIN
spec=importlib.util.spec_from_file_location('pinned_top_general_io_review',HELPER)
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
io,old,same=base.io,base.old,base.same
DEPENDENCIES=dict(base.DEPENDENCIES)
DEPENDENCIES.update({
    'base_source_sha256':('sep27-qft-two-bit-top-general/top_bit_general.py',base.SOURCE_PINS['top_bit_general.py']),
    'optimization_proof_sha256':('sep27-qft-two-bit-top-fast/POINT_AND_SETUP_REUSE.md',SOURCE_PINS['POINT_AND_SETUP_REUSE.md'])})

class Cursor(base.Cursor):
    def __init__(self,evidence,setups):
        super().__init__(evidence)
        self.setups=setups; self.setup_keys={}; self.coefficients={}
        self.setup_builds=0; self.setup_hits=0; self.coefficient_builds=0; self.coefficient_hits=0
        self.routes=Counter()

    def setup(self,req):
        g,ell=req['inputs']['g'],req['inputs']['ell']; key=(g,ell)
        index=req['setup_index']
        assert type(index) is int and 0<=index<len(self.setups)
        rec=self.setups[index]
        same(rec['inputs'],{'g':g,'ell':ell}); assert rec['complete'] is True
        if key in self.setup_keys:
            assert req['setup_cache_hit'] is True and index==self.setup_keys[key]
            assert rec['signed_operations_stop']<=self.i
            self.setup_hits+=1
        else:
            assert req['setup_cache_hit'] is False and index==len(self.setup_keys)
            assert rec['signed_operations_start']==self.i
            self.recorded(rec['V'],lambda:self.power(ell,rec['V']['value']))
            self.recorded(rec['M'],lambda:self.power(g-ell,rec['M']['value']))
            self.recorded(rec['L'],lambda:self.mul(rec['V']['value'],rec['M']['value']))
            self.recorded(rec['P'],lambda:self.add(rec['V']['value'],rec['V']['value']))
            self.exact(rec['H'],rec['L']['value'],2)
            assert rec['signed_operations_stop']==self.i
            self.setup_keys[key]=index; self.setup_builds+=1
        assert req['setup_access_operations_stop']==self.i
        self.current_setup=index
        return rec

    def segment(self,rec,piece,head,n,req,ignored):
        setup=self.setups[self.current_setup]
        V,M,R=setup['V']['value'],setup['M']['value'],req['inputs']['R']
        H,L=setup['H']['value'],setup['L']['value']
        same([rec['piece'],rec['coefficient_piece'],rec['head'],rec['n'],rec['step']],
             [piece,piece,head,n,R])
        same([rec['displacement_lower_bound'],rec['displacement_exclusive_upper_bound']],
             [0 if piece=='low' else H,H if piece=='low' else L])
        assert rec['signed_operations_start']==self.i
        route=rec['route']; self.routes[route]+=1
        b=head['value']
        if n==0:
            assert route=='EMPTY' and rec['empty'] is True and rec['table_calls']==[]
            assert 'coefficient_reference' not in rec
            answer=self.recorded(rec['zero'],lambda:self.add(0,0)); self.empty_progressions+=1
        elif n==1:
            assert route=='SINGLE_DISPLACEMENT' and rec['empty'] is False and rec['table_calls']==[]
            assert 'coefficient_reference' not in rec
            assert rec['displacement_lower_bound']<=b<rec['displacement_exclusive_upper_bound']
            z,t=self.division(rec['compressed_displacement'],b,V)
            _,parity=self.division(rec['parity'],z,2); assert parity in (0,1)
            if piece=='low':
                overlap=self.recorded(rec['base_overlap'],lambda:self.sub(M,self.mul(3,z))); alpha=-3
            else:
                overlap=self.recorded(rec['base_overlap'],lambda:self.sub(z,M)); alpha=1
            same(rec['alpha'],alpha)
            weight=self.recorded(rec['weight'],lambda:self.sub(V,self.mul(2,t)))
            unsigned=self.recorded(rec['unsigned_overlap'],lambda:self.sub(self.mul(weight,overlap),self.mul(alpha,t)))
            sign=1 if parity==0 else -1; same(rec['sign'],sign)
            answer=self.recorded(rec['result'],lambda:self.mul(sign,unsigned))
        else:
            assert n>=2 and route=='FLOOR_MOMENTS' and rec['empty'] is False
            ref=rec['coefficient_reference']; same(ref['piece'],piece)
            coeff=setup['coefficients'][piece]; assert coeff['complete'] is True
            key=(self.current_setup,piece)
            if key in self.coefficients:
                assert ref['cache_hit'] is True and coeff['signed_operations_stop']<=self.i
                values=self.coefficients[key]; self.coefficient_hits+=1
            else:
                assert ref['cache_hit'] is False
                values=self.coefficient_piece(coeff,piece,V,M)
                self.coefficients[key]=values; self.coefficient_builds+=1
            assert rec['moment_evaluation_signed_operations_start']==self.i
            # The inherited reader consumes only recorded moment outputs.
            # Segment start includes coefficient setup; moment start excludes it.
            moment_rec=dict(rec); moment_rec['signed_operations_start']=self.i
            answer=super().segment(moment_rec,piece,head,n,req,values)
        same(answer,rec['value']); assert rec['signed_operations_stop']==self.i
        return answer

    def request(self,req):
        inp=req['inputs']
        assert set(inp)=={'g','ell','k','R','r','stride'} and all(type(v) is int for v in inp.values())
        assert inp['g']>=2 and 0<=inp['ell']<inp['k']==inp['g']-1
        assert inp['R']>=1 and 0<=inp['r']<inp['R'] and inp['stride']==1
        assert req['signed_operations_start']==self.i and req['raw_denominator_exponent']==2*inp['g']
        assert req['modulus_alignment_required'] is False and req['route']=='TOP_BIT_POINT_AND_SETUP_REUSE'
        setup=self.setup(req)
        facade={'inputs':inp,**{k:setup[k]['value'] for k in ('V','M','L','P')},'half_length':setup['H']}
        assert len(req['orientations'])==2
        pos,neg=req['orientations']
        self.recorded(pos['head'],lambda:self.add(inp['r'],0))
        self.recorded(neg['head'],lambda:self.sub(inp['R'],inp['r']))
        p=self.orientation(pos,'nonnegative_difference',facade,{'low':None,'high':None})
        n=self.orientation(neg,'negative_difference_magnitude',facade,{'low':None,'high':None})
        same(self.recorded(req['final_addition'],lambda:self.total((p,n))),req['value'])
        tables=sum(len(s['table_calls']) for o in req['orientations'] for s in o['segments'])
        assert req['top_level_table_calls']==tables<=8 and req['signed_operations_stop']==self.i

def inspect_certificate(cert,native,partial=False):
    assert cert['schema']==('INCOMPLETE_' if partial else '')+SCHEMA
    assert cert['source_sha256']==SOURCE_PINS['top_bit_fast.py']
    if partial:
        assert cert['complete_certificate'] is False and cert['inflight_request'] is None
    else:
        for key,(_,pin) in DEPENDENCIES.items(): assert cert[key]==pin
    e=cert['actual_integer_evidence']; result=old.inspect_evidence(e,native,partial=partial)
    c=Cursor(e,cert['setups'])
    for req in cert['requests']: c.request(req)
    assert c.i==len(c.ops) and len(c.setup_keys)==len(cert['setups'])
    assert set(c.coefficients)=={(i,piece) for i,s in enumerate(cert['setups']) for piece in s['coefficients']}
    result.update(requests=len(cert['requests']),top_level_tables=c.seen_tables,route_counts=dict(c.routes),
        setup_builds=c.setup_builds,setup_hits=c.setup_hits,coefficient_builds=c.coefficient_builds,
        coefficient_hits=c.coefficient_hits,empty_segments=c.empty_progressions)
    return result

def coverage(certs,inspections):
    reqs=[r for c in certs for r in c['requests']]
    segs=[s for r in reqs for o in r['orientations'] for s in o['segments']]
    points=[s for s in segs if s['route']=='SINGLE_DISPLACEMENT']
    assert {s['piece'] for s in points}=={'low','high'} and {s['parity']['remainder'] for s in points}=={0,1}
    assert any(s['compressed_displacement']['remainder']>0 for s in points)
    assert any(s['coefficient_reference']['cache_hit'] for s in segs if s['route']=='FLOOR_MOMENTS')
    assert any(not c['setups'][0]['coefficients'] for c in certs) and any(r['value']<0 for r in reqs)
    half=certs[3]['requests'][3]['orientations']; assert half[0]['head']['value']==half[1]['head']['value']==3
    return {'requests':len(reqs),'segments':len(segs),'route_counts':dict(Counter(s['route'] for s in segs)),
        'top_level_table_calls':sum(x['top_level_tables'] for x in inspections),
        'setup_misses':sum(x['setup_builds'] for x in inspections),'setup_hits':sum(x['setup_hits'] for x in inspections),
        'coefficient_constructions':sum(x['coefficient_builds'] for x in inspections),
        'singleton_both_pieces_parities_nonzero_remainders':True,'empty_and_moment_routes':True,
        'unused_coefficients_not_built':True,'half_modulus_orientations_retained':True}

def check_cost(e,saved):
    same(saved['arithmetic_stats'],e['arithmetic_stats']); same(saved['moment_stats'],e['stats'])
    for field,trace in (('typed_operations','arithmetic_operations'),('signed_operations','signed_operations'),
        ('moment_nodes','moment_nodes'),('window_queries','window_weight_queries')):
        assert saved[field]==len(e[trace])

def main():
    data,summary=io.load(ROOT,'TOP_BIT_FAST',RAW_PIN,GZIP_PIN)
    same(data['source_sha256'],SOURCE_PINS)
    assert summary['raw_bytes']==33060129 and summary['gzip_bytes']==1258273
    for _,(rel,pin) in DEPENDENCIES.items(): assert digest((ROOT.parent/rel).read_bytes())==pin
    guardbytes=(ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guardbytes)==GUARD_PIN==data['startup_guard']['sha256']
    same(json.loads(guardbytes),data['startup_guard']['receipt'])
    guard=data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['boundary']=='startup' and guard['mode']=='TASK_RESEARCH'
    history,hs=io.load(base.ROOT,'TOP_BIT_GENERAL',base.RAW_PIN,base.GZIP_PIN)
    same(history['source_sha256'],base.SOURCE_PINS)
    hr=data['historical_evidence_reuse']
    for key,value in [('payload_sha256',base.RAW_PIN),('artifact_sha256',base.GZIP_PIN),
        ('raw_bytes',hs['raw_bytes']),('gzip_bytes',hs['gzip_bytes']),('source_sha256',base.SOURCE_PINS)]: same(hr[key],value)
    assert hr['whole_payload_read_and_hash_checked'] is True
    assert hr['historical_pair_comparator_reexecuted'] is False and hr['historical_production_reexecuted'] is False
    assert data['new_typed_pair_comparator_executions']==0 and data['historical_science_reexecuted'] is False
    hb=(base.ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(hb)==base.GUARD_PIN==hr['guard_sha256']==history['startup_guard']['sha256']
    same(json.loads(hb),history['startup_guard']['receipt'])
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    assert native['native_adder']['input_columns']==8 and native['native_adder']['positive_BRC_input_states']==12
    for name,rel in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/rel).read_bytes())==native['files_sha256'][name]
    groups={k:[] for k in ('production','positive_replay','cache_control','cache_control_replay','negative_replay')}
    reviewed=[]; certs=[]; history_pairs=0; percase=[]
    for index,case in enumerate(data['cases']):
        prior=history['cases'][index]
        same([case['inputs'][k] for k in ('g','ell','k','R')],base.CASES[index]); same(case['inputs'],prior['inputs'])
        cert,verify=case['certificate'],case['verification']; replay=verify['replay_certificate']
        assert case['all_residues_equal_saved_typed_comparator'] is True and verify['verified'] is True
        assert verify['requests_replayed']==len(cert['requests'])==case['inputs']['R']
        assert [r['inputs']['r'] for r in cert['requests']]==list(range(case['inputs']['R']))
        assert io.semantic(cert)==io.semantic(replay)
        same(case['values'],[r['value'] for r in cert['requests']]); same(case['values'],prior['values'])
        assert prior['all_residues_equal'] is True and prior['verification']['verified'] is True
        assert io.semantic(prior['certificate'])==io.semantic(prior['verification']['replay_certificate'])
        for key,(_,pin) in base.DEPENDENCIES.items(): assert prior['certificate'][key]==pin
        same(prior['certificate']['actual_integer_evidence']['native_source'],native)
        old_comparator=old.inspect_comparator(prior,native)
        history_pairs+=len(prior['typed_enumeration']['pair_observations'])
        reviewed.append({'inputs':case['inputs'],'values':case['values'],'production':inspect_certificate(cert,native),
            'positive_replay':inspect_certificate(replay,native),'historical_comparator_records_checked_not_charged':old_comparator})
        certs.append(cert)
        for key,e,costkey in (('production',cert['actual_integer_evidence'],'production_cost'),
            ('positive_replay',replay['actual_integer_evidence'],'positive_replay_cost')):
            groups[key].append(e); check_cost(e,case[costkey])
        same(case['historical_production_cost'],prior['production_cost'])
        same(case['historical_typed_comparator_cost'],prior['typed_enumeration_cost'])
        new=case['production_cost']['arithmetic_stats']['adder_digit_replays']
        before=prior['production_cost']['arithmetic_stats']['adder_digit_replays']
        brute=prior['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays']
        percase.append({'inputs':case['inputs'],'new_production_digits':new,'historical_production_digits':before,
            'historical_comparator_digits':brute,'production_decrease_digits':before-new,
            'new_below_historical_comparator':new<brute})
    assert len(reviewed)==6 and history_pairs==hr['historical_pair_records']==720
    measured=coverage(certs,[x['production'] for x in reviewed]); same(measured,data['coverage']); same(measured,summary['coverage'])
    mixed=data['mixed_cache_control']; mc=mixed['certificate']; mv=mixed['verification']; mr=mv['replay_certificate']
    same(mixed['requests_from_historical_grid'],[[1,0],[0,0],[1,1],[2,0]])
    assert mv['verified'] is True and mv['requests_replayed']==4 and io.semantic(mc)==io.semantic(mr)
    same([r['setup_index'] for r in mc['requests']],[0,1,0,0]); same([r['setup_cache_hit'] for r in mc['requests']],[False,False,True,True])
    for req,(index,residue) in zip(mc['requests'],mixed['requests_from_historical_grid']):
        same(req['inputs'],dict(history['cases'][index]['inputs'],r=residue,stride=1))
        same(req['value'],history['cases'][index]['values'][residue])
    mixed_review={'production':inspect_certificate(mc,native),'positive_replay':inspect_certificate(mr,native),
        'requests_from_historical_grid':mixed['requests_from_historical_grid'],'values':[r['value'] for r in mc['requests']]}
    groups['cache_control'].append(mc['actual_integer_evidence']); groups['cache_control_replay'].append(mr['actual_integer_evidence'])
    boundary=data['production_boundary_rejection']
    assert boundary['rejected'] is True and boundary['state_and_paid_evidence_unchanged'] is True
    assert boundary['additional_typed_operations']==boundary['additional_native_calls']==0
    assert boundary['native_subinterval']['start']==boundary['native_subinterval']['stop']
    same(boundary['before'],boundary['after']); same(boundary['before']['requests'],certs[0]['requests'][:1])
    boundary_review=inspect_certificate(boundary['before'],native,partial=True)
    assert boundary['reuse_completed_by_original_grid'] is True and len(certs[0]['requests'])==3
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations']==0
        assert row['call_interval']['start']==row['call_interval']['stop']
    assert len(data['input_rejections'])==12
    expected=['setup_scale','setup_input','setup_index','setup_hit','setup_complete','coefficient_value',
        'coefficient_reference','point_parity','point_alpha','point_result','table_output','half_modulus_orientation',
        'raw_exponent','valid_prefix_then_invalid_non_top','source_early','schema_early','bool_input_early','nonstring_key_early']
    same([r['name'] for r in data['negative_checks']],expected)
    negatives=[]
    for row in data['negative_checks']:
        assert row['rejected'] is True
        attempted=old.decode_keys(row['attempted_certificate_typed_key_encoding']); captured=row['actual_replay_certificates']
        if row['name'].endswith('_early'):
            assert captured==[] and row['call_interval']['start']==row['call_interval']['stop']
            result={'type':'early','paid_receipts':0}
        else:
            assert len(captured)==1
            replay=captured[0]; groups['negative_replay'].append(replay['actual_integer_evidence'])
            if row['name']=='valid_prefix_then_invalid_non_top':
                assert len(replay['requests'])==1
                same(replay['requests'],certs[row['source_case_index']]['requests'][:1])
                same(replay['requests'],attempted['requests'][:1])
                result=inspect_certificate(replay,native,partial=True); result['type']='paid_valid_prefix'
            else:
                assert io.semantic(replay)==io.semantic(certs[row['source_case_index']])
                assert io.semantic(replay)!=io.semantic(attempted)
                result=inspect_certificate(replay,native); result['type']='paid_full'
            result['paid_receipts']=1
        result.update(name=row['name'],kind=row['kind'],error=row['error']); negatives.append(result)
    assert Counter(r['type'] for r in negatives)=={'early':4,'paid_full':13,'paid_valid_prefix':1}
    calculated={k:old.costs(es) for k,es in groups.items()}
    same(calculated,data['cost_categories']); same(calculated,summary['cost_categories'])
    assert sum(len(es) for es in groups.values())==28
    calls=Counter(); frontier=0
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        calls[row['category']]+=row['stop']-row['start']; frontier=row['stop']
    same(dict(calls),data['native_calls_by_category']); same(data['call_intervals'],summary['call_intervals'])
    assert frontier==len(data['actual_core_calls'])==data['actual_core_call_count']==1 and data['actual_core_calls'][0]['states']==12
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for es in groups.values() for e in es)==1
    totals={k:sum(row['sum'][k] for row in calculated.values()) for k in calculated['production']['sum']}
    assert totals['adder_digit_replays']==122802
    new=sum(p['new_production_digits'] for p in percase); prior=sum(p['historical_production_digits'] for p in percase)
    brute=sum(p['historical_comparator_digits'] for p in percase)
    result={'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW','reader_sha256':digest(Path(__file__).read_bytes()),
        'scope':'Shared-context stdlib-only saved-record review; no scientific imports, answer evaluation or rerun',
        'pure_io_helpers':{'top_general':HELPER_PIN,'aligned':base.HELPER_PIN,'direct':old.HELPER_PIN},
        'source_sha256':SOURCE_PINS,'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,
        'raw_bytes':summary['raw_bytes'],'gzip_bytes':summary['gzip_bytes'],'startup_guard_sha256':GUARD_PIN,
        'native_source':native,'historical_evidence_reuse':hr,'cases':reviewed,'coverage':measured,
        'mixed_cache_control':mixed_review,'input_rejections':data['input_rejections'],'negative_checks':negatives,
        'boundary_rejection':{'inspection':boundary_review,'before_after_strict_equal':True,
            'subsequent_original_requests_complete':True,'additional_typed_operations':0,'additional_native_calls':0,
            'overlaps_production_not_charged_again':True},
        'charged_streams':28,'cost_categories':calculated,'total_current_run_cost':totals,
        'native_calls_by_category':dict(calls),'actual_core_calls':data['actual_core_calls'],'per_case_comparison':percase,
        'production_comparison':{'new':new,'historical_production':prior,'historical_comparator':brute,
            'decrease_percent_vs_predecessor_metadata':100*(prior-new)/prior,
            'decrease_percent_vs_historical_comparator_metadata':100*(brute-new)/brute,
            'cases_below_predecessor':sum(p['new_production_digits']<p['historical_production_digits'] for p in percase),
            'cases_below_historical_comparator':sum(p['new_below_historical_comparator'] for p in percase)},
        'elapsed_seconds_before_serialization':summary['elapsed_seconds_before_serialization'],
        'unexpected_failure_artifact_present':(ROOT/'TOP_BIT_FAST_FAILED_EXECUTION.json.gz').exists(),
        'scientific_execution_performed':False,'comparison_is_timing_benchmark':False,
        'limits':['Setup and coefficients are consumed once at their actual construction time and later references pay no duplicate arithmetic.',
            'Current all 28 streams and old 720 comparator records are read; old records and overlapping snapshots are not newly charged.',
            'Saved moment nodes, children, ranges, outputs, signed/typed links and native cells are checked, not numerically recomputed.',
            'Only the declared native primitive cache-delta counter is excluded from strict fresh-certificate equality.',
            'Same-g different-ell setups and deliberate valid numerical interruption remain unexecuted boundaries.',
            'Arithmetic counters exclude JSON, hashing, metadata and other uninstrumented host work.',
            'No matched timing, new asymptotic class, order discovery, full matrix Gram or Shor sampling claim follows.']}
    out=Path(__file__).parent/'TOP_BIT_FAST_RECORD_REVIEW.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'costs':totals,'comparison':result['production_comparison'],
        'coverage':measured,'mixed_cache':mixed_review,'sha256':digest(out.read_bytes())}))

if __name__=='__main__': main()
