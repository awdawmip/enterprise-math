"""Stdlib-only audit of saved free-trace records; never imports science code."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import argparse
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
OLD = BASE.parent/'sep27-brc-native-tool-discovery'
PINS = {
    'source': '2f0981f1dd25e8160bcd80207a6bc92d080e291b545f3be62b95eddffdd36708',
    'plan': 'c05b238b7c1f1c72319f6bbe3e41652f2d274f41cc05b6cdaf85e7c6a9e4cb52',
    'native_reader': 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825',
    'hbw_reader': '6dda7b6c995c457c24334507adfc44574e197f120d41f7d0775fdf3815f26b98',
}
METRICS = ('adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
sha = lambda b: hashlib.sha256(b).hexdigest()


def selected_definitions(path, pin, names, rename=None):
    source = path.read_bytes()
    assert sha(source) == pin
    nodes = [n for n in ast.parse(source).body
             if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
    assert {n.name for n in nodes} == names
    if rename:
        for node in nodes:
            node.name = rename.get(node.name, node.name)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path)+'::<stdlib-record-definitions>', 'exec'), globals())


def classify(g, N):
    if g == 1:
        return 'UNIT'
    if g == N:
        return 'SATURATED'
    assert 1 < g < N
    return 'PROPER_FACTOR'


def saved_factor_check(r, g):
    if not 1 < g < r.r['N']:
        return None
    saved = r.r['factor_checks'][str(g)]
    assert saved['factor'] == g and saved['remainder'] == 0
    assert 1 < saved['cofactor'] < r.r['N']
    if g not in r.fs:
        assert saved['typed_division_operation'] == r.pos
        op = r.op('divide')
        assert (op['value'], op['modulus'], op['quotient'], op['remainder']) == (
            r.r['N'], g, saved['cofactor'], 0)
        r.fs.add(g)
    return str(g)


SPECIAL = {'common_coordinate_gcd','free_trace_setup','companion_polynomial_square',
           'companion_polynomial_append_M','companion_polynomial_power',
           'both_signed_return_readouts','validation_matrix_power','complete_companion_validation'}


def visit(index):
    global position
    node = wiring[index]
    kind = node['kind']
    if kind not in SPECIAL:
        return hbw_visit(index)
    assert index == position and node['id'] == index and node['status'] == 'COMPLETE'
    position += 1
    r = cursors[node['route']]
    assert r.pos == node['direct_start']
    counts['wiring_'+kind] += 1

    def calc(field, operation, left, right):
        return child(node[field], operation, inputs=[left, right])

    if kind == 'common_coordinate_gcd':
        assert node['N'] == r.r['N']
        current = r.r['N']
        for value, step in zip(node['values'], node['coordinate_steps'], strict=True):
            assert (step['left'], step['right']) == (current, value)
            left, right = current, value
            for item in step['euclid']:
                assert right != 0 and (item['left'], item['right']) == (left, right)
                assert item['division_operation'] == r.pos
                op = r.op('divide')
                assert (op['value'], op['modulus']) == (left, right)
                assert (op['quotient'], op['remainder']) == (item['quotient'], item['remainder'])
                assert 0 <= op['remainder'] < right
                left, right = right, op['remainder']
            assert right == 0 and step['gcd'] == left
            current = left
        assert node['factor_check_key'] == saved_factor_check(r, current)
        result = current
    elif kind == 'free_trace_setup':
        N, k = node['N'], node['k']
        assert N == r.r['N'] and node['odd_modulus_division_operation'] == r.pos
        div = r.op('divide')
        assert (div['value'], div['modulus'], div['remainder']) == (N, 2, 1)
        assert node['odd_modulus_quotient'] == div['quotient']
        two = calc('two_link','addmod',1,1)
        four = calc('four_link','addmod',two,two)
        k2 = calc('k_square_link','modmul',k,k)
        delta = calc('discriminant_link','submod',k2,four)
        dg = calc('discriminant_gcd_link','gcd_of_difference',delta,0)
        neg = calc('negative_one_link','submod',0,1)
        result = {'k':k,'discriminant':delta,'discriminant_gcd':dg,
                  'status':'REGULAR' if dg == 1 else 'SETUP_FACTOR' if dg < N else 'DEGENERATE',
                  'two':two,'negative_one':neg,'M':[[0,1],[neg,k]],
                  'Minv':[[k,neg],[1,0]],'initial_vector':[0,1]}
        setups[node['route'].removesuffix('_setup')] = result
    elif kind == 'companion_polynomial_square':
        c0,c1 = node['before']; k = node['k']
        s0 = calc('c0_square_link','modmul',c0,c0)
        s1 = calc('c1_square_link','modmul',c1,c1)
        cross = calc('cross_link','modmul',c0,c1)
        double = calc('double_cross_link','addmod',cross,cross)
        kc1 = calc('k_c1_square_link','modmul',k,s1)
        next0 = calc('next_c0_link','submod',s0,s1)
        next1 = calc('next_c1_link','addmod',double,kc1)
        result = [next0,next1]
    elif kind == 'companion_polynomial_append_M':
        c0,c1 = node['before']; k = node['k']
        next0 = calc('negative_c1_link','submod',0,c1)
        kc1 = calc('k_c1_link','modmul',k,c1)
        next1 = calc('next_c1_link','addmod',c0,kc1)
        result = [next0,next1]
    elif kind == 'companion_polynomial_power':
        bits = format(node['E'],'b')
        assert node['public_exponent_bits'] == bits and node['initial'] == [1,0]
        state = [1,0]
        for index_bit,(bit,step) in enumerate(zip(bits,node['steps'],strict=True)):
            assert step['bit_index'] == index_bit and step['bit'] == bit
            state = child(step['square_link'],'companion_polynomial_square',before=state,k=node['k'])
            if bit == '1':
                state = child(step['append_link'],'companion_polynomial_append_M',before=state,k=node['k'])
            else:
                assert step['append_link'] is None
        assert node['public_bit_control'] == {'bits_read':len(bits),'square_dispatches':len(bits),
                                             'append_dispatches':bits.count('1')}
        result = state
    elif kind == 'both_signed_return_readouts':
        parameters = setups[node['route'].removesuffix('_readout')]
        state = node['polynomial']
        kc1 = calc('k_c1_link','modmul',parameters['k'],state[1])
        ypoint = calc('point_y_link','addmod',state[0],kc1)
        point = [state[1],ypoint]
        tr = calc('trace_link','addmod',state[0],ypoint)
        result = {'point':point,'trace':tr,'signed':{}}
        targets = (('identity',1),('antipodal',parameters['negative_one']))
        for item,(label,target) in zip(node['signs'],targets,strict=True):
            assert (item['label'],item['target']) == (label,target)
            yr = child(item['y_residual_link'],'submod',inputs=[ypoint,target])
            coords = [point[0],yr]
            gx = child(item['x_gcd_link'],'gcd_of_difference',inputs=[coords[0],0])
            gy = child(item['y_gcd_link'],'gcd_of_difference',inputs=[coords[1],0])
            joint = child(item['joint_gcd_link'],'common_coordinate_gcd',values=coords)
            tt = child(item['two_target_link'],'addmod',inputs=[target,target])
            tau = child(item['trace_residual_link'],'submod',inputs=[tr,tt])
            gt = child(item['trace_gcd_link'],'gcd_of_difference',inputs=[tau,0])
            result['signed'][label] = {'target':target,'coordinates':coords,
                'coordinate_gcds':[gx,gy],'joint_gcd':joint,'joint_class':classify(joint,r.r['N']),
                'trace_residual':tau,'trace_gcd':gt,'trace_class':classify(gt,r.r['N']),
                'coordinate_classes':[classify(gx,r.r['N']),classify(gy,r.r['N'])]}
    elif kind == 'validation_matrix_power':
        bits = format(node['E'],'b')
        assert bits == node['public_exponent_bits']
        acc = [[1,0],[0,1]]
        for index_bit,(bit,step) in enumerate(zip(bits,node['steps'],strict=True)):
            assert step['bit_index'] == index_bit and step['bit'] == bit
            acc = child(step['square_link'],'matrix_product',left=acc,right=acc)
            if bit == '1':
                acc = child(step['append_link'],'matrix_product',left=acc,right=node['matrix'])
            else:
                assert step['append_link'] is None
        result = acc
    elif kind == 'complete_companion_validation':
        prefix = node['route'].removesuffix('_validation')
        parameters = setups[prefix]
        case = cases_by_prefix[prefix]
        state,probes = case['polynomial'],case['probes']
        assert node['E'] == case['inputs']['E'] and node['polynomial'] == state
        assert child(node['inverse_identity_link'],'matrix_product',left=parameters['M'],right=parameters['Minv']) == [[1,0],[0,1]]
        full = child(node['matrix_power_link'],'validation_matrix_power',matrix=parameters['M'],E=node['E'])
        kc1 = calc('k_c1_link','modmul',parameters['k'],state[1])
        br = calc('bottom_right_link','addmod',state[0],kc1)
        neg = calc('negative_c1_link','submod',0,state[1])
        assert full == [[state[0],state[1]],[neg,br]]
        assert probes['point'] == [full[0][1],full[1][1]]
        tr = calc('trace_link','addmod',full[0][0],full[1][1]); assert tr == probes['trace']
        ad = calc('det_first_link','modmul',full[0][0],full[1][1])
        bc = calc('det_second_link','modmul',full[0][1],full[1][0])
        det = calc('det_difference_link','submod',ad,bc); assert det == 1
        x,y = probes['point']
        x2 = calc('conic_x_square_link','modmul',x,x)
        y2 = calc('conic_y_square_link','modmul',y,y)
        xy = calc('conic_xy_link','modmul',x,y)
        kxy = calc('conic_kxy_link','modmul',parameters['k'],xy)
        ss = calc('conic_sum_link','addmod',x2,y2)
        conic = calc('conic_difference_link','submod',ss,kxy); assert conic == 1
        for check,label in zip(node['signed_checks'],('identity','antipodal'),strict=True):
            observed = probes['signed'][label]
            assert (check['label'],check['target']) == (label,observed['target'])
            r00 = child(check['residual00_link'],'submod',inputs=[full[0][0],observed['target']])
            r11 = child(check['residual11_link'],'submod',inputs=[full[1][1],observed['target']])
            entries = [r00,full[0][1],full[1][0],r11]
            common = child(check['matrix_ideal_link'],'common_coordinate_gcd',values=entries)
            assert common == observed['joint_gcd'] == check['matrix_common_gcd']
            kx = child(check['k_residual_x_link'],'modmul',inputs=[parameters['k'],observed['coordinates'][0]])
            claimed00 = child(check['cyclic00_link'],'submod',inputs=[observed['coordinates'][1],kx])
            assert claimed00 == r00 and r11 == observed['coordinates'][1]
            if parameters['status'] == 'REGULAR':
                gs = child(check['joint_square_link'],'modmul',inputs=[common,common])
                g = child(check['joint_square_gcd_link'],'gcd_of_difference',inputs=[gs,0])
                assert g == observed['trace_gcd'] == check['trace_square_gcd']
            else:
                assert check['trace_square_claim'] == 'UNAVAILABLE_DEGENERATE_DISCRIMINANT'
        result = {'all_power_entries_equal':True,'determinant':det,'conic_value':conic,
                  'signed_checks':node['signed_checks']}
    else:
        raise AssertionError(kind)
    assert result == node['output'] and r.pos == node['direct_stop'], (index,kind,r.pos)
    return result


def main(args):
    global data,catalog,counts,payload,summary,binding,routes,cursors,wiring,position,setups,cases_by_prefix
    destination = ROOT/'FREE_TRACE_RECORD_REVIEW.json'
    assert not destination.exists(), 'refuse overwrite'
    packed = (ROOT/'FREE_TRACE_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(packed)
    assert (sha(raw),sha(packed),len(raw),len(packed)) == (
        args.raw_sha256,args.gzip_sha256,args.raw_bytes,args.gzip_bytes)
    payload = json.loads(raw)
    summary = json.loads((ROOT/'FREE_TRACE_SUMMARY.json').read_bytes())
    binding = payload['binding']
    assert payload['schema'] == summary['schema'] == 'BRC_FREE_TRACE_RETURN_V1'
    assert payload['status'] == summary['status'] == 'PASS_FINITE_FREE_TRACE_OBSERVER_NOT_ADMITTED'
    assert sha((ROOT/'free_trace_probe.py').read_bytes()) == binding['source_sha256'] == PINS['source']
    assert sha((ROOT/'PLAN.md').read_bytes()) == binding['plan_sha256'] == PINS['plan']
    for label in ('source','plan'):
        assert summary[label+'_sha256'] == PINS[label]
    assert (summary['raw_sha256'],summary['gzip_sha256'],summary['raw_bytes'],summary['gzip_bytes']) == (
        args.raw_sha256,args.gzip_sha256,args.raw_bytes,args.gzip_bytes)
    assert json.loads((ROOT/'STARTED.json').read_bytes()) == {k:v for k,v in binding.items() if k != 'reused_interfaces'}
    assert not (ROOT/'FAILED_EXECUTION.json.gz').exists() and not (ROOT/'FAILED_SERIALIZATION.txt').exists()
    guard_raw = Path(binding['guard_path']).read_bytes()
    guard = json.loads(guard_raw)
    assert sha(guard_raw) == binding['guard_sha256'] and guard == binding['guard']
    assert guard['record_sha256'] == binding['expected_guard_record_sha256'] == 'b56f4d69570979d37027ea355b312144de37a658307bb40bec5c6e98ea0e76b9'
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True and guard['sync_debt_events'] == []
    assert binding['global_knowledge_read_sha'] == '8c23cca3ed79ca2d6ecbdf76734606eabd94fd0d'
    for root,key in ((BASE,'dependencies'),(OLD,'old_dependencies')):
        for name,pin in binding[key].items():
            assert sha((root/name).read_bytes()) == pin
    data = {'binding':binding['reused_interfaces']}
    catalog = data['binding']['native_arithmetic']['native_adder']['columns']
    counts = Counter()
    selected_definitions(OLD/'read_native_port_review.py',PINS['native_reader'],
                         {'trace','stream','inverse','gcd','audit_route','Records'})
    selected_definitions(OLD/'hbw_marked_section/read_hbw_marked_records.py',PINS['hbw_reader'],
                         {'child','visit'},{'visit':'hbw_visit'})
    for path,pin in data['binding']['files'].items():
        assert sha(Path(path).read_bytes()) == pin
    assert sha((OLD/'native_relative_port.py').read_bytes()) == data['binding']['new_source_sha256']
    assert sha((OLD/'EXPERIMENT_PLAN.md').read_bytes()) == data['binding']['plan_sha256']
    for name,path in {
        'sparse_modular':'D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py',
    }.items():
        assert sha(Path(path).read_bytes()) == data['binding']['native_arithmetic']['files_sha256'][name]
    hist = Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src/enterprise_math/brc_histogram.py').read_bytes()
    assert hashlib.sha1(b'blob '+str(len(hist)).encode()+b'\0'+hist).hexdigest() == data['binding']['histogram_blob']
    vendor = Path('D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py').read_bytes()
    assert sha(vendor) == data['binding']['native_arithmetic']['native_adder']['vendor']['sha256']
    assert len(payload['all_native_records']) == summary['total_native_calls'] == payload['native_catalog_calls_after_source_admission'] == summary['native_catalog_calls_after_source_admission'] == 1
    native = payload['all_native_records'][0]
    assert (native['entrypoint'],native['states'],native['depth']) == ('recurrent_mass_power',12,1)
    routes = payload['routes']
    audits = {name:audit_route(route) for name,route in routes.items()}
    cursors = {name:Records(route) for name,route in routes.items()}
    total = sum((Counter(row['total']) for row in audits.values()),Counter())
    for name,audit in audits.items():
        cost = payload['costs'][name]
        assert {k:audit['total'][k] for k in METRICS} == {k:cost[k] for k in METRICS}
        assert cost['direct_typed_operations'] == len(routes[name]['arithmetic_operations'])
        assert cost['route_invocations'] == routes[name]['calls']
        assert not routes[name]['tables'] and not routes[name]['inverses']
    assert {k:total[k] for k in METRICS} == summary['total_cost']
    wiring = payload['wiring']; position = 0; setups = {}
    cases_by_prefix = {'case'+str(i):case for i,case in enumerate(payload['cases'])}
    grid = ((77,3,4),(77,3,8),(49,3,8))
    reports = []
    assert binding['inputs'] == [{'N':N,'k':k,'E':E} for N,k,E in grid]
    for i,(case,small,(N,k,E)) in enumerate(zip(payload['cases'],summary['cases'],grid,strict=True)):
        prefix = 'case'+str(i)
        assert case['inputs'] == small['inputs'] == {'N':N,'k':k,'E':E}
        names = {category:prefix+'_'+category for category in ('setup','power','readout','validation')}
        assert case['route_names'] == names
        parameters = child(case['setup_link'],'free_trace_setup',N=N,k=k)
        assert parameters == case['setup'] == small['setup']
        assert parameters['status'] == 'REGULAR', 'declared finite grid should use the regular branch'
        state = child(case['power_link'],'companion_polynomial_power',k=k,E=E)
        assert state == case['polynomial'] == small['polynomial']
        probes = child(case['readout_link'],'both_signed_return_readouts',polynomial=state)
        assert probes == case['probes'] == small['probes']
        validation = child(case['validation_link'],'complete_companion_validation',E=E,polynomial=state)
        assert validation == case['validation'] == small['validation']
        assert case['status'] == small['status'] == 'COMPLETE_OBSERVER_COMPARISON_NOT_A_SUCCESS_RATE_CLAIM'
        assert small['costs'] == {category:payload['costs'][name] for category,name in names.items()}
        gm = probes['signed']['identity']['joint_gcd']
        gp = probes['signed']['antipodal']['joint_gcd']
        gx = probes['signed']['identity']['coordinate_gcds'][0]
        assert gx == probes['signed']['antipodal']['coordinate_gcds'][0]
        if gm == 1:
            assert gx == gp
            partition = 'PASS_BY_UNIT_IDENTITY_AND_SAVED_EQUALITY'
        elif gp == 1:
            assert gx == gm
            partition = 'PASS_BY_UNIT_ANTIPODAL_AND_SAVED_EQUALITY'
        else:
            partition = 'NOT_NUMERICALLY_CHECKED_NO_TYPED_PRODUCT_RECEIPT'
        reports.append({'inputs':case['inputs'],'probes':probes,
            'signed_partition_metadata_check':partition,
            'category_digits':{category:audits[name]['total']['adder_digit_replays'] for category,name in names.items()},
            'production_digits':sum(audits[names[c]]['total']['adder_digit_replays'] for c in ('setup','power','readout'))})
    assert position == len(wiring)
    for cursor in cursors.values():
        cursor.close()
    assert total['adder_digit_replays'] == counts['checked_native_digit_cells']
    assert total['typed_operations'] == counts['checked_top_level_operations']
    assert set(routes) == {name for case in payload['cases'] for name in case['route_names'].values()}
    report = {'status':'PASS_STDLIB_FREE_TRACE_SAVED_RECORD_REVIEW_NOT_ADMISSION',
        'reader_sha256':sha(Path(__file__).read_bytes()),'source_pins':PINS,'binding':binding,
        'raw_sha256':sha(raw),'gzip_sha256':sha(packed),'raw_bytes':len(raw),'gzip_bytes':len(packed),
        'summary_sha256':sha((ROOT/'FREE_TRACE_SUMMARY.json').read_bytes()),
        'counts':dict(counts),'wiring_nodes':len(wiring),'route_audits':audits,'total_cost':dict(total),
        'native_records':payload['all_native_records'],'cases':reports,
        'scope':['All saved native digit cells, typed operations and outer power/readout/validation links consumed.',
                 'No scientific import, propagation, modular answer recomputation or host gcd/pow.',
                 'Signed partition checked only by unit/equality branches; no new host product of scientific values.',
                 'Shared-context metadata review, not independent admission or a success-rate benchmark.']}
    with destination.open('x',encoding='utf-8') as stream:
        stream.write(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:report[k] for k in ('status','counts','wiring_nodes','total_cost','cases')},indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw-sha256',required=True)
    parser.add_argument('--gzip-sha256',required=True)
    parser.add_argument('--raw-bytes',required=True,type=int)
    parser.add_argument('--gzip-bytes',required=True,type=int)
    main(parser.parse_args())
