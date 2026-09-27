"""Declared bounded check; compile-only until the parent authorizes execution.

No timing comparison. All metadata toy checks are explicitly host/schema checks,
not native scientific receipts. Actual comparisons use the frozen native program.
"""
from copy import copy, deepcopy
from dataclasses import replace
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
BASE = ROOT.parent
sys.path.insert(0, str(BASE/'sep26-shor-general/optimization/collision_analysis'))
from check_gram_sampler import load_bank, LazyStreamingProgram, ExactCarrierCodec, verify_vendor
from segmented_so_view import (SegmentedBoundarySOTrace, BoundaryCheckedSOTrace,
    SOTraceBank, PROFILE, packed, strict_bytes, metadata_bytes,
    compare_raw_or_frozen, PINS)
from gram_sampler import QueryBudgetExhausted
from stage45.brc_loop_recheck import CALLS

CONTEXT = {'stage': 'not_started'}
LIVE = {'completed_blocks': {}, 'engines': {}}


def hashes():
    paths = (Path(__file__), ROOT/'segmented_so_view.py', ROOT/'DESIGN.md', *PINS)
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


def clean(obj):
    assert obj._guard_depth == 0 and obj._guard_owner is None


def track(name, engine):
    """Retain a constructed object for failure-only, noncomputational capture."""
    LIVE['engines'][name] = engine
    return engine


def failure_snapshot():
    """Read stored fields only; never call evidence/report/mass or a guard.

    Encoding errors are isolated per block/engine field. Successful pieces are
    converted to JSON-safe values immediately so one later failure cannot erase
    them or prevent retaining the independent global actual CALLS stream.
    """
    snapshot = {'completed_blocks': {}, 'engine_fields': {}, 'capture_errors': [],
        'capture_mode': 'STORED_FIELDS_AND_JSON_ONLY; NO_SCIENTIFIC_METHOD_CALL',
        'incomplete_constructor_objects_available': False}
    def capture(destination, label, getter):
        try:
            destination[label] = json.loads(packed(getter()))
        except BaseException as error:
            snapshot['capture_errors'].append({'field': label,
                'exception_type': type(error).__name__, 'message': str(error)})
    for name, block in LIVE['completed_blocks'].items():
        capture(snapshot['completed_blocks'], name, lambda block=block: block)
    for name, engine in LIVE['engines'].items():
        fields = {}; snapshot['engine_fields'][name] = fields
        getters = {
            'history': lambda: engine.history,
            'steps': lambda: [dict(vars(step)) for step in engine.steps],
            'pending': lambda: engine.pending,
            'certificates': lambda: engine.certificates,
            'interruption_events': lambda: engine.interruptions,
            'observer_operations': lambda: engine.observer.operations,
            'correlations': lambda: [{'key': key, 'numerator_rows': matrix.rows,
                                      'denominator': matrix.den}
                                     for key, matrix in engine.cache.items()],
            'native_stats': lambda: engine.stats,
            'policy_stats': lambda: engine.policy_stats,
            'guard_stats': lambda: engine._guard_stats,
            'guard_depth': lambda: engine._guard_depth,
            'guard_owner': lambda: engine._guard_owner,
            'query_budget': lambda: engine.query_budget,
            'source_sha256': lambda: engine._own_source,
        }
        if hasattr(engine, '_view_stats'):
            getters['view_stats'] = lambda: engine._view_stats
        for label, getter in getters.items():
            capture(fields, label, getter)
    return snapshot


def semantic_cursor(cursor):
    return {key: cursor[key] for key in ('epsilon', 'program_sha256', 'history', 'steps')}


def metadata_predicate_checks():
    """Finite pure-JSON examples; never presented as an actual admitted program."""
    results = []
    native = (61, 6, (0, 1, 2, 3, 4, 5), (((0, 1),),))
    baseline = native + (metadata_bytes({'10': 0, '2': 0}), metadata_bytes({'x': 1}))

    def whole(raw):
        return metadata_bytes({'native_fields': raw[:-2],
            'phase_bindings': json.loads(raw[-2]), 'codec_binding': json.loads(raw[-1])})

    admitted = whole(baseline)
    decoded = json.loads(admitted)
    expected = tuple(metadata_bytes(decoded[key]) for key in
                     ('native_fields', 'phase_bindings', 'codec_binding'))

    def trial(name, raw, accepted, route=None):
        calls = []
        def old_check():
            calls.append('frozen_predicate_analogue')
            if whole(raw) != admitted:
                raise ValueError('pure JSON predicate mismatch')
        old_accepts = whole(raw) == admitted
        try:
            actual_route = compare_raw_or_frozen(raw, expected, old_check)
            actual_accepts = True
        except ValueError:
            actual_route, actual_accepts = 'REJECTED', False
        assert actual_accepts == old_accepts == accepted
        if route is not None:
            assert actual_route == route
        results.append({'case': name, 'accepted': accepted, 'route': actual_route,
            'fallback_calls': len(calls), 'matches_whole_JSON_predicate': True,
            'native_scientific_execution': False})

    trial('canonical_fast', baseline, True, 'SEGMENTED_FAST_ACCEPT')
    integer_keys = native + (metadata_bytes({2: 0, 10: 0}), baseline[-1])
    assert integer_keys[-2] != baseline[-2]
    trial('numeric_key_order_compatibility', integer_keys, True, 'FROZEN_COMPATIBILITY_ACCEPT')
    # Expected segments remain the original immutable tuple after slow acceptance.
    trial('canonical_after_slow_accept_no_refresh', baseline, True, 'SEGMENTED_FAST_ACCEPT')
    for label, zero in (('native_bool_int_distinguished', False),
                        ('native_float_int_distinguished', 0.0)):
        changed = list(native)
        changed[3] = (((zero, 1),),)
        raw = tuple(changed)+baseline[-2:]
        assert raw == baseline  # the weaker host equality would miss this
        trial(label, raw, False)
    trial('native_tuple_list_same_JSON', (61, 6, [0, 1, 2, 3, 4, 5], native[3])+baseline[-2:],
          True, 'SEGMENTED_FAST_ACCEPT')
    trial('changed_phase_value_rejected', native+(metadata_bytes({'10': 1, '2': 0}), baseline[-1]), False)
    trial('changed_codec_value_rejected', native+(baseline[-2], metadata_bytes({'x': True})), False)
    return results


def capture_tables(program):
    # Factory and inverse objects remain separate instances even when their
    # mathematical multiplier agrees. Do not deduplicate by N/b/content hash.
    tables = []
    for index, table in enumerate(program.lazy_factory.tables.values()):
        tables.append({'factory_index': index, 'role': 'factory',
                       'evidence': table.export_certificate()})
        inverse = getattr(table, '_inverse', None)
        if inverse is not None and inverse is not table:
            tables.append({'factory_index': index, 'role': 'created_inverse',
                           'evidence': inverse.export_certificate()})
    return {'N': program.N, 'a': program.a, 'phase_bindings': program.phase_bindings,
        'codec_binding': program.codec_binding, 'H4_binding': program.h4_binding,
        'permutation_verifications': program.lazy_permutation_verifications,
        'table_instances': tables,
        'scope': 'shared program final instances; not summed once per engine'}


def main():
    out = ROOT/'SEGMENTED_VIEW_RESULTS.json.gz'
    summary_path = ROOT/'SEGMENTED_VIEW_SUMMARY.json'
    if out.exists() or summary_path.exists() or any(ROOT.glob('FAILED_EXECUTION_*.json.gz')):
        raise ValueError('prior success or FAILED evidence exists; refusing a new scientific run')
    CONTEXT['stage'] = 'new_stage_startup_guard'
    guard_bytes = (ROOT/'STARTUP_GUARD.json').read_bytes()
    guard = json.loads(guard_bytes)
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    source = hashes()
    first, start = len(CALLS), perf_counter()
    CONTEXT['stage'] = 'pure_metadata_predicate_checks'
    before = len(CALLS)
    toy_checks = metadata_predicate_checks()
    LIVE['completed_blocks']['metadata_predicate_checks'] = toy_checks
    assert len(CALLS) == before
    CONTEXT['stage'] = 'actual_full_native_admission'
    vendor = verify_vendor()
    native_bank, native_binding = load_bank()
    programs = [LazyStreamingProgram(21, a, 4, native_bank, 61,
        codec=ExactCarrierCodec(61, tuple(range(6)))) for a in (2, 4)]
    admission_end = len(CALLS)
    CONTEXT['stage'] = 'unchanged_cold_SO_bank'
    bank = SOTraceBank(programs[0])
    LIVE['completed_blocks']['unchanged_cold_SO_bank'] = bank.evidence()
    fixtures = []
    LIVE['completed_blocks']['fixtures'] = fixtures
    for program in programs:
        CONTEXT['stage'] = 'matched_prefix:a'+str(program.a)
        interval_start = len(CALLS)
        old = track('fixture_a'+str(program.a)+'_old',
                    BoundaryCheckedSOTrace(program, F(1, 3), certificate_bank=bank))
        new = track('fixture_a'+str(program.a)+'_new',
                    SegmentedBoundarySOTrace(program, F(1, 3), certificate_bank=bank))
        steps = []
        LIVE['completed_blocks']['current_fixture_steps_a'+str(program.a)] = steps
        for bit in (1, 0, 0, 0):
            depth = len(new.history)
            old_plan, new_plan = old.probabilities(), new.probabilities()
            assert old_plan == new_plan and new_plan['child_masses'][bit] > 0
            assert old.pending == new.pending
            assert old.gamma(depth, 1) == new.gamma(depth, 1)
            assert old.advance(bit) == new.advance(bit)
            assert old.mass() == new.mass()
            assert semantic_cursor(old.cursor()) == semantic_cursor(new.cursor())
            clean(old); clean(new)
            steps.append({'depth': depth, 'bit': bit, 'plan': deepcopy(new_plan),
                'full_covariance_equal': True, 'pending_and_ledger_equal': True})
        old_evidence, new_evidence = deepcopy(old.evidence()), deepcopy(new.evidence())
        assert old_evidence['inherited']['correlations'] == new_evidence['inherited']['correlations']
        assert old_evidence['inherited']['observer_operations'] == new_evidence['inherited']['observer_operations']
        assert old.stats == new.stats
        assert old_evidence['policy_stats'] == new_evidence['policy_stats']
        assert old_evidence['boundary_guard']['stats'] == new_evidence['boundary_guard']['stats']
        assert old_evidence['cursor']['schema'] != new_evidence['cursor']['schema']
        assert strict_bytes(old_evidence['cursor']) != strict_bytes(new_evidence['cursor'])
        view = new_evidence['boundary_guard']['view_stats']
        assert view['compatibility_checks'] == 0
        assert view['fast_accepts'] == view['segmented_check_attempts']
        assert view['constructor_frozen_checks'] == 1
        fixtures.append({'N': program.N, 'a': program.a, 't': 4, 'history': [1, 0, 0, 0],
            'steps': steps, 'old_SO_boundary': old_evidence, 'segmented_boundary': new_evidence,
            'call_interval': [interval_start, len(CALLS)],
            'same_native_and_policy_counters': True, 'same_guard_call_topology': True,
            'same_complete_saved_covariances_and_observer_streams': True,
            'shared_modular_cache_cost_not_a_matched_timing_claim': True})

    p = programs[0]
    CONTEXT['stage'] = 'new_pending_cursor_and_restore'
    target = track('restore_original', SegmentedBoundarySOTrace(p, F(1, 3), certificate_bank=bank))
    for bit in (1, 0, 0):
        target.advance(bit)
    target.prepare_next()
    cursor = json.loads(strict_bytes(target.cursor()))
    pending_snapshot = deepcopy(target.evidence())
    LIVE['completed_blocks']['pending_cursor'] = cursor
    LIVE['completed_blocks']['pending_snapshot'] = pending_snapshot
    restored = track('restore_replayed', SegmentedBoundarySOTrace.restore(p, cursor, certificate_bank=bank))
    assert strict_bytes(restored.cursor()) == strict_bytes(cursor)
    negatives = []
    LIVE['completed_blocks']['negative_controls'] = negatives

    def reject(label, call, *, zero=False, engine=None):
        CONTEXT['stage'] = 'negative:'+label
        call_start = len(CALLS)
        observations = None if engine is None else len(engine.observer.operations)
        try:
            call()
        except ValueError as error:
            delta = len(CALLS)-call_start
            if zero:
                assert delta == 0
            failed = deepcopy(getattr(error, 'evidence', None))
            if engine is not None:
                clean(engine)
                if zero:
                    assert observations == len(engine.observer.operations)
            if failed is not None:
                assert failed['boundary_guard']['active_depth'] == 0
            negatives.append({'case': label, 'rejected': True, 'reason': str(error),
                'actual_core_calls': delta, 'call_interval': [call_start, len(CALLS)],
                'failed_replay_evidence': failed,
                'guard_after': None if engine is None else deepcopy(engine._guard_diagnostics()),
                'zero_new_observer_when_required': zero})
        else:
            raise AssertionError(label+' accepted')

    # One changed metadata field reaches each public outer entry. Unlike an
    # actual word replacement, this bypasses the Adaptive snapshot and therefore
    # specifically tests the new byte mismatch -> old frozen-check reject path.
    entries = {'gamma': lambda: target.gamma(3, 1), 'mass': target.mass,
        'probabilities': target.probabilities, 'advance': lambda: target.advance(0),
        'prepare_next': target.prepare_next, 'cursor': target.cursor,
        'evidence': target.evidence, 'report': target.report}
    original_phase = p.phase_bindings
    admitted_token = target._view_token
    for name, entry in entries.items():
        p.phase_bindings = {**original_phase, '__changed_metadata__': True}
        old_fallback_count = target._view_stats['compatibility_rejections']
        try:
            reject('phase_metadata_at_'+name, entry, zero=True, engine=target)
        finally:
            p.phase_bindings = original_phase
        assert target._view_stats['compatibility_rejections'] == old_fallback_count+1
        assert target._view_token is admitted_token
    original_codec = p.codec_binding
    p.codec_binding = {**original_codec, '__changed_metadata__': True}
    try:
        reject('codec_metadata_mismatch', target.cursor, zero=True, engine=target)
    finally:
        p.codec_binding = original_codec

    def swap_and_call(field, value):
        original = getattr(target, field)
        setattr(target, field, value)
        try:
            target.cursor()
        finally:
            setattr(target, field, original)
    reject('forged_equal_content_token', lambda: swap_and_call('_view_token', replace(admitted_token)),
           zero=True, engine=target)
    reject('wrong_bank_object_type', lambda: swap_and_call('word_certificates', object()),
           zero=True, engine=target)
    copied_bank = copy(bank)
    assert type(copied_bank) is SOTraceBank and copied_bank is not bank
    assert copied_bank.binding_sha256 == bank.binding_sha256
    reject('distinct_same_content_SO_bank_identity',
           lambda: swap_and_call('word_certificates', copied_bank), zero=True, engine=target)
    reject('wrong_type_at_constructor',
           lambda: SegmentedBoundarySOTrace(p, F(1, 3), certificate_bank=object()), zero=True)

    # Actual frozen native-object replacement must still be rejected by the
    # retained Adaptive snapshot before a segmented comparison or observer.
    gate = p.bank[3]
    gate_controls = (
        ('ordered_native_word_replacement', replace(gate, inverse_phase_word=gate.inverse_phase_word+(('neg', 0),))),
        ('native_column_replacement', replace(gate, columns=tuple(reversed(gate.columns)))),
    )
    for label, modified in gate_controls:
        before = target._view_stats['segmented_check_attempts']
        p.bank[3] = modified
        try:
            reject(label, lambda: target.gamma(3, 1), zero=True, engine=target)
        finally:
            p.bank[3] = gate
        assert target._view_stats['segmented_check_attempts'] == before
    assert target._view_token is admitted_token
    runtime_negative_count = len(negatives)
    after_rejections = deepcopy(target.evidence())
    LIVE['completed_blocks']['after_runtime_rejections'] = after_rejections

    for label, mutate in (
        ('wrong_own_source', lambda c: c.update(source_sha256='0'*64)),
        ('wrong_view_profile', lambda c: c.update(view_profile='NONE')),
        ('wrong_view_token_hash', lambda c: c.update(view_token_sha256='0'*64)),
        ('wrong_bank_hash', lambda c: c.update(certificate_bank_sha256='0'*64)),
        ('wrong_selected_word', lambda c: c['steps'][1]['selected_ids'].append(4)),
        ('wrong_charge', lambda c: c['steps'][0].update(charge='1/9')),
        ('bool_history', lambda c: c['history'].__setitem__(0, True))):
        bad = deepcopy(cursor); mutate(bad)
        reject(label, lambda: SegmentedBoundarySOTrace.restore(p, bad, certificate_bank=bank))
    reject('old_SO_cursor', lambda: SegmentedBoundarySOTrace.restore(
        p, fixtures[0]['old_SO_boundary']['cursor'], certificate_bank=bank))
    assert len(negatives)-runtime_negative_count == 8
    assert target.advance(0) == restored.advance(0)
    assert strict_bytes(target.cursor()) == strict_bytes(restored.cursor())
    clean(target); clean(restored)
    resume = {'input_cursor': cursor, 'pending_snapshot': pending_snapshot,
        'after_runtime_rejections': after_rejections,
        'original': deepcopy(target.evidence()), 'restored': deepcopy(restored.evidence()),
        'strict_new_cursor_equal': True, 'query_cache_or_rng_restored': False}
    LIVE['completed_blocks']['pending_restore'] = resume

    CONTEXT['stage'] = 'budget_rollback_same_bit_retry'
    interrupted = track('budget_interrupted',
        SegmentedBoundarySOTrace(p, F(1, 3), query_budget=2, certificate_bank=bank))
    try:
        interrupted.advance(1)
    except QueryBudgetExhausted:
        clean(interrupted)
        assert interrupted.history == () and not interrupted.steps and interrupted.pending is not None
        failed_attempt = deepcopy(interrupted.evidence())
        LIVE['completed_blocks']['budget_failed_attempt'] = failed_attempt
    else:
        raise AssertionError('expected bounded query interruption')
    interrupted.query_budget = 1000
    interrupted.advance(1)
    fresh = track('budget_fresh', SegmentedBoundarySOTrace(p, F(1, 3), certificate_bank=bank))
    fresh.advance(1)
    assert strict_bytes(interrupted.cursor()) == strict_bytes(fresh.cursor())
    assert interrupted.mass() == fresh.mass()
    clean(interrupted); clean(fresh)
    retry = {'failed_attempt': failed_attempt, 'retried': deepcopy(interrupted.evidence()),
        'fresh': deepcopy(fresh.evidence()), 'same_bit_committed_once': True}
    LIVE['completed_blocks']['budget_recovery'] = retry

    CONTEXT['stage'] = 'serialize_success'
    assert source == hashes()
    payload = {'schema': 'BRC_SEGMENTED_SO_VIEW_BOUNDED_CHECK_V1', 'status': 'PASSED',
        'source_hashes': source, 'startup_guard_sha256': hashlib.sha256(guard_bytes).hexdigest(),
        'vendor': vendor, 'native_bank_binding': native_binding,
        'metadata_predicate_checks': toy_checks,
        'initial_program_admission_call_interval': [first, admission_end],
        'unchanged_cold_SO_bank': bank.evidence(), 'fixtures': fixtures,
        'runtime_negative_controls': negatives[:runtime_negative_count],
        'cursor_negative_controls': negatives[runtime_negative_count:],
        'pending_restore': resume, 'budget_recovery': retry,
        'program_final_table_instances': [capture_tables(p) for p in programs],
        'actual_core_calls': CALLS[first:], 'core_call_count': len(CALLS)-first,
        'elapsed_seconds': perf_counter()-start,
        'scope': 'BOUNDED_NATIVE_PREFIX_AND_METADATA_CORRECTNESS; NO_TIMING_OR_FULL_LAW_CLAIM'}
    raw = packed(payload)
    with out.open('xb') as handle:
        handle.write(gzip.compress(raw, mtime=0))
    summary = {'status': 'PASSED', 'source_hashes': source, 'fixtures': 2, 'positive_steps': 8,
        'metadata_toy_checks': len(toy_checks), 'runtime_negative_controls': runtime_negative_count,
        'cursor_negative_controls': len(negatives)-runtime_negative_count,
        'strict_pending_restore': True, 'budget_rollback_same_bit_retry': True,
        'complete_covariances_observer_streams_and_native_counters_equal': True,
        'core_call_count': payload['core_call_count'], 'elapsed_seconds': payload['elapsed_seconds'],
        'raw_sha256': hashlib.sha256(raw).hexdigest(), 'raw_bytes': len(raw),
        'gzip_sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'gzip_bytes': out.stat().st_size,
        'scope': payload['scope']}
    with summary_path.open('xb') as handle:
        handle.write(packed(summary))
    print(packed(summary).decode(), flush=True)
    CONTEXT['stage'] = 'complete'


if __name__ == '__main__':
    first = len(CALLS)
    initial_sources = hashes()
    try:
        main()
    except BaseException as error:
        # This collector only reads already-stored fields and serializes them.
        # Its own failure is separate; actual CALLS are saved regardless.
        try:
            retained = failure_snapshot()
        except BaseException as capture_error:
            retained = {'capture_failed': True, 'exception_type': type(capture_error).__name__,
                        'message': str(capture_error)}
        try:
            failed_sources = hashes()
        except BaseException as hash_error:
            failed_sources = {'capture_failed': True, 'exception_type': type(hash_error).__name__,
                              'message': str(hash_error)}
        try:
            attached = json.loads(packed(getattr(error, 'evidence', None)))
        except BaseException as attached_error:
            attached = {'capture_failed': True, 'exception_type': type(attached_error).__name__,
                        'message': str(attached_error)}
        failure = {'schema': 'BRC_SEGMENTED_VIEW_FAILED_EXECUTION_V1', 'status': 'FAILED',
            'source_hashes_at_start': initial_sources, 'source_hashes_at_failure': failed_sources,
            'known_context': dict(CONTEXT), 'exception_type': type(error).__name__,
            'exception_message': str(error), 'traceback': traceback.format_exc(),
            'attached_exception_evidence': attached,
            'retained_live_work': retained,
            'call_interval': [first, len(CALLS)], 'actual_core_calls': CALLS[first:]}
        path = ROOT/('FAILED_EXECUTION_'+uuid4().hex+'.json.gz')
        with path.open('xb') as handle:
            handle.write(gzip.compress(packed(failure), mtime=0))
        print('FAILED execution evidence saved: '+str(path), file=sys.stderr, flush=True)
        raise
