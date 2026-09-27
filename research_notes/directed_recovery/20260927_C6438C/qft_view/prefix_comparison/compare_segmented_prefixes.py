"""Source-pinned matched experiment candidate; no execution until authorized.

One actual SO bank is shared. Fresh Gram caches and warmed modular tables are
the measured condition; complete native propagation and receipts are retained.
"""
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
from uuid import uuid4
import gzip
import hashlib
import json
import sys
import traceback

ROOT = Path(__file__).resolve().parent
STAGE = ROOT.parent
BASE = STAGE.parent
TEMPLATE = BASE/'sep27-qft-trace/prefix_comparison/compare_so_trace_prefixes.py'
TEMPLATE_SHA = '6a0c553244df66005af4c66e2333e318ae831c9b0905cdaf952f4495221eed47'
ADAPTER_SHA = '90c773c74a81ed239e32fcc12fa8d238032d6fbcfef3f4d6eb2056856666ed99'
CORRECTNESS_SHA = '6e226c8d54e41020aeb0d5d5126ba31b2c10f3dedcba7d17d5fd45550815db03'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


for path, expected in ((TEMPLATE, TEMPLATE_SHA), (STAGE/'segmented_so_view.py', ADAPTER_SHA),
                       (STAGE/'check_segmented_so_view.py', CORRECTNESS_SHA)):
    if sha(path) != expected:
        raise ValueError('matched comparison source changed: '+str(path))
sys.path.insert(0, str(STAGE))
from segmented_so_view import (SegmentedBoundarySOTrace, BoundaryCheckedSOTrace,
    SOTraceBank, _derive_token, PINS, packed)
from check_segmented_so_view import (load_bank, LazyStreamingProgram, ExactCarrierCodec,
    verify_vendor, CALLS, LIVE, track, failure_snapshot, capture_tables)

CONTEXT = {'stage': 'imported_not_started'}


def utc():
    return datetime.now(timezone.utc).isoformat()


def sources():
    paths = (Path(__file__), ROOT/'MATCHED_DESIGN.md', TEMPLATE,
             STAGE/'segmented_so_view.py', STAGE/'check_segmented_so_view.py', *PINS)
    return {str(path): sha(path) for path in paths}


def table_inventory(program):
    """Existing concrete factory/inverse fields; no new typed column requests."""
    result = []
    for index, table in enumerate(program.lazy_factory.tables.values()):
        result.append({'role': 'factory', 'parent_factory_index': index,
                       'stats': deepcopy(table.report_metrics())})
        if table._inverse is not None:
            result.append({'role': 'inverse', 'parent_factory_index': index,
                           'stats': deepcopy(table._inverse.report_metrics())})
    return result


def numeric_ledger(engine):
    return [{'history': step.history, 'reference_ids': step.reference_ids,
        'selected_ids': step.selected_ids, 'charge': step.charge, 'bit': step.bit}
        for step in engine.steps]


def run_prefix(label, cls, program, bank, history):
    before = table_inventory(program)
    wall_started = utc()
    first, started = len(CALLS), perf_counter()
    engine = track(label, cls(program, F(1, 3), certificate_bank=bank))
    assert engine.history == () and not engine.cache
    plans = [engine.advance(bit) for bit in history]
    terminal_mass = engine.mass()
    calculation_seconds = perf_counter()-started
    calculation_core_calls = len(CALLS)-first
    wall_calculation_end = utc()
    assert engine._guard_depth == 0 and engine._guard_owner is None
    counters = {'gram': deepcopy(engine.stats), 'policy': deepcopy(engine.policy_stats),
                'guard': engine._guard_diagnostics()}
    after = table_inventory(program)
    ledger = numeric_ledger(engine)
    capture_started = perf_counter()
    evidence = engine.evidence()
    evidence_seconds = perf_counter()-capture_started
    evidence_end = perf_counter()
    wall_evidence_end = utc()
    total_calls = len(CALLS)-first
    # Deep detachment and output encoding are excluded from both timing windows.
    evidence = deepcopy(evidence)
    assert evidence['boundary_guard']['active_depth'] == 0
    assert not evidence['boundary_guard']['owner_active']
    result = {'label': label, 'implementation': cls.__name__, 'history': history,
        'calculation_seconds': calculation_seconds, 'evidence_capture_seconds': evidence_seconds,
        'total_seconds_through_evidence': evidence_end-started,
        'counter_inventory_and_UTC_gap_seconds': evidence_end-started-calculation_seconds-evidence_seconds,
        'wall_started_utc': wall_started, 'wall_calculation_end_utc': wall_calculation_end,
        'wall_evidence_end_utc': wall_evidence_end,
        'calculation_actual_core_calls': calculation_core_calls,
        'total_actual_core_calls': total_calls, 'core_call_interval': [first, len(CALLS)],
        'table_instances_before': before, 'table_instances_after': after,
        'counters_before_evidence': counters, 'plans': plans, 'terminal_mass': terminal_mass,
        'numeric_ledger': ledger, 'evidence': evidence,
        'timing_scope': 'constructor, four advances, final mass; evidence separate; '
            'through-evidence includes diagnostic gap; detachment/JSON output excluded'}
    # Hold both completed receipts and engine fields if a later assertion fails.
    LIVE['completed_blocks']['run:'+label] = result
    return result


def assert_warm(before, after):
    assert [(x['role'], x['parent_factory_index']) for x in before] == [
        (x['role'], x['parent_factory_index']) for x in after]
    for old, new in zip(before, after):
        assert old['stats']['computed_columns'] == new['stats']['computed_columns']
        assert old['stats']['column_adder_digit_replays'] == new['stats']['column_adder_digit_replays']


def main():
    target = ROOT/'SEGMENTED_MATCHED_RESULTS.json.gz'
    summary_path = ROOT/'SEGMENTED_MATCHED_SUMMARY.json'
    if target.exists() or summary_path.exists() or any(ROOT.glob('FAILED_EXECUTION_*.json.gz')):
        raise ValueError('prior success or failure evidence exists; refusing a new scientific run')
    guard_path = STAGE/'STARTUP_GUARD.json'
    guard = json.loads(guard_path.read_bytes())
    assert guard['activity_allowed'] is True and guard['persistence_allowed'] is True
    assert guard['mode'] == 'TASK_RESEARCH' and guard['boundary'] == 'startup'
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC' and guard['sync_debt_events'] == []
    source = sources()
    first, started = len(CALLS), perf_counter()
    wall_start = utc()
    CONTEXT['stage'] = 'actual_native_bank_and_program_admission'
    vendor = verify_vendor()
    native_bank, native_source = load_bank()
    programs = [LazyStreamingProgram(N, a, 4, native_bank, 61,
        codec=ExactCarrierCodec(61, tuple(range(6)))) for N, a in ((21, 2), (21, 4), (65, 3))]
    admission_stop = len(CALLS)
    CONTEXT['stage'] = 'one_shared_cold_SO_bank'
    cold_first, cold_started = len(CALLS), perf_counter()
    bank = SOTraceBank(programs[0])
    cold_seconds = perf_counter()-cold_started
    cold = {'elapsed_seconds': cold_seconds, 'actual_core_calls': len(CALLS)-cold_first,
        'call_interval': [cold_first, len(CALLS)], 'evidence': bank.evidence(),
        'shared_by_both_implementations': True}
    LIVE['completed_blocks']['shared_cold_SO_bank'] = cold

    CONTEXT['stage'] = 'first_standalone_token_derivation_after_actual_admission'
    bank.check(programs[0])  # actual frozen binding; outside the token timer
    token_first, token_started = len(CALLS), perf_counter()
    token = _derive_token(bank, ADAPTER_SHA)
    token_seconds = perf_counter()-token_started
    assert len(CALLS) == token_first
    token_receipt = {'elapsed_seconds': token_seconds, 'actual_core_calls': 0,
        'segment_bytes': [len(part) for part in token.segments],
        'segment_payload_bytes': sum(map(len, token.segments)),
        'existing_admitted_view_bytes': len(bank._view_bytes),
        'token_sha256': token.token_sha256, 'bank_binding_sha256': bank.binding_sha256,
        'scope': 'first standalone pure-host derivation after paid admission; '
            'not injected into engines and not subtracted from measured constructors'}
    LIVE['completed_blocks']['standalone_token_derivation'] = token_receipt

    warmups, pairs = [], []
    LIVE['completed_blocks']['paid_warmups'] = warmups
    LIVE['completed_blocks']['completed_pairs'] = pairs
    history = (1, 0, 0, 0)
    for index, program in enumerate(programs):
        CONTEXT['fixture'] = {'N': program.N, 'a': program.a, 't': program.t}
        bank.check(program)
        CONTEXT['stage'] = 'paid_warmup'
        warmup = run_prefix(f'program{index}:warmup', BoundaryCheckedSOTrace, program, bank, history)
        warmups.append({'N': program.N, 'a': program.a, 'run': warmup})
        for repetition, order in enumerate(((BoundaryCheckedSOTrace, SegmentedBoundarySOTrace),
                                            (SegmentedBoundarySOTrace, BoundaryCheckedSOTrace))):
            CONTEXT['stage'] = 'matched_pair:'+str(repetition)
            runs = []
            LIVE['completed_blocks']['current_pair_runs'] = runs
            for cls in order:
                label = f'program{index}:pair{repetition}:{cls.__name__}'
                runs.append(run_prefix(label, cls, program, bank, history))
            old = next(run for run in runs if run['implementation'] == BoundaryCheckedSOTrace.__name__)
            new = next(run for run in runs if run['implementation'] == SegmentedBoundarySOTrace.__name__)
            assert old['plans'] == new['plans'] and old['numeric_ledger'] == new['numeric_ledger']
            assert old['terminal_mass'] == new['terminal_mass'] > 0
            assert old['calculation_actual_core_calls'] == new['calculation_actual_core_calls']
            assert old['total_actual_core_calls'] == new['total_actual_core_calls']
            assert old['counters_before_evidence']['gram'] == new['counters_before_evidence']['gram']
            assert old['counters_before_evidence']['policy'] == new['counters_before_evidence']['policy']
            assert old['counters_before_evidence']['guard']['stats'] == new['counters_before_evidence']['guard']['stats']
            for run in runs:
                assert_warm(run['table_instances_before'], run['table_instances_after'])
            for key in ('correlations', 'observer_operations'):
                assert old['evidence']['inherited'][key] == new['evidence']['inherited'][key]
            ng = new['counters_before_evidence']['guard']
            assert ng['view_stats']['compatibility_checks'] == 0
            assert ng['view_stats']['fast_accepts'] == ng['view_stats']['segmented_check_attempts']
            assert ng['view_token_sha256'] == token.token_sha256
            compact = {'N': program.N, 'a': program.a, 'repetition': repetition,
                'order': [run['implementation'] for run in runs],
                'old_seconds': old['calculation_seconds'], 'new_seconds': new['calculation_seconds'],
                'old_evidence_seconds': old['evidence_capture_seconds'],
                'new_evidence_seconds': new['evidence_capture_seconds'],
                'old_total_seconds': old['total_seconds_through_evidence'],
                'new_total_seconds': new['total_seconds_through_evidence'],
                'core_calls_each': old['calculation_actual_core_calls'],
                'logical_binding_checks_each': old['counters_before_evidence']['policy']['certificate_binding_checks'],
                'old_frozen_bank_method_calls': old['counters_before_evidence']['guard']['stats']['bank_check_attempts'],
                'new_frozen_bank_method_calls': ng['frozen_bank_check_invocations'],
                'new_segmented_view_stats': ng['view_stats'],
                'new_factory_and_inverse_columns_each': 0, 'new_column_digit_replays_each': 0,
                'full_covariances_observer_streams_numeric_ledger_native_counters_equal': True,
                'guard_topology_equal': True, 'strict_cross_version_cursor_equality_claimed': False}
            pairs.append({'summary': compact, 'runs': runs})
            print(json.dumps(compact), flush=True)
    assert source == sources()
    CONTEXT['stage'] = 'serialize_success_evidence'
    record = {'schema': 'BRC_SEGMENTED_SO_MATCHED_PREFIX_COMPARISON_V1', 'status': 'PASSED',
        'source_hashes': source, 'startup_guard': {'sha256': sha(guard_path), 'receipt': guard},
        'vendor': vendor, 'native_bank_source': native_source,
        'native_admission_call_interval': [first, admission_stop],
        'shared_cold_SO_bank': cold, 'standalone_token_derivation': token_receipt,
        'paid_warmups': warmups, 'pairs': pairs, 'actual_native_core_calls': CALLS[first:],
        'actual_native_core_call_count': len(CALLS)-first, 'elapsed_seconds': perf_counter()-started,
        'wall_start_utc': wall_start, 'wall_before_serialization_utc': utc(),
        'program_final_table_instances': [capture_tables(p) for p in programs],
        'scope': 'Three fixed positive prefixes, two alternating paired orders each, one process; '
            'fresh Gram engines, one actual SO bank and shared warmed modular instances. '
            'Cold bank/token derivation and paid warmups are separate. No full law, independent '
            'random trials, controlled-system-load claim, or asymptotic result.'}
    raw = packed(record)
    with target.open('xb') as handle:
        handle.write(gzip.compress(raw, mtime=0))
    summary = {'schema': record['schema'], 'status': record['status'], 'source_hashes': source,
        'pairs': [item['summary'] for item in pairs],
        'actual_native_core_call_count': record['actual_native_core_call_count'],
        'elapsed_seconds': record['elapsed_seconds'], 'raw_bytes': len(raw),
        'raw_sha256': hashlib.sha256(raw).hexdigest(), 'gzip_bytes': target.stat().st_size,
        'gzip_sha256': sha(target)}
    with summary_path.open('xb') as handle:
        handle.write(packed(summary))
    CONTEXT['stage'] = 'complete'
    print(packed(summary).decode(), flush=True)


if __name__ == '__main__':
    first = len(CALLS)
    initial_sources = sources()
    try:
        main()
    except BaseException as error:
        try:
            retained = failure_snapshot()
        except BaseException as capture_error:
            retained = {'capture_failed': True, 'exception_type': type(capture_error).__name__,
                        'message': str(capture_error)}
        try:
            failed_sources = sources()
        except BaseException as hash_error:
            failed_sources = {'capture_failed': True, 'exception_type': type(hash_error).__name__,
                              'message': str(hash_error)}
        try:
            attached = json.loads(packed(getattr(error, 'evidence', None)))
        except BaseException as attached_error:
            attached = {'capture_failed': True, 'exception_type': type(attached_error).__name__,
                        'message': str(attached_error)}
        failure = {'schema': 'BRC_SEGMENTED_MATCHED_FAILED_EXECUTION_V1', 'status': 'FAILED',
            'known_context': dict(CONTEXT), 'source_hashes_at_start': initial_sources,
            'source_hashes_at_failure': failed_sources, 'exception_type': type(error).__name__,
            'exception_message': str(error), 'traceback': traceback.format_exc(),
            'retained_live_work': retained, 'attached_exception_evidence': attached,
            'call_interval': [first, len(CALLS)], 'actual_native_core_calls': CALLS[first:]}
        path = ROOT/('FAILED_EXECUTION_'+uuid4().hex+'.json.gz')
        with path.open('xb') as handle:
            handle.write(gzip.compress(packed(failure), mtime=0))
        print('Failed execution evidence saved: '+str(path), file=sys.stderr, flush=True)
        raise
