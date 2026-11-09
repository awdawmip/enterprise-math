#!/usr/bin/env python3
"""Exact rational finite checks for constant-size four-cell cluster formula.
Frozen S23/AV source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
The source condition is m>=q, eta>0, theta_+=k/q+eta (or reflected),
and all circular cluster boundary gaps G_r(n)>0.
"""
from fractions import Fraction as Q
from math import gcd
from bisect import bisect_left


def overlap(*ranges):
    return max(0, min(r[1] for r in ranges)-max(r[0] for r in ranges))


def residue_intervals(q,m,n):
    L=n-m
    if L>=q:
        return [(0,q)]
    c=m%q
    if c+L<=q:
        return [(c,c+L)]
    return [(c,q),(0,c+L-q)]


def compact_risk(p,q,theta,m,n,strict=True):
    assert 0<theta<1 and 1<=q<=m<=n and gcd(p,q)==1
    epsilon=theta-Q(p,q)
    assert epsilon!=0
    if epsilon>0:
        k=p
    else:
        k=q-p
    eta=abs(epsilon)
    assert 0<=k<q and gcd(k,q)==1
    s=pow(k,-1,q) if q>1 else 0
    a,b=divmod(n,q)
    t=q-s
    E=residue_intervals(q,m,n)
    correction=Q(0)
    min_gap=None
    bins=[]
    for x in (0,1):
        X=(0,b) if x else (b,q)
        for y in (0,1):
            Y=(t,q) if y else (0,t)
            length=overlap(X,Y)
            if not length:
                continue
            # G_r constant on this bin, no loop over any residue.
            G=Q(1,q)-((a-1)*q-s+q*(x+y))*eta
            min_gap=G if min_gap is None else min(G,min_gap)
            count=sum(overlap(I,X,Y) for I in E)
            correction+=count*max(Q(0),q*eta-G)
            bins.append((x,y,length,count,G))
    if strict:
        assert min_gap>0, f'outside cluster-positive regime min_gap={min_gap}'
    return (n-m)*q*eta-correction,min_gap,bins


def original_q_loop(p,q,theta,m,n):
    eta=abs(theta-Q(p,q))
    k=p if theta>Q(p,q) else q-p
    s=pow(k,-1,q) if q>1 else 0
    risk=(n-m)*q*eta
    minimum=None
    for r in range(q):
        rp=(r+s)%q
        ell=r+q*((n-1-r)//q)
        oldell=r+q*((m-1-r)//q)
        g=Q(1,q)+(rp-ell)*eta
        minimum=g if minimum is None else min(minimum,g)
        if ell>oldell:
            risk-=max(Q(0),q*eta-g)
    return risk,minimum


def direct_phase_risk(theta,m,n):
    cuts=sorted(((i*theta)%1,i) for i in range(n))
    cur=next(i for _,i in reversed(cuts) if i<m)
    largest={i:Q(0) for i in range(m)}
    for j,(x,i) in enumerate(cuts):
        if i<m: cur=i
        next_x=cuts[(j+1)%n][0]+(j==n-1)
        g=next_x-x
        if g>largest[cur]:largest[cur]=g
    return 1-sum(largest.values(),Q(0))


def find_first_bad(p,q,theta,m):
    assert compact_risk(p,q,theta,m,m)[1]>0
    lo=m; hi=max(m+1,2*m)
    while compact_risk(p,q,theta,m,hi,strict=False)[1]>0:
        lo=hi;hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if compact_risk(p,q,theta,m,mid,strict=False)[1]>0:lo=mid
        else:hi=mid
    return lo,hi


def run():
    tested=0;direct=0;corrected=0;special=0
    # Dense finite cross-check, rational theta values, both perturbation signs,
    # all q<=15, mixed histories and horizons, including beyond n*eta<1/q.
    for q in range(1,16):
        for p in range(q+1):
            if gcd(p,q)!=1:continue
            for sign in (-1,1):
                if sign==1 and p==q:continue
                if sign==-1 and p==0:continue
                for denom in (250,600):
                    eta=Q(1,denom*q*q)
                    theta=Q(p,q)+sign*eta
                    if not (0<theta<1):continue
                    for m in range(q,max(q+1,3*q+1),max(1,q//3)):
                        for n in range(m,min(m+3*q+4,86)):
                            fast,G,_=compact_risk(p,q,theta,m,n,strict=False)
                            if G<=0:continue
                            ref,G2=original_q_loop(p,q,theta,m,n)
                            assert G==G2 and fast==ref,(p,q,m,n,fast,ref)
                            tested+=1
                            if fast!=(n-m)*q*eta:corrected+=1
                            if n*eta>=Q(1,q): special+=1
                            if (n-m<=q+2) or (n%q==0):
                                truth=direct_phase_risk(theta,m,n)
                                assert fast==truth,(p,q,m,n,fast,truth)
                                direct+=1
    # Boundary-focused cases with eta on the scale 1/(c*q^2):
    # certify nonzero correction and cluster order beyond the simple sufficient bound.
    for q in range(2,15):
        for p in range(1,q):
            if gcd(p,q)!=1:continue
            for sign in (-1,1):
                for c in (2,3,5,9):
                    eta=Q(1,c*q*q)
                    theta=Q(p,q)+sign*eta
                    if not(0<theta<1):continue
                    for m in (q,q+1,2*q+1):
                        for n in range(m,min(m+2*q+1,6*q+1)):
                            fast,G,_=compact_risk(p,q,theta,m,n,strict=False)
                            if G<=0:continue
                            ref,G2=original_q_loop(p,q,theta,m,n)
                            assert fast==ref and G==G2,(p,q,m,n,fast,ref)
                            tested+=1
                            if fast!=(n-m)*q*eta:corrected+=1
                            if n*eta>=Q(1,q):special+=1
                            if (n-m<=2) or (corrected>0 and corrected%173==0 and n%3==0):
                                truth=direct_phase_risk(theta,m,n)
                                assert fast==truth,(p,q,m,n,fast,truth)
                                direct+=1
    # Frozen S23 interval is prior certified (via a 160-term rational log bound)
    lo=Q(262204504569236716045286,10**24)
    hi=Q(262204504569236716045287,10**24)
    assert hi<Q(16,61)
    for th in (lo,hi):
        for n in range(128,226):
            fast,G,_=compact_risk(16,61,th,128,n)
            truth=direct_phase_risk(th,128,n)
            assert fast==truth,(n,fast,truth)
            expected=(n-128)*(16-61*th) if n<=164 else 36*(16-61*th)+(n-164)*(164*th-43)
            assert fast==expected,(n,fast,expected)
        a,b=find_first_bad(16,61,th,128)
        assert (a,b)==(225,226),(a,b)
        assert compact_risk(16,61,th,128,225)[0]==-2047+7808*th
        print(f'S23_ENDPOINT={"lower" if th==lo else "upper"}: valid_to_n={a}, first_bad_n={b}, n225_R=-2047+7808*theta')
    # Large-q O(1) regression. Compare q=10_007 against full loop;
    # for 1,000,003 and 1,000,000,007 evaluate without q-step enumeration.
    for q in (10007,1000003,1000000007):
        p=1;m=2*q+17;n=m+q+23
        eta=Q(1,1000*q*q*q)
        theta=Q(p,q)+eta
        val,G,bins=compact_risk(p,q,theta,m,n)
        assert G>0 and len(bins)<=4
        if q==10007:
            ref,_=original_q_loop(p,q,theta,m,n)
            assert val==ref
        print(f'LARGE_Q={q}: M={m}, N={n}, bins={len(bins)}, delta_positive={val>0}, exact_risk_numerator_digits={len(str(val.numerator))}, denominator_digits={len(str(val.denominator))}')
    print(f'FINITE_CHECK: fast_vs_q_loop={tested}, fast_vs_independent_circle={direct}, positive_correction_cases={corrected}, beyond_simple_inequality={special}')
    print('PASS_O1_CLUSTER_RISK_AND_LOG_BOUNDARY_SEARCH')

if __name__=='__main__':run()
