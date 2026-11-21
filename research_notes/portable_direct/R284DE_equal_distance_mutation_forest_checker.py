#!/usr/bin/env python3
"""Exact frozen-Port equal-distance source-mutation forest and quotient census.

Run alongside the pinned R284CO and R284DD checkers, using Python standard
library. Compare all 64 arc values at all 65,536 sites and exhaust every
legal local mutation edge independently of the 420-pair joining method.
"""
import hashlib
import json
from collections import Counter, defaultdict
from R284CO_spectral_witness_checker import words, arcs, dist, FROZEN_SHA
from R284DD_attributed_envelope_checker import attributed_envelope, labeled_farthest

EXPECTED_EDGE_SHA = '251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b'

def main():
    X, A = words(), arcs()
    T, profiles = attributed_envelope(A)
    profile = [labeled_farthest(x, T, profiles, len(A)) for x in X]
    assert all(len(labels) == 1 for _, labels in profile)
    # Fully independent 4,194,304 nearest-arc distances.
    baseline = []
    for x in X:
        ds = [dist(x, arc) for arc in A]
        d = max(ds)
        baseline.append((d, tuple(i for i, z in enumerate(ds) if z == d)))
    assert profile == baseline
    D = [d for d, _ in profile]
    fiber_sizes = Counter(D)
    assert Counter(fiber_sizes.values()) == Counter({1:64760, 2:366, 3:8, 4:5})

    # Independent exhaustive scan of all 1,474,560 undirected edges.
    # Top four bits are never modified.
    edges, attempts = [], 0
    for i in range(len(X)):
        for bit in range(12):
            j = i ^ (1 << bit)
            if i < j:
                attempts += 1
                if D[i] == D[j]:
                    p = 11-bit
                    edges.append(('flip',str(p),i,j,D[i],p,-1))
        for b in range(12):
            for a in range(b):
                if ((i >> a) ^ (i >> b)) & 1:
                    j = i ^ (1 << a) ^ (1 << b)
                    if i < j:
                        attempts += 1
                        if D[i] == D[j]:
                            p,q = 11-b,11-a
                            edges.append(('swap',f'{p},{q}',i,j,D[i],p,q))
    assert attempts == 1474560 and len(edges) == 307
    edges.sort(key=lambda e:(e[2], 0 if e[0]=='flip' else 1, e[5], e[6]))
    canonical = [[kind,mut,i,j,d,profile[i][1][0],profile[j][1][0]]
                 for kind,mut,i,j,d,_,_ in edges]
    digest = hashlib.sha256(json.dumps(canonical, separators=(',',':'),
                      ensure_ascii=False).encode()).hexdigest()
    assert digest == EXPECTED_EDGE_SHA

    adj = defaultdict(set)
    for kind,mut,i,j,d,p,q in edges:
        adj[i].add(j); adj[j].add(i)
    seen, shapes, path3 = set(), Counter(), []
    for start in sorted(adj):
        if start in seen: continue
        seen.add(start); todo=[start]; component=[]
        while todo:
            v=todo.pop(); component.append(v)
            for w in adj[v]:
                if w not in seen: seen.add(w); todo.append(w)
        component.sort()
        n, e = len(component), sum(len(adj[v]) for v in component)//2
        shapes[(n,e,e-n+1)]+=1
        if n==3:
            path3.append({'indices': component, 'residues':[X[v] for v in component],
                          'distance':D[component[0]],
                          'winning_arcs':[profile[v][1][0] for v in component],
                          'upper':component[0]//4096})
    assert shapes==Counter({(2,1,0):303,(3,2,0):2})
    assert len(adj)==612 and len(seen)==612
    assert 65536-len(edges)==65229
    assert len(fiber_sizes)==65139

    report={
      'schema':'R284DE_FROZEN_EQUAL_DISTANCE_MUTATION_FOREST_V1',
      'frozen_sha256':FROZEN_SHA,'independent_arc_distance_tests':len(X)*len(A),
      'legal_undirected_mutation_edges_tested':attempts,
      'equal_distance_mutation_edges':len(edges),
      'equal_distance_edge_sha256':digest,
      'nonisolated_vertices':len(adj),
      'component_types':[{'vertices':v,'edges':e,'cycle_rank':cy,'count':count}
            for (v,e,cy),count in sorted(shapes.items())],
      'all_graph_components_including_isolates':65229,
      'distinct_farthest_values':len(fiber_sizes),
      'excess_mutation_component_classes_over_value_classes':90,
      'three_vertex_paths':path3,
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'scope':'frozen 34-bit Port auxiliary observer, not native X6'
    }
    print(json.dumps(report,ensure_ascii=False,indent=2))
    with open('R284DE_equal_distance_mutation_forest_certificate.json','w',encoding='utf8') as out:
        json.dump(report,out,ensure_ascii=False,indent=2)
        out.write('\n')

if __name__ == '__main__': main()
