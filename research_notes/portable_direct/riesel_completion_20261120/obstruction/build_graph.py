"""Exact common-divisor graph and matching/vertex-cover certificate.

No sequence value A*2**(S*i)-1 is expanded. Pair gcds are computed through
G_d = gcd(A**d-1, 2**(S*d)-1), with exact modular powers.
"""
from __future__ import annotations

from collections import deque
import json
from math import gcd
from pathlib import Path
import time

BASE = Path(__file__).resolve().parent


def graph_from_packets(A, S, packets, size):
    edges = []
    pairs = 0
    for row in packets:
        d = row['q']
        if d >= size:
            break
        modulus = int(row['G'])
        assert modulus >= 1
        if modulus == 1:
            pairs += size-d
            continue
        power = pow(2, S, modulus)
        # x is N_i mod G_d, starting at i=1.
        x = (A*power-1) % modulus
        for i in range(1, size-d+1):
            common = gcd(x, modulus)
            if common > 1:
                edges.append({'i': i, 'j': i+d, 'gcd': str(common)})
            pairs += 1
            x = (power*x+power-1) % modulus
    assert pairs == size*(size-1)//2
    return edges, pairs


def matching_and_cover(edges, left_size, size):
    left = set(range(1, left_size+1))
    right = set(range(left_size+1, size+1))
    adjacency = {u: [] for u in sorted(left)}
    for e in edges:
        assert e['i'] in left and e['j'] in right
        adjacency[e['i']].append(e['j'])
    for neighbours in adjacency.values():
        neighbours.sort()
    matched_right = {}

    def augment(u, seen):
        for v in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in matched_right or augment(matched_right[v], seen):
                matched_right[v] = u
                return True
        return False

    for u in sorted(left):
        augment(u, set())
    matched_left = {u: v for v, u in matched_right.items()}
    reachable_left = left - set(matched_left)
    reachable_right = set()
    todo = deque(sorted(reachable_left))
    while todo:
        u = todo.popleft()
        for v in adjacency[u]:
            if matched_left.get(u) == v or v in reachable_right:
                continue
            reachable_right.add(v)
            if v in matched_right and matched_right[v] not in reachable_left:
                reachable_left.add(matched_right[v])
                todo.append(matched_right[v])
    cover = (left-reachable_left) | reachable_right
    matching = sorted([u, v] for v, u in matched_right.items())
    assert len(cover) == len(matching)
    assert len({u for u, _ in matching}) == len(matching)
    assert len({v for _, v in matching}) == len(matching)
    edge_set = {(e['i'], e['j']) for e in edges}
    assert all(tuple(e) in edge_set for e in matching)
    assert all(e['i'] in cover or e['j'] in cover for e in edges)
    independent = sorted((left | right)-cover)
    assert all(not (e['i'] in independent and e['j'] in independent) for e in edges)
    return matching, sorted(cover), independent


def main():
    start = time.monotonic()
    source = json.loads((BASE/'input.json').read_text())
    prior = json.loads(Path(source['old_certificate_path']).read_text())
    old_packets = prior['final_packets']
    extension = json.loads((BASE/'packets_258_512.json').read_text())
    last = [{'q':int(q), 'G':g, 'E':e} for q,g,e in
            (line.split() for line in (BASE/'packets_513.txt').read_text().splitlines())]
    packets = old_packets + extension + last
    assert [x['q'] for x in packets] == list(range(1,514))
    (BASE/'period_dictionary.json').write_text(json.dumps(packets,indent=2)+'\n')
    A, S = int(source['A']), int(source['S'])
    size = 514
    assert all(row['E']=='1' for row in packets[:256])
    edges, pairs = graph_from_packets(A,S,packets,size)
    matching, cover, independent = matching_and_cover(edges,257,size)
    result = {
        'schema':'RIESEL_EXACT_COMMON_DIVISOR_GRAPH_V5',
        'researcher_id':'EM-DIRECT-970E1C',
        'activity_id':'RA-D2EC212845B63844081F9A14',
        'a':source['a'], 'A':source['A'], 'S':source['S'],
        'sequence':'N_i = a^2 * 2^(66 + S*i) - 1',
        'vertex_interval':[1,size], 'vertex_count':size,
        'left_interval':[1,257], 'right_interval':[258,514],
        'complete_pair_count':pairs, 'edges':edges,
        'edge_count':len(edges), 'matching':matching,
        'minimum_vertex_cover':cover,
        'maximum_independent_set':independent,
        'maximum_matching_size':len(matching),
        'minimum_vertex_cover_size':len(cover),
        'maximum_pairwise_coprime_size':len(independent),
        'minimum_prime_cover_of_this_window':len(independent),
        'any_full_sequence_cover_minimum_new_primes':len(independent),
        'if_retaining_old_twenty_minimum_total':20+len(independent),
        'old_source_commit':source['old_source_commit'],
        'old_certificate_path':source['old_certificate_path'],
        'dictionary_period_interval':[1,513],
        'nontrivial_exact_periods':[row['q'] for row in packets if row['E']!='1'],
        'status':'AUTHOR_EXACT_FINITE_PROOF_NOT_INDEPENDENT_PROJECT_REVIEW',
        'scope':'Exact finite-window optima; lower bound on any full cover of fixed old root; no assertion of finite-cover existence or nonexistence.',
        'graph_seconds':time.monotonic()-start,
    }
    (BASE/'graph_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['vertex_count','complete_pair_count','edge_count',
        'maximum_matching_size','maximum_pairwise_coprime_size','minimum_prime_cover_of_this_window',
        'if_retaining_old_twenty_minimum_total','graph_seconds']}))


if __name__=='__main__':
    main()
