"""Bounded same-native-word matrix checks; no ideal/float phase reference."""
from pathlib import Path
from fractions import Fraction as F
import gzip
import hashlib
import json
import sys
from time import perf_counter

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent/'sep26-shor-general/optimization/collision_analysis'))
sys.path.insert(0, str(ROOT/'modular_alias'))
from check_gram_sampler import load_bank, bound_sources
from carry_executor import CarryExecutor, Correlation, normalized, transpose
from gram_sampler import GramSampler
from lazy_streaming import LazyStreamingProgram
from carrier_codec import ExactCarrierCodec
from typed_aliases import discover_aliases, source_hashes as alias_hashes
from certified_word_compiler import PositivePathObserver, packed
from stage45.brc_loop_recheck import CALLS, verify_vendor


def hash_sources():
    import gram_sampler, lazy_streaming, carrier_codec, certified_word_compiler
    modules = (gram_sampler, lazy_streaming, carrier_codec, certified_word_compiler)
    paths = [Path(x.__file__) for x in modules] + [Path(__file__), ROOT/'carry_executor.py']
    return {**{str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            **alias_hashes()}


def exact(matrix):
    return tuple(tuple(F(v, matrix.den) for v in row) for row in matrix.rows)


def prepared_paths(executor, depth, reverse_time=False):
    """Each individual native path, retaining signed full word-boundary rows."""
    program = executor.program
    basis = (1,)+(0,)*(program.full_dim-1)
    basis = basis if program.codec is None else program.codec.encode(basis)
    paths = []
    for n in range(1 << depth):
        row, den, words = basis, 1, []
        times = tuple(range(depth))
        if reverse_time:
            times = tuple(reversed(times))
        for j in times:
            if (n >> (depth-1-j)) & 1:
                for gate in executor._gates(j):
                    row = gate.apply_numer(row)
                    den *= gate.den
                    words.append(gate.inverse_phase_word)
                if executor.history[j]:
                    row = tuple(-x for x in row)
        paths.append({'address': n, 'row': row, 'den': den, 'words': words})
    return paths


def direct_coefficient(paths, depth, displacement, dim, observer):
    """Actual signed product-sum observations of same native path vectors."""
    out = []
    for k in range(dim):
        row = []
        for ell in range(dim):
            terms = []
            for n, left in enumerate(paths):
                m = n+displacement  # bounded path-address wiring
                if not 0 <= m < len(paths):
                    continue
                right = paths[m]
                if left['row'][k] and right['row'][ell]:
                    terms.append((F(left['row'][k], left['den']),
                                  F(right['row'][ell], right['den'])))
            value = observer.evaluate('same_native_unmerged_path_product_sum', tuple(terms)) if terms else F(0)
            # Native balanced-arm amplitude normalisation is exactly dyadic.
            row.append(F(value.numerator, value.denominator << (2*depth)))
        out.append(tuple(row))
    return tuple(out)


def record(matrix):
    return {'rows': matrix.rows, 'den': matrix.den}


def main():
    first, started = len(CALLS), perf_counter()
    guard = json.loads((ROOT/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    before = hash_sources()
    kernel, sources = verify_vendor(), bound_sources()
    bank, bank_source = load_bank()
    admission_start = len(CALLS)
    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=ExactCarrierCodec(61, tuple(range(6))))
    d6_admission_calls = len(CALLS)-admission_start
    coefficient_cases, saved = [], {}
    for history in ((1, 0, 1, 0), (1, 1, 1, 1)):
        carry = CarryExecutor(program, history)
        observer = PositivePathObserver()
        checks = []
        for depth in range(5):
            paths = prepared_paths(carry, depth)
            for d in range(-(1 << depth), (1 << depth)+1):
                actual = carry.coefficient(depth, d)
                expected = direct_coefficient(paths, depth, d, carry.dim, observer)
                assert exact(actual) == expected, (history, depth, d)
                checks.append({'depth': depth, 'displacement': d, 'actual': record(actual),
                               'same_native_direct': expected, 'all_entries_equal': True})
                if history == (1, 0, 1, 0):
                    saved[depth, d] = actual
            print(json.dumps({'coefficient_history': history, 'depth_complete': depth,
                              'all_entries_equal': True}), flush=True)
        coefficient_cases.append({'history': history, 'dimension': carry.dim,
            'checks': checks, 'carry': carry.evidence(),
            'direct_observer_operations': observer.operations,
            'final_native_preparation_paths': paths})

    # The wrong chronological order is an actual same-word negative control.
    fixture = CarryExecutor(program, (1, 0, 1))
    wrong_paths = prepared_paths(fixture, 3, reverse_time=True)
    wrong_observer = PositivePathObserver()
    wrong = direct_coefficient(wrong_paths, 3, 7, 6, wrong_observer)
    right = exact(saved[3, 7])
    assert right[0][2] > 0 and wrong[0][2] < 0
    assert tuple(right[k][k] for k in range(6)) == tuple(wrong[k][k] for k in range(6))
    order_negative = {'correct': right, 'reversed': wrong,
        'residual_0_2_sign_distinguishes_order': True, 'diagonal_does_not_distinguish_this_fixture': True,
        'wrong_native_paths': wrong_paths, 'actual_wrong_order_observer': wrong_observer.operations}

    full_admission_start = len(CALLS)
    full = LazyStreamingProgram(21, 2, 4, bank, 61)
    full_admission_calls = len(CALLS)-full_admission_start
    carry61 = CarryExecutor(full, (1, 0, 1))
    observer61 = PositivePathObserver()
    paths61 = prepared_paths(carry61, 3)
    full_checks = []
    for d in (1, 7):
        actual = carry61.coefficient(3, d)
        expected = direct_coefficient(paths61, 3, d, 61, observer61)
        assert exact(actual) == expected
        small = exact(saved[3, d])
        embedded = tuple(tuple(small[k][ell] if k < 6 and ell < 6 else F(0)
                               for ell in range(61)) for k in range(61))
        assert exact(actual) == embedded
        full_checks.append({'depth': 3, 'displacement': d, 'actual': record(actual),
                            'same_native_direct': expected, 'full_D61_and_D6_embedding_equal': True})
    print(json.dumps({'D61_checks': len(full_checks), 'all_entries_equal': True}), flush=True)

    gamma_cases = []
    for N, a in ((21, 2), (65, 3)):
        admission_at = len(CALLS)
        p = LazyStreamingProgram(N, a, 4, bank, 61, codec=ExactCarrierCodec(61, tuple(range(6))))
        admission_calls = len(CALLS)-admission_at
        history = (1, 0, 1, 0)
        for depth in (3, 4):
            targets = tuple(sorted(set((1, p.modular_powers[depth-1],
                                        p.modular_powers[depth] if depth < p.t else 1))))
            at = len(CALLS)
            aliases = discover_aliases(p, depth, targets, min(4, 1 << depth))
            alias_calls = len(CALLS)-at
            gram = GramSampler(p)
            gram.history = history[:depth]
            carry = CarryExecutor(p, history[:depth])
            comparisons, assembled = [], {}
            for z in targets:
                at = len(CALLS)
                expected = gram.gamma(depth, z)
                gram_calls = len(CALLS)-at
                at = len(CALLS)
                actual = carry.sum_coefficients(depth, aliases['aliases'][z])
                assembled[z] = actual
                carry_calls = len(CALLS)-at
                assert exact(actual) == exact(expected), (N, depth, z)
                comparisons.append({'target': z, 'alias_count': len(aliases['aliases'][z]),
                    'carry': record(actual), 'gram': record(expected), 'all_entries_equal': True,
                    'incremental_native_calls_gram_first': gram_calls,
                    'incremental_native_calls_carry_after_gram': carry_calls})
            parent = carry._trace(assembled[1], 'carry_assembled_parent_mass')
            assert parent == gram.mass()
            condition = {'parent_mass': parent, 'same_native_gram_mass_equal': True}
            if depth < p.t and parent > 0:
                shifted = assembled[p.modular_powers[depth]]
                cross = carry._trace(carry._left(shifted, carry._gates(depth)), 'carry_assembled_cross')
                children = tuple(carry._sum('carry_child_mass', (parent, sign*cross))/2 for sign in (1, -1))
                conditional = {'parent_mass': parent, 'cross': cross, 'child_masses': children,
                               'probabilities': tuple(x/parent for x in children)}
                assert conditional == gram.probabilities()
                condition.update(next_bit_conditional=conditional, all_next_bit_conditions_equal=True)
            elif depth < p.t:
                condition['conditioning_undefined_zero_mass'] = True
            else:
                condition['terminal_no_next_bit'] = True
            gamma_cases.append({'N': N, 'a': a, 'depth': depth, 'history': history,
                'admission_native_calls': admission_calls, 'aliases': aliases, 'alias_native_calls': alias_calls,
                'comparisons': comparisons, 'condition': condition,
                'carry_evidence': carry.evidence(), 'gram_evidence': gram.evidence(),
                'cost_scope': 'one fixed query set; shared admitted program and process-wide native cache; call counts are not cold runtime speedup measurements'})
            print(json.dumps({'gamma_N': N, 'depth': depth, 'targets': targets, 'all_entries_equal': True,
                'aliases': aliases['metrics']['output_aliases'], 'old_distinct_queries': len(gram.cache),
                'carry_digits': carry.carry_stats['carry_digits']}), flush=True)

    negatives = []
    def reject(name, fn):
        try:
            fn()
        except ValueError as e:
            negatives.append({'name': name, 'message': str(e), 'rejected': True})
        else:
            raise AssertionError('invalid call accepted: '+name)
    for name, fn in (
        ('boolean_history', lambda: CarryExecutor(program, (True,))),
        ('invalid_history_bit', lambda: CarryExecutor(program, (2,))),
        ('future_history', lambda: CarryExecutor(program, (0,)*5)),
        ('boolean_depth', lambda: fixture.coefficient(True, 0)),
        ('future_depth', lambda: fixture.coefficient(4, 0)),
        ('boolean_displacement', lambda: fixture.coefficient(1, True)),
        ('fractional_displacement', lambda: fixture.coefficient(1, F(1, 2))),
        ('duplicate_alias', lambda: fixture.sum_coefficients(3, (1, 1))),
        ('overflow_alias', lambda: fixture.sum_coefficients(3, (8,))),
        ('legacy_gamma', lambda: fixture.gamma(3, 1)),
        ('legacy_mass', lambda: fixture.mass()),
        ('legacy_probabilities', lambda: fixture.probabilities()),
        ('legacy_advance', lambda: fixture.advance(0)),
    ):
        reject(name, fn)
    fixture.history = (0, 0, 0)
    reject('changed_history_query', lambda: fixture.coefficient(1, 0))
    reject('changed_history_evidence', fixture.evidence)
    fixture.history = fixture._bound_history
    gate = full.bank[3]
    old_cache = gate._forward_nonzero
    gate._forward_nonzero = ()
    reject('changed_actual_D61_execution_cache', lambda: carry61.coefficient(3, 7))
    gate._forward_nonzero = old_cache
    assert hash_sources() == before
    payload = {'schema': 'BRC_TWO_CARRY_EXECUTION_V1',
        'status': 'AUTHOR_ACTUAL_TYPED_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256': before, 'dependencies_unchanged_during_execution': True,
        'startup_guard': guard, 'kernel': kernel, 'prior_sources': sources, 'bank_source': bank_source,
        'D6_admission_native_calls': d6_admission_calls, 'D61_admission_native_calls': full_admission_calls,
        'coefficient_cases': coefficient_cases, 'noncommuting_order_negative': order_negative,
        'D61_checks': full_checks, 'D61_carry_evidence': carry61.evidence(),
        'D61_direct_observer_operations': observer61.operations,
        'D61_preparation_paths': paths61, 'gamma_cases': gamma_cases,
        'negative_controls': negatives, 'native_core_call_receipts': CALLS[first:],
        'actual_native_core_calls': len(CALLS)-first, 'elapsed_seconds': perf_counter()-started,
        'ideal_QFT_reference_run': False, 'general_complexity_breakthrough_claimed': False,
        'scope': 'All entries of bounded actual native coefficients and assembled modular Gamma; fixed histories, no new conditional sampler or ideal error bound.'}
    raw = packed(payload)
    target = ROOT/'CARRY_EXECUTION_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {k: payload[k] for k in ('schema', 'status', 'source_sha256',
        'dependencies_unchanged_during_execution', 'actual_native_core_calls', 'elapsed_seconds', 'scope')}
    summary.update(coefficient_matrices_checked=sum(len(c['checks']) for c in coefficient_cases),
        full_D61_matrices_checked=len(full_checks), gamma_matrices_checked=sum(len(c['comparisons']) for c in gamma_cases),
        negative_controls_rejected=len(negatives), noncommuting_order_negative_detected=True,
        payload_sha256=hashlib.sha256(raw).hexdigest(), payload_bytes=len(raw),
        gzip_sha256=hashlib.sha256(target.read_bytes()).hexdigest(), gzip_bytes=target.stat().st_size,
        case_costs=[{'N': c['N'], 'depth': c['depth'], 'alias_metrics': c['aliases']['metrics'],
            'carry': c['carry_evidence']['carry_stats'], 'carry_actions': c['carry_evidence']['inherited_action_stats'],
            'gram_report': c['gram_evidence']['report']} for c in gamma_cases])
    (ROOT/'CARRY_EXECUTION_SUMMARY.json').write_bytes(packed(summary)+b'\n')
    print(json.dumps({k: v for k, v in summary.items() if k not in ('source_sha256', 'case_costs')}), flush=True)


if __name__ == '__main__':
    main()
