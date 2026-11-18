#!/usr/bin/env python3
"""Exact integer checks for R5 cycle observers and triangular-cactus repair.
No non-standard dependencies. All combinatorial enumerations are exhaustive
within their explicitly stated finite bounds.
"""
from itertools import product
from collections import Counter
import json


def q_cycle(bits):
    n = len(bits)
    return sum(bits[i] * bits[(i + 1) % n] for i in range(n))


def set_bit(bits, idx, value):
    return bits[:idx] + (value,) + bits[idx+1:]


def cycle_signature(bits, horizon):
    vals = [q_cycle(bits)]
    if horizon >= 1:
        vals += [q_cycle(set_bit(bits, i, val))
                 for i in range(len(bits)) for val in (0, 1)]
    if horizon >= 2:
        vals += [q_cycle(set_bit(set_bit(bits, i, a), j, b))
                 for i in range(len(bits)) for a in (0, 1)
                 for j in range(len(bits)) for b in (0, 1)]
    return tuple(vals)


def collision_report(n, horizon):
    buckets = {}
    for u in product((0, 1), repeat=n):
        buckets.setdefault(cycle_signature(u, horizon), []).append(u)
    collision_classes = [v for v in buckets.values() if len(v) > 1]
    return {'n': n, 'horizon': horizon, 'distinct_signatures': len(buckets),
            'collision_classes': len(collision_classes),
            'colliding_states': sum(map(len, collision_classes)),
            'largest_class': max(map(len, buckets.values()))}


def graph_cost(vertices, edges, W, selected):
    assert selected <= W
    return 2 * len(selected) + sum(a not in selected and b not in selected for a, b in edges)


def exact_graph_min(vertices, edges, W):
    w = sorted(W)
    best = None
    witness = None
    for z in range(1 << len(w)):
        s = {v for j,v in enumerate(w) if z >> j & 1}
        cost = graph_cost(vertices, edges, W, s)
        if best is None or cost < best:
            best, witness = cost, s
    return best, witness


def windmill(k):
    verts = list(range(2*k + 1))
    triangles = [(0, 2*i+1, 2*i+2) for i in range(k)]
    edges = [(a,b) for a,b,c in triangles] + [(a,c) for a,b,c in triangles] + [(b,c) for a,b,c in triangles]
    return verts, triangles, edges


def cactus_dp(triangles, W):
    """Exact binary factor-tree messages for a triangular cactus."""
    adjacency = {}
    for t,tri in enumerate(triangles):
        for v in tri:
            adjacency.setdefault(v, []).append(t)
    root = min(adjacency)

    def vm(v, excluded_t):
        arr = []
        for s in (0,1):
            if s and v not in W:
                arr.append(float('inf'))
            else:
                arr.append(2*s + sum(tm(t, v)[s] for t in adjacency[v] if t != excluded_t))
        return arr

    def tm(t, parent_v):
        x,y = [v for v in triangles[t] if v != parent_v]
        mx, my = vm(x,t), vm(y,t)
        return [min(mx[a] + my[b] + (1-s)*(1-a) + (1-s)*(1-b) + (1-a)*(1-b)
                    for a in (0,1) for b in (0,1)) for s in (0,1)]

    return min(vm(root, None))


def grow_triangular_cactus(k, pattern):
    # Build a cactus of k triangles by adding two fresh vertices per block,
    # attaching to an existing vertex. No two blocks share an edge.
    triangles = [(0, 1, 2)]
    next_v = 3
    for t in range(1, k):
        available = sorted(set(v for tr in triangles for v in tr))
        center = available[(t * 7 + pattern * 3) % len(available)]
        triangles.append((center, next_v, next_v+1))
        next_v += 2
    return triangles


OLD_CORES = [set(map(int, s)) for s in ('0125', '0135', '0235', '0245', '0246')]
NEW_A_CORES = [(set(map(int,s)), first) for s,first in
               [('1235',1),('1245',1),('1246',1),('1345',0),('1346',0)]]


def verify_source_labeled_cover(verts, edges, S):
    # All targets have two-hot edge suffix; source labels encode core,
    # first-bit and original helper/edge suffix; no numeric approximation.
    def edge_word(e): return frozenset(e)
    sources = []
    for e in edges: sources.append((1, 0, edge_word(e)))
    for v in S:
        sources.extend([(0,1,frozenset([v])), (4,1,frozenset([v]))])
    for e in edges:
        if e[0] not in S and e[1] not in S:
            sources.append((0,1,edge_word(e)))
    assert len(sources) == len(edges) + 2*len(S) + sum(a not in S and b not in S for a,b in edges)
    for e in edges:
        y = edge_word(e)
        for core,t in NEW_A_CORES:
            if not any(len(core-OLD_CORES[j]) + int(t!=s) + len(x^y) <= 2
                       for j,s,x in sources):
                raise AssertionError((e, ''.join(map(str,sorted(core))),t,sorted(S)))
    return len(sources)


def exact_cactus_checks():
    checked = 0
    sample = []
    for k in range(1, 6):
        for pattern in range(4):
            triangles = grow_triangular_cactus(k, pattern)
            verts = sorted(set(v for tri in triangles for v in tri))
            edges = sorted({tuple(sorted((a,b))) for tri in triangles
                            for a,b in ((tri[0],tri[1]), (tri[0],tri[2]), (tri[1],tri[2]))})
            masks = [0, (1<<len(verts))-1]
            masks += [sum((1<<j) for j in range(len(verts)) if (j+pattern) % r == 0)
                      for r in (2,3,4)]
            for mask in sorted(set(masks)):
                W = {v for j,v in enumerate(verts) if mask >> j & 1}
                brute, witness = exact_graph_min(verts, edges, W)
                dp = cactus_dp(triangles, W)
                assert brute == dp, (triangles, W, brute, dp)
                assert verify_source_labeled_cover(verts, edges, witness) == len(edges) + brute
                checked += 1
                if k == 5 and pattern == 2:
                    sample.append({'allowed': sorted(W), 'extra_cost': brute,
                                   'kappa_a': len(edges) + brute,
                                   'source_helper_vertex_ids':sorted(witness)})
    return checked, sample


def exact_windmill_checks():
    count = 0
    rows = []
    for k in range(1, 6):
        verts,triangles,edges = windmill(k)
        for has_hub in (False, True):
            W = ({0} if has_hub else set()) | set(verts[1:])
            brute, witness = exact_graph_min(verts,edges,W)
            expected = k+2 if has_hub else 3*k
            assert brute == expected, (k,has_hub,brute,expected)
            assert verify_source_labeled_cover(verts, edges, witness) == len(edges) + brute
            count += 1
            rows.append({'triangles':k, 'hub_available':has_hub,
                         'kappa_a':len(edges)+brute, 'kappa_ab':2*len(edges),
                         'optimal_helper_set':sorted(witness)})
    return count,rows


def main():
    cycle = [collision_report(n,1) for n in range(3,13)]
    for item in cycle:
        n=item['n']
        expected_classes=2 if n%4 == 0 else 0
        assert item['collision_classes']==expected_classes, item
        assert item['distinct_signatures']==(1<<n)-expected_classes, item
        assert item['largest_class']==(2 if expected_classes else 1), item
    # All original masks and every 0/1 set-command word of length <=2.
    horizon2 = [collision_report(n,2) for n in range(3,9)]
    assert all(row['distinct_signatures'] == 1<<row['n'] for row in horizon2)
    nwind,wind=exact_windmill_checks()
    ncactus,sample=exact_cactus_checks()
    result = {
        'name':'R5_BRANCHING_CACTUS_AND_HORIZON_TWO',
        'status':'PASS_R5_BRANCHING_CACTUS_AND_HORIZON_TWO',
        'model':'auxiliary source-labeled radius-2 indexed-center graph kernel',
        'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'cycle_horizon_one_exhaustive_n':list(range(3,13)),
        'cycle_horizon_one':cycle,
        'cycle_horizon_two_exhaustive_n':list(range(3,9)),
        'cycle_horizon_two':horizon2,
        'windmill_complete_numeric_checks':nwind,
        'windmill':wind,
        'triangular_cactus_exhaustive_selection_checks':ncactus,
        'source_labeled_cover_checks': nwind+ncactus,
        'triangular_cactus_example':sample,
        'verification_scope': 'All masks n=3..12 horizon1; all masks n=3..8 all length<=2 command words; exact all subset graph minimization for windmill k<=5; five helper masks for each of 4 deterministic cactus shapes at k<=5',
        'review':'NOT_REVIEWED'
    }
    print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))

if __name__ == '__main__':
    main()
