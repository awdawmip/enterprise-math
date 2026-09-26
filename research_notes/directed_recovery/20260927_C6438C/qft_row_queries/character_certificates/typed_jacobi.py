"""Jacobi and a one-bit character certificate from actual typed BRC division.

This observer never evaluates an ideal phase or changes a signed state.
The final-bit statement is restricted to the certified square schedule,
initial work label 1, and the existing complete native instrument.
"""
from __future__ import annotations

from pathlib import Path
from copy import deepcopy
import hashlib
import sys

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parents[1] / 'sep26-shor-general'
sys.path.insert(0, str(PREVIOUS / 'optimization/lazy_modular'))
from lazy_modular import (Arithmetic, LazyModularColumns, digest, require,
                          source_binding, sparse, verify_lazy_permutation)

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

JACOBI_SCHEMA = 'ACTUAL_TYPED_BRC_JACOBI_V1'
SCHEDULE_SCHEMA = 'ACTUAL_TYPED_BRC_SQUARE_CHARACTER_SCHEDULE_V1'
PROGRAM_SCHEMA = 'ACTUAL_NATIVE_PROGRAM_FINAL_CHARACTER_BIT_V1'


def binding():
    return {'jacobi_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'arithmetic_source': source_binding(),
            'math_sources': ['https://dlmf.nist.gov/27.9',
                'https://cacr.uwaterloo.ca/hac/about/chap2.pdf#page=26'],
            'tool_route': 'REUSE_APPLIED typed BRC long division; EXTEND domain character certificate',
            'admission': 'AUTHOR_ACTUAL_SHARED_CONTEXT_NOT_INDEPENDENTLY_ADMITTED'}


def deterministic_cost(arithmetic):
    return {k: v for k, v in arithmetic.stats.items() if k != 'native_kernel_calls_delta'}


def typed_jacobi_trace(a, N):
    """Return J(a,N), allowing any integer a and positive odd N (including 1).

    Every nontrivial remainder is an actual full-adder digit transducer.
    Parity, mod 4/mod 8, factor-of-two removal and +/-1 signs are label wiring.
    No factorization, order, ordinary pow or ordinary remainder is requested.
    """
    require(sparse.integer(a) and sparse.integer(N) and N >= 1,
            'integer numerator and positive odd integer denominator required')
    require(N & 1, 'Jacobi denominator must be odd')
    arithmetic = Arithmetic()
    wiring = 1  # N & 1 input check
    negative_flip = False
    if a < 0:
        negative_flip = (N & 3) == 3
        wiring += 1
    sign = -1 if negative_flip else 1
    quotient, residue, initial_division = arithmetic.divide(abs(a), N)
    x, n, steps = residue, N, []
    while x:
        before_x, before_n, before_sign = x, n, sign
        shifts = []
        while True:
            odd = x & 1
            wiring += 1
            if odd:
                break
            following = x >> 1
            wiring += 1
            shifts.append({'input': x, 'output': following})
            x = following
        n_mod8 = n & 7
        exponent_parity = len(shifts) & 1
        x_mod4, n_mod4 = x & 3, n & 3
        wiring += 4
        two_flip = exponent_parity == 1 and n_mod8 in (3, 5)
        reciprocal_flip = x_mod4 == 3 and n_mod4 == 3
        if two_flip:
            sign = -sign
        if reciprocal_flip:
            sign = -sign
        q, remainder, operation = arithmetic.divide(n, x)
        require(0 <= remainder < x, 'typed Jacobi remainder invariant')
        steps.append({'input_numerator': before_x, 'input_denominator': before_n,
            'input_sign': before_sign, 'factor_two_shifts': shifts,
            'odd_numerator': x, 'two_exponent_parity': exponent_parity,
            'denominator_mod8': n_mod8, 'numerator_mod4': x_mod4,
            'denominator_mod4': n_mod4, 'two_supplement_flip': two_flip,
            'reciprocity_flip': reciprocal_flip, 'output_sign': sign,
            'quotient': q, 'remainder': remainder, 'division_operation': operation})
        n, x = x, remainder
    value = sign if n == 1 else 0
    return {'schema': JACOBI_SCHEMA, 'a': a, 'N': N, 'value': value,
        'input_negative_supplement_flip': negative_flip,
        'initial_absolute_quotient': quotient, 'initial_absolute_residue': residue,
        'initial_division_operation': initial_division, 'steps': steps,
        'terminal_gcd': n, 'terminal_sign': sign,
        'arithmetic_operations': arithmetic.operations,
        'cost': {**deterministic_cost(arithmetic),
                 'jacobi_label_bit_wiring_operations': wiring},
        'source': binding(), 'host_remainder_used': False, 'factor_or_order_input': False,
        'resource_scope': 'native kernel calls are external run counts; digit replays and label wiring are separate',
        'convention': 'J(a,1)=1; J(a,N)=0 exactly when a and N are not coprime'}


def typed_jacobi(a, N):
    return typed_jacobi_trace(a, N)['value']


def verify_typed_jacobi(certificate):
    require(isinstance(certificate, dict) and certificate.get('schema') == JACOBI_SCHEMA,
            'wrong typed Jacobi certificate')
    rebuilt = typed_jacobi_trace(certificate['a'], certificate['N'])
    require(digest(rebuilt) == digest(certificate), 'typed Jacobi certificate does not replay')
    return {'verified': True, 'value': rebuilt['value'], 'certificate_sha256': digest(rebuilt),
            'replayed_adder_digits': rebuilt['cost']['adder_digit_replays']}


def certify_square_schedule(N, a, t, tables, *, initial_work_label=1):
    """Certify the final round of a reverse square schedule, never arbitrary state.

    This is a schedule theorem witness, not a certificate that a user-supplied
    mid-run state is reachable. Native instrument/phase admission stays with
    the already certified program. No work-support table is enumerated.
    """
    require(sparse.integer(N) and N >= 3 and (N & 1), 'odd integer N >= 3 required')
    require(sparse.integer(a) and 1 <= a < N, 'canonical positive base required')
    require(sparse.integer(t) and t >= 2 and not (t & 1), 'positive even t >= 2 required')
    require(sparse.integer(initial_work_label), 'integer initial work label required')
    require(type(tables) in (list, tuple) and len(tables) == t,
            'explicit t-entry schedule of lazy permutation objects required')
    jacobi = typed_jacobi_trace(a, N)
    permutations, sequence = {}, []
    for table in tables:
        require(type(table) is LazyModularColumns and table.N == N,
                'actual lazy permutation for this modulus required')
        key = str(table.b)
        if key not in permutations:
            verify_lazy_permutation(table)
            permutations[key] = deepcopy(table.permutation_certificate)
        else:
            # Each object must bind even when several schedule positions have
            # the same multiplier. A reused arithmetic proof is not a type waiver.
            require(table.certificate_sha256 == digest(permutations[key])
                    == digest(table.permutation_certificate), 'repeated permutation changed')
            require(table.width == permutations[key]['width']
                    and table.carrier_size == permutations[key]['carrier_size']
                    and table.inverse_multiplier == permutations[key]['inverse_certificate']['inverse_multiplier'],
                    'repeated permutation attributes changed')
        sequence.append({'multiplier': table.b,
                         'permutation_certificate_sha256': table.certificate_sha256})
    require(tables[-1].b == a, 'final work multiplier must equal the supplied base')
    arithmetic, squares = Arithmetic(), []
    for earlier in range(t-1):
        current = tables[earlier+1].b
        squared, operations = arithmetic.modmul(current, current, N)
        require(squared == tables[earlier].b, 'work multipliers are not a reversed typed square chain')
        squares.append({'earlier_round': earlier, 'later_multiplier': current,
                        'squared_multiplier': squared, 'product_operations': operations})
    available = initial_work_label == 1 and jacobi['value'] == -1
    reason = ('certified quadratic character separates the final translate'
              if available else ('initial work label is not the certified label 1'
              if initial_work_label != 1 else 'Jacobi character does not certify this schedule'))
    return {'schema': SCHEDULE_SCHEMA,
        'status': 'CERTIFIED_FINAL_BIT_FAIR' if available else 'UNAVAILABLE',
        'reason': reason, 'N': N, 'a': a, 't': t,
        'initial_work_label': initial_work_label, 'jacobi': jacobi,
        'schedule': sequence, 'permutation_certificates': permutations,
        'square_chain': squares, 'arithmetic_operations': arithmetic.operations,
        'schedule_arithmetic_cost': deterministic_cost(arithmetic),
        'permutation_verification_adder_digits': sum(
            p['inverse_certificate']['cost']['adder_digit_replays'] for p in permutations.values()),
        'source': binding(), 'final_round_index': t-1,
        'certified_fair_reported_bits': 1 if available else 0,
        'scope': 'only reachable positive-mass prefixes from work=1 under this schedule and the admitted complete native instrument',
        'arbitrary_midrun_state_authorized': False,
        'work_support_enumerated': False, 'claim_of_unfairness_if_unavailable': False,
        'hidden_factor_or_order_input': False,
        'residuals': 'all actual signed internal coordinates retained; no commutativity assumption'}


def verify_square_schedule(certificate, tables):
    require(isinstance(certificate, dict) and certificate.get('schema') == SCHEDULE_SCHEMA,
            'wrong square schedule character certificate')
    rebuilt = certify_square_schedule(certificate['N'], certificate['a'], certificate['t'], tables,
                                      initial_work_label=certificate['initial_work_label'])
    require(digest(rebuilt) == digest(certificate), 'square schedule character witness does not replay')
    return {'verified': True, 'status': rebuilt['status'], 'certificate_sha256': digest(rebuilt)}


def certify_program_final_bit(program):
    """Bind a schedule-only witness to the existing actual program descriptor.

    This adapter intentionally accepts no mid-run state. Its proof assumes the
    caller follows the original initial() and native transition contract. It
    does not replace full-row-oracle reachability or phase-word admission.
    """
    sys.path.insert(0, str(PREVIOUS / 'optimization/streaming'))
    import lazy_streaming
    require(type(program) in (lazy_streaming.LazyStreamingProgram,
                             lazy_streaming.SelectedStreamingProgram),
            'known actual native lazy program class required')
    require('initial' not in program.__dict__, 'instance initial-state override is not certified')
    initial, denominator = program.initial()
    require(denominator == 1 and set(initial) == {(0, 1, 0)},
            'program must start at work label 1 and zero spectator/control')
    row = initial[(0, 1, 0)]
    require(len(row) == program.dim and row[0] == 1 and not any(row[1:]),
            'program must retain the canonical complete initial internal vector')
    require(tuple(x.b for x in program.tables) == program.modular_powers,
            'program schedule descriptors disagree')
    schedule = certify_square_schedule(program.N, program.a, program.t, program.tables)
    return {'schema': PROGRAM_SCHEMA, 'status': schedule['status'], 'schedule_witness': schedule,
        'program_descriptor': {'N': program.N, 'a': program.a, 't': program.t,
            'dim': program.dim, 'full_dim': program.full_dim,
            'phase_bindings': deepcopy(program.phase_bindings),
            'codec_binding': deepcopy(program.codec_binding),
            'native_two_H4_binding': deepcopy(program.h4_binding),
            'initial_state': [[list(key), list(value)] for key, value in initial.items()],
            'initial_denominator': denominator,
            'program_source_sha256': hashlib.sha256(Path(lazy_streaming.__file__).read_bytes()).hexdigest()},
        'phase_and_instrument_admission': 'existing complete native program dependency, not repeated by this arithmetic certificate',
        'runtime_precondition': 'unchanged admitted program; history generated from the canonical initial state by its actual instrument',
        'authorizes_external_state_injection': False}


def verify_program_final_bit(certificate, program):
    require(isinstance(certificate, dict) and certificate.get('schema') == PROGRAM_SCHEMA,
            'wrong program character certificate')
    rebuilt = certify_program_final_bit(program)
    require(digest(rebuilt) == digest(certificate), 'program character descriptor does not replay')
    return {'verified': True, 'status': rebuilt['status'], 'certificate_sha256': digest(rebuilt)}
