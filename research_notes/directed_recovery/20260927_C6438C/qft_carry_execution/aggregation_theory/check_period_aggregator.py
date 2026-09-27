"""Eight declared same-native-word full-matrix comparisons, no ideal reference."""
from copy import deepcopy
from pathlib import Path
from fractions import Fraction
from time import perf_counter
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'sep26-shor-general'
for directory in (ROOT.parent, ROOT.parent / 'modular_alias',
                  OLD / 'optimization/collision_analysis'):
    sys.path.insert(0, str(directory))
from period_aggregator import PeriodAggregator, certify_period, source_hashes
from carry_executor import CarryExecutor
from check_gram_sampler import load_bank, ExactCarrierCodec, LazyStreamingProgram
from typed_aliases import discover_aliases
from stage45.brc_loop_recheck import CALLS, verify_vendor


def packed(value):
    def encode(item):
        if isinstance(item, Fraction):
            return str(item)
        raise TypeError(type(item).__name__)
    return json.dumps(value, sort_keys=True, separators=(',', ':'), default=encode).encode()


def matrix_record(matrix):
    return {'rows': matrix.rows, 'den': matrix.den}


def main():
    first, started = len(CALLS), perf_counter()
    startup = json.loads((ROOT.parent / 'STARTUP_GUARD.json').read_bytes())
    assert startup['activity_allowed'] and startup['persistence_allowed'] and not startup['sync_debt_events']
    before = source_hashes()
    before['check_period_aggregator.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before['carry_executor.py'] == 'f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810'
    vendor = verify_vendor()
    bank, bank_source = load_bank()
    programs, cases, cycles, negatives = [], [], [], []
    baseline_evidence, aggregation_evidence, alias_evidence = [], [], []
    history = (1, 0, 1, 0)
    saved = None
    for N, a in ((21, 2), (65, 3)):
        program = LazyStreamingProgram(N, a, 4, bank, 61,
                    codec=ExactCarrierCodec(61, tuple(range(6))))
        programs.append(program)
        aggregator, baseline = PeriodAggregator(program, history), CarryExecutor(program, history)
        for depth in (3, 4):
            certificate = certify_period(program, depth, 16)
            assert certificate['status'] == 'CERTIFIED'
            cycles.append(certificate)
            R = certificate['R']
            targets = (certificate['states'][0], certificate['states'][1])
            aliases = discover_aliases(program, depth, targets, 3)
            alias_evidence.append(aliases)
            for r, target in enumerate(targets):
                call0, time0 = len(CALLS), perf_counter()
                actual = aggregator.gamma_known_period(depth, r, R, target=target,
                                                       period_certificate=certificate)
                actual_cost = {'native_core_calls': len(CALLS)-call0,
                               'elapsed_seconds': perf_counter()-time0}
                call0, time0 = len(CALLS), perf_counter()
                ds = aliases['aliases'][target]
                reference = baseline.sum_coefficients(depth, ds)
                reference_cost = {'native_core_calls': len(CALLS)-call0,
                                  'elapsed_seconds': perf_counter()-time0}
                assert actual == reference
                cases.append({'N': N, 'a': a, 'depth': depth, 'history': history[:depth],
                    'R_discovered': R, 'r': r, 'target': target, 'aliases': ds,
                    'matrix': matrix_record(actual), 'all_matrix_entries_equal': True,
                    'any_residual_row_or_column_entry': any(v for j, row in enumerate(actual.rows)
                        for k, v in enumerate(row) if j >= 2 or k >= 2),
                    'aggregation_cost': actual_cost, 'alias_sum_cost': reference_cost})
                print(json.dumps({'N': N, 'depth': depth, 'r': r, 'R': R,
                    'aliases': len(ds), 'full_matrix_equal': True,
                    'core_calls_so_far': len(CALLS)-first}), flush=True)
            if saved is None:
                saved = (aggregator, program, depth, R, certificate, targets)
        aggregation_evidence.append(aggregator.evidence())
        baseline_evidence.append(baseline.evidence())
    agg, program, depth, R, certificate, targets = saved
    bad = deepcopy(certificate)
    bad['states'] = list(bad['states'])
    bad['states'][-1] = 2
    partial = certify_period(program, depth, 1)
    assert partial['status'] == 'PARTIAL'
    controls = [
        ('boolean_period', depth, 0, True, targets[0], certificate),
        ('wrong_period_multiple', depth, 0, 2*R, targets[0], certificate),
        ('boolean_address', depth, True, R, targets[1], certificate),
        ('address_out_of_range', depth, R, R, targets[0], certificate),
        ('address_target_mismatch', depth, 0, R, targets[1], certificate),
        ('wrong_certificate_depth', depth-1, 0, R, targets[0], certificate),
        ('tampered_return_evidence', depth, 0, R, targets[0], bad),
        ('partial_period_not_admitted', depth, 0, R, targets[0], partial),
    ]
    for name, d, r, order, target, cert in controls:
        start = len(CALLS)
        try:
            agg.gamma_known_period(d, r, order, target=target, period_certificate=cert)
        except ValueError as error:
            negatives.append({'name': name, 'rejected': True, 'message': str(error),
                'actual_native_core_calls_delta': len(CALLS)-start,
                'failed_replay_evidence': getattr(error, 'evidence', None)})
        else:
            raise AssertionError('negative accepted: '+name)
    after = source_hashes()
    after['check_period_aggregator.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before == after
    payload = {'schema': 'NATIVE_WHOLE_PERIOD_AGGREGATION_BOUNDED_CHECK_V1',
        'status': 'AUTHOR_ACTUAL_NATIVE_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256': before, 'source_unchanged_during_run': True,
        'startup_guard': startup, 'vendor': vendor, 'bank_source': bank_source,
        'cases': cases, 'certified_cycles': cycles, 'partial_period_certificate': partial,
        'aggregation_evidence': aggregation_evidence,
        'baseline_evidence': baseline_evidence, 'alias_discovery_evidence': alias_evidence,
        'negative_controls': negatives,
        'programs': [{'N': p.N, 'a': p.a, 't': p.t, 'dim': p.dim,
            'full_dim': p.full_dim, 'phase_bindings': p.phase_bindings,
            'codec_binding': p.codec_binding, 'h4_binding': p.h4_binding,
            'modular_powers': p.modular_powers,
            'program_table_instances': p.lazy_factory.export_certificate(),
            'program_permutation_verifications': p.lazy_permutation_verifications} for p in programs],
        'actual_native_core_calls': len(CALLS)-first,
        'native_core_call_receipts': CALLS[first:],
        'elapsed_seconds': perf_counter()-started,
        'scope': 'Eight fixed D6 complete-matrix equalities after actual full61 word/codec admission; O(R) actual cycle discovery; no ideal propagation, no general cost improvement claim'}
    raw = packed(payload)
    path = ROOT / 'PERIOD_AGGREGATION_RESULTS.json.gz'
    path.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    assert gzip.decompress(path.read_bytes()) == raw
    summary = {'status': payload['status'], 'source_sha256': before,
        'payload_sha256': hashlib.sha256(raw).hexdigest(), 'payload_bytes': len(raw),
        'gzip_bytes': path.stat().st_size, 'actual_native_core_calls': len(CALLS)-first,
        'elapsed_seconds': payload['elapsed_seconds'], 'case_count': len(cases),
        'all_matrix_entries_equal': all(c['all_matrix_entries_equal'] for c in cases),
        'negative_controls_rejected': len(negatives),
        'cases': [{k: v for k, v in case.items() if k != 'matrix'} for case in cases],
        'aggregation_stats': [x['aggregation_stats'] for x in aggregation_evidence],
        'baseline_stats': [x['carry_stats'] for x in baseline_evidence],
        'scope': payload['scope']}
    (ROOT / 'PERIOD_AGGREGATION_SUMMARY.json').write_bytes(packed(summary))
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
