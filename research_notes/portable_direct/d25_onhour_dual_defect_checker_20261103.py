#!/usr/bin/env python3
"""Exact modular check for middle/high dual-transfer defect (no floating point)."""
import json
from math import comb

def primes(n):
    out=[]
    for k in range(7,n+1):
        if k%6!=1: continue
        if all(k%d for d in range(2,int(k**.5)+1)): out.append(k)
    return out

def inv(x,m):
    return pow(x%m,-1,m)

def study(p,original=False):
    r=(p-1)//6;n=3*r;pm=p*p
    A=1 # middle from exact R_(n-t)^-1, MOD p²
    f=1 # high hypergeometric A_s 2^-s, modulo p²
    E=0
    value=[]; defect=[]
    signed_middle=0;signed_high=0
    for s in range(r):
        J=((2*s+1)**3*A*f)%pm
        assert J == (1+p*E)%pm, ('dual',p,s,J,(1+p*E)%pm)
        # Repair the determinant at mod p^2 by retaining the cumulative defect.
        V=((2*s+1)**3*f*(1-p*E))%pm
        assert A*V%pm==1, ('repaired-invariant',p,s)
        if s:
            Rprev=(p-2*s)*((3*p-6*s)**2-1)*inv(18*(p-2*s+1)**3,pm)%pm
            prevV=((2*(s-1)+1)**3*value[-1][2]*(1-p*value[-1][3]))%pm
            assert V==prevV*Rprev%pm,('repaired-transport',p,s)
        high_from_middle = (inv(((2*s+1)**3*A)%p,p))%p
        assert (f%p)==high_from_middle,(p,s,'reciprocal')
        signed_middle=(signed_middle + (3*p-2-6*s)*A)%pm
        signed_high=(signed_high+(6*s+4)*f)%p
        value.append((s,A,f,E,J))
        if s==r-1:break
        t=s+1
        # R_(n-t) = (p-2t)((3p-6t)^2-1)/(18(p-2t+1)^3)
        R=(p-2*t)*((3*p-6*t)**2-1)*inv(18*(p-2*t+1)**3,pm)%pm
        A=A*inv(R,pm)%pm
        # f_t/f_(t-1) = t(36t^2-1)/(9(2t+1)^3)
        f=f*t*(36*t*t-1)*inv(9*(2*t+1)**3,pm)%pm
        e=(inv(2*t,p)+3*inv(6*t-1,p)+3*inv(6*t+1,p)-3*inv(2*t-1,p))%p
        E=(E+e)%p
        defect.append(e)
    if original:
        # b_(n-s)/p exact from original integer binomials.
        b_n=(comb(2*n,n)**2*comb(3*n,n)) * inv(216**n, p**3) % (p**3)
        assert b_n%p==0
        L=b_n//p
        for s,A,_,_,_ in value:
            j=n-s
            b=(comb(2*j,j)**2*comb(3*j,j))*inv(216**j,p**3)%(p**3)
            assert b%p==0 and b//p == L*A%pm,(p,s,'original')
        bH=(comb(2*(n+1),n+1)**2*comb(3*(n+1),n+1))*inv(216**(n+1),p**3)%(p**3)
        assert bH%pm==0
        chi=pow(6,(p-1)//2,p);chi= -1 if chi==p-1 else 1
        assert bH//pm == chi*inv(9,p)%p
        original_sum=sum((6*k+1)*(comb(2*k,k)**2*comb(3*k,k))*inv(216**k,p**3) for k in range(p))%(p**3)
        assert original_sum%pm==p%pm
    return dict(p=p,r=r,chi=(-1 if pow(6,(p-1)//2,p)==p-1 else 1),last_E=E,last_J=value[-1][-1],dual_pairs=len(value),middle_weight_sum_mod_p2=signed_middle,high_weight_sum_mod_p=signed_high,first_rows=value[:3],last_row=value[-1])

if __name__=='__main__':
    ps=primes(2000)
    records=[study(p, original=p in {7,13,19,37,43,373}) for p in ps]
    print('PASS',len(records),'primes',sum(r['dual_pairs'] for r in records),'exact reciprocal-pair steps')
    print(json.dumps([x for x in records if x['p'] in {7,13,19,37,43,373}],indent=2))
    with open('d25_onhour_dual_defect_results_20261103.json','w') as f:
        json.dump({'schema':'AUTHOR_SIDE_EXACT_COMPUTATION_V1','count_primes':len(records),'total_pairs':sum(r['dual_pairs'] for r in records),'claim':'J_s=(2s+1)^3 P_(n-s) f_s=1+p E_s (mod p²); high reciprocal modp','coverage':'all primes 7..2000, p=1 mod6; original binomial independent check p=7,13,19,37,43,373','examples':[x for x in records if x['p'] in {7,13,19,37,43,373}]},f,indent=2)
