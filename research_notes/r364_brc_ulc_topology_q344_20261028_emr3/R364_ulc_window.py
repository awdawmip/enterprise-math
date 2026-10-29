#!/usr/bin/env python3
"""Finite *windowed* exact ULC/PF2 signed BRC scan. Standalone by supplied R346 kernel."""
from __future__ import annotations
import json,sys,time
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
P=Path(__file__).resolve().parent
SRC=P/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'
if not (SRC/'R346_verify.py').exists():
    SRC=P.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'
sys.path.insert(0,str(SRC))
from R346_verify import K,J,C,add,mul,forward_differences as fd,eval_newton

def D(b,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*b[q+w][q] for w in range(k+1))

def run(lo,hi):
    assert 1<=lo<=hi<=1000
    st=time.monotonic();lim=2*(hi+1)+2;smax=3*(hi+1)+2
    ks=[None]+[K(i) for i in range(1,13)]
    b=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(ks[i],b[s-i],lim),lim)
        b.append(z)
    L={}
    for r in range(lo-1,hi+2):
        ds=fd([Fraction(D(b,r+u,u),5**u) for u in range(r+2)])
        assert ds[-1]==0 and ds[-2]==6**r,(r,'H finite samples')
        x=[y*5**r for y in ds[:-1]]
        assert all(y.denominator==1 for y in x)
        L[r]=eval_newton([int(y) for y in x],2*hi+3)
    rowsh=[];h=sha256();total_newton=total_turan=fail=passed=zero=0
    for r in range(lo,hi+1):
        n=2*r
        c=fd([L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(n+1)])
        assert len(c)==n+1 and all(x>0 for x in c),(r,'Newton positive')
        assert c[-1]==30**n*comb(n,r)//(r+1),(r,'Catalan top')
        assert Fraction(c[-2],c[-1])==Fraction(17*r+11,10),(r,'top second')
        assert Fraction(c[-3],c[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1)),(r,'top third')
        assert all(c[j]**2>c[j-1]*c[j+1] for j in range(1,n)),(r,'Turan')
        ulc=[(c[j]**2*j*(n-j)>c[j-1]*c[j+1]*(j+1)*(n-j+1)) -
             (c[j]**2*j*(n-j)<c[j-1]*c[j+1]*(j+1)*(n-j+1)) for j in range(1,n)]
        runs=[]
        for j,x in enumerate(ulc,1):
            if not runs or runs[-1][0]!=x:runs.append([x,j,j])
            else:runs[-1][2]=j
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(c)).encode()
        dig=sha256(raw).hexdigest();h.update(raw)
        if r==343:assert dig=='019e7f8866384a1e5beed7ed05f69a77c784333932057106c3dd4a20dca90899'
        if r==344:assert dig=='8b840f5fa5cb8aff6ccb57600fa792ad8ee98bfde39393107f1784361bac2143'
        rowsh.append({'r':r,'ulc_negative':ulc.count(-1),'ulc_positive':ulc.count(1),'ulc_zero':ulc.count(0),
                      'sign_runs':runs,'q_sha256':dig})
        total_newton+=len(c);total_turan+=n-1;fail+=ulc.count(-1);passed+=ulc.count(1);zero+=ulc.count(0)
    out={'schema':'R364_SIGNED_BRC_ULC_WINDOW_EXACT_V1','lo':lo,'hi':hi,'rows':rowsh,
         'newton_strict_positive':total_newton,'turan_strict_positive':total_turan,
         'ulc_negative':fail,'ulc_positive':passed,'ulc_zero':zero,
         'all_coefficient_sha256_in_window':h.hexdigest(),
         'model':'signed 12-term K/J auxiliary BRC','arithmetic':'exact int/Fraction',
         'runtime_sec':round(time.monotonic()-st,3)}
    path=P/f'R364_window_{lo:03d}_{hi:03d}.json'
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS',lo,hi,'newton',total_newton,'turan',total_turan,'ULC',fail,passed,zero,
          'seconds',round(time.monotonic()-st,3),flush=True)
    return out

if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]))
