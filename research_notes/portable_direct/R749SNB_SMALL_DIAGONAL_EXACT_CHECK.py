#!/usr/bin/env python3
"""R749SNB: exact 6D polytope certificate for 0 <= t=s=r <= 1/5.

No floating point, external solver, or randomized sampling.
Coordinates: (r,h,u,v,w,z). Every constraint is b + row*x >= 0.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import json

SIGNS = list(product((1,-1), repeat=4))  # A,D,P,Q
def chi(mask, x):return (-1)**((mask & x).bit_count()%2)
X_BY_SIGN = [next(x for x in range(16) if (chi(3,x),chi(12,x),chi(1,x),chi(4,x))==(a,d,p,q)) for a,d,p,q in SIGNS]
ROWS = [(a+d,a*d,p,a*p,q,d*q) for a,d,p,q in SIGNS]
FACETS = [(tuple(map(F,row)), F(1)) for row in ROWS]
FACETS += [((F(1), F(0),F(0),F(0),F(0),F(0)), F(0)),
           ((F(-1),F(0),F(0),F(0),F(0),F(0)), F(1,5))]


def solve_exact(idxs):
    """Solve six selected independent active facets, or return None."""
    a=[[ *FACETS[i][0], -FACETS[i][1]] for i in idxs]
    n=6
    for k in range(n):
        j=next((j for j in range(k,n) if a[j][k]),None)
        if j is None:return None
        if j!=k:a[j],a[k]=a[k],a[j]
        pivot=a[k][k]
        a[k]=[v/pivot for v in a[k]]
        for j in range(k+1,n):
            mul=a[j][k]
            if mul:
                for l in range(k+1,n+1):a[j][l]-=mul*a[k][l]
                a[j][k]=F(0)
    ans=[F(0)]*n
    for k in reversed(range(n)):
        ans[k]=a[k][-1]-sum(a[k][l]*ans[l] for l in range(k+1,n))
    return tuple(ans)


def feasible(x):
    return all(b+sum(v*w for v,w in zip(a,x))>=0 for a,b in FACETS)


def laws(x):
    r,h,u,v,w,z=x
    mu=tuple((1+r*(a+d)+h*a*d+u*p+v*a*p+w*q+z*d*q)/16
             for a,d,p,q in SIGNS)
    q=tuple((1+r*(a+d+a*d))/16 for a,d,p,q in SIGNS)
    return mu,q


def risk_and_checks(x):
    r=x[0];mu,q=laws(x)
    assert sum(mu)==sum(q)==1 and all(v>=0 for v in mu+q)
    assert sum(mu[i]*SIGNS[i][0] for i in range(16))==r
    assert sum(mu[i]*SIGNS[i][1] for i in range(16))==r
    assert sum(q[i]*SIGNS[i][0] for i in range(16))==r
    assert sum(q[i]*SIGNS[i][1] for i in range(16))==r
    risk=sum(abs(a-b) for a,b in zip(mu,q))/2
    gap=(1-r)/2-risk
    assert gap>=0,(x,risk,gap)
    return risk,gap


def main():
    vert=set();nonzero=0;feasible_bases=0
    for idx in combinations(range(18),6):
        x=solve_exact(idx)
        if x is None:continue
        nonzero+=1
        if feasible(x):
            feasible_bases+=1;vert.add(x)
    assert vert
    count=Counter(v[0] for v in vert)
    assert set(count)=={F(0), F(1,5)}, ('unexpected interior vertex',count)
    risk_summary={}; tight=Counter()
    for x in sorted(vert):
        risk,gap=risk_and_checks(x)
        r=x[0]
        risk_summary.setdefault(r,[]).append(risk)
        if gap==0:tight[r]+=1
    assert len(vert)==79 and count[F(0)]==26 and count[F(1,5)]==53
    assert max(risk_summary[F(0)])==F(1,2)
    assert max(risk_summary[F(1,5)])==F(2,5)
    assert tight[F(0)]>0 and tight[F(1,5)]>0
    # Each full fiber is nonempty and q_r is an admissible calibrated decoder.
    # The explicit analytic pair mu_+/- has TV(mu_+,mu_-)=1-r for all 0<=r<=1/5.
    for r in (F(0),F(1,20),F(1,10),F(3,20),F(1,5)):
        m=[]
        for sgn in (-1,1):
            m.append(tuple(((1+r*a)*(1+r*d)+sgn*(1-r)*(1+r*a)*p)/16
                           for a,d,p,q in SIGNS))
        assert all(sum(v)==1 and min(v)>=0 for v in m)
        for v in m:
            assert sum(v[i]*SIGNS[i][0] for i in range(16))==r
            assert sum(v[i]*SIGNS[i][1] for i in range(16))==r
            # Retained B excludes masks 1, 2, 4, 8, 15.
            for k in (3,5,6,7,9,10,11,12,13,14):
                mk=sum(v[i]*chi(k, X_BY_SIGN[i]) for i in range(16))
                assert mk==(r if k in (3,12) else 0)
        assert sum(abs(a-b) for a,b in zip(*m))/2==1-r
    out={
       'schema':'R749SNB_SMALL_DIAGONAL_EXACT_POLYTOPE_CERTIFICATE_V1',
       'status':'PASS',
       'frozen_science_commit':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
       'domain':'G=F2^4, real 0<=r<=1/5, m_3=m_12=r, eight other B moments zero',
       'variables':['r','h','u','v','w','z'],
       'facets':len(FACETS),
       'six_facet_subsets':18564,
       'nonsingular_bases':nonzero,
       'feasible_bases':feasible_bases,
       'distinct_vertices':len(vert),
       'vertex_r_values':{'0':count[F(0)],'1/5':count[F(1,5)]},
       'exact_maximum_TV_at_r_endpoints':{'0':str(max(risk_summary[F(0)])),'1/5':str(max(risk_summary[F(1,5)]))},
       'tight_vertex_counts':{'0':tight[F(0)],'1/5':tight[F(1,5)]},
       'theorem':'rho_B(epsilon*r,eta*r)=rho_cal_B(epsilon*r,eta*r)=(1-r)/2 for 0<=r<=1/5 and both signs',
       'upper_decoder':'q_r(A,D,P,Q)=(1+r(A+D+AD))/16, sign-translated for other quadrants',
       'lower_pair_TV':'1-r',
       'arithmetic':'Python standard-library fractions.Fraction, exhaustive rank-six active facet bases',
       'not_claimed':'native V29/V39 mapping; independent scientific review; Foundation promotion'
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
