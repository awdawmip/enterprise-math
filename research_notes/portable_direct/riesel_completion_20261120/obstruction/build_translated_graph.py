"""Optimize the phase of a 514-term window using a complete order dictionary.

The output is exact, finite and independent of any factorization oracle.
The base dictionary is recomputed by verify_graph.py before use as evidence.
"""
from __future__ import annotations

from collections import Counter
import itertools
import json
from math import gcd, isqrt
from pathlib import Path

from build_graph import matching_and_cover

BASE = Path(__file__).resolve().parent
SIZE = 514


def phase_edges(row, offset):
    q = row['q']
    return [(i, i+q) for phase in row['phases']
            if 1 <= (i := (phase['phase']-offset) % q or q) <= SIZE-q]


def all_phases(A, S, packets):
    rows = []
    for packet in packets:
        if packet['E'] == '1':
            continue
        q, e = packet['q'], int(packet['E'])
        r, x = pow(2, S, e), (A-1) % e
        phases = []
        for c in range(q):
            common = gcd(x, e)
            if common > 1:
                phases.append({'phase': c, 'gcd': str(common)})
            x = (r*x+r-1) % e
        row = {'q': q, 'E': packet['E'], 'phases': phases}
        counts = [len(phase_edges(row, offset)) for offset in range(q)]
        row.update(min_pairs=min(counts), max_pairs=max(counts),
                   min_offsets=[t for t, count in enumerate(counts)
                                if count == min(counts)])
        rows.append(row)
    return rows


def crt(residues):
    x, modulus = 0, 1
    for q, residue in sorted(residues.items()):
        assert gcd(modulus, q) == 1
        x += modulus*((residue-x)*pow(modulus, -1, q) % q)
        modulus *= q
        assert 0 <= x < modulus
    assert all(x % q == residue for q, residue in residues.items())
    return x, modulus


def main():
    source = json.loads((BASE/'input.json').read_text())
    packets = json.loads((BASE/'period_dictionary.json').read_text())
    A, S = int(source['A']), int(source['S'])
    assert [r['q'] for r in packets] == list(range(1, SIZE))
    profiles = all_phases(A, S, packets)
    assert all(all(row['q'] % p for p in range(2, isqrt(row['q'])+1))
               for row in profiles)
    assert all(row['q'] >= 257 for row in profiles)
    (BASE/'phase_profiles.json').write_text(json.dumps(profiles, indent=2)+'\n')

    forced = [row for row in profiles if row['min_pairs'] > 0]
    assert forced[0]['q'] == 257
    options = {row['q']: [(t, phase_edges(row, t)) for t in range(row['q'])]
               for row in forced}
    exclusion_records = []
    for t257, mandatory_edges in options[257]:
        assert len(mandatory_edges) == 2
        assert len(set(itertools.chain.from_iterable(mandatory_edges))) == 4
        for chosen in itertools.product(*mandatory_edges):
            vertices = set(chosen)
            blocker = next((row['q'] for row in forced[1:]
                            if not any(all(u in vertices or v in vertices
                                           for u, v in edges)
                                       for _, edges in options[row['q']])), None)
            assert blocker is not None
            exclusion_records.append({'offset_mod_257': t257,
                                      'candidate_cover': sorted(vertices),
                                      'blocking_period': blocker})
    assert len(exclusion_records) == 257*4
    exclusion = {
        'schema': 'RIESEL_514_TRANSLATION_TWO_VERTEX_EXCLUSION_V5',
        'window_length': SIZE, 'base_period': 257,
        'base_phases': [row['phase'] for row in profiles[0]['phases']],
        'candidate_count': len(exclusion_records),
        'records': exclusion_records,
        'blocking_period_counts': dict(sorted(Counter(
            row['blocking_period'] for row in exclusion_records).items())),
        'claim': 'Every translated 514-term window requires at least three vertices to meet all common-divisor edges.'
    }
    (BASE/'two_vertex_exclusion.json').write_text(json.dumps(exclusion, indent=2)+'\n')

    # Deterministic search: extend the endpoints of the two forced q=257 edges
    # by one vertex; each other active q can be optimized independently by CRT.
    solution = None
    for _, mandatory_edges in options[257]:
        for chosen in itertools.product(*mandatory_edges):
            vertices = set(chosen)
            allowed = set(range(1, SIZE+1))
            for row in forced[1:]:
                possible = set()
                for _, edges in options[row['q']]:
                    uncovered = [(u, v) for u, v in edges
                                 if u not in vertices and v not in vertices]
                    if not uncovered:
                        possible = set(range(1, SIZE+1))
                        break
                    if len(uncovered) == 1:
                        possible.update(uncovered[0])
                allowed.intersection_update(possible)
                if not allowed:
                    break
            if allowed:
                vertices.add(min(allowed))
                residues = {row['q']: next(t for t in range(row['q'])
                            if all(u in vertices or v in vertices
                                   for u, v in phase_edges(row, t)))
                            for row in profiles}
                solution = sorted(vertices), residues
                break
        if solution:
            break
    assert solution is not None
    cover, residues = solution
    assert cover == [88, 146, 514]
    offset, modulus = crt(residues)

    # Compute every pair through G_d, rather than trusting the phase construction.
    edges, pairs = [], 0
    for row in packets:
        d, g = row['q'], int(row['G'])
        if g == 1:
            pairs += SIZE-d
            continue
        r = pow(2, S, g)
        x = (A*pow(2, S*(offset+1), g)-1) % g
        for i in range(1, SIZE-d+1):
            common = gcd(x, g)
            if common > 1:
                edges.append({'i': i, 'j': i+d, 'gcd': str(common)})
            pairs += 1
            x = (r*x+r-1) % g
    assert pairs == SIZE*(SIZE-1)//2
    assert all(e['i'] in cover or e['j'] in cover for e in edges)
    matching, algorithm_cover, independent = matching_and_cover(edges, 257, SIZE)
    assert len(matching) == len(algorithm_cover) == len(cover) == 3
    independent = sorted(set(range(1, SIZE+1))-set(cover))
    assert len(independent) == 511
    phase_edge_set = {e for row in profiles for e in phase_edges(row, offset % row['q'])}
    assert phase_edge_set == {(e['i'], e['j']) for e in edges}
    result = {
        'schema': 'RIESEL_CRT_TRANSLATED_COMMON_DIVISOR_GRAPH_V5',
        'researcher_id': 'EM-DIRECT-970E1C',
        'activity_id': 'RA-D2EC212845B63844081F9A14',
        'a': source['a'], 'A': source['A'], 'S': source['S'],
        'sequence': 'N_i = a^2 * 2^(66 + S*i) - 1',
        'window_formula': 'V_j = N_(offset+j), j=1,...,514',
        'offset': str(offset), 'offset_modulus': str(modulus),
        'offset_residues': {str(q): r for q, r in sorted(residues.items())},
        'vertex_interval': [1, SIZE], 'vertex_count': SIZE,
        'left_interval': [1, 257], 'right_interval': [258, SIZE],
        'complete_pair_count': pairs, 'edges': edges, 'edge_count': len(edges),
        'matching': matching, 'minimum_vertex_cover': cover,
        'maximum_independent_set': independent,
        'maximum_matching_size': len(matching),
        'minimum_vertex_cover_size': len(cover),
        'maximum_pairwise_coprime_size': len(independent),
        'minimum_prime_cover_of_this_window': len(independent),
        'any_full_sequence_cover_minimum_new_primes': len(independent),
        'if_retaining_old_twenty_minimum_total': 20+len(independent),
        'over_all_translated_514_windows_maximum_pairwise_coprime_size': 511,
        'dictionary_period_interval': [1, 513],
        'nontrivial_exact_periods': [row['q'] for row in profiles],
        'all_nontrivial_exact_periods_prime': True,
        'old_source_commit': source['old_source_commit'],
        'status': 'AUTHOR_EXACT_FINITE_PROOF_NOT_INDEPENDENT_PROJECT_REVIEW',
        'scope': 'Exact optimum within this 514-term translated-window family; only a lower bound for a full cover of the fixed old root, whose existence remains undecided.'
    }
    (BASE/'translated_graph_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['offset', 'offset_modulus', 'edge_count',
        'matching', 'minimum_vertex_cover', 'maximum_pairwise_coprime_size',
        'if_retaining_old_twenty_minimum_total']}))
    print('two_vertex_exclusion_blockers', exclusion['blocking_period_counts'])


if __name__ == '__main__':
    main()
