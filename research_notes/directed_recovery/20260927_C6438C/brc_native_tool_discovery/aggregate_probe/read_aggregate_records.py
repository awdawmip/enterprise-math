"""Standard-library audit of complete saved aggregate records; no science run."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
sha = lambda b: hashlib.sha256(b).hexdigest()
PINS = {
    'source':'830f28774f3a9e6e4aa9135dd7816c33e5cac78db6b8992990ae094b64d50b48',
    'plan':'de5c24bd2a0a8894be4dfd14928e0189f8a862e8d91a54d57bf4268c15d7fe62',
    'raw':'ad310010570d01a7edae1229289f2a8484f2e2ce5a581e274166522fe5fb687a',
    'gzip':'fb518cb7ee42100b9043f43adee43e1ad47045abde6f8461dc3b729ca4272a4c',
    'native_reader':'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825',
    'hbw_reader':'6dda7b6c995c457c24334507adfc44574e197f120d41f7d0775fdf3815f26b98',
}
compressed = (ROOT/'AGGREGATE_RESULTS.json.gz').read_bytes()
raw = gzip.decompress(compressed)
assert (len(raw),sha(raw),len(compressed),sha(compressed)) == (804733,PINS['raw'],54370,PINS['gzip'])
payload = json.loads(raw)
summary = json.loads((ROOT/'AGGREGATE_SUMMARY.json').read_bytes())
binding = payload['binding']
assert sha((ROOT/'aggregate_probe.py').read_bytes()) == binding['source_sha256'] == PINS['source']
assert sha((ROOT/'PLAN.md').read_bytes()) == binding['plan_sha256'] == PINS['plan']
for key in ('source','plan','raw','gzip'):
    assert summary[key+'_sha256'] == PINS[key]
assert (summary['raw_bytes'],summary['gzip_bytes']) == (len(raw),len(compressed))
assert json.loads((ROOT/'STARTED.json').read_bytes()) == {k:v for k,v in binding.items() if k != 'reused_interfaces'}
assert not (ROOT/'FAILED_EXECUTION.json.gz').exists() and not (ROOT/'FAILED_SERIALIZATION.txt').exists()
guard_raw = Path(binding['guard_path']).read_bytes()
assert sha(guard_raw) == binding['guard_sha256']
guard = json.loads(guard_raw)
assert guard == binding['guard'] and guard['record_sha256'] == binding['expected_guard_record_sha256']
assert guard['record_sha256'] == '8411a63c53ed2931d1353e7de4b341182eb3600b868b5a8d1c075a44c257d7f1'
assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events'] == []
for name,pin in binding['dependencies'].items(): assert sha((BASE/name).read_bytes()) == pin
data = {'binding':binding['reused_interfaces']}
catalog = data['binding']['native_arithmetic']['native_adder']['columns']
counts = Counter()


def selected_definitions(path,pin,names,rename=None):
    source = path.read_bytes(); assert sha(source) == pin
    nodes = [n for n in ast.parse(source).body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in names]
    assert {n.name for n in nodes} == names
    if rename:
        for node in nodes: node.name = rename.get(node.name,node.name)
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path)+'::<record-definitions>','exec'),globals())


selected_definitions(BASE/'read_native_port_review.py',PINS['native_reader'],
                     {'trace','stream','inverse','gcd','audit_route','Records','decoded','deposit','observe_final'})
selected_definitions(BASE/'hbw_marked_section/read_hbw_marked_records.py',PINS['hbw_reader'],
                     {'child','visit'},{'visit':'hbw_visit'})
for path,pin in data['binding']['files'].items(): assert sha(Path(path).read_bytes()) == pin
assert sha((BASE/'native_relative_port.py').read_bytes()) == data['binding']['new_source_sha256']
assert sha((BASE/'EXPERIMENT_PLAN.md').read_bytes()) == data['binding']['plan_sha256']
for name,path in {
    'sparse_modular':'D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py',
    'typed_integer_prechecks':'D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py',
}.items(): assert sha(Path(path).read_bytes()) == data['binding']['native_arithmetic']['files_sha256'][name]
hist = Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src/enterprise_math/brc_histogram.py').read_bytes()
assert hashlib.sha1(b'blob '+str(len(hist)).encode()+b'\0'+hist).hexdigest() == data['binding']['histogram_blob']
vendor = Path('D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py').read_bytes()
assert sha(vendor) == data['binding']['native_arithmetic']['native_adder']['vendor']['sha256']
assert len(payload['all_native_records']) == summary['total_native_calls'] == payload['native_catalog_calls_after_source_admission'] == summary['native_catalog_calls_after_source_admission'] == 1
call = payload['all_native_records'][0]
assert (call['entrypoint'],call['states'],call['depth']) == ('recurrent_mass_power',12,1)

routes = payload['routes']
audits = {name:audit_route(route) for name,route in routes.items()}
cursors = {name:Records(route) for name,route in routes.items()}
total = sum((Counter(a['total']) for a in audits.values()),Counter())
metrics = ('adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
for name,audit in audits.items():
    cost = payload['costs'][name]; assert cost == summary['costs'][name]
    assert {k:audit['total'][k] for k in metrics} == {k:cost[k] for k in metrics}
    assert cost['direct_typed_operations'] == len(routes[name]['arithmetic_operations'])
    assert cost['route_invocations'] == routes[name]['calls']
assert {k:total[k] for k in metrics} == summary['total_cost']
wiring = payload['wiring']; position = 0; setups = {}
SPECIAL = {'aggregate_doubling','aggregate_readout','moment_determinant',
           'marked_dual_row_validation','unstopped_original_moment_step',
           'marked_affine_moment_step','summary_bridge_identities'}


def classify(g,N):
    if g == 1: return 'UNIT'
    if g == N: return 'SATURATED'
    assert 1 < g < N
    return 'PROPER_FACTOR'


def visit(index):
    global position
    node = wiring[index]; kind = node['kind']
    if kind not in SPECIAL: return hbw_visit(index)
    assert index == position and node['id'] == index and node['status'] == 'COMPLETE'
    position += 1
    r = cursors[node['route']]; assert r.pos == node['direct_start']
    counts['wiring_'+kind] += 1

    def calc(field,operation,x,y):
        return child(node[field],operation,inputs=[x,y])

    if kind == 'aggregate_doubling':
        old = node['before']; A = old['A']
        a2 = calc('A_square_link','modmul',A,A)
        oneA = calc('one_plus_A_link','addmod',1,A)
        oneA2 = calc('one_plus_A_square_link','addmod',1,a2)
        g = calc('G_update_link','modmul',old['G'],oneA)
        h = calc('H_update_link','modmul',old['H'],oneA2)
        q = calc('Q_update_link','addmod',old['q'],old['q'])
        result = {'A':a2,'G':g,'H':h,'q':q}
    elif kind == 'aggregate_readout':
        state = node['registers']
        qh = calc('qH_link','modmul',state['q'],state['H'])
        g2 = calc('G_square_link','modmul',state['G'],state['G'])
        dm = calc('D_minus_link','submod',qh,g2)
        dp = calc('D_plus_link','addmod',qh,g2)
        ct = calc('C_tilde_link','modmul',dm,dp)
        result = {}
        for item,(label,value) in zip(node['probes'],(('D_minus',dm),('D_plus',dp),('C_tilde',ct)),strict=True):
            g = child(item['gcd_link'],'gcd_of_difference',inputs=[value,0])
            assert item == {'name':label,'value':value,'gcd':g,'classification':classify(g,r.r['N']),
                            'gcd_link':item['gcd_link'],'factor_check_key':str(g) if 1 < g < r.r['N'] else None}
            result[label] = item
    elif kind == 'moment_determinant':
        m0,m1,m2 = node['moments']
        product = calc('M0_M2_link','modmul',m0,m2)
        square = calc('M1_square_link','modmul',m1,m1)
        result = calc('difference_link','submod',product,square)
    elif kind == 'marked_dual_row_validation':
        setup = setups[node['setup_id']]
        negb = calc('negative_b_link','submod',0,setup['b']); ell = [negb,1]
        transposed = [[setup['M'][j][i] for j in range(2)] for i in range(2)]
        left = child(node['ell_M_link'],'matrix_vector',matrix=transposed,point=ell)
        right = [child(link,'modmul',inputs=[setup['a'],item]) for link,item in zip(node['a_ell_links'],ell,strict=True)]
        assert left == right
        bz = calc('initial_bz_link','modmul',setup['b'],setup['initial'][0])
        linear = calc('initial_linear_link','submod',setup['initial'][1],bz)
        l0 = calc('initial_L_link','submod',linear,setup['delta']); assert l0 == 0
        result = {'ell_M':left,'a_ell':right,'L0':l0}
    elif kind == 'unstopped_original_moment_step':
        assert node['initial'] == [1,1,1]
        setup = payload['cases'][0]['validation']['setup']
        a,b = node['a'],node['b']; assert (a,b) == (setup['a'],setup['b'])
        two = calc('two_link','addmod',1,1)
        four = calc('four_link','addmod',two,two)
        s = calc('s_link','addmod',a,b)
        alpha = calc('alpha_link','addmod',s,two)
        beta = calc('beta_link','modmul',s,s)
        result = [calc('M0_link','modmul',four,1),calc('M1_link','modmul',alpha,1),calc('M2_link','modmul',beta,1)]
    elif kind == 'marked_affine_moment_step':
        setup = payload['cases'][0]['validation']['setup']
        a,b,delta = node['a'],node['b'],node['delta']
        assert (a,b,delta) == (setup['a'],setup['b'],setup['delta'])
        l0 = wiring[payload['cases'][0]['validation']['checks'][0]['link']]['output']['L0']
        assert node['initial'] == [1,l0,0]
        am1 = calc('a_minus_one_link','submod',a,1)
        bm1 = calc('b_minus_one_link','submod',b,1)
        bp = calc('forward_offset_link','modmul',delta,am1)
        bm = calc('inverse_offset_link','modmul',delta,bm1)
        two = calc('two_link','addmod',1,1)
        four = calc('four_link','addmod',two,two)
        ab = calc('a_plus_b_link','addmod',a,b)
        linear = calc('linear_coefficient_link','addmod',two,ab)
        offset = calc('offset_sum_link','addmod',bp,bm)
        a2 = calc('a_square_link','modmul',a,a)
        b2 = calc('b_square_link','modmul',b,b)
        squares = calc('squares_sum_link','addmod',a2,b2)
        quadratic = calc('quadratic_coefficient_link','addmod',two,squares)
        ap = calc('a_forward_offset_link','modmul',a,bp)
        bmprod = calc('b_inverse_offset_link','modmul',b,bm)
        cross = calc('cross_sum_link','addmod',ap,bmprod)
        crosscoef = calc('cross_coefficient_link','addmod',cross,cross)
        bp2 = calc('forward_offset_square_link','modmul',bp,bp)
        bm2 = calc('inverse_offset_square_link','modmul',bm,bm)
        constant = calc('constant_coefficient_link','addmod',bp2,bm2)
        h0 = calc('h0_link','modmul',four,1)
        h1lin = calc('h1_linear_link','modmul',linear,l0)
        h1off = calc('h1_offset_link','modmul',offset,1)
        h1 = calc('h1_link','addmod',h1lin,h1off)
        second = calc('initial_second_moment_link','modmul',l0,l0)
        h2quad = calc('h2_quadratic_link','modmul',quadratic,second)
        h2cross = calc('h2_cross_link','modmul',crosscoef,l0)
        h2const = calc('h2_constant_link','modmul',constant,1)
        partial = calc('h2_partial_link','addmod',h2quad,h2cross)
        h2 = calc('h2_link','addmod',partial,h2const)
        result = [h0,h1,h2]
    elif kind == 'summary_bridge_identities':
        case = payload['cases'][0]; val = case['validation']; setup = val['setup']
        original,marked = val['moments']['original'],val['moments']['marked']
        m0,m1,m2 = original['values']; C = original['determinant']; dl = marked['determinant']; ct = case['probes']['C_tilde']['value']
        assert node['original'] == original['values'] and node['marked'] == marked['values']
        assert (node['C'],node['D_L'],node['C_tilde']) == (C,dl,ct)
        d2 = calc('delta_square_link','modmul',setup['delta'],setup['delta'])
        diff = calc('M1_minus_M0_link','submod',m1,m0)
        h1 = calc('expected_h1_link','modmul',setup['delta'],diff)
        twice = calc('twice_M1_link','addmod',m1,m1)
        partial = calc('M2_minus_twice_M1_link','submod',m2,twice)
        centered = calc('centered_second_link','addmod',partial,m0)
        h2 = calc('expected_h2_link','modmul',d2,centered)
        expected_dl = calc('scaled_determinant_link','modmul',d2,C)
        b2 = calc('inverse_square_link','modmul',setup['b'],setup['b'])
        expected_C = calc('inverse_scaled_C_tilde_link','modmul',b2,ct)
        assert marked['values'] == [m0,h1,h2] and dl == expected_dl and C == expected_C
        gc = child(node['C_gcd_link'],'gcd_of_difference',inputs=[C,0])
        gl = child(node['D_L_gcd_link'],'gcd_of_difference',inputs=[dl,0])
        gct = case['probes']['C_tilde']['gcd']; assert gc == gl == gct
        result = {'moment_equal':True,'determinant_equal':True,'inverse_free_equal':True,'gcds':{'C':gc,'D_L':gl,'C_tilde':gct}}
    else: raise AssertionError(kind)
    assert result == node['output'] and r.pos == node['direct_stop'], (index,kind)
    return result


grid = ((437,2,1),(35,2,2),(19,2,1),(25,2,1))
case_records = []
for index,(case,declared,small) in enumerate(zip(payload['cases'],grid,summary['cases'],strict=True)):
    N,a,t = declared
    assert case['inputs'] == small['inputs'] == {'N':N,'a':a,'layers':t}
    assert child(case['unit_gcd_link'],'gcd_of_difference',inputs=[a,0]) == case['unit_gcd'] == small['unit_gcd'] == 1
    assert case['public_horizon'] == {'Q':{'base':2,'exponent':t},'microscopic_count':{'base':4,'exponent':t}}
    state = {'A':a,'G':1,'H':1,'q':1}; assert state == case['initial_registers']
    assert len(case['layers']) == t
    for depth,layer in enumerate(case['layers'],1):
        assert layer['depth'] == depth
        state = child(layer['link'],'aggregate_doubling',depth=depth,before=state)
        assert state == layer['registers']
    assert case['layers'] == small['layers']
    probes = child(case['readout_link'],'aggregate_readout',registers=state)
    assert probes == case['probes'] == small['probes']
    classes = [p['classification'] for p in probes.values()]
    status = 'PROBE_FOUND_FACTOR' if 'PROPER_FACTOR' in classes else 'SATURATED_WITHOUT_PROPER_FACTOR' if 'SATURATED' in classes else 'NO_FACTOR_FROM_DECLARED_PROBES'
    assert case['status'] == small['status'] == status
    names = ['case'+str(index)+'_'+s for s in ('setup','production','readout')]
    assert names == case['production_route_names']
    assert all(not routes[n]['inverses'] and not routes[n]['tables'] for n in names)
    assert case['production_standalone_inverse_certificates'] == small['production_standalone_inverse_certificates'] == 0
    assert {n:payload['costs'][n] for n in names} == small['production_costs']
    if index == 0:
        val = case['validation']; assert val == small['validation']
        assert visit(val['setup']['setup_id']) == val['setup']
        assert visit(val['checks'][0]['link'])['L0'] == 0
        for key in ('original','marked'):
            m = val['moments'][key]
            assert visit(m['link']) == m['values']
            assert child(m['determinant_link'],'moment_determinant',moments=m['values']) == m['determinant']
        assert visit(val['checks'][1]['link'])['gcds']['C'] == probes['C_tilde']['gcd']
        assert val['status'] == 'PASS_ONE_LAYER_SUMMARY_IDENTITIES' and all(c['equal'] is True for c in val['checks'])
    else: assert 'validation' not in case
    case_records.append({'inputs':case['inputs'],'status':status,'probes':probes,
                         'production_digits':sum(audits[n]['total']['adder_digit_replays'] for n in names)})
assert position == len(wiring)
for cursor in cursors.values(): cursor.close()
assert total['adder_digit_replays'] == counts['checked_native_digit_cells']
assert total['typed_operations'] == counts['checked_top_level_operations']
validation_digits = sum(a['total']['adder_digit_replays'] for n,a in audits.items() if '_validation_' in n)
assert validation_digits + sum(c['production_digits'] for c in case_records) == total['adder_digit_replays']
report = {'status':'PASS_STDLIB_AGGREGATE_SAVED_RECORD_REVIEW_NOT_ADMISSION',
          'reader_sha256':sha(Path(__file__).read_bytes()),'pins':PINS,'binding':binding,
          'summary_sha256':sha((ROOT/'AGGREGATE_SUMMARY.json').read_bytes()),
          'raw_bytes':len(raw),'gzip_bytes':len(compressed),'native_records':payload['all_native_records'],
          'complete_counts':dict(counts),'complete_wiring_nodes':len(wiring),'route_audits':audits,
          'total_cost':dict(total),'validation_digits':validation_digits,'cases':case_records,
          'scope':['Standard-library saved-record inspection only; no native/scientific import or rerun.',
                   'All native digit cells and all new aggregate/affine-moment links checked.',
                   'Cases are targeted fixed inputs; no success-rate, first-hit law or runtime claim.',
                   'The two saved saturated/unit cases remain explicit non-successes.',
                   'Shared-context record review; not formal independent mathematical admission.']}
with (ROOT/'AGGREGATE_RECORD_REVIEW.json').open('x',encoding='utf-8') as f:
    f.write(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:report[k] for k in ('status','complete_counts','complete_wiring_nodes','total_cost','validation_digits','cases')},indent=2))
