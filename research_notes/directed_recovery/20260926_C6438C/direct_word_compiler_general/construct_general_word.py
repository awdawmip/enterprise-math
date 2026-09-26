"""Resumable actual-BRC four-square construction for any phase and tolerance.

Target expressions are certificate observers only. Every numeric square, floor
comparison, deficit, pair sum/complement and final norm uses existing actual
positive-path observations. Dictionaries route observed integer labels only.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMPILER_ROOT = ROOT.parent / 'new_word_compiler'
sys.path.insert(0, str(COMPILER_ROOT))
import certified_word_compiler as compiler
from stage80 import fixed_phase as fixed
from stage45.brc_loop_recheck import CALLS

PROFILE = ROOT / 'DIRECT_WORD_PROFILE.json'
FROZEN_COMPILER_SHA = 'e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d'
DIM = compiler.DIM


def require(test, message):
    if not test:
        raise ValueError(message)


def integer_observation(value):
    require(value.denominator == 1, 'integer endpoint required')
    return value.numerator


def source_binding():
    compiler_sha = hashlib.sha256((COMPILER_ROOT / 'certified_word_compiler.py').read_bytes()).hexdigest()
    require(compiler_sha == FROZEN_COMPILER_SHA, 'frozen compiler changed')
    return {'compiler': compiler.source_binding(),
            'constructor_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'profile_sha256': hashlib.sha256(PROFILE.read_bytes()).hexdigest(),
            'construction_proof_sha256': hashlib.sha256(
                (COMPILER_ROOT / 'CONSTRUCTIVE_FOUR_SQUARE_FRONTIER.md').read_bytes()).hexdigest()}


def floor_ratio(obs, name, numerator, denominator, upper):
    """Find an integer floor using only actual signed endpoint comparisons."""
    require(numerator >= 0 and denominator > 0, 'positive floor ratio')
    lo, hi = 0, upper + 1
    boundary = obs.evaluate(name + '_upper_boundary', ((hi, denominator), (-numerator,)))
    require(boundary > 0, 'floor range does not enclose target')
    steps = []
    while hi - lo > 1:
        mid = (lo + hi) // 2  # finite integer-label bisection
        observed = obs.evaluate(name + '_comparison', ((mid, denominator), (-numerator,)))
        steps.append({'candidate': mid, 'signed_observation': str(observed)})
        if observed <= 0:
            lo = mid
        else:
            hi = mid
    low = obs.evaluate(name + '_floor_lower', ((lo, denominator), (-numerator,)))
    high = obs.evaluate(name + '_floor_upper', ((lo + 1, denominator), (-numerator,)))
    require(low <= 0 < high, 'floor endpoint certificate')
    return lo, {'floor': lo, 'numerator': str(numerator), 'denominator': str(denominator),
                'lower_signed_probe': str(low), 'upper_signed_probe': str(high), 'steps': steps}


def choose_scale(obs, tolerance):
    """The least B >= 2 with 2**B * tolerance**2 > 128, by actual probes."""
    bits, probes = 2, []
    while True:
        scale = 1 << bits  # finite integer label, never a primitive coefficient change
        sufficient = obs.evaluate('S_delta_squared_minus_128',
                                  ((scale, tolerance, tolerance), (-128,)))
        probes.append({'denominator_exponent': bits, 'scale': scale,
                       'signed_observation': str(sufficient)})
        if sufficient > 0:
            return bits, scale, probes
        bits += 1


def construct_leading_normal(obs, m, tolerance, bits, scale, scale_probes):
    observer_bits = bits + 4
    interval = compiler.isolate_target(m + 1, observer_bits)
    lo, hi = F(interval['lower']), F(interval['upper'])
    lo2 = obs.evaluate('half_angle_lower_squared', ((lo, lo),))
    hi2 = obs.evaluate('half_angle_upper_squared', ((hi, hi),))
    cden = obs.add('c_lower_denominator', 1, hi2)
    cnum = obs.add('c_lower_numerator', 1, -hi2)
    sden = obs.add('s_lower_denominator', 1, lo2)
    snum = obs.evaluate('s_lower_numerator', ((2, lo),))
    scaled_cnum = obs.evaluate('scaled_c_lower_numerator', ((scale, cnum),))
    scaled_snum = obs.evaluate('scaled_s_lower_numerator', ((scale, snum),))
    a0, floor0 = floor_ratio(obs, 'a0', scaled_cnum, cden, scale)
    a1, floor1 = floor_ratio(obs, 'a1', scaled_snum, sden, scale)
    scale2 = obs.evaluate('scale_squared', ((scale, scale),))
    deficit = obs.evaluate('integer_norm_deficit', ((scale2,), (-a0, a0), (-a1, a1)))
    k = integer_observation(deficit)
    require(k >= 0, 'negative completion deficit')
    bound = obs.evaluate('five_scale_minus_deficit', ((5, scale), (-deficit,)))
    require(bound > 0, 'proved deficit bound failed')
    return {'phase_index': m, 'half_angle_index': m + 1, 'denominator_exponent': bits,
            'observer_depth': observer_bits, 'scale': scale, 'scale_squared': str(scale2),
            'tolerance': str(tolerance),
            'half_angle_interval': interval, 'leading_numerators': [a0, a1],
            'floor_certificates': [floor0, floor1], 'deficit': k,
            'minimal_scale_probes': scale_probes,
            'deficit_upper_bound_signed_probe': str(bound)}


def square_table(obs, k, square_limit):
    values = []
    for label in range(square_limit + 1):
        square = integer_observation(obs.evaluate('square_' + str(label), ((label, label),)))
        comparison = obs.add('deficit_minus_square_' + str(label), k, -square)
        if comparison < 0:
            return values, {'status': 'COMPLETE', 'first_excluded_label': label,
                            'first_excluded_square': square,
                            'strict_upper_signed_probe': str(comparison)}
        values.append(square)
    return values, {'status': 'PARTIAL', 'next_square_label': len(values),
                    'reason': 'square-table label limit reached'}


def four_square_search(obs, squares, k, budget, prior=None):
    """Meet observed pair sums with observed complements; no ordinary sqrt."""
    prior = prior or []
    records, lookup = [], {}
    ordinal, used = 0, 0
    for x in range(len(squares)):
        for y in range(x, len(squares)):
            replaying = ordinal < len(prior)
            if not replaying and used >= budget:
                return {'status': 'PARTIAL', 'records': records,
                        'next_pair': [x, y], 'next_pair_ordinal': ordinal,
                        'new_pairs_used': used, 'prefix_pairs_replayed': len(prior),
                        'reason': 'finite observed-pair budget exhausted; no no-solution conclusion'}
            pair_sum = integer_observation(obs.add('pair_sum', squares[x], squares[y]))
            complement = integer_observation(obs.add('pair_complement', k, -pair_sum))
            row = {'ordinal': ordinal, 'labels': [x, y],
                   'observed_pair_sum': pair_sum, 'observed_complement': complement}
            if replaying:
                require(row == prior[ordinal], 'saved pair observation does not replay')
            else:
                used += 1
            records.append(row)
            ordinal += 1
            if complement < 0:
                continue
            lookup.setdefault(pair_sum, (x, y))
            if complement in lookup:
                require(not replaying, 'partial cursor contains an already completed witness')
                witness = [*lookup[complement], x, y]
                observed_total = obs.evaluate('four_square_witness_total', tuple((v, v) for v in witness))
                equality = obs.add('four_square_witness_minus_deficit', observed_total, -k)
                require(equality == 0, 'observed four-square witness failed')
                return {'status': 'COMPLETE', 'records': records, 'witness': witness,
                        'observed_total': str(observed_total), 'equality_observation': str(equality),
                        'new_pairs_used': used, 'prefix_pairs_replayed': len(prior),
                        'matched_pair_observed_value': complement}
    raise AssertionError('complete bounded pair table contradicts four-square theorem')


def route_to_canonical(word):
    """Conjugate indexed native letters by actual adjacent-swap words."""
    output, routing = [], []
    for gate in word:
        labels = list(range(DIM))
        moves = []
        for slot, original in enumerate(gate[1:]):
            position = labels.index(original)
            while position > slot:
                moves.append(('swap', position - 1, position))
                labels[position - 1], labels[position] = labels[position], labels[position - 1]
                position -= 1
        canonical = {'h4': ('h4', 0, 1, 2, 3),
                     'neg': ('neg', 0), 'swap': ('swap', 0, 1)}[gate[0]]
        expansion = (*moves, canonical, *reversed(moves))
        require(all(g in compiler.ALPHABET for g in expansion), 'noncanonical routed letter')
        routing.append({'indexed_letter': list(gate), 'routing_swaps': list(moves),
                        'canonical_letter': list(canonical), 'expanded_length': len(expansion)})
        output.extend(expansion)
    return tuple(output), routing


def build(m, tolerance, pair_budget=5000, square_label_limit=256, previous=None):
    compiler.integer(m, 3)
    tolerance = compiler.rational(tolerance, positive=True)
    compiler.integer(pair_budget)
    compiler.integer(square_label_limit)
    source = source_binding()
    request_base = {'schema': 'DIRECT_FOUR_SQUARE_NATIVE_WORD_GENERAL_V1', 'source': source,
                    'phase_index': m, 'tolerance': str(tolerance), 'dim': DIM}
    previous = previous or {}
    if previous:
        require(previous['status'] == 'PARTIAL' and all(
            previous['request'].get(k) == v for k, v in request_base.items()),
                'resume source, target or status mismatch')
        require(square_label_limit >= previous['limits']['square_label_limit'],
                'resume must retain or increase the square-label budget')
    start = len(CALLS)
    obs = compiler.PositivePathObserver()
    bits, scale, scale_probes = choose_scale(obs, tolerance)
    observer_bits = bits + 4
    request = dict(request_base, denominator_exponent=bits, observer_depth=observer_bits)
    if previous:
        require(previous['request'] == request, 'resume derived scale mismatch')
    normal = construct_leading_normal(obs, m, tolerance, bits, scale, scale_probes)
    squares, square_status = square_table(obs, normal['deficit'], square_label_limit)
    result = {'request': request, 'status': 'PARTIAL',
              'execution_status': 'AUTHOR_ACTUAL_BOUNDED_EXECUTION_NOT_ADMITTED',
              'normal_construction': normal, 'actual_square_table': squares,
              'square_table_status': square_status, 'limits': {'pair_budget': pair_budget,
              'square_label_limit': square_label_limit}, 'old_seed_bank_used': False,
              'target_used_for_propagation': False}
    if square_status['status'] == 'COMPLETE':
        prior = previous.get('four_square_search', {}).get('records', [])
        search = four_square_search(obs, squares, normal['deficit'], pair_budget, prior)
        result['four_square_search'] = search
        if search['status'] == 'COMPLETE':
            vector = tuple(normal['leading_numerators'] + search['witness'] + [0]*(DIM - 6))
            actual_norm = fixed.brc_square_budget(vector)
            norm_difference = obs.add('complete_norm_minus_scale_squared', actual_norm,
                                      -F(normal['scale_squared']))
            require(norm_difference == 0, 'actual complete integer norm failed')
            result['actual_complete_norm'] = {'integer_vector': vector, 'dimension': DIM,
                'observed_norm_squared': str(actual_norm), 'signed_difference': str(norm_difference),
                'executor': 'stage80.fixed_phase.brc_square_budget, actual positive two-edge paths'}
            rotor = fixed.FixedRotor(vector, bits, {'constructor': request['schema']})
            word, routing = route_to_canonical(rotor.inverse_phase_word)
            require(compiler.positive_determinant(word), 'wrong determinant component')
            # This single candidate is freshly constructed; no legacy phase seeds are loaded.
            phase = compiler.compile_phase(m, tolerance, seeds=(word,), pair_budget=1,
                                            observer_start_bits=observer_bits)
            require(phase['status'] == 'CERTIFIED', 'constructive horizon failed strict certificate')
            complete_columns = phase['certificate']['actual_columns']['complete_basis_columns']
            comparisons = []
            for column in complete_columns:
                j = column['source']
                basis = [int(i == j) for i in range(DIM)]
                raw, den = fixed.apply_word(basis, 1, rotor.inverse_phase_word)
                require(tuple(F(x, den) for x in raw) == tuple(
                    F(x, column['denominator']) for x in column['numerators']),
                    'canonical routing changed an actual complete column')
                comparisons.append({'source': j, 'indexed_numerators': raw,
                                    'indexed_denominator': den, 'canonical_exact_equal': True})
            verification = compiler.verify_phase_record(phase)
            result.update(status='CERTIFIED', indexed_rotor=rotor.report(),
                canonical_routing=routing, indexed_vs_canonical_columns=comparisons,
                phase_record=phase, fresh_phase_verification=verification,
                canonical_word_length=len(word), indexed_word_length=len(rotor.inverse_phase_word),
                canonical_alphabet_only=True, all_residual_modes_retained=True)
    result['actual_constructor_observations'] = obs.operations
    result['native_core_calls'] = CALLS[start:]
    result['actual_core_call_count'] = len(CALLS) - start
    return compiler.json_value(result)


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--phase-index', type=int, required=True)
    ap.add_argument('--tolerance', type=str, required=True)
    ap.add_argument('--pair-budget', type=int, default=5000)
    ap.add_argument('--square-label-limit', type=int, default=256)
    ap.add_argument('--resume', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    result = build(args.phase_index, args.tolerance, args.pair_budget,
                   args.square_label_limit, read(args.resume) if args.resume else None)
    payload = compiler.packed(result)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(gzip.compress(payload, mtime=0) if args.out.suffix == '.gz' else payload)
    summary = {'status': result['status'], 'scope': 'one requested actual constructed phase, no Shor execution',
        'old_seed_bank_used': False, 'phase_index': args.phase_index,
        'tolerance': result['request']['tolerance'], 'B': result['request']['denominator_exponent'],
        'observer_depth': result['request']['observer_depth'],
        'deficit': result['normal_construction']['deficit'],
        'leading_numerators': result['normal_construction']['leading_numerators'],
        'actual_core_call_count': result['actual_core_call_count'],
        'constructor_observation_count': len(result['actual_constructor_observations']),
        'observed_pair_count': len(result.get('four_square_search', {}).get('records', [])),
        'four_square_witness': result.get('four_square_search', {}).get('witness'),
        'indexed_word_length': result.get('indexed_word_length'),
        'canonical_word_length': result.get('canonical_word_length'),
        'frobenius_squared_upper': result.get('phase_record', {}).get('certificate', {}).get(
            'error_observer', {}).get('frobenius_squared_upper'),
        'verification': result.get('fresh_phase_verification'),
        'payload_sha256': hashlib.sha256(payload).hexdigest(),
        'artifact': str(args.out.resolve()), 'request': result['request']}
    args.out.with_suffix('').with_suffix('.summary.json').write_text(
        json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    main()
