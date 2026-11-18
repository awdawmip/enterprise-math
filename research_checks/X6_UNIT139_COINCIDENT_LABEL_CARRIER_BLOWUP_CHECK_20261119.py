#!/usr/bin/env python3
"""X6 Unit139: finite exact rational site-identity blow-up check.

Replicates the dual_adjacent/dual_edges implementation from:
awdawmip/enterprise-math:scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py
Git blob 900e246b0dafaa35d2452191e3df508a2d15a389, lines 157--209.
Independent finite checker: original full script is not executed.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
import hashlib, json


def sqdist(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2


def dual_adjacent(sites,left,right):
    points=dict(sites)
    a,b=points[left],points[right]
    midpoint=((a[0]+b[0])/2,(a[1]+b[1])/2)
    v=(b[0]-a[0],b[1]-a[1])
    perp=(-v[1],v[0])
    lo=hi=None
    def x_of(t): return (midpoint[0]+t*perp[0],midpoint[1]+t*perp[1])
    for label,other in sites:
        if label in (left,right): continue
        f0=sqdist(x_of(F(0)),a)-sqdist(x_of(F(0)),other)
        f1=sqdist(x_of(F(1)),a)-sqdist(x_of(F(1)),other)
        slope=f1-f0;intercept=f0
        if slope==0:
            if intercept>0: return False
        elif slope>0:
            bound=-intercept/slope
            hi=bound if hi is None or bound<hi else hi
        else:
            bound=-intercept/slope
            lo=bound if lo is None or bound>lo else lo
        if lo is not None and hi is not None and lo>hi: return False
    return not (lo is not None and hi is not None and lo==hi)


def dual_edges(sites):
    labels=[label for label,_ in sites]
    return frozenset(frozenset((a,b)) for a,b in combinations(labels,2)
                     if dual_adjacent(sites,a,b))


def quotient_expected(sites):
    # Quotient by exact coordinate; preserve full label preimages.
    positions=sorted(set(p for _,p in sites))
    groups={p:tuple(l for l,q in sites if p==q) for p in positions}
    reduced=[('u'+str(i),p) for i,p in enumerate(positions)]
    qgraph=dual_edges(reduced)
    expected=set()
    for p,ls in groups.items():
        for x,y in combinations(ls,2): expected.add(frozenset((x,y)))
    for edge in qgraph:
        l1,l2=sorted(edge)
        p1,p2=dict(reduced)[l1],dict(reduced)[l2]
        for x in groups[p1]:
            for y in groups[p2]: expected.add(frozenset((x,y)))
    return frozenset(expected),qgraph


def main():
    pts=tuple((F(x),F(y)) for x in (-1,0,1) for y in (-1,0,1))
    tested=0; repeated=0; duplicate_pairs=0; malformed=0
    histogram={}; witness=None
    for n in (2,3,4):
        c=Counter()
        for coord_tuple in product(pts,repeat=n):
            sites=[(f'S{i}',p) for i,p in enumerate(coord_tuple)]
            actual=dual_edges(sites)
            expected,qgraph=quotient_expected(sites)
            if actual!=expected:
                raise AssertionError(f'blowup mismatch {sites}: {actual ^ expected}')
            n_duplicates=sum(len(g)*(len(g)-1)//2 for g in (
                [i for i,p in enumerate(coord_tuple) if p==pos] for pos in set(coord_tuple)))
            for a,b in combinations(range(n),2):
                if coord_tuple[a]==coord_tuple[b] and frozenset((f'S{a}',f'S{b}')) not in actual:
                    raise AssertionError('coincident pair missing source graph edge')
            if n_duplicates:
                repeated+=1
                duplicate_pairs+=n_duplicates
                if witness is None and n>=3:
                    witness={'n':n,'positions':[[int(p[0]),int(p[1])] for p in coord_tuple],
                            'source_edge_count':len(actual),'quotient_edges':len(qgraph),
                            'source_edges':[sorted(e) for e in sorted(actual,key=lambda e:sorted(e))]}
            tested+=1
            c[f'unique_{len(set(coord_tuple))}']+=1
        histogram[str(n)]=dict(sorted(c.items()))
    cert={'schema':'X6_UNIT139_COINCIDENT_LABEL_CARRIER_BLOWUP_EXACT_V1',
          'source_path':'scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py',
          'source_blob':'900e246b0dafaa35d2452191e3df508a2d15a389',
          'domain':'all labelled n=2,3,4-site ordered coordinate tuples in [-1,1]^2 integer grid',
          'total_cases':tested,'duplicate_position_cases':repeated,
          'coincident_label_pair_instances':duplicate_pairs,
          'cases_by_n_and_unique_positions':histogram,
          'blowup_mismatches':0,
          'example':witness,
          'check_type':'rational-exact source-equivalent replica; original full script not run',
          'review':'UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(cert,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
