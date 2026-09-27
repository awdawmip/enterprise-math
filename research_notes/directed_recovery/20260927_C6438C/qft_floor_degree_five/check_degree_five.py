"""Declared degree-five checker and serialized replay API; code-only until authorized.

The reference sums use only the inherited actual signed integer primitives,
never the recurrence, power-sum identities, Python pow, or host division.
"""
from copy import deepcopy
from pathlib import Path
import gzip
import hashlib
import json
import sys
import time
import traceback

from typed_floor_degree_five import FloorDegreeFiveRunner, BASE, BASE_PIN, PROOF_PIN, sha
from typed_floor_moments import TypedFloorMoments, require
from stage45.brc_loop_recheck import CALLS

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SOURCE_PIN = '755fcaf04832a5328e2464214f736ac661c410b3505edf10ab5218f935e2a7c7'
SCHEMA = 'BRC_DEGREE_FIVE_QUERY_CERTIFICATE_V1'
SOURCE_NAMES = ('typed_floor_degree_five.py', 'check_degree_five.py',
                'DESIGN.md', 'DEGREE_FIVE_RECIPROCITY.md')
DEGREES = tuple((p, e) for e in range(6) for p in range(6-e))
CASES = ((0,5,3,1), (1,7,-3,-2), (4,5,0,3), (5,7,2,1),
         (6,5,13,-4), (7,4,-3,9), (8,9,7,-11), (9,7,0,21), (4,1,-2,3))
NATIVE_PATHS = {
    'lazy_modular': (ROOT.parent/'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
                    '08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4'),
    'sparse_modular': (ROOT.parent/'sep26-shor-general/sparse/sparse_modular.py',
                       'fd9cbb019418a3c00890ba6e8cca5760e7e4d792bfd7b48306a71a66de301c46'),
    'typed_integer_prechecks': (ROOT.parent/'sep26-shor-general/completion/typed_integer_prechecks.py',
                              '0a817aa8124cceb5440233d543073dae71de6ac1d0d4e5d50f4ee2b4808d99eb')}
TARGETS = (ROOT/'DEGREE_FIVE_RESULTS.json.gz', ROOT/'DEGREE_FIVE_SUMMARY.json',
           ROOT/'DEGREE_FIVE_FAILED_EXECUTION.json.gz')
LIVE = {'stage':'IMPORTED_NOT_STARTED', 'output':None, 'guard':None, 'observer':None,
        'brute':None, 'replay_observer':None, 'replay_capture':[], 'tamper_attempts':[],
        'current_tamper':None, 'input_attempts':[], 'current_input':None, 'call_intervals':[]}


def pins():
    result = {name:sha(ROOT/name) for name in SOURCE_NAMES}
    require(result['typed_floor_degree_five.py'] == SOURCE_PIN, 'extension source mismatch')
    require(result['DEGREE_FIVE_RECIPROCITY.md'] == PROOF_PIN, 'proof mismatch')
    require(sha(BASE/'typed_floor_moments.py') == BASE_PIN, 'base arithmetic mismatch')
    result['base_arithmetic'] = BASE_PIN
    for key, (path, pin) in NATIVE_PATHS.items():
        require(sha(path) == pin, 'native ancestry mismatch: '+key)
        result[key] = pin
    return result


def strict_json(value):
    """JSON-compatible exact structure, distinguishing bool/int and key types."""
    if type(value) is dict:
        require(all(type(k) is str for k in value), 'only string object keys allowed')
        return {k:strict_json(v) for k,v in value.items()}
    if type(value) in (tuple, list):
        return [strict_json(x) for x in value]
    require(value is None or type(value) in (str, int, bool), 'non-exact JSON value')
    return value


def semantic_certificate(certificate):
    normalized = strict_json(certificate)
    require(type(normalized) is dict, 'certificate object required')
    evidence = normalized.get('actual_integer_evidence')
    require(type(evidence) is dict and type(evidence.get('arithmetic_stats')) is dict,
            'complete arithmetic statistics required')
    stats = evidence['arithmetic_stats']
    require('native_kernel_calls_delta' in stats, 'runtime native-call field required')
    value = stats['native_kernel_calls_delta']
    require(type(value) is int and value >= 0, 'invalid runtime native-call counter')
    del stats['native_kernel_calls_delta']
    return json.dumps(normalized, sort_keys=True, separators=(',',':'))


def input_values(n, m, a, b):
    require(all(type(x) is int for x in (n,m,a,b)) and n >= 0 and m >= 1,
            'strict integer n>=0, m>=1 and signed a,b required')
    return {'n':n, 'm':m, 'a':a, 'b':b}


def raw_runner(runner):
    """Snapshot fields only: no export, source_binding, arithmetic, or native calls."""
    return deepcopy({'arithmetic_operations':runner.arithmetic.operations,
        'arithmetic_stats':runner.arithmetic.stats, 'signed_operations':runner.signed_operations,
        'moment_nodes':runner.nodes, 'window_weight_queries':runner.weight_queries,
        'stats':runner.stats,
        'cache_entries':[{'parameters':key, 'moments':{f'{p},{e}':v for (p,e),v in row.items()}}
                         for key,row in runner.cache.items()]})


class DegreeFiveObserver:
    def __init__(self):
        self.source_pins = pins()
        self.runner = FloorDegreeFiveRunner()
        self.requests = []
        self.inflight = None

    def _check(self):
        require(pins() == self.source_pins, 'observer source changed')
        require(self.inflight is None, 'incomplete arithmetic request: new observer required')

    def query(self, n, m, a, b):
        self._check()
        inputs = input_values(n,m,a,b)
        r = self.runner
        self.inflight = {'inputs':inputs, 'signed_operations_start':len(r.signed_operations),
                         'moment_nodes_start':len(r.nodes), 'cache_hit':(n,m,a,b) in r.cache}
        values = r.moments(n,m,a,b)
        require(set(values) == set(DEGREES), 'incomplete degree-five moment family')
        self.inflight.update(outputs={f'{p},{e}':values[p,e] for p,e in DEGREES},
            signed_operations_stop=len(r.signed_operations), moment_nodes_stop=len(r.nodes))
        row = self.inflight
        self.requests.append(row)
        self.inflight = None
        return deepcopy(row)

    def incomplete_snapshot(self):
        return deepcopy({'schema':'INCOMPLETE_'+SCHEMA, 'source_bindings':self.source_pins,
            'complete_certificate':False, 'requests':self.requests, 'inflight_request':self.inflight,
            'actual_integer_evidence':raw_runner(self.runner),
            'scope':'Completed child nodes and raw operations retained; no uncompleted parent node asserted'})

    def export_certificate(self):
        self._check()
        return deepcopy({'schema':SCHEMA, 'source_bindings':self.source_pins,
            'complete_certificate':True, 'maximum_total_degree':5,
            'degrees':[list(x) for x in DEGREES], 'requests':self.requests,
            'actual_integer_evidence':self.runner.evidence(),
            'scope':'Exact fixed-degree single-floor moments only; no mixed-floor or Shor completion',
            'admission':'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED'})


def verify_degree_five_certificate(certificate, *, replay_capture=None):
    """Accept decoded serialized JSON; always perform a fresh actual replay.

    Only the process-cache-dependent native-call delta is omitted from equality.
    Invalid later requests preserve a complete paid prefix, never a full cert.
    """
    require(replay_capture is None or type(replay_capture) is list, 'list capture required')
    semantic_certificate(certificate)
    require(type(certificate) is dict and certificate.get('schema') == SCHEMA, 'wrong schema')
    require(certificate.get('complete_certificate') is True, 'complete certificate required')
    require(strict_json(certificate.get('source_bindings')) == pins(), 'source/proof binding mismatch')
    requests = certificate.get('requests')
    require(type(requests) is list, 'request list required')
    observer = DegreeFiveObserver()
    LIVE['replay_observer'] = observer
    try:
        for request in requests:
            require(type(request) is dict and type(request.get('inputs')) is dict, 'malformed request')
            inputs = request['inputs']
            require(set(inputs) == {'n','m','a','b'}, 'unexpected input fields')
            observer.query(inputs['n'],inputs['m'],inputs['a'],inputs['b'])
        replay = observer.export_certificate()
    except BaseException:
        if replay_capture is not None and (observer.requests or observer.inflight is not None
                                          or observer.runner.arithmetic.operations):
            replay_capture.append(observer.incomplete_snapshot())
        raise
    if replay_capture is not None:
        replay_capture.append(deepcopy(replay))
    require(semantic_certificate(certificate) == semantic_certificate(replay), 'full certificate replay mismatch')
    return {'verified':True, 'requests_replayed':len(requests), 'replay_certificate':replay,
            'excluded_runtime_field':'actual_integer_evidence.arithmetic_stats.native_kernel_calls_delta'}


class TypedFiniteSums:
    """Independent finite enumeration; base arithmetic only, no moment methods."""
    def __init__(self):
        self.runner = TypedFloorMoments()
        self.samples = []
        self.inputs = None
        self.inflight = None
        self.outputs = {f'{p},{e}':0 for p,e in DEGREES}

    def run(self, n, m, a, b):
        require(self.inputs is None, 'finite comparator is one-shot')
        self.inputs = input_values(n,m,a,b)
        r = self.runner
        for j in range(n):
            self.inflight = {'j':j, 'signed_operations_start':len(r.signed_operations), 'terms':[]}
            affine = r.add(r.mul(a,j),b)
            quotient,remainder = r.floor_div(affine,m)
            self.inflight.update(affine=affine, quotient=quotient, remainder=remainder,
                                 affine_operations_stop=len(r.signed_operations))
            powers_start = len(r.signed_operations)
            jp,qp = [1],[1]
            for _ in range(5):
                jp.append(r.mul(jp[-1],j))
                qp.append(r.mul(qp[-1],quotient))
            self.inflight.update(index_powers=jp, quotient_powers=qp,
                powers_operations_start=powers_start, powers_operations_stop=len(r.signed_operations))
            for p,e in DEGREES:
                key = f'{p},{e}'
                start = len(r.signed_operations)
                before = self.outputs[key]
                term = r.mul(jp[p],qp[e])
                after = r.add(before,term)
                self.outputs[key] = after
                self.inflight['terms'].append({'p':p,'e':e,'before':before,'term':term,'after':after,
                    'signed_operations_start':start,'signed_operations_stop':len(r.signed_operations)})
            self.inflight['signed_operations_stop'] = len(r.signed_operations)
            self.samples.append(self.inflight)
            self.inflight = None
        return deepcopy(self.outputs)

    def incomplete_snapshot(self):
        return deepcopy({'complete_comparator':False, 'inputs':self.inputs, 'samples':self.samples,
            'inflight_sample':self.inflight, 'current_outputs':self.outputs,
            'actual_integer_evidence':raw_runner(self.runner)})

    def evidence(self):
        require(self.inputs is not None and self.inflight is None, 'incomplete comparator')
        require(len(self.samples) == self.inputs['n'], 'missing finite-sum samples')
        return deepcopy({'complete_comparator':True, 'inputs':self.inputs, 'samples':self.samples,
            'outputs':self.outputs, 'actual_integer_evidence':self.runner.evidence(),
            'reference_route':'Actual signed affine evaluation, division, repeated multiply and bucket addition; no recurrence'})


def typed_keys(value):
    if type(value) is dict:
        return {'object_entries':[{'key_type':type(k).__name__,'key':k,'value':typed_keys(v)} for k,v in value.items()]}
    if type(value) in (list,tuple):
        return [typed_keys(x) for x in value]
    return value


def interval(category, label, start):
    row = {'category':category,'label':label,'start':start,'stop':len(CALLS)}
    LIVE['call_intervals'].append(row)
    return row


def cost(evidence):
    return {'arithmetic_stats':deepcopy(evidence['arithmetic_stats']),
        'typed_operations':len(evidence['arithmetic_operations']), 'signed_operations':len(evidence['signed_operations']),
        'moment_nodes':len(evidence['moment_nodes']), 'moment_stats':deepcopy(evidence['stats'])}


def aggregate(evidences):
    rows = [cost(e) for e in evidences]
    keys = ('typed_operations','adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
    totals = {key:sum(row['arithmetic_stats'][key] for row in rows) for key in keys}
    require(totals['typed_operations'] == sum(row['typed_operations'] for row in rows), 'typed cost mismatch')
    for key in ('signed_operations','moment_nodes'):
        totals[key] = sum(row[key] for row in rows)
    for key in ('moment_requests','cache_hits'):
        totals[key] = sum(row['moment_stats'][key] for row in rows)
    return {'receipts':len(rows),'sum':totals,
        'max':{key:max((row['moment_stats'][key] for row in rows),default=0)
               for key in ('max_recursion_depth','max_observed_integer_bits')},
        'native_calls_counted_from_disjoint_process_intervals':True}


def boundary_rejection(observer):
    before = observer.incomplete_snapshot()
    first = len(CALLS)
    try:
        observer.query(2,0,1,1)
    except ValueError as error:
        after = observer.incomplete_snapshot()
        assert before == after and first == len(CALLS)
        return {'args':[2,0,1,1],'rejected':True,'error':str(error),'before':before,'after':after,
            'additional_typed_operations':0,'additional_native_calls':0,
            'cost_containment':'Overlapping snapshots inside production; not a second charged stream'}
    raise AssertionError('invalid input accepted after a completed query')


def input_rejections():
    bad = ((True,5,3,1),(-1,5,3,1),(1,0,3,1),(1,-2,3,1),(1,True,3,1),
           (1,5,False,1),(1,5,3,True),(1,5,'3',1),(1,5,3,None),(1.0,5,3,1))
    records = []
    LIVE['input_attempts'] = records
    for args in bad:
        start = len(CALLS)
        observer = DegreeFiveObserver()
        LIVE.update(observer=observer,current_input=typed_keys(args))
        before = observer.incomplete_snapshot()
        try:
            observer.query(*args)
        except ValueError as error:
            after = observer.incomplete_snapshot()
            assert before == after and start == len(CALLS)
            records.append({'args':args,'rejected':True,'error':str(error),'actual_typed_operations':0,
                'call_interval':interval('input_rejection',repr(args),start)})
        else:
            raise AssertionError('invalid inputs accepted')
    LIVE['current_input'] = None
    return records


def find_node(certificate, branch):
    return next(row for row in certificate['actual_integer_evidence']['moment_nodes'] if row['branch'] == branch)


def negatives(certificates):
    changes = (
        ('output_degree_five',4,lambda c:c['requests'][0]['outputs'].__setitem__('0,5',999)),
        ('input_valid_changed',4,lambda c:c['requests'][0]['inputs'].__setitem__('b',-3)),
        ('node_output',4,lambda c:c['actual_integer_evidence']['moment_nodes'][-1]['moments'].__setitem__('5,0',999)),
        ('normalization',4,lambda c:find_node(c,'normalize_signed_coefficients')['degree_five_details']['normalization'].__setitem__('A',999)),
        ('transpose_child',3,lambda c:find_node(c,'transpose_lattice').__setitem__('child',[999,1,1,0])),
        ('exact_numerator',3,lambda c:find_node(c,'transpose_lattice')['degree_five_details']['reconstruction'][0].__setitem__('numerator',999)),
        ('omitted_zero_coefficient',7,lambda c:find_node(c,'normalize_signed_coefficients')['degree_five_details']['zero_coefficient_omissions'].pop()),
        ('signed_trace',4,lambda c:c['actual_integer_evidence']['signed_operations'][0].__setitem__('result',999)),
        ('native_source',4,lambda c:c['actual_integer_evidence']['native_source'].__setitem__('primitive_source','0'*40)),
        ('paid_cost',4,lambda c:c['actual_integer_evidence']['arithmetic_stats'].__setitem__('adder_digit_replays',999)),
        ('valid_prefix_then_invalid',3,lambda c:c['requests'].append({'inputs':{'n':1,'m':0,'a':1,'b':0}})),
        ('source_early',0,lambda c:c['source_bindings'].__setitem__('typed_floor_degree_five.py','0'*64)),
        ('proof_early',0,lambda c:c['source_bindings'].__setitem__('DEGREE_FIVE_RECIPROCITY.md','0'*64)),
        ('schema_early',0,lambda c:c.__setitem__('schema','UNRELATED')),
        ('bool_input_early',0,lambda c:c['requests'][0]['inputs'].__setitem__('n',False)),
        ('nonstring_key_early',0,lambda c:c['requests'][0].__setitem__(0,0)),
        ('bool_runtime_counter_early',0,lambda c:c['actual_integer_evidence']['arithmetic_stats'].__setitem__('native_kernel_calls_delta',False)))
    records = []
    LIVE['tamper_attempts'] = records
    for name,index,change in changes:
        attempted = deepcopy(certificates[index])
        change(attempted)
        # Python equality identifies False with 0; the attempted JSON types
        # must be distinguished even in the deliberately rejected input.
        assert json.dumps(typed_keys(attempted),sort_keys=True) != json.dumps(typed_keys(certificates[index]),sort_keys=True)
        capture = []
        LIVE.update(replay_capture=capture,current_tamper={'name':name,'source_case_index':index,'attempt':typed_keys(attempted)})
        start = len(CALLS)
        try:
            verify_degree_five_certificate(attempted,replay_capture=capture)
        except ValueError as error:
            if name.endswith('_early'):
                assert not capture and start == len(CALLS)
                kind = 'EARLY_ZERO_WORK_REJECTION'
            elif name == 'valid_prefix_then_invalid':
                assert len(capture) == 1 and capture[0]['complete_certificate'] is False
                assert capture[0]['inflight_request'] is None and len(capture[0]['requests']) == 1
                assert capture[0]['requests'] == certificates[index]['requests']
                assert capture[0]['actual_integer_evidence']['arithmetic_operations']
                kind = 'PAID_VALID_PREFIX_THEN_INPUT_REJECTION'
            else:
                assert len(capture) == 1 and capture[0]['complete_certificate'] is True
                if name != 'input_valid_changed':
                    assert semantic_certificate(capture[0]) == semantic_certificate(certificates[index])
                else:
                    assert capture[0]['requests'][0]['inputs'] == attempted['requests'][0]['inputs']
                kind = 'COMPLETE_PAID_REPLAY_THEN_MISMATCH'
            records.append({'name':name,'source_case_index':index,'rejected':True,'kind':kind,'error':str(error),
                'attempted_certificate_typed_key_encoding':typed_keys(attempted),'actual_replay_certificates':capture,
                'call_interval':interval('negative_replay',name,start)})
        else:
            raise AssertionError('forged certificate accepted: '+name)
    LIVE['current_tamper'] = None
    return records


def main():
    started = time.perf_counter()
    LIVE['stage'] = 'STARTUP_GUARD'
    guard = json.loads((ROOT/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events'] == []
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC' and guard['mode'] == 'TASK_RESEARCH' and guard['boundary'] == 'startup'
    LIVE['guard'] = {'sha256':sha(ROOT/'STARTUP_GUARD.json'),'receipt':guard}
    sources = pins()
    assert len(CALLS) == 0, 'requires fresh process with no previous scientific calls'
    output = {'status':'RUNNING','source_bindings':sources,'startup_guard':LIVE['guard'],'cases':[]}
    LIVE['output'] = output
    certificates = []
    for index,args in enumerate(CASES):
        LIVE.update(stage='PRODUCTION',current_case=args)
        start = len(CALLS)
        observer = DegreeFiveObserver()
        LIVE['observer'] = observer
        observer.query(*args)
        if index == 3:
            output['production_boundary_rejection'] = boundary_rejection(observer)
        cert = observer.export_certificate()
        prod_interval = interval('production',repr(args),start)
        LIVE['stage'] = 'TYPED_FINITE_SUMS'
        start = len(CALLS)
        brute = TypedFiniteSums()
        LIVE['brute'] = brute
        values = brute.run(*args)
        enumeration = brute.evidence()
        brute_interval = interval('typed_finite_sums',repr(args),start)
        assert values == cert['requests'][0]['outputs']
        LIVE['stage'] = 'POSITIVE_REPLAY'
        start = len(CALLS)
        capture = []
        LIVE['replay_capture'] = capture
        verification = verify_degree_five_certificate(json.loads(json.dumps(cert)),replay_capture=capture)
        assert len(capture) == 1
        replay_interval = interval('positive_replay',repr(args),start)
        output['cases'].append({'inputs':dict(zip(('n','m','a','b'),args)), 'values':values,
            'all_21_moments_equal':True,'certificate':cert,'typed_finite_sums':enumeration,'verification':verification,
            'production_cost':cost(cert['actual_integer_evidence']),
            'typed_finite_sum_cost':cost(enumeration['actual_integer_evidence']),
            'positive_replay_cost':cost(verification['replay_certificate']['actual_integer_evidence']),
            'call_intervals':[prod_interval,brute_interval,replay_interval]})
        certificates.append(cert)
        print(json.dumps({'stage':'CASE_COMPLETE','inputs':args,'all_21_moments_equal':True}),flush=True)
    # A separate new observer checks invalid-input reuse followed by a cache
    # hit. Its first computation and its fresh replay are explicitly charged.
    LIVE['stage'] = 'CACHE_AND_REUSE_CONTROL'
    start = len(CALLS)
    observer = DegreeFiveObserver()
    LIVE['observer'] = observer
    first = observer.query(*CASES[3])
    boundary = boundary_rejection(observer)
    again = observer.query(*CASES[3])
    assert first['outputs'] == again['outputs'] and again['cache_hit'] is True
    assert again['signed_operations_start'] == again['signed_operations_stop']
    assert again['moment_nodes_start'] == again['moment_nodes_stop']
    cache_cert = observer.export_certificate()
    cache_interval = interval('cache_control','query_invalid_cached_query',start)
    start = len(CALLS)
    LIVE['replay_capture'] = []
    cache_verify = verify_degree_five_certificate(json.loads(json.dumps(cache_cert)),replay_capture=LIVE['replay_capture'])
    output['cache_and_reuse_control'] = {'certificate':cache_cert,'verification':cache_verify,
        'invalid_boundary':boundary,'call_intervals':[cache_interval,interval('cache_control_replay','query_invalid_cached_query',start)]}
    LIVE['stage'] = 'INPUT_REJECTIONS'
    output['input_rejections'] = input_rejections()
    LIVE['stage'] = 'TAMPER_REJECTIONS'
    output['negative_checks'] = negatives(certificates)
    branches = {node['branch'] for cert in certificates for node in cert['actual_integer_evidence']['moment_nodes']}
    assert {'empty','normalize_signed_coefficients','normalized_constant_zero','normalized_zero_height','transpose_lattice'} <= branches
    streams = {
        'production':[c['actual_integer_evidence'] for c in certificates],
        'typed_finite_sums':[row['typed_finite_sums']['actual_integer_evidence'] for row in output['cases']],
        'positive_replay':[row['verification']['replay_certificate']['actual_integer_evidence'] for row in output['cases']],
        'cache_control':[cache_cert['actual_integer_evidence']],
        'cache_control_replay':[cache_verify['replay_certificate']['actual_integer_evidence']],
        'negative_replay':[c['actual_integer_evidence'] for row in output['negative_checks'] for c in row['actual_replay_certificates']]}
    costs = {key:aggregate(value) for key,value in streams.items()}
    native_by,frontier = {},0
    for row in LIVE['call_intervals']:
        assert row['start'] == frontier and row['stop'] >= frontier
        native_by[row['category']] = native_by.get(row['category'],0)+row['stop']-row['start']
        frontier = row['stop']
    assert frontier == len(CALLS) == 1, 'one actual native catalog expected in this fresh process'
    assert sources == pins() and sha(ROOT/'STARTUP_GUARD.json') == LIVE['guard']['sha256']
    output.update(status='PASS',coverage={'cases':9,'moment_equalities':189,'finite_sum_samples':sum(x[0] for x in CASES),
        'branch_types':sorted(branches),'extra_cache_queries':2,'scientific_failure_injection_performed':False},
        cost_categories=costs,native_calls_by_category=native_by,call_intervals=deepcopy(LIVE['call_intervals']),
        actual_core_calls=deepcopy(CALLS),actual_core_call_count=len(CALLS),
        elapsed_seconds_before_serialization=time.perf_counter()-started,
        full_shor_sampling_performed=False,mixed_floor_algorithm_implemented=False)
    LIVE['stage'] = 'SERIALIZE_SUCCESS'
    raw = json.dumps(output,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[0].open('xb') as handle:
        handle.write(gzip.compress(raw,compresslevel=6,mtime=0))
    summary = {'status':'PASS','source_bindings':sources,'coverage':output['coverage'],
        'input_rejections':len(output['input_rejections']),'negative_checks':len(output['negative_checks']),
        'negative_kinds':{kind:sum(row['kind']==kind for row in output['negative_checks'])
                          for kind in sorted({row['kind'] for row in output['negative_checks']})},
        'cost_categories':costs,'native_calls_by_category':native_by,'actual_core_call_count':len(CALLS),
        'per_case':[{'inputs':r['inputs'],'production':r['production_cost'],'typed_finite_sums':r['typed_finite_sum_cost']}
                    for r in output['cases']],
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'artifact_sha256':sha(TARGETS[0]),
        'raw_bytes':len(raw),'gzip_bytes':TARGETS[0].stat().st_size,
        'elapsed_seconds_before_serialization':output['elapsed_seconds_before_serialization'],
        'comparison_is_timing_benchmark':False,'full_shor_sampling_performed':False}
    with TARGETS[1].open('x',encoding='utf-8') as handle:
        handle.write(json.dumps(summary,indent=2)+'\n')
    LIVE['stage'] = 'COMPLETE'
    print(json.dumps(summary),flush=True)


def preserve_failure(error):
    failure = {'status':'FAILED_EXECUTION','stage':LIVE['stage'],'error_type':type(error).__name__,
        'error':str(error),'traceback':traceback.format_exc(),'snapshot_errors':{}}
    fields = {'startup_guard':lambda:deepcopy(LIVE['guard']), 'completed_output':lambda:deepcopy(LIVE['output']),
        'current_observer':lambda:None if LIVE['observer'] is None else LIVE['observer'].incomplete_snapshot(),
        'current_brute':lambda:None if LIVE['brute'] is None else LIVE['brute'].incomplete_snapshot(),
        'current_replay_observer':lambda:None if LIVE['replay_observer'] is None else LIVE['replay_observer'].incomplete_snapshot(),
        'replay_capture':lambda:deepcopy(LIVE['replay_capture']),
        'tamper_attempts':lambda:deepcopy(LIVE['tamper_attempts']),
        'current_tamper':lambda:deepcopy(LIVE['current_tamper']),
        'input_attempts':lambda:deepcopy(LIVE['input_attempts']),
        'current_input':lambda:deepcopy(LIVE['current_input']),
        'actual_core_calls':lambda:deepcopy(CALLS),'call_intervals':lambda:deepcopy(LIVE['call_intervals']),
        'current_source_sha256':lambda:{name:sha(ROOT/name) for name in SOURCE_NAMES}}
    for name,collect in fields.items():
        try:
            failure[name] = collect()
        except BaseException as exc:
            failure['snapshot_errors'][name] = repr(exc)
    raw = json.dumps(failure,sort_keys=True,separators=(',',':')).encode()+b'\n'
    with TARGETS[2].open('xb') as handle:
        handle.write(gzip.compress(raw,compresslevel=6,mtime=0))
    print(json.dumps({'status':'FAILED_EXECUTION','path':str(TARGETS[2]),'payload_sha256':hashlib.sha256(raw).hexdigest()}),flush=True)


if __name__ == '__main__':
    if any(path.exists() for path in TARGETS):
        raise ValueError('existing result/failure evidence: refusing overwrite or repeat run')
    try:
        main()
    except BaseException as error:
        preserve_failure(error)
        raise
