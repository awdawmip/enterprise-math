#!/usr/bin/env python3
"""Finite p-field Clausen polynomial, sextic-sum and involution checks.
Author-side only: no Source CLAIM, no H0/B0 execution and no admission."""
from math import comb
import json

def primes(n):
    return [p for p in range(7,n) if all(p%d for d in range(2,int(p**.5)+1))]

def case(p):
    assert p%6==1 and p>=7
    r=(p-1)//6; h=pow(2,-1,p); c=[1]
    for k in range(2*r):
        j=k+1
        c.append(c[-1]*(3*k+1)*(3*k+2)*(2*k+1)*pow(36,-1,p)*pow(j,-3,p)%p)
    a=[comb(r,k)*comb(2*r,k)*pow(h,k,p)%p for k in range(r+1)]
    sq=[0]*(2*r+1)
    for i,ai in enumerate(a):
        for j,aj in enumerate(a):
            sq[i+j]=(sq[i+j]+ai*aj)%p
    assert sq==c
    A=sum(a)%p; C=sum(c)%p
    dC=sum(k*ck for k,ck in enumerate(c))%p
    dA=sum(k*ak for k,ak in enumerate(a))%p
    assert C==A*A%p and dC==2*A*dA%p
    R={x: (x+1)**2*(2*x+1)*pow(x,-1,p)%p for x in range(1,p)}
    S=sum(pow(v,r,p) for v in R.values())%p
    assert A==(-pow(h,r,p)*S)%p
    D={x for x in range(p) if x not in (0,p-1,p-h)}
    inv_sum=0
    for x in D:
        y=-(2*x+1)*pow(2*(x+1),-1,p)%p
        assert y in D
        assert -(2*y+1)*pow(2*(y+1),-1,p)%p==x
        assert R[x]*R[y]%p==h
        inv_sum=(inv_sum+pow(R[x],-r,p))%p
    assert S==pow(h,r,p)*inv_sum%p
    return dict(p=p,r=r,A=A,C=C,C_prime=dC,sextic_sum=S)

def main():
    ps=[p for p in primes(400) if p%6==1]+[997,1213]
    out=[case(p) for p in ps]
    target=[o for o in out if o['p']%24 in (13,19)]
    assert all(o['A']==0 and o['C_prime']==0 for o in target)
    print(json.dumps({
      'status':'PASS','author_only':True,'prime_count':len(out),
      'target_prime_count':len(target),'tested_primes':ps,
      'target_zero_is_finite_observation':True,
      'selected_cases':[o for o in out if o['p'] in (7,13,19,373,997,1213)],
      'native_H0_B0':'NOT_EXECUTED','source_checkpoint':'NOT_PUBLISHED',
      'admission':'NOT_ADMITTED'
    },indent=2))
if __name__=='__main__':main()
