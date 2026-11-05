#!/usr/bin/env python3
"""D25 Clausen p^3 original 216 weighted convolution: standard-library exact checks."""
import json
from math import comb, isqrt

def primes(limit):
    f=[True]*(limit+1); f[0]=f[1]=False
    for j in range(2,isqrt(limit)+1):
        if f[j]:
            f[j*j::j]=[False]*((limit-j*j)//j+1)
    return [p for p in range(7,limit+1) if f[p] and p%6==1]

def check(p, full=False):
    n=(p-1)//6; mod=p**3
    q=[1]
    for k in range(1,p):
        q.append(q[-1]*(6*k-5)*(3*k-2)*pow(18*k*k,-1,mod)%mod)
    z=pow(2,-1,mod)
    zp=[1]
    for k in range(1,2*p):
        zp.append(zp[-1]*z%mod)
    Q=sum(q[k]*zp[k] for k in range(p))%mod
    dQ=sum(k*q[k]*zp[k] for k in range(p))%mod
    # Independent original binomial expression, not using Clausen.
    W=sum((6*k+1)*comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)
          for k in range(p))%mod
    B=sum(2*(6*(p+i-r)+1)*q[i]*q[p-r]*zp[p+i-r]
          for i in range(1,n+1) for r in range(1,i+1))%mod
    assert B%(p*p)==0 and (Q*(Q+12*dQ)-B-W)%mod==0
    assert all(q[k]%p==0 for k in range(n+1,p))
    assert all(q[k]%(p*p)==0 for k in range(2*n+1,p))
    assert all(q[k]%(p*p)!=0 for k in range(n+1,2*n+1))
    assert all(q[k]%mod!=0 for k in range(2*n+1,p))
    C=q[p-1]//(p*p); R=1; reduced=0
    for r in range(1,n+1):
        assert q[p-r]//(p*p)%p == C*R%p
        for i in range(r,n+1):
            reduced+=2*C*(6*(i-r)+1)*comb(n,i)*comb(2*n,i)*R*pow(2,-(1+i-r),p)
        reduced%=p
        R=R*(18*r*r)%p*pow((6*r+5)*(3*r+2),-1,p)%p
    assert B//(p*p)%p==reduced
    if full:
        for k in range(p):
            coeff=sum(q[i]*q[k-i] for i in range(k+1))%mod
            orig=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
            assert coeff*zp[k]%mod==orig,(p,k)
    return {'p':p,'Q_mod_p3':Q,'thetaQ_mod_p3':dQ,
            'boundary_over_p2_mod_p':reduced,'W_mod_p3':W}

if __name__=='__main__':
    rows=[check(p,p in (7,13,19,139,373)) for p in primes(997)]
    print(json.dumps({'count':len(rows),'failures':0,
      'anchors':[row for row in rows if row['p'] in (7,13,19,139,373)],
      'status':'AUTHOR_ONLY; NOT_NATIVE_H0B0; UNREVIEWED'},indent=2))
