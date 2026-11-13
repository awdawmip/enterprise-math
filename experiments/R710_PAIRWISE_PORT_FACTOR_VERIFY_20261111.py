#!/usr/bin/env python3
"""R710: exact edge-factorized admissibility check, no native physics execution."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
V=range(6)
P={frozenset(t) for t in [(0,1,2),(0,3,4),(1,3,5),(2,4,5)]}
U=frozenset(V)
E=tuple(map(frozenset,combinations(V,2)))
T=tuple(map(frozenset,combinations(V,3)))
req=set().union(*(set(map(frozenset,combinations(t,2))) for t in P))
missing=set(E)-req
assert missing==set(map(frozenset,[(0,5),(1,4),(2,3)]))

def triangles(G):
    return {t for t in T if all(frozenset(pair) in G for pair in combinations(t,2))}

def covers(H):
    return sum((U-t) in H for t in H)//2

H0=triangles(req)
assert H0==P|{U-t for t in P}
assert len(H0)==8 and covers(H0)==4
hist=Counter()
valid=0
for mask in range(1<<len(E)):
    G={e for j,e in enumerate(E) if mask>>j&1}
    H=triangles(G)
    if P<=H:
        assert req<=G
        assert H0<=H
        assert covers(H)>=4
        valid+=1
        hist[covers(H)]+=1
assert valid==8
assert sum(hist.values())==8
out={"schema":"EM_R710_PAIRWISE_PORT_FACTOR_EXACT_EVIDENCE_V1",
     "task":"RS-X6-TRIADIC-CLOSURE-DYNAMICS",
     "frozen_science":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
     "date":"2026-11-11","candidate_pasches":4,
     "forced_pairwise_graph_edges":len(req),
     "missing_pairs":[list(sorted(e)) for e in sorted(missing,key=lambda e:tuple(sorted(e)))],
     "minimum_graph_triangle_count":8,
     "minimum_graph_complementary_pairs":4,
     "six_vertex_simple_graph_count":1<<len(E),
     "graphs_containing_pasch_as_triangles":valid,
     "full_integer_cover_histogram":dict(sorted(hist.items())),
     "status":"R710_PAIRWISE_PORT_FACTOR_EXACT_PASS",
     "scope":"candidate pairwise clique eligibility; not derived from native X6 Link/Port event"}
Path(__file__).with_name("R710_PAIRWISE_PORT_FACTOR_EVIDENCE_20261111.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
print(out['status'],len(E),valid,len(req),len(H0),covers(H0),dict(hist))
