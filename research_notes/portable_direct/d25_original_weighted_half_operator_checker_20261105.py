#!/usr/bin/env python3
"""Exact original 216 weighted cutoff operator and reflected shell.
Checks original binomial input, polynomial coefficient identity mod p^3,
nonzero p^2 terminal, and independent 4F3 boundary for 80 primes.
"""
from math import comb, isqrt, factorial
import json

def primes(limit):
    return [p for p in range(7,limit+1)
            if p%6==1 and all(p%d for d in range(2,isqrt(p)+1))]

def certificate(p):
    N=(p-1)//2
    m=p**3
    inv18=pow(18,-1,m)
    aval=[]
    for k in range(N+2):
        aval.append(comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)%m)
    poly=[(6*k+1)*aval[k]*pow(2,k,m)%m for k in range(N+1)]
    for k in range(N+1):
        leading=(6*k-5)*k**3*poly[k]
        trailing=0
        if k>0:
            j=k-1
            f=(2*j+1)*(3*j+1)*(3*j+2)*inv18%m
            trailing=(6*k+1)*f*poly[j]
        assert (leading-trailing)%m==0, (p,k,(leading-trailing)%m)
    j=N
    f=(2*j+1)*(3*j+1)*(3*j+2)*inv18%m
    terminal=(-(6*(N+1)+1)*f*poly[j])%m
    source_at_half=terminal*pow(2,-(N+1),m)%m
    first_omitted=aval[N+1]
    ratio=(-(6*N+7)*(6*N+1)*(N+1)**3)%m
    assert ratio%p==1
    assert terminal == (ratio*first_omitted*pow(2,N+1,m))%m
    assert source_at_half==first_omitted
    assert terminal%(p*p)==0 and terminal!=0

    n=(p-1)//6
    C=pow(216,2*n,p)*pow(factorial(2*n),5,p)*pow(factorial(4*n+1),-1,p)%p
    h=1
    for r in range(n-1):
        h=h*(2*(3*r+2)**3)*pow(3*(6*r+7)*(3*r+4)*(r+1),-1,p)%p
    U=C*h*pow(2,n-1,p)%p
    assert U!=0
    assert (U+first_omitted//(p*p))%p==0, ('first-omitted source mismatch',p)
    assert U==(2*n*n*(aval[N]//p))%p, ('next-term ratio mismatch',p)

    g=1
    obs=0
    for r in range(n):
        obs=(obs+(3*r+2)*g*pow(2,-r,p))%p
        if r<n-1:
            g=g*2*(r+1)*(6*r+5)*(6*r+7)*pow((2*r+3)**3*9,-1,p)%p
    T_reversed=(-2*U*obs)%p
    full_shell=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,m)
                   for k in range(N+1,p))%m
    assert full_shell%(p*p)==0
    assert (full_shell//(p*p))%p==T_reversed, ('upper shell mismatch',p)
    return {'p':p,'N':N,'terminal_t_power_coeff':terminal,
            'terminal_eval_at_half':source_at_half,
            'original_first_omitted_a_Nplus1':first_omitted,
            'normalized_source_mod_p':(source_at_half//(p*p))%p,
            'residual_factor_mod_p':ratio%p,
            'U_reflected_mod_p':U,
            'T_A_original_and_reflected_mod_p':T_reversed}

if __name__=='__main__':
    records=[certificate(p) for p in primes(997)]
    assert len(records)==80
    anchors=[r for r in records if r['p'] in (7,13,19,139,373)]
    out={'schema':'D25_ORIGINAL_WEIGHTED_216_TRUNCATION_OPERATOR_V1',
         'checked_primes':len(records),'domain':'p=1 mod6 primes 7<=p<=997',
         'failures':0,'examples':anchors,
         'status':'finite exact original coefficient checks; theorem algebraic; native H0/B0 not run'}
    with open('d25_original_weighted_half_operator_results_20261105.json','w') as f:
        json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
