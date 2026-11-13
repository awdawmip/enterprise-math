#!/usr/bin/env python3
"""Exact signed BRC Newton interior minors, r=321..330; independent q320 regression.
Research-only auxiliary ordered-hex combinatorial model, no X6 native claim.
Uses unchanged K/J coefficients from the R346 original twelve-term recurrence.
"""
from pathlib import Path
import sys, json, time
from math import comb
from fractions import Fraction
from hashlib import sha256
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import C,K,J,add,mul,forward_differences,eval_newton

BASE=Path(__file__).resolve().parent
R348_320_SHA='ef944e5a2608a1566e8b508699dbf11b0428fd85e230a428d4cbb11071aa98e6'

def raw_D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def run():
    st=time.monotonic()
    r0,r1=320,330
    hmin,hmax=r0-1,r1+1
    smax=3*hmax+2
    limit=2*hmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(12,s)+1):z=add(z,mul(kk[i],B[s-i],limit),limit)
        B.append(z)
    assert len(B)==smax+1
    print('B_DONE',smax,'SECONDS',round(time.monotonic()-st,2),flush=True)
    L={};hd={}
    for r in range(hmin,hmax+1):
        x=[]
        for u in range(r+2):
            q=r+u
            x.append(Fraction(raw_D(B,q,u),5**u))
        nd=forward_differences(x)
        assert nd[-1]==0,(r,'extra finite interpolation check failed')
        nd=nd[:-1]
        assert len(nd)==r+1 and nd[-1]==6**r and all(v>0 for v in nd)
        sc=[v*5**r for v in nd]
        assert all(v.denominator==1 for v in sc)
        L[r]=eval_newton([int(v) for v in sc],2*r1+3)
        hd[r]=len(nd)
    print('H_DONE',hmin,hmax,'SECONDS',round(time.monotonic()-st,2),flush=True)
    d_all=sha256(); new_count=0; rows=[]; minor_checks=0; coeff_parts=[]
    for r in range(r0,r1+1):
        qvals=[L[r][u+1]*L[r][u+2]-L[r-1][u+2]*L[r+1][u+1] for u in range(2*r+1)]
        dif=forward_differences(qvals)
        assert len(dif)==2*r+1
        assert dif[-1]==30**(2*r)*comb(2*r,r)//(r+1),(r,'Catalan highest')
        assert all(isinstance(v,int) for v in dif)
        assert min(dif)>0,(r,'nonpositive Newton difference')
        lines=''.join(f'{r},{j},{v}\n' for j,v in enumerate(dif))
        digest=sha256(lines.encode()).hexdigest()
        if r==r0:
            assert digest==R348_320_SHA,(r,digest,R348_320_SHA)
        else:
            d_all.update(lines.encode());new_count+=len(dif);coeff_parts.append(lines)
            for k in range(1,5):
                q=r+k
                minor=raw_D(B,q,k)*raw_D(B,q+1,k+1)-raw_D(B,q,k+1)*raw_D(B,q+1,k)
                target=Fraction(qvals[k-1]*5**(2*k+1),5**(2*r))
                assert Fraction(minor)==target,(r,k,'raw D minor disagrees with Q')
                assert minor>0,(r,k,'raw D interior minor nonpositive')
                minor_checks+=1
        rows.append(dict(r=r,coeff_count=len(dif),sha256=digest,min_index=min(range(len(dif)),key=lambda i:dif[i]),min_digits=len(str(min(dif))),first_digits=len(str(dif[0])),last_digits=len(str(dif[-1])),all_positive=True,highest_catalan_pass=True))
        print('Q_DONE',r,'COUNT',len(dif),'DIGEST',digest,'SECONDS',round(time.monotonic()-st,2),flush=True)
    assert new_count==6520 and minor_checks==40
    coeffs=''.join(coeff_parts)
    (BASE/'R349_NEW_COEFFICIENTS.txt').write_text(coeffs)
    evidence=dict(schema='R349_EXACT_BRC_NEWTON_TP2_CORANK330_V1',date='2026-10-28',model='full signed 12-term ordered-hex BRC auxiliary recurrence',scope='author-side combinatorial model, no native X6 dynamics',source_unchanged='R346_verify.py from commit 37516cc5bb8d72098ce25f2d64881ec5da4279cd',smax=smax,truncation_degrees=[0,limit-1],H_range=[hmin,hmax],Q_range=[r0,r1],regression_r320_sha256=R348_320_SHA,new_r_range=[321,330],new_coeff_count=new_count,new_nonpositive_count=0,new_coeff_sha256=d_all.hexdigest(),highest_catalan_checks=11,raw_D_minor_checks=minor_checks,extra_node_zero_checks=len(L),rows=rows,arithmetic='exact Python integers/Fraction, no floating-point sign comparisons',theorem_strength='finite exact certificate + universal Newton polynomial theorem via previously published R348 author-side extraction proof; requires independent mathematical review',elapsed_seconds=round(time.monotonic()-st,3))
    (BASE/'R349_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print('RESULT',json.dumps({k:v for k,v in evidence.items() if k!='rows'}),flush=True)
if __name__=='__main__':run()
