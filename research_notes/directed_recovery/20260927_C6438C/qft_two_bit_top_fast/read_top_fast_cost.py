"""Author saved-record readback: stdlib I/O and one pinned metadata reader only.

Consumes recorded operation outputs and native cells. No scientific imports,
answer evaluation, replay invocation, or experiment is performed.
"""
from pathlib import Path
from collections import Counter
from copy import deepcopy
import gzip
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent/'sep27-qft-two-bit-top-general'
HELPER = BASE/'read_top_general_cost.py'
HELPER_PIN = 'a96696eb187d6c6251934f9b1651f5abc1b8d2db5a5357ea051960b8e4489f5a'
RAW_PIN = 'db60ed6dd188c5936585c0d1a4dbffa83652baca0dd2551182148d2c8457038a'
GZIP_PIN = '7cea2d841376650734622fe7d29b529a8f46cd195a4dc87b63993d9e995fc507'
SCHEMA = 'BRC_TOP_BIT_POINT_AND_SETUP_REUSE_V1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


assert digest(HELPER.read_bytes()) == HELPER_PIN
spec = importlib.util.spec_from_file_location('pinned_top_general_author_io', HELPER)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
same = old.same


class FastCursor(old.TopCursor):
    """Traverse saved chronology, including lazy construction and cache references."""
    def __init__(self, evidence):
        super().__init__(evidence)
        self.setups_seen = {}
        self.coefficients_seen = {}

    def setup(self, cert, req, g, ell):
        index = req['setup_index']
        assert type(index) is int and 0 <= index < len(cert['setups'])
        setup = cert['setups'][index]
        same(setup['inputs'], {'g':g,'ell':ell})
        assert setup['complete'] is True
        key = (g,ell)
        if key in self.setups_seen:
            assert req['setup_cache_hit'] is True
            assert index == self.setups_seen[key]
            assert setup['signed_operations_stop'] <= self.i
        else:
            assert req['setup_cache_hit'] is False and index == len(self.setups_seen)
            assert setup['signed_operations_start'] == self.i
            V = self.recorded(setup['V'],lambda:self.power(ell))
            M = self.recorded(setup['M'],lambda:self.power(g-ell))
            L = self.recorded(setup['L'],lambda:self.mul(V,M))
            self.recorded(setup['P'],lambda:self.add(V,V))
            self.exact(setup['H'],L,2)
            assert setup['signed_operations_stop'] == self.i
            self.setups_seen[key] = index
        assert req['setup_access_operations_stop'] == self.i
        return index, setup

    def fast_segment(self, rec, setup, index, R):
        assert rec['signed_operations_start'] == self.i
        n,b = rec['n'],rec['head']['value']
        V,M,P = [setup[x]['value'] for x in ('V','M','P')]
        if n == 0:
            assert rec['route']=='EMPTY' and rec['empty'] is True and rec['table_calls']==[]
            value=self.recorded(rec['zero'],lambda:self.add(0,0))
        elif n == 1:
            assert rec['route']=='SINGLE_DISPLACEMENT' and rec['empty'] is False
            assert rec['table_calls']==[] and 'coefficient_reference' not in rec
            z,t=self.division(rec['compressed_displacement'],b,V)
            _,parity=self.division(rec['parity'],z,2)
            assert parity in (0,1)
            if rec['piece']=='low':
                B=self.recorded(rec['base_overlap'],lambda:self.sub(M,self.mul(3,z)))
                alpha=-3
            else:
                assert rec['piece']=='high'
                B=self.recorded(rec['base_overlap'],lambda:self.sub(z,M))
                alpha=1
            assert rec['alpha']==alpha
            weight=self.recorded(rec['weight'],lambda:self.sub(V,self.mul(2,t)))
            unsigned=self.recorded(rec['unsigned_overlap'],lambda:self.sub(self.mul(weight,B),self.mul(alpha,t)))
            sign=1 if parity==0 else -1
            assert rec['sign']==sign
            value=self.recorded(rec['result'],lambda:self.mul(sign,unsigned))
        else:
            assert n>=2 and rec['route']=='FLOOR_MOMENTS' and rec['empty'] is False
            piece=rec['piece'];ref=rec['coefficient_reference']
            assert ref['piece']==piece
            coefficient=setup['coefficients'][piece]
            assert coefficient['complete'] is True
            key=(index,piece)
            if key in self.coefficients_seen:
                assert ref['cache_hit'] is True
                assert coefficient['signed_operations_stop']<=self.i
                coeff=self.coefficients_seen[key]
            else:
                assert ref['cache_hit'] is False
                coeff=self.coefficients(coefficient,piece,V,M)
                self.coefficients_seen[key]=coeff
            assert rec['moment_evaluation_signed_operations_start']==self.i
            # The old reader expects its start at moment evaluation; the new
            # source explicitly saves both outer and post-lazy-construction starts.
            moment_record={**rec,'signed_operations_start':self.i}
            value=super().segment(moment_record,P,V,R,coeff)
        same(value,rec['value'])
        assert rec['signed_operations_stop']==self.i
        return value

    def fast_orientation(self,rec,setup,index,R):
        assert rec['signed_operations_start']==self.i
        b=rec['head']['value'];L=setup['L']['value'];H=setup['H']['value']
        whole=self.length(rec['whole_length'],b,R,L)
        if rec['whole_length']['empty']:
            assert rec['empty'] is True and rec['segments']==[]
            value=self.recorded(rec['zero'],lambda:self.add(0,0))
        else:
            assert rec['empty'] is False and len(rec['segments'])==2
            low=self.length(rec['low_length'],b,R,H)
            high=self.recorded(rec['high_count'],lambda:self.sub(whole,low))
            assert high>=0
            head=self.recorded(rec['high_head'],lambda:self.add(b,self.mul(R,low)))
            values=[]
            for seg,piece,h,n in zip(rec['segments'],('low','high'),(b,head),(low,high)):
                same([seg['piece'],seg['head']['value'],seg['n'],seg['step'],seg['coefficient_piece']],
                     [piece,h,n,R,piece])
                same(seg['head'],rec['head'] if piece=='low' else rec['high_head'])
                same([seg['displacement_lower_bound'],seg['displacement_exclusive_upper_bound']],
                     [0,H] if piece=='low' else [H,L])
                if n: assert seg['displacement_lower_bound']<=h<seg['displacement_exclusive_upper_bound']
                values.append(self.fast_segment(seg,setup,index,R))
            value=self.recorded(rec['total'],lambda:self.total(values))
        same(value,rec['value'])
        assert rec['signed_operations_stop']==self.i
        return value

    def requests(self,cert):
        for req in cert['requests']:
            assert req['signed_operations_start']==self.i
            inp=req['inputs'];g,ell,k,R,r=[inp[x] for x in ('g','ell','k','R','r')]
            assert set(inp)=={'g','ell','k','R','r','stride'}
            assert all(type(x) is int for x in inp.values())
            assert g>=2 and 0<=ell<k<g and k==g-1 and R>0 and 0<=r<R and inp['stride']==1
            start_tables=self.seen_tables
            index,setup=self.setup(cert,req,g,ell)
            o=req['orientations'];assert len(o)==2
            self.recorded(o[0]['head'],lambda:self.add(r,0))
            self.recorded(o[1]['head'],lambda:self.sub(R,r))
            values=[]
            for rec,label in zip(o,('nonnegative_difference','negative_difference_magnitude')):
                assert rec['orientation']==label and rec['multiplicity']==1
                values.append(self.fast_orientation(rec,setup,index,R))
            value=self.recorded(req['final_addition'],lambda:self.total(values))
            same(value,req['value'])
            assert req['signed_operations_stop']==self.i
            assert self.seen_tables-start_tables==req['top_level_table_calls']<=8
            assert req['raw_denominator_exponent']==2*g and req['modulus_alignment_required'] is False
            assert req['route']=='TOP_BIT_POINT_AND_SETUP_REUSE'
        assert len(self.setups_seen)==len(cert['setups'])
        assert set(self.coefficients_seen)=={(i,p) for i,s in enumerate(cert['setups']) for p in s['coefficients']}
        assert self.i==len(self.ops)


def inspect(cert,native,partial=False):
    assert cert['schema']==('INCOMPLETE_' if partial else '')+SCHEMA
    if partial:
        assert cert['complete_certificate'] is False and cert['inflight_request'] is None
    e=cert['actual_integer_evidence']
    old.inspect_evidence(e,native)
    FastCursor(e).requests(cert)


def inspect_partial(cert,original,native):
    inspect(cert,native,True)
    assert cert['source_sha256']==original['source_sha256'] and len(cert['requests'])==1
    same(cert['requests'],original['requests'][:1])
    assert len(cert['setups'])==1
    for part,final in zip(cert['setups'],original['setups']):
        same({k:v for k,v in part.items() if k!='coefficients'},
             {k:v for k,v in final.items() if k!='coefficients'})
        for key,value in part['coefficients'].items():same(value,final['coefficients'][key])
    e=cert['actual_integer_evidence'];prev=original['actual_integer_evidence']
    same(e['signed_operations'],prev['signed_operations'][:len(e['signed_operations'])])
    same(e['arithmetic_operations'],prev['arithmetic_operations'][:len(e['arithmetic_operations'])])
    same(e['moment_nodes'],prev['moment_nodes'][:len(e['moment_nodes'])])


def hotspots(cert):
    e=cert['actual_integer_evidence'];ops=e['signed_operations'];labels=['routing_and_final']*len(ops)
    def mark(name,start,stop):
        assert 0<=start<=stop<=len(labels)
        labels[start:stop]=[name]*(stop-start)
    for req in cert['requests']:
        for orientation in req['orientations']:
            for seg in orientation['segments']:
                mark('segment_'+seg['route'],seg['signed_operations_start'],seg['signed_operations_stop'])
                for table in seg['table_calls']:
                    mark('moment_tables',table['signed_operations_start'],table['signed_operations_stop'])
    for setup in cert['setups']:
        mark('setup_scales',setup['signed_operations_start'],setup['signed_operations_stop'])
        for piece,c in setup['coefficients'].items():
            mark('coefficients_'+piece,c['signed_operations_start'],c['signed_operations_stop'])
    result={k:Counter(signed_operations=0,typed_operations=0,adder_digit_replays=0) for k in set(labels)}
    for name,op in zip(labels,ops):
        result[name]['signed_operations']+=1
        result[name]['typed_operations']+=len(op['typed_operation_indices'])
        result[name]['adder_digit_replays']+=sum(old.raw_digit_count(e['arithmetic_operations'][i]['trace']) for i in op['typed_operation_indices'])
    assert sum(c['adder_digit_replays'] for c in result.values())==e['arithmetic_stats']['adder_digit_replays']
    return {k:dict(v) for k,v in sorted(result.items())}


def source_pins(cert):
    targets={'source_sha256':ROOT/'top_bit_fast.py','optimization_proof_sha256':ROOT/'POINT_AND_SETUP_REUSE.md',
        'base_source_sha256':BASE/'top_bit_general.py','proof_sha256':BASE/'TOP_BIT_GENERAL_MODULUS.md',
        'proof_review_sha256':BASE/'guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md',
        'direct_source_sha256':ROOT.parent/'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
        'direct_proof_sha256':ROOT.parent/'sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md',
        'floor_moment_source_sha256':ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
        'baseline_helper_source_sha256':ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py'}
    for key,path in targets.items(): assert digest(path.read_bytes())==cert[key]
    return {k:{'path':str(p),'sha256':cert[k]} for k,p in targets.items()}


def main():
    target=ROOT/'TOP_FAST_COST_READBACK.json'
    if target.exists():raise FileExistsError('Author readback is already frozen')
    compressed=(ROOT/'TOP_BIT_FAST_RESULTS.json.gz').read_bytes();raw=gzip.decompress(compressed)
    assert digest(raw)==RAW_PIN and digest(compressed)==GZIP_PIN
    data=json.loads(raw);summary=json.loads((ROOT/'TOP_BIT_FAST_SUMMARY.json').read_bytes())
    assert data['status']==summary['status']=='PASS'
    assert summary['payload_sha256']==RAW_PIN and summary['artifact_sha256']==GZIP_PIN
    assert summary['raw_bytes']==len(raw) and summary['gzip_bytes']==len(compressed)
    same(data['source_sha256'],summary['source_sha256'])
    for path,pin in data['source_sha256'].items():assert digest((ROOT/path).read_bytes())==pin
    guardraw=(ROOT/'STARTUP_GUARD.json').read_bytes();guard=json.loads(guardraw)
    assert digest(guardraw)==data['startup_guard']['sha256'];same(guard,data['startup_guard']['receipt'])
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events']==[]
    assert guard['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and guard['mode']=='TASK_RESEARCH' and guard['boundary']=='startup'
    hr=data['historical_evidence_reuse'];hc=(BASE/'TOP_BIT_GENERAL_RESULTS.json.gz').read_bytes();hraw=gzip.decompress(hc)
    assert digest(hc)==hr['artifact_sha256']==old.GZIP_PIN and digest(hraw)==hr['payload_sha256']==old.RAW_PIN
    history=json.loads(hraw);assert history['status']=='PASS'
    same(history['source_sha256'],hr['source_sha256'])
    for name,pin in hr['source_sha256'].items():assert digest((BASE/name).read_bytes())==pin
    assert hr['whole_payload_read_and_hash_checked'] is True
    assert hr['historical_pair_comparator_reexecuted'] is False and hr['historical_production_reexecuted'] is False
    assert digest((BASE/'STARTUP_GUARD.json').read_bytes())==hr['guard_sha256']==history['startup_guard']['sha256']
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    same(native,history['cases'][0]['certificate']['actual_integer_evidence']['native_source'])
    for key,path in {'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}.items():
        assert digest((ROOT.parent/path).read_bytes())==native['files_sha256'][key]
    groups={key:[] for key in ('production','positive_replay','cache_control','cache_control_replay','negative_replay')}
    cases=[];all_hotspots={};routes=Counter();coverage=Counter();historical_pairs=0
    for index,case in enumerate(data['cases']):
        cert=case['certificate'];replay=case['verification']['replay_certificate'];h=history['cases'][index]
        assert cert['source_sha256']==data['source_sha256']['top_bit_fast.py'];pins=source_pins(cert)
        assert old.semantic(cert)==old.semantic(replay)
        same(case['inputs'],h['inputs']);same(case['values'],h['values'])
        same(case['historical_production_cost'],h['production_cost'])
        same(case['historical_typed_comparator_cost'],h['typed_enumeration_cost'])
        assert case['all_residues_equal_saved_typed_comparator'] is True
        assert old.semantic(h['certificate'])==old.semantic(h['verification']['replay_certificate'])
        old.inspect_evidence(h['typed_enumeration']['actual_integer_evidence'],native)
        values,pairs=old.inspect_pairs(h['typed_enumeration'],h['inputs']);historical_pairs+=pairs
        same(values,case['values']);same(values,[r['value'] for r in cert['requests']])
        assert [r['inputs']['r'] for r in cert['requests']]==list(range(case['inputs']['R']))
        assert len(cert['setups'])==1
        for item,cat,field in ((cert,'production','production_cost'),(replay,'positive_replay','positive_replay_cost')):
            inspect(item,native);e=item['actual_integer_evidence'];groups[cat].append(e)
            same(old.cost_record(e),case[field])
        assert case['verification']['verified'] is True and case['verification']['requests_replayed']==len(values)
        same(case['verification']['replay_arithmetic_stats'],replay['actual_integer_evidence']['arithmetic_stats'])
        hs=hotspots(cert)
        for k,v in hs.items():all_hotspots.setdefault(k,Counter()).update(v)
        for req in cert['requests']:
            coverage['requests']+=1;coverage['top_level_table_calls']+=req['top_level_table_calls']
            coverage['setup_hits' if req['setup_cache_hit'] else 'setup_misses']+=1
            for o in req['orientations']:
                coverage['orientations']+=1;coverage['empty_orientations']+=int(o['empty'])
                for seg in o['segments']:routes[seg['route']]+=1;coverage['segments']+=1
        coverage['coefficient_constructions']+=sum(len(s['coefficients']) for s in cert['setups'])
        cases.append({'inputs':case['inputs'],'values':values,'historical_pairs_read':pairs,
            'production_digits':case['production_cost']['arithmetic_stats']['adder_digit_replays'],
            'historical_production_digits':h['production_cost']['arithmetic_stats']['adder_digit_replays'],
            'historical_comparator_digits':h['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays'],
            'production_hotspots':hs})
    assert len(cases)==6 and coverage['requests']==37 and historical_pairs==hr['historical_pair_records']==720
    for key in ('requests','segments','top_level_table_calls','setup_hits','setup_misses','coefficient_constructions'):
        assert coverage[key]==data['coverage'][key]
    same(dict(routes),data['coverage']['route_counts']);same(data['coverage'],summary['coverage'])
    mixed=data['mixed_cache_control'];mc=mixed['certificate'];mr=mixed['verification']['replay_certificate']
    assert old.semantic(mc)==old.semantic(mr) and mixed['verification']['verified'] is True
    for c,cat in ((mc,'cache_control'),(mr,'cache_control_replay')):
        inspect(c,native);groups[cat].append(c['actual_integer_evidence'])
    same(mixed['requests_from_historical_grid'],[[1,0],[0,0],[1,1],[2,0]])
    assert len(mc['requests'])==4 and len(mc['setups'])==2
    same([r['setup_index'] for r in mc['requests']],[0,1,0,0])
    same([r['setup_cache_hit'] for r in mc['requests']],[False,False,True,True])
    for req,(idx,res) in zip(mc['requests'],mixed['requests_from_historical_grid']):
        same(req['value'],history['cases'][idx]['values'][res])
        same(req['inputs'],{**history['cases'][idx]['inputs'],'r':res,'stride':1})
    boundary=data['production_boundary_rejection']
    assert boundary['rejected'] is True and boundary['reuse_completed_by_original_grid'] is True
    assert boundary['state_and_paid_evidence_unchanged'] is True
    same(boundary['before'],boundary['after']);inspect_partial(boundary['before'],data['cases'][0]['certificate'],native)
    assert boundary['additional_native_calls']==boundary['additional_typed_operations']==0
    assert boundary['native_subinterval']['start']==boundary['native_subinterval']['stop']
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations']==0
        assert row['call_interval']['start']==row['call_interval']['stop']
    assert len(data['input_rejections'])==12
    negrows=[];negkinds=Counter()
    for row in data['negative_checks']:
        assert row['rejected'] is True
        original=data['cases'][row['source_case_index']]['certificate']
        attempted=old.decode_keys(row['attempted_certificate_typed_key_encoding'])
        assert row['attempted_certificate_typed_key_encoding']!=old.encode_keys(original)
        captures=row['actual_replay_certificates'];negkinds[row['kind']]+=1
        if row['name'].endswith('_early'):
            assert not captures and row['call_interval']['start']==row['call_interval']['stop']
            if row['name']=='bool_input_early':assert type(attempted['requests'][0]['inputs']['g']) is bool
            if row['name']=='nonstring_key_early':assert 0 in attempted['requests'][0]
        else:
            assert len(captures)==1;capture=captures[0]
            if row['name']=='valid_prefix_then_invalid_non_top':
                inspect_partial(capture,original,native)
                assert attempted['requests'][1]['inputs']['g']==4
            else:
                assert old.semantic(capture)==old.semantic(original);inspect(capture,native)
            groups['negative_replay'].append(capture['actual_integer_evidence'])
        negrows.append({'name':row['name'],'kind':row['kind'],'error':row['error'],
            'receipts':len(captures),'digits':sum(c['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'] for c in captures)})
    assert len(negrows)==18 and len(groups['negative_replay'])==14
    same(dict(negkinds),summary['negative_kinds'])
    resources={key:old.costs(rows) for key,rows in groups.items()}
    same(resources,data['cost_categories']);same(resources,summary['cost_categories'])
    frontier=0;native_by=Counter()
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        native_by[row['category']]+=row['stop']-row['start'];frontier=row['stop']
    assert frontier==len(data['actual_core_calls'])==summary['actual_core_call_count']==1
    same(dict(native_by),data['native_calls_by_category']);same(dict(native_by),summary['native_calls_by_category'])
    same(data['call_intervals'],summary['call_intervals'])
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for rows in groups.values() for e in rows)==1
    assert data['actual_core_calls'][0]['states']==12 and data['actual_core_calls'][0]['depth']==1
    assert data['actual_core_calls'][0]['entrypoint']=='recurrent_mass_power'
    assert data['new_typed_pair_comparator_executions']==0 and data['historical_science_reexecuted'] is False
    log=(ROOT/'TOP_BIT_FAST_EXECUTION_LOG.txt').read_bytes()
    lines=[json.loads(s) for s in log.decode('utf-8-sig').splitlines() if s.strip().startswith('{')]
    assert len([x for x in lines if x.get('stage')=='CASE_COMPLETE'])==6;same(lines[-1],summary)
    total=sum(row['sum']['adder_digit_replays'] for row in resources.values())
    result={'status':'PASS_FULL_AUTHOR_SAVED_EVIDENCE_READBACK','scientific_execution_performed':False,
        'reader_sha256':digest(Path(__file__).read_bytes()),'pure_io_helper_sha256':HELPER_PIN,
        'source_sha256':data['source_sha256'],'proof_and_helper_pins':pins,
        'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':len(raw),'gzip_bytes':len(compressed),
        'summary_sha256':digest((ROOT/'TOP_BIT_FAST_SUMMARY.json').read_bytes()),
        'log_sha256':digest(log),'guard_sha256':digest(guardraw),'case_rows':cases,'cost_categories':resources,
        'all_disjoint_current_streams_read':sum(len(rows) for rows in groups.values()),'current_total_adder_digits':total,
        'historical_evidence_reuse':hr,'historical_pairs_read':historical_pairs,'historical_pair_reexecution':False,
        'structural_counts':dict(coverage),'route_counts':dict(routes),
        'production_hotspots':{k:dict(v) for k,v in sorted(all_hotspots.items())},
        'mixed_cache_control':{'accepted_queries':4,'setups':2,'indices':[0,1,0,0],
            'hits':[False,False,True,True],'production_cost':old.cost_record(mc['actual_integer_evidence']),
            'replay_cost':old.cost_record(mr['actual_integer_evidence']),'separately_charged':True},
        'negative_checks':negrows,'negative_kinds':dict(negkinds),'input_rejections':12,
        'boundary_before_after_equal':True,'boundary_cost_counted_once_inside_first_production':True,
        'native_source':native,'actual_core_calls':data['actual_core_calls'],'native_calls_by_category':dict(native_by),
        'elapsed_seconds_before_serialization':data['elapsed_seconds_before_serialization'],
        'production_below_historical_comparator_cases':sum(c['production_digits']<c['historical_comparator_digits'] for c in cases),
        'failure_artifact_present':(ROOT/'TOP_BIT_FAST_FAILED_EXECUTION.json.gz').exists(),
        'scope':'Saved outer expression links, lazy setup/coefficient references, point routes, signed-to-typed outputs, actual native cells, historical pair updates, complete/partial replay and disjoint accounting. No scientific recomputation.',
        'admission':'AUTHOR_SHARED_CONTEXT_READBACK_NOT_FORMAL_ADMISSION'}
    with target.open('x',encoding='utf-8') as f:f.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'reader_sha256':result['reader_sha256'],
        'record_sha256':digest(target.read_bytes()),'streams':result['all_disjoint_current_streams_read'],
        'digits':total,'production_hotspots':result['production_hotspots'],'case_rows':cases}))


if __name__=='__main__':
    main()
