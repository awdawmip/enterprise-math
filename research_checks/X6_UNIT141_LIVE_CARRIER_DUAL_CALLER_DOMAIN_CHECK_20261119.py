#!/usr/bin/env python3
"""Unit141: exact finite typed caller-domain closure, original source blob 900e246b...
Carrier-only evidence; does not run or modify the frozen signed X6 benchmark.
"""
import json
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter

SOURCE_BLOB = '900e246b0dafaa35d2452191e3df508a2d15a389'

class CarrierDomainError(ValueError):
    pass

def orientation(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def typed_domain(sites):
    labels = [n for n,_ in sites]
    points = [p for _,p in sites]
    if len(labels) != len(set(labels)):
        raise CarrierDomainError('DUPLICATE_LABEL')
    if len(points) != len(set(points)):
        raise CarrierDomainError('COINCIDENT_POSITION')
    if not any(orientation(a,b,c) != 0 for a,b,c in combinations(points,3)):
        raise CarrierDomainError('AFFINE_RANK_LT_2')
    return True

def sqdist(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

def source_dual_adjacent(sites,left,right):
    points=dict(sites);a,b=points[left],points[right]
    m=((a[0]+b[0])/2,(a[1]+b[1])/2)
    perp=(-(b[1]-a[1]),b[0]-a[0]);lo=hi=None
    def x(t):return(m[0]+t*perp[0],m[1]+t*perp[1])
    for label,other in sites:
        if label in (left,right):continue
        f0=sqdist(x(F(0)),a)-sqdist(x(F(0)),other)
        f1=sqdist(x(F(1)),a)-sqdist(x(F(1)),other)
        slope=f1-f0
        if slope==0:
            if f0>0:return False
        elif slope>0:
            hi=min(hi,-f0/slope) if hi is not None else -f0/slope
        else:
            lo=max(lo,-f0/slope) if lo is not None else -f0/slope
        if lo is not None and hi is not None and lo>hi:return False
    return not(lo is not None and hi is not None and lo==hi)

def source_dual_edges(sites):
    return frozenset(frozenset((a,b)) for a,b in combinations([n for n,_ in sites],2)
                     if source_dual_adjacent(sites,a,b))

def circle(a,b,c):
    aa=2*(b[0]-a[0]);ab=2*(b[1]-a[1]);ba=2*(c[0]-a[0]);bb=2*(c[1]-a[1])
    rhs1=b[0]**2+b[1]**2-a[0]**2-a[1]**2
    rhs2=c[0]**2+c[1]**2-a[0]**2-a[1]**2
    det=aa*bb-ab*ba
    if det==0:return None
    center=((rhs1*bb-ab*rhs2)/det,(aa*rhs2-rhs1*ba)/det)
    return center,sqdist(center,a)

def source_delaunay_cells(sites):
    points=dict(sites);valid={}
    for triple in combinations([n for n,_ in sites],3):
        candidate=circle(*(points[n] for n in triple))
        if candidate is None:continue
        c,r=candidate
        inside=[n for n,p in sites if sqdist(c,p)<r]
        if not inside:
            boundary=frozenset(n for n,p in sites if sqdist(c,p)==r)
            valid[boundary]=(c,r)
    return {k:v for k,v in valid.items() if not any(k<o for o in valid)}

def source_hull_labels(boundary,sites):
    points=dict(sites)
    ordered=sorted((points[n][0],points[n][1],n) for n in boundary)
    if len(ordered)<=1:return tuple(p[2] for p in ordered)
    def cross(o,a,b):return(a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in ordered:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(ordered):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return tuple(p[2] for p in lo[:-1]+hi[:-1])

def source_cell_edges(sites,cells):
    edges=set()
    for boundary in cells:
        hull=source_hull_labels(boundary,sites)
        if len(hull)==2:edges.add(frozenset(hull))
        elif len(hull)>=3:
            for i,n in enumerate(hull):edges.add(frozenset((n,hull[(i+1)%len(hull)])))
    return frozenset(edges)

def guarded_comparison(sites):
    typed_domain(sites)
    return source_dual_edges(sites)==source_cell_edges(sites,source_delaunay_cells(sites))

def encode_edges(e):return sorted(sorted(edge) for edge in e)

def main():
    generic=[('A',(F(0),F(0))),('B',(F(4),F(0))),('C',(F(0),F(3))),('D',(F(5),F(4)))]
    square=[('A',(F(0),F(0))),('B',(F(2),F(0))),('C',(F(2),F(2))),('D',(F(0),F(2)))]
    examples={}
    for name,sites in [('generic',generic),('square',square)]:
        if not guarded_comparison(sites):raise RuntimeError('original current run equality failed: '+name)
        edges=encode_edges(source_dual_edges(sites));examples[name]=edges
    if len(examples['generic'])!=5 or len(examples['square'])!=4:
        raise RuntimeError('unexpected source consumer edge cardinality')
    grid=tuple((F(x),F(y)) for x in (-1,0,1) for y in (-1,0,1))
    counts=Counter()
    for ps in product(grid,repeat=4):
        sites=[('S'+str(i),p) for i,p in enumerate(ps)]
        try:good=guarded_comparison(sites)
        except CarrierDomainError as e:counts[str(e)]+=1
        else:
            if not good:raise RuntimeError('typed source-equivalent mismatch: '+repr(ps))
            counts['ACCEPT_EQ_TRUE']+=1
    if counts['ACCEPT_EQ_TRUE']!=3024 or counts['COINCIDENT_POSITION']!=3537:
        raise RuntimeError('unexpected exhaustive domain partition '+repr(counts))
    for name,sites,expected in [
        ('duplicate_position',[('A',(F(0),F(0))),('AA',(F(0),F(0))),('B',(F(1),F(0))),('C',(F(0),F(1)))],'COINCIDENT_POSITION'),
        ('rank_one',[('A',(F(0),F(0))),('B',(F(1),F(0))),('C',(F(2),F(0))),('D',(F(3),F(0)))],'AFFINE_RANK_LT_2'),
        ('duplicate_label',[('A',(F(0),F(0))),('A',(F(1),F(0))),('B',(F(0),F(1)))],'DUPLICATE_LABEL')]:
        try:guarded_comparison(sites)
        except CarrierDomainError as e:
            if str(e)!=expected:raise RuntimeError('wrong rejection for '+name)
        else:raise RuntimeError('missing rejection for '+name)
        counts['EXPLICIT_REJECT_'+name.upper()]+=1
    result={'schema':'X6_UNIT141_CURRENT_CARRIER_CALLER_TYPED_DOMAIN_V1','source_blob':SOURCE_BLOB,
            'source_lines':'original current run() 365-426; source functions 88-254',
            'scope':'finite exact source-equivalent methods, not native X6 and not original full program',
            'enumeration':'4 named labels, ordered placements in [-1,1]^2',
            'total_assignments':9**4,'counts':dict(sorted(counts.items())),
            'current_source_caller_edges':examples,'status':'AUTHOR_CHECKED_UNREVIEWED_NOT_ADMITTED'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
