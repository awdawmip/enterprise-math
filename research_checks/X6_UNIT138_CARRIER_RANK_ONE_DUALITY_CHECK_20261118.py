#!/usr/bin/env python3
"""Independent exact witness for frozen/current 2026-08-23 carrier Voronoi
consumer (blob 900e246b0dafaa35d2452191e3df508a2d15a389).
This copies the relevant function logic, not an import or execution of the full
historical program, and does not test/replace any native X6 benchmark.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import hashlib
import json


def check(condition, msg):
    if not condition:
        raise RuntimeError(msg)


def sqnorm(p):
    return p[0] * p[0] + p[1] * p[1]


def euclidean_sqdist(a, b):
    return sqnorm((a[0]-b[0],a[1]-b[1]))


def circumcircle(a,b,c):
    ax,ay=a;bx,by=b;cx,cy=c
    a11=2*(bx-ax);a12=2*(by-ay)
    a21=2*(cx-ax);a22=2*(cy-ay)
    r1=sqnorm(b)-sqnorm(a);r2=sqnorm(c)-sqnorm(a)
    det=a11*a22-a12*a21
    if det==0: return None
    ux=(r1*a22-a12*r2)/det;uy=(a11*r2-r1*a21)/det
    center=(ux,uy)
    return center, euclidean_sqdist(center,a)


def empty_circle_certificate(sites,triple):
    points=dict(sites)
    circle=circumcircle(*(points[label] for label in triple))
    if circle is None:return None
    center,radius2=circle
    inside=[];boundary=[];outside=[]
    for label,point in sites:
        d2=euclidean_sqdist(center,point)
        if d2<radius2:inside.append(label)
        elif d2==radius2:boundary.append(label)
        else:outside.append(label)
    return center,radius2,tuple(sorted(inside)),tuple(sorted(boundary)),tuple(sorted(outside))


def delaunay_cells(sites):
    labels=[label for label,_ in sites]
    valid={}
    for triple in combinations(labels,3):
        cert=empty_circle_certificate(sites,triple)
        if cert is None:continue
        center,radius2,inside,boundary,_=cert
        if not inside: valid[frozenset(boundary)]=(center,radius2)
    keys=list(valid)
    maximal=[key for key in keys if not any(key<other for other in keys)]
    return {key:valid[key] for key in maximal}


def dual_adjacent(sites,left,right):
    points=dict(sites);a,b=points[left],points[right]
    midpoint=((a[0]+b[0])/2,(a[1]+b[1])/2)
    v=(b[0]-a[0],b[1]-a[1]);perp=(-v[1],v[0])
    lo=None;hi=None
    def x_of(t):return midpoint[0]+t*perp[0],midpoint[1]+t*perp[1]
    for label,other in sites:
        if label in(left,right):continue
        f0=euclidean_sqdist(x_of(F(0)),a)-euclidean_sqdist(x_of(F(0)),other)
        f1=euclidean_sqdist(x_of(F(1)),a)-euclidean_sqdist(x_of(F(1)),other)
        slope=f1-f0;intercept=f0
        if slope==0:
            if intercept>0:return False
        elif slope>0:
            bound=-intercept/slope
            hi=bound if hi is None or bound<hi else hi
        else:
            bound=-intercept/slope
            lo=bound if lo is None or bound>lo else lo
        if lo is not None and hi is not None and lo>hi:return False
    return not(lo is not None and hi is not None and lo==hi)


def dual_edges(sites):
    labels=[label for label,_ in sites]
    return frozenset(frozenset((a,b))for a,b in combinations(labels,2) if dual_adjacent(sites,a,b))


def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def expected_collinear_edges(sites):
    points={label:p for label,p in sites}
    a=sites[0][1];b=next(p for _,p in sites[1:] if p!=a)
    v=(b[0]-a[0],b[1]-a[1])
    order=sorted(sites,key=lambda item:(item[1][0]-a[0])*v[0]+(item[1][1]-a[1])*v[1])
    return frozenset(frozenset((order[i][0],order[i+1][0]))for i in range(len(order)-1))


def main():
    coords=[(F(a),F(b))for a in range(-2,3)for b in range(-2,3)]
    count=Counter();first={};mismatches=[]
    for tri in combinations(coords,3):
        sites=list(zip(('A','B','C'),tri))
        isline=orient(*tri)==0
        cells=delaunay_cells(sites)
        edges=dual_edges(sites)
        k='rank_one' if isline else 'rank_two'
        count[k]+=1
        if k not in first:first[k]={'sites':[list(map(int,p))for p in tri]}
        if isline:
            count['rank_one_empty_delaunay']+=not bool(cells)
            count['rank_one_two_voronoi_edges']+=len(edges)==2
            count['rank_one_edges_are_sorted_neighbors']+=edges==expected_collinear_edges(sites)
            if cells or len(edges)!=2 or edges!=expected_collinear_edges(sites):
                mismatches.append((tri,cells,edges))
        else:
            count['rank_two_one_delaunay_triangle']+=set(cells)=={frozenset(('A','B','C'))}
            count['rank_two_three_voronoi_edges']+=len(edges)==3
            if set(cells)!={frozenset(('A','B','C'))} or len(edges)!=3:mismatches.append((tri,cells,edges))
    check(not mismatches, f'Unexpected discrepancy {mismatches[:3]}')
    check(count['rank_one']>0 and count['rank_two']>0,'empty stratum')
    for s in ['rank_one_empty_delaunay','rank_one_two_voronoi_edges','rank_one_edges_are_sorted_neighbors']:
        check(count[s]==count['rank_one'],s)
    for s in ['rank_two_one_delaunay_triangle','rank_two_three_voronoi_edges']:
        check(count[s]==count['rank_two'],s)
    witness=[('A',(F(0),F(0))),('B',(F(1),F(0))),('C',(F(2),F(0)))]
    check(delaunay_cells(witness)=={},'witness 2D Delaunay')
    check(dual_edges(witness)==frozenset((frozenset(('A','B')),frozenset(('B','C')))),'witness Voronoi')
    result={'schema':'X6_UNIT138_BOUNDED_SOURCE_CONSUMER_DIAGNOSTIC_V1','source_git_blob_sha1':'900e246b0dafaa35d2452191e3df508a2d15a389','original_executable_imported':False,'scope':'all 2300 unordered triples of distinct sites from [-2,2]^2 Euclidean carrier, relevant functions exact source-derived replicas','counts':dict(sorted(count.items())),'witness':{'sites':[[0,0],[1,0],[2,0]],'original_delaunay_cells':[],'original_dual_edges':[['A','B'],['B','C']]},'theorem_scope':'Three distinct collinear Euclidean sites: nearest-site Voronoi codim-1 edges are exactly consecutive collinear sites; original maximal-noncollinear-triple Delaunay routine has no cell; this is a rank-1 interface gap, not signed X6 native failure.','all_guard_checks_pass':True,'R063_original_benchmark_rerun':False}
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    print(data.decode(),end='')

if __name__=='__main__':main()
