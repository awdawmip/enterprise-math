"""Saved-record review only: stdlib I/O, lineage checks and cost recounts.

No scientific imports or numerical answer evaluation. Cursor arithmetic
consumes saved operation outputs; host arithmetic concerns indices and costs.
"""
from pathlib import Path
from collections import Counter
import ast
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT.parent/'sep27-qft-two-bit-aligned/guard_review/read_aligned_result.py'
HELPER_PIN = '6266405a29c589c67708149ee43942ff3fdde22a8da7966e123e58ab9bd3b450'
RAW_PIN = '4f6fae5355d3a809b765af17c6be7b2ac709cf63ec2e6fbd4e5b81a35cf79dc9'
GZIP_PIN = 'ba39feafb35e6d902c1ba1de8c7e64aba581eca7d02e429064c389f6d79e9dc0'
GUARD_PIN = 'fd9b5bf7a1b9680a23e3f4ea2ac0f0dce5d3ce362936635044c9324c3aa99f1b'
SOURCE_PINS = {
    'top_bit_general.py':'33a46d5f3dacf61e83cedd75cb3424f2375485b3b58984429d5c9fc76b8c96d0',
    'check_top_bit_general.py':'2b9b04fa1670af5c857eac4ba0810fe6a3c9e45d14f62a6f4371d1bd7ebefc9c',
    'DESIGN.md':'228c00ba4a2a29dc645e2d126b586183d7e6539a40396adf7719db4cdabc0ad3'}
SCHEMA = 'BRC_TOP_BIT_GENERAL_MODULUS_V1'
CASES = ((2,0,1,3),(3,1,2,3),(3,1,2,5),(4,2,3,6),(4,2,3,9),(3,1,2,11))
def digest(raw):
    return hashlib.sha256(raw).hexdigest()
assert digest(HELPER.read_bytes()) == HELPER_PIN
spec = importlib.util.spec_from_file_location('pinned_aligned_io_review',HELPER)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
io, same = old.io, old.same
DEPENDENCIES = {k:v for k,v in old.DEPENDENCIES.items() if k!='two_bit_proof_sha256'}
DEPENDENCIES.update({
    'proof_sha256':('sep27-qft-two-bit-top-general/TOP_BIT_GENERAL_MODULUS.md','880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89'),
    'proof_review_sha256':('sep27-qft-two-bit-top-general/guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md','e5f31e9619a3233c65af23b642d262e98996d6ca9ee538910e38c21ba412aaab')})

class Cursor(old.Cursor):
    def length(self,rec,head,step,limit):
        same([rec['head'],rec['step'],rec['exclusive_limit']],[head,step,limit])
        t = self.recorded(rec['last_minus_head'],lambda:self.sub(self.sub(limit,1),head))
        if t < 0:
            assert rec['empty'] is True
            n = self.recorded(rec['zero'],lambda:self.add(0,0))
            assert n == 0
        else:
            assert rec['empty'] is False
            quotient,_ = self.division(rec['division'],t,step)
            n = self.recorded(rec['length_addition'],lambda:self.add(quotient,1))
        same(n,rec['n'])
        return n

    def coefficient_piece(self,rec,piece,V,M):
        assert rec['piece']==piece and rec['signed_operations_start']==self.i
        if piece=='low':
            operations = (
                ('a0',lambda:self.mul(V,M)),
                ('a1',lambda:self.sub(3,self.mul(2,M))),
                ('b0',lambda:self.sub(self.mul(self.mul(2,V),M),self.mul(6,V))),
                ('b1',lambda:self.add(6,0)),('c',lambda:self.mul(-6,V)))
        else:
            assert piece=='high'
            operations = (
                ('a0',lambda:self.mul(-1,self.mul(V,M))),
                ('a1',lambda:self.sub(self.mul(2,M),1)),
                ('b0',lambda:self.sub(self.mul(2,V),self.mul(self.mul(2,V),M))),
                ('b1',lambda:self.add(-2,0)),('c',lambda:self.mul(2,V)))
        primitive = {name:self.recorded(rec['primitive'][name],fn) for name,fn in operations}
        a0,a1,b0,b1,c = (primitive[name] for name in ('a0','a1','b0','b1','c'))
        operations = (
            ('n',lambda:self.mul(3,a0)),('d',lambda:self.mul(3,a1)),
            ('q',lambda:self.mul(6,b0)),('dq',lambda:self.mul(6,b1)),('q2',lambda:self.mul(12,c)),
            ('delta1',lambda:self.sub(self.add(self.mul(-6,a0),self.mul(3,b0)),c)),
            ('ddelta1',lambda:self.add(self.mul(-6,a1),self.mul(3,b1))),
            ('delta2',lambda:self.add(self.mul(-6,b0),self.mul(6,c))),
            ('ddelta2',lambda:self.mul(-6,b1)),('delta3',lambda:self.mul(-8,c)))
        result = {name:self.recorded(rec['coefficients'][name],fn) for name,fn in operations}
        assert rec['signed_operations_stop']==self.i
        return result

    def segment(self,rec,piece,head,n,req,coeff):
        V,P,R = req['V'],req['P'],req['inputs']['R']
        H,L = req['half_length']['value'],req['L']
        same([rec['piece'],rec['coefficient_piece'],rec['head'],rec['n'],rec['step']],
             [piece,piece,head,n,R])
        same([rec['displacement_lower_bound'],rec['displacement_exclusive_upper_bound']],
             [0 if piece=='low' else H,H if piece=='low' else L])
        assert rec['signed_operations_start']==self.i
        b=head['value']
        if n==0:
            assert rec['empty'] is True and rec['table_calls']==[]
            answer=self.recorded(rec['zero'],lambda:self.add(0,0))
            self.empty_progressions += 1
        else:
            assert n>0 and rec['empty'] is False and len(rec['table_calls'])==2
            assert rec['displacement_lower_bound']<=b<rec['displacement_exclusive_upper_bound']
            table=self.table(rec['table_calls'][0],n,P,R,b)
            offset=self.recorded(rec['shifted_offset'],lambda:self.add(b,V))
            shifted=self.table(rec['table_calls'][1],n,P,R,offset)
            delta={key:self.recorded(rec['deltas'][key],lambda key=key:self.sub(shifted[key],table[key]))
                   for key in ('0,1','1,1','0,2','1,2','0,3')}
            w=rec['weighted_sums']
            d=self.recorded(w['d'],lambda:self.add(self.mul(b,table['0,0']),self.mul(R,table['1,0'])))
            dq=self.recorded(w['dq'],lambda:self.add(self.mul(b,table['0,1']),self.mul(R,table['1,1'])))
            dd1=self.recorded(w['ddelta1'],lambda:self.add(self.mul(b,delta['0,1']),self.mul(R,delta['1,1'])))
            dd2=self.recorded(w['ddelta2'],lambda:self.add(self.mul(b,delta['0,2']),self.mul(R,delta['1,2'])))
            factors={'n':table['0,0'],'d':d,'q':table['0,1'],'dq':dq,'q2':table['0,2'],
                'delta1':delta['0,1'],'ddelta1':dd1,'delta2':delta['0,2'],'ddelta2':dd2,'delta3':delta['0,3']}
            same(factors,rec['term_factors'])
            terms=[self.recorded(rec['terms'][name],lambda name=name:self.mul(coeff[name],factors[name]))
                   for name in factors]
            numerator=self.recorded(rec['three_sum_numerator'],lambda:self.total(terms))
            answer=self.exact(rec['exact_third'],numerator,3)
        same(answer,rec['value'])
        assert rec['signed_operations_stop']==self.i
        return answer

    def orientation(self,rec,label,req,coeff):
        assert rec['orientation']==label and rec['multiplicity']==1
        assert rec['signed_operations_start']==self.i
        b,R,L,H=rec['head']['value'],req['inputs']['R'],req['L'],req['half_length']['value']
        whole=self.length(rec['whole_length'],b,R,L)
        if rec['whole_length']['empty']:
            assert rec['empty'] is True and rec['segments']==[]
            answer=self.recorded(rec['zero'],lambda:self.add(0,0))
        else:
            assert rec['empty'] is False and len(rec['segments'])==2
            low=self.length(rec['low_length'],b,R,H)
            high=self.recorded(rec['high_count'],lambda:self.sub(whole,low))
            assert high>=0
            self.recorded(rec['high_head'],lambda:self.add(b,self.mul(R,low)))
            x=self.segment(rec['segments'][0],'low',rec['head'],low,req,coeff['low'])
            y=self.segment(rec['segments'][1],'high',rec['high_head'],high,req,coeff['high'])
            answer=self.recorded(rec['total'],lambda:self.total((x,y)))
        same(answer,rec['value'])
        assert rec['signed_operations_stop']==self.i
        return answer

    def request(self,req,index):
        inp=req['inputs']
        assert set(inp)=={'g','ell','k','R','r','stride'} and all(type(v) is int for v in inp.values())
        assert inp['g']>=2 and 0<=inp['ell']<inp['k']==inp['g']-1
        assert inp['R']>=1 and 0<=inp['r']<inp['R'] and inp['r']==index and inp['stride']==1
        assert req['signed_operations_start']==self.i and req['raw_denominator_exponent']==2*inp['g']
        assert req['route']=='TOP_BIT_TWO_PIECE_FLOOR_MOMENTS' and req['modulus_alignment_required'] is False
        self.power(inp['ell'],req['V']); self.power(inp['g']-inp['ell'],req['M'])
        same(self.mul(req['V'],req['M']),req['L']); same(self.add(req['V'],req['V']),req['P'])
        self.exact(req['half_length'],req['L'],2)
        assert req['scales_operations_stop']==self.i
        coeff={p:self.coefficient_piece(req['coefficients'][p],p,req['V'],req['M']) for p in ('low','high')}
        assert len(req['orientations'])==2
        pos,neg=req['orientations']
        self.recorded(pos['head'],lambda:self.add(inp['r'],0))
        self.recorded(neg['head'],lambda:self.sub(inp['R'],inp['r']))
        p=self.orientation(pos,'nonnegative_difference',req,coeff)
        n=self.orientation(neg,'negative_difference_magnitude',req,coeff)
        same(self.recorded(req['final_addition'],lambda:self.total((p,n))),req['value'])
        tables=sum(len(s['table_calls']) for o in req['orientations'] for s in o['segments'])
        assert req['top_level_table_calls']==tables<=8 and req['signed_operations_stop']==self.i

def inspect_certificate(cert,native,partial=False):
    assert cert['schema']==('INCOMPLETE_' if partial else '')+SCHEMA
    assert cert['source_sha256']==SOURCE_PINS['top_bit_general.py']
    if partial:
        assert cert['complete_certificate'] is False and cert['inflight_request'] is None
    else:
        for key,(_,pin) in DEPENDENCIES.items(): assert cert[key]==pin
    e=cert['actual_integer_evidence']
    result=old.inspect_evidence(e,native,partial=partial)
    c=Cursor(e)
    for index,req in enumerate(cert['requests']): c.request(req,index)
    assert c.i==len(c.ops)
    result.update(requests=len(cert['requests']),top_level_tables=c.seen_tables,empty_segments=c.empty_progressions)
    return result

def coverage(certs,cases):
    reqs=[r for c in certs for r in c['requests']]
    seg=[s for r in reqs for o in r['orientations'] for s in o['segments']]
    assert any(r['value']<0 for r in reqs)
    assert any(o['empty'] for r in reqs for o in r['orientations']) and any(s['empty'] for s in seg)
    assert {s['piece'] for s in seg if not s['empty']}=={'low','high'}
    assert any(s['piece']=='high' and s['head']['value']==s['displacement_lower_bound'] for s in seg if not s['empty'])
    half=certs[3]['requests'][3]['orientations']
    assert half[0]['head']['value']==half[1]['head']['value']==3
    assert any(r['inputs']['R']>r['L'] for r in reqs)
    assert any(d['low_remainder']!=0 for c in cases for d in c['typed_enumeration']['digit_observations'])
    return {'requests':len(reqs),'segments':len(seg),'nonempty_segments':sum(not s['empty'] for s in seg),
        'top_level_table_calls':sum(r['top_level_table_calls'] for r in reqs),'at_most_eight_tables_each':True,
        'both_polynomial_pieces_and_exact_third_seen':True,'negative_output_seen':True,
        'empty_segments_and_orientations_seen':True,'high_piece_exact_boundary_seen':True,
        'half_modulus_both_orientations_retained':True,'R_larger_than_L_seen':True,
        'alignment_test_or_order_discovery_performed':False,'actual_comparator_nonzero_low_remainder_seen':True}

def main():
    data,summary=io.load(ROOT,'TOP_BIT_GENERAL',RAW_PIN,GZIP_PIN)
    same(data['source_sha256'],SOURCE_PINS)
    assert summary['raw_bytes']==75217873 and summary['gzip_bytes']==2684245
    for _,(rel,pin) in DEPENDENCIES.items(): assert digest((ROOT.parent/rel).read_bytes())==pin
    guardbytes=(ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guardbytes)==GUARD_PIN==data['startup_guard']['sha256']
    same(json.loads(guardbytes),data['startup_guard']['receipt'])
    guard=data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['boundary']=='startup'
    template=(old.ROOT/'check_aligned_two_bit.py').read_bytes()
    comp=data['comparator_source']
    assert digest(template)==comp['template_sha256']==old.SOURCE_PINS['check_aligned_two_bit.py']
    def function_text(text):
        tree=ast.parse(text)
        node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='typed_pair_histogram')
        return ast.get_source_segment(text,node)
    function=function_text(template.decode('utf-8'))
    same(function,function_text((ROOT/'check_top_bit_general.py').read_text(encoding='utf-8')))
    assert digest(function.encode())==comp['copied_function_sha256']=='c665b55053b03bb96a0411bd5fab39ae0f7d920ec08b1cf1ee0d62ac0b4f58e7'
    assert comp['historical_checker_imported_or_executed'] is False and comp['exact_source_text_equal'] is True
    assert data['historical_science_reexecuted'] is False
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    assert native['native_adder']['input_columns']==8 and native['native_adder']['positive_BRC_input_states']==12
    for name,rel in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/rel).read_bytes())==native['files_sha256'][name]
    groups={k:[] for k in ('production','typed_pair_comparator','positive_replay','negative_replay')}
    reviewed=[]; certs=[]; pairs=0; percase=[]
    for index,case in enumerate(data['cases']):
        same([case['inputs'][k] for k in ('g','ell','k','R')],CASES[index])
        cert,verify=case['certificate'],case['verification']; replay=verify['replay_certificate']
        assert case['all_residues_equal'] is True and verify['verified'] is True
        assert verify['requests_replayed']==len(cert['requests'])==case['inputs']['R']
        assert io.semantic(cert)==io.semantic(replay)
        same(case['values'],[r['value'] for r in cert['requests']])
        reviewed.append({'inputs':case['inputs'],'values':case['values'],
            'production':inspect_certificate(cert,native),'typed_comparator':old.inspect_comparator(case,native),
            'positive_replay':inspect_certificate(replay,native)})
        pairs+=len(case['typed_enumeration']['pair_observations']); certs.append(cert)
        for key,e,costkey in (
            ('production',cert['actual_integer_evidence'],'production_cost'),
            ('typed_pair_comparator',case['typed_enumeration']['actual_integer_evidence'],'typed_enumeration_cost'),
            ('positive_replay',replay['actual_integer_evidence'],'positive_replay_cost')):
            groups[key].append(e)
            same(case[costkey]['arithmetic_stats'],e['arithmetic_stats'])
            assert case[costkey]['typed_operations']==len(e['arithmetic_operations'])
            assert case[costkey]['signed_operations']==len(e['signed_operations'])
            assert case[costkey]['moment_nodes']==len(e['moment_nodes'])
            same(case[costkey]['moment_stats'],e['stats'])
        prod=case['production_cost']['arithmetic_stats']['adder_digit_replays']
        brute=case['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays']
        percase.append({'inputs':case['inputs'],'production_digits':prod,'comparator_digits':brute,
            'production_extra_digits':prod-brute,'production_over_comparator_metadata':prod/brute})
    assert len(reviewed)==6 and pairs==720 and sum(len(c['requests']) for c in certs)==37
    measured=coverage(certs,data['cases']); same(measured,data['coverage']); same(measured,summary['coverage'])
    boundary=data['production_boundary_rejection']
    assert boundary['rejected'] is True and boundary['state_and_paid_evidence_unchanged'] is True
    assert boundary['additional_native_calls']==boundary['additional_typed_operations']==0
    assert boundary['native_subinterval']['start']==boundary['native_subinterval']['stop']
    same(boundary['before'],boundary['after'])
    same(boundary['before']['requests'],certs[0]['requests'][:1])
    boundary_review=inspect_certificate(boundary['before'],native,partial=True)
    assert boundary['reuse_completed_by_original_grid'] is True and len(certs[0]['requests'])==3
    for r in data['input_rejections']:
        assert r['rejected'] is True and r['actual_typed_operations']==0
        assert r['call_interval']['start']==r['call_interval']['stop']
    assert len(data['input_rejections'])==12
    expected=['segment_split','segment_high_head','polynomial_coefficient','shifted_offset','exact_third',
        'drop_half_modulus_orientation','moment_table_output','raw_exponent','signed_output',
        'valid_prefix_then_invalid_non_top','source_early','schema_early','bool_input_early','nonstring_key_early']
    same([r['name'] for r in data['negative_checks']],expected)
    negatives=[]
    for row in data['negative_checks']:
        assert row['rejected'] is True
        attempted=old.decode_keys(row['attempted_certificate_typed_key_encoding'])
        captured=row['actual_replay_certificates']
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
    assert Counter(r['type'] for r in negatives)=={'early':4,'paid_full':9,'paid_valid_prefix':1}
    calculated={k:old.costs(es) for k,es in groups.items()}
    same(calculated,data['cost_categories']); same(calculated,summary['cost_categories'])
    assert sum(len(es) for es in groups.values())==28
    calls=Counter(); frontier=0
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        calls[row['category']]+=row['stop']-row['start']; frontier=row['stop']
    same(dict(calls),data['native_calls_by_category']); same(data['call_intervals'],summary['call_intervals'])
    assert frontier==len(data['actual_core_calls'])==data['actual_core_call_count']==1
    assert data['actual_core_calls'][0]['states']==12
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for es in groups.values() for e in es)==1
    totals={k:sum(row['sum'][k] for row in calculated.values()) for k in calculated['production']['sum']}
    assert totals['adder_digit_replays']==325030
    result={'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW','reader_sha256':digest(Path(__file__).read_bytes()),
        'scope':'Shared-context stdlib-only saved-record review; no scientific import, answer evaluation or rerun',
        'pure_io_helpers':{'aligned':HELPER_PIN,'direct':old.HELPER_PIN},'source_sha256':SOURCE_PINS,
        'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':summary['raw_bytes'],'gzip_bytes':summary['gzip_bytes'],
        'startup_guard_sha256':GUARD_PIN,'native_source':native,'comparator_source':comp,'cases':reviewed,
        'coverage':measured,'typed_ordered_pairs':pairs,'input_rejections':data['input_rejections'],'negative_checks':negatives,
        'boundary_rejection':{'inspection':boundary_review,'before_after_strict_equal':True,
            'completed_request_count':1,'inflight_request':None,'subsequent_original_requests_complete':True,
            'additional_typed_operations':0,'additional_native_calls':0,'overlaps_production_not_charged_again':True},
        'charged_streams':28,'cost_categories':calculated,'total_current_run_cost':totals,
        'native_calls_by_category':dict(calls),'actual_core_calls':data['actual_core_calls'],'per_case_comparison':percase,
        'production_over_comparator_metadata':96452/34544,
        'elapsed_seconds_before_serialization':summary['elapsed_seconds_before_serialization'],
        'unexpected_failure_artifact_present':(ROOT/'TOP_BIT_GENERAL_FAILED_EXECUTION.json.gz').exists(),
        'scientific_execution_performed':False,'comparison_is_timing_benchmark':False,
        'limits':['Saved source-bound full-adder columns anchor all cells; no arithmetic answer is recomputed here.',
            'All moment nodes, children, ranges and saved table outputs are linked, not numerically re-evaluated.',
            'Fresh replay comparisons ignore only the declared native cache-delta counter.',
            'Early non-top rejection preserves a complete prefix and allows reuse; this is not incomplete arithmetic recovery.',
            'All six production digit costs exceed the same-tuple typed enumeration costs.',
            'Host bookkeeping, JSON, serialization and index work are outside instrumented arithmetic counters.',
            'This is a bounded scalar count at supplied R, not order discovery, matrix Gram integration or a full Shor result.']}
    out=Path(__file__).parent/'TOP_BIT_GENERAL_RECORD_REVIEW.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'total':totals,'per_case':percase,'sha256':digest(out.read_bytes())}))

if __name__=='__main__':
    main()
