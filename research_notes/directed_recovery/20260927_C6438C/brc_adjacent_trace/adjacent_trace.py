"""One-shot typed adjacent Lucas traces and two signed return clocks.

Importing this file imports no scientific dependency. Only run() executes them.
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
FREE = OUT.parent / 'sep27-brc-hbw-free-trace'
ELLIPTIC = OUT.parent / 'sep27-brc-elliptic-mark'
OLD = OUT.parent / 'sep27-brc-native-tool-discovery'
SCHEMA = 'BRC_ADJACENT_TRACE_TWO_CLOCK_V1'
ACTIVITY_ID = 'RA-CAAAC604CB513AEA8BBC1DFC'
GRID = ((77, 3, 4, 6), (77, 3, 8, 10), (49, 3, 8, 10), (77, 3, 6, 8))
FREE_EXPECTED = {
    'TRANSLATED_TRACE_MARK.md': 'a3562a0b3151c86a7d5c1767af876daafa245ea7426da7dc387c70f0db9f0c6c',
    'TRANSLATED_TRACE_MARK_REVIEW.md': '1c5930502377fa9bd925ded827f3eb034668e6d7fd86dd27d40adfe172ac60dc',
    'FREE_TRACE_TORUS_WITNESS.md': '6ad4bbf2db92ffbec7fc57c8da3e16aca9f43a6fb05b89a73aa396aca6f1730c',
    'TRACE_SQUARE_VALUATION_LEMMA.md': '35a8259080ccfb7b608eab922a1562c20836e718b9dff09f2af6209937bcb3d5',
    'native_probe/free_trace_probe.py': '2f0981f1dd25e8160bcd80207a6bc92d080e291b545f3be62b95eddffdd36708',
    'native_probe/PLAN.md': 'c05b238b7c1f1c72319f6bbe3e41652f2d274f41cc05b6cdaf85e7c6a9e4cb52',
    'native_probe/FREE_TRACE_SUMMARY.json': '73fd0e23753e4a8dd46a02c7d24d2bc123c0e267a789a734d6e6fd6bc516c41e',
    'native_probe/FREE_TRACE_RESULTS.json.gz': '2b714edc7cd51728377ef5269451724feb96a8896af3037fcb60101ef09e37c5',
}
ELLIPTIC_EXPECTED = {
    'TWO_CLOCK_TRANSLATED_SECTION.md': '2294c28339c1de5b40d1a3012ad7762c063229a684676d35dff78821b7ea4a9b',
    'TWO_CLOCK_SECTION_REVIEW.md': '4fe4b5a07dc1e4494babe7ec68782919146d3dd62cd0d64155765b384e742b4a',
    'TWO_CLOCK_SECTION_PARENT_REVIEW.md': 'be6b765fce71a4ca4d7a40606ba989b63806282569f921b9a2cf27230e86fe0a',
}
OLD_EXPECTED = {
    'native_relative_port.py': '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8',
    'hbw_marked_section/hbw_marked_section.py': 'e2929468d9b430f9a0ef93a3412f132c692ce994c7b5061bece21a3960974851',
}
LOCAL_EXPECTED = {
    'EQUAL_OUTPUT_COMPARISON_CONTRACT.md': 'd0a334328bcf1d2be5860a2eca7970aebb3916a9586890e7d0acd4228d21cbf8',
}
BASELINE_RAW_SHA = 'bd9ccd13f75e41b44edcfd294990ce1bd5673011fe906b4780c05662dfe70158'
OUTPUTS = ('STARTED.json', 'ADJACENT_TRACE_RESULTS.json.gz', 'ADJACENT_TRACE_SUMMARY.json',
           'FAILED_EXECUTION.json.gz', 'FAILED_SERIALIZATION.txt')
CATEGORIES = ('setup', 'power', 'expressions', 'joint', 'single', 'quotient', 'validation')
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
    for root, mapping in ((FREE, FREE_EXPECTED), (ELLIPTIC, ELLIPTIC_EXPECTED),
                          (OLD, OLD_EXPECTED), (OUT, LOCAL_EXPECTED)):
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
            'plan_sha256': sha(OUT/'PLAN.md'), 'free_dependencies': FREE_EXPECTED,
            'elliptic_dependencies': ELLIPTIC_EXPECTED, 'old_dependencies': OLD_EXPECTED,
            'local_dependencies': LOCAL_EXPECTED, 'guard_path': str(path),
            'guard_sha256': hashlib.sha256(raw).hexdigest(),
            'expected_guard_record_sha256': args.guard_record_sha256, 'guard': guard,
            'inputs': [{'N': N, 'k': k, 'E': E, 'Eplus2': E2} for N, k, E, E2 in GRID],
            'coordinator_actual_global_knowledge_read_sha': args.global_knowledge_sha,
            'author_actual_policy_read_sha': 'b3047603607cebcbd3f39e7028bf707f199c3f48'}


def load_frozen():
    path = FREE/'native_probe/free_trace_probe.py'
    spec = importlib.util.spec_from_file_location('adjacent_frozen_free_trace', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, module.load_wrappers()


class Ops:
    """Named wiring to actual frozen operations, without host propagation."""
    def __init__(self, work, hbw, free, route, rec):
        self.work, self.hbw, self.free, self.route, self.rec = work, hbw, free, route, rec
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
        return self.call(role, self.free.common_gcd, values)


def adjacent_power(work, hbw, free, route, parameters, E):
    bits = format(E, 'b')
    pair = [parameters['two'], parameters['k']]
    rec = work.begin(route, 'ordered_adjacent_trace_power', E=E, k=parameters['k'],
                     public_exponent_bits=bits, initial=list(pair), steps=[])
    for index, bit in enumerate(bits):
        step = {'bit_index': index, 'bit': bit, 'before': list(pair), 'status': 'INCOMPLETE'}
        rec['steps'].append(step)
        op = Ops(work, hbw, free, route, step)
        product = op.mul('adjacent_product', pair[0], pair[1])
        odd = op.sub('odd_trace', product, parameters['k'])
        selected = pair[0] if bit == '0' else pair[1]
        square = op.mul('selected_square', selected, selected)
        even = op.sub('selected_even_trace', square, parameters['two'])
        pair = [even, odd] if bit == '0' else [odd, even]
        step.update(after=list(pair), status='COMPLETE')
    rec['public_bit_control'] = {'bits_read': len(bits), 'multiplications_per_bit': 2,
                                 'subtractions_per_bit': 2,
                                 'orientation': '(V_E,V_(E+1)); never folded'}
    return work.end(route, rec, pair)


def signed_expressions(work, hbw, free, route, pair, parameters):
    rec = work.begin(route, 'both_signed_translated_expressions', pair=list(pair), signs=[])
    output = {}
    for label in ('identity', 'antipodal'):
        step = {'label': label, 'status': 'INCOMPLETE'}
        rec['signs'].append(step)
        op = Ops(work, hbw, free, route, step)
        if label == 'identity':
            tau = op.sub('tau', pair[0], parameters['two'])
            w = op.sub('w', pair[1], parameters['k'])
            target = 1
        else:
            tau = op.add('tau', pair[0], parameters['two'])
            w = op.add('w', pair[1], parameters['k'])
            target = parameters['negative_one']
        output[label] = {'target': target, 'tau': tau, 'w': w}
        step.update(output=output[label], status='COMPLETE')
    return work.end(route, rec, output)


def quotient_readout(work, free, route, union, first):
    rec = work.begin(route, 'exact_two_clock_quotient', numerator=union, denominator=first)
    require(first > 0 and union > 0, 'positive exact quotient inputs')
    value, remainder, rec['division_operation'] = route.arithmetic.divide(union, first)
    rec.update(quotient=value, remainder=remainder)
    require(remainder == 0 and value >= 1, 'two-clock exact division failed')
    rec['factor_check_key'] = free.factor_check(work, route, value)
    return work.end(route, rec, {'value': value, 'class': free.classification(value, route.N),
                                 'remainder': remainder})


def matrix_residual(work, hbw, free, route, full, target):
    rec = work.begin(route, 'full_matrix_signed_residual_ideal', matrix=full, target=target)
    op = Ops(work, hbw, free, route, rec)
    r00 = op.sub('residual_00', full[0][0], target)
    r11 = op.sub('residual_11', full[1][1], target)
    entries = [r00, full[0][1], full[1][0], r11]
    common = op.common('all_four_entries_gcd', entries)
    return work.end(route, rec, {'entries': entries, 'common_gcd': common})


def validate(work, hbw, free, route, parameters, E, E2, pair, expressions, readouts):
    rec = work.begin(route, 'independent_two_clock_full_matrix_validation', E=E, Eplus2=E2,
                     pair=list(pair), signed_checks=[], determinants=[])
    op = Ops(work, hbw, free, route, rec)
    M = parameters['M']
    inverse, rec['inverse_check_link'] = hbw.matmul(work, route, M, parameters['Minv'])
    require(inverse == [[1, 0], [0, 1]], 'companion inverse')
    full, rec['E_power_link'] = free.matrix_power_validation(work, hbw, route, M, E)
    full2, rec['Eplus2_power_link'] = free.matrix_power_validation(work, hbw, route, M, E2)
    next_full, rec['Eplus1_link'] = hbw.matmul(work, route, full, M)
    second_full, rec['Eplus2_from_adjacency_link'] = hbw.matmul(work, route, next_full, M)
    require(second_full == full2, 'public E+2/full matrix chronology')
    trace0 = op.add('trace_E', full[0][0], full[1][1])
    trace1 = op.add('trace_Eplus1', next_full[0][0], next_full[1][1])
    require([trace0, trace1] == pair, 'both adjacent traces/full matrices')
    rec.update(full_E=full, full_Eplus1=next_full, full_Eplus2=full2)
    for label, matrix in (('E', full), ('Eplus2', full2)):
        ad = op.mul(label+'_det_ad', matrix[0][0], matrix[1][1])
        bc = op.mul(label+'_det_bc', matrix[0][1], matrix[1][0])
        determinant = op.sub(label+'_det', ad, bc)
        rec['determinants'].append({'clock': label, 'value': determinant})
        require(determinant == 1, 'full matrix determinant')
    for label in ('identity', 'antipodal'):
        ex, observed = expressions[label], readouts[label]
        check = {'label': label, 'target': ex['target'], 'status': 'INCOMPLETE'}
        rec['signed_checks'].append(check)
        sop = Ops(work, hbw, free, route, check)
        first, check['E_ideal_link'] = matrix_residual(work, hbw, free, route, full, ex['target'])
        second, check['Eplus2_ideal_link'] = matrix_residual(work, hbw, free, route, full2, ex['target'])
        require(first['common_gcd'] == observed['dE'], 'first clock ideal')
        require(second['common_gcd'] == observed['dEplus2']['value'], 'second clock ideal')
        x, y = first['entries'][1], first['entries'][3]
        kx = sop.mul('k_x', parameters['k'], x)
        residual00 = sop.sub('cyclic_residual_00', y, kx)
        negative_x = sop.sub('negative_x', 0, x)
        require(first['entries'] == [residual00, x, negative_x, y], 'cyclic residual four entries')
        double_y = sop.add('two_y', y, y)
        tau = sop.sub('tau_from_cyclic_mark', double_y, kx)
        ky = sop.mul('k_y', parameters['k'], y)
        double_x = sop.add('two_x', x, x)
        w = sop.sub('w_from_cyclic_mark', ky, double_x)
        require(tau == ex['tau'] and w == ex['w'], 'translated mark matrix bridge')
        coprime = sop.common('clock_divisors_coprime', [first['common_gcd'], second['common_gcd']])
        require(coprime == 1, 'return clocks must have disjoint prime support')
        product, check['exact_product_operation'] = route.arithmetic.multiply(
            first['common_gcd'], second['common_gcd'])
        require(product == observed['dUnion'], 'exact integer two-clock product')
        check.update(first_clock_gcd=first['common_gcd'], second_clock_gcd=second['common_gcd'],
                     product=product, coprime=coprime, tau=tau, w=w, status='COMPLETE')
    return work.end(route, rec, {'both_adjacent_traces_equal': True,
                                 'full_E': full, 'full_Eplus2': full2,
                                 'signed_checks': rec['signed_checks']})


def main_case(work, hbw, free, index, N, k, E, E2):
    require(type(N) is int and N > 1, 'integer modulus greater than one')
    require(type(k) is int and 0 <= k < N, 'principal public trace required')
    require(type(E) is int and E >= 0 and type(E2) is int and E2 >= 0,
            'nonnegative public integer clocks')
    prefix = 'case'+str(index)
    case = {'inputs': {'N': N, 'k': k, 'E': E, 'Eplus2': E2}, 'route_names': {}, 'readouts': {}}
    work.completed[prefix] = case
    routes = {}
    for category in CATEGORIES:
        work.stage = prefix+'_construct_'+category
        routes[category] = work.route(N, prefix+'_'+category)
        case['route_names'][category] = routes[category].name
    work.stage = prefix+'_setup'
    parameters, case['setup_link'] = free.setup(work, hbw, routes['setup'], k)
    case['setup'] = parameters
    require(parameters['status'] == 'REGULAR', 'declared regular fixture inadmissible')
    clock = work.begin(routes['setup'], 'public_clock_relation_check', E=E, declared_Eplus2=E2)
    actual_E2, clock['addition_operation'] = routes['setup'].arithmetic.add(E, 2)
    clock['actual_Eplus2'] = actual_E2
    require(actual_E2 == E2, 'public Eplus2 must equal E+2')
    _, case['clock_relation_link'] = work.end(routes['setup'], clock, True)
    work.stage = prefix+'_power'
    pair, case['power_link'] = adjacent_power(work, hbw, free, routes['power'], parameters, E)
    case['terminal_pair'] = pair
    work.stage = prefix+'_expressions'
    expressions, case['expressions_link'] = signed_expressions(
        work, hbw, free, routes['expressions'], pair, parameters)
    case['expressions'] = expressions
    for label in ('identity', 'antipodal'):
        ex = expressions[label]
        readout = {'target': ex['target']}
        case['readouts'][label] = readout
        work.stage = prefix+'_'+label+'_joint'
        readout['dE'], readout['joint_link'] = free.common_gcd(
            work, routes['joint'], [ex['tau'], ex['w']])
        readout['dE_class'] = free.classification(readout['dE'], N)
        work.stage = prefix+'_'+label+'_single'
        readout['dUnion'], readout['single_link'] = hbw.observed_gcd(
            work, routes['single'], ex['w'], 0)
        readout['dUnion_class'] = free.classification(readout['dUnion'], N)
        work.stage = prefix+'_'+label+'_quotient'
        readout['dEplus2'], readout['quotient_link'] = quotient_readout(
            work, free, routes['quotient'], readout['dUnion'], readout['dE'])
    work.stage = prefix+'_validation'
    case['validation'], case['validation_link'] = validate(
        work, hbw, free, routes['validation'], parameters, E, E2, pair, expressions, case['readouts'])
    require(all(not r.tables and not r.inverses for r in routes.values()), 'unexpected inverse/table')
    case['status'] = 'COMPLETE_FINITE_TWO_CLOCK_OBSERVATION_NOT_SUCCESS_RATE'
    return case


def compare_saved_baseline(cases):
    """Pure I/O after every new scientific case; no old runner is invoked."""
    compressed = (FREE/'native_probe/FREE_TRACE_RESULTS.json.gz').read_bytes()
    require(hashlib.sha256(compressed).hexdigest() == FREE_EXPECTED['native_probe/FREE_TRACE_RESULTS.json.gz'],
            'saved compressed baseline binding')
    raw = gzip.decompress(compressed)
    require(hashlib.sha256(raw).hexdigest() == BASELINE_RAW_SHA, 'saved raw baseline binding')
    saved = json.loads(raw)
    require(saved['schema'] == 'BRC_FREE_TRACE_RETURN_V1' and
            saved['status'] == 'PASS_FINITE_FREE_TRACE_OBSERVER_NOT_ADMITTED', 'saved baseline status')
    require(saved['binding']['source_sha256'] == FREE_EXPECTED['native_probe/free_trace_probe.py'],
            'saved baseline source binding')
    require(len(saved['cases']) == 3, 'saved baseline case count')
    matched = []
    for index, old in enumerate(saved['cases']):
        new = cases[index]
        inp = {name: new['inputs'][name] for name in ('N', 'k', 'E')}
        require(encode(inp) == encode(old['inputs']), 'paired input mismatch')
        require(new['setup'] == old['setup'], 'paired setup outputs')
        require(new['terminal_pair'][0] == old['probes']['trace'], 'paired V_E')
        for label in ('identity', 'antipodal'):
            require(new['readouts'][label]['dE'] == old['probes']['signed'][label]['joint_gcd'],
                    'paired signed return gcd')
            require(new['readouts'][label]['dE_class'] == old['probes']['signed'][label]['joint_class'],
                    'paired signed return class')
        matched.append({'case_index': index, 'inputs': inp, 'common_outputs_equal': True,
                        'historical_probes_with_extra_outputs_preserved': old['probes'],
                        'historical_costs': {category: saved['costs'][name]
                                             for category, name in old['route_names'].items()},
                        'scope': 'output equality and component invoices; unequal full interfaces'})
    return {'compressed_sha256': hashlib.sha256(compressed).hexdigest(), 'compressed_bytes': len(compressed),
            'raw_sha256': BASELINE_RAW_SHA, 'raw_bytes': len(raw), 'matched': matched,
            'unpaired_case_index': 3, 'new_scientific_execution_of_old_program': False,
            'equal_output_end_to_end_ratio_claimed': False}


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
        free, hbw = load_frozen()
        work = hbw.Work(binding)
        sys.path.insert(0, str(OLD))
        import native_relative_port as old
        work.old = old
        work.stage = 'native_source_admission'
        binding['reused_interfaces'] = old.source_check()
        calls_after_admission = len(old.CALLS)
        cases = [main_case(work, hbw, free, index, *values) for index, values in enumerate(GRID)]
        work.stage = 'read_saved_baseline_after_production_and_validation'
        comparison = compare_saved_baseline(cases)
        work.completed['saved_baseline_comparison'] = comparison
        work.stage = 'end_source_check'
        end_binding(binding)
        require(old.source_check() == binding['reused_interfaces'], 'native binding changed')
        routes = {name: route.export() for name, route in work.routes.items()}
        costs = {name: hbw.route_cost(route) for name, route in routes.items()}
        payload = {'schema': SCHEMA, 'status': 'PASS_FINITE_ADJACENT_TRACE_NOT_ADMITTED',
                   'binding': binding, 'cases': cases, 'routes': routes, 'wiring': work.wiring,
                   'costs': costs, 'all_native_records': old.CALLS,
                   'saved_baseline_comparison': comparison,
                   'native_catalog_calls_after_source_admission': calls_after_admission,
                   'scope': 'ordered modular observer; no raw Cell trajectory, rate or Shor closure claim'}
        work.stage = 'serialize_success'
        raw = hbw.encode(payload)
        compressed = gzip.compress(raw, mtime=0)
        write_new(OUT/'ADJACENT_TRACE_RESULTS.json.gz', compressed)
        summaries = []
        for case in cases:
            item = {key: case[key] for key in ('inputs', 'status', 'setup', 'terminal_pair',
                                              'expressions', 'readouts', 'validation')}
            item['costs'] = {category: costs[name] for category, name in case['route_names'].items()}
            summaries.append(item)
        summary = {'schema': SCHEMA, 'status': payload['status'], 'cases': summaries,
                   'source_sha256': binding['source_sha256'], 'plan_sha256': binding['plan_sha256'],
                   'raw_bytes': len(raw), 'raw_sha256': hashlib.sha256(raw).hexdigest(),
                   'gzip_bytes': len(compressed), 'gzip_sha256': hashlib.sha256(compressed).hexdigest(),
                   'total_cost': {key: sum(value[key] for value in costs.values()) for key in METRICS},
                   'category_totals': {category: {key: sum(costs[case['route_names'][category]][key]
                                                         for case in cases) for key in METRICS}
                                       for category in CATEGORIES},
                   'native_catalog_calls_after_source_admission': calls_after_admission,
                   'total_native_calls': len(old.CALLS), 'saved_baseline_comparison': comparison,
                   'cost_scope': 'all seven categories; validation separate, full interfaces differ'}
        write_new(OUT/'ADJACENT_TRACE_SUMMARY.json', hbw.encode(summary))
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
