"""Exact finite witnesses for the unbounded cost spectrum at one larger observer.

Reuses the published all-cost refinement theorem and its unchanged seed covers.
Constructs new explicit coprimalized roots for costs5,6,7, and reuses cost8.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
import json
from math import gcd, lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
DEPENDENCY = Path('research_notes/portable_direct/riesel_spectrum_20261121/spectrum/small_spectrum_certificate.json')
DEPENDENCY_COMMIT = 'af9e1a5e49386a28283781876e10742a71991036'
K = 14436565
RESIDUES = {5: 3, 13: 1, 11: 0, 61: 0, 331: 0}


def strip(value, primes):
    for p in primes:
        while value % p == 0:
            value //= p
    return value


def crt(pairs):
    a, m = 0, 1
    for r, q in pairs:
        assert gcd(m, q) == 1
        a += m * ((r-a)*pow(m, -1, q) % q)
        m *= q
    return a, m


def main():
    root = next(p for p in HERE.parents if (p/DEPENDENCY).is_file())
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=HERE/'fixed_observer_certificate.json')
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)
    source_bytes = (root/DEPENDENCY).read_bytes()
    old = json.loads(source_bytes)
    astar, M = int(old['a_star']), int(old['M'])
    P = [row[0] for row in old['old_rows']]
    private_old = [row[3] for row in old['old_rows']]
    assert prod(P) == M and 3 in private_old and 63 in private_old
    T = strip((1 << 210)-1, P)
    assert all(T % p == 0 for p in (3, 11, 331))
    for q in (11, 61, 331):
        assert ((1 << 60)-1) % q == 0
    results = []
    for seed in old['seeds'][:3]:
        rows = seed['rows']
        s = seed['additional_cost']
        S = P + [row['p'] for row in rows]
        indices = private_old + [2*row['private_u'] for row in rows]
        assert len(indices) == len(set(indices)) == 20+s
        assert not set((11, 61, 331)).intersection(S)
        differences = sorted({abs(i-j) for i, j in combinations(indices, 2)})
        D = lcm(*[(1 << d)-1 for d in differences])
        E = strip(D, S)
        assert all(E % q == 0 for q in (11, 61, 331))
        forcing = lcm(E, T)
        pairs = [(astar, 2*M)] + [(row['root_residue'], row['p']) for row in rows]
        pairs.append((0, forcing))
        a, modulus = crt(pairs)
        assert a > 1 and a % 3 == 0 and a % T == 0
        assert (a-astar) % (2*M) == 0 and a % K == 666303
        assert all(a % q == r for q, r in RESIDUES.items())
        values = [(a*a << n)-1 for n in indices]
        checks = 0
        for x, y in combinations(values, 2):
            assert gcd(x, y) == 1
            checks += 1
        for n, assigned, value in zip(indices, S, values):
            assert [q for q in S if value % q == 0] == [assigned]
            assert assigned < value
        assert all(all(value % p for p in P) for value in values[20:])
        assert 2*a*a-1 > max(S)
        results.append({'additional_cost': s, 'total_cost': 20+s,
                        'root_hex': hex(a), 'progression_modulus_hex': hex(modulus),
                        'root_decimal_digits': len(str(a)),
                        'root_decimal_sha256': sha256(str(a).encode()).hexdigest(),
                        'root_residue_mod_K': a % K,
                        'private_indices': indices,
                        'checked_pairwise_gcd_count': checks,
                        'all_pairwise_gcd_one': True,
                        'old_hole_private_terms': s,
                        'properness': True,
                        'coverage_reuse': 'All root residues equal the already certified full-cover seed residues; its complete-period evidence is reused.'})
    n8 = old['numeric_cost_8']
    a8 = int(n8['root_hex'], 16)
    assert all(a8 % q == r for q, r in RESIDUES.items()) and a8 % K == 666303
    assert n8['all_pairwise_gcd_one'] and n8['gcd_pair_count'] == 378
    result = {'schema': 'riesel-fixed-larger-observer-spectrum-v1',
              'status': 'AUTHOR_PROOF_AND_EXACT_FINITE_WITNESSES; NOT_INDEPENDENT_REVIEW',
              'dependency': {'commit': DEPENDENCY_COMMIT, 'path': str(DEPENDENCY),
                             'sha256': sha256(source_bytes).hexdigest()},
              'observer_modulus_K': K, 'observer_residue': 666303,
              'observer_prime_residues': RESIDUES,
              'optimizer_flags': {'E1': True, 'E2': True, 'E3': False, 'E4': False, 'N': False},
              'old_private_indices_forcing_new_zeros': [3, 63],
              'new_explicit_witnesses': results,
              'unchanged_cost8_witness': {'additional_cost': 8, 'total_cost': 28,
                                         'root_decimal_digits': n8['root_decimal_digits'],
                                         'root_decimal_sha256': n8['root_decimal_sha256'],
                                         'root_residue_mod_K': a8 % K,
                                         'reuse': 'The full numeric root,378 gcd results and native1040-step execution remain in the unchanged published dependency.'},
              'all_cost_theorem': 'For every integer s>=5 there are infinitely many ordinary roots in the same old class and observer residue666303 modK with delta_P=s and tau(a^2)=20+s.',
              'infinite_proof_basis': 'All retained old private indices include3 and63, so2^60-1 divides D. The primes11,61,331 are outside every constructed dictionary: their orders10,60,30 are neither fixed orders4,9,12,18 nor multiples36. Thus all divide E and a. Fixed prime phases5 and13 retain residues3 and1. Apply the published coprimalization/refinement theorem.',
              'quantifier_boundary': 'This is forall s exists infinitely many a, all sharing a finite observer. It does not prove infinite cost for any one ordinary root.'}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'output': str(args.output),
                      'new_numeric_costs': [r['additional_cost'] for r in results],
                      'new_root_digits': [r['root_decimal_digits'] for r in results],
                      'new_gcd_checks': sum(r['checked_pairwise_gcd_count'] for r in results),
                      'fixed_observer_residue': 666303, 'reused_cost': 8}))


if __name__ == '__main__':
    main()
