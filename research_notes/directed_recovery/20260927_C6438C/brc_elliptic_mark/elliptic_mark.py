"""One-shot actual typed Montgomery ladder and translated-return comparison.

Importing this module does not import or execute its scientific dependencies.
"""
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
OLD = OUT.parent / 'sep27-brc-native-tool-discovery'
PROOFS = OUT.parent / 'sep27-brc-hbw-free-trace'
SCHEMA = 'BRC_ELLIPTIC_TRANSLATED_MARK_V1'
ACTIVITY_ID = 'RA-CAAAC604CB513AEA8BBC1DFC'
GRID = ((9, 0, 4), (35, 4, 8), (19, 0, 4))
EXPECTED = {
    'GEOMETRIC_NEXT_TOOL.md': '76e39469669e4068b297377ad9beb0c6dd5b19b9a1a929a2f07378f1dfe281e2',
    'GEOMETRIC_NEXT_TOOL_PARENT_REVIEW.md': '584540d5caef89f5c8b4d160e25c76e11ff634725b4558171c595d162f2eee81',
    'TRANSLATED_KUMMER_MARK.md': '50e899863bcec4001ee6a5dd7d2f069a57358e97b6de07b90bc7378b013fd492',
    'TRANSLATED_KUMMER_MARK_PARENT_REVIEW.md': '9306dd45b1d3960c5ce47d26cf3e0528f0b2ede0933e2a07f7eb212a0e8a91c7',
    'KUMMER_RETURN_VALUATION.md': '3b7a522fdb487bb5fdbe054a8e41a517f7f067881fdd5ac1822d367a1975f222',
}
LOCAL_EXPECTED = {
    'JACOBIAN_VALIDATION_PROOF.md': 'ba77080e3d4400cd669f4f819c49e6e2dfacc65f4507d0b8718498c1712517be',
}
OLD_EXPECTED = {
    'native_relative_port.py': '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8',
    'hbw_marked_section/hbw_marked_section.py': 'e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851',
}
OUTPUTS = ('STARTED.json', 'ELLIPTIC_MARK_RESULTS.json.gz', 'ELLIPTIC_MARK_SUMMARY.json',
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
    for root, mapping in ((PROOFS, EXPECTED), (OUT, LOCAL_EXPECTED), (OLD, OLD_EXPECTED)):
        for name, expected in mapping.items():
            require(sha(root/name) == expected, 'frozen dependency mismatch: '+str(root/name))


def check_binding(args):
    for name in OUTPUTS:
        require(not (OUT/name).exists(), 'refuse repeat: '+name)
    require(re.fullmatch('[0-9a-f]{64}', args.guard_record_sha256) is not None,
            'guard record SHA256 must be lowercase hex')
    require(re.fullmatch('[0-9a-f]{40}', args.global_knowledge_sha) is not None,
            'actual coordinator knowledge SHA must be supplied')
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
            'plan_sha256': sha(OUT/'PLAN.md'), 'proof_dependencies': EXPECTED,
            'local_dependencies': LOCAL_EXPECTED, 'old_dependencies': OLD_EXPECTED,
            'guard_path': str(path), 'guard_sha256': hashlib.sha256(raw).hexdigest(),
            'expected_guard_record_sha256': args.guard_record_sha256, 'guard': guard,
            'inputs': [{'N': N, 'A': A, 'E': E} for N, A, E in GRID],
            'coordinator_actual_global_knowledge_read_sha': args.global_knowledge_sha,
            'author_previous_policy_read_sha': '7a639845946cb5f8edfa22d3d5d0d47a44f6080e'}


def load_wrappers():
    path = OLD/'hbw_marked_section/hbw_marked_section.py'
    spec = importlib.util.spec_from_file_location('elliptic_frozen_hbw', path)
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


def factor_check(route, g):
    if not 1 < g < route.N:
        return None
    if g not in route.factor_checks:
        quotient, remainder, op = route.arithmetic.divide(route.N, g)
        require(remainder == 0 and 1 < quotient < route.N, 'factor division failed')
        route.factor_checks[g] = {'factor': g, 'cofactor': quotient, 'remainder': remainder,
                                 'typed_division_operation': op}
    return str(g)


def common_gcd(work, route, values):
    rec = work.begin(route, 'common_coordinate_gcd', N=route.N,
                     values=list(values), coordinate_steps=[])
    route.calls['common_gcd_requests'] = route.calls.get('common_gcd_requests', 0)+1
    current = route.N
    for value in values:
        step = {'left': current, 'right': value, 'euclid': []}
        rec['coordinate_steps'].append(step)
        left, right = current, value
        while right:
            division = {'left': left, 'right': right}
            step['euclid'].append(division)
            quotient, remainder, op = route.arithmetic.divide(left, right)
            require(0 <= remainder < right, 'Euclid remainder invariant')
            division.update(quotient=quotient, remainder=remainder, division_operation=op)
            left, right = right, remainder
        current = left
        step['gcd'] = current
    rec['factor_check_key'] = factor_check(route, current)
    return work.end(route, rec, current)


class Ops:
    """Only wires named actual wrapper outputs; performs no host propagation."""
    def __init__(self, work, hbw, route, rec):
        self.work, self.hbw, self.route, self.rec = work, hbw, route, rec
        rec['links'] = []

    def call(self, role, function, *args):
        value, link = function(self.work, self.route, *args)
        self.rec['links'].append({'role': role, 'wiring_id': link})
        return value

    def add(self, role, x, y):
        return self.call(role, self.hbw.addmod, x, y)

    def sub(self, role, x, y):
        return self.call(role, self.hbw.submod, x, y)

    def mul(self, role, x, y):
        return self.call(role, self.hbw.modmul, x, y)

    def gcd(self, role, x):
        return self.call(role, self.hbw.observed_gcd, x, 0)

    def common(self, role, values):
        return self.call(role, common_gcd, values)


def setup(work, hbw, route, A):
    rec = work.begin(route, 'montgomery_setup', N=route.N, A=A)
    op = Ops(work, hbw, route, rec)
    quotient, parity, rec['odd_modulus_operation'] = route.arithmetic.divide(route.N, 2)
    rec['odd_modulus_quotient'] = quotient
    require(parity == 1, 'odd modulus required')
    two = op.add('two', 1, 1)
    three = op.add('three', two, 1)
    four = op.add('four', two, two)
    eight = op.add('eight', four, four)
    ten = op.add('ten', eight, two)
    fourA = op.mul('four_A', four, A)
    B = op.add('B', ten, fourA)
    A2 = op.mul('A_square', A, A)
    disc = op.sub('discriminant', A2, four)
    product = op.mul('smoothness_product', B, disc)
    gB = op.gcd('B_gcd', B)
    gdisc = op.gcd('discriminant_gcd', disc)
    gsmooth = op.gcd('smoothness_gcd', product)
    gx = op.gcd('base_x_gcd', two)
    x2 = op.mul('base_x_square', two, two)
    x3 = op.mul('base_x_cube', x2, two)
    Ax2 = op.mul('A_base_x_square', A, x2)
    partial = op.add('base_rhs_partial', x3, Ax2)
    rhs = op.add('base_rhs', partial, two)
    require(B == rhs, 'initial point membership')
    proper = [g for g in (gB, gdisc, gsmooth, gx) if 1 < g < route.N]
    status = 'SETUP_FACTOR' if proper else 'REGULAR' if gsmooth == gx == 1 else 'DEGENERATE'
    result = {'N': route.N, 'A': A, 'B': B, 'discriminant': disc,
              'smoothness_product': product, 'setup_gcds': [gB, gdisc, gsmooth, gx],
              'status': status, 'proper_setup_factors': proper,
              'P_affine': [two, 1], 'P_xz': [two, 1],
              'constants': {'two': two, 'three': three, 'four': four, 'eight': eight},
              'membership_lhs': B, 'membership_rhs': rhs}
    return work.end(route, rec, result)


def x_double(work, hbw, route, point, parameters):
    rec = work.begin(route, 'kummer_double', point=list(point), A=parameters['A'])
    op = Ops(work, hbw, route, rec)
    X, Z = point
    x2 = op.mul('X_square', X, X)
    z2 = op.mul('Z_square', Z, Z)
    difference = op.sub('square_difference', x2, z2)
    newX = op.mul('new_X', difference, difference)
    xz = op.mul('XZ', X, Z)
    Axz = op.mul('A_XZ', parameters['A'], xz)
    partial = op.add('quadratic_partial', x2, Axz)
    quadratic = op.add('quadratic', partial, z2)
    fourxz = op.mul('four_XZ', parameters['constants']['four'], xz)
    newZ = op.mul('new_Z', fourxz, quadratic)
    return work.end(route, rec, [newX, newZ])


def x_add(work, hbw, route, left, right, difference):
    rec = work.begin(route, 'fixed_difference_add', left=list(left), right=list(right),
                     difference=list(difference), relation='left-right=+-fixed_P')
    op = Ops(work, hbw, route, rec)
    xx = op.mul('X_left_X_right', left[0], right[0])
    zz = op.mul('Z_left_Z_right', left[1], right[1])
    first = op.sub('first_factor', xx, zz)
    first2 = op.mul('first_factor_square', first, first)
    newX = op.mul('new_X', difference[1], first2)
    xz = op.mul('X_left_Z_right', left[0], right[1])
    zx = op.mul('Z_left_X_right', left[1], right[0])
    second = op.sub('second_factor', xz, zx)
    second2 = op.mul('second_factor_square', second, second)
    newZ = op.mul('new_Z', difference[0], second2)
    return work.end(route, rec, [newX, newZ])


def ladder(work, hbw, route, parameters, E):
    bits = format(E, 'b')
    R0, R1 = [1, 0], list(parameters['P_xz'])
    rec = work.begin(route, 'montgomery_ladder', E=E, public_exponent_bits=bits,
                     initial=[list(R0), list(R1)], steps=[],
                     chart_certificate='GEOMETRIC_NEXT_TOOL fixed unit difference')
    for index, bit in enumerate(bits):
        step = {'bit_index': index, 'bit': bit, 'before': [list(R0), list(R1)],
                'status': 'INCOMPLETE'}
        rec['steps'].append(step)
        added, step['addition_link'] = x_add(work, hbw, route, R0, R1, parameters['P_xz'])
        selected = R0 if bit == '0' else R1
        doubled, step['doubling_link'] = x_double(work, hbw, route, selected, parameters)
        R0, R1 = (doubled, added) if bit == '0' else (added, doubled)
        step.update(after=[list(R0), list(R1)], status='COMPLETE')
    rec['public_bit_control'] = {'bits_read': len(bits), 'add_dispatches': len(bits),
                                 'double_dispatches': len(bits)}
    return work.end(route, rec, [R0, R1])


def mark_expression(work, hbw, route, pair, parameters):
    rec = work.begin(route, 'translated_mark_expression', pair=pair, a=parameters['P_affine'][0])
    op = Ops(work, hbw, route, rec)
    aZ1 = op.mul('a_Z1', parameters['P_affine'][0], pair[1][1])
    W = op.sub('W', pair[1][0], aZ1)
    return work.end(route, rec, W)


def scalar_readout(work, hbw, route, value, label):
    rec = work.begin(route, 'scalar_factor_readout', value=value, label=label)
    op = Ops(work, hbw, route, rec)
    g = op.gcd('gcd', value)
    return work.end(route, rec, {'value': g, 'class': classification(g, route.N)})


def common_readout(work, hbw, route, values):
    rec = work.begin(route, 'marked_common_readout', values=list(values))
    op = Ops(work, hbw, route, rec)
    g = op.common('common_gcd', values)
    return work.end(route, rec, {'value': g, 'class': classification(g, route.N)})


def jacobian_double(work, hbw, route, point, a2, a4, constants):
    rec = work.begin(route, 'jacobian_double_validation', point=list(point), a2=a2, a4=a4)
    op = Ops(work, hbw, route, rec)
    X, Y, Z = point
    x2 = op.mul('X_square', X, X)
    y2 = op.mul('Y_square', Y, Y)
    z2 = op.mul('Z_square', Z, Z)
    z4 = op.mul('Z_fourth', z2, z2)
    y4 = op.mul('Y_fourth', y2, y2)
    yz = op.mul('YZ', Y, Z)
    newZ = op.mul('new_Z', constants['two'], yz)
    m0 = op.mul('three_X_square', constants['three'], x2)
    xz2 = op.mul('X_Z_square', X, z2)
    a2xz2 = op.mul('a2_X_Z_square', a2, xz2)
    m1 = op.mul('two_a2_X_Z_square', constants['two'], a2xz2)
    m2 = op.mul('a4_Z_fourth', a4, z4)
    mpartial = op.add('M_partial', m0, m1)
    M = op.add('M', mpartial, m2)
    xy2 = op.mul('X_Y_square', X, y2)
    S = op.mul('S', constants['four'], xy2)
    Msquare = op.mul('M_square', M, M)
    twoS = op.mul('two_S', constants['two'], S)
    znew2 = op.mul('new_Z_square', newZ, newZ)
    a2znew2 = op.mul('a2_new_Z_square', a2, znew2)
    xpartial = op.sub('new_X_partial', Msquare, twoS)
    newX = op.sub('new_X', xpartial, a2znew2)
    difference = op.sub('S_minus_new_X', S, newX)
    ypartial = op.mul('M_times_difference', M, difference)
    eighty4 = op.mul('eight_Y_fourth', constants['eight'], y4)
    newY = op.sub('new_Y', ypartial, eighty4)
    return work.end(route, rec, [newX, newY, newZ])


def check_jacobian(work, hbw, route, point, a2, a4):
    rec = work.begin(route, 'jacobian_curve_and_primitive_check', point=list(point), a2=a2, a4=a4)
    op = Ops(work, hbw, route, rec)
    X, Y, Z = point
    lhs = op.mul('Y_square', Y, Y)
    x2 = op.mul('X_square', X, X)
    x3 = op.mul('X_cube', x2, X)
    z2 = op.mul('Z_square', Z, Z)
    z4 = op.mul('Z_fourth', z2, z2)
    x2z2 = op.mul('X_square_Z_square', x2, z2)
    term2 = op.mul('a2_term', a2, x2z2)
    xz4 = op.mul('X_Z_fourth', X, z4)
    term4 = op.mul('a4_term', a4, xz4)
    partial = op.add('rhs_partial', x3, term2)
    rhs = op.add('rhs', partial, term4)
    primitive = op.common('primitive_gcd', point)
    rec.update(lhs=lhs, rhs=rhs, primitive_gcd=primitive)
    require(lhs == rhs, 'Jacobian curve equation')
    require(primitive == 1, 'Jacobian all-zero local tuple')
    return work.end(route, rec, {'lhs': lhs, 'rhs': rhs, 'primitive_gcd': primitive})


def validate(work, hbw, route, parameters, E, pair, ladder_record, readouts):
    bits = format(E, 'b')
    require(bits.count('1') == 1, 'bounded full-point validator requires public power of two')
    rec = work.begin(route, 'independent_full_point_validation', E=E,
                     public_exponent_bits=bits, pair=pair, primitive_pair_checks=[],
                     doubling_steps=[], full_point_states=[])
    op = Ops(work, hbw, route, rec)
    saved_pairs = [('initial', ladder_record['initial'])]
    saved_pairs.extend(('after_bit_'+str(s['bit_index']), s['after']) for s in ladder_record['steps'])
    for label, points in saved_pairs:
        for index, point in enumerate(points):
            g = op.common('pair_primitive_'+label+'_'+str(index), point)
            rec['primitive_pair_checks'].append({'label': label, 'pair_index': index,
                                                'point': point, 'gcd': g})
            require(g == 1, 'Kummer all-zero local pair')
    a2 = op.mul('a2', parameters['A'], parameters['B'])
    a4 = op.mul('a4', parameters['B'], parameters['B'])
    initX = op.mul('initial_X', parameters['constants']['two'], parameters['B'])
    point = [initX, a4, 1]
    rec.update(a2=a2, a4=a4, initial=list(point))
    rec['full_point_states'].append(list(point))
    _, rec['initial_check_link'] = check_jacobian(work, hbw, route, point, a2, a4)
    for index in range(len(bits)-1):
        step = {'doubling_index': index, 'before': list(point), 'status': 'INCOMPLETE'}
        rec['doubling_steps'].append(step)
        point, step['double_link'] = jacobian_double(
            work, hbw, route, point, a2, a4, parameters['constants'])
        step['after'] = list(point)
        rec['full_point_states'].append(list(point))
        _, step['check_link'] = check_jacobian(work, hbw, route, point, a2, a4)
        step['status'] = 'COMPLETE'
    z2 = op.mul('terminal_Z_square', point[2], point[2])
    Bz2 = op.mul('terminal_B_Z_square', parameters['B'], z2)
    cross_left = op.mul('cross_left', pair[0][0], Bz2)
    cross_right = op.mul('cross_right', pair[0][1], point[0])
    require(cross_left == cross_right, 'original-x/full-point cross relation')
    gpoint = op.gcd('primitive_return_gcd', point[2])
    require(gpoint == readouts['marked']['value'], 'translated mark/full-point return ideal')
    gsquare = op.mul('return_gcd_square', gpoint, gpoint)
    gsquare_gcd = op.gcd('squared_return_gcd', gsquare)
    require(gsquare_gcd == readouts['ordinary']['value'], 'Kummer square valuation')
    output = {'full_point': point, 'full_point_return_gcd': gpoint,
              'cross_left': cross_left, 'cross_right': cross_right,
              'Kummer_square_gcd': gsquare_gcd, 'marked_gcd_equal': True,
              'public_doublings': len(bits)-1,
              'scope': 'terminal E point; adjacent R1 certified by production ladder induction'}
    return work.end(route, rec, output)


def main_case(work, hbw, index, N, A, E):
    require(type(N) is int and N > 1, 'integer modulus greater than one')
    require(type(A) is int and 0 <= A < N, 'principal public A required')
    require(type(E) is int and E > 0, 'positive public exponent required')
    prefix = 'case'+str(index)
    case = {'inputs': {'N': N, 'A': A, 'E': E}, 'route_names': {}}
    work.completed[prefix] = case
    routes = {}
    for category in ('setup', 'ladder', 'ordinary', 'mark_expression', 'marked', 'single_W', 'validation'):
        work.stage = prefix+'_construct_'+category
        routes[category] = work.route(N, prefix+'_'+category)
        case['route_names'][category] = routes[category].name
    work.stage = prefix+'_setup'
    parameters, case['setup_link'] = setup(work, hbw, routes['setup'], A)
    case['setup'] = parameters
    require(parameters['status'] == 'REGULAR', 'declared fixture unexpectedly inadmissible')
    work.stage = prefix+'_ladder'
    pair, case['ladder_link'] = ladder(work, hbw, routes['ladder'], parameters, E)
    case['terminal_pair'] = pair
    work.stage = prefix+'_ordinary_readout'
    ordinary, case['ordinary_link'] = scalar_readout(work, hbw, routes['ordinary'], pair[0][1], 'Kummer_Z0')
    case['readouts'] = {'ordinary': ordinary}
    work.stage = prefix+'_mark_expression'
    W, case['mark_expression_link'] = mark_expression(work, hbw, routes['mark_expression'], pair, parameters)
    case['W'] = W
    work.stage = prefix+'_marked_readout'
    marked, case['marked_link'] = common_readout(work, hbw, routes['marked'], [pair[0][1], W])
    case['readouts']['marked'] = marked
    work.stage = prefix+'_single_W_readout'
    single, case['single_W_link'] = scalar_readout(work, hbw, routes['single_W'], W, 'single_W')
    case['readouts']['single_W'] = single
    work.stage = prefix+'_validation'
    case['validation'], case['validation_link'] = validate(
        work, hbw, routes['validation'], parameters, E, pair,
        work.wiring[case['ladder_link']], case['readouts'])
    require(all(not r.tables and not r.inverses for r in routes.values()), 'unexpected inverse/table')
    case['status'] = 'COMPLETE_FINITE_OBSERVER_COMPARISON_NOT_SUCCESS_RATE'
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
        cases = [main_case(work, hbw, index, *values) for index, values in enumerate(GRID)]
        work.stage = 'end_source_check'
        end_binding(binding)
        require(old.source_check() == binding['reused_interfaces'], 'native binding changed')
        routes = {name: route.export() for name, route in work.routes.items()}
        costs = {name: hbw.route_cost(route) for name, route in routes.items()}
        payload = {'schema': SCHEMA, 'status': 'PASS_FINITE_ELLIPTIC_MARK_NOT_ADMITTED',
                   'binding': binding, 'cases': cases, 'routes': routes, 'wiring': work.wiring,
                   'costs': costs, 'all_native_records': old.CALLS,
                   'native_catalog_calls_after_source_admission': calls_after_admission,
                   'scope': 'actual typed modular registers; no raw Cell trajectory or general factoring claim'}
        work.stage = 'serialize_success'
        raw = hbw.encode(payload)
        compressed = gzip.compress(raw, mtime=0)
        write_new(OUT/'ELLIPTIC_MARK_RESULTS.json.gz', compressed)
        summaries = []
        for case in cases:
            item = {key: case[key] for key in ('inputs', 'status', 'setup', 'terminal_pair',
                                              'W', 'readouts', 'validation')}
            item['costs'] = {category: costs[name] for category, name in case['route_names'].items()}
            summaries.append(item)
        summary = {'schema': SCHEMA, 'status': payload['status'], 'cases': summaries,
                   'source_sha256': binding['source_sha256'], 'plan_sha256': binding['plan_sha256'],
                   'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
                   'gzip_bytes': len(compressed), 'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
                   'total_cost': {key: sum(value[key] for value in costs.values()) for key in METRICS},
                   'native_catalog_calls_after_source_admission': calls_after_admission,
                   'total_native_calls': len(old.CALLS),
                   'cost_scope': 'all seven categories; validation is not production'}
        write_new(OUT/'ELLIPTIC_MARK_SUMMARY.json', hbw.encode(summary))
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
    parser.add_argument('--global-knowledge-sha', required=True)
    run(parser.parse_args())
