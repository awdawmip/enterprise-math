"""Native BRC checks for cost-six classification and crossing R2 covers.

The analytic necessity, optimality and arbitrary-cost theorems are in companion
notes. This checks three actual integer trajectories and their complete finite
coverage periods on the pinned native implementation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
import json
from math import gcd, lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_REL = Path('research_notes/portable_direct/riesel_mixed_20261119/certificate.json')
GAP_REL = Path('research_notes/portable_direct/riesel_spectrum_20261121/gap/small_gap_certificate.json')
BASE_BLOB = 'c1909a5e2e209b0f6bd5f613d0f758dde45caee9'
NATIVE_COMMIT = 'b1efc6c805661ed7b476e6e730107da6043176ee'
V9_COMMIT = 'b1de1acbdc97b5e51d486127abd1fadd24babd99'
V = (5, 13, 11, 61, 331)
W = (19, 37, 73, 109)
B = (433, 38737)
L, L2 = 80754838636615, 1354510679787418425415
R1_RESIDUE, R2_RESIDUE = 12926327728523, 602924359709868072943
ORDER2 = {5: 4, 13: 12, 19: 18, 73: 9, 433: 72, 38737: 72,
          181: 180, 631: 45, 23311: 45, 577: 144, 487824887233: 144}
BINARY_ROWS = [(5, 1), (13, 0), (19, 4), (73, 1), (38737, 34),
               (577, 16), (487824887233, 52)]
C_ROWS = [(5, 1), (13, 0), (19, 4), (73, 1), (181, 16),
          (631, 25), (23311, 34)]
CASES = [
    {'label': 'R1_complete_cost_six_minimum',
     'a': 1597463687996365290740241630260436015028835427889255944107518938773290244463,
     'period_n': 2520, 'fiber': 'R1',
     'routes': [{'label': 'six_completion',
                 'rows': [(5, 1), (13, 0), (19, 4), (73, 1), (433, 34), (38737, 16)],
                 'expected_missing': [432, 216, 78, 52, 26, 13, 0]}]},
    {'label': 'R2_compact_binary_cost_seven',
     'a': 142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303,
     'period_n': 5040, 'fiber': 'R2',
     'routes': [{'label': 'binary', 'rows': BINARY_ROWS,
                 'expected_missing': [864, 432, 156, 104, 52, 26, 13, 0]}]},
    {'label': 'R2_same_root_crossing_routes',
     'a': 5638859082119336258239285976823481197493104557616679794390344515886945665210917791971325889059624133,
     'period_n': 5040, 'fiber': 'R2',
     'routes': [{'label': 'modulo_five', 'rows': C_ROWS,
                 'expected_missing': [864, 432, 156, 104, 52, 32, 12, 0]},
                {'label': 'binary', 'rows': BINARY_ROWS,
                 'expected_missing': [864, 432, 156, 104, 52, 26, 13, 0]}]},
]


def blob(data):
    return sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def prime_factors(n):
    result, p = set(), 2
    while p*p <= n:
        while n % p == 0:
            result.add(p)
            n //= p
        p += 1
    if n > 1:
        result.add(n)
    return result


def unsigned_bytes(value):
    return value.to_bytes((value.bit_length()+7)//8, 'big')


def main():
    root = next(p for p in HERE.parents if (p/BASE_REL).is_file())
    source_default = next((p for p in (root/'src', root/'vendor_src')
                           if (p/'enterprise_math/brc_transport.py').is_file()), None)
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path, default=source_default)
    parser.add_argument('--output', type=Path, default=HERE/'native_certificate.json')
    args = parser.parse_args()
    if args.source_dir is None:
        parser.error('Pass --source-dir for the pinned native source directory.')
    base_bytes = (root/BASE_REL).read_bytes()
    assert blob(base_bytes) == BASE_BLOB
    base = json.loads(base_bytes)
    assert base['project_source_commit'] == NATIVE_COMMIT
    source_checks = []
    for filename, expected in base['project_source_blobs'].items():
        observed = blob((args.source_dir/'enterprise_math'/filename).read_bytes())
        assert observed == expected
        source_checks.append({'module': filename, 'git_blob': observed})
    gap = json.loads((root/GAP_REL).read_text())
    astar, M = int(gap['a_star']), int(gap['M'])
    P, H = set(gap['P']), set(gap['H'])
    assert prod(P) == M and len(P) == 20 and len(H) == 36
    assert prod(V+W) == L and prod(V+W+B) == L2
    common29, common31 = sorted(P | set(V+W)), sorted(P | set(V+W+B))
    assert len(common29) == 29 and len(common31) == 31
    assert all(case['a'] % L == R1_RESIDUE for case in CASES)
    assert all((case['a']-CASES[0]['a']) % (M*L) == 0 for case in CASES)
    assert (CASES[2]['a']-CASES[1]['a']) % (M*L2) == 0

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    twice = step.then(step)
    assert step.entries == ((Fraction(1), Affine(((2,),), (1,)), 1),)
    assert twice.entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)

    def evaluate(effect, value):
        (point, weight), = effect.evaluate((value,)).items()
        assert weight.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    reference29, reference31 = {}, {}
    comparisons29 = comparisons31 = 0
    checks = []
    for index, case in enumerate(CASES):
        a, period, routes = case['a'], case['period_n'], case['routes']
        assert a >= astar and a % 2 == 1 and (a-astar) % (6*M) == 0
        is_r2 = case['fiber'] == 'R2'
        if is_r2:
            assert a % L2 == R2_RESIDUE
            assert (a % 433, a % 38737) == (0, 38733)
        all_rows = sorted({row for route in routes for row in route['rows']})
        assert lcm(210, *(ORDER2[q] for q, _ in all_rows)) == period
        for q, c in all_rows:
            order = ORDER2[q]
            assert pow(2, order, q) == 1
            assert all(pow(2, order//p, q) != 1 for p in prime_factors(order))
            assert a*a*pow(4, c, q) % q == 1
        channels = sorted(set(common31) | {q for q, _ in all_rows})
        assert 2*a*a-1 > max(channels)
        route_data = []
        for route in routes:
            rows = route['rows']
            assert len({q for q, _ in rows}) == len(rows)
            route_period = lcm(210, *(ORDER2[q] for q, _ in rows))
            assert period % route_period == 0
            route_data.append({'label': route['label'], 'rows': rows,
                               'coverage_period_n': route_period,
                               'missing': [0]*(len(rows)+1), 'private': {},
                               'prefix_sets': [set(q for q, _ in rows[:t])
                                               for t in range(len(rows)+1)]})
        x = previous_even = a*a-1
        readouts = formula_checks = old_equalities = fiber_equalities = 0
        even_evaluations = 0
        for n in range(1, period+1):
            x = evaluate(step, x)
            assert x == (a*a << n)-1
            if n % 2 == 0:
                assert evaluate(twice, previous_even) == x
                previous_even = x
                even_evaluations += 1
            hits, residues = set(), {}
            for q in channels:
                quotient, (residual,) = euclidean_digits(x, (q,))
                assert quotient*q+residual == x and 0 <= residual < q
                assert residual == (a*a*pow(2, n, q)-1) % q
                readouts += 1
                formula_checks += 1
                residues[q] = residual
                if residual == 0:
                    assert 1 < q < x
                    hits.add(q)
                if q in P:
                    assert residual == (astar*astar*pow(2, n, q)-1) % q
                    old_equalities += 1
                if q in V+W:
                    assert residual == (R1_RESIDUE*R1_RESIDUE*pow(2, n, q)-1) % q
                    fiber_equalities += 1
                if is_r2 and q in B:
                    assert residual == (R2_RESIDUE*R2_RESIDUE*pow(2, n, q)-1) % q
                    fiber_equalities += 1
            vector29 = tuple(residues[q] for q in common29)
            if index == 0:
                reference29[n] = vector29
            elif n in reference29:
                assert vector29 == reference29[n]
                comparisons29 += len(common29)
            if is_r2:
                vector31 = tuple(residues[q] for q in common31)
                if index == 1:
                    reference31[n] = vector31
                else:
                    assert vector31 == reference31[n]
                    comparisons31 += len(common31)
            old_hole = not bool(hits.intersection(P))
            assert old_hole == (n % 2 == 0 and (n//2) % 105 in H)
            for q, c in all_rows:
                assert (q in hits) == (n % ORDER2[q] == 2*c % ORDER2[q])
            if old_hole:
                for route in route_data:
                    for t, prefix in enumerate(route['prefix_sets']):
                        if not hits.intersection(prefix):
                            route['missing'][t] += 1
                    selected_hits = hits.intersection(route['prefix_sets'][-1])
                    if len(selected_hits) == 1:
                        q, = selected_hits
                        route['private'].setdefault(q, n)
        route_records = []
        for original, route in zip(routes, route_data):
            assert route['missing'] == original['expected_missing']
            assert set(route['private']) == {q for q, _ in route['rows']}
            route_records.append({
                'label': route['label'],
                'ordered_rows': [{'q': q, 'phase_u': c, 'order2': ORDER2[q],
                                  'root_residue': a % q} for q, c in route['rows']],
                'coverage_period_n': route['coverage_period_n'],
                'uncovered_counts_over_observed_period': route['missing'],
                'proper_private_old_hole_indices': route['private'],
                'all_assigned_divisors_proper': True,
            })
        checks.append({
            'label': case['label'], 'root': str(a), 'root_digits': len(str(a)),
            'fixed_fiber': case['fiber'], 'observed_period_n': period,
            'readout_channels': channels, 'routes': route_records,
            'native_single_step_updates': period,
            'native_two_step_evaluations': even_evaluations,
            'native_readouts': readouts, 'formula_readout_checks': formula_checks,
            'old_projection_equalities': old_equalities,
            'additional_fixed_fiber_equalities': fiber_equalities,
            'last_native_state_bits': x.bit_length(),
            'last_native_state_sha256_unsigned_big_endian': sha256(unsigned_bytes(x)).hexdigest(),
        })
    crossing_routes = checks[-1]['routes']
    assert crossing_routes[0]['uncovered_counts_over_observed_period'][5:7] == [32, 12]
    assert crossing_routes[1]['uncovered_counts_over_observed_period'][5:7] == [26, 13]
    count_keys = ['native_single_step_updates', 'native_two_step_evaluations',
                  'native_readouts', 'formula_readout_checks',
                  'old_projection_equalities', 'additional_fixed_fiber_equalities']
    result = {
        'schema': 'riesel-finite-observers-and-crossing-routes-native-v1',
        'status': 'AUTHOR_NATIVE_EXECUTION; NOT_INDEPENDENT_REVIEW',
        'native_source_commit': NATIVE_COMMIT, 'native_source_blobs': source_checks,
        'base_certificate_git_blob': BASE_BLOB,
        'reused_mathematical_inputs': {'commit': V9_COMMIT,
            'path': 'research_notes/portable_direct/riesel_five_cover_20261123',
            'scope': 'Old hole predicate, R1 minimum root and rows; new execution compares them with the two R2 roots.'},
        'cases': checks,
        **{key: sum(c[key] for c in checks) for key in count_keys},
        'native_effect_evaluations_total': sum(c['native_single_step_updates']+
                                              c['native_two_step_evaluations'] for c in checks),
        'between_root_R1_29_channel_equalities': comparisons29,
        'between_root_R2_31_channel_equalities': comparisons31,
        'all_future_root_congruences': {
            'all_three_roots_equal_modulo': str(M*L),
            'two_R2_roots_equal_modulo': str(M*L2),
            'proof': 'For equal root residues modulo N, a^2*2^n-1 has the same residue for every n>=0.'},
        'all_future_coverage_bridge': 'The previously proved old-hole predicate has period210 in n. New zero predicates have exact periods ord_q(2). The complete coverage periods are2520,5040 and1260 for the specified routes; the modulo-five route is counted over four complete periods in the common5040 comparison. Residue-value trajectories need not have those smaller periods.',
        'mathematical_scope': 'Native execution proves these concrete trajectories and counts. Complete-six classification, sharp budget-six equality, all-cost observer limitations and lower bounds require the companion written proofs. Dictionary privacy alone is not a total-minimum certificate.',
        'native_scope': 'Fixed X6 anchor and typed integer register; positive singleton BRC weight1 and multiplicity1. The arithmetic index is not physical time, and prime readouts are observations, not axes or extra branches.',
        'observer_scope': 'Finite residue observations retain exact stated congruence scope; the full integer state and joint cofactor relations are retained.'
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'cases': len(checks),
                      **{key: result[key] for key in count_keys},
                      'between_root_R1_29_channel_equalities': comparisons29,
                      'between_root_R2_31_channel_equalities': comparisons31,
                      'output': str(args.output)}))


if __name__ == '__main__':
    main()
