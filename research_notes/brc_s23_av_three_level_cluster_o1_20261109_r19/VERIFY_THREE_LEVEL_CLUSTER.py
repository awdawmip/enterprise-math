#!/usr/bin/env python3
"""Exact Fraction checks for constant-size residue-class correction formula.
No scientific GitHub I/O, user credentials, floating-point comparison, or native-X6 inference.
"""
from fractions import Fraction as F
from math import gcd
import random
from bisect import bisect_right, bisect_left


def prefix_E(x, q, m, n):
    w = n - m
    if w == 0:
        return 0
    if w >= q:
        return x
    d = m % q
    z = d + w
    if z <= q:
        return max(0, min(x, z) - d)
    return min(x, z - q) + max(0, x - d)


def fast_risk(theta, p, q, m, n):
    """Return (risk, three class counts, minimum gap, eta) if cluster chain ordered."""
    assert 0 <= theta <= 1 and n >= m >= q >= 1 and gcd(p, q) == 1
    eps = theta - F(p,q)
    assert eps != 0
    eta = abs(eps)
    k = p if eps > 0 else q-p
    assert 0 <= k < q and gcd(k,q) == 1
    h = pow(k,-1,q) if q>1 else 0
    a,b=divmod(n,q)
    th = q-h
    d=F(1,q)
    delta=q*eta
    def gap(j):
        return d+(h-q*(a-1)-q*j)*eta
    # T = I(r>=q-h)+I(r<b). Its maximum can be checked without a residue scan.
    tmax = 2 if b>th else (1 if h>0 or b>0 else 0)
    mingap=gap(tmax)
    if mingap <= 0:
        return None
    sz = min(n-m,q)
    a_count = prefix_E(q,q,m,n)-prefix_E(th,q,m,n) if h else 0
    b_count = prefix_E(b,q,m,n)
    ab_count = (prefix_E(b,q,m,n)-prefix_E(th,q,m,n)) if b>th else 0
    counts=(sz-a_count-b_count+ab_count,
            a_count+b_count-2*ab_count,
            ab_count)
    assert all(z>=0 for z in counts) and sum(counts)==sz
    correction=sum(counts[j]*max(F(0),delta-gap(j)) for j in range(3))
    return ((n-m)*delta-correction,counts,mingap,eta)


def slow_cluster(theta, p, q, m, n):
    eps=theta-F(p,q); eta=abs(eps)
    k=p if eps>0 else q-p
    h=pow(k,-1,q) if q>1 else 0
    delta=q*eta
    correct=F(0)
    gaps=[]
    for r in range(q):
        last = r+q*((n-1-r)//q)
        old = r+q*((m-1-r)//q)
        next_r=(r+h)%q
        g=F(1,q)+(next_r-last)*eta
        gaps.append(g)
        if last>old:
            correct+=max(F(0),delta-g)
    if min(gaps)<=0: return None
    return (n-m)*delta-correct


def direct(theta,m,n):
    c=sorted((i*theta)%1 for i in range(n))
    h=sorted((i*theta)%1 for i in range(m))
    cc=c+[x+1 for x in c]
    ans=F(1)
    for t,a in enumerate(h):
        b=h[(t+1)%m] if t<m-1 else h[0]+1
        j=bisect_right(cc,a)
        k=bisect_left(cc,b)
        prev=a
        maxgap=F(0)
        for x in cc[j:k]:
            maxgap=max(maxgap,x-prev)
            prev=x
        maxgap=max(maxgap,b-prev)
        ans-=maxgap
    return ans


def linear_coeff_2_ends(xlo,ylo,xhi,yhi):
    B=(yhi-ylo)/(xhi-xlo)
    A=ylo-B*xlo
    assert B.denominator==1 and A.denominator==1
    return (int(A),int(B))


def main():
    rng=random.Random(202611091931)
    checked=0; triples=0; crossings=0; extended=0; direct_count=0
    for q in range(1,20):
        pp=[0] if q==1 else [p for p in range(1,q) if gcd(p,q)==1]
        if q==1: pp_neg=[1]
        else: pp_neg=pp
        for sgn in (-1,1):
            for rep in range(8):
                p = rng.choice(pp if sgn>0 else pp_neg)
                m=rng.randrange(q,3*q+1)
                n=rng.randrange(m,min(6*q,90)+1) if m<=min(6*q,90) else m
                den=q*(n+10)*rng.choice((2,5,7,11))
                eta=F(1,den)
                theta=F(p,q)+sgn*eta
                z=fast_risk(theta,p,q,m,n)
                assert z is not None
                assert z[0]==slow_cluster(theta,p,q,m,n)
                if n<=90:
                    assert z[0]==direct(theta,m,n), (q,p,sgn,m,n,z)
                    direct_count+=1
                checked+=1
                triples+= int(z[1][2]>0)
                extended+=int(n*eta>=F(1,q))
    # A broad set of positive-gap values where n*eta>=1/q but cluster order survives.
    for q in range(2,23):
        for p in range(1,q):
            if gcd(p,q)>1: continue
            for sgn in (-1,1):
                for n in range(q+2,4*q+1):
                    m=min(n,2*q+1)
                    eta=F(1,q*(n-2))
                    theta=F(p,q)+sgn*eta
                    if not(0<theta<1):continue
                    z=fast_risk(theta,p,q,m,n)
                    if z is None:continue
                    assert z[0]==slow_cluster(theta,p,q,m,n)
                    if n<=90:
                        assert z[0]==direct(theta,m,n)
                        direct_count+=1
                    crossings+=1
                    extended+=int(n*eta>=F(1,q))
    print(f'PASS_FRACTION_CASES={checked}, EXTRA_ORDERED_CASES={crossings}, DIRECT_PHASE_COMPARISONS={direct_count}')
    print(f'CLASS_TWO_NONZERO_CASES={triples}, GAINED_BEYOND_OLD_SUFFICIENT_BOUND={extended}')
    # Frozen S23: strict enclosure, two rational endpoints certify the algebraic branch.
    lo=F(262204504569236716045286,10**24)
    hi=F(262204504569236716045287,10**24)
    assert lo<hi<F(16,61)
    pinned_n=0
    s23_results={}
    for n in range(128,227):
        zz=[fast_risk(t,F(16,61).numerator,61,128,n) for t in (lo,hi)]
        if n<=225:
            assert all(v is not None for v in zz),n
            B=linear_coeff_2_ends(lo,zz[0][0],hi,zz[1][0])
            if n<=164:
                expect=(16*(n-128),-61*(n-128))
            else:
                # 36(16-61theta)+(n-164)(164theta-43)
                expect=(36*16-43*(n-164),-36*61+164*(n-164))
            assert B==expect, (n,B,expect)
            pinned_n+=1
            if n in (128,164,165,180,225): s23_results[n]=B
        else:
            assert all(v is None for v in zz)
    print('S23_EXACT_ENDPOINT_BRANCHES=',s23_results)
    print('S23_FULL_POSITIVE_GAP_INTERVAL=128..225, CHECKS=',pinned_n)
    print('S23_FIRST_INVALID_N=226')
    # Large q exact operation independent of q: no loop over q appears in fast_risk.
    q=1_000_000_007; p=2; m=2*q+20; n=2*q+500
    eta=F(1, q*(n+500))
    z=fast_risk(F(p,q)+eta,p,q,m,n)
    assert z is not None and z[0]>=0
    print('LARGE_Q_EXACT_INPUT_OUTPUT=',q,m,n,str(z[0]),'counts=',z[1])
    print('PASS_THREE_LEVEL_CLUSTER_O1_CORRECTION')

if __name__ == '__main__':main()
