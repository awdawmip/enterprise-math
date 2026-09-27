"""One-shot typed aggregate certificate probes; no scientific work on import."""
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
SCHEMA = 'BRC_AGGREGATE_WITNESS_PROBE_V1'
GRID = ((437, 2, 1), (35, 2, 2), (19, 2, 1), (25, 2, 1))
ACTIVITY_ID = 'RA-CAAAC604CB513AEA8BBC1DFC'
EXPECTED = {
    'native_relative_port.py': '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8',
    'EXPERIMENT_PLAN.md': '931d7b7659c3e62707f10d20a2312cb03c945e6354f715c1ebda5d72fdb178a6',
    'AGGREGATE_WITNESS_PROBE_AUDIT.md': 'c76465057ce793825916c3d22c85acc83703becfeb5154c05b362468dd5933fd',
    'hbw_marked_section/hbw_marked_section.py': 'e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851',
}
OUTPUTS = ('STARTED.json', 'AGGREGATE_RESULTS.json.gz',
           'AGGREGATE_SUMMARY.json', 'FAILED_EXECUTION.json.gz',
           'FAILED_SERIALIZATION.txt')
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


def check_binding(args):
    for name in OUTPUTS:
        require(not (OUT/name).exists(), 'refuse repeat: '+name)
    require(re.fullmatch('[0-9a-f]{64}', args.guard_record_sha256) is not None,
            'guard record SHA256 must be 64 lowercase hex characters')
    guard_path = Path(args.guard_file).resolve()
    guard_raw = guard_path.read_bytes()
    guard = json.loads(guard_raw)
    require(guard['activity_id'] == ACTIVITY_ID, 'wrong activity')
    require(guard['activity_allowed'] is True and guard['persistence_allowed'] is True,
            'guard disallows activity/persistence')
    require(guard['sync_debt_events'] == [], 'sync debt')
    require(guard['record_sha256'] == args.guard_record_sha256,
            'guard differs from supplied immutable activity record')
    for name, expected in EXPECTED.items():
        require(sha(BASE/name) == expected, 'frozen source mismatch: '+name)
    return {'schema': SCHEMA, 'source_sha256': sha(Path(__file__)),
            'plan_sha256': sha(OUT/'PLAN.md'), 'dependencies': EXPECTED,
            'guard_path': str(guard_path), 'guard_sha256': hashlib.sha256(guard_raw).hexdigest(),
            'expected_guard_record_sha256': args.guard_record_sha256, 'guard': guard,
            'inputs': [{'N': n, 'a': a, 'layers': t} for n, a, t in GRID],
            'global_knowledge_read_sha': '7a639845946cb5f8edfa22d3d5d0d47a44f6080e'}


def load_wrappers():
    # This pinned module imports only standard-library modules at module scope.
    path = BASE/'hbw_marked_section/hbw_marked_section.py'
    spec = importlib.util.spec_from_file_location('aggregate_hbw_wrappers', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def probe_class(g, N):
    if g == 1:
        return 'UNIT'
    if g == N:
        return 'SATURATED'
    require(1 < g < N, 'invalid gcd output')
    return 'PROPER_FACTOR'


def doubling(work, hbw, route, state, depth):
    rec = work.begin(route, 'aggregate_doubling', depth=depth, before=dict(state))
    A2, rec['A_square_link'] = hbw.modmul(work, route, state['A'], state['A'])
    one_A, rec['one_plus_A_link'] = hbw.addmod(work, route, 1, state['A'])
    one_A2, rec['one_plus_A_square_link'] = hbw.addmod(work, route, 1, A2)
    G, rec['G_update_link'] = hbw.modmul(work, route, state['G'], one_A)
    H, rec['H_update_link'] = hbw.modmul(work, route, state['H'], one_A2)
    q, rec['Q_update_link'] = hbw.addmod(work, route, state['q'], state['q'])
    return work.end(route, rec, {'A': A2, 'G': G, 'H': H, 'q': q})


def read_probes(work, hbw, route, state):
    rec = work.begin(route, 'aggregate_readout', registers=dict(state), probes=[])
    qH, rec['qH_link'] = hbw.modmul(work, route, state['q'], state['H'])
    G2, rec['G_square_link'] = hbw.modmul(work, route, state['G'], state['G'])
    dm, rec['D_minus_link'] = hbw.submod(work, route, qH, G2)
    dp, rec['D_plus_link'] = hbw.addmod(work, route, qH, G2)
    ct, rec['C_tilde_link'] = hbw.modmul(work, route, dm, dp)
    outputs = {}
    for label, value in (('D_minus', dm), ('D_plus', dp), ('C_tilde', ct)):
        g, link = hbw.observed_gcd(work, route, value, 0)
        item = {'name': label, 'value': value, 'gcd': g,
                'classification': probe_class(g, route.N), 'gcd_link': link,
                'factor_check_key': str(g) if 1 < g < route.N else None}
        rec['probes'].append(item)
        outputs[label] = item
    return work.end(route, rec, outputs)


def determinant(work, hbw, route, moments):
    rec = work.begin(route, 'moment_determinant', moments=list(moments))
    product, rec['M0_M2_link'] = hbw.modmul(work, route, moments[0], moments[2])
    square, rec['M1_square_link'] = hbw.modmul(work, route, moments[1], moments[1])
    value, rec['difference_link'] = hbw.submod(work, route, product, square)
    return work.end(route, rec, value)


def validate_first_case(work, hbw, case):
    require(case['inputs'] == {'N': 437, 'a': 2, 'layers': 1},
            'validation lease is only the first declared one-layer case')
    N, a = case['inputs']['N'], case['inputs']['a']
    setup_route = work.route(N, 'case0_validation_setup')
    moments_route = work.route(N, 'case0_validation_original_moments')
    hbw_route = work.route(N, 'case0_validation_hbw_moments')
    check_route = work.route(N, 'case0_validation_identities')
    report = {'scope': 'one-layer unstopped summary identities, no branch expansion',
              'checks': [], 'moments': {}}
    case['validation'] = report
    work.stage = 'case0_validation_setup'
    setup = hbw.setup_parameters(work, setup_route, a)
    report['setup'] = setup
    require(setup['status'] == 'REGULAR', 'declared validation requires regular marked section')
    b, delta, k = setup['b'], setup['delta'], setup['k']

    rec = work.begin(check_route, 'marked_dual_row_validation', setup_id=setup['setup_id'])
    negb, rec['negative_b_link'] = hbw.submod(work, check_route, 0, b)
    ell = [negb, 1]
    transposed = [[setup['M'][j][i] for j in range(2)] for i in range(2)]
    left, rec['ell_M_link'] = hbw.matvec(work, check_route, transposed, ell)
    right = []
    rec['a_ell_links'] = []
    for item in ell:
        value, link = hbw.modmul(work, check_route, a, item)
        right.append(value)
        rec['a_ell_links'].append(link)
    require(left == right, 'marked dual eigenrow identity')
    bz, rec['initial_bz_link'] = hbw.modmul(work, check_route, b, setup['initial'][0])
    initial_linear, rec['initial_linear_link'] = hbw.submod(work, check_route, setup['initial'][1], bz)
    L0, rec['initial_L_link'] = hbw.submod(work, check_route, initial_linear, delta)
    require(L0 == 0, 'initial marked value')
    _, dual_link = work.end(check_route, rec, {'ell_M': left, 'a_ell': right, 'L0': L0})
    report['checks'].append({'name': 'marked_dual_and_initial', 'link': dual_link, 'equal': True})

    work.stage = 'case0_validation_original_moments'
    rec = work.begin(moments_route, 'unstopped_original_moment_step', initial=[1, 1, 1], a=a, b=b)
    two, rec['two_link'] = hbw.addmod(work, moments_route, 1, 1)
    four, rec['four_link'] = hbw.addmod(work, moments_route, two, two)
    s, rec['s_link'] = hbw.addmod(work, moments_route, a, b)
    alpha, rec['alpha_link'] = hbw.addmod(work, moments_route, s, two)
    beta, rec['beta_link'] = hbw.modmul(work, moments_route, s, s)
    m0, rec['M0_link'] = hbw.modmul(work, moments_route, four, 1)
    m1, rec['M1_link'] = hbw.modmul(work, moments_route, alpha, 1)
    m2, rec['M2_link'] = hbw.modmul(work, moments_route, beta, 1)
    moments, moment_link = work.end(moments_route, rec, [m0, m1, m2])
    C, C_link = determinant(work, hbw, moments_route, moments)
    report['moments']['original'] = {'values': moments, 'link': moment_link,
                                      'determinant': C, 'determinant_link': C_link}

    work.stage = 'case0_validation_hbw_moments'
    rec = work.begin(hbw_route, 'marked_affine_moment_step', initial=[1, L0, 0],
                     a=a, b=b, delta=delta)
    am1, rec['a_minus_one_link'] = hbw.submod(work, hbw_route, a, 1)
    bm1, rec['b_minus_one_link'] = hbw.submod(work, hbw_route, b, 1)
    bp, rec['forward_offset_link'] = hbw.modmul(work, hbw_route, delta, am1)
    bm, rec['inverse_offset_link'] = hbw.modmul(work, hbw_route, delta, bm1)
    ht, rec['two_link'] = hbw.addmod(work, hbw_route, 1, 1)
    hf, rec['four_link'] = hbw.addmod(work, hbw_route, ht, ht)
    ab_sum, rec['a_plus_b_link'] = hbw.addmod(work, hbw_route, a, b)
    linear_coef, rec['linear_coefficient_link'] = hbw.addmod(work, hbw_route, ht, ab_sum)
    offset_sum, rec['offset_sum_link'] = hbw.addmod(work, hbw_route, bp, bm)
    a2, rec['a_square_link'] = hbw.modmul(work, hbw_route, a, a)
    b2, rec['b_square_link'] = hbw.modmul(work, hbw_route, b, b)
    squares_sum, rec['squares_sum_link'] = hbw.addmod(work, hbw_route, a2, b2)
    quadratic_coef, rec['quadratic_coefficient_link'] = hbw.addmod(work, hbw_route, ht, squares_sum)
    ap, rec['a_forward_offset_link'] = hbw.modmul(work, hbw_route, a, bp)
    bm_product, rec['b_inverse_offset_link'] = hbw.modmul(work, hbw_route, b, bm)
    cross_sum, rec['cross_sum_link'] = hbw.addmod(work, hbw_route, ap, bm_product)
    cross_coef, rec['cross_coefficient_link'] = hbw.addmod(work, hbw_route, cross_sum, cross_sum)
    bp2, rec['forward_offset_square_link'] = hbw.modmul(work, hbw_route, bp, bp)
    bm2, rec['inverse_offset_square_link'] = hbw.modmul(work, hbw_route, bm, bm)
    constant_coef, rec['constant_coefficient_link'] = hbw.addmod(work, hbw_route, bp2, bm2)
    h0, rec['h0_link'] = hbw.modmul(work, hbw_route, hf, 1)
    h1_linear, rec['h1_linear_link'] = hbw.modmul(work, hbw_route, linear_coef, L0)
    h1_offset, rec['h1_offset_link'] = hbw.modmul(work, hbw_route, offset_sum, 1)
    h1, rec['h1_link'] = hbw.addmod(work, hbw_route, h1_linear, h1_offset)
    initial_second, rec['initial_second_moment_link'] = hbw.modmul(work, hbw_route, L0, L0)
    h2_quadratic, rec['h2_quadratic_link'] = hbw.modmul(work, hbw_route, quadratic_coef, initial_second)
    h2_cross, rec['h2_cross_link'] = hbw.modmul(work, hbw_route, cross_coef, L0)
    h2_constant, rec['h2_constant_link'] = hbw.modmul(work, hbw_route, constant_coef, 1)
    h2_partial, rec['h2_partial_link'] = hbw.addmod(work, hbw_route, h2_quadratic, h2_cross)
    h2, rec['h2_link'] = hbw.addmod(work, hbw_route, h2_partial, h2_constant)
    marked, marked_link = work.end(hbw_route, rec, [h0, h1, h2])
    D_L, D_L_link = determinant(work, hbw, hbw_route, marked)
    report['moments']['marked'] = {'values': marked, 'link': marked_link,
                                   'determinant': D_L, 'determinant_link': D_L_link}

    work.stage = 'case0_validation_identities'
    rec = work.begin(check_route, 'summary_bridge_identities', original=moments, marked=marked,
                     C=C, D_L=D_L, C_tilde=case['probes']['C_tilde']['value'])
    d2, rec['delta_square_link'] = hbw.modmul(work, check_route, delta, delta)
    first_difference, rec['M1_minus_M0_link'] = hbw.submod(work, check_route, m1, m0)
    expected_h1, rec['expected_h1_link'] = hbw.modmul(work, check_route, delta, first_difference)
    twice_m1, rec['twice_M1_link'] = hbw.addmod(work, check_route, m1, m1)
    second_partial, rec['M2_minus_twice_M1_link'] = hbw.submod(work, check_route, m2, twice_m1)
    second_centered, rec['centered_second_link'] = hbw.addmod(work, check_route, second_partial, m0)
    expected_h2, rec['expected_h2_link'] = hbw.modmul(work, check_route, d2, second_centered)
    expected_D_L, rec['scaled_determinant_link'] = hbw.modmul(work, check_route, d2, C)
    b_squared, rec['inverse_square_link'] = hbw.modmul(work, check_route, b, b)
    expected_C, rec['inverse_scaled_C_tilde_link'] = hbw.modmul(
        work, check_route, b_squared, case['probes']['C_tilde']['value'])
    require([h0, h1, h2] == [m0, expected_h1, expected_h2], 'marked moment bridge')
    require(D_L == expected_D_L, 'marked determinant unit scaling')
    require(C == expected_C, 'inverse-free determinant unit scaling')
    gC, rec['C_gcd_link'] = hbw.observed_gcd(work, check_route, C, 0)
    gL, rec['D_L_gcd_link'] = hbw.observed_gcd(work, check_route, D_L, 0)
    gct = case['probes']['C_tilde']['gcd']
    require(gC == gL == gct, 'determinant gcd equivalence')
    _, checks_link = work.end(check_route, rec,
        {'moment_equal': True, 'determinant_equal': True, 'inverse_free_equal': True,
         'gcds': {'C': gC, 'D_L': gL, 'C_tilde': gct}})
    report['checks'].append({'name': 'aggregate_marked_bridge', 'link': checks_link, 'equal': True})
    report['status'] = 'PASS_ONE_LAYER_SUMMARY_IDENTITIES'
    return report


def main_case(work, hbw, index, N, a, t):
    prefix = 'case'+str(index)
    setup = work.route(N, prefix+'_setup')
    production = work.route(N, prefix+'_production')
    readout = work.route(N, prefix+'_readout')
    case = {'inputs': {'N': N, 'a': a, 'layers': t}, 'layers': [],
            'public_horizon': {'Q': {'base': 2, 'exponent': t},
                               'microscopic_count': {'base': 4, 'exponent': t}},
            'production_route_names': [setup.name, production.name, readout.name]}
    work.completed[prefix] = case
    work.stage = prefix+'_setup'
    require(type(N) is int and N > 1 and type(a) is int and 0 < a < N,
            'principal input residues required')
    require(type(t) is int and t >= 0, 'nonnegative public horizon required')
    g, case['unit_gcd_link'] = hbw.observed_gcd(work, setup, a, 0)
    case['unit_gcd'] = g
    if g != 1:
        case['status'] = 'SETUP_FACTOR' if 1 < g < N else 'NONUNIT_UNUSABLE'
        return case
    state = {'A': a, 'G': 1, 'H': 1, 'q': 1}
    case['initial_registers'] = dict(state)
    for depth in range(1, t+1):
        work.stage = prefix+'_layer_'+str(depth)
        state, link = doubling(work, hbw, production, state, depth)
        case['layers'].append({'depth': depth, 'registers': dict(state), 'link': link})
    work.stage = prefix+'_readout'
    case['probes'], case['readout_link'] = read_probes(work, hbw, readout, state)
    classifications = [row['classification'] for row in case['probes'].values()]
    case['status'] = ('PROBE_FOUND_FACTOR' if 'PROPER_FACTOR' in classifications else
                      'SATURATED_WITHOUT_PROPER_FACTOR' if 'SATURATED' in classifications else
                      'NO_FACTOR_FROM_DECLARED_PROBES')
    case['production_standalone_inverse_certificates'] = sum(
        len(route.inverses) for route in (setup, production, readout))
    require(case['production_standalone_inverse_certificates'] == 0,
            'unexpected inverse in aggregate production contract')
    require(not setup.tables and not production.tables and not readout.tables,
            'unexpected inverse-bearing modular table in aggregate production')
    if index == 0:
        validate_first_case(work, hbw, case)
    return case


def check_end_binding(binding):
    require(sha(Path(__file__)) == binding['source_sha256'], 'source changed during execution')
    require(sha(OUT/'PLAN.md') == binding['plan_sha256'], 'plan changed during execution')
    require(sha(Path(binding['guard_path'])) == binding['guard_sha256'], 'guard changed during execution')
    for name, expected in EXPECTED.items():
        require(sha(BASE/name) == expected, 'dependency changed during execution: '+name)


def run(args):
    binding = check_binding(args)
    write_new(OUT/'STARTED.json', encode(binding))
    work = None
    try:
        hbw = load_wrappers()
        work = hbw.Work(binding)
        sys.path.insert(0, str(BASE))
        import native_relative_port as old
        work.old = old
        work.stage = 'native_source_admission'
        binding['reused_interfaces'] = old.source_check()
        calls_after_source_admission = len(old.CALLS)
        cases = [main_case(work, hbw, i, N, a, t) for i, (N, a, t) in enumerate(GRID)]
        work.stage = 'end_source_check'
        check_end_binding(binding)
        require(old.source_check() == binding['reused_interfaces'], 'native runtime binding changed')
        routes = {name: route.export() for name, route in work.routes.items()}
        costs = {name: hbw.route_cost(route) for name, route in routes.items()}
        payload = {'schema': SCHEMA, 'status': 'PASS_FINITE_AGGREGATE_AUTHOR_EXECUTION_NOT_ADMITTED',
                   'binding': binding, 'cases': cases, 'routes': routes,
                   'wiring': work.wiring, 'costs': costs,
                   'native_catalog_calls_after_source_admission': calls_after_source_admission,
                   'all_native_records': old.CALLS,
                   'scope': 'unstopped polynomial certificate probes; no first-hit law or branch expansion'}
        work.stage = 'serialize_success'
        raw = hbw.encode(payload)
        compressed = gzip.compress(raw, mtime=0)
        write_new(OUT/'AGGREGATE_RESULTS.json.gz', compressed)
        summaries = []
        for case in cases:
            item = {'inputs': case['inputs'], 'status': case['status'],
                    'unit_gcd': case['unit_gcd'], 'layers': case['layers'],
                    'probes': case.get('probes', {}),
                    'production_costs': {name: costs[name] for name in case['production_route_names']},
                    'production_standalone_inverse_certificates': case.get(
                        'production_standalone_inverse_certificates', 0)}
            if 'validation' in case:
                item['validation'] = case['validation']
            summaries.append(item)
        summary = {'schema': SCHEMA, 'status': payload['status'],
                   'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
                   'gzip_bytes': len(compressed), 'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
                   'source_sha256': binding['source_sha256'], 'plan_sha256': binding['plan_sha256'],
                   'cases': summaries, 'costs': costs,
                   'total_cost': {key: sum(value[key] for value in costs.values()) for key in METRICS},
                   'native_catalog_calls_after_source_admission': calls_after_source_admission,
                   'total_native_calls': len(old.CALLS),
                   'cost_scope': 'typed ledgers; setup/production/readout/validation separate; no total runtime or success-rate claim'}
        write_new(OUT/'AGGREGATE_SUMMARY.json', hbw.encode(summary))
        print(json.dumps(summary, indent=2, default=hbw.plain))
    except BaseException:
        failure_trace = traceback.format_exc()
        try:
            evidence = {'binding': binding} if work is None else work.snapshot()
            failure = {'schema': SCHEMA, 'status': 'FAILED_NOT_RESUMABLE',
                       'traceback': failure_trace, 'evidence': evidence,
                       'scope': 'available completed records; an unreturned primitive may lack its final internal record'}
            failure_raw = encode(failure) if work is None else hbw.encode(failure)
            write_new(OUT/'FAILED_EXECUTION.json.gz', gzip.compress(failure_raw, mtime=0))
        except BaseException:
            fallback = failure_trace+'\nFailure serialization also failed:\n'+traceback.format_exc()
            write_new(OUT/'FAILED_SERIALIZATION.txt', fallback.encode('utf-8'))
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--guard-file', required=True)
    parser.add_argument('--guard-record-sha256', required=True)
    run(parser.parse_args())
