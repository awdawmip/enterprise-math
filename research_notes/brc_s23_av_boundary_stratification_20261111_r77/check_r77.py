#!/usr/bin/env python3
"""R77: exact rational critical-cell partition for original-labelled circular arcs.
All operations use fractions.Fraction; no numerical tolerance or randomness in decisions.
"""
from fractions import Fraction as Q
from random import Random
from collections import Counter
import json

def frac(y): return y-Q(y.numerator//y.denominator)

def inside(t,branch,theta,a,b,j,x):
    A,B=frac(a*theta),frac(b*theta)
    s=frac(x+(t-j)*theta)
    if A==B: return False  # Declared convention: coincident labels -> empty arc
    return (A<=s<B) if A<B else (s>=A or s<B)

def winner(events,theta,a,b,j,x):
    # Branch identity is a stable integer label with a declared total order.
    return max((t,br) for t,br in events if inside(t,br,theta,a,b,j,x)) if any(inside(t,br,theta,a,b,j,x) for t,br in events) else None

def crossing_points(v,c,L,U):
    if v==0:return []
    yl,yu=sorted([v*L+c,v*U+c])
    lo=yl.numerator//yl.denominator
    hi=yu.numerator//yu.denominator+1
    return [(Q(k)-c)/v for k in range(lo,hi+1) if L<=(Q(k)-c)/v<=U]

def partition(events,L,U,a,b,j,x):
    assert L<=U
    points={L,U}
    # Target label floor jumps, label order crossings; each source's phase
    # floor jumps and intersections with both original-labelled boundaries.
    tests=[(a,Q(0)),(b,Q(0)),(a-b,Q(0))]
    for t,_ in events:
        tests.extend(((t-j,x),(t-j-a,x),(t-j-b,x)))
    for v,c in set(tests):points.update(crossing_points(v,c,L,U))
    knots=sorted(points)
    cells=[]
    for i,z in enumerate(knots):
        cells.append({'kind':'point','low':z,'high':z,'witness':z,'latest':winner(events,z,a,b,j,x)})
        if i+1<len(knots):
            nz=knots[i+1]
            if nz>z:
                mid=(z+nz)/2
                cells.append({'kind':'open','low':z,'high':nz,'witness':mid,'latest':winner(events,mid,a,b,j,x)})
    return cells

def val(q):return f'{q.numerator}/{q.denominator}'

def stats(cells):
    return {'cells':len(cells),'critical_points':sum(c['kind']=='point' for c in cells),
            'distinct_latest':len(set(c['latest'] for c in cells)),
            'changes_between_adjacent_cells':sum(cells[i]['latest']!=cells[i-1]['latest'] for i in range(1,len(cells)))}

def self_test():
    rng=Random(771126)
    comparisons=0;cases=0;nontrivial=0;maxcells=0
    # Independently inspect every source's pointwise result on sampled rational
    # positions from each exact stratum; in addition test all critical points.
    for _ in range(160):
        n=rng.randrange(1,8)
        events={(rng.randrange(-30,31),rng.randrange(0,4)) for _ in range(n)}
        a,b=rng.sample(range(-6,7),2)
        j=rng.randrange(-3,4)
        x=Q(rng.randrange(-8,9),rng.choice([1,2,3,4,5,7]))
        L=Q(rng.randrange(-4,5),rng.choice([3,4,5,7]))
        U=L+Q(rng.randrange(0,5),rng.choice([5,9,15,25]))
        cells=partition(events,L,U,a,b,j,x)
        cases+=1;maxcells=max(maxcells,len(cells))
        if len(set(z['latest'] for z in cells))>1:nontrivial+=1
        for cell in cells:
            if cell['kind']=='point':test=[cell['witness']]
            else:
                l,u=cell['low'],cell['high']
                test=[(3*l+u)/4,(l+u)/2,(l+3*u)/4]
            for z in test:
                assert winner(events,z,a,b,j,x)==cell['latest'],(events,L,U,a,b,j,x,cell,z)
                comparisons+=1
    # Prove output oscillation via an explicit rational family: in every
    # complete period inside I=[1/4,1/3], (k+2/5)/t belongs to [theta,2theta)
    # whereas (k+9/10)/t is outside, for t>0.
    family=[]
    for t in (24,48,96,192,384):
        I0,I1=Q(1,4),Q(1,3)
        klist=[k for k in range(t) if Q(k,t)>=I0 and Q(k+1,t)<=I1]
        for k in klist:
            yes=Q(5*k+2,5*t)
            no=Q(10*k+9,10*t)
            assert I0<=yes<no<=I1
            assert inside(t,0,yes,1,2,0,Q(0))
            assert not inside(t,0,no,1,2,0,Q(0))
        cells=partition({(t,0)},I0,I1,1,2,0,Q(0))
        # Transitions grow linearly with source time; no floating-point scan.
        family.append({'time':t,'full_periods':len(klist),**stats(cells)})
    result={'seed':771126,'random_models':cases,'independent_rational_checks':comparisons,
            'random_models_with_latest_changes':nontrivial,'maximum_cells':maxcells,
            'oscillation_family':family,'assertions':'PASS'}
    print(json.dumps(result,ensure_ascii=False,indent=2));return result

if __name__=='__main__':self_test()
