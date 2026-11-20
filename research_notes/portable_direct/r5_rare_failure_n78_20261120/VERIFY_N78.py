#!/usr/bin/env python3
"""R5 rare-failure asymptotic through N^78; exact integer/rational verification.
Requires frozen input and pinned predecessor VERIFY_N84.py, RESULT_N84.json.
"""
import json, hashlib
from math import comb, factorial, prod
from fractions import Fraction as Q
from pathlib import Path
from VERIFY_N84 import short_moments, overlap_moments

PIN = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
ORDER = 17
A = tuple(range(214,219))
S1 = (214,216,217,218,219,220,221)
S2 = (215,216,217,218,219,220,221)
S4 = tuple(range(296,313))
B = tuple(range(219,315))
D = tuple(range(222,315))
E4 = tuple(range(214,296)) + (313,314)
E04 = tuple(range(219,296)) + (313,314)
PPRIME = prod(B)
J = 219*220*221

def factor_series(n):
    # x/(1-exp(-x)) by exact reciprocal series
    f=[Q(0)]*(n+1); f[0]=Q(1)
    for k in range(1,n+1):
        f[k]=-sum(f[k-i]*Q((-1)**i,factorial(i+1)) for i in range(1,k+1))
    return f

def log_series(f):
    n=len(f)-1; g=[Q(0)]*(n+1)
    for j in range(1,n+1):
        g[j]=f[j]-sum(Q(k,j)*g[k]*f[j-k] for k in range(1,j))
    return g

FAC=factor_series(ORDER)
LOG=log_series(FAC)

def laplace(prices,n):
    logs=[Q(0)]+[LOG[k]*sum(p**k for p in prices) for k in range(1,n+1)]
    out=[Q(1)]+[Q(0)]*n
    for j in range(1,n+1):
        out[j]=sum(k*logs[k]*out[j-k] for k in range(1,j+1))/j
    return out

def laplace_by_convolution(prices,n):
    out=[Q(1)]+[Q(0)]*n
    for p in prices:
        out=[sum(out[j-k]*FAC[k]*p**k for k in range(j+1)) for j in range(n+1)]
    return out

def direct_s4_moments(m,power):
    ans=[0]*(power+1)
    def rec(i,k,w):
        if i==len(S4):
            for j in range(power+1): ans[j]+=w**j
            return
        for t in range(m-k): rec(i+1,k+t,w+t*S4[i])
    rec(0,0,0)
    return ans

def coefficients(m):
    M=short_moments(A,m,ORDER)
    H1=short_moments(S1,m,ORDER-2)
    H2=short_moments(S2,m,ORDER-2)
    V=overlap_moments(m,ORDER-3)
    L=short_moments(S4,m,ORDER-12)
    aB=laplace(B,ORDER); aD=laplace(D,ORDER-3)
    a1=laplace(D+(215,),ORDER-2)
    a2=laplace(D+(214,),ORDER-2)
    a4=laplace(E4,ORDER-12)
    ratio4=Q(PPRIME,prod(E4))
    ratio04=Q(PPRIME,prod(E04))
    assert L[0]==comb(m+16,17)
    assert M[0]==comb(m+4,5)
    full={}; new_parts={}
    for j in range(ORDER+1):
        first=sum(Q((-1)**r*M[r],factorial(r))*aB[j-r] for r in range(j+1))
        second=Q(0)
        if j>=2:
            for e,H,a in ((215,H1,a1),(214,H2,a2)):
                second+=Q(J,e)*sum(Q((-1)**r*H[r],factorial(r))*a[j-2-r]
                                 for r in range(j-1))
        third=-J*sum(Q((-1)**r*V[r],factorial(r))*aD[j-3-r]
                     for r in range(j-2)) if j>=3 else Q(0)
        s4=ratio4*sum(Q((-1)**r*L[r],factorial(r))*a4[j-12-r]
                     for r in range(j-11)) if j>=12 else Q(0)
        overlap04=-ratio04*M[0]*L[0] if j==17 else Q(0)
        full[str(95-j)]=str(first+second+third+s4+overlap04)
        if j>=12:
            new_parts[str(95-j)]={'s4':str(s4),'s0s4':str(overlap04)}
    return {
        'm':m,
        'S4_moments_L0_to_L5':[str(x) for x in L],
        'V14':str(V[14]),
        'new_coefficients':{k:v for k,v in full.items() if int(k)<=83},
        'new_event_terms':new_parts,
        'all_coefficients':full,
    }

def main():
    here=Path(__file__).parent
    data=here/'EXACT_R5_ALL_101_BUDGETS.json'
    digest=hashlib.sha256(data.read_bytes()).hexdigest()
    assert digest==PIN, ('frozen input mismatch',digest)
    for m in (1,2,3):
        assert short_moments(S4,m,5)==direct_s4_moments(m,5),m
    for prices in (B,D,D+(214,),D+(215,),E4,E04):
        assert laplace(prices,ORDER)==laplace_by_convolution(prices,ORDER),prices
    for k in range(3,ORDER+1,2): assert FAC[k]==0,k
    rows=[coefficients(m) for m in (1,2,3,5,8,17)]
    predecessor=json.loads((here/'RESULT_N84.json').read_text())
    for now,old in zip(rows,predecessor['rows']):
        assert now['m']==old['m']
        for degree,value in old['all_high_coefficients'].items():
            assert now['all_coefficients'][degree]==value,(now['m'],degree)
    assert Q(rows[0]['new_event_terms']['83']['s4'])==Q(PPRIME,prod(E4))
    assert Q(rows[0]['new_event_terms']['78']['s0s4'])==-Q(PPRIME,prod(E04))
    outcome={
        'schema':'R5_RARE_FAILURE_N78_V1',
        'source_frozen_sha256':PIN,
        'theorem':'F_m(N)=sum_{j=0}^{17} B_{95-j}(m) N^(95-j)/((95-j)!*Pprime)+O_m(N^77), fixed m>=1',
        'evidence':'AUTHOR_SYMBOLIC_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED',
        'verification':{
            'S4_direct_brute_m':[1,2,3],
            'predecessor_B95_through_B84_m':[1,2,3,5,8,17],
            'two_laurent_engines':True,
            'laurent_order':ORDER,
            'full_pair_census_recomputed':False,
            'exact_arithmetic':True,
        },
        'constants':{
            'Pprime':'product(219..314)',
            'E4':'214..295,313,314',
            'E04':'219..295,313,314',
            'K4':str(Q(PPRIME,prod(E4))),
            'K04':str(Q(PPRIME,prod(E04))),
        },
        'rows':rows
    }
    (here/'RESULT_N78.json').write_text(json.dumps(outcome,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'verified':True,
        'samples':[{'m':r['m'],'B83':r['new_coefficients']['83'],
                    'B78':r['new_coefficients']['78'],
                    'S4_bad_configs':r['S4_moments_L0_to_L5'][0]} for r in rows]},
        ensure_ascii=False,indent=2))
    return outcome

if __name__=='__main__':main()
