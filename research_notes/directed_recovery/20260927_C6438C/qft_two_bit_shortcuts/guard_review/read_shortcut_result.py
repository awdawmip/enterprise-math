"""Complete saved-record I/O review. No scientific module import or evaluation.

Cursor arithmetic consumes recorded outputs; host arithmetic is limited to
indices, coverage, hashes and costs. The pinned helper imports only stdlib I/O.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT.parent/'sep27-qft-two-bit-aligned/guard_review/read_aligned_result.py'
HELPER_PIN = '6266405a29c589c67708149ee43942ff3fdde22a8da7966e123e58ab9bd3b450'
RAW_PIN = '55f0652225cffe7a658f5528e30ebf8c90342b9422def6799285d32a7dc66be7'
GZIP_PIN = '07ff488f357a2d80a682508f28b7f242a4cdd92c2cc15cfd54b95e884104e53a'
GUARD_PIN = 'd002bf88886316a60af33391ebaf0ef54325c0dc5f9787fb88a96c08022fb297'
SOURCE_PINS = {
    'shortcut_two_bit.py':'874d5d79f67ef5a00176b48faa2959811b925820031a90f71f80b6ba6fd5a34b',
    'check_shortcut_two_bit.py':'e7dca9fe712c367ed5434ed88ac2027178bbf05fff1fb94373d77c8c01d39e22',
    'DESIGN.md':'b41ebf07ab34b9fa6981f529a5d230952b050786dd97f64eb1886827b1b3d667'}
SCHEMA = 'BRC_TWO_BIT_STRUCTURAL_SHORTCUTS_V1'
def digest(raw):
    return hashlib.sha256(raw).hexdigest()
assert digest(HELPER.read_bytes()) == HELPER_PIN
spec = importlib.util.spec_from_file_location('pinned_aligned_io_review', HELPER)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
io, same = old.io, old.same
DEPENDENCIES = dict(old.DEPENDENCIES)
DEPENDENCIES.update({
    'aligned_source_sha256':('sep27-qft-two-bit-aligned/aligned_two_bit.py',old.SOURCE_PINS['aligned_two_bit.py']),
    'shortcut_proof_sha256':('sep27-qft-two-bit-shortcuts/STRUCTURAL_SHORTCUTS.md','845df9a8a9e67862f197412d2bd8a20fdc10aedf14db73efc59f70ca97cfda7f'),
    'shortcut_review_sha256':('sep27-qft-two-bit-shortcuts/guard_review/STRUCTURAL_SHORTCUTS_REVIEW.md','133d81d27860bc108075a8b995ec42644d37834c3824caaacfc6c22b30f946ab')})

class Cursor(old.Cursor):
    def affine_T(self, rec, s, head, step):
        same([rec['s'],rec['head'],rec['step']],[s,head,step])
        assert rec['signed_operations_start'] == self.i
        less = self.recorded(rec['less'],lambda:self.sub(s,1))
        numerator = self.recorded(rec['numerator'],lambda:self.mul(s,less))
        half = self.exact(rec['exact_half'],numerator,2)
        first = self.recorded(rec['head_term'],lambda:self.mul(s,head))
        second = self.recorded(rec['step_term'],lambda:self.mul(step,half))
        answer = self.recorded(rec['total'],lambda:self.add(first,second))
        same(answer,rec['value'])
        assert rec['signed_operations_stop'] == self.i
        return answer

    def progression(self, rec, head, label, req):
        if rec['strategy'] == 'FROZEN_DIRECT_MOMENTS':
            assert req['coefficients'] is not None
            return super().progression(rec,head,label,req)
        assert rec['strategy'] == 'HIGHEST_BIT_AFFINE' and req['coefficients'] is None
        same(rec['head'],head)
        assert rec['orientation'] == label and rec['multiplicity'] == 1
        assert rec['signed_operations_start'] == self.i and rec['table_calls'] == []
        M,U,step,b = req['L'],req['U'],req['inputs']['R'],head['value']
        same([rec['step'],rec['limit'],rec['junction']],[step,M,U])
        n = self.length(rec['canonical_length'],b,step,M)
        same(n,rec['n'])
        same(rec['empty'],rec['canonical_length']['empty'])
        if rec['empty']:
            answer = self.recorded(rec['zero'],lambda:self.add(0,0))
            self.empty_progressions += 1
        else:
            difference = self.recorded(rec['junction_minus_head'],lambda:self.sub(U,b))
            selection = rec['q_selection']
            if difference < 0:
                assert selection['route'] == 'HEAD_ABOVE_JUNCTION'
                q = self.recorded(selection['selected'],lambda:self.add(0,0))
            else:
                assert selection['route'] == 'TYPED_MIN_WITH_N'
                quotient,_ = self.division(selection['division'],difference,step)
                candidate = self.recorded(selection['candidate'],lambda:self.add(quotient,1))
                excess = self.recorded(selection['candidate_minus_n'],lambda:self.sub(candidate,n))
                choice = n if excess > 0 else candidate
                assert selection['selected_source'] == ('n' if excess > 0 else 'candidate')
                q = self.recorded(selection['selected'],lambda:self.add(choice,0))
            same(q,rec['q'])
            Tn,Tq = self.affine_T(rec['Tn'],n,b,step),self.affine_T(rec['Tq'],q,b,step)
            twice = self.recorded(rec['twice_q'],lambda:self.add(q,q))
            count = self.recorded(rec['signed_count'],lambda:self.sub(twice,n))
            mass = self.recorded(rec['mass_term'],lambda:self.mul(M,count))
            four = self.recorded(rec['four_Tq'],lambda:self.mul(4,Tq))
            answer = self.recorded(rec['sumA'],lambda:self.sub(self.add(mass,Tn),four))
        same(answer,rec['value'])
        assert rec['signed_operations_stop'] == self.i
        return answer

    def branch(self, branch, label, head, step, expected, req, remainder):
        shift = branch['shifted']
        if remainder:
            assert shift['execution'] == 'EVALUATED' and branch['progression_calls'] == 2
            return super().branch(branch,label,head,step,expected,req,remainder)
        assert branch['label'] == label and branch['signed_operations_start'] == self.i
        same([branch['head'],branch['step'],branch['expected_n']],[head,step,expected])
        _,parity = self.division(branch['parity'],head['value'],2)
        assert parity in (0,1)
        sign = -1 if parity else 1
        same(sign,branch['sign'])
        small = {'inputs':{'R':step},'L':req['M'],'U':req['U'],'P':req['P'],'coefficients':req['coefficients']}
        answer0 = self.progression(branch['original'],head,label+':original',small)
        assert self.recorded(branch['canonical_count_difference'],
            lambda:self.sub(branch['original']['n'],expected['value'])) == 0
        same(branch['shifted_weight'],0)
        same(shift,{'execution':'OMITTED_ZERO_COEFFICIENT','observed_coefficient':0,
            'arithmetic_executed':False,'progression_called':False,
            'identity':'A_two(V*z)=(-1)^z*V*A_one(z); omitted sum not evaluated'})
        first = self.recorded(branch['original_product'],lambda:self.mul(req['V'],answer0))
        answer = self.recorded(branch['signed_result'],lambda:self.mul(sign,first))
        same(answer,branch['value'])
        assert branch['progression_calls'] == 1 and branch['sign_is_original_z_not_shifted_z'] is True
        assert branch['signed_operations_stop'] == self.i
        return answer

def inspect_certificate(cert,native):
    assert cert['schema'] == SCHEMA and cert['source_sha256'] == SOURCE_PINS['shortcut_two_bit.py']
    for key,(_,pin) in DEPENDENCIES.items():
        assert cert[key] == pin
    e = cert['actual_integer_evidence']
    result = old.inspect_evidence(e,native)
    c = Cursor(e)
    for index,req in enumerate(cert['requests']):
        inp = req['inputs']
        assert all(type(v) is int for v in inp.values())
        assert set(inp) == {'g','ell','k','R','r','stride'}
        assert inp['g'] >= 2 and 0 <= inp['ell'] < inp['k'] < inp['g']
        assert inp['R'] >= 1 and inp['r'] == index and inp['stride'] == 1
        assert req['signed_operations_start'] == c.i
        assert req['raw_denominator_exponent'] == 2*inp['g']
        assert req['negative_values_are_valid'] is True and req['compressed_length_is_not_normalization'] is True
        c.power(inp['ell'],req['V'])
        h,rem = c.division(req['alignment'],inp['R'],req['V'])
        assert rem == 0 and req['alignment_checked_before_zero_test'] is True
        c.power(inp['k'],req['original_highest_U'])
        _,zero_rem = c.division(req['zero_test'],req['original_highest_U'],inp['R'])
        if zero_rem == 0:
            assert req['route'] == 'RESIDUE_HISTOGRAM_CANCELLATION'
            assert req['orientations_evaluated'] is False and req['orientations'] == []
            same(c.recorded(req['zero'],lambda:c.add(0,0)),req['value'])
            assert req['value'] == 0
            for key in ('single_progression_calls','top_level_table_calls','affine_progression_calls',
                        'moment_progression_calls','omitted_shifted_progressions'):
                assert req[key] == 0
        else:
            same(h,req['h'])
            c.division(req['h_parity'],h,2)
            c.power(inp['g']-inp['ell'],req['M'])
            U,urem = c.division(req['compressed_U'],req['original_highest_U'],req['V'])
            same(U,req['U']); assert urem == 0
            same(c.add(U,U),req['P'])
            c.power(inp['g']-inp['k']-1,req['H'])
            same(c.mul(req['V'],req['M']),req['L'])
            assert req['scales_operations_stop'] == c.i
            if inp['k'] == inp['g']-1:
                assert req['route'] == 'HIGHEST_BIT_AFFINE'
                assert req['coefficients'] is None and req['coefficient_helpers'] is None
            else:
                assert req['route'] == 'DIRECT_MOMENT_FALLBACK'
                c.coefficients(req)
            assert req['orientations_evaluated'] is True and len(req['orientations']) == 2
            pos,neg = req['orientations']
            c.recorded(pos['head'],lambda:c.add(inp['r'],0))
            c.recorded(neg['head'],lambda:c.sub(inp['R'],inp['r']))
            p = c.orientation(pos,'nonnegative_difference',req)
            n = c.orientation(neg,'negative_difference_magnitude',req)
            answer = c.recorded(req['final_addition'],lambda:c.add(p,n))
            same(answer,req['value'])
            branches = [b for o in req['orientations'] for b in o['branches']]
            progressions = [b['original'] for b in branches]
            progressions += [b['shifted'] for b in branches if b['shifted']['execution']=='EVALUATED']
            assert req['single_progression_calls'] == len(progressions) <= 8
            assert req['top_level_table_calls'] == sum(len(p['table_calls']) for p in progressions) <= 16
            assert req['affine_progression_calls'] == sum(p['strategy']=='HIGHEST_BIT_AFFINE' for p in progressions)
            assert req['moment_progression_calls'] == sum(p['strategy']=='FROZEN_DIRECT_MOMENTS' for p in progressions)
            assert req['omitted_shifted_progressions'] == sum(b['shifted']['execution']=='OMITTED_ZERO_COEFFICIENT' for b in branches)
        assert req['signed_operations_stop'] == c.i
    assert c.i == len(c.ops)
    result.update(requests=len(cert['requests']),top_level_tables=c.seen_tables,empty_progressions=c.empty_progressions)
    return result

def inspect_partial(cert,native):
    assert cert['schema'] == 'INCOMPLETE_'+SCHEMA and cert['complete_certificate'] is False
    assert cert['source_sha256'] == SOURCE_PINS['shortcut_two_bit.py'] and cert['requests'] == []
    e,req = cert['actual_integer_evidence'],cert['inflight_request']
    result = old.inspect_evidence(e,native,partial=True)
    assert e['moment_nodes'] == [] and req['signed_operations_start'] == 0
    assert 'zero_test' not in req
    c = Cursor(e)
    c.power(req['inputs']['ell'],req['V'])
    _,rem = c.division(req['alignment'],req['inputs']['R'],req['V'])
    assert rem > 0 and c.i == len(c.ops)
    result['paid_unaligned_rejection_before_zero_test'] = True
    return result

def coverage(certs):
    requests = [r for c in certs for r in c['requests']]
    branches = [b for r in requests for o in r['orientations'] for b in o['branches']]
    progressions = [b['original'] for b in branches]
    progressions += [b['shifted'] for b in branches if b['shifted']['execution']=='EVALUATED']
    affine = [p for p in progressions if p['strategy']=='HIGHEST_BIT_AFFINE']
    half = certs[4]['requests'][3]['orientations']
    assert len(half)==2 and half[0]['head']['value']==half[1]['head']['value']
    assert any(r['value']<0 for r in requests)
    assert any(o['empty'] for r in requests for o in r['orientations']) and any(p['empty'] for p in affine)
    assert any(p.get('q')==0 for p in affine if not p['empty'])
    assert any(p.get('q')==p['n'] for p in affine if not p['empty'])
    assert any(p.get('junction_minus_head',{}).get('value')==0 for p in affine)
    assert any(b.get('shifted_zero_tail',{}).get('removed_zero_terms')==1 for b in branches)
    return {'requests':len(requests),'route_counts':dict(Counter(r['route'] for r in requests)),
        'private_progressions':len(progressions),
        'omitted_shifted_progressions':sum(b['shifted']['execution']=='OMITTED_ZERO_COEFFICIENT' for b in branches),
        'affine_progressions':len(affine),'moment_progressions':len(progressions)-len(affine),
        'top_level_tables':sum(len(p['table_calls']) for p in progressions),
        'negative_output_seen':True,'empty_orientation_and_affine_progression_seen':True,
        'affine_q_zero_full_and_junction_seen':True,'nonzero_shifted_M_tail_seen':True,
        'half_modulus_multiplicity_preserved':True}

def main():
    data,summary = io.load(ROOT,'SHORTCUT',RAW_PIN,GZIP_PIN)
    same(data['source_sha256'],SOURCE_PINS)
    assert summary['raw_bytes']==57941257 and summary['gzip_bytes']==2027431
    history,hs = io.load(old.ROOT,'TWO_BIT_ALIGNED',old.RAW_PIN,old.GZIP_PIN)
    same(history['source_sha256'],old.SOURCE_PINS)
    same(data['history'],summary['history'])
    same(data['history']['source_sha256'],old.SOURCE_PINS)
    for key,value in [('payload_sha256',old.RAW_PIN),('artifact_sha256',old.GZIP_PIN),
                      ('raw_bytes',hs['raw_bytes']),('gzip_bytes',hs['gzip_bytes'])]:
        same(data['history'][key],value)
    assert data['history']['whole_payload_read_and_hash_checked'] is True
    for k in ('historical_production_reexecuted','historical_pair_comparator_reexecuted','historical_fresh_replay_reexecuted'):
        assert data['history'][k] is False
    oldguard = (old.ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(oldguard)==data['history']['guard_sha256']==history['startup_guard']['sha256']
    same(json.loads(oldguard),history['startup_guard']['receipt'])
    for _,(rel,pin) in DEPENDENCIES.items():
        assert digest((ROOT.parent/rel).read_bytes()) == pin
    guardbytes = (ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guardbytes)==GUARD_PIN==data['startup_guard']['sha256']
    same(json.loads(guardbytes),data['startup_guard']['receipt'])
    guard=data['startup_guard']['receipt']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC'
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    assert native['native_adder']['input_columns']==8 and native['native_adder']['positive_BRC_input_states']==12
    for name,rel in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
                     'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
                     'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/rel).read_bytes())==native['files_sha256'][name]
    groups={k:[] for k in ('production','positive_replay','paid_input_rejection','negative_replay')}
    reviewed=[]; certs=[]; pair_count=0
    for index,case in enumerate(data['cases']):
        prior=history['cases'][index]
        same([case['inputs'][k] for k in ('g','ell','k','R')],old.CASES[index])
        same(case['inputs'],prior['inputs'])
        cert,verification=case['certificate'],case['verification']
        replay=verification['replay_certificate']
        assert case['all_historical_residues_equal'] is True and verification['verified'] is True
        assert verification['requests_replayed']==len(cert['requests'])
        assert io.semantic(cert)==io.semantic(replay)
        same(case['values'],prior['values']); same(case['values'],[r['value'] for r in cert['requests']])
        assert io.semantic(prior['certificate'])==io.semantic(prior['verification']['replay_certificate'])
        ref=case['history_reference']
        assert ref['case_index']==index and ref['certificate_pointer']==f'cases/{index}/certificate'
        same(ref['values'],prior['values'])
        same(ref['historical_production_cost'],prior['production_cost'])
        same(ref['historical_comparator_cost'],prior['typed_enumeration_cost'])
        assert ref['historical_pairs_read']==len(prior['typed_enumeration']['pair_observations'])
        assert ref['historical_pair_comparator_reexecuted'] is False
        pair_count+=ref['historical_pairs_read']
        same(prior['certificate']['actual_integer_evidence']['native_source'],native)
        reviewed.append({'inputs':case['inputs'],'values':case['values'],
            'production':inspect_certificate(cert,native),'positive_replay':inspect_certificate(replay,native),
            'history_reference':ref})
        certs.append(cert)
        groups['production'].append(cert['actual_integer_evidence'])
        groups['positive_replay'].append(replay['actual_integer_evidence'])
    assert len(reviewed)==6 and pair_count==720 and sum(len(c['requests']) for c in certs)==36
    measured_coverage=coverage(certs)
    same(measured_coverage,data['coverage']); same(measured_coverage,summary['coverage'])
    inputs=[]
    for r in data['input_rejections']:
        assert r['rejected'] is True
        if r['kind']=='ordinary_pre_rejection':
            assert r['actual_typed_operations']==0 and 'incomplete_receipt' not in r
            assert r['call_interval']['start']==r['call_interval']['stop']
            result={'kind':r['kind'],'no_work_recorded':True}
        else:
            assert r['kind']=='paid_unaligned_rejection'
            result=inspect_partial(r['incomplete_receipt'],native)
            groups['paid_input_rejection'].append(r['incomplete_receipt']['actual_integer_evidence'])
            reuse=r['reuse_rejection']
            assert reuse['rejected'] is True and reuse['prior_inflight_and_all_evidence_unchanged'] is True
            assert reuse['additional_typed_operations']==0 and reuse['call_interval']['start']==reuse['call_interval']['stop']
            result['reuse_negative']=reuse
        result.update(args=r['args'],error=r['error']); inputs.append(result)
    assert len(inputs)==12 and len(groups['paid_input_rejection'])==2
    expected=['zero_divisibility_reason','zero_route_output','drop_half_modulus_orientation','omitted_shifted_coefficient',
        'affine_canonical_length','affine_typed_min_selection','affine_exact_half','shifted_zero_tail','original_branch_sign',
        'fallback_table_offset','signed_output','unaligned_input_paid_partial','source_early','schema_early','bool_input_early','nonstring_key_early']
    same([r['name'] for r in data['negative_checks']],expected)
    negatives=[]
    for r in data['negative_checks']:
        assert r['rejected'] is True
        attempted=old.decode_keys(r['attempted_certificate_typed_key_encoding'])
        capture=r['actual_replay_certificates']
        if r['name'].endswith('_early'):
            assert capture==[] and r['call_interval']['start']==r['call_interval']['stop']
            result={'type':'early','paid_receipts':0}
        else:
            assert len(capture)==1
            replay=capture[0]
            groups['negative_replay'].append(replay['actual_integer_evidence'])
            if r['name']=='unaligned_input_paid_partial':
                result=inspect_partial(replay,native)
                same(replay['inflight_request']['inputs'],attempted['requests'][0]['inputs'])
                result['type']='paid_partial'
            else:
                assert io.semantic(replay)==io.semantic(certs[r['source_case_index']])
                assert io.semantic(replay)!=io.semantic(attempted)
                result=inspect_certificate(replay,native); result['type']='paid_full'
            result['paid_receipts']=1
        result.update(name=r['name'],error=r['error']); negatives.append(result)
    assert Counter(r['type'] for r in negatives)=={'early':4,'paid_full':11,'paid_partial':1}
    calculated={k:old.costs(es) for k,es in groups.items()}
    same(calculated,data['cost_categories']); same(calculated,summary['cost_categories'])
    assert sum(len(es) for es in groups.values())==26
    calls=Counter(); frontier=0
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        calls[row['category']]+=row['stop']-row['start']; frontier=row['stop']
    same(dict(calls),data['native_calls_by_category']); same(data['call_intervals'],summary['call_intervals'])
    assert frontier==len(data['actual_core_calls'])==data['actual_core_call_count']==1
    assert data['actual_core_calls'][0]['states']==12
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for es in groups.values() for e in es)==1
    totals={k:sum(row['sum'][k] for row in calculated.values()) for k in calculated['production']['sum']}
    assert totals['adder_digit_replays']==186710
    percase=[]
    for index,(case,prior) in enumerate(zip(data['cases'],history['cases'])):
        new=case['production_cost']['arithmetic_stats']['adder_digit_replays']
        same(case['production_cost']['arithmetic_stats'],groups['production'][index]['arithmetic_stats'])
        before=prior['production_cost']['arithmetic_stats']['adder_digit_replays']
        brute=prior['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays']
        percase.append({'inputs':case['inputs'],'new_production_digits':new,'historical_production_digits':before,
            'historical_comparator_digits':brute,'production_decrease_digits':before-new,
            'new_below_historical_comparator':new<brute})
    same([p['new_production_digits'] for p in percase],[16,11894,78,204,8065,17246])
    historical_total=sum(p['historical_production_digits'] for p in percase)
    historical_brute=sum(p['historical_comparator_digits'] for p in percase)
    new_total=calculated['production']['sum']['adder_digit_replays']
    result={'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW','reader_sha256':digest(Path(__file__).read_bytes()),
        'scope':'Shared-context stdlib I/O peer review; no scientific import, arithmetic evaluation or rerun',
        'pure_io_helpers':{'aligned':HELPER_PIN,'direct':old.HELPER_PIN},'source_sha256':SOURCE_PINS,
        'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':summary['raw_bytes'],'gzip_bytes':summary['gzip_bytes'],
        'startup_guard_sha256':GUARD_PIN,'native_source':native,'history':data['history'],
        'cases':reviewed,'coverage':measured_coverage,'input_rejections':inputs,'negative_checks':negatives,
        'charged_streams':26,'cost_categories':calculated,'total_current_run_cost':totals,
        'native_calls_by_category':dict(calls),'actual_core_calls':data['actual_core_calls'],
        'per_case_comparison':percase,'production_comparison':{'old':historical_total,'new':new_total,
            'decrease_numerator':historical_total-new_total,'decrease_denominator':historical_total,
            'decrease_percent_metadata':100*(historical_total-new_total)/historical_total,
            'historical_comparator_total':historical_brute,
            'cases_below_historical_comparator':sum(p['new_below_historical_comparator'] for p in percase)},
        'elapsed_seconds_before_serialization':summary['elapsed_seconds_before_serialization'],
        'unexpected_failure_artifact_present':(ROOT/'SHORTCUT_FAILED_EXECUTION.json.gz').exists(),
        'scientific_execution_performed':False,'comparison_is_timing_benchmark':False,
        'limits':['All native cell links use saved source-bound primitive columns; no arithmetic is scientifically recomputed.',
            'Moment node/child/cache and table outputs are linked to fresh replay, not evaluated anew.',
            'No-work reuse equality is an executed checker assertion plus original retained snapshot, not a second saved after-snapshot.',
            'The six tuples do not re-exercise surviving even-step propagation after failed cancellation.',
            'Historical pair records are read only and excluded from new costs; elapsed times are unmatched.',
            'Host cost counters exclude serialization, dictionary/index work and other uninstrumented overhead.']}
    out=Path(__file__).parent/'SHORTCUT_RECORD_REVIEW.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'total':totals,'comparison':result['production_comparison'],'sha256':digest(out.read_bytes())}))

if __name__=='__main__':
    main()
