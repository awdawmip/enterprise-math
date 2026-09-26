"""Common-generator native composition through the complete terminal route.

Every reference below is a compiled BRC circuit. No ideal QFT is executed.
"""
import gzip, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
from general_streaming import GeneralStreamingProgram, common_phase3_bank, PREVIOUS
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'sparse'))
from sparse_modular import sparse_modular_columns
from terminal_instrument import load_frozen_bank, streaming_leaves, encode, digest_rows
from stage80.fixed_phase import prepare_fixed, run_qft, law, fixed_error, apply_word
from stage45.brc_loop_recheck import verify_vendor, CALLS
from stage78.shor_benchmark import classical_postprocess


def check_word(new, old):
    squared = F(0)
    for j in range(new.dim):
        basis = [int(i == j) for i in range(new.dim)]
        v = new.apply_numer(basis)
        actual, ad = apply_word(basis, 1, new.inverse_phase_word)
        assert all(x * ad == y * new.den for x, y in zip(v, actual))
        back = new.apply_numer(v, inverse=True)
        assert back == [x * new.den ** 2 for x in basis]
        actual_back, bd = apply_word(actual, ad, new.inverse_phase_word, True)
        assert actual_back == basis and bd == 1
        oldcol = old.apply_numer(basis)
        squared += sum((F(x, new.den) - F(y, old.den)) ** 2 for x, y in zip(v, oldcol))
    # Frobenius norm is a conservative complete-carrier operator bound. This
    # deliberately does not silently import the sharper Stage89 Gram theorem.
    eta = F(819, 1 << 39)
    assert squared <= eta ** 2
    return {'all_forward_and_inverse_columns': new.dim,
        'frobenius_norm_squared_exact': squared,
        'operator_upper_bound': eta, 'bound_scope': 'whole carrier; inverse and controlled direct sums',
        'root_H4': new.root.h4_count, 'phase3_new_H4': new.h4_count,
        'phase3_old_H4': old.h4_count, 'no_exact_phase3_equality_claim': True}


def check_case(spec, bank, oldbank, dim, intervals, eta):
    N, a, t = spec; started = perf_counter()
    source, sd, _ = prepare_fixed(N, a, t, dim)
    full, fd, trace = run_qft(source, sd, t, bank, dim, trace=True)
    fullnums, fullden = law(full, fd, t)
    old, od, _ = run_qft(source, sd, t, oldbank, dim)
    oldnums, oldden = law(old, od, t)
    program = GeneralStreamingProgram(N, a, t, bank, dim, column_factory=sparse_modular_columns)
    leaves = streaming_leaves(program)
    rows = {}; bins = [F(0)] * (1 << t)
    for history, state, den in leaves:
        k = sum(bit << i for i, bit in enumerate(history))
        bins[k] = F(sum(v * v for row in state.values() for v in row), den * den)
        for (x, w, anc), row in state.items():
            assert x == anc == 0
            rows[k, w, anc] = (row, den)
    comparisons = 0
    for key in set(full) | set(rows):
        v = full.get(key, (0,) * dim); r, rd = rows.get(key, ((0,) * dim, 1))
        assert all(x * rd == y * fd for x, y in zip(v, r))
        comparisons += dim
    assert all(p == F(q, fullden) for p, q in zip(bins, fullnums))
    total_variation = sum(abs(p - F(q, oldden)) for p, q in zip(bins, oldnums)) / 2
    assert total_variation <= (t - 2) * eta
    posts = {k: classical_postprocess(N, a, t, k) for k in range(1 << t)}
    success = sum((p for k, p in enumerate(bins) if posts[k]['factors']), F(0))
    statuses = {}
    for k, p in enumerate(bins):
        label = posts[k]['status']; statuses[label] = statuses.get(label, F(0)) + p
    assert sum(statuses.values()) == 1
    fullhash = digest_rows((list(key) + [j, F(v * v, fd * fd)])
        for key, row in sorted(full.items()) for j, v in enumerate(row) if v)
    streamhash = digest_rows((list(key) + [j, F(v * v, den * den)])
        for key, (row, den) in sorted(rows.items()) for j, v in enumerate(row) if v)
    assert fullhash == streamhash
    return {'N': N, 'a': a, 't': t, 'dim': dim,
        'full_joint_coordinates_checked': comparisons, 'all_joint_amplitudes_equal': True,
        'all_control_bins_equal': True, 'joint_probability_sha256': fullhash,
        'all_leaf_slots': len(leaves), 'zero_leaf_slots': sum(not s for h, s, d in leaves),
        'success_probability': success, 'status_law': statuses,
        'TV_from_old_compiled_BRC_law': total_variation,
        'TV_old_to_new_upper_bound': (t - 2) * eta,
        'ideal_error_upper_bound_inherited': fixed_error(t, intervals, 64)['total'] + (t - 2) * eta,
        'streaming_metrics': program.report_metrics(),
        'full_macro_peak_endpoints': max([len(source)] + [x['endpoints'] for x in trace]),
        'new_QFT_phase_H4_count': sum((t - m + 1) * bank[m].h4_count for m in range(3, t + 1)),
        'old_QFT_phase_H4_count': sum((t - m + 1) * oldbank[m].h4_count for m in range(3, t + 1)),
        'control_law': bins, 'elapsed_seconds': perf_counter() - started}


def main():
    kernel = verify_vendor(); oldbank, intervals, dim = load_frozen_bank(6)
    bank = common_phase3_bank(oldbank)
    word = check_word(bank[3], oldbank[3]); print('complete native word certified', dim, flush=True)
    results = []
    for spec in [(15, 2, 4), (21, 2, 6), (15, 14, 4)]:
        row = check_case(spec, bank, oldbank, dim, intervals, word['operator_upper_bound'])
        results.append(row)
        print(json.dumps({'case': spec, 'coordinates': row['full_joint_coordinates_checked'],
            'seconds': row['elapsed_seconds']}), flush=True)
    output = {'schema': 'BRC_COMMON_ROOT_STREAMING_INTEGRATION_V1',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC',
        'status': 'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
        'route': 'ACTUAL_TYPED_BRC_ONLY', 'kernel': kernel, 'word_certificate': word,
        'phase_change': 'phase3 = literal phase4 word squared; all other phases unchanged',
        'precision': {'target_bits': 32, 'vector_bits': 64, 'dim': dim},
        'cases': results, 'actual_BRC_calls': len(CALLS), 'core_call_receipts': CALLS,
        'new_ideal_reference_execution': False, 'precision_increase': False,
        'streaming_representation_error': '0', 'polynomial_classical_time_claim': False}
    data = json.dumps(encode(output), sort_keys=True, separators=(',', ':')).encode()
    (ROOT / 'COMMON_RESULTS.json.gz').write_bytes(gzip.compress(data, mtime=0))
    brief = {k: v for k, v in output.items() if k not in ('cases', 'core_call_receipts')}
    brief['case_summaries'] = [{k: v for k, v in r.items() if k not in ('control_law', 'streaming_metrics', 'status_law')} for r in results]
    brief['payload_sha256'] = hashlib.sha256(data).hexdigest()
    (ROOT / 'COMMON_SUMMARY.json').write_text(json.dumps(encode(brief), indent=2) + '\n', encoding='utf-8')
    print('COMPLETE', len(CALLS), 'actual BRC calls', flush=True)


if __name__ == '__main__': main()
