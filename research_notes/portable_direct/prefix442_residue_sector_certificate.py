#!/usr/bin/env python3
"""PREFIX-442 exact source-residue observer certificate. Run with PYTHONPATH=.

Pinned native signed BRC: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d
module experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py
blob 300a96e3dc24bf6fff73743037a0347a8bc83176.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path
from hashlib import sha1
from experiments.x6_signed_native_spatial_v16_20260905 import signed_brc

EXPECTED_BRC_BLOB = "300a96e3dc24bf6fff73743037a0347a8bc83176"

def source_blob_check():
    raw = Path(signed_brc.__file__).read_bytes()
    digest = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert digest == EXPECTED_BRC_BLOB, (digest, EXPECTED_BRC_BLOB)
    return digest

def rank(rows):
    if not rows: return 0
    a = [list(map(Fraction, row)) for row in rows]
    m,n = len(a), len(a[0]); pivot_col = 0; r = 0
    while pivot_col < n and r < m:
        pivot = next((t for t in range(r,m) if a[t][pivot_col]), None)
        if pivot is None:
            pivot_col += 1; continue
        a[r],a[pivot] = a[pivot],a[r]
        v = a[r][pivot_col]
        a[r] = [w/v for w in a[r]]
        for t in range(r+1,m):
            w = a[t][pivot_col]
            if w: a[t] = [u-w*z for u,z in zip(a[t],a[r])]
        r += 1; pivot_col += 1
    return r

def determinant(rows):
    a = [list(map(Fraction,row)) for row in rows]
    n = len(a); assert all(len(row)==n for row in a)
    ans = Fraction(1)
    for j in range(n):
        i = next((i for i in range(j,n) if a[i][j]),None)
        if i is None: return Fraction(0)
        if i != j: a[i],a[j] = a[j],a[i]; ans = -ans
        v = a[j][j]; ans *= v
        for i in range(j+1,n):
            z = a[i][j]/v
            for t in range(j+1,n):a[i][t] -= z*a[j][t]
            a[i][j] = Fraction(0)
    return ans

def obs_matrix(n,q,d):
    return [[int(k%q == r) * (n-2*k)**j for k in range(n+1)]
            for r in range(q) for j in range(d+1)]

def obs_hist(hist,n,q,d):
    return {(r,j):sum(count*(n-2*k)**j for k,count in hist.items() if k%q==r)
            for r in range(q) for j in range(d+1)}

def pol_mul(a,b):
    z=[Fraction(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j] += v*w
    return z

def recover(hist_obs,n,q,d):
    recovered={}
    for r in range(q):
        ks=[k for k in range(n+1) if k%q==r]
        if len(ks)>d+1: raise ValueError("observer beyond complete recovery horizon")
        xs=[n-2*k for k in ks]
        for k,x in zip(ks,xs):
            p=[Fraction(1)]; den=Fraction(1)
            for y in xs:
                if y!=x:
                    p=pol_mul(p,[Fraction(-y),Fraction(1)])
                    den *= x-y
            val=sum((co*hist_obs[r,j] for j,co in enumerate(p)),Fraction())/den
            assert val.denominator==1
            recovered[k]=int(val)
    return recovered

def witness(n,q,d):
    m=d+1; assert n>=q*m
    plus=Counter(); minus=Counter()
    for j in range(m+1):
        k=q*j
        (plus if j%2==0 else minus)[k]=comb(m,j)
        # Distinct one-axis words exist: choose entire q-block subsets.
        assert comb(n,k)>=comb(m,j)
        signed_x6=(n-2*k,0,0,0,0,0)
        assert signed_brc.endpoint_multiplicity(n,signed_x6)>=comb(n,k)
    assert sum(plus.values())==sum(minus.values())==2**d
    assert obs_hist(plus,n,q,d)==obs_hist(minus,n,q,d)
    gap=sum(c*(n-2*k)**m for k,c in plus.items())-sum(c*(n-2*k)**m for k,c in minus.items())
    assert gap==factorial(m)*(2*q)**m
    return plus,minus,gap

def sector_readout(words,q,d):
    h=Counter(sum(1 for t in w if t==-1) for w in words)
    n=len(words[0]) if words else 0
    assert all(len(w)==n for w in words)
    return obs_hist(h,n,q,d)

def stepped_observer(source,q,d,sign):
    target={(r,j):Fraction(0) for r in range(q) for j in range(d+1)}
    for r in range(q):
        dest=(r+(sign==-1))%q
        for j in range(d+1):
            target[dest,j]+=sum(comb(j,i)*sign**(j-i)*source[r,i] for i in range(j+1))
    return target

def test_rank_and_recovery():
    cases=0
    for n in range(0,22):
        for q in range(1,8):
            for d in range(0,6):
                rows=obs_matrix(n,q,d)
                expected=sum(min(d+1,len(range(r,n+1,q))) for r in range(q))
                assert rank(rows)==expected
                assert (rank(rows)==n+1)==(n < q*(d+1))
                if n < q*(d+1):
                    bag=Counter({k:min(comb(n,k),(7*k+3)%4) for k in range(n+1)})
                    assert recover(obs_hist(bag,n,q,d),n,q,d)==dict(bag)
                cases+=1
    print('PASS rank/recovery:',cases,'(n,q,d) cases; exact Fraction Gaussian elimination + Lagrange inversion')

def test_witnesses():
    cases=0
    for q in range(1,6):
        for d in range(0,5):
            for n in range(q*(d+1),min(q*(d+1)+3,30)):
                witness(n,q,d);cases+=1
    E,O,gap=witness(6,2,2)
    assert E==Counter({0:1,4:3}) and O==Counter({2:3,6:1}) and gap==384
    A=Counter({0:1,3:2});B=Counter({1:2,4:1})
    assert obs_hist(A,4,1,2)==obs_hist(B,4,1,2)
    assert obs_hist(A,4,2,2)!=obs_hist(B,4,2,2)
    assert obs_hist(A,4,2,2)[0,1]-obs_hist(B,4,2,2)[0,1]==8
    mat=obs_matrix(4,1,2)+[[int(k%2==0) for k in range(5)],
            [int(k%2==0)*(4-2*k) for k in range(5)]]
    assert determinant(mat)==-512
    print('PASS integer source fibers:',cases,'general witness checks; q=2 d=2 gap=384; n=4 hybrid determinant=-512')

def test_future_closure():
    cases=0
    for q in range(1,5):
        for d in range(0,5):
            words=[(1,1,-1,-1),(1,-1,1,-1),(-1,1,-1,1),(-1,-1,1,1)]
            for sig in (1,-1):
                now=sector_readout(words,q,d)
                later=sector_readout([w+(sig,) for w in words],q,d)
                assert stepped_observer(now,q,d,sig)==later
                cases+=1
    print('PASS future signed-axis port closure:',cases,'cases; derived exact affine update (not an upstream ControlPacket run)')

def main():
    sha=source_blob_check()
    print('SOURCE pinned native signed_brc git blob:',sha)
    test_rank_and_recovery();test_witnesses();test_future_closure()
    print('PASS PREFIX-442 EXACT CERTIFICATE')

if __name__=='__main__':main()
