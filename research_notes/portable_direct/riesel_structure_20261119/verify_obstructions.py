"""Exact bounded-period dictionaries and arbitrary-size supplement obstruction.

The coefficient is the 45-digit root from the previous research round.
This proves that extending its specified 20-prime cover to all exponents,
if possible, requires at least 19 additional distinct primes of any size.
It also exhausts every prime whose even-index order divides 105.

No probabilistic primality or unbounded non-cover claim is used. Proposed
factorizations are input certificates; all factors are proved by trial
division and products are checked against independently computed integers.
The actual orbit uses a positive singleton BRC affine packet. Its arithmetic
register is internal to an unchanged X6 anchor, not an added spatial axis.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd, isqrt, prod
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parents[3] / 'src')
    parser.add_argument('--input', type=Path, default=Path(__file__).with_name('theory_certificate.json'))
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('theory_results.json'))
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits

    even_step = EffectHistogram.from_terms(1, [(1, Affine(((4,),), (3,)), 1)])
    four = EffectHistogram.from_terms(1, [(1, Affine(((4,),), (0,)), 1)])

    def advance(packet, x):
        out = packet.evaluate((x,))
        (point, weights), = out.items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    def rem(x, p):
        return euclidean_digits(x, (p,))[1][0]

    prime_proofs = {}

    def prove_prime(p):
        if p not in prime_proofs:
            assert p >= 2
            bound = isqrt(p)
            assert all(rem(p, divisor) for divisor in range(2, bound + 1))
            prime_proofs[p] = {'p': p, 'trial_bound': bound,
                               'every_integer_divisor_2_through_bound_tested': True}

    def verify_factorization(value, factors):
        assert len({p for p, _ in factors}) == len(factors)
        assert all(e >= 1 for _, e in factors)
        for p, _ in factors:
            prove_prime(p)
        assert prod(p**e for p, e in factors) == value

    def first_return(packet, p, return_bound):
        current = 1
        for q in range(1, return_bound + 1):
            current = rem(advance(packet, current), p)
            if current == 1:
                return q
        raise AssertionError('provided return bound does not close the orbit')

    a = int(data['a'])
    k = a * a
    # Specialization of the proved positive-binomial criterion: every
    # valuation of a square is even, and v_3(k)=2 forces their gcd to be 2.
    assert a % 9 == 6 and k % 27 == 9
    rows = data['original_twenty_channels']
    old_primes = {row['p'] for row in rows}
    assert len(old_primes) == 20
    period = data['same_period']['u_period']
    assert period == 105
    # Even-order 2-channels have odd n phase and are absent on n=2u.
    # All the remaining orders divide 105, proving this short hole period.
    for row in rows:
        assert a % row['p'] == row['a_residue']
        assert (k * pow(2, row['exponent_phase'], row['p']) - 1) % row['p'] == 0
        if row['order'] % 2 == 0:
            assert row['exponent_phase'] % 2 == 1
        else:
            assert period % row['order'] == 0
    H = [u for u in range(period)
         if not any((2 * u) % row['order'] == row['exponent_phase'] for row in rows)]
    assert len(H) == 36

    same = data['same_period']
    value = 1
    for _ in range(period):
        value = advance(four, value)
    value -= 1
    assert value == int(same['four_power_minus_one']) == 4**105 - 1
    verify_factorization(value, same['factorization'])
    dictionary = []
    covered = set()
    for p, exponent in same['factorization']:
        order = first_return(four, p, period)
        current = rem(k - 1, p)
        phases = []
        for u in range(order):
            if current == 0:
                phases.append(u)
            current = rem(advance(even_step, current), p)
        assert current == rem(k - 1, p) and len(phases) <= 1
        hits = [h for h in H if phases and h % order == phases[0]]
        covered.update(hits)
        dictionary.append({'p': p, 'factor_exponent': exponent, 'ord_p_4': order,
                           'phase_u': phases[0] if phases else None,
                           'hole_classes_hit': hits,
                           'already_in_old_P': p in old_primes})
    remaining = sorted(set(H) - covered)
    assert len(covered) == 16 and len(remaining) == 20
    assert {r['p'] for r in dictionary if r['hole_classes_hit']} == {11, 43, 211}
    hits_by_11 = next(set(r['hole_classes_hit']) for r in dictionary if r['p'] == 11)
    hits_by_43 = next(set(r['hole_classes_hit']) for r in dictionary if r['p'] == 43)
    hits_by_211 = next(set(r['hole_classes_hit']) for r in dictionary if r['p'] == 211)
    assert hits_by_211 <= hits_by_11
    assert hits_by_11 | hits_by_43 == covered

    fibre = data['deep_fibre']
    h, step = fibre['u_initial'], fibre['u_step']
    assert h == 33 and step == 630 and h in H and step % period == 0
    assert fibre['n_initial'] == 2 * h == 66
    assert fibre['n_step'] == 2 * step == 1260
    N0 = k - 1
    for _ in range(h):
        N0 = advance(even_step, N0)
    A = N0 + 1
    R = 1
    sampled = EffectHistogram.unit(1)
    for _ in range(step):
        R = advance(four, R)
        sampled = sampled.then(even_step)
    assert A == int(fibre['A']) == k * 4**h
    assert R == int(fibre['R']) == 4**step
    assert advance(sampled, 0) == R - 1
    assert advance(sampled, 1) == 2 * R - 1
    multiplier = EffectHistogram.from_terms(1, [(1, Affine(((R,),), (0,)), 1)])

    # Check every old channel along its full sampled orbit, and preserve the
    # independent proof from h mod 105 and 630 being a multiple of 105.
    old_fibre_proofs = []
    for row in rows:
        p = row['p']
        e = row['order'] // gcd(row['order'], 2)
        q = e // gcd(e, step)
        assert first_return(multiplier, p, q) == q
        current = rem(N0, p)
        cycle = []
        for _ in range(q):
            cycle.append(current)
            current = rem(advance(sampled, current), p)
        assert current == cycle[0] and all(cycle)
        old_fibre_proofs.append({'p': p, 'sampled_period': q, 'nonzero_residue_cycle': cycle})

    certificates = fibre['gcd_certificates']
    bound = fibre['period_dictionary_bound']
    assert bound == 20 and [r['q'] for r in certificates] == list(range(1, bound + 1))
    q_dictionary = []
    selected = []
    for cert in certificates:
        q = cert['q']
        G = gcd(A**q - 1, R**q - 1)
        assert G == int(cert['gcd'])
        verify_factorization(G, cert['factorization'])
        factors = []
        for p, exponent in cert['factorization']:
            actual_q = first_return(multiplier, p, q)
            assert q % actual_q == 0 and rem(pow(R, q, p), p) == 1
            matched = actual_q == q
            phase = None
            if matched:
                current = rem(N0, p)
                zeroes = []
                for v in range(q):
                    if current == 0:
                        zeroes.append(v)
                    current = rem(advance(sampled, current), p)
                assert len(zeroes) == 1 and current == rem(N0, p)
                phase = zeroes[0]
                assert p not in old_primes
                selected.append({'p': p, 'q': q, 'phase_v': phase})
            factors.append({'p': p, 'exponent': exponent, 'actual_order_R': actual_q,
                            'exact_q_channel': matched, 'phase_v': phase})
        q_dictionary.append({'q': q, 'gcd': str(G), 'factorization_and_orders': factors})
    assert selected == [
        {'p': 23, 'q': 11, 'phase_v': 1},
        {'p': 89, 'q': 11, 'phase_v': 9},
        {'p': 53, 'q': 13, 'phase_v': 6},
        {'p': 3061, 'q': 17, 'phase_v': 9},
        {'p': 761, 'q': 19, 'phase_v': 5},
    ]

    # All other active prime channels have q>=21. Each hits density 1/q.
    # The five listed densities are each >1/21, so selecting all five gives
    # a universal upper bound even if a proposed 18-prime supplement omits
    # some of them. Overlaps can only decrease the covered density.
    small_mass = sum((Fraction(1, r['q']) for r in selected), start=Fraction(0))
    maximum_channels = 18
    upper = small_mass + Fraction(maximum_channels - len(selected), bound + 1)
    assert small_mass == Fraction(17099, 46189)
    assert upper == Fraction(959536, 969969) < 1
    gap = 1 - upper
    assert gap == Fraction(10433, 969969)

    deep_primes = {p for cert in certificates for p, _ in cert['factorization']}
    output = {
        'schema': 'RIESEL_PERIOD_DICTIONARY_OBSTRUCTIONS_V1',
        'researcher_id': data['researcher_id'], 'activity_id': data['activity_id'],
        'status': 'AUTHOR_PROOF_AND_EXACT_FINITE_CERTIFICATE; NOT_INDEPENDENT_REVIEW',
        'a': str(a), 'k': str(k),
        'previous_science_commit': data['previous_science_commit'],
        'project_arithmetic_source_commit': data['project_arithmetic_source_commit'],
        'positive_binomial_specialization': {
            'root_mod_9': a % 9, 'coefficient_v3': 2,
            'gcd_of_coefficient_prime_valuations': 2,
            'proof': 'All valuations are even because k=a^2; v_3(k)=2 bounds their gcd by 2.',
            'rational_polynomial_reducible_iff': 'n is even',
            'integer_value_primality_is_a_different_question': True,
        },
        'brc_entrypoints': ['EffectHistogram.from_terms', 'EffectHistogram.unit',
                           'EffectHistogram.then', 'EffectHistogram.evaluate', 'euclidean_digits'],
        'same_period': {
            'u_period': period, 'old_holes_H': H,
            'complete_candidate_integer': str(value),
            'candidate_dictionary': dictionary,
            'newly_covered_H': sorted(covered), 'remaining_H': remaining,
            'effective_supplement': [11, 43],
            'remaining_density_among_all_positive_n': str(Fraction(len(remaining), 2*period)),
            'scope': 'Every odd prime with ord_p(4) dividing 105, with no bound on prime size; completeness follows from prime divisors of 4^105-1.',
        },
        'deep_fibre': {
            'n': '66+1260*v', 'v_domain': 'nonnegative integers',
            'u': '33+630*v', 'A': str(A), 'R': str(R),
            'N_formula': 'A*R^v-1',
            'proper_algebraic_factorization': '(a*2^(33+630*v)-1)*(a*2^(33+630*v)+1)',
            'old_prime_fibre_checks': old_fibre_proofs,
            'exact_period_dictionary_max_q': bound,
            'complete_gcd_certificates': q_dictionary,
            'all_active_prime_channels_q_at_most_20': selected,
            'maximum_prime_in_gcd_factorizations': max(deep_primes),
            'maximum_trial_division_bound_in_gcd_factorizations': isqrt(max(deep_primes)),
            'remaining_active_channel_period_lower_bound': bound + 1,
            'density_bound_for_18_arbitrary_additional_primes': str(upper),
            'uncovered_density_lower_bound_on_v_for_18': str(gap),
            'minimum_number_of_additional_distinct_primes': 19,
            'minimum_total_if_all_twenty_old_primes_retained': 39,
            'quantifier_scope': 'All primes of arbitrary size; bound concerns finite extensions of the fixed old 20-prime dictionary. It does not prove absence of every finite cover.',
        },
        'primality_certificates': [prime_proofs[p] for p in sorted(prime_proofs)],
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'output': str(args.output), 'same_period_holes': len(remaining),
                      'fibre': output['deep_fibre']['n'], 'small_period_channels': selected,
                      '18_channel_upper_density': str(upper),
                      'additional_prime_lower_bound': 19}, ensure_ascii=False))


if __name__ == '__main__':
    main()
