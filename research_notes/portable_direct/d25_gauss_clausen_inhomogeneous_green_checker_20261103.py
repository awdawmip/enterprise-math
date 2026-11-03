"""Finite exact regression for D25 Gauss-Clausen inhomogeneous finite ODE.
Author-side arithmetic, NOT native H0/B0 or mathematical admission.
"""
from math import comb
import json

def primes(limit):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\x00\x00'
    for k in range(2,int(limit**.5)+1):
        if sieve[k]:
            sieve[k*k:limit+1:k]=bytes((limit-k*k)//k+1)
    return [p for p in range(7,limit+1) if sieve[p] and p%24 in (13,19)]

def verify(p,full=False):
    r=(p-1)//6; m=p**3; inv2=pow(2,-1,p)
    c=[1];ell=[1]
    for k in range(p-1):
        c.append(c[-1]*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,m)%m)
        if k<r:
            ell.append(ell[-1]*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,p)%p)
    assert ell==[comb(r,k)*comb(2*r,k)%p for k in range(r+1)]
    assert c[-1]%m==p*p*pow(10,-1,p)%m
    K=[0]*(r+1)
    for t in range(r,0,-1):
        Q=(2*t-1)*(3*t-2)*(3*t-1)*pow(18,-1,p)%p
        assert Q
        K[t-1]=(t**3*K[t]-t*pow(3,-1,p)*ell[t])*pow(Q,-1,p)%p
    for t in range(1,r+1):
        Q=(2*t-1)*(3*t-2)*(3*t-1)*pow(18,-1,p)%p
        assert (t**3*K[t]-Q*K[t-1]-t*pow(3,-1,p)*ell[t])%p==0
    E_ode=inv2*sum((1+6*t)*K[t]*pow(inv2,t,p) for t in range(r))%p
    B=1;W=0
    for k in range(p):
        W=(W+(6*k+1)*B)%m
        if k<p-1:
            B=B*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m)%m
    g=dg=ddg=0
    for k in range(p):
        zc=c[k]*pow(2,-k,m)%m
        g=(g+zc)%m;dg=(dg+2*k*zc)%m
        ddg=(ddg+4*k*(k-1)*zc)%m
    residue=(W-g*g-6*g*dg)%m
    assert residue%(p*p)==0
    E_original=residue//(p*p)%p
    assert E_ode==E_original
    ode=(ddg+dg-2*pow(9,-1,m)*g)%m
    assert ode==(-2*p*p*pow(9,-1,m))%m
    if full:
        for t in range(p-1):
            n=p+t
            coef=sum(c[i]*c[n-i] for i in range(max(0,n-p+1),p) if 0<=n-i<p)%m
            assert coef%(p*p)==0
            assert ((-coef%m)//(p*p))%p==(K[t] if t<r else 0)
        m4=p**4;last=1
        for k in range(p-1):
            last=last*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,m4)%m4
        assert last == -p**3%m4
        tail=(-(p-1+pow(2,-1,m4))*(p-1+pow(3,-1,m4))*
             (p-1+2*pow(3,-1,m4))*pow(2,-1,m4)*last)%m4
        assert tail==(-p**3*pow(18,-1,m4))%m4
    return {'p':p,'r':r,'K0':K[0],'K_last':K[r-1],
      'E_from_operator':E_ode,'E_from_original':E_original,
      'Gauss_ODE_residual_mod_p3':ode,'original_W_mod_p3':W}

def main():
    ps=primes(2000)
    rows=[verify(p,p in (13,19,37,373)) for p in ps]
    assert len(rows)==77
    result={'status':'PASS','domain':'77 primes <=2000 in residue classes 13,19 mod24',
      'full_high_convolution':[13,19,37,373],
      'samples':[row for row in rows if row['p'] in (13,19,37,373)]}
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
