#!/usr/bin/env python3
"""R762GN: exact orientation-graph absorption for moving Port STAR candidate.
Pure Python 3; all computations finite integers, no external dependencies.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
import json

V = tuple(range(4))
E = tuple(combinations(V, 2))  # (01,02,03,12,13,23)
EID = {edge: i for i, edge in enumerate(E)}
ID = tuple(range(6))
E0 = EID[(0, 1)]
E_OP = EID[(2, 3)]
STARS = tuple(tuple(EID[tuple(sorted((v, w)))] for w in V if w != v) for v in V)

def compose(p, q):
    return tuple(p[q[i]] for i in range(6))

def inverse(p):
    return tuple(p.index(i) for i in range(6))

def cycle(t):
    p = list(ID)
    a, b, c = t
    p[a], p[b], p[c] = b, c, a
    return tuple(p)

CYC = tuple(cycle(t) for t in STARS)
CYC_NEG = tuple(inverse(g) for g in CYC)

def parity(p):
    return sum(p[i] > p[j] for i in range(6) for j in range(i+1, 6)) % 2

def next_states(p):
    for v in E[p[E0]]:
        yield compose(p, CYC[v])
        yield compose(p, CYC_NEG[v])

def walk_from(roots, adjacent):
    seen = set(roots)
    queue = deque(roots)
    while queue:
        for y in adjacent[queue.popleft()]:
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen

def verify():
    all_p = tuple(p for p in permutations(ID) if parity(p) == 0)
    assert len(all_p) == 360
    adj = {p:tuple(next_states(p)) for p in all_p}
    assert all(len(z) == 4 for z in adj.values())
    rev = defaultdict(list)
    for p, qs in adj.items():
        for q in qs:
            rev[q].append(p)
    reach = walk_from([ID], adj)
    sink = {p for p in all_p if p[E0] == E_OP}
    assert len(reach) == 350 and len(sink) == 60
    assert sink <= reach
    assert all(set(adj[p]) <= sink for p in sink)
    root = reach - sink
    assert len(root) == 290
    # Complete directed reachability, on both sides, certifies two SCCs.
    assert walk_from([ID], {p:tuple(q for q in adj[p] if q in root) for p in root}) == root
    assert walk_from([ID], {p:tuple(q for q in rev[p] if q in root) for p in root}) == root
    pivot = next(iter(sink))
    assert walk_from([pivot], {p:adj[p] for p in sink}) == sink
    assert walk_from([pivot], {p:tuple(q for q in rev[p] if q in sink) for p in sink}) == sink
    # Shortest allowed hitting distances, computed from all A6 orientations.
    distance = {p:0 for p in sink}
    queue = deque(sink)
    while queue:
        y = queue.popleft()
        for p in rev[y]:
            if p not in distance:
                distance[p] = distance[y] + 1
                queue.append(p)
    assert len(distance) == 360
    hist = {str(k):v for k,v in sorted(Counter(distance.values()).items())}
    assert hist == {'0':60,'1':144,'2':144,'3':12}
    assert distance[ID] == 3
    # Exact positive-BRC path count without entering absorbing class.
    active = {ID:1}
    data = []
    for m in range(17):
        alive = sum(active.values())
        data.append({'m':m,'not_yet_absorbed_words':alive,
                     'total_words':4**m,'absorbed_words':4**m-alive})
        if m < 16:
            nxt = defaultdict(int)
            for p,mult in active.items():
                for q in adj[p]:
                    if q not in sink:
                        nxt[q] += mult
            active = nxt
    expected = {0:1, 3:60, 6:2900, 9:137728,
                12:6534252, 16:1118196052}
    for m, n in expected.items():
        assert data[m]['not_yet_absorbed_words'] == n
    return {'schema':'R762GN_MOVING_PORT_ABSORPTION_CERTIFICATE_V1',
            'candidate':'R762GM signed STAR semidirect with e=p(01)',
            'arithmetic':'exact positive integer path multiplicities',
            'A6_orientations':len(all_p), 'reachable_from_id':len(reach),
            'absorbing_port23_orientations':len(sink),
            'nonabsorbing_reachable_SCC':len(root),
            'absorbing_SCC':len(sink),
            'unreachable_orientations':len(set(all_p)-reach),
            'distance_to_absorption_histogram':hist,
            'max_hit_distance_any_orientation':max(distance.values()),
            'first_hit_from_id_distance':distance[ID],
            'survival':data,
            'uniform_4_branch_bound':'Pr(no absorption by m) <= (63/64)^floor(m/3)',
            'review':'NOT_REVIEWED','native_license':'CANDIDATE_NOT_ADOPTED',
            'status':'PASS'}

if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
