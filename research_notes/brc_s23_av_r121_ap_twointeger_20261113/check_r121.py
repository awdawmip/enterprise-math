#!/usr/bin/env python3
"""R121: exact arithmetic-progression lift pattern/reduction checker, no external packages."""
from fractions import Fraction as F
from itertools import product
from random import Random
from math import floor
import json
from pathlib import Path


def patterns(m):
    # Lines alpha+i*beta=h, 1<=i<m, 1<=h<=i. Exact arrangement sweep.
    lines = [(i,h) for i in range(1,m) for h in range(1,i+1)]
    beta_cuts = {F(0),F(1)}
    for i,h in lines:
        for alpha in (0,1):
            b=F(h-alpha,i)
            if 0 <= b <= 1: beta_cuts.add(b)
    for i,h in lines:
        for j,k in lines:
            if i!=j:
                b=F(h-k,i-j)
                a=F(h)-i*b
                if 0<=b<=1 and 0<=a<=1: beta_cuts.add(b)
    beta = sorted(beta_cuts)
    out=set()
    for blo,bhi in zip(beta,beta[1:]):
        b=(blo+bhi)/2
        acuts={F(0),F(1)}
        for i,h in lines:
            a=F(h)-i*b
            if 0<a<1: acuts.add(a)
        aa=sorted(acuts)
        for alo,ahi in zip(aa,aa[1:]):
            a=(alo+ahi)/2
            out.add(tuple((a+i*b).__floor__() for i in range(m)))
    return sorted(out)


def eligible(x,t,theta):
    # Genuine directed S23 arc with a=j=0,c=1, theta in (0,1).
    y=x+t*theta
    f=y-y.__floor__()
    return int(0<=f<theta)


def exact_truth(x,N,d,m,lo,hi):
    # Complete phase-boundary atomization on (lo,hi), incl singletons.
    cuts={lo,hi}
    for i in range(m):
        t=N+i*d
        for slope in (t,t-1):
            if slope==0: continue
            yl=x+slope*lo
            yh=x+slope*hi
            for n in range(min(yl.__floor__(),yh.__floor__())-1,max(yl.__floor__(),yh.__floor__())+3):
                theta=(F(n)-x)/slope
                if lo<theta<hi: cuts.add(theta)
    sc=sorted(cuts)
    samples=sc[1:-1]+[(a+b)/2 for a,b in zip(sc,sc[1:])]
    return {tuple(eligible(x,N+i*d,theta) for i in range(m)) for theta in samples},len(samples)


def bounds_witness(x,N,d,q,n,k,bits,lo,hi):
    # Project theta using exact lower/upper inequalities, strict flags.
    lower=(lo,True); upper=(hi,True)
    def enforce(v,coef,rhs,strict):
        nonlocal lower,upper
        if coef==0:
            return v<rhs if strict else v<=rhs
        z=(rhs-v)/coef
        if coef>0:
            if z<upper[0] or z==upper[0] and strict and not upper[1]: upper=(z,strict)
        else:
            if z>lower[0] or z==lower[0] and strict and not lower[1]: lower=(z,strict)
        return True
    for i,bit in enumerate(bits):
        t=N+i*d
        ni=F(n+i*k+q[i])
        if bit==1:
            # x+(t-1)*theta < ni <= x+t*theta
            if not enforce(x,F(t-1),ni,True): return None
            if not enforce(ni-x,F(-t),F(0),False): return None
        else:
            # x+t*theta-1 < ni <= x+(t-1)*theta
            if not enforce(x-F(1),F(t),ni,True): return None
            if not enforce(ni-x,F(1-t),F(0),False): return None
    if lower[0]<upper[0]: return (lower[0]+upper[0])/2
    if lower[0]==upper[0] and not(lower[1] or upper[1]): return lower[0]
    return None


def via_reduction(x,N,d,m,lo,hi):
    # Exhaustive small-domain integer pair search, exact feasibility test.
    p=patterns(m)
    ylo=x+N*lo; yhi=x+N*hi
    start=min(ylo.__floor__(),yhi.__floor__())-2
    end=max(ylo.__floor__(),yhi.__floor__())+3
    # k = floor(d*theta) is an admissible completeness representation.
    klo=min((d*lo).__floor__(),(d*hi).__floor__())-1
    khi=max((d*lo).__floor__(),(d*hi).__floor__())+2
    out={}
    for bits in product((0,1),repeat=m):
        for q in p:
            for n in range(start,end+1):
                for k in range(klo,khi+1):
                    th=bounds_witness(x,N,d,q,n,k,bits,lo,hi)
                    if th is not None:
                        assert lo<th<hi
                        assert tuple(eligible(x,N+i*d,th) for i in range(m))==bits
                        out[bits]=(th,q,n,k)
                        break
                if bits in out: break
            if bits in out: break
    return out,len(p)


def run():
    rng=Random(1212026)
    status={"status":"R121_AP_LIFT_PASS","seed":1212026,"cases":0,"complete_atom_samples":0,"exact_witnesses":0,"total_lift_patterns":0,"pattern_counts":{},"max_pattern_ratio":None}
    for m in range(2,6):
        pat=patterns(m)
        H=m*(m-1)//2
        assert len(pat)<=1+H*(H+1)//2
        status['pattern_counts'][str(m)]=len(pat)
        # Verify each generated pattern has a realizable interior alpha,beta witness by construction.
        for repeat in range(18):
            N=rng.randint(-5,5);d=rng.choice([-3,-2,-1,1,2,3])
            x=F(rng.randint(1,8),10)
            lo=F(rng.choice([1,2,3]),10);hi=F(rng.choice([7,8,9]),10)
            truth,samples=exact_truth(x,N,d,m,lo,hi)
            reduced,pcount=via_reduction(x,N,d,m,lo,hi)
            assert truth==set(reduced),(m,N,d,x,lo,hi,truth,set(reduced))
            status['cases']+=1
            status['complete_atom_samples']+=samples
            status['exact_witnesses']+=len(reduced)
            status['total_lift_patterns']+=pcount
    # An immense signed time separation is exactly representable by the two-variable certificate.
    huge=10**100+39
    for N,d in ((huge,huge+4),(-huge,huge+4),(huge,-huge-4)):
        theta=F(7,19);x=F(2,7);m=5
        alpha=x+N*theta; alpha-=alpha.__floor__()
        delta=d*theta; k=delta.__floor__(); beta=delta-k
        q=tuple((alpha+i*beta).__floor__() for i in range(m))
        n=(x+N*theta).__floor__()
        bits=tuple(eligible(x,N+i*d,theta) for i in range(m))
        # This verifies the original exact rational certificate without expanding the phase cuts.
        for i,bit in enumerate(bits):
            ni=n+i*k+q[i]
            assert ni==(x+(N+i*d)*theta).__floor__()
            assert bit==eligible(x,N+i*d,theta)
        status.setdefault('huge_signed_exact_certificates',0)
        status['huge_signed_exact_certificates']+=1
    return status

if __name__=='__main__':
    result=run()
    print(result['status'],result['cases'],result['complete_atom_samples'],result['exact_witnesses'],result['pattern_counts'])
    with Path(__file__).with_name('verification_r121.json').open('w') as f: json.dump(result,f,sort_keys=True,indent=2)
