"""Declared bounded actual-integer checks; no ideal phase/reference execution."""
from pathlib import Path
import gzip
import hashlib
import json
import time

from typed_floor_moments import TypedFloorMoments, DEGREES
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
MOMENT_CASES = ((0, 1, 0, 0), (1, 1, -3, -2), (7, 5, 3, -4),
                (6, 7, -5, 9), (8, 3, 11, -13), (5, 11, 0, -23),
                (9, 13, 2, 1), (7, 5, 3, 8))
WEIGHT_CASES = ((2, 4, 4, 5, 1, 1), (4, 1, 2, 6, 5, -1),
                (1, 4, 2, 3, 0, 1), (2, 4, 2, 1, 0, -1))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def brute_moments(args):
    n, m, a, b = args
    runner = TypedFloorMoments()
    output = {(p, e): 0 for p, e in DEGREES}
    points = []
    for j in range(n):
        affine = runner.add(runner.mul(a, j), b)
        value, remainder = runner.floor_div(affine, m)
        reconstructed = runner.add(runner.mul(m, value), remainder)
        assert reconstructed == affine and 0 <= remainder < m
        points.append({'j': j, 'affine': affine, 'floor': value, 'remainder': remainder})
        for p, e in DEGREES:
            term = runner.mul(runner.small_power(j, p), runner.small_power(value, e))
            output[p, e] = runner.add(output[p, e], term)
    return output, {'points': points, 'actual_integer_evidence': runner.evidence()}


def brute_weight(args):
    H, V, P, R, r, d = args
    runner = TypedFloorMoments()
    S = runner.mul(V, P)
    vd = runner.mul(V, d)
    answer, rows = 0, []
    for A in range(H):
        for Ap in range(H):
            for y in range(V):
                for yp in range(V):
                    left = runner.add(runner.mul(S, A), y)
                    right = runner.add(runner.mul(S, Ap), yp)
                    difference = runner.sub(runner.add(runner.sub(right, left), vd), r)
                    _, residue = runner.floor_div(difference, R)
                    hit = residue == 0
                    if hit:
                        answer = runner.add(answer, 1)
                    rows.append({'A': A, 'Ap': Ap, 'y': y, 'yp': yp,
                                 'difference': difference, 'residue': residue, 'hit': hit})
    return answer, {'pair_tests': rows, 'actual_integer_evidence': runner.evidence()}


def main():
    started = time.perf_counter()
    sources = {name: sha(ROOT/name) for name in ('typed_floor_moments.py', 'check_typed_floor_moments.py')}
    output = {'status': 'RUNNING', 'source_sha256': sources,
              'scope': 'bounded actual integer counting; no quantum phase or order discovery',
              'moment_cases': [], 'weight_cases': [], 'negative_checks': []}
    optimized_digits = brute_digits = 0
    for args in MOMENT_CASES:
        runner = TypedFloorMoments()
        actual = runner.moments(*args)
        explicit, enumeration = brute_moments(args)
        assert actual == explicit
        evidence = runner.evidence()
        optimized_digits += evidence['arithmetic_stats']['adder_digit_replays']
        brute_digits += enumeration['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        output['moment_cases'].append({'inputs': args,
            'values': {f'{p},{e}': actual[p, e] for p, e in DEGREES},
            'all_ten_equal': True, 'recurrence': evidence, 'enumeration': enumeration})
    for args in WEIGHT_CASES:
        runner = TypedFloorMoments()
        actual = runner.window_weight(*args)
        explicit, enumeration = brute_weight(args)
        assert actual == explicit
        evidence = runner.evidence()
        optimized_digits += evidence['arithmetic_stats']['adder_digit_replays']
        brute_digits += enumeration['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays']
        output['weight_cases'].append({'inputs': args, 'value': actual, 'equal': True,
                                      'recurrence': evidence, 'enumeration': enumeration})
    invalid = [('moments', (-1, 3, 1, 0)), ('moments', (3, 0, 1, 0)),
               ('moments', (True, 3, 1, 0)), ('moments', (3, 5, 1.0, 0)),
               ('window_weight', (0, 2, 2, 3, 0, 0)),
               ('window_weight', (2, 2, 2, 0, 0, 0)),
               ('window_weight', (2, 2, 2, 3, 3, 0)),
               ('window_weight', (2, 2, 2, 3, 0, 2)),
               ('window_weight', (2, 2, True, 3, 0, 0))]
    for method, args in invalid:
        runner = TypedFloorMoments()
        try:
            getattr(runner, method)(*args)
        except ValueError as error:
            assert not runner.arithmetic.operations
            output['negative_checks'].append({'method': method, 'inputs': args,
                                              'rejected': True, 'error': str(error),
                                              'typed_operations': 0})
        else:
            raise AssertionError('invalid input accepted')
    assert sources == {name: sha(ROOT/name) for name in sources}
    output.update(status='PASS', actual_core_call_count=len(CALLS), actual_core_calls=CALLS,
        optimized_adder_digit_replays=optimized_digits,
        explicit_enumeration_adder_digit_replays=brute_digits,
        elapsed_seconds=time.perf_counter()-started)
    raw = json.dumps(output, sort_keys=True, separators=(',', ':')).encode()+b'\n'
    target = ROOT/'TYPED_FLOOR_MOMENT_RESULTS.json.gz'
    assert not target.exists(), 'do not overwrite frozen evidence'
    target.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
    summary = {'status': 'PASS', 'source_sha256': sources, 'moment_cases': len(MOMENT_CASES),
        'moment_scalar_equalities': len(MOMENT_CASES)*len(DEGREES),
        'weight_cases': len(WEIGHT_CASES), 'weight_values': [x['value'] for x in output['weight_cases']],
        'explicit_weight_pair_tests': sum(len(x['enumeration']['pair_tests']) for x in output['weight_cases']),
        'negative_checks': len(invalid), 'actual_core_call_count': len(CALLS),
        'optimized_adder_digit_replays': optimized_digits,
        'explicit_enumeration_adder_digit_replays': brute_digits,
        'maximum_recursion_depth': max(x['recurrence']['stats']['max_recursion_depth']
                                       for x in output['moment_cases']+output['weight_cases']),
        'maximum_integer_bits': max(x['recurrence']['stats']['max_observed_integer_bits']
                                   for x in output['moment_cases']+output['weight_cases']),
        'elapsed_seconds': output['elapsed_seconds'], 'raw_bytes': len(raw),
        'gzip_bytes': target.stat().st_size, 'payload_sha256': hashlib.sha256(raw).hexdigest(),
        'artifact_sha256': sha(target), 'artifact': str(target),
        'quantum_phase_propagation_performed': False, 'order_discovery_performed': False,
        'full_active_window_gamma_integration_performed': False,
        'resource_scope': 'digit counts exclude host metadata, receipt serialization and general bit-operation internals'}
    (ROOT/'TYPED_FLOOR_MOMENT_SUMMARY.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary))


if __name__ == '__main__':
    main()
