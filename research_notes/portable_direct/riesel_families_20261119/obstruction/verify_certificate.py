#!/usr/bin/env python3
"""Verify the fixed-root 258-new-prime obstruction using exact integers.

Default: recompile/run the GMP engine for every certified round, and cross-check
the final packets q <= 64 plus q = 257 with an independent pure-Python routine.
Use --backend python for a slow, entirely Python integer recomputation of all
packets; no primality/factorization package or probabilistic test is required.

This is author-side research checking, not independent project Review.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import subprocess
import sys
import time


def prime_divisors(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result


def prove_prime(p):
    assert p >= 2
    assert all(p % d for d in range(2, isqrt(p) + 1))
    return {'p': p, 'trial_division_through': isqrt(p),
            'all_integer_trial_divisors_tested': True}


def prove_order_two(p, order, factors=None):
    if factors is not None:
        assert prod(r**e for r, e in factors) == order
        assert len({r for r, _ in factors}) == len(factors)
        assert all(e >= 1 for _, e in factors)
        for r, _ in factors:
            prove_prime(r)
        divisors = [r for r, _ in factors]
    else:
        divisors = prime_divisors(order)
    assert pow(2, order, p) == 1
    witnesses = {str(r): pow(2, order // r, p) for r in divisors}
    assert all(x != 1 for x in witnesses.values())
    return witnesses


def packet_python(A, m, q):
    """Independent filter: remove every proper-divisor order, not just q/r."""
    C = A**q - 1
    G = gcd(C, pow(2, m*q, C) - 1)
    H = G
    # The engine uses only q/r with r prime. This uses all proper divisors.
    for d in range(1, q):
        if q % d:
            continue
        while H > 1:
            common = gcd(H, pow(2, m*d, H) - 1)
            if common == 1:
                break
            H //= common
    return {'q': q, 'G': str(G), 'E': str(H)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    base = Path(__file__).resolve().parent
    parser.add_argument('--input', type=Path, default=base/'certificate.json')
    parser.add_argument('--output', type=Path, default=base/'verification_results.json')
    parser.add_argument('--backend', choices=['gmp', 'python'], default='gmp')
    parser.add_argument('--python-crosscheck-limit', type=int, default=64)
    parser.add_argument('--source-dir', type=Path, default=base.parent/'vendor_src')
    args = parser.parse_args()
    start = time.monotonic()
    data = json.loads(args.input.read_text())
    assert data['schema'] == 'RIESEL_FIXED_ROOT_FACTOR_FREE_COPRIME_CERTIFICATE_V4'
    a = int(data['a'])
    A = int(data['A'])
    m0 = int(data['initial_m'])
    m = int(data['final_m'])
    bound = data['bound']
    assert a == 690786768637635218740714348513373826260012289
    assert A == a*a*2**66 and data['n_initial'] == 66
    assert m0 == 1260 * 11**2 * 37 == 5641020
    assert m % m0 == 0 and m % 1260 == 0 and bound == 256
    assert data['complete'] is True

    # Actual positive singleton BRC arithmetic, on the inherited fixed anchor.
    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits
    step = EffectHistogram.from_terms(1, [(1, Affine(((4,),), (3,)), 1)])

    def native_evaluate(packet, x):
        (point, weight), = packet.evaluate((x,)).items()
        assert weight.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    state = a*a - 1
    for _ in range(33):
        state = native_evaluate(step, state)
    assert state + 1 == A

    binary = base/'period_packets'
    if args.backend == 'gmp':
        subprocess.run(['g++', '-O2', '-std=c++17', str(base/'period_packets.cpp'),
                        '-lgmpxx', '-lgmp', '-o', str(binary)], check=True)

    def recompute(step_m, first, last):
        if args.backend == 'python':
            return [packet_python(A, step_m, q) for q in range(first, last+1)]
        output = subprocess.run([str(binary), str(step_m), str(last), str(first)],
                                check=True, capture_output=True, text=True).stdout
        rows = [{'q': int(q), 'G': G, 'E': E}
                for q, G, E in (line.split() for line in output.splitlines())]
        assert [row['q'] for row in rows] == list(range(first, last+1))
        return rows

    rounds_verified = []
    expected_m = m0
    for index, round_data in enumerate(data['rounds'], 1):
        step_m = int(round_data['m'])
        assert step_m == expected_m
        rows = recompute(step_m, 1, bound)
        assert rows == round_data['packets']
        active = [row for row in rows if int(row['E']) > 1]
        assert round_data['obstacles'] == []
        assert all(gcd(int(row['E']), A-1) == 1 for row in active)
        multiplier = lcm(*(row['q'] for row in active)) if active else 1
        assert multiplier == int(round_data['multiplier'])
        expected_m = step_m * multiplier
        rounds_verified.append({'round': index, 'm': str(step_m),
                                'active_periods': [row['q'] for row in active],
                                'multiplier': str(multiplier),
                                'all_packets_verified': True})
        print(f'round {index}: checked q=1..{bound}, '
              f'{len(active)} active packets', flush=True)
    assert expected_m == m
    assert all(row['E'] == '1' for row in data['rounds'][-1]['packets'])

    final_packets = data['final_packets']
    assert [row['q'] for row in final_packets] == list(range(1, 258))
    assert final_packets[:256] == data['rounds'][-1]['packets']
    assert recompute(m, 257, 257) == final_packets[256:]

    crosschecked = []
    if args.backend == 'gmp':
        requested = set(range(1, min(256, args.python_crosscheck_limit)+1)) | {257}
        for q in sorted(requested):
            assert packet_python(A, m, q) == final_packets[q-1]
            crosschecked.append(q)
    print('final dictionary and independent integer cross-check passed', flush=True)

    old_proofs = []
    P = set()
    for row in data['original_twenty_channels']:
        p = row['p']
        assert p not in P
        P.add(p)
        prove_prime(p)
        prove_order_two(p, row['order'])
        assert a % p == row['a_residue']
        assert (a*a*pow(2, row['exponent_phase'], p)-1) % p == 0
        q = row['order'] // gcd(row['order'], m)
        R_mod = pow(2, m, p)
        residues = [(A*pow(R_mod, w, p)-1) % p for w in range(q)]
        assert residues and all(residues)
        old_proofs.append({'p':p, 'relative_order':q,
                           'entire_cycle_nonzero': True})
    assert len(P) == 20

    channels = data['period_257_channels']
    G257 = int(final_packets[-1]['G'])
    E257 = int(final_packets[-1]['E'])
    assert G257 == E257 == prod(row['p'] for row in channels)
    assert len(channels) == 2 and {row['p'] for row in channels} == {2143381,48324739}
    channel_proofs = []
    for row in channels:
        p, order = row['p'], row['order_two']
        primality = prove_prime(p)
        order_witnesses = prove_order_two(p, order, row['order_two_factorization'])
        assert order // gcd(order, m) == row['relative_order'] == 257
        A_mod, R_mod = A % p, pow(2, m, p)
        assert A_mod == row['A_residue'] and R_mod == row['R_residue']
        assert pow(R_mod, 257, p) == 1 and R_mod != 1
        phases = [w for w in range(257) if (A_mod*pow(R_mod, w, p)-1) % p == 0]
        assert phases == [row['phase']]
        projected_step = EffectHistogram.from_terms(
            1, [(1, Affine(((R_mod,),), (R_mod-1,)), 1)])
        native_residue = euclidean_digits(native_evaluate(projected_step, A-1), (p,))[1][0]
        assert native_residue == (A_mod*R_mod-1) % p
        channel_proofs.append({**row, 'primality':primality,
                                'order_test_witnesses':order_witnesses,
                                'unique_phase_verified':True,
                                'native_projected_update_verified':True})

    # All d<=256 common-divisor channels are absent. For d=257 only the
    # endpoints (w=1,w=258) occur in the specified finite window.
    endpoint_residue = (A*pow(2, m, G257)-1) % G257
    endpoint_gcd = gcd(G257, endpoint_residue)
    assert endpoint_gcd == 1
    window = data['pairwise_coprime_window']
    assert window == {'w_first':1, 'w_last':258, 'count':258,
                      'max_difference':257, 'exceptional_endpoint_gcd':'1'}
    density = Fraction(2,257) + Fraction(255,258)
    assert density == Fraction(22017,22102) < 1
    assert data['density_bound_for_257_new_primes'] == {
        'numerator':density.numerator,'denominator':density.denominator}
    assert data['cover_lower_bound_outside_old_twenty'] == 258
    assert data['cover_lower_bound_if_retaining_old_twenty'] == 278

    obstruction = next(row for row in channels if row['p'] == 48324739)
    assert (A-1) % obstruction['p'] == 0
    assert obstruction['relative_order'] == 257
    # Any further unshifted refinement m'=mL gives p relative order
    # 257/gcd(257,L), equal to 257 or 1, with phase zero in either case.
    result = {
        'schema':'RIESEL_FIXED_ROOT_FACTOR_FREE_COPRIME_VERIFIED_V4',
        'researcher_id':data['researcher_id'],'activity_id':data['activity_id'],
        'all_assertions_passed':True,'backend':args.backend,
        'integer_rounds_verified':rounds_verified,
        'independent_python_final_periods':crosschecked,
        'fixed_X6_anchor':'unchanged; one internal integer register',
        'native_BRC':'positive singleton x -> 4x+3; final modular projections checked',
        'a':str(a),'A':str(A),'n_initial':66,'n_step':str(m),
        'old_prime_channels':old_proofs,
        'exact_dictionary_range':[1,257],
        'empty_exact_periods':[1,256],
        'period_257_channels':channel_proofs,
        'pairwise_coprime_terms':{'indices':[1,258],'count':258,
            'formula':'a^2 * 2^(66 + m*w) - 1',
            'max_index_difference':257,'endpoint_G257_residue':str(endpoint_residue),
            'endpoint_gcd':endpoint_gcd,'all_escape_old_twenty':True,
            'all_composite':'(a*2^(33+(m/2)*w)-1)*(a*2^(33+(m/2)*w)+1)'},
        'density_of_257_best_possible_channels_upper':str(density),
        'positive_uncovered_density_lower':str(1-density),
        'any_finite_cover_new_primes_lower_bound':258,
        'if_old_twenty_retained_total_lower_bound':278,
        'unshifted_refinement_uniform_period_threshold_maximum':257,
        'scope':'finite lower bound; no assertion of no finite cover, no unbounded lpf assertion, no optimality of 258',
        'verification_status':data['provenance']['verification_status'],
        'elapsed_seconds':time.monotonic()-start,
    }
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_assertions_passed':True,'new_primes_lower_bound':258,
                      'pairwise_coprime_composite_terms':258,
                      'elapsed_seconds':round(result['elapsed_seconds'],3)}),flush=True)


if __name__ == '__main__':
    main()
