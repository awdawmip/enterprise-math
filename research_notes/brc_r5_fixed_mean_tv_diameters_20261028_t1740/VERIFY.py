#!/usr/bin/env python3
"""Exact rational checks for fixed-mean two-law TV diameters."""
from fractions import Fraction as F
from itertools import combinations

def tv(a, b):
    return sum((abs(x-y) for x,y in zip(a,b)), F(0))/2

def mean(s,q):
    return sum((x*y for x,y in zip(s,q)), F(0))

def two_point(s,r,i,j):
    assert i<j and s[i]<=r<=s[j]
    q=[F(0)]*len(s)
    q[i]=(s[j]-r)/(s[j]-s[i])
    q[j]=(r-s[i])/(s[j]-s[i])
    assert sum(q)==1 and mean(s,q)==r
    return tuple(q)

def caps(s,r):
    assert len(s)>=3 and s[0]<r<s[-1]
    return (min(F(1),(r-s[0])/(s[1]-s[0]),(s[-1]-r)/(s[-1]-s[-2])),
            min(F(1),s[1]*(r-s[0])/(r*(s[1]-s[0])),
                s[-2]*(s[-1]-r)/(r*(s[-1]-s[-2]))))

def endpoints(s,r):
    n=len(s)
    if r<s[1]:
        return two_point(s,r,0,1),two_point(s,r,0,n-1)
    if r>s[-2]:
        return two_point(s,r,n-2,n-1),two_point(s,r,0,n-1)
    if n==3:
        return two_point(s,r,0,2), (F(0),F(1),F(0))
    return two_point(s,r,0,n-2),two_point(s,r,1,n-1)

def baseline(s,r):
    n=len(s); eta=F(1,10000)
    q=[F(0)]*n
    for i in range(1,n-1): q[i]=eta
    rest=1-(n-2)*eta
    mrest=r-eta*sum(s[1:-1])
    q[0]=(s[-1]*rest-mrest)/(s[-1]-s[0])
    q[-1]=(mrest-s[0]*rest)/(s[-1]-s[0])
    assert min(q)>0 and sum(q)==1 and mean(s,q)==r
    return tuple(q)

def check(s,r,qa,qb):
    assert all(z>=0 for z in qa+qb)
    assert sum(qa)==sum(qb)==1
    assert mean(s,qa)==mean(s,qb)==r
    pa=tuple(s[i]*qa[i]/r for i in range(len(s)))
    pb=tuple(s[i]*qb[i]/r for i in range(len(s)))
    assert sum(pa)==sum(pb)==1
    dq,dp=tv(qa,qb),tv(pa,pb)
    mq,mp=caps(s,r)
    assert 0<=dq<=mq and 0<=dp<=mp
    if dq: assert (s[1]/r)*dq<=dp<=(s[-2]/r)*dq
    return dq,dp

def witness(s,r,name):
    qa,qb=endpoints(s,r)
    mq,mp=caps(s,r)
    assert check(s,r,qa,qb)==(mq,mp)
    q0=baseline(s,r); eps=F(1,100)
    a=tuple((1-eps)*x+eps*y for x,y in zip(qa,q0))
    b=tuple((1-eps)*x+eps*y for x,y in zip(qb,q0))
    assert all(z>0 for z in a+b)
    d=check(s,r,a,b)
    assert d==((1-eps)*mq,(1-eps)*mp)
    print(f'{name}: r={r}; Q_diameter_sup={mq}; P_diameter_sup={mp}; boundary_witness=({mq},{mp}); positive_1pct_witness=({d[0]},{d[1]})')

def positive_grid(n,den):
    for cuts in combinations(range(1,den),n-1):
        bounds=(0,)+cuts+(den,)
        yield tuple(F(bounds[i+1]-bounds[i],den) for i in range(n))

def grid(s,den):
    groups={}
    for q in positive_grid(len(s),den):
        groups.setdefault(mean(s,q),[]).append(q)
    count=0
    for r,kernels in groups.items():
        for a,b in combinations(kernels,2):
            check(s,r,a,b)
            count+=1
    print(f'grid n={len(s)} denominator={den} mean_groups={len(groups)} checked_pairs={count}')
    return count

def main():
    s=(F(1,2),F(1),F(2),F(3))
    for name,r in [('left',F(3,4)),('center',F(3,2)),('right',F(5,2))]:
        witness(s,r,name)
    witness((F(1,2),F(1),F(3)),F(1),'three-signature-midpoint')
    count=0
    for ss,den in [((F(1,2),F(1),F(3)),19),
                   ((F(1,2),F(1),F(2),F(3)),14),
                   ((F(1,3),F(2,3),F(1),F(2),F(4)),11),
                   ((F(1,4),F(1,2),F(1),F(3,2),F(5,2),F(4)),12)]:
        count+=grid(ss,den)
    assert count==3278
    print(f'EXACT_GRID_PAIRS={count}')
    print('ALL EXACT FIXED-MEAN DUAL-LAW TV DIAMETER CHECKS PASSED')

if __name__=='__main__':
    main()
