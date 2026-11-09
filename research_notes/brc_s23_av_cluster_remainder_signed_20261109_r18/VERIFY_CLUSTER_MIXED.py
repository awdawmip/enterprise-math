#!/usr/bin/env python3
"""Exact rational certification of rational-cluster finite-risk identities.
All phase coordinates, comparisons and risks use Fraction; no float decisions.
Scientific observer is the auxiliary circle-cut Bayes risk, not native X6 dynamics.
"""
from fractions import Fraction as F
from math import gcd
from itertools import product

Q = F(1)

def direct_risk(theta, m, n):
    """Independent reference: explicitly subdivide each historical circle arc."""
    assert 0 < theta < 1 and 1 <= m <= n
    z = [(i * theta) % 1 for i in range(n)]
    assert len(set(z)) == n, ('phase collision', theta, m, n)
    hist = sorted(z[:m])
    total = F(0)
    for j, s in enumerate(hist):
        end = hist[(j + 1) % m]
        span = (end - s) % 1
        if m == 1:
            span = F(1)
        cuts = sorted([F(0), span] + [d for t in z[m:] if 0 < (d := ((t - s) % 1)) < span])
        total += max(b-a for a,b in zip(cuts,cuts[1:]))
    return Q-total

def cluster_risk(theta, p, q, m, n):
    """Proved cluster formula, positive and negative perturbations.
    Returns risk, correction, delta, and number of active corrections.
    """
    assert q>=1 and gcd(p,q)==1 and m>=q and n>=m and 0<theta<1
    eps = theta-F(p,q)
    assert eps != 0
    eta = abs(eps)
    assert n*eta < F(1,q), (eta,n,q)
    k = p if eps>0 else q-p
    assert 0<=k<q and gcd(k,q)==1
    inv = pow(k,-1,q) if q>1 else 0
    delta = q*eta
    corr = F(0); active=0
    for r in range(q):
        next_r=(r+inv)%q if q>1 else 0
        last_m=r+q*((m-1-r)//q)
        last_n=r+q*((n-1-r)//q)
        G=F(1,q)+(next_r-last_n)*eta
        assert G>0
        if last_n>last_m and G<delta:
            corr += delta-G
            active+=1
    return (n-m)*delta-corr,corr,delta,active

def check_family():
    cases=0; adjustments=0; nonmult=0; negative=0
    # Many independently selected rational near-rational parameters.
    for q in range(1,10):
      for p in range(0,q+1):
        if gcd(p,q)!=1: continue
        for sign in [-1,1]:
          if sign==1 and p==q:continue
          if sign==-1 and p==0:continue
          for m in [q,q+1,2*q-1,2*q+2]:
            for cap in [m+1,m+q+3]:
              # Four scales, including tight near the cluster separation boundary.
              for s in [F(1,8), F(1,3), F(4,5), F(99,100)]:
                eta=s/F(q*cap)
                theta=F(p,q)+sign*eta
                if not 0<theta<1:continue
                for n in range(m,cap+1):
                    if n*eta>=F(1,q):continue
                    got,corr,delta,active=cluster_risk(theta,p,q,m,n)
                    expected=direct_risk(theta,m,n)
                    assert got==expected,(p,q,m,n,theta,got,expected)
                    assert 0<=got<=1
                    cases+=1
                    adjustments+=int(corr>0)
                    nonmult+=int(m%q!=0)
                    negative+=int(sign==-1)
    return cases,adjustments,nonmult,negative

def s23_certificate():
    lo=F(262204504569236716045286,10**24)
    hi=F(262204504569236716045287,10**24)
    assert lo<hi<F(16,61)
    assert 180*(F(16,61)-lo)<F(1,61)
    assert 181*(F(16,61)-hi)>F(1,61)
    # Expected integer affine coefficients in theta, certified from both ends.
    values=[]
    for n in range(128,181):
        L=n-128
        vals=[]; corrs=[]; active=[]
        # Every linear boundary comparison has the same strict sign at both endpoints.
        pattern=[]
        for theta in [lo,hi]:
            val,corr,_,a=cluster_risk(theta,16,61,128,n)
            assert val==direct_risk(theta,128,n)
            vals.append(val);corrs.append(corr);active.append(a)
            eta=F(16,61)-theta
            flags=[]
            for r in range(61):
                sr=(r+pow(45,-1,61))%61
                last_m=r+61*((128-1-r)//61)
                last_n=r+61*((n-1-r)//61)
                G=F(1,61)+(sr-last_n)*eta
                assert G>0 and G!=61*eta
                flags.append(last_n>last_m and G<61*eta)
            assert sum(flags)==a
            pattern.append(tuple(flags))
        assert pattern[0]==pattern[1]
        B=(vals[1]-vals[0])/(hi-lo)
        A=vals[0]-B*lo
        assert A.denominator==1 and B.denominator==1,(n,A,B)
        if L<=36:
            assert (A,B)==(16*L,-61*L)
        if L==37:
            assert (A,B)==(533,-2032)
        values.append((n,int(A),int(B),active[0]))
    # Show nontrivial exact frontier, selected breakpoints, and change points.
    changes=[]
    prev=None
    for row in values:
        n,A,B,a=row
        if prev is not None:
            d=(A-prev[1],B-prev[2])
            if d!=last_delta:
                changes.append((n,d))
            last_delta=d
        else:last_delta=(0,0)
        prev=row
    return values,changes

if __name__=='__main__':
    cases,adj,nonmult,negative=check_family()
    vals,changes=s23_certificate()
    print('PASS_CLUSTER_MIXED_SIGN_GENERAL_RATIONAL_EXACT')
    print('direct_fraction_comparisons',cases)
    print('positive_correction_cases',adj,'nonmultiple_history_cases',nonmult,'negative_perturbation_cases',negative)
    print('S23_theta_interval','262204504569236716045286/10^24','262204504569236716045287/10^24')
    print('S23_cluster_reference','p/q=16/61, theta=16/61-eta, m=128, exact_for_128<=n<=180')
    print('S23_n_180',vals[-1])
    print('S23_change_events',changes)
