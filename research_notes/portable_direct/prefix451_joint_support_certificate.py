#!/usr/bin/env python3
"""PREFIX-451: exact native X6 endpoint/history support and typed quadratic moments.
Uses the unmodified pinned signed_brc.py (Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176).
Only standard-library integers and Fraction; no floating arithmetic or external models.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial
import hashlib
import importlib.util
import os
from pathlib import Path

HERE=Path(__file__).resolve().parent
PINNED=Path(os.environ.get('EM_PINNED_BRC_PATH', str(HERE.parents[1]/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py')))
raw=PINNED.read_bytes()
blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
assert blob=='300a96e3dc24bf6fff73743037a0347a8bc83176'
spec=importlib.util.spec_from_file_location('pinned_signed_brc',PINNED)
signed=importlib.util.module_from_spec(spec)
spec.loader.exec_module(signed)
ZERO=(0,)*6
STEPS=tuple(tuple(s if j==i else 0 for j in range(6))
            for i in range(6) for s in (1,-1))

def shell(m):
    if m==0: return 1
    return sum(2**j*comb(6,j)*comb(m-1,j-1) for j in range(1,min(6,m)+1))

def binom7(n):
    return comb(n,7) if n>=7 else 0

def H_formula(q,n):
    return sum(comb(4,j)*(binom7(n-j+7)-binom7(n-2*q-j+7)) for j in range(5))

def H_shell(q,n):
    return sum(shell(n-2*t)*min(q,t+1) for t in range(n//2+1))

def sector_count(q,n,x):
    m=sum(abs(v) for v in x)
    if m>n or (n-m)%2: return 0
    return min(q,(n-m)//2+1)

def support_dp(q,N):
    d={(0,ZERO):1}
    yield 0,d
    for n in range(1,N+1):
        e=defaultdict(int)
        for (r,x),mass in d.items():
            for v in STEPS:
                s=(r+(v[0]==-1 and sum(abs(z) for z in v)==1))%q
                y=tuple(a+b for a,b in zip(x,v))
                e[(s,y)]+=mass
        d=dict(e)
        yield n,d

def exact_moment(hist):
    """Per-sector packed symmetric 7x7 moments, exactly the MomentState convention."""
    res={}
    for (r,x),w in hist.items():
        v=x+(1,)
        if r not in res: res[r]=[Fraction(0) for _ in range(28)]
        p=0
        for i in range(7):
            for j in range(i,7):
                res[r][p]+=w*v[i]*v[j]
                p+=1
    return {k:tuple(v) for k,v in res.items()}

def weighted_step(hist,q,kernel):
    e=defaultdict(Fraction)
    for (r,x),mass in hist.items():
        for v in STEPS:
            target=(r+(v[0]==-1))%q
            y=tuple(a+b for a,b in zip(x,v))
            e[target,y]+=mass*kernel[r,v]
    return dict(e)

def transfer_quadratic(hist,q,kernel):
    """Exact H Q H^T on moments; no endpoint iteration in the transfer."""
    first=exact_moment(hist)
    out={s:[[Fraction(0) for _ in range(7)] for _ in range(7)] for s in range(q)}
    for r,upper in first.items():
        Q=[[Fraction(0) for _ in range(7)] for _ in range(7)]
        z=0
        for i in range(7):
            for j in range(i,7): Q[i][j]=Q[j][i]=upper[z]; z+=1
        for v in STEPS:
            s=(r+(v[0]==-1))%q
            w=kernel[r,v]
            h=[list(row) for row in [[int(i==j) for j in range(7)] for i in range(7)]]
            for i in range(6): h[i][6]=v[i]
            for i in range(7):
                for j in range(i,7):
                    val=Fraction(0)
                    for a in range(7):
                        for b in range(7):
                            if h[i][a] and h[j][b]: val+=h[i][a]*Q[a][b]*h[j][b]
                    out[s][i][j]+=w*val
                    if i!=j: out[s][j][i]+=w*val
    packed={}
    for r,Q in out.items(): packed[r]=tuple(Q[i][j] for i in range(7) for j in range(i,7))
    return packed

def run():
    checks=0
    for q in (2,3,4,7):
        for n,d in support_dp(q,7):
            assert len(d)==H_formula(q,n)==H_shell(q,n),(q,n,len(d),H_formula(q,n))
            endpoints={x for r,x in d}
            assert sum(sector_count(q,n,x) for x in endpoints)==len(d)
            assert sum(d.values())==12**n
            subset=sorted(endpoints) if n<=3 else sorted(endpoints)[::max(1,len(endpoints)//40)]
            for x in subset:
                assert sum(c for (r,y),c in d.items() if y==x)==signed.endpoint_multiplicity(n,x)
                checks+=1
            print(f'REACHABLE_PASS q={q} N={n} joint_bins={len(d)} endpoints={len(endpoints)} words={12**n}')
    q=3
    states=list(support_dp(q,4))[-1][1]
    assert len(states)==1059
    assert sum(1 for (r,x) in states if x==ZERO)==3
    assert [states[(r,ZERO)] for r in range(3)]==[270,120,6]
    assert sum(states[(r,ZERO)] for r in range(3))==signed.endpoint_multiplicity(4,ZERO)==396
    print('ORIGIN_CERTIFICATE_PASS q=3 N=4 counts_by_residue=(270,120,6) total=396')

    p0=((1,0,0,0,0,0),(-1,0,0,0,0,0))
    p1=((0,1,0,0,0,0),(0,-1,0,0,0,0))
    assert tuple(sum(x[i] for x in p0) for i in range(6))==ZERO
    assert tuple(sum(x[i] for x in p1) for i in range(6))==ZERO
    assert sum(step[0]==-1 for step in p0)%q==1
    assert sum(step[0]==-1 for step in p1)%q==0
    print('MINIMAL_RESIDUAL_PASS N=2 same_endpoint=(0,...,0), histories=0/1, future_weights=1/2')

    kernel={(r,v):Fraction(1+(r*3+idx)%5, 1+(r+idx)%4)
            for r in range(q) for idx,v in enumerate(STEPS)}
    original={(r,x):Fraction(c) for (r,x),c in list(support_dp(q,3))[-1][1].items()}
    for round_i in range(2):
        predicted=transfer_quadratic(original,q,kernel)
        actual=weighted_step(original,q,kernel)
        dense=exact_moment(actual)
        zero=(Fraction(0),)*28
        assert all(predicted[r]==dense.get(r,zero) for r in range(q))
        print(f'BRC_MOMENT_PASS round={round_i+1} input_bins={len(original)} output_bins={len(actual)} packed=84')
        original=actual
    print(f'PASS frozen_brc_blob={blob} pinned_endpoint_checks={checks}')

if __name__=='__main__':run()
