#!/usr/bin/env python3
"""Author-side finite p-adic check for D25 endpoint moment law. Standard library only."""
from math import comb
from fractions import Fraction
import json

def primes(n):
    return [p for p in range(7,n+1) if all(p%d for d in range(2,__import__('math').isqrt(p)+1))]

def check(p):
    assert p%6==1
    m=(p-1)//6; mod=p**6
    b=[0]*(p+1); b[0]=1
    for n in range(1,p):
        b[n]=(b[n-1]*6*(6*n-5)*(3*n-2)*pow(n*n,-1,mod))%mod
    assert b[p-1]%(p*p)==0
    bp=((b[p-1]//(p*p))*6*(6*p-5)*(3*p-2))%p**4
    gamma=[comb(2*k,k)**2*comb(3*k,k)%p**4 for k in range(p+1)]
    t=[gamma[k]*b[p-k]%p**4 for k in range(1,p)]
    low=range(1,2*m+1)
    mid=range(2*m+1,3*m+1)
    upper=range(5*m+1,6*m+1)
    assert all(t[k-1]%p**2==0 for k in low)
    assert all(t[k-1]%p**3==0 for k in list(mid)+list(upper))
    assert all(t[k-1]%p**4==0 for k in range(3*m+1,5*m+1))
    assert (2*p*(gamma[p]-2*bp)+sum((6*k-4*p)*t[k-1] for k in range(1,p)))%p**4==0
    assert (gamma[p]-2*bp)%p==0
    lo=[(k,t[k-1]//p**2) for k in low]
    mu=[(k,t[k-1]//p**3) for k in list(mid)+list(upper)]
    q=((gamma[p]-2*bp)%p**3)//p%p**2
    first=(-3*sum(k*a for k,a in lo))%p**2
    low2=(2*sum(a for k,a in lo))%p
    middle=(-3*sum(k*t[k-1]//p**3 for k in mid))%p
    high=(-3*sum(k*t[k-1]//p**3 for k in upper))%p
    correction=(low2+middle+high)%p
    assert q==(first+p*correction)%p**2
    assert gamma[p]%p**3==12
    pred=(6-(p*first+p*p*correction)*pow(2,-1,p**3))%p**3
    assert bp%p**3==pred,(p,bp%p**3,pred)
    return {'p':p,'endpoint_quotient_mod_p2':q,'low':first,'low_secondary':low2,
            'middle':middle,'upper':high,'correction_mod_p':correction,
            'b_p_mod_p3':bp%p**3}

def exact_check(p):
    b=[Fraction(1)]
    for n in range(1,p+1):
        b.append(b[-1]*Fraction(6*(6*n-5)*(3*n-2),n*n))
    g=[comb(2*k,k)**2*comb(3*k,k) for k in range(p+1)]
    assert sum((6*k-4*p)*g[k]*b[p-k] for k in range(p+1))==0

if __name__=='__main__':
    vals=[check(p) for p in primes(997) if p%6==1]
    assert len(vals)==80
    for p in (7,13,19,31): exact_check(p)
    samples=[r for r in vals if r['p'] in (13,19,67,373)]
    print(json.dumps({'n_primes':len(vals),'exact_fraction_cases':[7,13,19,31],
                      'all_pass':True,'samples':samples},indent=2))
