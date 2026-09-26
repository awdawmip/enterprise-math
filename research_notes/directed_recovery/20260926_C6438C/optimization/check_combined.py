"""Cross-check demand columns, selected-child contraction and exact codec."""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from random import Random
import hashlib
import json
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT.parent
for path in (ROOT / 'carrier_codec', ROOT / 'streaming',
             PACKAGE / 'direct_word_integration'):
    sys.path.insert(0, str(path))
from check_direct_word_integration import load_phase
from carrier_codec import ExactCarrierCodec, CompleteNativeWord
from lazy_streaming import SelectedStreamingProgram, sample_selected
from general_streaming import GeneralStreamingProgram
from general_driver import sample_once
from sparse_modular import sparse_modular_columns
from stage80.fixed_phase import norm
from stage45.brc_loop_recheck import CALLS, verify_vendor
from stage79.phase_compiler import encode


def instrument_only(N, a, t, k):
    return {'status': 'INSTRUMENT_ONLY_EQUALITY_TEST', 'factors': []}


def modular_resources(program):
    tables = list(program.lazy_factory.tables.values())
    reports = [table.report_metrics() for table in tables]
    proofs = {p['certificate_sha256']: p for p in program.lazy_permutation_verifications}
    return {'distinct_multipliers': len(tables),
        'cached_columns': sum(r['cached_column_count'] for r in reports),
        'setup_adder_digit_replays': sum(r['setup_adder_digit_replays'] for r in reports),
        'column_adder_digit_replays': sum(r['column_adder_digit_replays'] for r in reports),
        'verification_adder_digit_replays': sum(p['replayed_adder_digits'] for p in proofs.values()),
        'whole_domain_enumerated': False, 'tables': reports}


def main():
    started = perf_counter()
    first_call = len(CALLS)
    kernel = verify_vendor()
    bank = {2: CompleteNativeWord((('swap', 0, 1), ('neg', 1)), 61)}
    phase_provenance = {}
    for m in (3, 4):
        record, phase_provenance[str(m)] = load_phase(m)
        bank[m] = CompleteNativeWord(record['word'], 61)
    codec = ExactCarrierCodec(61, tuple(range(6)))
    cases = []
    for N in (15, 21, 35):
        full = GeneralStreamingProgram(N, 2, 4, bank, 61, column_factory=sparse_modular_columns)
        opt = SelectedStreamingProgram(N, 2, 4, bank, 61, codec=codec)
        fs, fd = full.initial()
        cs, cd = opt.initial()
        queue = [((), fs, fd, cs, cd)]
        comparisons, residual = [], False
        for depth in range(4):
            next_queue = []
            for history, fs, fd, cs, cd in queue:
                native_children = full.branches(fs, fd, history)
                plan = opt.branch_plan(cs, cd, history)
                for bit, (ns, nd) in enumerate(native_children):
                    small, small_den = opt.materialize(plan, bit)
                    decoded = codec.decode_state(small)
                    assert (decoded, small_den) == (ns, nd)
                    assert plan.masses[bit] == norm(ns, nd)
                    residual |= any(any(row[2:]) for row in small.values())
                    comparisons.append({'history': history + (bit,), 'mass': str(plan.masses[bit]),
                                        'rows': len(small), 'all_61_coordinates_equal': True})
                    next_queue.append((history + (bit,), ns, nd, small, small_den))
            queue = next_queue
        assert sum(norm(fs, fd) for _, fs, fd, _, _ in queue) == 1
        # A true one-history run, separate from the exhaustive law checker.
        ref = GeneralStreamingProgram(N, 2, 4, bank, 61, column_factory=sparse_modular_columns)
        selected = SelectedStreamingProgram(N, 2, 4, bank, 61, codec=codec)
        reference_draw = sample_once(ref, Random(20260926), postprocess=instrument_only)
        selected_draw = sample_selected(selected, Random(20260926), postprocess=instrument_only)
        for key in ('history', 'history_probability', 'events', 'postprocessing'):
            assert reference_draw[key] == selected_draw[key], key
        sm = selected.report_metrics()
        assert sm['selected_child']['materialized_children'] == 4
        cases.append({'N': N, 'a': 2, 't': 4, 'all_history_edges': comparisons,
            'nonzero_residual_seen': residual, 'single_sample': selected_draw,
            'full_single_sample_metrics': ref.report_metrics(),
            'optimized_single_sample_metrics': sm,
            'lazy_modular_resources': modular_resources(selected)})
    # Huge work carrier, deliberately only four rounds. This is a demand-cost
    # check, not the t=2n factorization regime and not a factoring benchmark.
    N = (1 << 127) - 1
    large = SelectedStreamingProgram(N, 2, 4, bank, 61, codec=codec)
    record = sample_selected(large, Random(17), postprocess=instrument_only)
    assert len(record['history']) == 4
    large_case = {'N': str(N), 'input_bits': 127, 't': 4,
        'scope': 'four-round instrument only; not default-width Shor or factorization',
        'sample': record, 'metrics': large.report_metrics(),
        'lazy_modular_resources': modular_resources(large)}
    sources = {}
    for path in (Path(__file__), ROOT / 'carrier_codec/carrier_codec.py',
                 ROOT / 'streaming/lazy_streaming.py', ROOT / 'lazy_modular/lazy_modular.py'):
        sources[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    result = {'status': 'AUTHOR_EXECUTED_SHARED_CONTEXT_NOT_ADMITTED',
        'kernel': kernel, 'phase_provenance': phase_provenance, 'cases': cases,
        'large_carrier_case': large_case, 'source_sha256': sources,
        'actual_BRC_calls': len(CALLS) - first_call, 'seconds': perf_counter() - started}
    (ROOT / 'COMBINED_RESULTS.json').write_text(json.dumps(encode(result), indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'all_cases_exact': True, 'small_cases': len(cases),
        'history_edges': sum(len(c['all_history_edges']) for c in cases),
        'actual_BRC_calls': result['actual_BRC_calls'], 'seconds': result['seconds'],
        'large_carrier': large_case['lazy_modular_resources']}))


if __name__ == '__main__':
    main()
