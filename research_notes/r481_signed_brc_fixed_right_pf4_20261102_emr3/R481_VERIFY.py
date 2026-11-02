#!/usr/bin/env python3
"""R481: exact right-edge signed-BRC PF4 asymptotic sign checks.
Scientific input: frozen R462; analytic comparison with R479.
Python standard library only. Integers/Fraction, no floating point.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import permutations
import json

PERM4 = [(p, (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))
         for p in permutations(range(4))]

def cat(n):
    if n < 0: return 0
    return comb(2*n,n)//(n+1)

def h_catalan(k,s):
    r=2*k+1
    if s<2 or s>r:return 0
    return comb(r+s,2*s)*sum(comb(s-1,2*q)*4**q*cat(k-q)
                               for q in range((s-1)//2+1))

def h_original(k,s):
    r=2*k+1
    if s<2 or s>r:return 0
    # exact coefficient [t^r] (1-t)(1+t)^(2s)(1+t^2)^(r-s)
    return comb(r+s,2*s)*sum(comb(r-s,u)*(
        (comb(2*s,r-2*u) if 0<=r-2*u<=2*s else 0)-
        (comb(2*s,r-2*u-1) if 0<=r-2*u-1<=2*s else 0))
        for u in range(r-s+1))

def determinant4(M):
    val=0
    for p,sign in PERM4:
        prod=1
        for i in range(4):prod*=M[i][p[i]]
        val+=sign*prod
    return val

def d4_exact(k,s):
    return determinant4([[h_catalan(k,s+i-j) for j in range(4)] for i in range(4)])

def A(s):
    return Fraction(2**(s-2),factorial(2*s)) if s>=2 else Fraction(0)

def c(s):
    return Fraction(2**s,factorial(2*s)) if s>=0 else Fraction(0)

def limit_m4(s):
    return determinant4([[A(s+i-j) for j in range(4)] for i in range(4)])

if __name__=='__main__':
    # Independent original-coefficient check for all valid small inputs.
    comparisons=0
    for k in range(2,22):
        for s in range(2,min(2*k+1,15)+1):
            x,y=h_catalan(k,s),h_original(k,s)
            assert x==y,(k,s,x,y)
            comparisons+=1
    limits={s:limit_m4(s) for s in range(2,31)}
    assert limits[2]==Fraction(1,331776)
    assert limits[3]==Fraction(-31,144850083840000)
    assert limits[4]==Fraction(50137,32884851013926912000000)
    # For s>=5 all matrix indices>=2; A=c/4 and standard Toeplitz strict PF-infinity.
    for s in range(5,31):
        assert limits[s]==determinant4([[c(s+i-j) for j in range(4)] for i in range(4)])/4**4
        assert limits[s]>0
    signs={}; n=0; exceptions=[]
    for k in range(4,101):
        for s in range(2,min(2*k+1,12)+1):
            actual=d4_exact(k,s)
            expected=1 if s!=3 else (-1 if k>=49 else 1)
            signs[(k,s)] = 1 if actual>0 else (-1 if actual<0 else 0)
            if signs[(k,s)]!=expected: exceptions.append([k,s,signs[(k,s)],expected])
            n+=1
    summary={
        'status':'R481_EXACT_PASS' if not exceptions else 'R481_FINITE_EXCEPTIONS',
        'scientific_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'original_vs_catalan_exact_checks': comparisons,
        'exact_fourth_order_determinant_checks':n,
        's2_constant':str(limits[2]),'s3_constant':str(limits[3]),'s4_constant':str(limits[4]),
        'fixed_s_limit_signs_2_to_30':{str(s):'+' if limits[s]>0 else '-' for s in limits},
        'finite_sign_exceptions':exceptions,
        'finite_check_window': {'k': [4,100],'s':[2,12],'condition':'s<=2k+1'},
        'mathematical_scope':'Exact limiting constants via Catalan ratios; strict positivity for s>=5 by cosh-product and Schur Jacobi-Trudi proof. Finite checks are only independent validation.'
    }
    with open('/mnt/data/r481_evidence.json','w') as f:json.dump(summary,f,indent=2,ensure_ascii=False)
    print(json.dumps(summary,indent=2,ensure_ascii=False))
