#!/usr/bin/env python3
"""X6 Unit140: source-equivalent Delaunay/dual adjacency on noninjective labelled carrier sites.

Original function bodies follow git blob 900e246b0dafaa35d2452191e3df508a2d15a389,
lines 87--235 of scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py.
This checker does not execute the original full historical script.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import json

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

def orient(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def sqnorm(p):return p[0]*p[0]+p[1]*p[1]
def euclidean_sqdist(a,b):return sqnorm((a[0]-b[0],a[1]-b[1]))

def circumcircle(a,b,c):
    ax,ay=a;bx,by=b;cx,cy=c
    a11=2*(bx-ax); a12=2*(by-ay);a21=2*(cx-ax);a22=2*(cy-ay)
    r1=sqnorm(b)-sqnorm(a);r2=sqnorm(c)-sqnorm(a)
    det=a11*a22-a12*a21
    if det==0:return None
    ux=(r1*a22-a12*r2)/det
    uy=(a11*r2-r1*a21)/det
    center=(ux,uy)
    return center,euclidean_sqdist(center,a)

def empty_circle_certificate(sites,triple):
    points=dict(sites)
    circle=circumcircle(*(points[label] for label in triple))
    if circle is None:return None
    center,radius2=circle
    inside,boundary,outside=[],[],[]
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

def convex_hull_labels(boundary,sites):
    points=dict(sites)
    ordered=sorted((points[label][0],points[label][1],label) for label in boundary)
    if len(ordered)<=1:return tuple(item[2] for item in ordered)
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for point in ordered:
        while len(lower)>=2 and cross(lower[-2],lower[-1],point)<=0:lower.pop()
        lower.append(point)
    upper=[]
    for point in reversed(ordered):
        while len(upper)>=2 and cross(upper[-2],upper[-1],point)<=0:upper.pop()
        upper.append(point)
    hull=lower[:-1]+upper[:-1]
    return tuple(item[2] for item in hull)

def delaunay_cell_edges(sites,cells):
    edges=set()
    for boundary in cells:
        hull=convex_hull_labels(boundary,sites)
        if len(hull)==2:edges.add(frozenset(hull))
        elif len(hull)>=3:
            for i,label in enumerate(hull):
                edges.add(frozenset((label,hull[(i+1)%len(hull)])))
    return frozenset(edges)


def main():
    lattice=tuple((F(x),F(y)) for x in (-1,0,1) for y in (-1,0,1))
    counts=Counter()
    first=None
    for coords in product(lattice,repeat=4):
        labels=[(f'S{i}',p) for i,p in enumerate(coords)]
        uq=tuple(sorted(set(coords)))
        if len(uq)==3 and orient(*uq)!=0:
            de=dual_edges(labels)
            ce=delaunay_cell_edges(labels,delaunay_cells(labels))
            if len(de)!=6 or len(ce)!=3 or not ce<=de:
                raise AssertionError(f'source unexpected ({coords}): {len(de)} {len(ce)}')
            counts['three_unique_noncollinear_missing_three_edges']+=1
            if first is None:
                first={'labels':{l:[int(x),int(y)] for l,(x,y) in labels},
                       'source_dual_edges':[sorted(e) for e in sorted(de,key=lambda e:sorted(e))],
                       'source_delaunay_edges':[sorted(e) for e in sorted(ce,key=lambda e:sorted(e))]}
        elif len(uq)==4:
            de=dual_edges(labels)
            ce=delaunay_cell_edges(labels,delaunay_cells(labels))
            if de!=ce:
                counts['four_unique_mismatch']+=1
                raise AssertionError(f'distinct rank-two mismatch: {coords} / dual {de} / primal {ce}')
            else:counts['four_unique_equal']+=1
        else:
            counts['other_domain']+=1
    if counts['three_unique_noncollinear_missing_three_edges'] != 2736:
        raise AssertionError('not exhaustive expected noncollinear 2736')
    cert={'schema':'X6_UNIT140_DUAL_DELAUNAY_COINCIDENT_CARRIER_CONSUMER_V1',
          'source_blob':'900e246b0dafaa35d2452191e3df508a2d15a389',
          'coverage':'ordered 4-label configurations on 9-point grid [-1,1]^2',
          'total_cases':9**4,'counts':dict(sorted(counts.items())),'example':first,
          'execution_scope':'source-equivalent replicas of seven original functions; original full script not run',
          'status':'UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(cert,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
