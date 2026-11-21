#!/usr/bin/env python3
"""One requested adaptive endpoint and one new direct-road crosscheck."""
import sys
sys.dont_write_bytecode = True
import argparse
from fractions import Fraction as F
from pathlib import Path
import json
from certify_matched_nodes import (
    DIGITS, SCALE, ZERO, ONE, Y, Z, Elementary, EndpointEngine,
    add, sub, scale, mul, rat, render, make_nodes,
)


def saved_interval(record):
    return F(record['lower']), F(record['upper'])


def intersect_saved(actual, saved):
    lo, hi = saved_interval(saved)
    return max(F(actual[0], SCALE), lo) <= min(F(actual[1], SCALE), hi)


def direct_left_endpoint(engine):
    """Factor products, no weighted-Mobius recurrence, for n <= Y only."""
    m, oracle = engine.m, engine.oracle
    roads = [[ONE] * (Y + 1) for _ in range(m)]
    A, B, G_smoothing = ZERO, ZERO, ZERO
    for n in range(2, Y + 1):
        p = oracle.spf[n]
        quotient = n // p
        D = ZERO
        for j, (a, w) in enumerate(zip(engine.nodes, engine.weights)):
            roads[j][n] = (roads[j][quotient] if quotient % p == 0 else
                           mul(roads[j][quotient], sub(ONE, oracle.prime_powers[p][j])))
            D = add(D, scale(roads[j][n], w / a))
        A = add(A, scale(D, F(1, n)))
        B = add(B, D)
        q = n
        while q % p == 0:
            q //= p
        if q == 1:
            G_smoothing = add(G_smoothing, scale(oracle.elementary.log_integer(p), F(Y, n) - 1))
    center = sub(scale(add(ONE, engine.gamma), Y), scale(oracle.elementary.log_integer(Y), Y))
    value = add(sub(scale(A, Y), B), center)
    target_G = add(G_smoothing, center)
    return A, B, value, target_G


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--node', type=int, choices=(1848, 24648), default=1848)
    args = parser.parse_args()
    directory = Path(__file__).parent
    original = json.loads((directory / 'rational_window_certificate.json').read_text())
    elementary = Elementary()
    nodes, weights, certificate = make_nodes(elementary)
    assert certificate['nodes'] == original['node_certificate']['nodes']
    assert certificate['weights'] == original['node_certificate']['weights']
    engine = EndpointEngine(nodes, weights, elementary)
    adaptive = engine.endpoint(args.node)
    direct_report = None
    if args.node == 1848:
        A, B, left, target_G = direct_left_endpoint(engine)
        old_left = next(row for row in original['endpoints'] if row['N'] == Y)
        assert intersect_saved(A, old_left['A_D_excluding_unit'])
        assert intersect_saved(B, old_left['B_D_excluding_unit'])
        assert intersect_saved(left, old_left['F'])
        error = sub(left, target_G)
        coefficient = F(certificate['derivative_error_coefficient_exact'])
        # A sharper Y-local version of the already-proved interpolation bridge.
        logY = elementary.log_integer(Y)
        power = ONE
        for _ in range(engine.m + 2):
            power = mul(power, logY)
        bound = scale(power, coefficient * Y)
        assert max(abs(error[0]), abs(error[1])) <= bound[1]
        direct_report = {
            'N': Y, 'all_integer_population': Y - 1,
            'method': 'original prime-factor products for every road, independent of the weighted-Mobius summation route',
            'F': render(left), 'A_D': render(A), 'B_D': render(B),
            'target_G_via_Lambda': render(target_G), 'F_minus_G': render(error),
            'Y_local_absolute_bridge_bound': render(bound),
            'agrees_with_all_saved_F_A_B_intervals': True,
        }
    selection = ('1848=floor((1296+2401)/2), selected from the global-eta local budget'
                 if args.node == 1848 else
                 '24648=floor((20736+28561)/2), selected after replacing eta_Z by the sharper cell-local eta_v')
    report = {
        'status': ('EXACT_ADAPTIVE_ENDPOINT_AND_DIRECT_MATCHED_ROAD_CHECK_PASSED'
                   if direct_report is not None else 'EXACT_LOCALIZED_ADAPTIVE_ENDPOINT_PASSED'),
        'same_node_and_weight_certificate': 'rational_window_certificate.json',
        'adaptive_selection': selection,
        'endpoint': adaptive,
        'direct_left_crosscheck': direct_report,
        'counts': {'sieve_cutoff': engine.oracle.base, 'M_states_above_cutoff': len(engine.cache),
                   'recursion_blocks': engine.recursion_blocks,
                   'endpoint_blocks': engine.endpoint_blocks,
                   'exp_evaluations': elementary.exp_calls},
        'scope': ['Only the requested additional endpoint is recomputed in this invocation; the ten-point sweep is not rerun.',
                  'The direct Y crosscheck was performed only for the 1848 invocation and is not repeated for the localized addition.',
                  'The Lambda sum is only an independent comparison target, not a replacement for the road inputs.',
                  'No infinite-window energy claim is inferred from this finite certificate.'],
    }
    filename = 'adaptive_point_certificate.json' if args.node == 1848 else 'localized_point_certificate.json'
    (directory / filename).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'N': adaptive['N'], 'F': adaptive['F'],
                      'direct_crosscheck_performed': direct_report is not None,
                      'counts': report['counts']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
