#!/usr/bin/env python3
"""Independent original-216 / Gauss / signed-prefix Green integer check."""
from math import comb
def targets(limit):
    def prime(n):
        return n>1 and all(n%d for d in range(2,int(n**.5)+1))
    return [p for p in range(13,limit+1) if p%24 in (13,19) and prime(p)]
def check(p):
    r=(p-1)//6; m=p**3; a=[1]; c=[1]
    for k in range(p-1):
        n=k+1
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*n**3,-1,m)%m)
        c.append(c[-1]*(6*k+1)*(3*k+1)*pow(18*n**2,-1,m)%m)
    z=1; inv2=pow(2,-1,m); G=D=W=0
    for k in range(p):
        G=(G+c[k]*z)%m; D=(D+k*c[k]*z)%m
        W=(W+(6*k+1)*a[k]*z)%m; z=z*inv2%m
    diff=(W-G*G-12*G*D)%m
    assert diff%(p*p)==0
    E=diff//(p*p)
    ell=[comb(r,t)*comb(2*r,t)%p for t in range(r+1)]
    assert [x%p for x in c[:r+1]]==ell
    K=[0]*(r+1)
    for t in range(r,0,-1):
        q=(2*t-1)*(3*t-2)*(3*t-1)*pow(18,-1,p)%p
        K[t-1]=(t**3*K[t]-t*ell[t]*pow(3,-1,p))*pow(q,-1,p)%p
    tail=0; K2=[0]*(r+1); h=[0]*(r+1)
    for j in range(1,r+1):
        h[j]=ell[j]*pow(j*j*a[j],-1,p)%p
    for t in range(r-1,-1,-1):
        tail=(tail+h[t+1])%p
        K2[t]=-a[t]*tail*pow(3,-1,p)%p
    assert K==K2
    v=pow(2,-1,p); pref=0; E2=0
    for j in range(1,r+1):
        t=j-1
        pref=(pref+(6*t+1)*a[t]*pow(v,t,p))%p
        E2=(E2-h[j]*pref*pow(6,-1,p))%p
    EK=sum((6*t+1)*pow(v,t,p)*K[t] for t in range(r))*v%p
    assert E==E2==EK, (p,E,E2,EK)
    if p in (13,19,37,373):
        for t in range(r):
            n=p+t; v0=sum(c[i]*c[n-i] for i in range(n-p+1,p) if 0<=n-i<p)%m
            assert v0%(p*p)==0 and K[t]==-(v0//(p*p))%p
    A=(G//p)%(p*p); first=(12*A*(D%(p*p)))%(p*p)
    assert first%p==1
    carry=(first-1)//p
    balance=(carry+A*A+E2)%p
    assert balance==((W-p)%(p**3))//(p*p)
    return (p,r,K[0],E,carry,A*A%p,balance)
if __name__=="__main__":
    rows=[check(p) for p in targets(2000)]
    assert len(rows)==77
    print("PASS",len(rows),"target primes; full high coefficient crosschecks 13,19,37,373")
    for row in rows:
        if row[0] in (13,19,37,373): print(row)
