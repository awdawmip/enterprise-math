#!/usr/bin/env python3
"""R71 compact exact certificate checker; auxiliary rational circle model only."""
from fractions import Fraction as F
from collections import defaultdict

def floor(x): return x.numerator // x.denominator
def ceil(x): return -((-x.numerator) // x.denominator)
def frac(x): return x-floor(x)
def arc_ok(a,b,L,U):
    return (floor(a*L)==floor(a*U) and floor(b*L)==floor(b*U)
            and all(frac(a*z)<frac(b*z) for z in (L,U)))
def member(t,a,b,th,j=0,x=F(0)):
    return frac(a*th)<=frac(x+(t-j)*th)<frac(b*th)
def index(times,anchor):
    g=defaultdict(list)
    for t in times:g[frac(t*anchor)].append(t)
    return tuple((r,min(ts),max(ts)) for r,ts in g.items())
def exclude(groups,a,b,L,U,anchor,j=0,x=F(0)):
    if not groups or not L<=anchor<=U or not arc_ok(a,b,L,U):return False
    dl,du=L-anchor,U-anchor
    ka,kb=floor(a*L),floor(b*L)
    qlo=min(a*L-ka,a*U-ka);qhi=max(b*L-kb,b*U-kb)
    for r,tlo,thi in groups:
        phase=frac(r+x-j*anchor)
        slopes=(tlo-j,thi-j)
        corners=[d*z for d in slopes for z in (dl,du)]
        slo=phase+min(corners);shi=phase+max(corners)
        if ceil(slo-qhi)<=floor(shi-qlo):return False
    return True

def run():
    anchor=F(1,4); L=F(249,1000);U=F(251,1000)
    assert exclude(index((3,4,4),anchor),1,2,L,U,anchor)
    for th in (L,F(499,2000),anchor,F(501,2000),U):
        assert all(not member(t,1,2,th) for t in (3,4))
    assert member(6,1,2,L) and not member(6,1,2,anchor)
    # Four extrema cannot decide all-source exclusion.
    z=F(1,10);l=F(99,1000);u=F(101,1000)
    def extreme(T): return (min(T),max(T),min(frac(t*z) for t in T),max(frac(t*z) for t in T))
    assert extreme((1,9))==extreme((1,5,9))
    assert all(not member(t,4,6,th) for t in (1,9) for th in (l,z,u))
    assert all(member(5,4,6,th) for th in (l,z,u))
    # Infinite explicit family: 2N distinct source times, 2 phase classes.
    for N in (1,2,4,8,16,64,256,1024):
        T=tuple(4*k for k in range(1,N+1))+tuple(4*k-1 for k in range(1,N+1))
        h=F(1,100*N);l=anchor-h;u=anchor+h
        G=index(T,anchor)
        assert len(G)==2 and exclude(G,1,2,l,u,anchor)
        for th in (l,anchor,u):assert all(not member(t,1,2,th) for t in T)
    # Moving observation: absolute groups are reused with typed j,x.
    T=(1,3,4,4,8,11,12,19)
    G=index(T,anchor)
    for j,x in ((0,F(0)),(7,F(1,7)),(-4,F(2,5))):
        for a,b in ((1,2),(2,3),(1,3)):
            if exclude(G,a,b,L,U,anchor,j,x):
                for k in range(101):
                    th=L+(U-L)*F(k,100)
                    assert all(not member(t,a,b,th,j,x) for t in T)
    print('R71_MIN_PASS 8_family_sizes 3_observers 3_arcs')

if __name__=='__main__':run()
