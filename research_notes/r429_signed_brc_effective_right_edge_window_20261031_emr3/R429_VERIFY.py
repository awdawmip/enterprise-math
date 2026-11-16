#!/usr/bin/env python3
"""R429 exact signed-BRC / finite-window verification; Python stdlib only."""
from math import comb, factorial
from fractions import Fraction
from itertools import combinations
from json import dump
from pathlib import Path

OUT = Path(__file__).resolve().parent

def choose(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0

def cat(r):
    return comb(2*r,r)//(r+1)

def delta_signed(r,s):
    return sum(comb(r-s,j)*(choose(2*s,r-2*j)-choose(2*s,r-2*j-1))
               for j in range(r-s+1))

def H(r,s):
    return comb(r+s,2*s)*delta_signed(r,s) if 2<=s<=r else 0

def B(r,h):
    return H(r,r-h) if 0<=h<=r-2 else 0

def c(r,h):
    return Fraction(B(r,h),cat(r)*r**h) if 0<=h<=r-2 else Fraction(0)

def det_integer(mat):
    a=[list(row) for row in mat]
    n=len(a)
    if not n: return 1
    previous=1
    sign=1
    for k in range(n-1):
        if a[k][k]==0:
            ip=next((p for p in range(k+1,n) if a[p][k]),None)
            if ip is None: return 0
            a[k],a[ip]=a[ip],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%previous==0
                a[i][j]=z//previous
            a[i][k]=0
        previous=pivot
    return sign*a[n-1][n-1]

def R(K):
    return 2**(K+6)*K**3*factorial(K+1)*(K+1)*factorial(K)**(K+1)

def main():
    exact_conv_checks=0
    coeff_checks=0
    for r in range(4,83):
        for h in range(min(8,r-2)+1):
            q=r-h
            lhs=delta_signed(r,q)
            rhs=sum(comb(h,j)*(choose(2*q,q+h-2*j)-choose(2*q,q+h-2*j-1))
                    for j in range(h+1))
            assert lhs==rhs,(r,h,lhs,rhs)
            exact_conv_checks+=1
    for K in range(1,9):
        for r in (16*K*K,16*K*K+1,20*K*K,32*K*K,64*K*K):
            for h in range(K+1):
                measured=abs(c(r,h)-Fraction(1,factorial(h)))
                bound=Fraction(32*K**3,r*factorial(h))
                assert measured<=bound,(K,r,h,measured,bound)
                coeff_checks+=1

    results=[]
    total_minors=0
    cases=[(3,8),(3,12),(4,8),(4,16),(5,8),(5,16),
           (5,32),(5,64),(6,16),(6,32)]
    for K,r in cases:
        bad=[]
        zeros=[]
        positive=0
        tested=0
        for k in range(1,K+2):
            idx=list(combinations(range(K+1),k))
            for u in idx:
                for v in idx:
                    if any(vj<ui for ui,vj in zip(u,v)):continue
                    d=det_integer([[B(r,vj-ui) for vj in v] for ui in u])
                    tested+=1
                    if d<0:
                        if len(bad)<10:bad.append(
                            {'size':k,'u':list(u),'v':list(v),'value':str(d)})
                    elif d==0:
                        if len(zeros)<10:zeros.append(
                            {'size':k,'u':list(u),'v':list(v)})
                    else:positive+=1
        total_minors+=tested
        results.append({
            'K':K,'r':r,'tested_structural_minors':tested,
            'strict_positive_count':positive,'negative_examples':bad,
            'zero_examples':zeros,'all_structural_positive':tested==positive
        })
    evidence={
        'research_id':'R429',
        'model':'original signed BRC auxiliary coefficients, not native X6',
        'exact_signed_branch_crosschecks':exact_conv_checks,
        'quantitative_coefficient_bound_checks':coeff_checks,
        'theoretical_R':{str(k):str(R(k)) for k in range(1,7)},
        'complete_finite_window_checks':results,
        'total_determinants_computed':total_minors,
        'proof_scope':'Analytic R(K) proof separate; tests only finite, exact Python integers and Fraction.'
    }
    with open(OUT/'r429_evidence.json','w',encoding='utf-8') as f:
        dump(evidence,f,ensure_ascii=False,indent=2)
    print('R429_EXACT_PASS',exact_conv_checks,coeff_checks,total_minors)
    for row in results:
        print(row['K'],row['r'],row['tested_structural_minors'],
              row['strict_positive_count'],row['all_structural_positive'])
    print('R_K',{k:R(k) for k in range(1,4)})

if __name__=='__main__':
    main()
