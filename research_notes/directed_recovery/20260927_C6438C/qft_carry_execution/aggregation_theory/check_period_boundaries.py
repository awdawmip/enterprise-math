"""Separate bounded branch coverage; prior eight-case evidence stays untouched."""
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json

from check_period_aggregator import (ROOT, packed, matrix_record, load_bank, ExactCarrierCodec,
                                    LazyStreamingProgram, discover_aliases, CALLS, verify_vendor)
from period_aggregator import PeriodAggregator, certify_period, source_hashes
from carry_executor import CarryExecutor


def main():
    first, start_time = len(CALLS), perf_counter()
    startup = json.loads((ROOT.parent / 'STARTUP_GUARD.json').read_bytes())
    assert startup['activity_allowed'] and startup['persistence_allowed'] and not startup['sync_debt_events']
    before = source_hashes()
    before['check_period_boundaries.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before['period_aggregator.py'] == '6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c'
    vendor = verify_vendor()
    bank, bank_source = load_bank()
    cases, inputs = [], []
    coverage = {k: False for k in ('q_one_nonempty_high', 's_equals_depth', 's_above_depth',
                                  'large_two_part_negative_displacement', 'large_two_part_empty_alias')}
    for N, a, depth, history in ((17, 4, 3, (0, 0, 1, 0)),
                                 (17, 3, 3, (1, 0, 1, 0)),
                                 (97, 5, 2, (1, 0, 1, 0))):
        program = LazyStreamingProgram(N, a, 4, bank, 61,
                    codec=ExactCarrierCodec(61, tuple(range(6))))
        certificate = certify_period(program, depth, N)
        assert certificate['status'] == 'CERTIFIED'
        R = certificate['R']
        s, q = 0, R
        while not q & 1:
            q >>= 1
            s += 1
        addresses = sorted(set((0, 1, R-1)))
        addresses = [r for r in addresses if 0 <= r < R]
        if s > depth:
            addresses = sorted(set((*addresses, R >> 1)))
        targets = tuple(certificate['states'][r] for r in addresses)
        aliases = discover_aliases(program, depth, targets, min(3, 1 << depth))
        aggregator, baseline = PeriodAggregator(program, history), CarryExecutor(program, history)
        for r, target in zip(addresses, targets):
            first_query = len(CALLS)
            actual = aggregator.gamma_known_period(depth, r, R, target=target,
                                                   period_certificate=certificate)
            aggregate_calls = len(CALLS)-first_query
            first_query = len(CALLS)
            ds = aliases['aliases'][target]
            reference = baseline.sum_coefficients(depth, ds)
            baseline_calls = len(CALLS)-first_query
            assert actual == reference
            coverage['q_one_nonempty_high'] |= q == 1 and s < depth
            coverage['s_equals_depth'] |= s == depth
            coverage['s_above_depth'] |= s > depth
            coverage['large_two_part_negative_displacement'] |= s > depth and any(d < 0 for d in ds)
            coverage['large_two_part_empty_alias'] |= s > depth and not ds
            cases.append({'N': N, 'a': a, 'depth': depth, 'history': history[:depth],
                'R_discovered': R, 's': s, 'q': q, 'r': r, 'target': target,
                'aliases': ds, 'matrix': matrix_record(actual), 'all_matrix_entries_equal': True,
                'zero_matrix': not any(v for row in actual.rows for v in row),
                'residual_row_or_column_nonzero': any(v for j, row in enumerate(actual.rows)
                    for k, v in enumerate(row) if j >= 2 or k >= 2),
                'aggregation_core_calls': aggregate_calls, 'baseline_core_calls': baseline_calls})
            print(json.dumps({'N': N, 'R': R, 's': s, 'depth': depth, 'r': r,
                'aliases': ds, 'all_matrix_entries_equal': True,
                'actual_core_calls_so_far': len(CALLS)-first}), flush=True)
        inputs.append({'N': N, 'a': a, 't': 4, 'depth': depth, 'history': history,
            'phase_bindings': program.phase_bindings, 'codec_binding': program.codec_binding,
            'h4_binding': program.h4_binding, 'modular_powers': program.modular_powers,
            'program_table_instances': program.lazy_factory.export_certificate(),
            'program_permutation_verifications': program.lazy_permutation_verifications,
            'period_certificate': certificate, 'alias_discovery': aliases,
            'aggregation_evidence': aggregator.evidence(), 'baseline_evidence': baseline.evidence()})
    after = source_hashes()
    after['check_period_boundaries.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before == after
    payload = {'schema': 'NATIVE_PERIOD_AGGREGATION_BOUNDARY_CHECK_V1',
        'status': 'AUTHOR_ACTUAL_NATIVE_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256': before, 'source_unchanged_during_run': True,
        'startup_guard': startup, 'vendor': vendor, 'bank_source': bank_source,
        'inputs': inputs, 'cases': cases, 'observed_branch_coverage': coverage,
        'all_requested_branches_observed': all(coverage.values()),
        'actual_native_core_calls': len(CALLS)-first, 'native_core_call_receipts': CALLS[first:],
        'elapsed_seconds': perf_counter()-start_time,
        'scope': 'Independent positive boundary run; first-return cycles are actual O(R) typed discovery; no ideal reference or supplied-order assumption'}
    raw = packed(payload)
    artifact = ROOT / 'PERIOD_BOUNDARY_RESULTS.json.gz'
    artifact.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    assert gzip.decompress(artifact.read_bytes()) == raw
    summary = {'status': payload['status'], 'source_sha256': before,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'payload_bytes': len(raw),
        'gzip_bytes': artifact.stat().st_size, 'actual_native_core_calls': len(CALLS)-first,
        'elapsed_seconds': payload['elapsed_seconds'], 'case_count': len(cases),
        'all_matrix_entries_equal': all(x['all_matrix_entries_equal'] for x in cases),
        'observed_branch_coverage': coverage, 'all_requested_branches_observed': all(coverage.values()),
        'cases': [{k: v for k, v in x.items() if k != 'matrix'} for x in cases],
        'aggregation_stats': [x['aggregation_evidence']['aggregation_stats'] for x in inputs],
        'native_phase_vector_applications': {
            'aggregation': [x['aggregation_evidence']['inherited_action_stats']['native_phase_vector_applications'] for x in inputs],
            'baseline': [x['baseline_evidence']['inherited_action_stats']['native_phase_vector_applications'] for x in inputs]}}
    (ROOT / 'PERIOD_BOUNDARY_SUMMARY.json').write_bytes(packed(summary))
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
