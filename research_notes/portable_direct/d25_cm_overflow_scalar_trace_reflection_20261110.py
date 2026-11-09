#!/usr/bin/env python3
"""Exact p² one-scalar CM overflow and carry-preserving reflected trace."""
from math import comb
import json

def add(a,b,m): return ((a[0]+b[0])%m,(a[1]+b[1])%m)
def mul(a,b,m): return ((a[0]*b[0]+2*a[1]*b[1])%m,(a[0]*b[1]+a[1]*b[0])%m)
def power(a,n,m):
    out=(1,0)
    while n:
        if n&1: out=mul(out,a,m)
        a=mul(a,a,m);n>>=1
    return out
def horner(coeff,x,m):
    out=(0,0)
    for c in reversed(coeff): out=add(mul(out,x,m),(c,0),m)
    return out
def run(p):
    assert p>3 and p%24==13
    m=p*p
    f,g=[1],[1]
    for k in range(1,p):
        f.append(f[-1]*(8*k-7)*(8*k-5)*pow(64*k*k,-1,m)%m)
        g.append(g[-1]*(4*k-3)*(4*k-1)*pow(16*k*k,-1,m)%m)
    s=(3*pow(6,-1,m)%m,-2*pow(6,-1,m)%m)
    F=sum(f[k]*pow(pow(9,-1,m),k,m) for k in range(p))%m
    G=horner(g,s,m)
    edge=[0]*(p-1)
    for k in range((p+1)//2,p):
        c=f[k]*pow(4,k,m)%m
        for j in range(p-k,k+1):
            edge[k+j-p]=(edge[k+j-p]+c*(-1 if j&1 else 1)*comb(k,j))%m
    E=horner(edge,s,m)
    assert add(G,mul(power(s,p,m),E,m),m)==(F,0)
    assert G[0]==0 and G[1]%p==0 and E[0]%p==E[1]%p==0
    gd,u,v=G[1]//p,E[0]//p,E[1]//p
    tr=[2,1]
    inv36=pow(36,-1,m)
    for r in range(2,p+1):
        tr.append((tr[-1]-inv36*tr[-2])%m)
    scalar=sum(edge[r]*tr[r] for r in range(p-1))%m
    assert scalar==(2*E[0])%m and scalar%p==0
    assert ((scalar//p)*pow(2,-1,p)-u)%p==0
    sigma=(s[0],-s[1]%m)
    sp=power(s,p,m)
    assert all((sp[i]-sigma[i])%p==0 for i in range(2))
    zeta=tuple(((sp[i]-sigma[i])%m)//p for i in range(2))
    paired=(2*edge[0]+edge[1])%m
    for r in range(2,(p+1)//2):
        zsig=mul(zeta,power(sigma,r,p),p)
        tcarry=(2*zsig[0])%p
        reflected=pow(36,r,m)*(tr[r+1]+p*tcarry)%m
        assert reflected==tr[p-r]
        paired+=(edge[r]*tr[r]+edge[p-r]*reflected)
    assert paired%m==scalar
    assert (2*u+3*v+6*gd)%p==0
    assert F%p==0 and (18*(F//p)-u+24*gd)%p==0
    return dict(p=p,g=gd,u=u,v=v,S=scalar,F=F,odd_constraint=0,
                proposed_residual=(u-24*gd)%p)
if __name__=="__main__":
    print(json.dumps([run(p) for p in (13,37,61,109,157,181,373,397,421,541)],indent=2))
