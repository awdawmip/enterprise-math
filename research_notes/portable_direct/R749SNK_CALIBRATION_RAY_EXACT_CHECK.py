#!/usr/bin/env python3
"""R749SNK: exact all-real certificate for s=3/10, t in [1/2,1]."""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
import json

S=F(3,10)
R=[tuple(1 if ((m&x).bit_count()%2)==0 else -1 for m in (3,12,15,1,2,4,8)) for x in range(16)]
E_LEFT=(3,5,7,9,11,13,14,15)
E_RIGHT=(3,5,6,7,11,13,14,15)

def law(t,h,u,v,w,z):
    return tuple((1+t*a+S*d+h*ad+u*p+v*ap+w*q+z*dq)/16 for a,d,ad,p,ap,q,dq in R)

def decoder(t,eta):
    return tuple((1+t*a+S*d+eta*ad)/16 for a,d,ad,*_ in R)

def tv(mu,q):
    return sum((abs(a-b) for a,b in zip(mu,q)),F(0))/2

def solve6(indices,M,b):
    n=6
    a=[list(M[i])+[b[i]] for i in indices]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            q=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*p-q*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=p
    if a[-1][-2]==0:return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][-1])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def exact_segment(lo,hi,eta,radius):
    L=lcm(10,lo.denominator,hi.denominator)
    M=[(a,ad,p,ap,q,dq) for a,d,ad,p,ap,q,dq in R]
    b=[-L-int(L*S)*d for a,d,ad,p,ap,q,dq in R]
    M.extend([(1,0,0,0,0,0),(-1,0,0,0,0,0)])
    b.extend([int(L*lo),-int(L*hi)])
    counts={'facet_subsets':0,'nonsingular':0,'feasible_bases':0}
    seen=set()
    for inds in combinations(range(18),6):
        counts['facet_subsets']+=1
        v=solve6(inds,M,b)
        if v is None:continue
        counts['nonsingular']+=1
        if any(sum((x*y for x,y in zip(row,v)),F(0))<lim for row,lim in zip(M,b)):
            continue
        counts['feasible_bases']+=1
        seen.add(tuple(x/L for x in v))
    assert seen
    counts['distinct_vertices']=len(seen)
    counts['tight_vertices']=0
    for par in seen:
        t=par[0]
        assert lo<=t<=hi
        mu=law(*par)
        q=decoder(t,eta(t))
        assert all(x>=0 for x in mu+q)
        assert sum(mu)==sum(q)==1
        dist=tv(mu,q)
        assert dist<=radius(t),('UPPER_BOUND_FAILED',par,dist,radius(t))
        counts['tight_vertices']+=int(dist==radius(t))
    return counts

def main():
    left_radius=lambda t:F(27,80)+t/8
    right_radius=lambda t:F(3,5)-t/4
    left=exact_segment(F(1,2),F(7,10),lambda t:F(0),left_radius)
    right=exact_segment(F(7,10),F(1),lambda t:t-F(7,10),right_radius)
    for event in (E_LEFT,E_RIGHT):
        assert len(event)==8
        assert all(sum(R[x][i] for x in event)==0 for i in (0,1,2))
    witness_left=lambda t:law(t,F(0),-F(7,10),-t,-F(3,10),-F(3,10))
    witness_right=lambda t:law(t,t-F(7,10),-F(7,10),-F(7,10),t-1,t-1)
    for t in (F(1,2),F(7,10)):
        mu=witness_left(t)
        assert sum(mu)==1 and all(z>=0 for z in mu)
        assert sum((mu[i] for i in E_LEFT),F(0))-F(1,2)==left_radius(t)
    for t in (F(7,10),F(1)):
        mu=witness_right(t)
        assert sum(mu)==1 and all(z>=0 for z in mu)
        assert sum((mu[i] for i in E_RIGHT),F(0))-F(1,2)==right_radius(t)
    assert left_radius(F(7,10))==right_radius(F(7,10))==F(17,40)
    return {'unit':'R749SNK','status':'PASS',
            'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
            'scope':'t in [1/2,1], s=3/10; auxiliary G=F_2^4 Walsh fiber; all real t',
            'formulae':{'free_equals_calibrated_left':'27/80+t/8 on [1/2,7/10]',
                        'free_equals_calibrated_right':'3/5-t/4 on [7/10,1]'},
            'transition':'t=7/10 with value 17/40',
            'segment_certificates':{'left':left,'right':right},
            'witness_checks':'feasible affine families and balanced-event dual lower bounds at endpoints',
            'method':'integer Bareiss 6-variable enumeration over every joint-polytope vertex; Fraction total variation'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
