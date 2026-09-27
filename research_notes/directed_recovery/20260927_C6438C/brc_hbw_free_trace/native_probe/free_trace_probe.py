"""One-shot typed free-companion return observers; no scientific import work."""
from pathlib import Path
import argparse
import gzip
import hashlib
import importlib.util
import json
import re
import sys
import traceback

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
OLD = BASE.parent / 'sep27-brc-native-tool-discovery'
SCHEMA = 'BRC_FREE_TRACE_RETURN_V1'
ACTIVITY_ID = 'RA-CAAAC604CB513AEA8BBC1DFC'
GRID = ((77, 3, 4), (77, 3, 8), (49, 3, 8))
EXPECTED = {
    'FREE_TRACE_TORUS_WITNESS.md': '6ad4bbf2db92ffbec7fc57c8da3e16aca9f43a6fb05b89a73aa396aca6f1730c',
    'TRACE_SQUARE_VALUATION_LEMMA.md': '35a8259080ccfb7b608eab922a1562c20836e718b9dff09f2af6209937bcb3d5',
}
OLD_EXPECTED = {
    'native_relative_port.py': '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8',
    'hbw_marked_section/hbw_marked_section.py': 'e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851',
}
OUTPUTS = ('STARTED.json', 'FREE_TRACE_RESULTS.json.gz', 'FREE_TRACE_SUMMARY.json',
           'FAILED_EXECUTION.json.gz', 'FAILED_SERIALIZATION.txt')
METRICS = ('adder_digit_replays', 'host_bit_wiring_operations',
           'host_bit_length_calls_in_arithmetic')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode('utf-8')


def write_new(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


def check_dependencies():
    for root, mapping in ((BASE, EXPECTED), (OLD, OLD_EXPECTED)):
        for name, expected in mapping.items():
            require(sha(root/name) == expected, 'frozen dependency mismatch: '+str(root/name))


def check_binding(args):
    for name in OUTPUTS:
        require(not (OUT/name).exists(), 'refuse repeat: '+name)
    require(re.fullmatch('[0-9a-f]{64}', args.guard_record_sha256) is not None,
            'guard record SHA256 must be lowercase hex')
    path = Path(args.guard_file).resolve()
    raw = path.read_bytes()
    guard = json.loads(raw)
    require(guard['activity_id'] == ACTIVITY_ID, 'wrong activity')
    require(guard['activity_allowed'] is True and guard['persistence_allowed'] is True,
            'guard disallows activity/persistence')
    require(guard['sync_debt_events'] == [], 'sync debt')
    require(guard['record_sha256'] == args.guard_record_sha256, 'wrong immutable guard record')
    check_dependencies()
    return {'schema': SCHEMA, 'source_sha256': sha(Path(__file__)),
            'plan_sha256': sha(OUT/'PLAN.md'), 'dependencies': EXPECTED,
            'old_dependencies': OLD_EXPECTED, 'old_root': str(OLD),
            'guard_path': str(path), 'guard_sha256': hashlib.sha256(raw).hexdigest(),
            'expected_guard_record_sha256': args.guard_record_sha256, 'guard': guard,
            'inputs': [{'N': N, 'k': k, 'E': E} for N, k, E in GRID],
            'global_knowledge_read_sha': '8c23cca3ed79ca2d6ecbdf76734606eabd94fd0d'}


def load_wrappers():
    path = OLD/'hbw_marked_section/hbw_marked_section.py'
    spec = importlib.util.spec_from_file_location('free_trace_frozen_hbw', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def classification(g, N):
    if g == 1:
        return 'UNIT'
    if g == N:
        return 'SATURATED'
    require(1 < g < N, 'invalid gcd output')
    return 'PROPER_FACTOR'


def factor_check(work, route, g):
    if not 1 < g < route.N:
        return None
    key = str(g)
    if g not in route.factor_checks:
        quotient, remainder, op = route.arithmetic.divide(route.N, g)
        require(remainder == 0 and 1 < quotient < route.N, 'factor division failed')
        route.factor_checks[g] = {'factor': g, 'cofactor': quotient, 'remainder': remainder,
                                 'typed_division_operation': op}
    return key


def common_gcd(work, route, values):
    rec = work.begin(route, 'common_coordinate_gcd', N=route.N,
                     values=list(values), coordinate_steps=[])
    current = route.N
    for value in values:
        step = {'left': current, 'right': value, 'euclid': []}
        rec['coordinate_steps'].append(step)
        left, right = current, value
        while right:
            division = {'left': left, 'right': right}
            step['euclid'].append(division)
            q, remainder, op = route.arithmetic.divide(left, right)
            require(0 <= remainder < right, 'Euclid remainder invariant')
            division.update(quotient=q, remainder=remainder, division_operation=op)
            left, right = right, remainder
        current = left
        step['gcd'] = current
    rec['factor_check_key'] = factor_check(work, route, current)
    return work.end(route, rec, current)


def setup(work, hbw, route, k):
    rec = work.begin(route, 'free_trace_setup', N=route.N, k=k)
    parity_q, parity, rec['odd_modulus_division_operation'] = route.arithmetic.divide(route.N, 2)
    rec['odd_modulus_quotient'] = parity_q
    require(parity == 1, 'declared odd-modulus interface')
    two, rec['two_link'] = hbw.addmod(work, route, 1, 1)
    four, rec['four_link'] = hbw.addmod(work, route, two, two)
    k2, rec['k_square_link'] = hbw.modmul(work, route, k, k)
    delta, rec['discriminant_link'] = hbw.submod(work, route, k2, four)
    dg, rec['discriminant_gcd_link'] = hbw.observed_gcd(work, route, delta, 0)
    negone, rec['negative_one_link'] = hbw.submod(work, route, 0, 1)
    result = {'k': k, 'discriminant': delta, 'discriminant_gcd': dg,
              'status': 'REGULAR' if dg == 1 else 'SETUP_FACTOR' if dg < route.N else 'DEGENERATE',
              'two': two, 'negative_one': negone, 'M': [[0, 1], [negone, k]],
              'Minv': [[k, negone], [1, 0]], 'initial_vector': [0, 1]}
    return work.end(route, rec, result)


def polynomial_square(work, hbw, route, state, k):
    rec = work.begin(route, 'companion_polynomial_square', before=list(state), k=k)
    c0, c1 = state
    c02, rec['c0_square_link'] = hbw.modmul(work, route, c0, c0)
    c12, rec['c1_square_link'] = hbw.modmul(work, route, c1, c1)
    cross, rec['cross_link'] = hbw.modmul(work, route, c0, c1)
    double, rec['double_cross_link'] = hbw.addmod(work, route, cross, cross)
    kterm, rec['k_c1_square_link'] = hbw.modmul(work, route, k, c12)
    next0, rec['next_c0_link'] = hbw.submod(work, route, c02, c12)
    next1, rec['next_c1_link'] = hbw.addmod(work, route, double, kterm)
    return work.end(route, rec, [next0, next1])


def polynomial_append(work, hbw, route, state, k):
    rec = work.begin(route, 'companion_polynomial_append_M', before=list(state), k=k)
    next0, rec['negative_c1_link'] = hbw.submod(work, route, 0, state[1])
    kterm, rec['k_c1_link'] = hbw.modmul(work, route, k, state[1])
    next1, rec['next_c1_link'] = hbw.addmod(work, route, state[0], kterm)
    return work.end(route, rec, [next0, next1])


def polynomial_power(work, hbw, route, k, E):
    bits = format(E, 'b')
    rec = work.begin(route, 'companion_polynomial_power', k=k, E=E,
                     public_exponent_bits=bits, steps=[], initial=[1, 0])
    state = [1, 0]
    for index, bit in enumerate(bits):
        step = {'bit_index': index, 'bit': bit}
        rec['steps'].append(step)
        state, step['square_link'] = polynomial_square(work, hbw, route, state, k)
        if bit == '1':
            state, step['append_link'] = polynomial_append(work, hbw, route, state, k)
        else:
            step['append_link'] = None
    rec['public_bit_control'] = {'bits_read': len(bits), 'square_dispatches': len(bits),
                                 'append_dispatches': bits.count('1')}
    return work.end(route, rec, state)


def readout(work, hbw, route, state, parameters):
    rec = work.begin(route, 'both_signed_return_readouts', polynomial=list(state), signs=[])
    kterm, rec['k_c1_link'] = hbw.modmul(work, route, parameters['k'], state[1])
    ypoint, rec['point_y_link'] = hbw.addmod(work, route, state[0], kterm)
    point = [state[1], ypoint]
    trace, rec['trace_link'] = hbw.addmod(work, route, state[0], ypoint)
    result = {'point': point, 'trace': trace, 'signed': {}}
    for label, target in (('identity', 1), ('antipodal', parameters['negative_one'])):
        item = {'label': label, 'target': target}
        rec['signs'].append(item)
        yr, item['y_residual_link'] = hbw.submod(work, route, ypoint, target)
        coords = [point[0], yr]
        gx, item['x_gcd_link'] = hbw.observed_gcd(work, route, coords[0], 0)
        gy, item['y_gcd_link'] = hbw.observed_gcd(work, route, coords[1], 0)
        joint, item['joint_gcd_link'] = common_gcd(work, route, coords)
        two_target, item['two_target_link'] = hbw.addmod(work, route, target, target)
        tau, item['trace_residual_link'] = hbw.submod(work, route, trace, two_target)
        gt, item['trace_gcd_link'] = hbw.observed_gcd(work, route, tau, 0)
        result['signed'][label] = {'target': target, 'coordinates': coords,
                                  'coordinate_gcds': [gx, gy], 'joint_gcd': joint,
                                  'joint_class': classification(joint, route.N),
                                  'trace_residual': tau, 'trace_gcd': gt,
                                  'trace_class': classification(gt, route.N),
                                  'coordinate_classes': [classification(gx, route.N),
                                                         classification(gy, route.N)]}
    return work.end(route, rec, result)


def matrix_power_validation(work, hbw, route, M, E):
    rec = work.begin(route, 'validation_matrix_power', matrix=M, E=E,
                     public_exponent_bits=format(E, 'b'), steps=[])
    acc = [[1, 0], [0, 1]]
    for index, bit in enumerate(rec['public_exponent_bits']):
        step = {'bit_index': index, 'bit': bit}
        rec['steps'].append(step)
        acc, step['square_link'] = hbw.matmul(work, route, acc, acc)
        if bit == '1':
            acc, step['append_link'] = hbw.matmul(work, route, acc, M)
        else:
            step['append_link'] = None
    return work.end(route, rec, acc)


def validate(work, hbw, route, parameters, E, state, probes):
    rec = work.begin(route, 'complete_companion_validation', E=E,
                     polynomial=state, signed_checks=[])
    identity = [[1, 0], [0, 1]]
    mm, rec['inverse_identity_link'] = hbw.matmul(work, route, parameters['M'], parameters['Minv'])
    require(mm == identity, 'companion inverse')
    full, rec['matrix_power_link'] = matrix_power_validation(work, hbw, route, parameters['M'], E)
    kc1, rec['k_c1_link'] = hbw.modmul(work, route, parameters['k'], state[1])
    bottomright, rec['bottom_right_link'] = hbw.addmod(work, route, state[0], kc1)
    negative, rec['negative_c1_link'] = hbw.submod(work, route, 0, state[1])
    reconstructed = [[state[0], state[1]], [negative, bottomright]]
    require(full == reconstructed, 'all four power entries')
    require([full[0][1], full[1][1]] == probes['point'], 'marked column')
    tr, rec['trace_link'] = hbw.addmod(work, route, full[0][0], full[1][1])
    require(tr == probes['trace'], 'trace agreement')
    ad, rec['det_first_link'] = hbw.modmul(work, route, full[0][0], full[1][1])
    bc, rec['det_second_link'] = hbw.modmul(work, route, full[0][1], full[1][0])
    determinant, rec['det_difference_link'] = hbw.submod(work, route, ad, bc)
    require(determinant == 1, 'determinant one')
    x, y = probes['point']
    x2, rec['conic_x_square_link'] = hbw.modmul(work, route, x, x)
    y2, rec['conic_y_square_link'] = hbw.modmul(work, route, y, y)
    xy, rec['conic_xy_link'] = hbw.modmul(work, route, x, y)
    kxy, rec['conic_kxy_link'] = hbw.modmul(work, route, parameters['k'], xy)
    squares, rec['conic_sum_link'] = hbw.addmod(work, route, x2, y2)
    conic, rec['conic_difference_link'] = hbw.submod(work, route, squares, kxy)
    require(conic == 1, 'conic value one')
    for label in ('identity', 'antipodal'):
        observed = probes['signed'][label]
        check = {'label': label, 'target': observed['target']}
        rec['signed_checks'].append(check)
        r00, check['residual00_link'] = hbw.submod(work, route, full[0][0], observed['target'])
        r11, check['residual11_link'] = hbw.submod(work, route, full[1][1], observed['target'])
        entries = [r00, full[0][1], full[1][0], r11]
        common, check['matrix_ideal_link'] = common_gcd(work, route, entries)
        require(common == observed['joint_gcd'], 'full matrix/mark ideal agreement')
        kx, check['k_residual_x_link'] = hbw.modmul(work, route, parameters['k'], observed['coordinates'][0])
        claimed00, check['cyclic00_link'] = hbw.submod(work, route, observed['coordinates'][1], kx)
        require(claimed00 == r00 and r11 == observed['coordinates'][1], 'cyclic residual identity')
        check['matrix_common_gcd'] = common
        if parameters['status'] == 'REGULAR':
            gsquare, check['joint_square_link'] = hbw.modmul(work, route, common, common)
            square_gcd, check['joint_square_gcd_link'] = hbw.observed_gcd(work, route, gsquare, 0)
            require(square_gcd == observed['trace_gcd'], 'signed trace square valuation identity')
            check['trace_square_gcd'] = square_gcd
        else:
            check['trace_square_claim'] = 'UNAVAILABLE_DEGENERATE_DISCRIMINANT'
    return work.end(route, rec, {'all_power_entries_equal': True, 'determinant': determinant,
                                'conic_value': conic, 'signed_checks': rec['signed_checks']})


def main_case(work, hbw, index, N, k, E):
    require(type(N) is int and N > 1, 'integer modulus greater than one')
    require(type(k) is int and 0 <= k < N, 'principal public trace required')
    require(type(E) is int and E >= 0, 'nonnegative public exponent required')
    prefix = 'case'+str(index)
    case = {'inputs': {'N': N, 'k': k, 'E': E}, 'route_names': {}}
    work.completed[prefix] = case
    routes = {}
    for category in ('setup', 'power', 'readout', 'validation'):
        work.stage = prefix+'_construct_'+category
        routes[category] = work.route(N, prefix+'_'+category)
        case['route_names'][category] = routes[category].name
    work.stage = prefix+'_setup'
    parameters, case['setup_link'] = setup(work, hbw, routes['setup'], k)
    case['setup'] = parameters
    if parameters['status'] == 'SETUP_FACTOR':
        case['status'] = 'SETUP_FACTOR_NO_POWER_EXECUTED'
        return case
    work.stage = prefix+'_power'
    state, case['power_link'] = polynomial_power(work, hbw, routes['power'], k, E)
    case['polynomial'] = state
    work.stage = prefix+'_readout'
    probes, case['readout_link'] = readout(work, hbw, routes['readout'], state, parameters)
    case['probes'] = probes
    work.stage = prefix+'_validation'
    case['validation'], case['validation_link'] = validate(
        work, hbw, routes['validation'], parameters, E, state, probes)
    require(all(not r.tables and not r.inverses for r in routes.values()), 'unexpected inverse/table')
    case['status'] = 'COMPLETE_OBSERVER_COMPARISON_NOT_A_SUCCESS_RATE_CLAIM'
    return case


def end_binding(binding):
    require(sha(Path(__file__)) == binding['source_sha256'], 'source changed during run')
    require(sha(OUT/'PLAN.md') == binding['plan_sha256'], 'plan changed during run')
    require(sha(Path(binding['guard_path'])) == binding['guard_sha256'], 'guard changed during run')
    check_dependencies()


def run(args):
    binding = check_binding(args)
    write_new(OUT/'STARTED.json', encode(binding))
    work = None
    hbw = None
    try:
        hbw = load_wrappers()
        work = hbw.Work(binding)
        sys.path.insert(0, str(OLD))
        import native_relative_port as old
        work.old = old
        work.stage = 'native_source_admission'
        binding['reused_interfaces'] = old.source_check()
        calls_after_admission = len(old.CALLS)
        cases = [main_case(work, hbw, i, *args) for i, args in enumerate(GRID)]
        work.stage = 'end_source_check'
        end_binding(binding)
        require(old.source_check() == binding['reused_interfaces'], 'native binding changed')
        routes = {name: route.export() for name, route in work.routes.items()}
        costs = {name: hbw.route_cost(route) for name, route in routes.items()}
        payload = {'schema': SCHEMA, 'status': 'PASS_FINITE_FREE_TRACE_OBSERVER_NOT_ADMITTED',
                   'binding': binding, 'cases': cases, 'routes': routes, 'wiring': work.wiring,
                   'costs': costs, 'all_native_records': old.CALLS,
                   'native_catalog_calls_after_source_admission': calls_after_admission,
                   'scope': 'modular observer; no raw X6, first-hit law, timing or general success claim'}
        work.stage = 'serialize_success'
        raw = hbw.encode(payload)
        compressed = gzip.compress(raw, mtime=0)
        write_new(OUT/'FREE_TRACE_RESULTS.json.gz', compressed)
        summaries = []
        for case in cases:
            item = {key: case[key] for key in ('inputs', 'status', 'setup')}
            for key in ('polynomial', 'probes', 'validation'):
                if key in case:
                    item[key] = case[key]
            item['costs'] = {category: costs[name] for category, name in case['route_names'].items()}
            summaries.append(item)
        summary = {'schema': SCHEMA, 'status': payload['status'], 'cases': summaries,
                   'source_sha256': binding['source_sha256'], 'plan_sha256': binding['plan_sha256'],
                   'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
                   'gzip_bytes': len(compressed), 'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
                   'total_cost': {key: sum(value[key] for value in costs.values()) for key in METRICS},
                   'native_catalog_calls_after_source_admission': calls_after_admission,
                   'total_native_calls': len(old.CALLS),
                   'cost_scope': 'all setup/power/readout/validation typed streams; no performance claim'}
        write_new(OUT/'FREE_TRACE_SUMMARY.json', hbw.encode(summary))
        print(json.dumps(summary, indent=2, default=hbw.plain))
    except BaseException:
        failure_trace = traceback.format_exc()
        try:
            evidence = {'binding': binding} if work is None else work.snapshot()
            failure = {'schema': SCHEMA, 'status': 'FAILED_NOT_RESUMABLE',
                       'traceback': failure_trace, 'evidence': evidence,
                       'scope': 'available records; unreturned primitive/constructor may lack its final internal record'}
            raw = encode(failure) if hbw is None else hbw.encode(failure)
            write_new(OUT/'FAILED_EXECUTION.json.gz', gzip.compress(raw, mtime=0))
        except BaseException:
            fallback = failure_trace+'\nFailure serialization also failed:\n'+traceback.format_exc()
            write_new(OUT/'FAILED_SERIALIZATION.txt', fallback.encode('utf-8'))
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--guard-file', required=True)
    parser.add_argument('--guard-record-sha256', required=True)
    run(parser.parse_args())
