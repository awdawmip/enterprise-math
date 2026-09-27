"""Stdlib saved-record audit; no scientific imports, modular oracle or rerun."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
sha = lambda raw: hashlib.sha256(raw).hexdigest()
SOURCE = 'e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851'
PLAN = '45790e24d270fdd3382d8012e9539979818499f6c5126967eef893dc9c664ea6'
RAW = '92306d3d74f39a2b5b6b6d499c901a8cffe8dbdcde946b48e01fd1ff48198a7d'
GZ = 'b782880a3786c0441d80bc4a7ba865dd4918f79d9482325c76edf9c0721cadd2'
HELPER = 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825'
packed = (ROOT/'HBW_MARKED_RESULTS.json.gz').read_bytes()
raw = gzip.decompress(packed)
assert (sha(raw), sha(packed), len(raw), len(packed)) == (RAW, GZ, 1728971, 91934)
payload = json.loads(raw)
summary = json.loads((ROOT/'HBW_MARKED_SUMMARY.json').read_bytes())
binding = payload['binding']
assert sha((ROOT/'hbw_marked_section.py').read_bytes()) == SOURCE == binding['source_sha256']
assert sha((ROOT/'PLAN.md').read_bytes()) == PLAN == binding['plan_sha256']
assert summary['source_sha256'] == SOURCE and summary['raw_sha256'] == RAW and summary['gzip_sha256'] == GZ
assert summary['raw_bytes'] == len(raw) and summary['gzip_bytes'] == len(packed)
guardraw = (ROOT/'STARTUP_GUARD.json').read_bytes()
assert sha(guardraw) == binding['guard_sha256']
guard = json.loads(guardraw)
assert guard == binding['guard']
assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events'] == []
assert guard['record_sha256'] == '59d0da33e8cc4b1a9f50ec7519c136c597eb827ecec6a06fd841a6c68bb44e21'
assert json.loads((ROOT/'STARTED.json').read_bytes()) == {k:v for k,v in binding.items() if k != 'reused_interfaces'}
assert not (ROOT/'FAILED_EXECUTION.json.gz').exists()
for name,pin in binding['dependencies'].items():
    assert sha((BASE/name).read_bytes()) == pin
savedraw = gzip.decompress((BASE/'conic_transport/CONIC_RESULTS.json.gz').read_bytes())
assert sha(savedraw) == binding['saved_raw_sha256']
saved = json.loads(savedraw)
baseline = next(c for c in saved['cases'] if c['inputs'] == {'N':35,'a':2,'layers':3})

# Select definitions only from the previously reviewed, pinned I/O reader.
data = {'binding': binding['reused_interfaces']}
catalog = data['binding']['native_arithmetic']['native_adder']['columns']
counts = Counter()
helper = (BASE/'read_native_port_review.py').read_bytes()
assert sha(helper) == HELPER
selected = {'trace','stream','inverse','gcd','audit_route','Records','decoded','deposit','observe_final'}
nodes = [n for n in ast.parse(helper).body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in selected]
assert {n.name for n in nodes} == selected
exec(compile(ast.Module(body=nodes,type_ignores=[]),'<pinned-stdlib-record-definitions>','exec'),globals())
for path,pin in data['binding']['files'].items():
    assert sha(Path(path).read_bytes()) == pin
assert sha((BASE/'native_relative_port.py').read_bytes()) == data['binding']['new_source_sha256']
assert sha((BASE/'EXPERIMENT_PLAN.md').read_bytes()) == data['binding']['plan_sha256']
for name,path in {
    'sparse_modular':'D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py',
    'typed_integer_prechecks':'D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py',
}.items():
    assert sha(Path(path).read_bytes()) == data['binding']['native_arithmetic']['files_sha256'][name]
hist = Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src/enterprise_math/brc_histogram.py').read_bytes()
assert hashlib.sha1(b'blob '+str(len(hist)).encode()+b'\0'+hist).hexdigest() == data['binding']['histogram_blob']
vendor = Path('D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py').read_bytes()
assert sha(vendor) == data['binding']['native_arithmetic']['native_adder']['vendor']['sha256']
assert len(payload['all_native_records']) == summary['total_native_calls'] == summary['native_catalog_calls_after_source_admission'] == 1
assert payload['native_catalog_calls_after_source_admission'] == 1
call = payload['all_native_records'][0]
assert (call['entrypoint'],call['states'],call['depth']) == ('recurrent_mass_power',12,1)

routes = payload['routes']
audits = {name:audit_route(route) for name,route in routes.items()}
cursors = {name:Records(route) for name,route in routes.items()}
total = sum((Counter(a['total']) for a in audits.values()),Counter())
metrics = ('adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
for name,audit in audits.items():
    cost = payload['costs'][name]
    assert cost == summary['costs'][name]
    assert {k:audit['total'][k] for k in metrics} == {k:cost[k] for k in metrics}
    assert cost['direct_typed_operations'] == len(routes[name]['arithmetic_operations'])
    assert cost['route_invocations'] == routes[name]['calls']
assert {k:total[k] for k in metrics} == summary['total_cost']

wiring = payload['wiring']
position = 0
setups = {}
one = Counter({Fraction(1):1})
atom = Counter({Fraction(1,4):1})
double = Counter({Fraction(1,4):2})


def child(index, kind, **expected):
    node = wiring[index]
    assert node['kind'] == kind
    for key,value in expected.items():
        assert node[key] == value, (index,key,node[key],value)
    return visit(index)


def visit(index):
    global position
    assert index == position
    position += 1
    node = wiring[index]
    assert node['id'] == index and node['status'] == 'COMPLETE'
    r = cursors[node['route']]
    assert r.pos == node['direct_start']
    kind = node['kind']
    counts['wiring_'+kind] += 1
    if kind == 'addmod':
        assert node['add_operation'] == r.pos
        ad = r.op('add'); assert [ad['left'],ad['right']] == node['inputs']
        assert node['division_operation'] == r.pos
        div = r.op('divide'); assert (div['value'],div['modulus']) == (ad['low'],r.r['N'])
        assert div['quotient'] == node['quotient']; result = div['remainder']
    elif kind == 'modmul':
        assert node['operations']['multiply_operation'] == r.pos
        mul = r.op('multiply'); assert [mul['left'],mul['right']] == node['inputs']
        assert node['operations']['division_operation'] == r.pos
        div = r.op('divide'); assert (div['value'],div['modulus']) == (mul['value'],r.r['N'])
        result = div['remainder']
    elif kind == 'submod':
        x,y = node['inputs']; ids = node['operations']
        assert ids['comparison'] == r.pos
        relation,result = r.compare(x,y)
        if relation < 0:
            assert ids['add_modulus'] == r.pos
            ad = r.op('add'); assert (ad['left'],ad['right']) == (x,r.r['N'])
            assert ids['subtract_after_extension'] == r.pos
            relation,result = r.compare(ad['low'],y); assert relation >= 0
        else:
            assert ids['add_modulus'] is None
    elif kind == 'gcd_of_difference':
        x,y = node['inputs']
        difference = child(node['difference_link'],'submod',inputs=[x,y])
        result = r.observe(x,y)
        assert node['gcd_key'] == difference and node['gcd_certificate_cached_key'] == str(difference)
        assert node['factor_check_key'] == (str(result) if 1 < result < r.r['N'] else None)
    elif kind in ('matrix_product','matrix_vector'):
        matrix = node.get('left',node.get('matrix'))
        result = [[0,0],[0,0]] if kind == 'matrix_product' else [0,0]
        expected_positions = [(i,j) for i in range(2) for j in range(2)] if kind == 'matrix_product' else [(i,None) for i in range(2)]
        assert len(node['entries']) == len(expected_positions)
        for entry,(i,j) in zip(node['entries'],expected_positions,strict=True):
            assert entry['row'] == i
            if j is not None:
                assert entry['column'] == j
                right = [node['right'][0][j],node['right'][1][j]]
            else:
                right = node['point']
            first = child(entry['product_links'][0],'modmul',inputs=[matrix[i][0],right[0]])
            second = child(entry['product_links'][1],'modmul',inputs=[matrix[i][1],right[1]])
            value = child(entry['sum_link'],'addmod',inputs=[first,second])
            if j is None: result[i] = value
            else: result[i][j] = value
    elif kind == 'S_fold':
        z,w = node['point']; kz = child(node['kz_link'],'modmul',inputs=[node['k'],z])
        partner = child(node['partner_link'],'submod',inputs=[kz,w])
        assert node['comparison_operation'] == r.pos
        relation,_ = r.compare(w,partner)
        assert node['relation'] == relation and node['partner'] == [z,partner]
        result = [z,w if relation <= 0 else partner]
    elif kind == 'marked_readout':
        setup = setups[node['setup_id']]
        assert (node['b'],node['delta']) == (setup['b'],setup['delta'])
        z,w = node['point']
        bz = child(node['bz_link'],'modmul',inputs=[setup['b'],z])
        shifted = child(node['subtract_bz_link'],'submod',inputs=[w,bz])
        value = child(node['subtract_delta_link'],'submod',inputs=[shifted,setup['delta']])
        assert node['L'] == value
        result = child(node['gcd_link'],'gcd_of_difference',inputs=[value,0])
    elif kind == 'fixed_setup':
        N,a = node['N'],node['a']; assert N == r.r['N'] and str(a) == node['inverse_certificate_key']
        b = r.inv(a)
        delta = child(node['delta_link'],'submod',inputs=[a,b])
        k = child(node['k_link'],'addmod',inputs=[a,b])
        g = child(node['setup_gcd_link'],'gcd_of_difference',inputs=[delta,0])
        assert g == 1
        neg = child(node['negative_one_link'],'submod',inputs=[0,1])
        two = child(node['initial_two_link'],'addmod',inputs=[1,1])
        result = {'setup_id':index,'N':N,'a':a,'b':b,'delta':delta,'k':k,'setup_gcd':g,
                  'status':'REGULAR','M':[[0,1],[neg,k]],'Minv':[[k,neg],[1,0]],
                  'P':[[1,1],[a,b]],'S':[[1,0],[k,neg]],'initial':[two,k]}
        setups[index] = result
    elif kind == 'matrix_identity_validation':
        setup = setups[node['setup_id']]; checks = node['checks']; assert len(checks) == 5
        for check,(label,left,right) in zip(checks[:3],(('M_Minv',setup['M'],setup['Minv']),('Minv_M',setup['Minv'],setup['M']),('S_squared',setup['S'],setup['S'])),strict=True):
            assert check['label'] == label and check['expected'] == [[1,0],[0,1]]
            assert child(check['link'],'matrix_product',left=left,right=right) == check['expected']
        check = checks[3]; assert check['label'] == 'S_M_S'
        sm = child(check['links'][0],'matrix_product',left=setup['S'],right=setup['M'])
        assert child(check['links'][1],'matrix_product',left=sm,right=setup['S']) == setup['Minv'] == check['expected']
        check = checks[4]; assert check['label'] == 'M_P_equals_P_D'
        mp = child(check['links'][0],'matrix_product',left=setup['M'],right=setup['P'])
        pd = child(check['links'][1],'matrix_product',left=setup['P'],right=[[setup['a'],0],[0,setup['b']]])
        assert mp == pd; result = True
    elif kind == 'stopped_layer':
        state = decoded(node['input_states']); out = {}; cursor = 0
        setup = payload['main_case']['setup']
        for key,packet in sorted(state.items()):
            if key[0] == 'FACTOR':
                branch = node['branches'][cursor]; cursor += 1
                assert branch == {'input_port':list(key),'action':'absorb','atom':[[1,1,1]],'output_port':list(key)}
                deposit(out,key,packet,one,r); continue
            for action,matrix,weight,atoms in (('identity',None,double,[[1,4,2]]),('forward',node['matrix'],atom,[[1,4,1]]),('inverse',node['inverse'],atom,[[1,4,1]])):
                branch = node['branches'][cursor]; cursor += 1
                assert branch['input_port'] == list(key) and branch['action'] == action and branch['atom'] == atoms
                if matrix is None:
                    assert branch['action_link'] is None; point = list(key[1:])
                else: point = child(branch['action_link'],'matrix_vector',matrix=matrix,point=list(key[1:]))
                assert branch['unfolded_point'] == point
                g = child(branch['marker_link'],'marked_readout',point=point,setup_id=setup['setup_id'])
                assert branch['gcd'] == g
                if 1 < g < r.r['N']:
                    assert branch['fold_link'] is None; dest = ('FACTOR',g,node['depth'])
                else:
                    folded = child(branch['fold_link'],'S_fold',point=point,k=setup['k']); dest = ('LIVE',*folded)
                assert branch['output_port'] == list(dest)
                deposit(out,dest,packet,weight,r)
        assert cursor == len(node['branches']) and out == decoded(node['output'])
        assert sum(w*c for packet in out.values() for w,c in packet.items()) == 1
        result = node['output']
    elif kind == 'saved_conic_P_S_projection':
        setup = payload['main_case']['setup']; out = {}
        savedstates = decoded(baseline['layers'][node['depth']-1]['states'])
        assert len(savedstates) == len(node['points'])
        for (key,packet),point in zip(sorted(savedstates.items()),node['points'],strict=True):
            assert point['saved_port'] == list(key)
            if key[0] == 'FACTOR': dest = key
            else:
                mapped = child(point['P_link'],'matrix_vector',matrix=setup['P'],point=list(key[1:]))
                original = child(point['original_gcd_link'],'gcd_of_difference',inputs=[key[1],1])
                marked = child(point['marked_gcd_link'],'marked_readout',point=mapped,setup_id=setup['setup_id'])
                assert original == marked and not (1 < original < r.r['N'])
                folded = child(point['S_fold_link'],'S_fold',point=mapped,k=setup['k']); dest = ('LIVE',*folded)
            assert point['projected_port'] == list(dest)
            deposit(out,dest,packet,one,r)
        assert out == decoded(node['output']); result = node['output']
    elif kind == 'primepower_saturation_fixture':
        assert (node['N'],node['a'],node['u']) == (25,2,6)
        setup = setups[node['setup_id']]; v = r.inv(6)
        assert node['inverse_certificate_key'] == '6' and node['v'] == v
        assert child(node['unit_product_link'],'modmul',inputs=[6,v]) == 1
        point = child(node['P_link'],'matrix_vector',matrix=setup['P'],point=[6,v])
        original = child(node['original_gcd_link'],'gcd_of_difference',inputs=[6,1])
        naive = child(node['naive_trace_gcd_link'],'gcd_of_difference',inputs=[point[0],setup['initial'][0]])
        marked = child(node['marked_gcd_link'],'marked_readout',point=point,setup_id=setup['setup_id'])
        reflected = child(node['S_link'],'matrix_vector',matrix=setup['S'],point=point)
        reflected_g = child(node['reflected_marked_gcd_link'],'marked_readout',point=reflected,setup_id=setup['setup_id'])
        assert (original,naive,marked,reflected_g) == (5,25,5,5)
        result = {'point':point,'reflected':reflected,'original_gcd':original,'naive_trace_gcd':naive,
                  'marked_gcd':marked,'reflected_marked_gcd':reflected_g,'wiring_link':index}
    else: raise AssertionError(kind)
    assert result == node['output'], (index,kind)
    assert r.pos == node['direct_stop'], (index,kind,r.pos,node['direct_stop'])
    return result


main = payload['main_case']
assert main['inputs'] == {'N':35,'a':2,'layers':3}
setup = visit(main['setup']['setup_id']); assert setup == main['setup']
assert visit(main['matrix_validation_link']) is True
matrix,inverse_matrix,scalar = setup['M'],setup['Minv'],setup['a']
states = decoded(main['initial_states']); assert states == {('LIVE',*setup['initial']):one}
for depth,layer in enumerate(main['layers'],1):
    assert layer['depth'] == depth and layer['matrix'] == matrix and layer['inverse'] == inverse_matrix
    n = wiring[layer['layer_link']]; assert decoded(n['input_states']) == states
    states = decoded(child(layer['layer_link'],'stopped_layer',depth=depth,matrix=matrix,inverse=inverse_matrix))
    projected = decoded(child(layer['reference_projection_link'],'saved_conic_P_S_projection',depth=depth))
    assert states == projected == decoded(layer['states']) and layer['histograms_equal'] is True
    assert baseline['layers'][depth-1]['multiplier'] == scalar
    if depth < 3:
        schedule = main['schedule'][depth-1]; assert schedule['after_depth'] == depth
        matrix = child(schedule['forward_square_link'],'matrix_product',left=matrix,right=matrix)
        inverse_matrix = child(schedule['inverse_square_link'],'matrix_product',left=inverse_matrix,right=inverse_matrix)
        scalar = child(schedule['validation_scalar_square_link'],'modmul',inputs=[scalar,scalar])
assert len(main['layers']) == 3 and len(main['schedule']) == 2
assert observe_final(states) == decoded(main['output']) == decoded(summary['main_output']) == decoded(baseline['output'])
fixture = payload['primepower_fixture']; fixture_node = wiring[fixture['wiring_link']]
visit(fixture_node['setup_id'])
assert visit(fixture['wiring_link']) == fixture == summary['primepower_fixture']
assert position == len(wiring)
for cursor in cursors.values(): cursor.close()
assert not routes['production']['inverses'] and not routes['production']['tables']
assert summary['production_state_inverse_certificates'] == main['production_state_inverse_certificates'] == 0
assert total['adder_digit_replays'] == counts['checked_native_digit_cells']
assert total['typed_operations'] == counts['checked_top_level_operations']


def saved_cost(route):
    out = {key:route['arithmetic_stats'][key] for key in metrics}
    for group in ('inverses','gcds'):
        for cert in route[group].values():
            for key in metrics: out[key] += cert['cost'][key]
    for table in route['tables'].values():
        for key in metrics: out[key] += table['stats']['setup_'+key]+table['stats']['column_'+key]
    out.update(direct_typed_operations=len(route['arithmetic_operations']),route_invocations=route['calls'])
    return out


assert {r['name']:saved_cost(r) for r in baseline['routes']} == summary['historical_conic_costs']
report = {'status':'PASS_STDLIB_SAVED_MARKED_RECORD_REVIEW_NOT_ADMISSION',
          'reader_sha256':sha(Path(__file__).read_bytes()),'helper_sha256':HELPER,
          'source_sha256':SOURCE,'plan_sha256':PLAN,'raw_sha256':RAW,'gzip_sha256':GZ,
          'raw_bytes':len(raw),'gzip_bytes':len(packed),'summary_sha256':sha((ROOT/'HBW_MARKED_SUMMARY.json').read_bytes()),
          'guard_sha256':sha(guardraw),'source_bindings':binding,'native_records':payload['all_native_records'],
          'complete_counts':dict(counts),'complete_wiring_nodes':len(wiring),
          'route_audits':audits,'combined_cost':dict(total),'historical_costs':summary['historical_conic_costs'],
          'full_histogram_equalities':3,'terminal_histogram':main['output'],'primepower_fixture':fixture,
          'scope':['No scientific imports, modular/gcd reference answers, native calls or scientific rerun.',
                   'All saved digit cells checked against source-bound native full-adder columns.',
                   'All outer nodes/operation spans and exact microscopic histogram multiplicities consumed.',
                   'Setup factor/degenerate branches not executed; failure handler not exercised by the successful unit.',
                   'This is shared-context author evidence review, not independent mathematical admission.',
                   'Historical costs are read from old ledgers, not a fresh timing experiment.']}
target = ROOT/'HBW_MARKED_RECORD_REVIEW.json'
with target.open('x',encoding='utf-8') as stream_out:
    stream_out.write(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:report[k] for k in ('status','complete_counts','complete_wiring_nodes','combined_cost','full_histogram_equalities','primepower_fixture')},indent=2))
