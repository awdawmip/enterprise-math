"""One-shot actual typed marked companion certificate; no work at import time.

This is the modular observer quotient of an integer X6 macro-program. It does
not compute raw Cell trajectories/carries and does not claim a speedup.
"""
from pathlib import Path
from fractions import Fraction
import gzip
import hashlib
import json
import sys
import traceback

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
SCHEMA = 'HBW_MARKED_SECTION_V1'
GUARD_RECORD = '59d0da33e8cc4b1a9f50ec7519c136c597eb827ecec6a06fd841a6c68bb44e21'
EXPECTED = {
    'native_relative_port.py': '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8',
    'HBW_MARKED_SECTION_CONJUGACY.md': 'fbec0b42234fe7a126e5bf03b14842ee0935d7801836b4dce99e5b6167346ce1',
    'conic_transport/conic_transport.py': '420ab2e9502fd45fd2dab85da09a69a129f8a63e95fee17eb9d895d6a9c18d65',
    'conic_transport/EXPERIMENT_PLAN.md': 'b8ce9ebb39124c4a2eba25ad24ad4b998bff9601aa4c79affb617e62483622e5',
    'conic_transport/CONIC_RESULTS.json.gz': 'fc18630a78ffbec5d89d59ac84d8ab21f884f028631e3ac0d4a4c1522c9e8b4e',
}
RAW_SHA = '2ab5d7853310c2a1b9240c51f629b3374ee938f8a4eb75ef0d88a2711c253c75'
OUTPUTS = ('STARTED.json', 'HBW_MARKED_RESULTS.json.gz',
           'HBW_MARKED_SUMMARY.json', 'FAILED_EXECUTION.json.gz')
METRICS = ('adder_digit_replays', 'host_bit_wiring_operations',
           'host_bit_length_calls_in_arithmetic')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plain(value):
    if isinstance(value, Fraction):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    raise TypeError(type(value).__name__)


def encode(value):
    return (json.dumps(value, sort_keys=True, default=plain,
                       separators=(',', ':'))+'\n').encode('utf-8')


def write_new(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


class Work:
    """Available evidence registry; no primitive is executed by its constructor."""
    def __init__(self, binding):
        self.binding = binding
        self.old = None
        self.routes = {}
        self.wiring = []
        self.completed = {}
        self.stage = 'before_import'

    def route(self, N, name):
        require(name not in self.routes, 'duplicate route name')
        route = self.old.Route(N, name)
        self.routes[name] = route
        return route

    def begin(self, route, kind, **fields):
        record = {'id': len(self.wiring), 'route': route.name, 'kind': kind,
                  'status': 'INCOMPLETE',
                  'direct_start': len(route.arithmetic.operations), **fields}
        self.wiring.append(record)
        return record

    def end(self, route, record, output):
        record.update(status='COMPLETE', output=output,
                      direct_stop=len(route.arithmetic.operations))
        return output, record['id']

    def snapshot(self):
        return {'stage': self.stage, 'binding': self.binding,
                'completed': self.completed, 'wiring': self.wiring,
                'routes': {name: route.export() for name, route in self.routes.items()},
                'all_native_records': [] if self.old is None else self.old.CALLS}


def addmod(work, route, x, y):
    rec = work.begin(route, 'addmod', inputs=[x, y], N=route.N)
    value, rec['add_operation'] = route.arithmetic.add(x, y)
    q, remainder, rec['division_operation'] = route.arithmetic.divide(value, route.N)
    rec['quotient'] = q
    return work.end(route, rec, remainder)


def modmul(work, route, x, y):
    rec = work.begin(route, 'modmul', inputs=[x, y], N=route.N)
    value, rec['operations'] = route.arithmetic.modmul(x, y, route.N)
    return work.end(route, rec, value)


def submod(work, route, x, y):
    rec = work.begin(route, 'submod', inputs=[x, y], N=route.N)
    value, rec['operations'] = route.arithmetic.modsubtract(x, y, route.N)
    return work.end(route, rec, value)


def observed_gcd(work, route, x, y):
    rec = work.begin(route, 'gcd_of_difference', inputs=[x, y], N=route.N)
    # Retain the explicit cache key, then the Route's actual public readout.
    difference, rec['difference_link'] = submod(work, route, x, y)
    g = route.observe(x, y)
    rec.update(gcd_key=difference, gcd_certificate_cached_key=str(difference),
               factor_check_key=str(g) if 1 < g < route.N else None)
    return work.end(route, rec, g)


def matmul(work, route, left, right):
    rec = work.begin(route, 'matrix_product', left=left, right=right, entries=[])
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            entry = {'row': i, 'column': j, 'product_links': []}
            rec['entries'].append(entry)
            first, link = modmul(work, route, left[i][0], right[0][j])
            entry['product_links'].append(link)
            second, link = modmul(work, route, left[i][1], right[1][j])
            entry['product_links'].append(link)
            result[i][j], entry['sum_link'] = addmod(work, route, first, second)
    return work.end(route, rec, result)


def matvec(work, route, matrix, point):
    rec = work.begin(route, 'matrix_vector', matrix=matrix, point=point, entries=[])
    result = []
    for i in range(2):
        row = {'row': i, 'product_links': []}
        rec['entries'].append(row)
        left, link = modmul(work, route, matrix[i][0], point[0])
        row['product_links'].append(link)
        right, link = modmul(work, route, matrix[i][1], point[1])
        row['product_links'].append(link)
        value, row['sum_link'] = addmod(work, route, left, right)
        result.append(value)
    return work.end(route, rec, result)


def sfold(work, route, point, setup):
    rec = work.begin(route, 'S_fold', point=point, k=setup['k'])
    kz, rec['kz_link'] = modmul(work, route, setup['k'], point[0])
    partner, rec['partner_link'] = submod(work, route, kz, point[1])
    relation, _, rec['comparison_operation'] = route.arithmetic.compare(point[1], partner)
    rec.update(partner=[point[0], partner], relation=relation)
    canonical = [point[0], point[1] if relation <= 0 else partner]
    return work.end(route, rec, canonical)


def marker(work, route, point, setup):
    rec = work.begin(route, 'marked_readout', point=point,
                     setup_id=setup['setup_id'], b=setup['b'], delta=setup['delta'])
    bz, rec['bz_link'] = modmul(work, route, setup['b'], point[0])
    shifted, rec['subtract_bz_link'] = submod(work, route, point[1], bz)
    value, rec['subtract_delta_link'] = submod(work, route, shifted, setup['delta'])
    g, rec['gcd_link'] = observed_gcd(work, route, value, 0)
    rec['L'] = value
    return work.end(route, rec, g)


def setup_parameters(work, route, a):
    require(type(a) is int and 0 < a < route.N, 'unit input must be a principal residue')
    rec = work.begin(route, 'fixed_setup', N=route.N, a=a)
    b = route.inv(a)
    rec['inverse_certificate_key'] = str(a)
    delta, rec['delta_link'] = submod(work, route, a, b)
    k, rec['k_link'] = addmod(work, route, a, b)
    g, rec['setup_gcd_link'] = observed_gcd(work, route, delta, 0)
    setup = {'setup_id': rec['id'], 'N': route.N, 'a': a, 'b': b,
             'delta': delta, 'k': k, 'setup_gcd': g}
    if 1 < g < route.N:
        setup.update(status='SETUP_FACTOR', factor=g)
    elif g == route.N:
        setup.update(status='DEGENERATE', reason='a_equals_inverse; no regular companion claim')
    else:
        require(g == 1, 'unexpected setup gcd')
        negone, rec['negative_one_link'] = submod(work, route, 0, 1)
        two, rec['initial_two_link'] = addmod(work, route, 1, 1)
        setup.update(status='REGULAR', M=[[0, 1], [negone, k]],
                     Minv=[[k, negone], [1, 0]], P=[[1, 1], [a, b]],
                     S=[[1, 0], [k, negone]], initial=[two, k])
    work.end(route, rec, setup)
    return setup


def validate_matrices(work, route, setup):
    rec = work.begin(route, 'matrix_identity_validation', setup_id=setup['setup_id'], checks=[])
    identity = [[1, 0], [0, 1]]
    for label, left, right, expected in (
            ('M_Minv', setup['M'], setup['Minv'], identity),
            ('Minv_M', setup['Minv'], setup['M'], identity),
            ('S_squared', setup['S'], setup['S'], identity)):
        result, link = matmul(work, route, left, right)
        rec['checks'].append({'label': label, 'link': link, 'expected': expected})
        require(result == expected, label)
    sm, link = matmul(work, route, setup['S'], setup['M'])
    sms, next_link = matmul(work, route, sm, setup['S'])
    require(sms == setup['Minv'], 'S M S')
    rec['checks'].append({'label': 'S_M_S', 'links': [link, next_link], 'expected': setup['Minv']})
    mp, link = matmul(work, route, setup['M'], setup['P'])
    pd, next_link = matmul(work, route, setup['P'], [[setup['a'], 0], [0, setup['b']]])
    require(mp == pd, 'modular intertwining')
    rec['checks'].append({'label': 'M_P_equals_P_D', 'links': [link, next_link]})
    return work.end(route, rec, True)


def layer(work, route, states, matrix, inverse, setup, depth):
    rec = work.begin(route, 'stopped_layer', depth=depth, matrix=matrix, inverse=inverse,
                     input_states=work.old.encode_states(states), branches=[])
    out = {}
    for key, packet in sorted(states.items()):
        if key[0] == 'FACTOR':
            branch = {'input_port': list(key), 'action': 'absorb', 'atom': [[1, 1, 1]],
                      'output_port': list(key)}
            rec['branches'].append(branch)
            route.deposit(out, key, packet, work.old.ONE)
            continue
        for action, current, atom, atom_record in (
                ('identity', None, work.old.DOUBLE, [[1, 4, 2]]),
                ('forward', matrix, work.old.ATOM, [[1, 4, 1]]),
                ('inverse', inverse, work.old.ATOM, [[1, 4, 1]])):
            branch = {'input_port': list(key), 'action': action, 'atom': atom_record}
            rec['branches'].append(branch)
            if current is None:
                point = list(key[1:])
                branch['action_link'] = None
            else:
                point, branch['action_link'] = matvec(work, route, current, list(key[1:]))
            branch['unfolded_point'] = point
            g, branch['marker_link'] = marker(work, route, point, setup)
            branch['gcd'] = g
            if 1 < g < route.N:
                destination = ('FACTOR', g, depth)
                branch['fold_link'] = None
            else:
                canonical, branch['fold_link'] = sfold(work, route, point, setup)
                destination = ('LIVE', *canonical)
            branch['output_port'] = list(destination)
            route.deposit(out, destination, packet, atom)
    require(work.old.total_packet(out).total_mass == 1, 'layer mass')
    work.end(route, rec, work.old.encode_states(out))
    return out, rec['id']


def decode(work, rows):
    result = {}
    for row in rows:
        key = tuple(row['port'])
        require(key not in result, 'duplicate reference port')
        packet = work.old.hist.WeightHistogram.from_counts(
            {Fraction(n, d): count for n, d, count in row['histogram']})
        result[key] = packet
    return result


def reference_projection(work, route, rows, setup, depth):
    rec = work.begin(route, 'saved_conic_P_S_projection', depth=depth, points=[])
    out = {}
    for key, packet in sorted(decode(work, rows).items()):
        point = {'saved_port': list(key)}
        rec['points'].append(point)
        if key[0] == 'FACTOR':
            destination = key
        else:
            mapped, point['P_link'] = matvec(work, route, setup['P'], list(key[1:]))
            old_g, point['original_gcd_link'] = observed_gcd(work, route, key[1], 1)
            new_g, point['marked_gcd_link'] = marker(work, route, mapped, setup)
            require(old_g == new_g, 'saved conic readout equality')
            require(not (1 < old_g < route.N), 'saved live already proper')
            canonical, point['S_fold_link'] = sfold(work, route, mapped, setup)
            destination = ('LIVE', *canonical)
        point['projected_port'] = list(destination)
        route.deposit(out, destination, packet, work.old.ONE)
    work.end(route, rec, work.old.encode_states(out))
    return out, rec['id']


def main_case(work, saved):
    work.stage = 'main_setup'
    setup_route = work.route(35, 'main_setup')
    production = work.route(35, 'production')
    schedule = work.route(35, 'matrix_schedule')
    validation = work.route(35, 'validation')
    setup = setup_parameters(work, setup_route, 2)
    work.completed['main_setup'] = setup
    require(setup['status'] == 'REGULAR', 'declared N35 fixture expects regular setup')
    _, matrix_check = validate_matrices(work, validation, setup)
    states = {('LIVE', *setup['initial']): work.old.ONE}
    matrix, inverse, scalar = setup['M'], setup['Minv'], setup['a']
    case = {'inputs': {'N': 35, 'a': 2, 'layers': 3}, 'setup': setup,
            'matrix_validation_link': matrix_check, 'initial_states': work.old.encode_states(states),
            'layers': [], 'schedule': []}
    work.completed['main_case'] = case
    for depth in range(1, 4):
        work.stage = 'main_layer_'+str(depth)
        baseline = saved['layers'][depth-1]
        require(baseline['depth'] == depth and baseline['multiplier'] == scalar, 'saved schedule')
        states, layer_link = layer(work, production, states, matrix, inverse, setup, depth)
        expected, reference_link = reference_projection(work, validation, baseline['states'], setup, depth)
        require(states == expected, 'complete saved histogram differs at depth '+str(depth))
        case['layers'].append({'depth': depth, 'matrix': matrix, 'inverse': inverse,
                               'layer_link': layer_link, 'reference_projection_link': reference_link,
                               'states': work.old.encode_states(states), 'histograms_equal': True})
        if depth < 3:
            next_matrix, forward_link = matmul(work, schedule, matrix, matrix)
            next_inverse, inverse_link = matmul(work, schedule, inverse, inverse)
            next_scalar, scalar_link = modmul(work, validation, scalar, scalar)
            case['schedule'].append({'after_depth': depth, 'forward_square_link': forward_link,
                                     'inverse_square_link': inverse_link,
                                     'validation_scalar_square_link': scalar_link})
            matrix, inverse, scalar = next_matrix, next_inverse, next_scalar
    final = work.old.final_observation(states)
    require(final == decode(work, saved['output']), 'terminal saved histogram mismatch')
    case['output'] = work.old.encode_states(final)
    require(not production.inverses and not production.tables, 'production unexpectedly acquired inverse/table')
    case['production_state_inverse_certificates'] = 0
    return case


def primepower_fixture(work):
    work.stage = 'primepower_setup'
    setup_route = work.route(25, 'primepower_setup')
    fixture = work.route(25, 'primepower_fixture')
    setup = setup_parameters(work, setup_route, 2)
    work.completed['primepower_setup'] = setup
    require(setup['status'] == 'REGULAR', 'declared primepower fixture expects regular')
    rec = work.begin(fixture, 'primepower_saturation_fixture', N=25, a=2, u=6,
                     setup_id=setup['setup_id'])
    v = fixture.inv(6)
    rec.update(v=v, inverse_certificate_key='6')
    product, rec['unit_product_link'] = modmul(work, fixture, 6, v)
    require(product == 1, 'fixture unit admission')
    point, rec['P_link'] = matvec(work, fixture, setup['P'], [6, v])
    original, rec['original_gcd_link'] = observed_gcd(work, fixture, 6, 1)
    naive, rec['naive_trace_gcd_link'] = observed_gcd(work, fixture, point[0], setup['initial'][0])
    marked, rec['marked_gcd_link'] = marker(work, fixture, point, setup)
    reflected, rec['S_link'] = matvec(work, fixture, setup['S'], point)
    reflected_g, rec['reflected_marked_gcd_link'] = marker(work, fixture, reflected, setup)
    require((original, naive, marked) == (5, 25, 5), 'primepower expected saturation/repair')
    require(reflected_g == original, 'marked gcd must be S invariant')
    result = {'point': point, 'reflected': reflected, 'original_gcd': original,
              'naive_trace_gcd': naive, 'marked_gcd': marked,
              'reflected_marked_gcd': reflected_g, 'wiring_link': rec['id']}
    work.end(fixture, rec, result)
    work.completed['primepower_fixture'] = result
    return result


def route_cost(route):
    """Metadata sum only; nested snapshots are not separately recharged."""
    result = {key: route['arithmetic_stats'][key] for key in METRICS}
    for item in route['inverses'].values():
        for key in METRICS:
            result[key] += item['cost'][key]
    for item in route['gcds'].values():
        for key in METRICS:
            result[key] += item['cost'][key]
    for item in route['tables'].values():
        for key in METRICS:
            result[key] += item['stats']['setup_'+key] + item['stats']['column_'+key]
    result['direct_typed_operations'] = len(route['arithmetic_operations'])
    result['route_invocations'] = route['calls']
    return result


def check_inputs_and_binding():
    for name in OUTPUTS:
        require(not (OUT/name).exists(), 'refuse repeat: '+name)
    guard_raw = (OUT/'STARTUP_GUARD.json').read_bytes()
    guard = json.loads(guard_raw)
    require(guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC', 'wrong activity')
    require(guard['activity_allowed'] is True and guard['persistence_allowed'] is True, 'guard disallows')
    require(guard['sync_debt_events'] == [], 'sync debt')
    require(guard['record_sha256'] == GUARD_RECORD, 'wrong immutable activity record')
    for name, expected in EXPECTED.items():
        require(sha(BASE/name) == expected, 'source/reference mismatch '+name)
    raw = gzip.decompress((BASE/'conic_transport/CONIC_RESULTS.json.gz').read_bytes())
    require(len(raw) == 808809 and hashlib.sha256(raw).hexdigest() == RAW_SHA, 'reference raw mismatch')
    saved = json.loads(raw)
    require(saved['binding']['source_sha256'] == EXPECTED['conic_transport/conic_transport.py'], 'saved source')
    require(saved['binding']['plan_sha256'] == EXPECTED['conic_transport/EXPERIMENT_PLAN.md'], 'saved plan')
    matching = [c for c in saved['cases'] if c['inputs'] == {'N': 35, 'a': 2, 'layers': 3}]
    require(len(matching) == 1, 'reference case ambiguous/missing')
    binding = {'schema': SCHEMA, 'source_sha256': sha(Path(__file__)),
               'plan_sha256': sha(OUT/'PLAN.md'),
               'guard_sha256': hashlib.sha256(guard_raw).hexdigest(), 'guard': guard,
               'dependencies': EXPECTED, 'saved_raw_sha256': RAW_SHA,
               'saved_package_commit': '742f4c75566466751f1071015e0eb7d8249986e2',
               'global_knowledge_read_sha': '7a639845946cb5f8edfa22d3d5d0d47a44f6080e'}
    return binding, matching[0]


def run():
    binding, baseline = check_inputs_and_binding()
    write_new(OUT/'STARTED.json', encode(binding))
    work = Work(binding)
    try:
        sys.path.insert(0, str(BASE))
        import native_relative_port as old
        work.old = old
        work.stage = 'source_admission'
        binding['reused_interfaces'] = old.source_check()
        initial_core_calls = len(old.CALLS)
        main = main_case(work, baseline)
        fixture = primepower_fixture(work)
        work.stage = 'end_source_check'
        require(sha(Path(__file__)) == binding['source_sha256'], 'source changed during execution')
        require(sha(OUT/'PLAN.md') == binding['plan_sha256'], 'plan changed during execution')
        for name, expected in EXPECTED.items():
            require(sha(BASE/name) == expected, 'dependency changed during execution: '+name)
        # Cached source_binding does not execute another native catalog.
        require(old.source_check() == binding['reused_interfaces'], 'runtime binding changed')
        work.stage = 'serialize_success'
        exported = {name: route.export() for name, route in work.routes.items()}
        costs = {name: route_cost(value) for name, value in exported.items()}
        payload = {'schema': SCHEMA, 'status': 'PASS_FINITE_MARKED_SECTION_NOT_ADMITTED',
                   'binding': binding, 'main_case': main, 'primepower_fixture': fixture,
                   'routes': exported, 'wiring': work.wiring,
                   'costs': costs, 'native_catalog_calls_after_source_admission': initial_core_calls,
                   'all_native_records': old.CALLS,
                   'scope': 'modular observer quotient; inactive X6 coordinates fixed zero; raw carries not executed'}
        raw = encode(payload)
        compressed = gzip.compress(raw, mtime=0)
        write_new(OUT/'HBW_MARKED_RESULTS.json.gz', compressed)
        summary = {'schema': SCHEMA, 'status': payload['status'],
                   'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
                   'gzip_bytes': len(compressed), 'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
                   'source_sha256': binding['source_sha256'], 'costs': costs,
                   'total_cost': {key: sum(c[key] for c in costs.values()) for key in METRICS},
                   'historical_conic_costs': {r['name']: route_cost(r) for r in baseline['routes']},
                   'native_catalog_calls_after_source_admission': initial_core_calls,
                   'total_native_calls': len(old.CALLS),
                   'histograms_equal': [item['histograms_equal'] for item in main['layers']],
                   'main_output': main['output'], 'primepower_fixture': fixture,
                   'production_state_inverse_certificates': 0,
                   'cost_scope': 'all typed Route ledgers charged once; histogram invocations separate; no timing, scaling or state-compression claim'}
        write_new(OUT/'HBW_MARKED_SUMMARY.json', encode(summary))
        print(json.dumps(summary, indent=2, default=plain))
    except BaseException:
        failure = {'schema': SCHEMA, 'status': 'FAILED_NOT_RESUMABLE',
                   'traceback': traceback.format_exc(), 'evidence': work.snapshot(),
                   'failure_scope': 'completed primitive records and available wiring; no claim to capture inside an unreturned primitive'}
        write_new(OUT/'FAILED_EXECUTION.json.gz', gzip.compress(encode(failure), mtime=0))
        raise


if __name__ == '__main__':
    run()
