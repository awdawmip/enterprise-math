#!/usr/bin/env python3
"""All q=1 polynomial coefficients N^95..N^48, and parity resonance at N^47.
Run after VERIFY_N78.py; input EXACT_R5_ALL_101_BUDGETS.json must match PIN.
Only standard-library exact arithmetic.
"""
from fractions import Fraction as F
from math import comb, factorial, prod
import json, hashlib
from pathlib import Path
from VERIFY_N84 import short_moments, overlap_moments

PIN='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
A0=tuple(range(214,219))
A1=(214,216,217,218,219,220,221)
A2=(215,216,217,218,219,220,221)
A4=tuple(range(296,313))
P=tuple(range(214,315))
B=tuple(range(219,315))
D=tuple(range(222,315))
E4=tuple(p for p in P if p not in A4)
E04=tuple(p for p in P if p not in A0+A4)
E14=tuple(p for p in P if p not in A1+A4)
E24=tuple(p for p in P if p not in A2+A4)
Eh4=tuple(p for p in P if p not in tuple(range(214,222))+A4)
Pprime=prod(B)

def laplace(prices,n):
    f=[F(1)]+[F(0)]*n
    for k in range(1,n+1):
        f[k]=-sum(f[k-i]*F((-1)**i,factorial(i+1)) for i in range(1,k+1))
    g=[F(0)]*(n+1)
    for j in range(1,n+1):
        g[j]=f[j]-sum(F(k,j)*g[k]*f[j-k] for k in range(1,j))
    sums=[0]+[sum(p**j for p in prices) for j in range(1,n+1)]
    x=[F(1)]+[F(0)]*n
    for j in range(1,n+1):
        x[j]=sum(k*g[k]*sums[k]*x[j-k] for k in range(1,j+1))/j
    return x

def convolution(a,b,n):
    return [sum(comb(k,j)*a[j]*b[k-j] for j in range(k+1)) for k in range(n+1)]

def coefficients(m,degree=47):
    M=short_moments(A0,m,degree)
    H1=short_moments(A1,m,max(0,degree-2))
    H2=short_moments(A2,m,max(0,degree-2))
    V=overlap_moments(m,max(0,degree-3))
    L=short_moments(A4,m,max(0,degree-12))
    LM=convolution(L,M,max(0,degree-17))
    LH1=convolution(L,H1,max(0,degree-19))
    LH2=convolution(L,H2,max(0,degree-19))
    LV=convolution(L,V,max(0,degree-20))
    entries=[
        (0,+1,B,M),
        (2,+1,tuple(sorted(set(P)-set(A1))),H1),
        (2,+1,tuple(sorted(set(P)-set(A2))),H2),
        (3,-1,D,V),
        (12,+1,E4,L),
        (17,-1,E04,LM),
        (19,-1,E14,LH1),
        (19,-1,E24,LH2),
        (20,+1,Eh4,LV),
    ]
    result=[F(0)]*(degree+1)
    for shift,sign,E,moments in entries:
        if shift>degree:continue
        factor=F(Pprime,prod(E))
        a=laplace(E,degree-shift)
        for j in range(degree-shift+1):
            result[shift+j]+=sign*factor*sum(
                F((-1)**r*moments[r],factorial(r))*a[j-r]
                for r in range(j+1))
    return result

def main():
    here=Path(__file__).parent
    frozen=here/'EXACT_R5_ALL_101_BUDGETS.json'
    assert hashlib.sha256(frozen.read_bytes()).hexdigest()==PIN
    old_file=here/'RESULT_N78.json'
    if not old_file.is_file():
        from VERIFY_N78 import main as run_n78
        run_n78()
    old=json.loads(old_file.read_text())
    cases=[]
    for m in (1,2,3):
        full=coefficients(m,47)
        predecessor=next(r for r in old['rows'] if r['m']==m)
        for degree,value in predecessor['all_coefficients'].items():
            assert full[95-int(degree)]==F(value),(m,degree)
        cases.append({'m':m,'B48':str(full[47]),'B77':str(full[18]),
            'B76':str(full[19]),
            'all_high_coefficients':{str(95-j):str(x) for j,x in enumerate(full)}})
    for m in (5,8,17):
        fine=coefficients(m,20)
        predecessor=next(r for r in old['rows'] if r['m']==m)
        for degree,value in predecessor['all_coefficients'].items():
            assert fine[95-int(degree)]==F(value),(m,degree)
        cases.append({'m':m,'B77':str(fine[18]),'B76':str(fine[19]),
            'B78':str(fine[17])})
    evenB=tuple(p for p in B if p%2==0)
    E2=tuple(sorted(set(P)-set(A2)))
    evenE2=tuple(p for p in E2 if p%2==0)
    assert len(evenB)==len(evenE2)==48
    assert sum(p%2 for p in B)==48
    assert sum(p%2 for p in E2)==46
    parity=F(1,2**48*prod(evenB))+F(1,2**46*prod(evenE2))
    assert parity>0
    out={
        'schema':'R5_RARE_FAILURE_HIGH_DEGREE_N48_V1',
        'theorem':'fixed m>=1: F_m(N)=sum_{j=0}^{47} B_(95-j)(m) N^(95-j)/((95-j)! Pprime)+O_m(N^47)',
        'nonzero_period_2_m1':'(-1)^N * parity_constant * N^47 / 47! plus lower powers',
        'parity_constant':str(parity),
        'frozen_sha256':PIN,
        'evidence':'AUTHOR_SYMBOLIC_PROOF / EXACT_FRACTION_VERIFIED / NOT_REVIEWED',
        'verification':{'full_48_coefficients_for_m':[1,2,3],
            'through_N75_for_m':[5,8,17],
            'all_prior_B95_to_B78_matched':True,
            'full_pair_census_recomputed':False},
        'rows':cases
    }
    (here/'RESULT_HIGH_DEGREE.json').write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'verified':True,'parity_constant':str(parity),
        'samples':[{'m':r['m'],'B77':r['B77'],'B76':r['B76']} for r in cases]},
        ensure_ascii=False,indent=2))
    return out

if __name__=='__main__': main()
