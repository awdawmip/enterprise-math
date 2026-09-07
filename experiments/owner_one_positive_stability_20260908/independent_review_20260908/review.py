"""Independent finite oracles and transformations for the one-positive consumer.

Run with Python 3.12: python -B review.py [repository-root]
Only adjacent review.json is written. The author's fixed12 build is not called.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('repo', nargs='?', type=Path, default=Path(__file__).resolve().parents[3])
ROOT = parser.parse_args().repo.resolve()
OUT = Path(__file__).resolve().parent
UNIT = ROOT.joinpath('experiments/owner_one_positive_stability_20260908')
if not __debug__:
    raise RuntimeError('Normal assertions are required; do not use -O.')
INPUT_PINS = {
    'check_one_positive_stability.py': '283c0b64e995077d01e5b42114ffd5791bafadeb5f175b4df17118ee1a9d5878',
    'certificate.json': '11fd30fcc2894ffdcd7ed43e1266b65dc063aa12b57f9f5b653eb9d437bc3010',
    'README.md': '91f4c918eead64e0efb32f24577c9e4db081412131ccf4b22313a0ae96e4d820',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frozen_inputs():
    actual = {name: sha(UNIT.joinpath(name).read_bytes()) for name in INPUT_PINS}
    assert actual == INPUT_PINS, 'frozen consumer input drift'
    return actual


before = frozen_inputs()
sys.path.insert(0, str(UNIT))
import check_one_positive_stability as consumer
source_pins = consumer.verify_sources()
author = json.loads(UNIT.joinpath('certificate.json').read_text(encoding='utf-8'))
assert author['checker_sha256'] == INPUT_PINS['check_one_positive_stability.py']
assert author['source_sha256'] == source_pins
assert len(author['cases']) == 12
assert author['main_ledger_call_audit']['limitation'] == 'runtime call boundary plus reviewed selected source, not a transitive static certificate'
AXES = tuple(combinations(range(6), 3))
assert len(AXES) == 20 and set(consumer.SLICES) == set(AXES)


def positive_totals(atoms):
    totals = Counter()
    for cell, weight in atoms:
        totals[cell.coords] += weight
    return dict(totals)


def projection(totals, axes):
    # Independent aggregation, with no call to the consumer's projection helper.
    addresses = {tuple(coords[a] for a in axes) for coords in totals}
    return {address: sum(mass for coords, mass in totals.items()
                         if tuple(coords[a] for a in axes) == address)
            for address in addresses}


def table_oracle(mu, nu):
    left, right = positive_totals(mu), positive_totals(nu)
    cells = set(left) | set(right)
    positive = {coords: left.get(coords, 0) - right.get(coords, 0)
                for coords in cells if left.get(coords, 0) > right.get(coords, 0)}
    negative = {coords: right.get(coords, 0) - left.get(coords, 0)
                for coords in cells if right.get(coords, 0) > left.get(coords, 0)}
    P, N = sum(positive.values()), sum(negative.values())
    table_norms, raw = {}, {}
    for axes in AXES:
        pos, neg = projection(positive, axes), projection(negative, axes)
        overlap = sum(min(pos.get(address, 0), neg.get(address, 0))
                      for address in set(pos) | set(neg))
        # Jordan positive/negative mass minus twice their projected overlap.
        # This does not use |P-N+a_I|+a_I or distinguish-count lower bounds.
        table_norms[axes] = P + N - 2 * overlap
        raw[axes] = (projection(left, axes), projection(right, axes))
    difference = {coords: left.get(coords, 0) - right.get(coords, 0)
                  for coords in cells if left.get(coords, 0) != right.get(coords, 0)}
    return {'left': left, 'right': right, 'positive': positive, 'negative': negative,
            'difference': difference, 'P': P, 'N': N, 'norm': P + N,
            'table_norms': table_norms, 'raw': raw}


def div_node(value, numerator, denominator):
    assert value == {'node': 'DIV', 'numerator': numerator,
                     'denominator': denominator, 'state': 'UNEVALUATED'}
    assert type(value['numerator']) is int and type(value['denominator']) is int


results = []


def checked_case(name, mu, nu, denominator=1):
    oracle = table_oracle(mu, nu)
    result = consumer.audit_case(name, mu, nu, denominator)
    assert result['p'] == len(oracle['positive'])
    assert result['P_numerator'] == oracle['P'] and result['N_numerator'] == oracle['N']
    assert result['l1_numerator'] == oracle['norm']
    assert result['D_numerator'] == sum(oracle['table_norms'].values())
    assert {tuple(row['coords']): row['numerator'] for row in result['aggregated_signed_difference']} == oracle['difference']
    for side, atoms in [('mu', mu), ('nu', nu)]:
        assert result['positive_populations'][side] == [
            {'input_index': i, 'coords': list(cell.coords), 'positive_weight_numerator': weight}
            for i, (cell, weight) in enumerate(atoms)]
    expected_cancel = {coords: min(oracle['left'][coords], oracle['right'][coords])
                       for coords in set(oracle['left']) & set(oracle['right'])}
    assert {tuple(row['coords']): row['cancelled_numerator'] for row in result['cell_cancellations']} == expected_cancel
    tables = {tuple(table['axes']): table for table in result['raw_tables']}
    assert len(result['raw_tables']) == 20 and set(tables) == set(AXES)
    for axes, table in tables.items():
        assert table['l1_numerator'] == oracle['table_norms'][axes]
        left, right = oracle['raw'][axes]
        rows = {tuple(row['raw_address']): row for row in table['rows']}
        assert len(rows) == len(table['rows']) and set(rows) == set(left) | set(right)
        for address, row in rows.items():
            assert row['mu_numerator'] == left.get(address, 0)
            assert row['nu_numerator'] == right.get(address, 0)
            assert row['signed_difference_numerator'] == left.get(address, 0) - right.get(address, 0)
            assert tuple(value + row['common_offset'] for value in row['joint_can3_address']) == address
            assert min(row['joint_can3_address']) == 0
        assert table['missing_addresses_are_zero'] and table['joint_roundtrip_verified']
    norm, D = oracle['norm'], sum(oracle['table_norms'].values())
    div_node(result['common_mass_unit'], 1, denominator)
    div_node(result['l1_mass'], norm, denominator)
    div_node(result['D_mass'], D, denominator)
    div_node(result['general_bound']['constant'], 3, 20)
    div_node(result['equal_mass_bound']['constant'], 1, 10)
    if norm:
        div_node(result['ratio'], norm, D)
    else:
        assert result['ratio'] is None and result['zero_equality_status'] == 'TRIVIAL_ZERO'
    payload_digest = sha(json.dumps(result, sort_keys=True, separators=(',', ':')).encode())
    norms = [oracle['table_norms'][axes] for axes in AXES]
    results.append({'case': name, 'p': result['p'], 'norm_bit_length': norm.bit_length(),
                    'l1_numerator': norm if norm.bit_length() <= 128 else {'hex': hex(norm)},
                    'D_numerator': D if D.bit_length() <= 128 else {'hex': hex(D)},
                    'denominator_bit_length': denominator.bit_length(),
                    'equal_mass': result['equal_mass_bound']['applicable'],
                    'general_sharp': result['general_bound']['nonzero_sharp_equality'],
                    'equal_mass_sharp': result['equal_mass_bound']['nonzero_sharp_equality'],
                    'twenty_raw_tables_and_jordan_overlap_oracle': 'PASS',
                    'table_l1_values': norms if norm.bit_length() <= 128 else None,
                    'table_l1_sha256': sha(json.dumps(norms, separators=(',', ':')).encode()),
                    'full_consumer_output_sha256': payload_digest})
    return result


def cell(coords):
    return consumer.x6.Spatial6(tuple(coords))


q = cell((4, -7, 2, 9, -3, 6))


def offset(axis, amount):
    coords = list(q.coords)
    coords[axis] += amount
    return cell(coords)


balanced_nu = [(offset(0, -2), 2), (offset(0, 5), 7), (offset(1, -3), 9),
               (offset(2, 1), 4), (offset(2, -7), 5), (offset(3, 6), 9),
               (offset(4, -4), 9), (offset(5, 2), 1), (offset(5, 8), 3), (offset(5, -9), 5)]
balanced_mu = [(q, 12), (q, 15)]
selected_calls = Counter()
forbidden_calls = Counter()
allowed_exact = {'division', 'compare_divisions', '__init__', '__post_init__', '_require_natural', '_require_positive'}
allowed_signed = {'support_size', 'shortest_event_count', 'spatial_norm_squared', '_z6', '<genexpr>'}


def observe(frame, event, arg):
    if event == 'call':
        module = frame.f_globals.get('__name__', '')
        name = frame.f_code.co_name
        key = module + '.' + name
        if module == 'fractions':
            forbidden_calls[key] += 1
        if module.startswith('enterprise_math.') and (module != consumer.exact.__name__ or name not in allowed_exact):
            forbidden_calls[key] += 1
        if module == consumer.signed_brc.__name__ and name not in allowed_signed:
            forbidden_calls[key] += 1
        if module == consumer.x6.__name__ and name in {'positive_path_multiplicity', 'relative_endpoint_multiplicity'}:
            forbidden_calls[key] += 1
        if module in {consumer.exact.__name__, consumer.signed_brc.__name__, consumer.x6.__name__}:
            selected_calls[key] += 1
    elif event == 'c_call':
        key = (getattr(arg, '__module__', ''), getattr(arg, '__name__', ''))
        if key in {('builtins', 'divmod'), ('math', 'sqrt'), ('math', 'isqrt')}:
            forbidden_calls['.'.join(key)] += 1


assert sys.getprofile() is None
original_decimal_limit = sys.get_int_max_str_digits()
sys.setprofile(observe)
try:
    general = checked_case('balanced_axis_aggregate_split_locations', balanced_mu, balanced_nu, 17)
    assert general['axis_negative_masses'] == [9] * 6
    assert (general['l1_numerator'], general['D_numerator']) == (81, 540)
    assert general['general_bound']['nonzero_sharp_equality']

    unbalanced_nu = list(balanced_nu)
    unbalanced_nu[0] = (unbalanced_nu[0][0], 1)
    unbalanced_nu[2] = (unbalanced_nu[2][0], 10)
    unbalanced = checked_case('N_equals_2P_but_unequal_axis_aggregates', balanced_mu, unbalanced_nu, 17)
    assert unbalanced['axis_negative_masses'] == [8, 10, 9, 9, 9, 9]
    assert (unbalanced['l1_numerator'], unbalanced['D_numerator']) == (81, 552)
    assert not unbalanced['general_bound']['nonzero_sharp_equality']

    equal_nu = [(offset(0, -5), 2), (offset(0, 8), 3), (offset(1, 2), 7),
                (offset(3, -4), 11), (offset(4, 3), 13), (offset(5, -6), 17)]
    equal = checked_case('equal_mass_unequal_axis_and_location_weights', [(q, 20), (q, 33)], equal_nu, 29)
    assert equal['axis_negative_masses'] == [5, 7, 0, 11, 13, 17]
    assert (equal['l1_numerator'], equal['D_numerator']) == (106, 1060)
    assert equal['equal_mass_bound']['nonzero_sharp_equality']
    assert not equal['general_bound']['nonzero_sharp_equality']

    background = [(q, 11), (balanced_nu[0][0], 7), (cell((-11, 13, 4, -8, 19, -2)), 20),
                  (cell((-11, 13, 4, -8, 19, -2)), 3)]
    cancelled = checked_case('common_population_added_to_both_sides', balanced_mu + background, balanced_nu + background, 17)
    assert cancelled['aggregated_signed_difference'] == general['aggregated_signed_difference']
    assert [t['l1_numerator'] for t in cancelled['raw_tables']] == [t['l1_numerator'] for t in general['raw_tables']]

    shift = (-101, 37, -11, 0, 25, -8)
    translate = lambda atoms: [(cell(tuple(a + b for a, b in zip(z.coords, shift))), weight) for z, weight in atoms]
    translated = checked_case('signed_common_translation', translate(balanced_mu), translate(balanced_nu), 17)
    assert [t['l1_numerator'] for t in translated['raw_tables']] == [t['l1_numerator'] for t in general['raw_tables']]
    assert translated['D_numerator'] == general['D_numerator']

    perm = (5, 2, 0, 4, 1, 3)
    permute = lambda atoms: [(cell(tuple(z.coords[a] for a in perm)), weight) for z, weight in atoms]
    permuted = checked_case('labelled_axis_permutation', permute(balanced_mu), permute(unbalanced_nu), 17)
    original_norms = {tuple(t['axes']): t['l1_numerator'] for t in unbalanced['raw_tables']}
    for table in permuted['raw_tables']:
        assert table['l1_numerator'] == original_norms[tuple(sorted(perm[a] for a in table['axes']))]
    assert permuted['D_numerator'] == unbalanced['D_numerator']

    scale = (1 << 2053) + 113
    denominator = scale * 1009
    large = checked_case('large_unreduced_symbolic_common_factor', [(z, weight * scale) for z, weight in balanced_mu],
                         [(z, weight * scale) for z, weight in balanced_nu], denominator)
    div_node(large['ratio'], 81 * scale, 540 * scale)
    div_node(large['l1_mass'], 81 * scale, 1009 * scale)
    assert large['general_bound']['nonzero_sharp_equality']
    assert denominator.bit_length() > 2000

    a, b = offset(0, 3), offset(4, -5)
    zero = checked_case('zero_after_duplicate_multi_cell_cancellation', [(q, 2), (q, 3), (a, 5)],
                        [(q, 5), (a, 1), (a, 4)], 31)
    assert zero['p'] == 0 and zero['difference_kind'] == 'ZERO_DIFFERENCE'
    assert not zero['general_bound']['nonzero_sharp_equality'] and not zero['equal_mass_bound']['nonzero_sharp_equality']
    nonpositive = checked_case('nonpositive_after_overcancellation', [(q, 4), (a, 2)],
                               [(q, 9), (a, 2), (b, 7)], 37)
    assert nonpositive['p'] == 0 and (nonpositive['l1_numerator'], nonpositive['D_numerator']) == (12, 240)
    assert nonpositive['difference_kind'] == 'NONPOSITIVE_NONZERO'

    off_axis_coords = list(q.coords)
    off_axis_coords[1] += 2
    off_axis_coords[2] -= 3
    off_axis = cell(off_axis_coords)
    one = checked_case('positive_support_count_after_exact_cancellation', [(q, 8), (a, 5)],
                       [(a, 5), (off_axis, 2)], 41)
    assert one['p'] == 1 and (one['l1_numerator'], one['D_numerator']) == (10, 184)
    assert one['negative_sites'][0]['distinguishing_tables'] == 16
    try:
        consumer.audit_case('positive_support_after_partial_cancellation_reject', [(q, 8), (a, 5)],
                            [(a, 4), (off_axis, 2)], 41)
    except ValueError as error:
        rejection = {'case': 'one_residual_unit_creates_second_positive_site', 'status': 'REJECTED', 'reason': str(error)}
        assert 'p(f)<=1' in str(error)
    else:
        raise AssertionError('two positive sites after cancellation were accepted')
finally:
    sys.setprofile(None)

assert not forbidden_calls, dict(forbidden_calls)
assert selected_calls['enterprise_math.exact_arithmetic.division'] > 0
assert selected_calls['enterprise_math.exact_arithmetic.compare_divisions'] > 0
assert selected_calls['signed_brc.support_size'] > 0
assert selected_calls['x6_signed.from_hidden_slice_coordinates'] > 0
assert sys.get_int_max_str_digits() == original_decimal_limit
assert frozen_inputs() == before and consumer.verify_sources() == source_pins
assert len(results) == 10
report = {
    'schema': 'owner_one_positive_consumer_independent_review_v1',
    'status': 'PASS_BOUNDED_INDEPENDENT_CONSUMER_REVIEW',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'input_sha256': before, 'source_sha256': source_pins,
    'executed_review_script_sha256': sha(Path(__file__).read_bytes()),
    'execution_receipt': {'python': sys.version.split()[0], 'argv': sys.argv,
                          'assertions_enabled': __debug__, 'cases': 10, 'raw_tables_checked': 200,
                          'input_rejections': 1, 'author_fixed_build_called': False,
                          'author_static_gate_rerun': False, 'negative_callguard_probes_rerun': False},
    'oracle': 'Independently aggregate Jordan positive/negative masses; each raw L1 is P+N minus twice projected overlap. Also compare all original mu/nu rows and joint-address reconstruction.',
    'cases': results, 'post_cancellation_rejection': rejection,
    'limited_runtime_observation': {'scope': 'Only this finite review after canonical imports; selected Python/C call observation and reviewed source, not transitive static compliance.',
                                    'forbidden_observed_calls': dict(forbidden_calls),
                                    'selected_call_counts': dict(sorted(selected_calls.items())),
                                    'module_initialization': 'OUTSIDE_OBSERVATION_NOT_RECLASSIFIED',
                                    'no_quotient_or_root_readout_requested': True,
                                    'interpreter_decimal_limit_unchanged': original_decimal_limit},
    'boundaries': ['Shared external anchor and labelled frame remain caller premises.',
                   'Analytical signed mass differences do not create negative BRC primitives.',
                   'No general p<=7 claim, branch history recovery, new mathematical proof or formal task/review/promotion authority.',
                   'All author source and evidence bytes remain unchanged; only this independent package is written.'],
    'global_knowledge_sync': 'main@990d7c1 / GLOBAL_KNOWLEDGE_V1'
}
output = OUT.joinpath('review.json')
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'status': report['status'], 'cases': len(results), 'raw_tables_checked': 200,
                  'post_cancellation_rejection': rejection['status'], 'source_pins': len(source_pins),
                  'script_sha256': report['executed_review_script_sha256'],
                  'output_sha256': sha(output.read_bytes())}))
