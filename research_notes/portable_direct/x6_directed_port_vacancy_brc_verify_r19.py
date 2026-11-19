#!/usr/bin/env python3
"""R19: exact directed-port vacancy and swapped-label witness checker.
Finite six-coordinate, three-axis chart subset; not an admitted native triadic controller.
No third-party packages. Python >=3.10.
"""
from __future__ import annotations
from collections import deque
from itertools import combinations
import json
from pathlib import Path
import random

N = 8
CELLS = tuple(tuple((i >> j) & 1 for j in range(3)) + (0, 0, 0) for i in range(N))
CANDIDATES = tuple((u, v) for u in range(N) for v in range(N)
                   if sum(abs(a-b) for a, b in zip(CELLS[u], CELLS[v])) == 1)
assert len(CANDIDATES) == 24
FULL = (1 << N) - 1


def neighbors(edges):
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u].append(v)
    return adj


def directed_shortest_path(adj, occupied, start):
    seen = {start}
    q = deque([(start,)])
    while q:
        path = q.popleft()
        u = path[-1]
        if not (occupied >> u & 1):
            return path
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(path+(v,))
    return None


def bfs_first_movement(adj, occupied, target):
    q = deque([(occupied, target, 0)])
    seen = {(occupied, target)}
    while q:
        occ, pos, depth = q.popleft()
        for u in range(N):
            if not (occ >> u & 1):
                continue
            for v in adj[u]:
                if occ >> v & 1:
                    continue
                if u == pos:
                    return depth+1
                nxt = (occ ^ (1 << u) ^ (1 << v), pos)
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt[0], nxt[1], depth+1))
    return None


def move(positions, edge):
    label, dest = edge
    out = dict(positions)
    if label not in out:
        return None
    u = out[label]
    if dest in out.values() or dest not in [v for a, v in EDGES if a == u]:
        return None
    out[label] = dest
    return out


def variant_edges():
    rng = random.Random(20261119)
    patterns = [
        ('full', CANDIDATES),
        ('forward', tuple((u,v) for u,v in CANDIDATES if v > u)),
        ('backward', tuple((u,v) for u,v in CANDIDATES if v < u)),
        ('first-axis', tuple((u,v) for u,v in CANDIDATES if abs(CELLS[u][0]-CELLS[v][0])==1)),
        ('empty', tuple()),
        ('half-odd', tuple((u,v) for u,v in CANDIDATES if u % 2)),
        ('half-even', tuple((u,v) for u,v in CANDIDATES if not u % 2)),
    ]
    for i in range(24):
        mask = rng.getrandbits(len(CANDIDATES))
        patterns.append((f'fixed-seed-{i:02d}', tuple(pair for j,pair in enumerate(CANDIDATES) if mask>>j & 1)))
    return patterns


def guarded_one_shot_counterexample():
    """A finite-control Port budget makes locally present edges non-composable."""
    edges = {(0, 1), (1, 2)}
    initial = (frozenset({0, 1}), 1)  # occupied, remaining Port credit
    target = 0
    q = deque([(initial, 0)])
    seen = {initial}
    first = None
    while q:
        (occ, credit), dist = q.popleft()
        for u, v in edges:
            if u not in occ or v in occ or credit == 0:
                continue
            if u == target:
                first = dist+1
                break
            nxt = (frozenset((set(occ)-{u})|{v}), credit-1)
            if nxt not in seen:
                seen.add(nxt);q.append((nxt,dist+1))
        if first is not None:
            break
    assert first is None
    assert (0,1) in edges and (1,2) in edges
    return {'static_directed_distance':2, 'one_shot_credit_first_move':None,
            'initial_occupied_cells':[0,1], 'initial_vacancy_cell':2,
            'test':'PASS'}


def run():
    checked_first = checked_lift = checked_swaps = permanent = 0
    edge_count = {}
    finite_depth_hist = {}
    max_depth = 0
    for name, edges in variant_edges():
        global EDGES
        EDGES = edges
        adj = neighbors(edges)
        edge_count[name] = len(edges)
        for occ in range(1,FULL+1):
            if occ == FULL:
                # all occupied, vacancy-free: nobody can move
                pass
            labels = [i for i in range(N) if occ >> i & 1]
            paths = {a: directed_shortest_path(adj,occ,a) for a in labels}
            dist = {a:len(paths[a])-1 if paths[a] else None for a in labels}
            for a in labels:
                answer = bfs_first_movement(adj,occ,a)
                assert answer == dist[a], (name,occ,a,answer,dist[a])
                checked_first += 1
                if dist[a] is not None:
                    max_depth = max(max_depth,dist[a]); finite_depth_hist[str(dist[a])] = finite_depth_hist.get(str(dist[a]),0)+1
                    path=paths[a]
                    # The reverse vacancy chain is a valid word, ending in source initially at a.
                    positions={x:x for x in labels}
                    for k in range(len(path)-2,-1,-1):
                        source=path[k]
                        result=move(positions,(source,path[k+1]))
                        assert result is not None, (name,occ,a,path,k)
                        positions=result
                    checked_lift += 1
            for a,b in combinations(labels,2):
                da,db=dist[a],dist[b]
                if da is None and db is None:
                    permanent += 1
                    continue
                # Strict unequal distances, including infinity, are differentiated at min depth.
                if da == db:
                    continue
                if da is None or (db is not None and db < da):
                    a,b=b,a;da,db=db,da
                assert da is not None and (db is None or da<db)
                path=paths[a]
                assert b not in path[1:], (name,a,b,path)
                P={x:x for x in labels}
                Q={x:(b if x==a else a if x==b else x) for x in labels}
                word=[(path[k],path[k+1]) for k in range(len(path)-2,0,-1)]+[(a,path[1])]
                assert len(word)==da
                for step in word[:-1]:
                    pnew=move(P,step);qnew=move(Q,step)
                    assert pnew is not None and qnew is not None, (name,occ,a,b,step)
                    P,Q=pnew,qnew
                assert move(P,word[-1]) is not None
                assert move(Q,word[-1]) is None
                checked_swaps+=1
    report={
      'schema':'EM_X6_R19_DIRECTED_PORT_BRC_RESULTS_V1',
      'date':'2026-11-19',
      'test_domain':'8 finite Cells in signed six-coordinate X6 chart; 3 varying axes, 3 fixed axes; directed signed-unit edges',
      'edge_patterns':len(edge_count),
      'edge_counts':edge_count,
      'occupied_subsets_per_pattern':FULL,
      'first_move_vs_graph_distance_checks':checked_first,
      'canonical_path_replay_checks':checked_lift,
      'strict_depth_swapped_label_witness_checks':checked_swaps,
      'both_permanently_immobile_pair_cases':permanent,
      'max_finite_directed_distance':max_depth,
      'finite_depth_histogram':finite_depth_hist,
      'one_shot_guard_counterexample':guarded_one_shot_counterexample(),
      'all_assertions':'PASS',
      'limitations':'Directed, static, source-neutral Port graph; limited finite subcarrier; no tested TRIADIC_CLOSURE_E state-dependent dynamics or independent review'
    }
    return report

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, sort_keys=True, indent=2))
