#!/usr/bin/env python3
"""R351 exact signed BRC: r=332 Newton certificate and universal leading-law checks.

The code reuses the archived R346_verify.py exact 12-term K/J/arithmetics,
which must be placed in sibling research_notes/r346_... in the repository.
No native X6 transfer or mathematical admission is asserted.
"""
import json, sys, time
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from math import comb

BASE = Path(__file__).resolve().parent
repo_notes = BASE.parent
sys.path.insert(0, str(repo_notes/'r346_unbounded_interior_tp2_corank301_20261028_emr3'))
from R346_verify import K,J,C,add,mul,forward_differences,eval_newton

R350_Q331_SHA256 = '65eb081346caaa5a373437169ec27bf419537cdd69af14601017e197c2283356'

def D(B,q,k):
    return sum((-1)**(k-w)*C(k,w)*2**(q-w)*B[q+w][q] for w in range(k+1))

def run():
    start=time.monotonic()
    # These are exact identities of the signed 12-term K/J, NOT fitted coefficients.
    K0=[K(i)[0] if 0 < len(K(i)) else 0 for i in range(1,13)]
    K1=[K(i)[1] if 1 < len(K(i)) else 0 for i in range(1,13)]
    K2=[K(i)[2] if 2 < len(K(i)) else 0 for i in range(1,13)]
    assert K0==[2]+[0]*11
    assert K1==[3,-1]+[0]*10
    assert K2==[0,4,-8]+[0]*9
    assert sum(Fraction(coef,2**(i+1)) for i,coef in enumerate(K2))==0
    # K^(1)((1-y)/2) = 5/4 - y - y²/4, hence [y]K^(1)=-1.
    # Together with K^(2)(1/2)=0: E1(z) = z, E0(z)=1-5z/4.
    rmax=333; rmin=330
    smax=3*rmax+2; lim=2*rmax+2
    kk=[None]+[K(i) for i in range(1,13)]
    B=[[1,1]]
    for s in range(1,smax+1):
        z=J(s)
        for i in range(1,min(s,12)+1): z=add(z,mul(kk[i],B[s-i],lim),lim)
        B.append(z)
    print('B',smax,'seconds',round(time.monotonic()-start,3),flush=True)
    L={}; H_top={}
    for r in range(rmin,rmax+1):
        values=[]
        for u in range(r+2):
            q=r+u
            values.append(Fraction(D(B,q,u),5**u))
        dif=forward_differences(values)
        assert dif[-1]==0,(r,'extra degree-test node failed')
        dif=dif[:-1]
        assert dif[-1]==6**r,(r,'universal leading-law mismatch')
        assert all(v>0 for v in dif)
        scaled=[v*5**r for v in dif]
        assert all(x.denominator==1 for x in scaled)
        L[r]=eval_newton([int(v) for v in scaled],2*332+3)
        H_top[r]=str(dif[-1])
        print('H',r,'seconds',round(time.monotonic()-start,3),flush=True)
    summaries=[]; counts=0; q332_text=''
    for r in (331,332):
        vals=[L[r][u+1]*L[r][u+2]-L[r-1][u+2]*L[r+1][u+1] for u in range(2*r+1)]
        dif=forward_differences(vals)
        assert all(isinstance(x,int) for x in dif)
        assert all(x>0 for x in dif),(r,'sign not all positive')
        expected_top=30**(2*r)*comb(2*r,r)//(r+1)
        assert dif[-1]==expected_top,(r,'Catalan leading coefficient mismatch')
        lines=''.join(f'{r},{i},{x}\n' for i,x in enumerate(dif))
        digest=sha256(lines.encode()).hexdigest()
        if r==331:assert digest==R350_Q331_SHA256,(digest,R350_Q331_SHA256)
        else:
            q332_text=lines
            (BASE/'R351_Q332_FULL_COEFFICIENTS.txt').write_text(lines)
            counts=len(dif)
            for k in range(1,9):
                q=r+k
                actual=D(B,q,k)*D(B,q+1,k+1)-D(B,q,k+1)*D(B,q+1,k)
                desired=Fraction(vals[k-1]*5**(2*k+1),5**(2*r))
                assert Fraction(actual)==desired,(r,k,'direct determinant mismatch')
                assert actual>0
        summaries.append(dict(r=r,coefficients=len(dif),sha256=digest,strict_positive=all(x>0 for x in dif),zero_count=0,negative_count=0,min_index=min(range(len(dif)),key=lambda i:dif[i]),first_digits=len(str(dif[0])),last_digits=len(str(dif[-1])),universal_catalan_top_equal=True))
        print('Q',r,'sha256',digest,'seconds',round(time.monotonic()-start,3),flush=True)
    assert counts==665
    evidence=dict(schema='R351_BRC_NEWTON_CORANK332_V1',date='2026-10-28',status='AUTHOR_SIDE_EXACT_UNREVIEWED_NOT_ADMITTED',model='signed 12-term BRC auxiliary combinatorial recurrence',not_native_X6=True,signed_K_t_slices=['2x','3x-x^2','4x^2-8x^3'],K2_half_exact_zero=True,E0='1-5z/4',E1='z',proof_dependency='Author audit of R348 A1-A5 universal extraction, pending independent review',inherited_leading_law='R350: Delta^r H_r(0)=6^r and Delta^(2r) Q_r(0)=30^(2r) Catalan(r); conditional on R348 extraction',smax=smax,t_coefficient_range=[0,lim-1],H_range=[rmin,rmax],H_top_checks=H_top,r350_regression_r331=R350_Q331_SHA256,r332=next(x for x in summaries if x['r']==332),q331=next(x for x in summaries if x['r']==331),direct_minor_checks=8,full_integer_coeff_file='R351_Q332_FULL_COEFFICIENTS.txt',full_integer_coeff_file_sha256=sha256(q332_text.encode()).hexdigest(),exact_arithmetic=True,floating_sign_comparison=False,elapsed_seconds=round(time.monotonic()-start,3))
    (BASE/'R351_EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print('DONE',json.dumps(evidence,ensure_ascii=False),flush=True)

if __name__=='__main__': run()
