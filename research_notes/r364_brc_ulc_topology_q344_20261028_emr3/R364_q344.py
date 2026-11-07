#!/usr/bin/env python3
"""R364: exact Q344 Newton/Turan/ULC, original signed 12 K/J recurrence."""
from __future__ import annotations
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
SRC=P/'research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3'
if not (SRC/'R346_verify.py').exists():
    SRC=P.parent/'r346_unbounded_interior_tp2_corank301_20261028_emr3'
sys.path.insert(0,str(SRC))
from R346_verify import K,J,C,add,mul,forward_differences as fd,eval_newton

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def main():
    start=time.monotonic();R=344;smax=3*(R+1)+2;lim=2*(R+1)+2
    kk=[None]+[K(i) for i in range(1,13)]; B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    print('B_READY',round(time.monotonic()-start,3),flush=True)
    L={}
    for r in range(R-2,R+2):
        ds=fd([Fraction(D(B,r+u,u),5**u) for u in range(r+2)])
        assert ds[-1]==0 and ds[-2]==6**r,(r,'H support/lead')
        z=[x*5**r for x in ds[:-1]]
        assert all(x.denominator==1 for x in z)
        L[r]=eval_newton([int(x) for x in z],2*R+3)
    out={};all_c={}
    for r in (343,344):
        val=[L[r][v+1]*L[r][v+2]-L[r-1][v+2]*L[r+1][v+1] for v in range(2*r+1)]
        c=fd(val); all_c[r]=c;n=2*r
        assert len(c)==n+1 and all(x>0 for x in c)
        assert c[-1]==30**n*comb(n,r)//(r+1)
        assert Fraction(c[-2],c[-1])==Fraction(17*r+11,10)
        assert Fraction(c[-3],c[-1])==Fraction(7803*r**3+2252*r**2-5523*r+3328,2700*(2*r-1))
        assert all(c[j]**2>c[j-1]*c[j+1] for j in range(1,n))
        signs=[(c[j]**2*j*(n-j)>c[j-1]*c[j+1]*(j+1)*(n-j+1))-
               (c[j]**2*j*(n-j)<c[j-1]*c[j+1]*(j+1)*(n-j+1)) for j in range(1,n)]
        runs=[]
        for j,sign in enumerate(signs,1):
            if not runs or sign!=runs[-1][0]:runs.append([sign,j,j])
            else:runs[-1][2]=j
        raw=''.join(f'{r},{j},{x}\n' for j,x in enumerate(c)).encode()
        h=sha256(raw).hexdigest()
        if r==343: assert h=='019e7f8866384a1e5beed7ed05f69a77c784333932057106c3dd4a20dca90899'
        if r==344:(P/'R364_Q344_FULL_COEFFICIENTS.txt').write_bytes(raw)
        out[r]={'coefficient_count':len(c),'positive_coefficients':len(c),'turan_strict':n-1,
                'ulc_fail':signs.count(-1),'ulc_pass':signs.count(1),'ulc_equal':signs.count(0),
                'ulc_runs':runs,'sha256':h,'peak_index':max(range(len(c)),key=c.__getitem__),
                'first_three':[str(v) for v in c[:3]],'last_three':[str(v) for v in c[-3:]]}
        print(r,len(c),h,runs,flush=True)
    for k in range(1,9):
        q=344+k
        m=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
        assert m==Fraction((L[344][k]*L[344][k+1]-L[343][k+1]*L[345][k])*5**(2*k+1),5**(2*344)) and m>0
    res={'schema':'R364_Q344_SIGNED_BRC_EXACT_V1','model':'original signed 12-term K/J auxiliary model',
         'B_max_s':smax,'H_r_range':[342,345],'q343_regression':'PASS','eight_raw_D_minors':'PASS',
         'r343':out[343],'r344':out[344],
         'scope':'finite r=344, all k inference conditional on diagonal extraction (R363) and independent review pending',
         'native_X6_bridge':'not established','arithmetic':'exact int Fraction only',
         'runtime_sec':round(time.monotonic()-start,3)}
    (P/'R364_Q344_EVIDENCE.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
    print('FINAL',json.dumps({k:v for k,v in res.items() if k not in ['r343','r344']}),flush=True)
if __name__=='__main__':main()
