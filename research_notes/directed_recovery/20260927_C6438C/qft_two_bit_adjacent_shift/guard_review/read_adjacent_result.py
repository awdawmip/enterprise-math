"""Complete saved-record review, stdlib I/O only; no scientific executor import.

Arithmetic cursor methods consume recorded outputs and check their input and
range links. They do not evaluate the observed integer arithmetic again.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import gzip,hashlib,importlib.util,json

ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'sep27-qft-two-bit-top-general/read_top_general_cost.py'
HELPER_PIN='a96696eb187d6c6251934f9b1651f5abc1b8d2db5a5357ea051960b8e4489f5a'
RAW_PIN='a084a16fa26a9a2143729620ba3f2fdc1331579ae16087a5f3ddcce199a96d82'
GZIP_PIN='385295e9a5581ce762761f24d0d5c25e32f9bc06d645f32fbaecbdffd75b8294'
SOURCE_PIN='bee8a702062dfb16a75139a63b6c52b9451a02834a5b3033f5d52fcaebff9c6e'
PROOF_PIN='96757c3624c69bf3ec1e313504f56bb6099d1a79e47032813084b19340c272ad'
CASES=((3,0,1,5),(4,0,1,5),(4,1,2,6),(4,1,2,9),(3,0,1,11),(4,0,1,1))

def digest(data):return hashlib.sha256(data).hexdigest()
assert digest(HELPER.read_bytes())==HELPER_PIN
spec=importlib.util.spec_from_file_location('adjacent_saved_io',HELPER)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
same=old.same


class Cursor(old.RecordedCursor):
    def power(self,exponent):
        value=1
        for _ in range(exponent):value=self.add(value,value)
        return value

    def coefficients(self,req,H,P):
        h=req['coefficient_helpers'];c=req['coefficients']
        f=self.recorded(h['four_H'],lambda:self.mul(4,H))
        e=self.recorded(h['eight_H'],lambda:self.mul(8,H))
        operations={
            'n':lambda:self.mul(H,P),'q':lambda:self.mul(self.sub(f,2),P),
            'dq':lambda:self.add(4,0),'q2':lambda:self.mul(-4,P),
            'd':lambda:self.sub(1,f),'ddelta':lambda:self.sub(e,4),
            'dqdelta':lambda:self.add(-8,0),'q2delta':lambda:self.mul(8,P),
            'qdelta':lambda:self.mul(self.sub(8,e),P),
            'delta':lambda:self.mul(self.sub(2,f),P)}
        assert set(c)==set(operations)
        for k,op in operations.items():self.recorded(c[k],op)

    def adjacent_progression(self,rec,head,orientation,req):
        assert rec['signed_operations_start']==self.i
        assert rec['orientation']==orientation and rec['multiplicity']==1
        base=rec['single_bit_progression']
        result=self.progression(base,head,orientation,req)
        same([rec['empty'],rec['n']],[base['empty'],base['n']])
        if rec['empty']:
            assert rec['correction'] is None
            same(result,rec['value'])
            assert rec['signed_operations_stop']==self.i
            return result
        c=rec['correction'];assert c['signed_operations_start']==self.i
        b,n,R,P,V=head['value'],rec['n'],req['inputs']['R'],req['P'],req['V']
        coefficients=req['correction_coefficients']
        a_offset=self.recorded(c['offsets'][0],lambda:self.add(b,coefficients['threeV']['value']))
        a=self.table(c['table_calls'][0],n,P,R,a_offset)
        b_offset=self.recorded(c['offsets'][1],lambda:self.add(b,V))
        z=self.table(c['table_calls'][1],n,P,R,b_offset)
        da=self.recorded(c['weighted_floors'][0],lambda:self.add(self.mul(b,a['0,1']),self.mul(R,a['1,1'])))
        db=self.recorded(c['weighted_floors'][1],lambda:self.add(self.mul(b,z['0,1']),self.mul(R,z['1,1'])))
        sd=base['weighted_sums']['d']['value'];same(c['reused_single_bit_displacement_sum'],sd)
        operations={
            'linear_d':lambda:self.mul(-2,sd),
            'weighted_floor_difference':lambda:self.mul(4,self.sub(da,db)),
            'floor_sum':lambda:self.mul(coefficients['fourV']['value'],self.add(a['0,1'],z['0,1'])),
            'floor_square_difference':lambda:self.mul(coefficients['eightV']['value'],self.sub(z['0,2'],a['0,2']))}
        assert set(c['terms'])==set(operations)
        terms=[self.recorded(c['terms'][k],op) for k,op in operations.items()]
        correction=self.recorded(c['sum'],lambda:self.total(terms))
        assert c['signed_operations_stop']==self.i
        answer=self.recorded(rec['combined'],lambda:self.add(result,correction))
        same(answer,rec['value']);assert rec['signed_operations_stop']==self.i
        return answer

    def requests(self,cert):
        for req in cert['requests']:
            i=req['inputs'];g,ell,k,R,r=[i[key] for key in ('g','ell','k','R','r')]
            assert all(type(x) is int for x in (g,ell,k,R,r,i['stride']))
            assert g>=2 and 0<=ell and k==ell+1 and k<g and R>=1 and 0<=r<R and i['stride']==1
            assert req['signed_operations_start']==req['scales_operations_start']==self.i
            V=self.power(ell);U=self.add(V,V);P=self.add(U,U);H=self.power(g-k-1);L=self.mul(H,P)
            same([V,U,P,H,L],[req[key] for key in ('V','U','P','H','L')])
            assert req['scales_operations_stop']==self.i
            self.coefficients(req,H,P)
            cc=req['correction_coefficients']
            self.recorded(cc['threeV'],lambda:self.add(U,V))
            self.recorded(cc['fourV'],lambda:self.mul(4,V))
            self.recorded(cc['eightV'],lambda:self.mul(8,V))
            assert len(req['progressions'])==2
            answers=[]
            for j,orientation in enumerate(('nonnegative_difference','negative_difference_magnitude')):
                rec=req['progressions'][j];head=rec['single_bit_progression']['head']
                self.recorded(head,(lambda:self.add(r,0)) if j==0 else (lambda:self.sub(R,r)))
                answers.append(self.adjacent_progression(rec,head,orientation,req))
            answer=self.recorded(req['final_addition'],lambda:self.add(*answers))
            same(answer,req['value']);assert req['signed_operations_stop']==self.i
            assert req['complete'] is True and req['negative_values_are_valid'] is True
            assert req['raw_denominator_exponent']==2*g
        assert self.i==len(self.ops)


def source_pins(cert):
    paths={'source_sha256':ROOT/'adjacent_shift.py','adjacent_proof_sha256':ROOT/'ADJACENT_SHIFT_REDUCTION.md',
        'direct_source_sha256':ROOT.parent/'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
        'direct_proof_sha256':ROOT.parent/'sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md',
        'baseline_helper_source_sha256':ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py',
        'floor_moment_source_sha256':ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py'}
    for key,path in paths.items():assert digest(path.read_bytes())==cert[key]
    return {key:{'path':str(path),'sha256':cert[key]} for key,path in paths.items()}


def inspect(cert,native,partial=False):
    assert cert['source_sha256']==SOURCE_PIN
    if partial:
        assert cert['complete_certificate'] is False and cert['inflight'] is None and cert['failed'] is False
        assert cert['schema']=='INCOMPLETE_BRC_ADJACENT_BITS_SHIFTED_SINGLE_BIT_V1'
    else:
        assert cert['schema']=='BRC_ADJACENT_BITS_SHIFTED_SINGLE_BIT_V1'
        source_pins(cert)
    e=cert['actual_integer_evidence'];old.inspect_evidence(e,native)
    cursor=Cursor(e);cursor.requests(cert)
    return {'tables':cursor.seen_tables,'empty_orientations':cursor.empty_progressions}


def main():
    target=ROOT/'guard_review/ADJACENT_RECORD_REVIEW.json'
    if target.exists():raise FileExistsError('frozen review already exists')
    compressed=(ROOT/'ADJACENT_SHIFT_RESULTS.json.gz').read_bytes();raw=gzip.decompress(compressed)
    assert digest(raw)==RAW_PIN and digest(compressed)==GZIP_PIN
    data=json.loads(raw);summary=json.loads((ROOT/'ADJACENT_SHIFT_SUMMARY.json').read_bytes())
    assert data['status']==summary['status']=='PASS'
    assert summary['payload_sha256']==RAW_PIN and summary['artifact_sha256']==GZIP_PIN
    assert len(raw)==summary['raw_bytes'] and len(compressed)==summary['gzip_bytes']
    same(data['source_sha256'],summary['source_sha256'])
    for name,pin in data['source_sha256'].items():assert digest((ROOT/name).read_bytes())==pin
    assert data['source_sha256']['adjacent_shift.py']==SOURCE_PIN and data['proof_sha256']==PROOF_PIN
    guardraw=(ROOT/'STARTUP_GUARD.json').read_bytes();guard=json.loads(guardraw)
    same(guard,data['startup_guard']['receipt']);assert digest(guardraw)==data['startup_guard']['sha256']
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['boundary']=='startup'
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    for key,path in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/path).read_bytes())==native['files_sha256'][key]
    groups={k:[] for k in ('production','typed_pair_comparator','positive_replay','negative_replay')}
    rows=[];pairs=0;tables=0;empty=0
    for case,inputs in zip(data['cases'],CASES):
        same(case['inputs'],dict(zip(('g','ell','k','R'),inputs)))
        cert=case['certificate'];replay=case['verification']['replay_certificate']
        assert old.semantic(cert)==old.semantic(replay)
        assert case['all_residues_equal'] is True and case['verification']['verified'] is True
        assert case['verification']['requests_replayed']==len(cert['requests'])==inputs[-1]
        same([r['inputs']['r'] for r in cert['requests']],list(range(inputs[-1])))
        same(case['values'],[r['value'] for r in cert['requests']])
        for item,category,field in ((cert,'production','production_cost'),(replay,'positive_replay','positive_replay_cost')):
            links=inspect(item,native);groups[category].append(item['actual_integer_evidence'])
            same(old.cost_record(item['actual_integer_evidence']),case[field])
            if category=='production':tables+=links['tables'];empty+=links['empty_orientations']
        brute=case['typed_enumeration'];old.inspect_evidence(brute['actual_integer_evidence'],native)
        values,count=old.inspect_pairs(brute,case['inputs']);same(values,case['values']);pairs+=count
        groups['typed_pair_comparator'].append(brute['actual_integer_evidence'])
        same(old.cost_record(brute['actual_integer_evidence']),case['typed_enumeration_cost'])
        rows.append({'inputs':case['inputs'],'values':values,'typed_pairs':count,
            'production_digits':case['production_cost']['arithmetic_stats']['adder_digit_replays'],
            'comparator_digits':case['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays']})
    assert len(data['cases'])==6 and pairs==1152 and sum(len(r['values']) for r in rows)==37
    assert tables==data['coverage']['top_level_table_calls']==268
    same(data['coverage'],summary['coverage'])
    boundary=data['production_boundary_rejection'];same(boundary['before'],boundary['after'])
    assert boundary['rejected'] is True and boundary['reuse_completed_by_original_grid'] is True
    assert boundary['additional_typed_operations']==boundary['additional_native_calls']==0
    inspect(boundary['before'],native,True)
    same(boundary['before']['requests'],data['cases'][0]['certificate']['requests'][:1])
    negatives=[];kinds=Counter()
    for row in data['negative_checks']:
        assert row['rejected'] is True
        original=data['cases'][row['source_case_index']]['certificate']
        attempted=old.decode_keys(row['attempted_certificate_typed_key_encoding'])
        assert old.canonical(row['attempted_certificate_typed_key_encoding'])!=old.canonical(old.encode_keys(original))
        captures=row['actual_replay_certificates'];kinds[row['kind']]+=1
        if row['name'].endswith('_early'):
            assert not captures and row['call_interval']['start']==row['call_interval']['stop']
        else:
            assert len(captures)==1
            capture=captures[0]
            if row['name']=='valid_prefix_then_invalid_nonadjacent':
                inspect(capture,native,True);same(capture['requests'],original['requests'][:1])
                assert attempted['requests'][1]['inputs']['ell']==1
            else:
                assert old.semantic(capture)==old.semantic(original);inspect(capture,native)
            groups['negative_replay'].append(capture['actual_integer_evidence'])
        negatives.append({'name':row['name'],'kind':row['kind'],'error':row['error'],
            'digits':sum(c['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'] for c in captures)})
    assert len(negatives)==14 and len(groups['negative_replay'])==10
    same(dict(kinds),summary['negative_kinds'])
    assert len(data['input_rejections'])==12
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations']==0
        assert row['call_interval']['start']==row['call_interval']['stop']
    costs={k:old.costs(v) for k,v in groups.items()}
    same(costs,data['cost_categories']);same(costs,summary['cost_categories'])
    frontier=0;native_by=Counter()
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        native_by[row['category']]+=row['stop']-row['start'];frontier=row['stop']
    assert frontier==len(data['actual_core_calls'])==summary['actual_core_call_count']==1
    same(dict(native_by),data['native_calls_by_category']);same(dict(native_by),summary['native_calls_by_category'])
    same(data['call_intervals'],summary['call_intervals'])
    call=data['actual_core_calls'][0]
    assert call['entrypoint']=='recurrent_mass_power' and call['states']==12 and call['depth']==1
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for v in groups.values() for e in v)==1
    lograw=(ROOT/'run.log').read_bytes()
    log=[json.loads(x) for x in lograw.decode('utf-8-sig').splitlines() if x.strip().startswith('{')]
    same(log[-1],summary);assert sum(x.get('stage')=='CASE_COMPLETE' for x in log)==6
    total=sum(c['sum']['adder_digit_replays'] for c in costs.values())
    result={'status':'PASS_COMPLETE_SAVED_RECORD_REVIEW','scientific_execution_performed':False,
        'reader_sha256':digest(Path(__file__).read_bytes()),'helper_sha256':HELPER_PIN,
        'source_sha256':data['source_sha256'],'source_dependencies':source_pins(data['cases'][0]['certificate']),
        'raw_bytes':len(raw),'gzip_bytes':len(compressed),'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,
        'summary_sha256':digest((ROOT/'ADJACENT_SHIFT_SUMMARY.json').read_bytes()),'log_sha256':digest(lograw),
        'startup_guard_sha256':digest(guardraw),'cases':rows,'moment_tables':tables,'empty_orientations':empty,
        'typed_pairs':pairs,'negative_controls':negatives,'cost_categories':costs,
        'all_charged_streams':sum(len(v) for v in groups.values()),'total_adder_digits':total,
        'native_source':native,'actual_core_calls':data['actual_core_calls'],
        'failure_artifact_present':(ROOT/'ADJACENT_SHIFT_FAILED_EXECUTION.json.gz').exists(),
        'scope':'All saved outer formula links, moment-node/cache references, signed-typed links, native cells, 1152 pair updates, full/partial replays and costs; no numerical answer recomputation',
        'limits':'Shared context, not formal admission; bounded small fixtures, not a matched timing or Shor completion'}
    with target.open('x',encoding='utf-8') as f:f.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'reader_sha256':result['reader_sha256'],
        'record_sha256':digest(target.read_bytes()),'streams':result['all_charged_streams'],
        'total_adder_digits':total,'tables':tables,'cases':rows}))

if __name__=='__main__':main()
