#!/usr/bin/env python3
"""Exact cost-eight construction in the fixed 43-prime observation fiber.

This arithmetic calculator is self-contained.  The inherited all-seven-cover
classification supplies the global lower bound; this file verifies every new
prime, phase, CRT progression, private witness and fixed-observer condition.
"""
from __future__ import annotations

import argparse
from itertools import combinations, product
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path

P = (7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417)
A_STAR = 690786768637635218740714348513373826260012289
M = 1397394912916194098609132326092145093313722687204526281
L = 80754838636615
A2 = 9807947978443488306255509703402695727949968778703073231931137913705883712843
S2 = 11356718000553566643685496313583434507970452519839503606327232707476034989690
OBSERVERS = (181, 577, 631, 23311, 54001, 87211, 246241, 262657, 279073,
             18837001, 29247661, 487824887233)
T = 35095524795781473254136196580356738045833417602831290421525609131
RT = 21450781839625171583347380029424471704699683386785900439176732195
NEW_PRIMES = (33975937, 138991501037953)
INACTIVE = (3, 11, 37, 61, 109, 331, 433, 181, 577, 631, 23311,
            54001, 87211, 262657, 279073, 18837001, 29247661)
OLD_WITNESSES = (37, 3, 89, 5, 293, 117, 413, 113, 41, 33, 87, 233, 773,
                 207, 237, 257, 53, 593, 63, 111)
PREFIX = (5, 13, 19, 73)
PREFIX_WITNESSES = (6, 12, 152, 20)
HOLES_B = {0, 3, 5, 8, 10, 15, 21, 23, 26, 28, 30, 31, 33}


def prime_trial(n: int) -> bool:
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def crt(pairs: list[tuple[int, int]]) -> tuple[int, int]:
    root, modulus = 0, 1
    for residue, new_modulus in pairs:
        assert gcd(modulus, new_modulus) == 1
        root += modulus * ((residue - root) * pow(modulus, -1, new_modulus) % new_modulus)
        modulus *= new_modulus
    return root, modulus


def root_phase(q: int, b: int) -> int:
    return pow(pow(2, 16 + 18 * b, q), -1, q)


def prime_divisors(n: int) -> list[int]:
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def order2(q: int) -> int:
    order = q - 1
    for factor in prime_divisors(order):
        while order % factor == 0 and pow(2, order // factor, q) == 1:
            order //= factor
    return order


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('cost_eight_certificate.json'))
    parser.add_argument('--coprimalized-example', action='store_true',
                        help='Also compute a full exact-total-cost root; the existence proof does not need this optional large integer.')
    args = parser.parse_args()
    assert prod(P) == M and prod(OBSERVERS) == T
    assert crt([(A_STAR, 6*M), (12926327728523, L), (0, 433), (38733, 38737)]) == (A2, S2)
    assert gcd(S2, T) == 1
    A3, S3 = crt([(A2, S2), (RT, T)])
    assert S3 == S2*T and 0 < A3 < S3
    fixed = {q: A3 % q for q in P + PREFIX + (11, 61, 331, 37, 109, 433, 38737) + OBSERVERS}
    assert len(fixed) == 43
    assert all(A3 % q == 0 for q in INACTIVE)
    assert A3 % 246241 == 182629 and A3 % 487824887233 == 487823838657
    assert A3 % 38737 == 38733
    for q, b in ((38737, 1), (246241, 1), (487824887233, 2)):
        assert A3 % q == root_phase(q, b)

    # Deterministic elementary primality and exact orders, including all factors
    # of the particular cyclotomic value used for the construction.
    assert prod(NEW_PRIMES) == 2**72 - 2**36 + 1
    assert all(prime_trial(q) for q in NEW_PRIMES)
    assert all(pow(2, 216, q) == 1 and pow(2, 108, q) != 1 and pow(2, 72, q) != 1
               for q in NEW_PRIMES)
    assert all(gcd(q, S3) == 1 for q in NEW_PRIMES)
    phase_residues = {q: {b: [root_phase(q, b), (-root_phase(q, b)) % q] for b in (0, 2)}
                      for q in NEW_PRIMES}
    rows = ((38737, 2, 1), (246241, 3, 1), (NEW_PRIMES[0], 6, 0), (NEW_PRIMES[1], 6, 2))
    hits_mod6 = {w: [q for q, h, b in rows if w % h == b] for w in range(6)}
    assert all(hits_mod6.values())

    # Both assignments of the new primes and all independent root signs.
    starts = []
    for phases in ((0, 2), (2, 0)):
        for signs in product((1, -1), repeat=2):
            extra = [(sign*root_phase(q, b) % q, q)
                     for q, b, sign in zip(NEW_PRIMES, phases, signs)]
            root, modulus = crt([(A3, S3)] + extra)
            assert root % S3 == A3 and root > 0
            assert all((root*root*pow(2, 32 + 36*b, q)-1) % q == 0
                       for q, b in zip(NEW_PRIMES, phases))
            starts.append({'phases': list(phases), 'signs': list(signs),
                           'root_residues': [r for r, q in extra],
                           'start': str(root), 'modulus': str(modulus)})
    assert len({item['start'] for item in starts}) == 8
    minimum = min(starts, key=lambda item: int(item['start']))
    root = int(minimum['start'])
    dictionary = P + PREFIX + (38737, 246241) + NEW_PRIMES
    assert len(dictionary) == len(set(dictionary)) == 28
    assert 2*root*root-1 > max(dictionary)
    orders = {q: order2(q) for q in dictionary}
    period = lcm(*orders.values())
    assert period == 60480
    residues = {q: (root*root-1) % q for q in dictionary}
    coverage_counts = {q: 0 for q in dictionary}
    missing = []
    for n in range(1, period+1):
        for q in dictionary:
            residues[q] = (2*residues[q] + 1) % q
        hit = [q for q in dictionary if residues[q] == 0]
        if not hit:
            missing.append(n)
        for q in hit:
            coverage_counts[q] += 1
    assert not missing
    assert all(residues[q] == (root*root-1) % q for q in dictionary)

    # Private terms for the fixed orientation (q0 at phase 0, q1 at phase 2).
    fixed_root, fixed_modulus = crt([(A3, S3), (root_phase(NEW_PRIMES[0], 0), NEW_PRIMES[0]),
                                    (root_phase(NEW_PRIMES[1], 2), NEW_PRIMES[1])])
    witnesses = dict(zip(P, OLD_WITNESSES))
    witnesses.update(zip(PREFIX, PREFIX_WITNESSES))
    witnesses.update({38737: 3812, 246241: 10112, NEW_PRIMES[0]: 32, NEW_PRIMES[1]: 5072})
    assert len(set(witnesses.values())) == 28
    for q, n in witnesses.items():
        hit = [r for r in dictionary if (fixed_root*fixed_root*pow(2, n, r)-1) % r == 0]
        assert hit == [q]
        assert (fixed_root*fixed_root*pow(2, n, 487824887233)-1) % 487824887233 != 0
    for w in (105, 280, 0, 140):
        assert w % 35 in HOLES_B
    # Every fixed prime absent from the dictionary is inactive or the one
    # explicitly avoided active observer.  This is the precise compatibility
    # condition needed by the stripped-difference coprimalization lemma.
    extra_fixed = sorted(set(fixed) - set(dictionary))
    assert [q for q in extra_fixed if fixed[q] != 0] == [487824887233]
    known_primes = (2, 3) + tuple(sorted(set(fixed) | set(NEW_PRIMES)))
    assert prod(known_primes) == fixed_modulus
    witness_data = [{'prime': q, 'index': n} for q, n in witnesses.items()]
    certificate = {
        'schema': 'riesel-fixed-43-observer-cost-eight-v1',
        'native_semantics': {'state': 'fixed-X6 typed integer register', 'update': 'x -> 2x+1',
                             'weight': 1, 'multiplicity': 1, 'new_native_execution': False},
        'inherited_lower_bound': {'scope': 'R3 subset R2', 'reason': 'All three seven-cover family predicates are false',
                                 'source': 'riesel_seven_cover_20261124/observer/proof.md'},
        'R3': {'base_root': str(A3), 'progression_modulus': str(S3), 'observer_modulus': str(T),
               'observer_residue': str(RT), 'fixed_prime_residues': fixed},
        'new_primes': {q: {'prime': True, 'primality_method': 'deterministic odd trial division',
                           'trial_bound': isqrt(q), 'order2': 216,
                           'order_check_residues': {216: pow(2, 216, q), 108: pow(2, 108, q), 72: pow(2, 72, q)},
                           'phase_root_residues': phase_residues[q]} for q in NEW_PRIMES},
        'cyclotomic_identity': {'value': str(2**72 - 2**36 + 1), 'prime_factors': NEW_PRIMES},
        'tail_hits_mod6': hits_mod6,
        'eight_progressions': starts,
        'minimum_of_this_explicit_family': minimum,
        'minimum_scope': 'Only these eight CRT progressions, not all cost-eight roots in R3',
        'compact_root': {'delta_P': 8, 'tau_upper_bound': 28, 'decimal_digits': len(str(root)),
                         'proper_divisors_checked': True},
        'coverage': {'full_residue_period': period, 'missing_indices': missing,
                     'base2_orders': orders, 'channel_hit_counts': coverage_counts,
                     'method': 'Exact scalar recurrence modulo each selected prime'},
        'coprimalization': {'fixed_orientation_root': str(fixed_root), 'fixed_orientation_modulus': str(fixed_modulus),
                            'private_witnesses': witness_data, 'extra_fixed_active_prime': 487824887233,
                            'extra_active_hits_any_private_witness': False,
                            'strip_primes': known_primes,
                            'rule': 'D=lcm(2^abs(n_i-n_j)-1); strip all prime powers supported on fixed_orientation_modulus to E; impose a=0 mod E',
                            'exact_costs_on_resulting_infinite_progression': {'delta_P': 8, 'tau': 28}},
        'finite_cost_spectrum_R3': {'minimum': 8, 'all_integers_at_least_minimum_occur': True,
                                   'costs_at_least_nine_dependency': 'riesel_seven_cover_20261124/finite/proof.md Section 8'},
        'independent_project_review': False,
    }
    if args.coprimalized_example:
        D = 1
        for n, m in combinations(witnesses.values(), 2):
            D = lcm(D, (1 << abs(n-m))-1)
        E = D
        for q in known_primes:
            while E % q == 0:
                E //= q
        assert gcd(E, fixed_modulus) == 1
        co_root, co_modulus = crt([(fixed_root, fixed_modulus), (0, E)])
        terms = [(co_root*co_root << n)-1 for n in witnesses.values()]
        assert all(gcd(x, y) == 1 for x, y in combinations(terms, 2))
        certificate['coprimalization']['executed_example'] = {
            'D_bits': D.bit_length(), 'E_bits': E.bit_length(), 'root_bits': co_root.bit_length(),
            'progression_modulus_bits': co_modulus.bit_length(),
            'root_hex': hex(co_root), 'modulus_hex': hex(co_modulus), 'E_hex': hex(E),
            'pairwise_gcd_checks': 378, 'all_gcds_one': True,
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps({'certificate': str(args.output), 'compact_minimum': str(root),
                      'digits': len(str(root)), 'phases': minimum['phases'], 'signs': minimum['signs'],
                      'full_period': period, 'fixed_R3_base': str(A3),
                      'exact_total_example': args.coprimalized_example}, indent=2))


if __name__ == '__main__':
    main()
