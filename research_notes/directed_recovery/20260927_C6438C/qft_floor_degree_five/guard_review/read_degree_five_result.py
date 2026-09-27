"""Independent stdlib-only readback of complete saved degree-five evidence.
All arithmetic cursor methods consume recorded outputs; none evaluates a
scientific expression or imports an arithmetic/science module.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import ast, gzip, hashlib, importlib.util, json
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT.parent/'sep27-qft-two-bit-top-general/read_top_general_cost.py'
HELPER_PIN='a96696eb187d6c6251934f9b1651f5abc1b8d2db5a5357ea051960b8e4489f5a'
RAW_PIN='da675f8e04929116dac64552775f85ad75d39c71a03f78aad7c45d571fdf267e'
GZIP_PIN='b044570bb55e81ea0ff1fe73ef35af6fa7438281c2d6dac87c1c31f3ee251c9f'
PINS={'typed_floor_degree_five.py':'755fcaf04832a5328e2464214f736ac661c410b3505edf10ab5218f935e2a7c7',
'check_degree_five.py':'975b574b85a3531da4443bf9f70cd4644ccc4ceadec81359506a2d00da3b1223',
'DESIGN.md':'f6eb1b1e7b7dece0956e2ead166fbb9e901be3f5c9a44a1b367d1130206b7c22',
'DEGREE_FIVE_RECIPROCITY.md':'1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6'}
PATHS={'base_arithmetic':'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}
DEGREES=tuple((p,e) for e in range(6) for p in range(6-e))
CASES=((0,5,3,1),(1,7,-3,-2),(4,5,0,3),(5,7,2,1),(6,5,13,-4),(7,4,-3,9),(8,9,7,-11),(9,7,0,21),(4,1,-2,3))
def sha(raw):return hashlib.sha256(raw).hexdigest()
assert sha(HELPER.read_bytes())==HELPER_PIN
spec=importlib.util.spec_from_file_location('frozen_stdlib_readback_helpers',HELPER)
io=importlib.util.module_from_spec(spec);spec.loader.exec_module(io)
same=io.same
# Read only literal fixed coefficient arrays; do not import the scientific source.
tree=ast.parse((ROOT/'typed_floor_degree_five.py').read_text(encoding='utf-8-sig'))
constants={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign)
    and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('BINOMIAL','POWER_SUMS')}
BINOMIAL,POWER_SUMS=constants['BINOMIAL'],constants['POWER_SUMS']

class Cursor:
    def __init__(self,e):
        self.e=e;self.ops=e['signed_operations'];self.i=0;self.nodes=e['moment_nodes']
        self.node_i=0;self.cache={};self.requests=0;self.hits=0;self.depth=0
    def take(self,kind,args):
        row=self.ops[self.i];assert row['operation']==kind;same(row['inputs'],args)
        self.i+=1;return row['result']
    def add(self,a,b):return self.take('signed_add',[a,b])
    def sub(self,a,b):return self.take('signed_add',[a,-b])
    def mul(self,a,b):return self.take('signed_multiply',[a,b])
    def div(self,a,b):return self.take('signed_euclidean_division',[a,b])
    def exact(self,a,b):
        q,r=self.div(a,b);assert r==0;return q
    def total(self,terms):
        out=0
        for term in terms:out=self.add(out,term)
        return out
    def power(self,a,e):
        out=1
        for _ in range(e):out=self.mul(out,a)
        return out
    def power_sums(self,n):
        if not n:return (0,0,0,0,0,0)
        powers=[1,n]
        for _ in range(2,7):powers.append(self.mul(powers[-1],n))
        out=[]
        for den,terms in POWER_SUMS:
            num=self.total(self.mul(coeff,powers[exponent]) for exponent,coeff in terms)
            out.append(self.exact(num,den))
        return tuple(out)
    def moment(self,n,m,a,b,depth=0):
        self.requests+=1;self.depth=max(self.depth,depth)
        key=n,m,a,b
        if key in self.cache:self.hits+=1;return self.cache[key]
        start=self.i;sums=self.power_sums(n)
        out={(p,e):sums[p] if e==0 else 0 for p,e in DEGREES}
        branch,child='empty',None
        details={'maximum_total_degree':5,'normalization':None,'height':None,
                 'zero_coefficient_omissions':[],'reconstruction':[]}
        if n:
            ns=self.i;A,a0=self.div(a,m);B,b0=self.div(b,m)
            details['normalization']={'A':A,'a0':a0,'B':B,'b0':b0,
                'signed_operations_start':ns,'signed_operations_stop':self.i}
            if A or B:
                branch,child='normalize_signed_coefficients',(n,m,a0,b0)
                low=self.moment(*child,depth+1)
                for p,e in DEGREES:
                    if not e:continue
                    st=self.i;terms=[]
                    for k in range(e+1):
                        for l in range(e-k+1):
                            if (A==0 and l>0) or (B==0 and e-k-l>0):
                                details['zero_coefficient_omissions'].append({'p':p,'e':e,'k':k,'l':l,'A_zero':A==0,'B_zero':B==0});continue
                            coefficient=self.mul(BINOMIAL[e][k],BINOMIAL[e-k][l])
                            coefficient=self.mul(coefficient,self.power(A,l))
                            coefficient=self.mul(coefficient,self.power(B,e-k-l))
                            terms.append(self.mul(coefficient,low[p+l,k]))
                    out[p,e]=self.total(terms)
                    details['reconstruction'].append({'p':p,'e':e,'value':out[p,e],
                        'signed_operations_start':st,'signed_operations_stop':self.i})
            elif not a:branch='normalized_constant_zero'
            else:
                st=self.i;Y,remainder=self.div(self.add(self.mul(a,self.sub(n,1)),b),m)
                details['height']={'Y':Y,'remainder':remainder,'signed_operations_start':st,'signed_operations_stop':self.i}
                if not Y:branch='normalized_zero_height'
                else:
                    offset=self.sub(self.add(self.sub(m,b),a),1)
                    branch,child='transpose_lattice',(Y,a,m,offset)
                    low=self.moment(*child,depth+1)
                    for p,e in DEGREES:
                        if not e:continue
                        st=self.i;den,coefficients=POWER_SUMS[p]
                        endpoint=self.mul(self.mul(den,self.power(Y,e)),sums[p]);terms=[]
                        for v in range(e):
                            for h,c in coefficients:terms.append(self.mul(self.mul(BINOMIAL[e][v],c),low[v,h]))
                        num=self.sub(endpoint,self.total(terms));out[p,e]=self.exact(num,den)
                        details['reconstruction'].append({'p':p,'e':e,'denominator':den,'numerator':num,
                            'value':out[p,e],'signed_operations_start':st,'signed_operations_stop':self.i})
        expected={'parameters':key,'branch':branch,'child':child,'signed_operations_start':start,
            'signed_operations_stop':self.i,'moments':{f'{p},{e}':out[p,e] for p,e in DEGREES},'degree_five_details':details}
        same(self.nodes[self.node_i],expected);self.node_i+=1;self.cache[key]=out
        return out
    def request(self,row):
        inp=row['inputs']
        assert set(inp)=={'n','m','a','b'}
        args=tuple(inp[k] for k in ('n','m','a','b'))
        assert all(type(x) is int for x in args) and args[0]>=0 and args[1]>=1
        same(row['cache_hit'],args in self.cache)
        assert row['signed_operations_start']==self.i and row['moment_nodes_start']==self.node_i
        values=self.moment(*args)
        same(row['outputs'],{f'{p},{e}':values[p,e] for p,e in DEGREES})
        assert row['signed_operations_stop']==self.i and row['moment_nodes_stop']==self.node_i
    def finish(self,check_moments=True):
        assert self.i==len(self.ops) and self.node_i==len(self.nodes)
        if check_moments:
            s=self.e['stats'];assert s['moment_requests']==self.requests and s['cache_hits']==self.hits and s['max_recursion_depth']==self.depth
        bits=0
        for op in self.ops:
            vals=list(op['inputs'])+(op['result'] if type(op['result']) is list else [op['result']])
            bits=max(bits,*(abs(v).bit_length() for v in vals))
        assert bits==self.e['stats']['max_observed_integer_bits']

def evidence(e,native):
    io.inspect_evidence(e,native)
    if 'native_source' in e:same(e['native_source'],native)
    return {'typed':len(e['arithmetic_operations']),'signed':len(e['signed_operations']),
            'digits':e['arithmetic_stats']['adder_digit_replays'],'nodes':len(e['moment_nodes'])}

def certificate(cert,native,bindings,partial=False):
    same(cert['source_bindings'],bindings)
    if partial:
        assert cert['schema']=='INCOMPLETE_BRC_DEGREE_FIVE_QUERY_CERTIFICATE_V1' and cert['complete_certificate'] is False
        assert cert['inflight_request'] is None
    else:
        assert cert['schema']=='BRC_DEGREE_FIVE_QUERY_CERTIFICATE_V1' and cert['complete_certificate'] is True
        same(cert['degrees'],DEGREES);assert cert['maximum_total_degree']==5
        e=cert['actual_integer_evidence']
        assert e['schema']=='BRC_DEGREE_FIVE_SINGLE_FLOOR_MOMENTS_V1' and e['maximum_total_degree']==5
        assert e['source_sha256']==bindings['typed_floor_degree_five.py']
        assert e['base_arithmetic_source_sha256']==bindings['base_arithmetic'] and e['proof_sha256']==bindings['DEGREE_FIVE_RECIPROCITY.md']
    e=cert['actual_integer_evidence'];counts=evidence(e,native);cur=Cursor(e)
    for row in cert['requests']:cur.request(row)
    cur.finish()
    if partial:
        expected=[{'parameters':key,'moments':{f'{p},{q}':v for (p,q),v in values.items()}} for key,values in cur.cache.items()]
        same(e['cache_entries'],expected)
    return counts

def comparator(row,native):
    e=row['actual_integer_evidence'];evidence(e,native);cur=Cursor(e)
    inp=row['inputs'];n,m,a,b=(inp[k] for k in ('n','m','a','b'))
    assert row['complete_comparator'] is True and len(row['samples'])==n
    buckets={f'{p},{q}':0 for p,q in DEGREES}
    for j,sample in enumerate(row['samples']):
        assert sample['j']==j and sample['signed_operations_start']==cur.i
        val=cur.add(cur.mul(a,j),b);q,r=cur.div(val,m)
        same([val,q,r],[sample['affine'],sample['quotient'],sample['remainder']])
        assert sample['affine_operations_stop']==cur.i==sample['powers_operations_start']
        jp,qp=[1],[1]
        for _ in range(5):jp.append(cur.mul(jp[-1],j));qp.append(cur.mul(qp[-1],q))
        same(jp,sample['index_powers']);same(qp,sample['quotient_powers']);assert sample['powers_operations_stop']==cur.i
        assert len(sample['terms'])==21
        for (p,q),term in zip(DEGREES,sample['terms']):
            assert term['p']==p and term['e']==q and term['signed_operations_start']==cur.i
            key=f'{p},{q}';same(term['before'],buckets[key])
            product=cur.mul(jp[p],qp[q]);after=cur.add(buckets[key],product)
            same([product,after],[term['term'],term['after']]);buckets[key]=after
            assert term['signed_operations_stop']==cur.i
        assert sample['signed_operations_stop']==cur.i
    same(buckets,row['outputs']);cur.finish();return n

def cost(e):
    return {'arithmetic_stats':e['arithmetic_stats'],'typed_operations':len(e['arithmetic_operations']),
        'signed_operations':len(e['signed_operations']),'moment_nodes':len(e['moment_nodes']),'moment_stats':e['stats']}
def aggregate(rows):
    rows=list(rows)
    keys=('typed_operations','adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
    sums={k:sum(r['arithmetic_stats'][k] for r in rows) for k in keys}
    sums.update(signed_operations=sum(len(r['signed_operations']) for r in rows),moment_nodes=sum(len(r['moment_nodes']) for r in rows),
        moment_requests=sum(r['stats']['moment_requests'] for r in rows),cache_hits=sum(r['stats']['cache_hits'] for r in rows))
    maxima={k:max((r['stats'][k] for r in rows),default=0) for k in ('max_recursion_depth','max_observed_integer_bits')}
    return {'receipts':len(rows),'sum':sums,'max':maxima,'native_calls_counted_from_disjoint_process_intervals':True}

def boundary(record,original):
    same(record['before'],record['after']);snap=record['before']
    assert snap['complete_certificate'] is False and snap['inflight_request'] is None
    same(snap['requests'],original['requests'][:1])
    e=snap['actual_integer_evidence'];oe=original['actual_integer_evidence']
    for key in ('arithmetic_operations','arithmetic_stats','signed_operations','moment_nodes','window_weight_queries'):
        same(e[key],oe[key])
    assert record['additional_typed_operations']==record['additional_native_calls']==0

def main():
    blob=(ROOT/'DEGREE_FIVE_RESULTS.json.gz').read_bytes();raw=gzip.decompress(blob)
    assert sha(raw)==RAW_PIN and sha(blob)==GZIP_PIN and len(raw)==88217988 and len(blob)==3468068
    data=json.loads(raw);summary=json.loads((ROOT/'DEGREE_FIVE_SUMMARY.json').read_bytes())
    assert data['status']==summary['status']=='PASS'
    same(data['source_bindings'],summary['source_bindings']);bindings=data['source_bindings']
    for f,p in PINS.items():assert bindings[f]==p==sha((ROOT/f).read_bytes())
    for f,path in PATHS.items():assert bindings[f]==sha((ROOT.parent/path).read_bytes())
    assert summary['payload_sha256']==RAW_PIN and summary['artifact_sha256']==GZIP_PIN
    same([summary['raw_bytes'],summary['gzip_bytes']],[len(raw),len(blob)])
    gb=(ROOT/'STARTUP_GUARD.json').read_bytes();guard=json.loads(gb)
    assert sha(gb)==data['startup_guard']['sha256'];same(guard,data['startup_guard']['receipt'])
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['mode']=='TASK_RESEARCH' and guard['boundary']=='startup'
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    for key in ('lazy_modular','sparse_modular','typed_integer_prechecks'):assert native['files_sha256'][key]==bindings[key]
    assert native['primitive_source']=='0852cad130c1d877174d235687cf60c19f318c58'
    adder=native['native_adder'];assert adder['input_columns']==8 and adder['positive_BRC_input_states']==12
    same(adder['columns'],[[0,0],[1,0],[1,0],[0,1],[1,0],[0,1],[0,1],[1,1]])
    vendor=(ROOT.parent/'sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py').read_bytes()
    assert sha(vendor)==adder['vendor']['sha256']
    assert hashlib.sha1(b'blob '+str(len(vendor)).encode()+b'\0'+vendor).hexdigest()==adder['vendor']['git_blob']
    assert len(data['actual_core_calls'])==data['actual_core_call_count']==summary['actual_core_call_count']==1
    call=data['actual_core_calls'][0];assert call['entrypoint']=='recurrent_mass_power' and call['states']==12 and call['depth']==1 and call['elapsed_ns']>=0
    groups={k:[] for k in ('production','typed_finite_sums','positive_replay','cache_control','cache_control_replay','negative_replay')}
    per=[];sample_count=0;branch_counts=Counter()
    assert len(data['cases'])==9
    for args,row in zip(CASES,data['cases']):
        inp=dict(zip(('n','m','a','b'),args));same(inp,row['inputs'])
        cert=row['certificate'];rep=row['verification']['replay_certificate'];brute=row['typed_finite_sums']
        assert len(cert['requests'])==1; same(cert['requests'][0]['inputs'],inp);same(brute['inputs'],inp)
        certificate(cert,native,bindings);certificate(rep,native,bindings)
        assert io.semantic(cert)==io.semantic(rep) and row['verification']['verified'] is True and row['verification']['requests_replayed']==1
        sample_count+=comparator(brute,native)
        same(row['values'],cert['requests'][0]['outputs']);same(row['values'],brute['outputs']);assert row['all_21_moments_equal'] is True
        for key,item,field in (('production',cert,'production_cost'),('positive_replay',rep,'positive_replay_cost'),('typed_finite_sums',brute,'typed_finite_sum_cost')):
            e=item['actual_integer_evidence'];groups[key].append(e);same(cost(e),row[field])
        branch_counts.update(n['branch'] for n in cert['actual_integer_evidence']['moment_nodes'])
        per.append({'inputs':inp,'production_digits':cert['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'],
                    'finite_sum_digits':brute['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']})
    assert sample_count==44
    boundary(data['production_boundary_rejection'],data['cases'][3]['certificate'])
    ctrl=data['cache_and_reuse_control'];cert=ctrl['certificate'];rep=ctrl['verification']['replay_certificate']
    certificate(cert,native,bindings);certificate(rep,native,bindings);assert io.semantic(cert)==io.semantic(rep)
    assert len(cert['requests'])==2 and cert['requests'][1]['cache_hit'] is True
    same(cert['requests'][0]['outputs'],cert['requests'][1]['outputs'])
    assert cert['requests'][1]['signed_operations_start']==cert['requests'][1]['signed_operations_stop']
    assert cert['requests'][1]['moment_nodes_start']==cert['requests'][1]['moment_nodes_stop']
    boundary(ctrl['invalid_boundary'],cert)
    groups['cache_control'].append(cert['actual_integer_evidence']);groups['cache_control_replay'].append(rep['actual_integer_evidence'])
    assert len(data['input_rejections'])==10
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations']==0
        assert row['call_interval']['start']==row['call_interval']['stop']
    negative=[]
    for row in data['negative_checks']:
        assert row['rejected'] is True;attempt=io.decode_keys(row['attempted_certificate_typed_key_encoding'])
        original=data['cases'][row['source_case_index']]['certificate'];captures=row['actual_replay_certificates']
        assert io.canonical(io.encode_keys(attempt))!=io.canonical(io.encode_keys(original))
        kind=row['kind'];name=row['name']
        if kind=='EARLY_ZERO_WORK_REJECTION':
            assert not captures and name.endswith('_early')
            assert row['call_interval']['start']==row['call_interval']['stop']
        elif kind=='PAID_VALID_PREFIX_THEN_INPUT_REJECTION':
            assert len(captures)==1 and name=='valid_prefix_then_invalid'
            c=captures[0];certificate(c,native,bindings,True);same(c['requests'],original['requests'])
            for key in ('signed_operations','arithmetic_operations','moment_nodes'):same(c['actual_integer_evidence'][key],original['actual_integer_evidence'][key])
            groups['negative_replay'].append(c['actual_integer_evidence'])
        else:
            assert kind=='COMPLETE_PAID_REPLAY_THEN_MISMATCH' and len(captures)==1
            c=captures[0];certificate(c,native,bindings)
            if name!='input_valid_changed':assert io.semantic(c)==io.semantic(original)
            else:same(c['requests'][0]['inputs'],attempt['requests'][0]['inputs'])
            assert io.semantic(c)!=io.semantic(attempt);groups['negative_replay'].append(c['actual_integer_evidence'])
        negative.append({'name':name,'kind':kind,'paid_streams':len(captures)})
    assert Counter(x['kind'] for x in negative)==Counter({'COMPLETE_PAID_REPLAY_THEN_MISMATCH':10,'PAID_VALID_PREFIX_THEN_INPUT_REJECTION':1,'EARLY_ZERO_WORK_REJECTION':6})
    costs={k:aggregate(v) for k,v in groups.items()};same(costs,data['cost_categories']);same(costs,summary['cost_categories'])
    intervals=data['call_intervals'];front=0;native_by=Counter()
    for row in intervals:
        assert row['start']==front and row['stop']>=front
        native_by[row['category']]+=row['stop']-front;front=row['stop']
    assert front==1;same(dict(native_by),data['native_calls_by_category']);same(dict(native_by),summary['native_calls_by_category'])
    nested=[interval for row in data['cases'] for interval in row['call_intervals']]+ctrl['call_intervals']
    nested += [row['call_interval'] for row in data['input_rejections']]+[row['call_interval'] for row in data['negative_checks']]
    same(nested,intervals)
    same(data['coverage'],summary['coverage']);assert data['coverage']['moment_equalities']==189 and data['coverage']['finite_sum_samples']==44
    assert set(branch_counts)==set(data['coverage']['branch_types'])
    for stored,row in zip(summary['per_case'],data['cases']):same(stored,{'inputs':row['inputs'],'production':row['production_cost'],'typed_finite_sums':row['typed_finite_sum_cost']})
    assert summary['comparison_is_timing_benchmark'] is False and summary['full_shor_sampling_performed'] is False
    assert data['mixed_floor_algorithm_implemented'] is False and data['full_shor_sampling_performed'] is False
    result={'status':'PASS','review_scope':'Independent shared-context stdlib saved-record review; no science import or answer recomputation',
        'reader_sha256':sha(Path(__file__).read_bytes()),'helper_source_sha256':HELPER_PIN,'source_bindings':bindings,
        'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':len(raw),'gzip_bytes':len(blob),
        'summary_sha256':sha((ROOT/'DEGREE_FIVE_SUMMARY.json').read_bytes()),'startup_guard_sha256':sha(gb),
        'reviewed_streams':sum(len(v) for v in groups.values()),'cost_categories':costs,
        'total_digits':sum(v['sum']['adder_digit_replays'] for v in costs.values()),
        'total_signed_operations':sum(v['sum']['signed_operations'] for v in costs.values()),
        'total_typed_operations':sum(v['sum']['typed_operations'] for v in costs.values()),
        'total_moment_nodes':sum(v['sum']['moment_nodes'] for v in costs.values()),
        'complete_node_reconstructions_checked':True,'all_signed_to_typed_links_checked':True,
        'all_retained_adder_cells_checked_against_native_columns':True,'all_costs_independently_recounted':True,
        'finite_samples':sample_count,'finite_bucket_terms':sample_count*len(DEGREES),'moment_equalities':189,
        'production_branch_counts':dict(branch_counts),'per_case':per,'negative_checks':negative,
        'input_rejections':len(data['input_rejections']),'cache_and_boundary_controls_checked':True,
        'global_native_calls':data['actual_core_calls'],'native_calls_by_category':dict(native_by),
        'production_exceeds_brute':costs['production']['sum']['adder_digit_replays']>costs['typed_finite_sums']['sum']['adder_digit_replays'],
        'elapsed_not_benchmark':data['elapsed_seconds_before_serialization'],
        'failure_artifact_present':(ROOT/'DEGREE_FIVE_FAILED_EXECUTION.json.gz').exists(),
        'formal_admission':False,'scientific_execution_performed_by_this_reader':False}
    assert not result['failure_artifact_present']
    out=Path(__file__).with_name('DEGREE_FIVE_RECORD_REVIEW.json');out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','reviewed_streams','total_digits','total_typed_operations','total_signed_operations','total_moment_nodes','finite_samples','moment_equalities')}))
if __name__=='__main__':main()
