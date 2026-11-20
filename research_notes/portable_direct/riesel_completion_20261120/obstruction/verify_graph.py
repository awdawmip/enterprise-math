#!/usr/bin/env python3
"""Standalone exact verification of the 489 baseline and 511 CRT witness.

Default: recompute all 513 G/E packets with a separate GMP implementation,
perform selected Python integer cross-checks, independently construct both
complete gcd graphs and their phase graphs, check every matching/cover edge,
check the universal two-vertex exclusion, and run the native BRC projections.

No factorization service, probabilistic primality test, numerical tolerance or
expansion of a sequence term is used. This is author-side exact checking, not
the project's independent Review process.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import itertools
import json
from math import gcd, isqrt, prod
from pathlib import Path
import subprocess
import sys
import time

from verify_source_pins import verify_native_source_pins

BASE = Path(__file__).resolve().parent
SIZE = 514
EXPECTED_A_ROOT = 690786768637635218740714348513373826260012289
EXPECTED_S = 7543152493250337317777998389729624720196910046042166547544586890203606088003198926478506067947700


def prime_divisors(n):
    out, d = [], 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def python_packet(A, S, q):
    C = A**q-1
    G = gcd(C, pow(2, S*q, C)-1)
    E = G
    # Independent saturation by every proper divisor.
    for d in range(1, q):
        if q % d:
            continue
        while E > 1:
            h = gcd(E, pow(2, S*d, E)-1)
            if h == 1:
                break
            E //= h
    return {'q': q, 'G': str(G), 'E': str(E)}


def independently_compute_graph(A, S, packets, offset):
    """Maintain A*R^(offset+i), rather than the builder's N recurrence."""
    found, pairs = {}, 0
    for row in packets:
        d, g = row['q'], int(row['G'])
        r = pow(2, S, g)
        z = A*pow(2, S*(offset+1), g) % g
        for i in range(1, SIZE-d+1):
            common = gcd(z-1, g)
            if common > 1:
                found[i, i+d] = str(common)
            z = z*r % g
            pairs += 1
    assert pairs == SIZE*(SIZE-1)//2
    return found, pairs


def phase_edges(q, phases, offset):
    result = set()
    for c in phases:
        i = (c-offset-1) % q+1
        if i <= SIZE-q:
            result.add((i, i+q))
    return result


def check_graph(certificate, computed, phase_graph):
    supplied = {(r['i'], r['j']): r['gcd'] for r in certificate['edges']}
    assert len(supplied) == len(certificate['edges'])
    assert supplied == computed and set(supplied) == phase_graph
    assert certificate['vertex_count'] == SIZE
    assert certificate['complete_pair_count'] == SIZE*(SIZE-1)//2
    assert certificate['edge_count'] == len(supplied)
    assert all(1 <= u <= 257 < v <= SIZE for u, v in supplied)
    matching = [tuple(e) for e in certificate['matching']]
    cover = set(certificate['minimum_vertex_cover'])
    independent = set(certificate['maximum_independent_set'])
    assert len(cover) == len(certificate['minimum_vertex_cover'])
    assert len(independent) == len(certificate['maximum_independent_set'])
    assert all(e in supplied for e in matching)
    assert len(set(itertools.chain.from_iterable(matching))) == 2*len(matching)
    assert len(matching) == len(cover)
    assert all(u in cover or v in cover for u, v in supplied)
    assert independent == set(range(1, SIZE+1))-cover
    assert all(not (u in independent and v in independent) for u, v in supplied)
    assert certificate['maximum_matching_size'] == len(matching)
    assert certificate['minimum_vertex_cover_size'] == len(cover)
    for field in ['maximum_pairwise_coprime_size', 'minimum_prime_cover_of_this_window',
                  'any_full_sequence_cover_minimum_new_primes']:
        assert certificate[field] == len(independent)
    assert certificate['if_retaining_old_twenty_minimum_total'] == len(independent)+20
    return {'pairs_checked': SIZE*(SIZE-1)//2, 'edges': len(supplied),
            'matching_size': len(matching), 'vertex_cover_size': len(cover),
            'maximum_pairwise_coprime_size': len(independent),
            'minimum_prime_cover_size': len(independent),
            'two_independent_graph_constructions_agree': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--backend', choices=['gmp', 'python'], default='gmp')
    parser.add_argument('--source-dir', type=Path)
    parser.add_argument('--output', type=Path, default=BASE/'verification_results.json')
    parser.add_argument('--python-crosscheck-periods', default='1,2,3,16,64,257,271,277')
    args = parser.parse_args()
    start = time.monotonic()
    source = json.loads((BASE/'input.json').read_text())
    A, a, S = int(source['A']), int(source['a']), int(source['S'])
    assert a == EXPECTED_A_ROOT and S == EXPECTED_S
    assert A == a*a*2**66 and source['n_initial'] == 66
    assert S % 5641020 == 0 and S % 2 == 0
    assert source['old_source_commit'] == 'a4d8c6a537a2f9c8c02beba4eae4b0c399fd7d52'
    if args.source_dir is None:
        args.source_dir = next((parent/'vendor_src' for parent in [BASE, *BASE.parents]
                                if (parent/'vendor_src/enterprise_math/brc_transport.py').is_file()), None)
    assert args.source_dir is not None, 'Pass --source-dir for the pinned native vendor_src.'
    source_pins = verify_native_source_pins(args.source_dir)
    assert source['project_source_commit'] == source_pins['project_source_commit']
    assert source['project_source_blobs'] == source_pins['project_source_blobs']
    packets = json.loads((BASE/'period_dictionary.json').read_text())
    assert [row['q'] for row in packets] == list(range(1, 514))
    print('Recomputing the complete q=1,...,513 dictionary', flush=True)
    if args.backend == 'gmp':
        executable = BASE/'period_packets_verify'
        subprocess.run(['g++', '-O2', '-std=c++17', str(BASE/'period_packets_verify.cpp'),
                        '-lgmpxx', '-lgmp', '-o', str(executable)], check=True)
        output = subprocess.run([str(executable), str(A), str(S), '513'],
                                check=True, text=True, stdout=subprocess.PIPE).stdout
        recomputed = [{'q': int(q), 'G': g, 'E': e}
                      for q, g, e in (line.split() for line in output.splitlines())]
    else:
        recomputed = [python_packet(A, S, q) for q in range(1, 514)]
    assert recomputed == packets
    crosschecked = []
    if args.backend == 'gmp':
        for q in sorted({int(q) for q in args.python_crosscheck_periods.split(',') if q}):
            assert 1 <= q <= 513
            assert python_packet(A, S, q) == packets[q-1]
            crosschecked.append(q)
            print(f'Independent Python packet q={q} passed', flush=True)
    assert all(row['E'] == '1' for row in packets[:256])

    # Exact-order packets contain all active primes of that order. Exhausting
    # all phases, with gcd > 1, therefore requires no factorization of E_q.
    profiles = json.loads((BASE/'phase_profiles.json').read_text())
    active = [row for row in packets if row['E'] != '1']
    assert [row['q'] for row in profiles] == [row['q'] for row in active]
    phase_map = {}
    for packet, row in zip(active, profiles):
        q, e = row['q'], int(row['E'])
        assert row['E'] == packet['E'] and q >= 257 and is_prime(q)
        actual = []
        for c in range(q):
            h = gcd(A*pow(2, S*c, e)-1, e)
            if h > 1:
                actual.append({'phase': c, 'gcd': str(h)})
        assert actual == row['phases']
        phases = [p['phase'] for p in actual]
        phase_map[q] = phases
        counts = [len(phase_edges(q, phases, t)) for t in range(q)]
        assert min(counts) == row['min_pairs'] and max(counts) == row['max_pairs']
        assert [i for i, count in enumerate(counts) if count == min(counts)] == row['min_offsets']
    assert len(active) == 37
    assert phase_map[257] == [0, 88]
    assert phase_map[271] == [4, 11, 116]
    assert phase_map[277] == [78, 97, 243]
    print('All active-prime phase supports independently verified', flush=True)

    base = json.loads((BASE/'graph_certificate.json').read_text())
    translated = json.loads((BASE/'translated_graph_certificate.json').read_text())
    t = int(translated['offset'])
    modulus = prod(phase_map)
    assert modulus == int(translated['offset_modulus']) and 0 <= t < modulus
    residues = {int(q): r for q, r in translated['offset_residues'].items()}
    assert set(residues) == set(phase_map)
    assert all(t % q == r and 0 <= r < q for q, r in residues.items())
    graph_checks = []
    for cert, offset in [(base, 0), (translated, t)]:
        assert all(cert[key] == source[key] for key in ['a', 'A', 'S'])
        computed, _ = independently_compute_graph(A, S, packets, offset)
        predicted = set().union(*(phase_edges(q, phases, offset % q)
                                  for q, phases in phase_map.items()))
        graph_checks.append(check_graph(cert, computed, predicted))
    assert graph_checks[0]['maximum_pairwise_coprime_size'] == 489
    assert graph_checks[1]['maximum_pairwise_coprime_size'] == 511
    assert translated['minimum_vertex_cover'] == [88, 146, 514]
    assert translated['matching'] == [[88, 345], [146, 423], [221, 514]]
    assert translated['over_all_translated_514_windows_maximum_pairwise_coprime_size'] == 511
    degrees = Counter(v for e in translated['edges'] for v in (e['i'], e['j']))
    assert sorted(degrees.values()) == [1]*11+[2,4,5]
    assert [degrees[v] for v in (88,146,514)] == [4,5,2]
    print('Both complete gcd graphs, matchings and vertex covers verified', flush=True)

    # Universal obstruction to removing just two vertices. Every translated
    # q=257 graph consists of two disjoint edges, so its four endpoint choices
    # exhaust all possible two-vertex covers of the full graph.
    excluded = json.loads((BASE/'two_vertex_exclusion.json').read_text())
    records = excluded['records']
    expected = {}
    for s in range(257):
        edges = sorted(phase_edges(257, phase_map[257], s))
        assert len(edges) == 2 and len(set(sum((list(e) for e in edges), []))) == 4
        for vertices in itertools.product(*edges):
            expected[s, tuple(sorted(vertices))] = True
    assert len(expected) == len(records) == excluded['candidate_count'] == 1028
    seen = set()
    for row in records:
        key = row['offset_mod_257'], tuple(row['candidate_cover'])
        assert key in expected and key not in seen
        seen.add(key)
        q, vertices = row['blocking_period'], set(row['candidate_cover'])
        assert q in [271, 277]
        assert all(any(u not in vertices and v not in vertices
                       for u, v in phase_edges(q, phase_map[q], s)) for s in range(q))
    assert seen == set(expected)
    counts = Counter(row['blocking_period'] for row in records)
    assert {str(q): count for q, count in sorted(counts.items())} == excluded['blocking_period_counts']

    # Additional short analytic certificate. The q=257 endpoint choices only
    # have four differences. Neither q=271 nor q=277 can have two of their
    # edges covered by such a pair, so each must be reduced to a single edge.
    differences = {abs(v[0]-v[1]) for _, v in expected}
    assert differences == {88, 169, 345, 426}
    sole_endpoint_sets = {}
    for q in (271, 277):
        phase_differences = {(u-v) % q for u in phase_map[q] for v in phase_map[q] if u != v}
        assert all(d % q not in phase_differences and -d % q not in phase_differences
                   for d in differences)
        sole_edges = [next(iter(edges)) for s in range(q)
                      if len(edges := phase_edges(q, phase_map[q], s)) == 1]
        sole_endpoint_sets[q] = set(itertools.chain.from_iterable(sole_edges))
    assert sole_endpoint_sets[271] == set(range(85,106)) | set(range(356,377))
    assert sole_endpoint_sets[277] == set(range(126,147)) | set(range(403,424))
    assert sole_endpoint_sets[271].isdisjoint(sole_endpoint_sets[277])
    assert all(abs(u-v) not in differences for u in sole_endpoint_sets[271]
               for v in sole_endpoint_sets[277])
    print('Universal 514-window optimum: both exhaustive and analytic exclusions passed', flush=True)

    # Inherited old channels are checked again on their entire relative cycles.
    old_channels, old_primes = [], set()
    for row in source['original_twenty_channels']:
        p, order = row['p'], row['order']
        assert p not in old_primes and is_prime(p)
        old_primes.add(p)
        assert pow(2, order, p) == 1
        assert all(pow(2, order//r, p) != 1 for r in prime_divisors(order))
        q = order//gcd(order, S)
        assert all((A*pow(2, S*i, p)-1) % p for i in range(q))
        old_channels.append({'p': p, 'relative_order': q, 'entire_cycle_nonzero': True})
    assert len(old_primes) == 20

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram, euclidean_digits

    def native(packet, x):
        (point, weight), = packet.evaluate((x,)).items()
        assert weight.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    step = EffectHistogram.from_terms(1, [(1, Affine(((4,),), (3,)), 1)])
    state = a*a-1
    for _ in range(33):
        state = native(step, state)
    assert state+1 == A
    projection_count = 0
    for g in sorted({int(row['G']) for row in packets if row['G'] != '1'}):
        r = pow(2, S, g)
        packet = EffectHistogram.from_terms(1, [(1, Affine(((r,),), (r-1,)), 1)])
        for offset in (0, t):
            x = (A*pow(2, S*offset, g)-1) % g
            observed = euclidean_digits(native(packet, x), (g,))[1][0]
            assert observed == (A*pow(2, S*(offset+1), g)-1) % g
            projection_count += 1
    assert all(e['gcd'] not in [str(p) for p in old_primes] for e in translated['edges'])

    result = {
        'schema': 'RIESEL_EXACT_GRAPH_AND_CRT_PHASE_VERIFIED_V5',
        'researcher_id': 'EM-DIRECT-970E1C', 'activity_id': 'RA-D2EC212845B63844081F9A14',
        **source_pins,
        'all_assertions_passed': True, 'backend': args.backend,
        'exact_dictionary_range': [1,513], 'exact_dictionary_rows_recomputed': len(recomputed),
        'independent_gmp_algorithm': 'A^q from scratch; saturation by all proper divisors',
        'independent_python_periods': crosschecked,
        'all_active_periods_prime': True, 'active_period_count': len(active),
        'all_active_phase_supports_verified_without_factorization': True,
        'baseline_window': graph_checks[0], 'translated_window': graph_checks[1],
        'translated_offset': str(t), 'translated_offset_modulus': str(modulus),
        'minimum_deleted_vertices': [88,146,514],
        'maximum_pairwise_coprime_size_over_all_514_term_translates': 511,
        'universal_two_vertex_candidate_count': len(records),
        'universal_two_vertex_blocking_periods': sorted(counts),
        'analytic_phase_interval_exclusion_verified': True,
        'old_twenty_channels': old_channels,
        'all_selected_terms_composite': 'a^2 * 2^(66+S*i)-1 = (a*2^(33+S*i/2)-1)*(a*2^(33+S*i/2)+1)',
        'fixed_X6_anchor': 'unchanged; one arithmetic internal register',
        'native_BRC': 'positive singleton x -> 4*x+3; exact modular sampled projections',
        'native_projected_updates_verified': projection_count,
        'any_full_cover_minimum_new_primes': 511,
        'if_retaining_old_twenty_minimum_total': 531,
        'scope': 'Exact finite-window and translated-window-family optima; no claim about full-cover existence or nonexistence.',
        'verification_status': 'AUTHOR_EXACT_RECOMPUTATION_NOT_INDEPENDENT_PROJECT_REVIEW',
        'elapsed_seconds': time.monotonic()-start
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['all_assertions_passed', 'any_full_cover_minimum_new_primes',
        'if_retaining_old_twenty_minimum_total', 'native_projected_updates_verified', 'elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
