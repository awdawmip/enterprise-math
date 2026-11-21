"""Exact endpoint overlap kernels after the Farey width reduction."""
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json

@lru_cache(None)
def pairs(poly):
    return tuple((b[0]-a[0],b[1]-a[1]) for a,b in combinations(poly,2))

@lru_cache(None)
def width_breaks(poly):
    return tuple(sorted(set(-F(x,y)for x,y in pairs(poly) if y)))

def support(poly,r):
    lo=None;hi=None
    for x,y in pairs(poly):
        if not y:
            if abs(x)*r>=1:return None
        else:
            l,h=sorted([(-1/r-x)/y,(1/r-x)/y])
            lo=l if lo is None else max(lo,l)
            hi=h if hi is None else min(hi,h)
    if lo>=hi:return None
    return lo,hi

def width_line(poly,t):
    low=min(poly,key=lambda p:p[0]+p[1]*t)
    high=max(poly,key=lambda p:p[0]+p[1]*t)
    return high[0]-low[0],high[1]-low[1]

def width_pieces(poly):
    cuts=width_breaks(poly)
    bounds=[None]+list(cuts)+[None]
    out=[]
    for l,h in zip(bounds,bounds[1:]):
        t=h-1 if l is None else l+1 if h is None else (l+h)/2
        A,B=width_line(poly,t)
        if out and out[-1][2:]==(A,B):out[-1]=(out[-1][0],h,A,B)
        else:out.append((l,h,A,B))
    return out

def zero_shift_identity():
    from collections import defaultdict
    atoms=defaultdict(F);intervals=[];breaks={F(0)}
    for p,c in load_terms():
        for l,h,A,B in width_pieces(p):
            if B==0:
                assert l is not None and h is not None
                atoms[F(A)]+=c*(h-l)
            else:
                vals=[None if t is None else A+B*t for t in [l,h]]
                low=min(x for x in vals if x is not None)
                high=None if None in vals else max(vals)
                intervals.append((low,high,c/abs(B)));breaks.add(low)
                if high is not None:breaks.add(high)
    breaks=sorted(breaks)
    density=[]
    for l,h in zip(breaks,breaks[1:]+[None]):
        t=l+1 if h is None else (l+h)/2
        value=sum((c for low,high,c in intervals if low<t and(high is None or t<high)),F(0))
        density.append((l,h,value))
    return {'atoms':[(str(x),str(c))for x,c in sorted(atoms.items())if c],
            'density':[(str(l),str(h),str(c))for l,h,c in density]}

def kernel(poly,a,r,s):
    r,s,a=F(r),F(s),F(a);p=support(poly,r);q=support(poly,s)
    if p is None or q is None:return F(0)
    u=a/(r*s);lo=max(p[0],q[0]+u);hi=min(p[1],q[1]+u)
    if lo>=hi:return F(0)
    cuts=sorted(set([lo,hi]+[x for x in width_breaks(poly)if lo<x<hi]
                    +[x+u for x in width_breaks(poly)if lo<x+u<hi]))
    total=F(0)
    for l,h in zip(cuts,cuts[1:]):
        t=(l+h)/2
        x1,y1=width_line(poly,t);x2,y2=width_line(poly,t-u)
        A,B=1-r*x1,-r*y1;C,D=1-s*(x2-y2*u),-s*y2
        total+=A*C*(h-l)+(A*D+B*C)*(h*h-l*l)/2+B*D*(h**3-l**3)/3
    assert total>=0
    return total

def load_terms():
    p=Path(__file__).with_name('width_kernels.json')
    d=json.loads(p.read_text())
    return [(tuple(tuple(p)for p in row['polygon']),F(row['coefficient']))for row in d['kernel_terms']]

def combined(a,r,s):
    return sum((c*kernel(p,a,r,s)for p,c in load_terms()),F(0))

if __name__=='__main__':
    print(zero_shift_identity())
    for r,s in [(F(1,3),F(1,4)),(F(2,3),F(1,2)),(F(1,5),F(2,5)),(F(1,10),F(1,9)),(F(4,5),F(7,8))]:
        v=combined(0,r,s);alt=F(7,8)*(1-r)*(1-s)
        print(r,s,v,alt,'ratio',v/alt,'symmetric', (v+combined(0,s,r))/2==alt)
