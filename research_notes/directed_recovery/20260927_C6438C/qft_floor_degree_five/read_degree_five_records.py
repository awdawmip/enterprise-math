"""Complete saved-record author readback, stdlib only.

Cursor arithmetic reads saved signed outputs and checks their input edges.
It never evaluates a scientific answer, imports a scientific runner, or
replays a primitive. Host additions below are indices and resource counts.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import gzip
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parent
HELPER = ROOT.parent/'sep27-qft-two-bit-aligned/guard_review/read_aligned_result.py'
HELPER_PIN = '6266405a29c589c67708149ee43942ff3fdde22a8da7966e123e58ab9bd3b450'
RAW_PIN = 'da675f8e04929116dac64552775f85ad75d39c71a03f78aad7c45d571fdf267e'
GZIP_PIN = 'b044570bb55e81ea0ff1fe73ef35af6fa7438281c2d6dac87c1c31f3ee251c9f'
GUARD_PIN = '6f718b837610e417935e468381b0da97d38203d551b04505e8264e71d8cf2c4f'
PINS = {
    'typed_floor_degree_five.py':'755fcaf04832a5328e2464214f736ac661c410b3505edf10ab5218f935e2a7c7',
    'check_degree_five.py':'975b574b85a3531da4443bf9f70cd4644ccc4ceadec81359506a2d00da3b1223',
    'DESIGN.md':'f6eb1b1e7b7dece0956e2ead166fbb9e901be3f5c9a44a1b367d1130206b7c22',
    'DEGREE_FIVE_RECIPROCITY.md':'1453444f21c113c0d1819328b731031d0fe296e25756caac7e94d9cf628047b6',
    'base_arithmetic':'633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2',
    'lazy_modular':'08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4',
    'sparse_modular':'fd9cbb019418a3c00890ba6e8cca5760e7e4d792bfd7b48306a71a66de301c46',
    'typed_integer_prechecks':'0a817aa8124cceb5440233d543073dae71de6ac1d0d4e5d50f4ee2b4808d99eb'}
ANCESTRY = {
    'base_arithmetic':'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
    'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
    'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
    'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}
CASES = ((0,5,3,1),(1,7,-3,-2),(4,5,0,3),(5,7,2,1),(6,5,13,-4),
         (7,4,-3,9),(8,9,7,-11),(9,7,0,21),(4,1,-2,3))
DEGREES = tuple((p,e) for e in range(6) for p in range(6-e))
BINOMIAL = ((1,),(1,1),(1,2,1),(1,3,3,1),(1,4,6,4,1),(1,5,10,10,5,1))
POWER_SUMS = ((1,((1,1),)),(2,((2,1),(1,-1))),
    (6,((3,2),(2,-3),(1,1))),(4,((4,1),(3,-2),(2,1))),
    (30,((5,6),(4,-15),(3,10),(1,-1))), (12,((6,2),(5,-6),(4,5),(2,-1))))
SCHEMA = 'BRC_DEGREE_FIVE_QUERY_CERTIFICATE_V1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


assert digest(HELPER.read_bytes()) == HELPER_PIN
spec = importlib.util.spec_from_file_location('pinned_aligned_saved_io',HELPER)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
io,same = old.io,old.same


class Cursor(io.RecordedCursor):
    def __init__(self,evidence):
        self.evidence = evidence
        self.ops = evidence['signed_operations']
        self.i = 0
        self.nodes = evidence['moment_nodes']
        self.node_map = {}
        self.completed = 0
        self.cache = {}
        self.requests = self.hits = self.depth = 0
        for index,node in enumerate(self.nodes):
            key = tuple(node['parameters'])
            assert key not in self.node_map and len(key) == 4
            assert all(type(x) is int for x in key) and key[0]>=0 and key[1]>=1
            assert set(node['moments']) == {f'{p},{e}' for p,e in DEGREES}
            assert 0 <= node['signed_operations_start'] <= node['signed_operations_stop'] <= len(self.ops)
            if node['child'] is not None:
                assert self.node_map[tuple(node['child'])][0] < index
            self.node_map[key] = (index,node)

    def exact_value(self,value,denominator):
        result,remainder = self.div(value,denominator)
        assert remainder == 0
        return result

    def power(self,value,exponent):
        result = 1
        for _ in range(exponent):
            result = self.mul(result,value)
        return result

    def sums(self,n):
        if not n:
            return (0,0,0,0,0,0)
        powers = [1,n]
        for _ in range(2,7):
            powers.append(self.mul(powers[-1],n))
        result = []
        for denominator,terms in POWER_SUMS:
            numerator = self.total(self.mul(c,powers[h]) for h,c in terms)
            result.append(self.exact_value(numerator,denominator))
        return tuple(result)

    def moments(self,n,m,a,b,depth=0):
        self.requests += 1
        self.depth = max(self.depth,depth)
        key = (n,m,a,b)
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        index,node = self.node_map[key]
        assert node['signed_operations_start'] == self.i
        sums = self.sums(n)
        values = {(p,e):sums[p] if e==0 else 0 for p,e in DEGREES}
        branch,child = 'empty',None
        details = {'maximum_total_degree':5,'normalization':None,'height':None,
                   'zero_coefficient_omissions':[],'reconstruction':[]}
        if n:
            begin = self.i
            A,a0 = self.div(a,m)
            B,b0 = self.div(b,m)
            details['normalization'] = {'A':A,'a0':a0,'B':B,'b0':b0,
                'signed_operations_start':begin,'signed_operations_stop':self.i}
            if A or B:
                branch,child = 'normalize_signed_coefficients',(n,m,a0,b0)
                g = self.moments(*child,depth=depth+1)
                for p,e in DEGREES:
                    if not e:
                        continue
                    begin = self.i
                    terms = []
                    for k in range(e+1):
                        for l in range(e-k+1):
                            if (A==0 and l>0) or (B==0 and e-k-l>0):
                                details['zero_coefficient_omissions'].append(
                                    {'p':p,'e':e,'k':k,'l':l,'A_zero':A==0,'B_zero':B==0})
                                continue
                            coefficient = self.mul(BINOMIAL[e][k],BINOMIAL[e-k][l])
                            coefficient = self.mul(coefficient,self.power(A,l))
                            coefficient = self.mul(coefficient,self.power(B,e-k-l))
                            terms.append(self.mul(coefficient,g[p+l,k]))
                    values[p,e] = self.total(terms)
                    details['reconstruction'].append({'p':p,'e':e,'value':values[p,e],
                        'signed_operations_start':begin,'signed_operations_stop':self.i})
            elif not a:
                branch = 'normalized_constant_zero'
            else:
                begin = self.i
                Y,remainder = self.div(self.add(self.mul(a,self.sub(n,1)),b),m)
                details['height'] = {'Y':Y,'remainder':remainder,
                    'signed_operations_start':begin,'signed_operations_stop':self.i}
                if not Y:
                    branch = 'normalized_zero_height'
                else:
                    offset = self.sub(self.add(self.sub(m,b),a),1)
                    branch,child = 'transpose_lattice',(Y,a,m,offset)
                    g = self.moments(*child,depth=depth+1)
                    for p,e in DEGREES:
                        if not e:
                            continue
                        begin = self.i
                        denominator,termspec = POWER_SUMS[p]
                        endpoint = self.mul(self.mul(denominator,self.power(Y,e)),sums[p])
                        terms = []
                        for v in range(e):
                            for h,c in termspec:
                                coefficient = self.mul(BINOMIAL[e][v],c)
                                terms.append(self.mul(coefficient,g[v,h]))
                        numerator = self.sub(endpoint,self.total(terms))
                        values[p,e] = self.exact_value(numerator,denominator)
                        details['reconstruction'].append({'p':p,'e':e,'denominator':denominator,
                            'numerator':numerator,'value':values[p,e],
                            'signed_operations_start':begin,'signed_operations_stop':self.i})
        same(node['branch'],branch)
        same(node['child'],child)
        same(node['degree_five_details'],details)
        same(node['moments'],{f'{p},{e}':values[p,e] for p,e in DEGREES})
        assert index == self.completed and node['signed_operations_stop'] == self.i
        self.completed += 1
        self.cache[key] = values
        return values

    def request(self,row):
        inp = row['inputs']
        assert set(inp) == {'n','m','a','b'} and all(type(x) is int for x in inp.values())
        key = tuple(inp[k] for k in ('n','m','a','b'))
        assert key[0]>=0 and key[1]>=1
        assert row['signed_operations_start'] == self.i and row['moment_nodes_start'] == self.completed
        assert row['cache_hit'] is (key in self.cache)
        values = self.moments(*key)
        same(row['outputs'],{f'{p},{e}':values[p,e] for p,e in DEGREES})
        assert row['signed_operations_stop'] == self.i and row['moment_nodes_stop'] == self.completed

    def finish(self,with_moments=True):
        assert self.i == len(self.ops)
        assert self.completed == len(self.nodes)
        if with_moments:
            same([self.requests,self.hits,self.depth],
                 [self.evidence['stats'][k] for k in ('moment_requests','cache_hits','max_recursion_depth')])
        else:
            same([self.evidence['stats'][k] for k in ('moment_requests','cache_hits','max_recursion_depth')],[0,0,0])


def inspect_evidence(e,native,kind):
    old.signed_typed_links(e)
    assert e['window_weight_queries'] == []
    if kind != 'partial':
        same(e['native_source'],native)
        if kind == 'brute':
            assert e['source_sha256'] == PINS['base_arithmetic']
            assert e['schema'] == 'BRC_DEGREE_THREE_FLOOR_MOMENTS_V1'
        else:
            assert e['source_sha256'] == PINS['typed_floor_degree_five.py']
            assert e['base_arithmetic_source_sha256'] == PINS['base_arithmetic']
            assert e['proof_sha256'] == PINS['DEGREE_FIVE_RECIPROCITY.md']
            assert e['schema'] == 'BRC_DEGREE_FIVE_SINGLE_FLOOR_MOMENTS_V1' and e['maximum_total_degree'] == 5
    view = dict(e,native_source=native)
    recounted = io.trace_accounting(view)
    observed_bits = max((abs(v).bit_length() for op in e['signed_operations']
        for v in op['inputs']+(op['result'] if type(op['result']) is list else [op['result']])),default=0)
    assert e['stats']['max_observed_integer_bits'] == observed_bits
    return {'signed_operations':len(e['signed_operations']), 'typed_operations':len(e['arithmetic_operations']),
            'moment_nodes':len(e['moment_nodes']), 'recounted_cost':recounted,
            'all_signed_to_typed_and_saved_native_cell_links_checked':True}


def inspect_certificate(cert,native,partial=False):
    assert cert['schema'] == ('INCOMPLETE_' if partial else '')+SCHEMA
    same(cert['source_bindings'],PINS)
    assert cert['complete_certificate'] is (not partial)
    if partial:
        assert cert['inflight_request'] is None
    else:
        assert cert['maximum_total_degree'] == 5
        same(cert['degrees'],DEGREES)
    e = cert['actual_integer_evidence']
    result = inspect_evidence(e,native,'partial' if partial else 'production')
    cursor = Cursor(e)
    for row in cert['requests']:
        cursor.request(row)
    cursor.finish()
    if partial:
        same(e['cache_entries'],[{'parameters':key,'moments':{f'{p},{ee}':v for (p,ee),v in vals.items()}}
                                for key,vals in cursor.cache.items()])
    result.update(requests=len(cert['requests']),all_21_moment_reconstruction_edges_checked=True,
        branches=dict(Counter(n['branch'] for n in e['moment_nodes'])))
    return result


def inspect_brute(record,native,expected):
    assert record['complete_comparator'] is True
    e = record['actual_integer_evidence']
    result = inspect_evidence(e,native,'brute')
    cursor = Cursor(e)
    n,m,a,b = [record['inputs'][k] for k in ('n','m','a','b')]
    buckets = {f'{p},{ee}':0 for p,ee in DEGREES}
    assert len(record['samples']) == n
    for j,row in enumerate(record['samples']):
        assert row['j'] == j and row['signed_operations_start'] == cursor.i
        affine = cursor.add(cursor.mul(a,j),b)
        quotient,remainder = cursor.div(affine,m)
        same([affine,quotient,remainder],[row['affine'],row['quotient'],row['remainder']])
        assert row['affine_operations_stop'] == row['powers_operations_start'] == cursor.i
        jp,qp = [1],[1]
        for _ in range(5):
            jp.append(cursor.mul(jp[-1],j))
            qp.append(cursor.mul(qp[-1],quotient))
        same([jp,qp],[row['index_powers'],row['quotient_powers']])
        assert row['powers_operations_stop'] == cursor.i and len(row['terms']) == 21
        for (p,ee),term in zip(DEGREES,row['terms']):
            key = f'{p},{ee}'
            assert term['signed_operations_start'] == cursor.i
            same([term['p'],term['e'],term['before']],[p,ee,buckets[key]])
            value = cursor.mul(jp[p],qp[ee])
            after = cursor.add(buckets[key],value)
            same([term['term'],term['after']],[value,after])
            buckets[key] = after
            assert term['signed_operations_stop'] == cursor.i
        assert row['signed_operations_stop'] == cursor.i
    cursor.finish(with_moments=False)
    same(buckets,record['outputs'])
    same(buckets,expected)
    result.update(samples=n,term_records=sum(len(row['terms']) for row in record['samples']),
        all_affine_power_and_bucket_edges_checked=True)
    return result


def aggregate(evidences):
    keys = ('typed_operations','adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
    total = {key:sum(e['arithmetic_stats'][key] for e in evidences) for key in keys}
    total['signed_operations'] = sum(len(e['signed_operations']) for e in evidences)
    total['moment_nodes'] = sum(len(e['moment_nodes']) for e in evidences)
    for key in ('moment_requests','cache_hits'):
        total[key] = sum(e['stats'][key] for e in evidences)
    return {'receipts':len(evidences),'sum':total,
        'max':{key:max((e['stats'][key] for e in evidences),default=0)
               for key in ('max_recursion_depth','max_observed_integer_bits')},
        'native_calls_counted_from_disjoint_process_intervals':True}


def check_cost(e,cost):
    same(cost['arithmetic_stats'],e['arithmetic_stats'])
    same(cost['moment_stats'],e['stats'])
    for key,field in (('typed_operations','arithmetic_operations'),('signed_operations','signed_operations'),('moment_nodes','moment_nodes')):
        assert cost[key] == len(e[field])


def main():
    compressed = (ROOT/'DEGREE_FIVE_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert digest(raw) == RAW_PIN and digest(compressed) == GZIP_PIN
    assert len(raw) == 88217988 and len(compressed) == 3468068
    data = json.loads(raw)
    summary = json.loads((ROOT/'DEGREE_FIVE_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASS'
    same(data['source_bindings'],PINS)
    same(summary['source_bindings'],PINS)
    assert summary['payload_sha256'] == RAW_PIN and summary['artifact_sha256'] == GZIP_PIN
    assert summary['raw_bytes'] == len(raw) and summary['gzip_bytes'] == len(compressed)
    for name,pin in PINS.items():
        path = ROOT.parent/ANCESTRY[name] if name in ANCESTRY else ROOT/name
        assert digest(path.read_bytes()) == pin
    guard = (ROOT/'STARTUP_GUARD.json').read_bytes()
    assert digest(guard) == GUARD_PIN == data['startup_guard']['sha256']
    same(json.loads(guard),data['startup_guard']['receipt'])
    receipt = data['startup_guard']['receipt']
    assert receipt['activity_allowed'] is True and receipt['persistence_allowed'] is True and receipt['sync_debt_events'] == []
    assert receipt['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC' and receipt['mode'] == 'TASK_RESEARCH' and receipt['boundary'] == 'startup'
    native = data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    same(native['files_sha256'],{key:PINS[key] for key in ('lazy_modular','sparse_modular','typed_integer_prechecks')})
    assert native['primitive_source'] == '0852cad130c1d877174d235687cf60c19f318c58'
    adder = native['native_adder']
    assert adder['input_columns'] == 8 and adder['positive_BRC_input_states'] == 12
    same(adder['columns'],[[0,0],[1,0],[1,0],[0,1],[1,0],[0,1],[0,1],[1,1]])
    same(adder['vendor'],{'commit':'bc7babbb9e890f6d5a7094430a5fbdccf66c77ad',
        'git_blob':'4e6b3132580e3cd70a20a0d8bd4d28792b961afb','path':'src/enterprise_math/brc_weighted_recurrent.py',
        'sha256':'7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'})
    groups = {key:[] for key in ('production','typed_finite_sums','positive_replay','cache_control','cache_control_replay','negative_replay')}
    cases,certs,comparisons = [],[],[]
    assert len(data['cases']) == 9
    for index,row in enumerate(data['cases']):
        same([row['inputs'][k] for k in ('n','m','a','b')],CASES[index])
        cert = row['certificate']
        verify = row['verification']
        replay = verify['replay_certificate']
        assert verify['verified'] is True and verify['requests_replayed'] == 1
        assert io.semantic(cert) == io.semantic(replay)
        assert row['all_21_moments_equal'] is True and len(row['values']) == 21
        same(row['values'],cert['requests'][0]['outputs'])
        same(row['inputs'],cert['requests'][0]['inputs'])
        same(row['inputs'],row['typed_finite_sums']['inputs'])
        cases.append({'inputs':row['inputs'],'values':row['values'],
            'production':inspect_certificate(cert,native),
            'typed_finite_sums':inspect_brute(row['typed_finite_sums'],native,row['values']),
            'positive_replay':inspect_certificate(replay,native)})
        certs.append(cert)
        for category,e,costkey in (
            ('production',cert['actual_integer_evidence'],'production_cost'),
            ('typed_finite_sums',row['typed_finite_sums']['actual_integer_evidence'],'typed_finite_sum_cost'),
            ('positive_replay',replay['actual_integer_evidence'],'positive_replay_cost')):
            groups[category].append(e)
            check_cost(e,row[costkey])
        prod = row['production_cost']['arithmetic_stats']['adder_digit_replays']
        brute = row['typed_finite_sum_cost']['arithmetic_stats']['adder_digit_replays']
        comparisons.append({'inputs':row['inputs'],'production_digits':prod,'finite_sum_digits':brute,
                            'production_strictly_less':prod<brute})
    cache = data['cache_and_reuse_control']
    cc,cr = cache['certificate'],cache['verification']['replay_certificate']
    assert cache['verification']['verified'] is True and cache['verification']['requests_replayed'] == 2
    assert io.semantic(cc) == io.semantic(cr)
    same([r['cache_hit'] for r in cc['requests']],[False,True])
    same(cc['requests'][0]['outputs'],cc['requests'][1]['outputs'])
    same(cc['requests'][0]['inputs'],data['cases'][3]['inputs'])
    cache_review = {'production':inspect_certificate(cc,native),'positive_replay':inspect_certificate(cr,native)}
    groups['cache_control'].append(cc['actual_integer_evidence'])
    groups['cache_control_replay'].append(cr['actual_integer_evidence'])
    boundaries = []
    for boundary in (data['production_boundary_rejection'],cache['invalid_boundary']):
        assert boundary['rejected'] is True and boundary['additional_typed_operations'] == boundary['additional_native_calls'] == 0
        same(boundary['before'],boundary['after'])
        same(boundary['before']['requests'],cc['requests'][:1])
        boundaries.append(inspect_certificate(boundary['before'],native,partial=True))
    assert len(data['input_rejections']) == summary['input_rejections'] == 10
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations'] == 0
        assert row['call_interval']['start'] == row['call_interval']['stop']
    negatives = []
    expected = ['output_degree_five','input_valid_changed','node_output','normalization','transpose_child',
        'exact_numerator','omitted_zero_coefficient','signed_trace','native_source','paid_cost',
        'valid_prefix_then_invalid','source_early','proof_early','schema_early','bool_input_early',
        'nonstring_key_early','bool_runtime_counter_early']
    same([row['name'] for row in data['negative_checks']],expected)
    for row in data['negative_checks']:
        assert row['rejected'] is True
        attempted = old.decode_keys(row['attempted_certificate_typed_key_encoding'])
        captured = row['actual_replay_certificates']
        if row['name'].endswith('_early'):
            assert not captured and row['call_interval']['start'] == row['call_interval']['stop']
            result = {'type':'early','paid_receipts':0}
        else:
            assert len(captured) == 1
            replay = captured[0]
            groups['negative_replay'].append(replay['actual_integer_evidence'])
            if row['name'] == 'valid_prefix_then_invalid':
                same(replay['requests'],certs[row['source_case_index']]['requests'])
                same(replay['requests'],attempted['requests'][:1])
                assert attempted['requests'][1]['inputs']['m'] == 0
                result = inspect_certificate(replay,native,partial=True)
                result['type'] = 'paid_prefix'
            else:
                assert io.semantic(replay) != io.semantic(attempted)
                if row['name'] != 'input_valid_changed':
                    assert io.semantic(replay) == io.semantic(certs[row['source_case_index']])
                else:
                    same(replay['requests'][0]['inputs'],attempted['requests'][0]['inputs'])
                result = inspect_certificate(replay,native)
                result['type'] = 'paid_full'
            result['paid_receipts'] = 1
        result.update(name=row['name'],kind=row['kind'],error=row['error'])
        negatives.append(result)
    assert Counter(r['type'] for r in negatives) == {'early':6,'paid_full':10,'paid_prefix':1}
    same(dict(Counter(r['kind'] for r in negatives)),summary['negative_kinds'])
    calculated = {key:aggregate(es) for key,es in groups.items()}
    same(calculated,data['cost_categories'])
    same(calculated,summary['cost_categories'])
    assert sum(len(es) for es in groups.values()) == 40
    calls,frontier = Counter(),0
    for row in data['call_intervals']:
        assert row['start'] == frontier and row['stop'] >= frontier
        calls[row['category']] += row['stop']-row['start']
        frontier = row['stop']
    same(dict(calls),data['native_calls_by_category'])
    same(dict(calls),summary['native_calls_by_category'])
    assert frontier == len(data['actual_core_calls']) == data['actual_core_call_count'] == 1
    assert data['actual_core_calls'][0]['states'] == 12 and data['actual_core_calls'][0]['depth'] == 1
    assert data['actual_core_calls'][0]['entrypoint'] == 'recurrent_mass_power'
    # Empty-case export initializes the shared native catalog outside any
    # arithmetic operation, so all per-Arithmetic deltas are zero this run.
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for es in groups.values() for e in es) == 0
    assert data['call_intervals'][0] == {'category':'production','label':repr(CASES[0]),'start':0,'stop':1}
    totals = {key:sum(row['sum'][key] for row in calculated.values()) for key in calculated['production']['sum']}
    samples = sum(c['typed_finite_sums']['samples'] for c in cases)
    terms = sum(c['typed_finite_sums']['term_records'] for c in cases)
    assert samples == 44 and terms == 924
    coverage = {'cases':9,'moment_equalities':189,'finite_sum_samples':44,
        'branch_types':sorted({n['branch'] for c in certs for n in c['actual_integer_evidence']['moment_nodes']}),
        'extra_cache_queries':2,'scientific_failure_injection_performed':False}
    same(coverage,data['coverage'])
    same(coverage,summary['coverage'])
    assert data['full_shor_sampling_performed'] is False and data['mixed_floor_algorithm_implemented'] is False
    result = {'status':'PASS_COMPLETE_SAVED_RECORD_AUTHOR_REVIEW',
        'scope':'Shared-context checker author; complete stdlib-only saved evidence traversal, no scientific imports or re-execution',
        'reader_sha256':digest(Path(__file__).read_bytes()),'source_bindings':PINS,
        'io_helpers':{'aligned':HELPER_PIN,'direct':old.HELPER_PIN},
        'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,'raw_bytes':len(raw),'gzip_bytes':len(compressed),
        'startup_guard_sha256':GUARD_PIN,'native_source':native,'actual_core_calls':data['actual_core_calls'],
        'cases':cases,'coverage':coverage,'finite_sum_term_records_checked':terms,
        'cache_and_reuse_control':cache_review,'overlapping_boundary_snapshots_not_charged_again':boundaries,
        'negative_checks':negatives,'input_rejections':data['input_rejections'],
        'charged_streams':40,'cost_categories':calculated,'total_run_cost':totals,
        'native_calls_by_category':dict(calls),
        'catalog_initialization':'First empty production export; global CALLS=1, per-Arithmetic deltas sum to zero',
        'per_case_comparison':comparisons,'elapsed_seconds_before_serialization':data['elapsed_seconds_before_serialization'],
        'unexpected_failure_artifact_present':(ROOT/'DEGREE_FIVE_FAILED_EXECUTION.json.gz').exists(),
        'scientific_execution_performed_by_reader':False,'comparison_is_timing_benchmark':False,
        'limits':['All signed edges, recursive outputs, preserved typed traces and source-bound native cells were read, not numerically recomputed.',
                  'The changed-valid-input negative replays its changed input, not the old fixture.',
                  'Only the declared native-call cache delta is omitted in full fresh semantic equality.',
                  'No deliberate mid-arithmetic interruption was tested; available-field failure preservation is source-reviewed.',
                  'Digit counters exclude hashing, allocation, JSON, metadata and other uninstrumented host work.',
                  'No practical speedup, general mixed-floor closure, order discovery or Shor completion is claimed.']}
    target = ROOT/'DEGREE_FIVE_RECORD_READBACK.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'charged_streams':40,'totals':totals,
        'production_vs_finite_sum':comparisons,'sha256':digest(target.read_bytes())}))


if __name__ == '__main__':
    main()
