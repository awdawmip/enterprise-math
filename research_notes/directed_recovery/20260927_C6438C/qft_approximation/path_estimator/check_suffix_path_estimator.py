"""Exhaustive finite native-path variance identities, not approximate sampling."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import gzip
import hashlib
import json
import random
import sys

ROOT = Path(__file__).resolve().parent
RESEARCH = ROOT.parents[1] / 'sep27-qft-research'
sys.path.insert(0, str(RESEARCH / 'gram_research'))
from suffix_path_estimator import SuffixPathEstimator, draw_path_list
from check_single_walker import (load_bank, serializable, LazyStreamingProgram,
    SelectedStreamingProgram, ExactCarrierCodec, packed, CALLS, verify_vendor, PREVIOUS)
from stage80.fixed_phase import norm


def norm_rows(rows, helper, label):
    return helper.observe(label, ((F(v, row.den), F(v, row.den))
        for row in rows.values() for v in row.values if v))


def squared_error(rows, actual_state, actual_den, helper, label):
    terms = []
    for work, row in rows.items():
        target = actual_state.get((0, work, 0), (0,)*helper.dim)
        for x, y in zip(row.values, target):
            error = helper.observe('signed_estimation_error_coordinate',
                ((F(x, row.den),), (-F(y, actual_den),)))
            if error:
                terms.append((error, error))
    return helper.observe(label, terms)


def path_supports(program, prefix_state, k, paths):
    support, receipts = set(), []
    for path_index, path in enumerate(paths):
        for _, source, _ in prefix_state:
            target = source
            steps = []
            for offset, selected in enumerate(path):
                if selected:
                    following = program.tables[k+offset][target]
                    steps.append({'round': k+offset, 'input': target, 'output': following})
                    target = following
            support.add(target)
            receipts.append({'path_index': path_index, 'source': source, 'target': target, 'typed_steps': steps})
    return tuple(sorted(support)), receipts


def check_dimension(bank, use_codec):
    codec = ExactCarrierCodec(61, tuple(range(6))) if use_codec else None
    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=codec)
    actual = SelectedStreamingProgram(21, 2, 4, bank, 61, codec=codec)
    initial, initial_den = actual.initial()
    prefixes = {(): (initial, initial_den)}
    for _ in range(2):
        following = {}
        for history, (state, den) in prefixes.items():
            for bit, child in enumerate(actual.branches(state, den, history)):
                following[history+(bit,)] = child
        prefixes = following
    paths = tuple(product((0, 1), repeat=2))
    prefix_records, all_variances, all_m2_variances = [], [], []
    shared_tables = {}
    nonzero_residual = False
    observed = None
    total_pair_checks = 0
    for prefix_history, (prefix_state, prefix_den) in sorted(prefixes.items()):
        Mk = norm(prefix_state, prefix_den)
        assert Mk > 0
        support, support_proof = path_supports(program, prefix_state, 2, paths)
        targets = {prefix_history: (prefix_state, prefix_den)}
        for _ in range(2):
            following = {}
            for history, (state, den) in targets.items():
                for bit, child in enumerate(actual.branches(state, den, history)):
                    following[history+(bit,)] = child
            targets = following
        targets_record, prefix_variances, prefix_m2 = [], [], []
        for history, (state, den) in sorted(targets.items()):
            Mh = norm(state, den)
            assert {key[1] for key in state} <= set(support)
            estimator = SuffixPathEstimator(program, prefix_state, prefix_den, prefix_history, history, paths)
            helper = estimator.helper
            observed = helper
            path_vectors = [{work: estimator.point_path(j, work) for work in support} for j in range(4)]
            for vector in path_vectors:
                assert norm_rows(vector, helper, 'native_path_full_norm') == Mk
            mean = {work: estimator.point_mean(work) for work in support}
            for work, row in mean.items():
                target = state.get((0, work, 0), (0,)*program.dim)
                assert tuple(F(x, row.den) for x in row.values) == tuple(F(x, den) for x in target)
                nonzero_residual |= any(row.values[j] for j in range(2, program.dim))
            errors = [squared_error(vector, state, den, helper, 'native_path_error_norm') for vector in path_vectors]
            variance = helper.observe('uniform_native_path_variance', ((F(1, 4), value) for value in errors))
            expected_variance = helper.observe('raw_mass_variance_identity', ((Mk,), (-Mh,)))
            assert variance == expected_variance
            pairs, pair_errors = [], []
            for left in range(4):
                for right in range(4):
                    pair = SuffixPathEstimator(program, prefix_state, prefix_den, prefix_history,
                        history, (paths[left], paths[right]))
                    pair_mean = {work: pair.point_mean(work) for work in support}
                    error = squared_error(pair_mean, state, den, pair.helper, 'two_path_mean_error_norm')
                    pair_errors.append(error)
                    pairs.append({'indices': (left, right), 'squared_error': error,
                                  'estimator': pair.evidence(include_shared_bindings=False)})
                    for table in pair.helper.tables:
                        # Equal permutation certificates can belong to distinct
                        # actual caches. Preserve each instance's columns/cost.
                        shared_tables[id(table)] = table
                    total_pair_checks += 1
            m2_error = helper.observe('all_ordered_iid_two_path_means', ((F(1, 16), value) for value in pair_errors))
            assert m2_error == variance/2
            prefix_variances.append(variance)
            prefix_m2.append(m2_error)
            for table in estimator.helper.tables:
                shared_tables[id(table)] = table
            targets_record.append({'target_history': history, 'raw_target_mass': Mh,
                'raw_prefix_mass': Mk, 'all_point_mean_rows_equal_actual': True,
                'every_native_path_norm_equals_prefix_mass': True,
                'path_squared_errors': errors, 'path_variance': variance,
                'variance_identity': expected_variance, 'm2_mean_squared_error': m2_error,
                'm2_equals_variance_over_2': True,
                'estimator': estimator.evidence(include_shared_bindings=False), 'all_ordered_pairs': pairs})
        aggregate = observed.observe('fixed_raw_prefix_suffix_variance_sum', ((v,) for v in prefix_variances))
        assert aggregate == 3*Mk
        aggregate_m2 = observed.observe('fixed_raw_prefix_m2_variance_sum', ((v,) for v in prefix_m2))
        assert aggregate_m2 == F(3, 2)*Mk
        all_variances.append(aggregate)
        all_m2_variances.append(aggregate_m2)
        prefix_records.append({'prefix_history': prefix_history, 'raw_prefix_mass': Mk,
            'raw_prefix_denominator': prefix_den, 'raw_prefix_state': sorted(prefix_state.items()),
            'enumerated_union_support': support, 'typed_path_support_receipts': support_proof,
            'sum_over_its_four_suffix_histories': aggregate,
            'sum_over_its_four_suffix_m2_errors': aggregate_m2,
            'prefix_aggregation_operations': list(observed.observer.operations[-2:]),
            'targets': targets_record})
        print(json.dumps({'dim': program.dim, 'prefix': prefix_history,
                          'mass': str(Mk), 'variance_sum': str(aggregate)}), flush=True)
    total = observed.observe('all_raw_prefixes_variance_sum', ((v,) for v in all_variances))
    total_m2 = observed.observe('all_raw_prefixes_m2_variance_sum', ((v,) for v in all_m2_variances))
    assert total == 3 and total_m2 == F(3, 2)
    assert nonzero_residual
    table_metrics = [table.report_metrics() for table in shared_tables.values()]
    estimator_reports = [record['estimator']['report']
        for prefix in prefix_records for target in prefix['targets']
        for record in [target, *target['all_ordered_pairs']]]
    resources = {
        'distinct_actual_modular_table_instances': len(table_metrics),
        'computed_columns_across_distinct_instances': sum(row['computed_columns'] for row in table_metrics),
        'actual_adder_digit_replays': sum(row['setup_adder_digit_replays']+row['column_adder_digit_replays'] for row in table_metrics),
        'actual_host_bit_wiring_operations': sum(row['setup_host_bit_wiring_operations']+row['column_host_bit_wiring_operations'] for row in table_metrics),
        'point_path_requests': sum(row['point_path_requests'] for row in estimator_reports),
        'point_mean_requests': sum(row['point_mean_requests'] for row in estimator_reports),
        'native_phase_vector_applications': sum(row['helper']['native_phase_vector_applications'] for row in estimator_reports),
        'positive_path_observer_calls': sum(row['helper']['actual_positive_path_observations'] for row in estimator_reports)+2*len(prefix_records)+2,
        'max_path_denominator_bits': max(row['max_path_denominator_bits'] for row in estimator_reports),
        'max_mean_denominator_bits': max(row['max_mean_denominator_bits'] for row in estimator_reports),
        'scope': 'estimator fixture including union-support validation; shared table instances counted once; comparator and bank admission separate'}
    return {'N': 21, 'a': 2, 't': 4, 'k': 2, 'ell': 2, 'dimension': program.dim,
        'complete_raw_prefixes': len(prefix_records), 'target_histories': 16,
        'paths_per_target': 4, 'ordered_m2_pairs_checked': total_pair_checks,
        'total_path_variance_across_all_raw_histories': total,
        'total_m2_error_across_all_raw_histories': total_m2,
        'global_aggregation_operations': list(observed.observer.operations[-2:]),
        'nonzero_residual_retained': nonzero_residual,
        'estimator_fixture_resources': resources,
        'prefix_records': prefix_records,
        'shared_native_bindings': {'phase_bindings': program.phase_bindings,
            'codec_binding': program.codec_binding, 'native_two_H4_binding': program.h4_binding},
        'shared_typed_modular_certificates': [table.export_certificate() for table in shared_tables.values()],
        'actual_state_preparation_metrics': actual.report_metrics(),
        'query_cost_scope': 'full prefix input construction separately charged; typed tables shared across exhaustive fixture'}


class ExhaustedSource:
    def randrange(self, stop):
        raise StopIteration


def interface_checks(bank):
    program = LazyStreamingProgram(21, 2, 4, bank, 61,
                                  codec=ExactCarrierCodec(61, tuple(range(6))))
    initial, den = program.initial()
    # This fixed software fixture checks list construction/consistency only;
    # no empirical iid or variance conclusion is inferred from its one seed.
    receipt = draw_path_list((), (1, 0), 3, random.Random(927081))
    estimator = SuffixPathEstimator(program, initial, den, (), (1, 0), receipt['paths'], construction_receipt=receipt)
    before = estimator.function_sha256
    first = estimator.point_mean(1)
    estimator.point_mean(4)
    repeated = estimator.point_mean(1)
    assert first == repeated and estimator.function_sha256 == before
    assert receipt['requested_sample_count'] == 3 and len(receipt['drawn_bits']) == 6
    exhausted = draw_path_list((), (1, 0), 2, ExhaustedSource())
    assert exhausted['status'] == 'INCOMPLETE_PATH_RANDOM_SOURCE' and not exhausted['estimator_ready']
    rejected = []
    for name, action in (
        ('incomplete_construction_receipt', lambda: SuffixPathEstimator(program, initial, den, (),
            (1, 0), ((0, 0),), construction_receipt=exhausted)),
        ('path_length_mismatch', lambda: SuffixPathEstimator(program, initial, den, (), (1, 0), ((0,),))),
        ('target_not_extending_prefix', lambda: draw_path_list((1,), (0, 0), 2, random.Random(1))),
        ('boolean_path_bit', lambda: SuffixPathEstimator(program, initial, den, (), (1, 0), ((True, 0),))),
        ('outside_carrier_query', lambda: estimator.point_mean(32))):
        try:
            action()
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('invalid fixed-function input accepted: '+name)
    empty_suffix = SuffixPathEstimator(program, initial, den, (), (), ((), ()))
    empty_row = empty_suffix.point_mean(1)
    assert F(empty_row.values[0], empty_row.den) == 1
    return {'fixed_list_query_order_independent': True, 'non_power_of_two_sample_count': 3,
        'construction_receipt': receipt, 'estimator': estimator.evidence(),
        'exhausted_source': exhausted, 'negative_controls_rejected': rejected,
        'empty_suffix_exact_identity': True}


def main():
    files = [Path(__file__), ROOT / 'suffix_path_estimator.py',
        RESEARCH / 'gram_research/single_walker.py',
        PREVIOUS / 'optimization/streaming/lazy_streaming.py',
        PREVIOUS / 'optimization/lazy_modular/lazy_modular.py',
        PREVIOUS / 'optimization/carrier_codec/carrier_codec.py',
        PREVIOUS / 'new_word_compiler/certified_word_compiler.py']
    sources = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    first = len(CALLS)
    kernel = verify_vendor()
    bank, source_bank = load_bank()
    cases = [check_dimension(bank, codec) for codec in (True, False)]
    for left, right in zip(cases[0]['prefix_records'], cases[1]['prefix_records']):
        assert left['raw_prefix_mass'] == right['raw_prefix_mass']
        for lhs, rhs in zip(left['targets'], right['targets']):
            assert lhs['path_squared_errors'] == rhs['path_squared_errors']
            assert lhs['m2_mean_squared_error'] == rhs['m2_mean_squared_error']
    controls = interface_checks(bank)
    assert sources == {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in files}
    result = {'status': 'AUTHOR_ACTUAL_NATIVE_PATH_VARIANCE_SHARED_CONTEXT_NOT_ADMITTED',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'source_control': '671530e485921a9eeed91c1635decd60cc195dc3',
        'kernel': kernel, 'source_bank': source_bank, 'source_sha256': sources,
        'dependency_sources_unchanged_during_execution': True,
        'cases': cases, 'full61_and_codec6_variance_observations_equal': True,
        'interface_checks': controls, 'actual_BRC_core_calls': len(CALLS)-first,
        'actual_BRC_core_receipts': CALLS[first:], 'new_ideal_reference_run': False,
        'order_or_factors_supplied': False, 'approximate_sampler_executed': False,
        'claim': 'exact iid-path L2 variance identities; neither a TV lower bound nor a general sampling no-go'}
    raw = packed(serializable(result))
    target = ROOT / 'SUFFIX_PATH_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {key: result[key] for key in ('status', 'activity', 'source_control', 'source_bank',
        'source_sha256', 'dependency_sources_unchanged_during_execution',
        'full61_and_codec6_variance_observations_equal', 'actual_BRC_core_calls',
        'new_ideal_reference_run', 'order_or_factors_supplied', 'approximate_sampler_executed', 'claim')}
    summary['cases'] = [{key: case[key] for key in ('N', 'a', 't', 'k', 'ell', 'dimension',
        'complete_raw_prefixes', 'target_histories', 'paths_per_target', 'ordered_m2_pairs_checked',
        'total_path_variance_across_all_raw_histories', 'total_m2_error_across_all_raw_histories',
        'nonzero_residual_retained', 'estimator_fixture_resources')} | {'prefixes': [
            {key: item[key] for key in ('prefix_history', 'raw_prefix_mass',
                'sum_over_its_four_suffix_histories', 'sum_over_its_four_suffix_m2_errors')}
            for item in case['prefix_records']]} for case in cases]
    summary['interface_checks'] = {key: controls[key] for key in ('fixed_list_query_order_independent',
        'non_power_of_two_sample_count', 'negative_controls_rejected', 'empty_suffix_exact_identity')}
    summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
    summary['gzip_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT / 'SUFFIX_PATH_SUMMARY.json').write_text(
        json.dumps(json.loads(packed(serializable(summary))), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'calls': result['actual_BRC_core_calls'],
        'payload_sha256': summary['payload_sha256']}), flush=True)


if __name__ == '__main__':
    main()
