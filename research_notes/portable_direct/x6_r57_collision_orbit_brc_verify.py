#!/usr/bin/env python3
"""R57 conditional R44 positive-labelled BRC collision-pair orbit certificate."""
from collections import deque
from functools import lru_cache
from itertools import permutations, product
from math import factorial
from pathlib import Path
import json

def successors(p, geometry, state):
    j_a, j_b = geometry
    a, b, occupant, rotated = state
    moves = {}
    for who, port, shared in (("A", a, j_a), ("B", b, j_b)):
        if port != -1:
            continue
        for i in range(p):
            if i == shared and occupant:
                continue
            target = (i, b, "A" if i == shared else occupant, rotated) if who == "A" else (a, i, "B" if i == shared else occupant, rotated)
            moves[f"{who}{i}"] = target
    if occupant:
        moves["R"] = (a, b, "", rotated)
    if rotated == 0 and occupant == "" and ((a != -1) != (b != -1)):
        used_who = "A" if a != -1 else "B"
        used_port = a if used_who == "A" else b
        shared_port = j_a if used_who == "A" else j_b
        moves["T"] = (a, b, used_who if used_port == shared_port else "", 1)
    return moves

def graph(p, geom):
    initial = (-1, -1, "", 0)
    states = {initial}
    edges = {}
    todo = deque([initial])
    while todo:
        state = todo.popleft()
        edges[state] = successors(p, geom, state)
        for nxt in edges[state].values():
            if nxt not in states:
                states.add(nxt)
                todo.append(nxt)
    return initial, states, edges

def future_partition(edges):
    @lru_cache(None)
    def suffixes(state):
        words = {()}
        for label, nxt in edges[state].items():
            words.update((label,) + tail for tail in suffixes(nxt))
        return frozenset(words)
    return {s: suffixes(s) for s in edges}

def transform(p, geom, state, label, pi_a, pi_b, swap):
    j_a, j_b = geom
    a, b, occ, t = state
    if swap:
        mapped_geom = (pi_b[j_b], pi_a[j_a])
        mapped_state = (pi_b[b] if b >= 0 else -1, pi_a[a] if a >= 0 else -1,
                        "A" if occ == "B" else "B" if occ == "A" else "", t)
    else:
        mapped_geom = (pi_a[j_a], pi_b[j_b])
        mapped_state = (pi_a[a] if a >= 0 else -1, pi_b[b] if b >= 0 else -1, occ, t)
    if label in ("R", "T"):
        mapped_label = label
    else:
        who, idx = label[0], int(label[1:])
        mapped_label = (("B" if who == "A" else "A") if swap else who) + str((pi_a if who == "A" else pi_b)[idx])
    return mapped_geom, mapped_state, mapped_label

def verify(p):
    graphs = {(ja,jb):graph(p,(ja,jb)) for ja,jb in product(range(p), repeat=2)}
    expected_words = 4*p*p + 16*p - 3
    expected_states = 2*p*p + 8*p + 5
    all_futures = set()
    roots = {}
    for geom, (initial, states, edges) in graphs.items():
        assert len(states) == expected_states, (p, geom, 'state count')
        future = future_partition(edges)
        assert len(future[initial]) == expected_words, (p,geom,'word count')
        roots[geom] = future[initial]
        all_futures.update(future.values())
    assert len(all_futures) == (11 if p == 1 else p*p+10*p+2), (p, 'global future-class count')
    for geom in graphs:
        witness = (f'A{geom[0]}', f'B{geom[1]}')
        assert witness not in roots[geom]
        assert all(witness in roots[other] for other in roots if other != geom)
    transformations = 0
    if p <= 3:
        perms = list(permutations(range(p)))
        for geom, (_, states, edges) in graphs.items():
            for pa,pb,swap in product(perms,perms,(False,True)):
                for state in states:
                    g2,s2,_ = transform(p,geom,state,'R',pa,pb,swap)
                    assert s2 in graphs[g2][1]
                    new_moves = graphs[g2][2][s2]
                    for label,dst in edges[state].items():
                        _,_,mlabel = transform(p,geom,state,label,pa,pb,swap)
                        _,mdst,_ = transform(p,geom,dst,label,pa,pb,swap)
                        assert new_moves[mlabel] == mdst
                    assert len(new_moves) == len(edges[state])
                transformations += 1
    return {
        'p':p, 'geometry_count':p*p, 'states_per_geometry':expected_states,
        'successful_words_per_geometry':expected_words,
        'distinct_root_future_languages':len(set(roots.values())),
        'joint_future_language_classes':len(all_futures),
        'minimum_geometry_bits':(p*p-1).bit_length(),
        'fixed_geometry_source_partition_automorphisms':2*factorial(p-1)**2,
        'fully_checked_group_actions_on_geometry_graph_pairs':transformations,
        'check':'PASS'
    }

if __name__ == '__main__':
    result={'schema':'X6_R57_COLLISION_PAIR_ORBIT_BRC_V1',
            'scope':'conditional R44 named positive-branch grammar; all p theorem plus p=1..8 exhaustive',
            'runs':[verify(p) for p in range(1,9)],
            'native_admission':'NOT_ESTABLISHED',
            'independent_review':'NOT_REVIEWED'}
    with Path(__file__).with_name('x6_r57_collision_orbit_brc_results.json').open('w',encoding='utf-8') as out:
        json.dump(result,out,ensure_ascii=False,indent=2)
        out.write('\n')
    print(json.dumps(result,indent=2))
