#!/usr/bin/env python3
"""Original Gauss three-strip and signed original-216 second-carry exact checker."""
import json
from math import comb, factorial

def primes_upto(n):
    s=[True]*(n+1);s[0]=s[1]=False
    for d in range(2,int(n**0.5)+1):
        if s[d]:
            for v in range(d*d,n+1,d):s[v]=False
    return [p for p in range(7,n+1) if s[p] and p%6==1]

def expansion(p,k):
    """Returns the three coefficients in c_k=c0+p*c1+p*p*c2 modulo p**3."""
    r=(p-1)//6;m=p**3
    zeros=0;prod=1;T=T2=0
    for root,denom in [(r,6),(2*r,3)]:
        for i in range(k):
            x=i-root
            if x==0:zeros+=1
            else:
                prod=prod*x%m
                u=pow(denom*x,-1,m)
                T=(T+u)%m
                T2=(T2+u*u)%m
    assert zeros==int(k>r)+int(k>2*r)
    prod=prod*pow(factorial(k),-2,m)%m
    if zeros==0:return prod,prod*T%m,prod*(T*T-T2)*pow(2,-1,m)%m
    if zeros==1:return 0,prod*pow(6,-1,m)%m,prod*T*pow(6,-1,m)%m
    return 0,0,prod*pow(18,-1,m)%m

def far_hypergeom(p):
    r=(p-1)//6
    e0=(-1)**r*factorial(r)**2*pow(18*(2*r+1)**2*factorial(2*r),-1,p)%p
    v=e0; z=pow(2,-(2*r+1),p); total=0
    for s in range(4*r):
        total=(total+v*z)%p
        if s<4*r-1:
            v=v*(6*s+5)*(3*s+3)*pow(2*(3*s+5)**2,-1,p)%p
            z=z*pow(2,-1,p)%p
    return total

def weighted_original(p):
    m=p**3;inv2=pow(2,-1,m);a=z=1;W=0
    for k in range(p):
        W=(W+(6*k+1)*a*z)%m
        if k<p-1:a=a*(2*k+1)*(3*k+1)*(3*k+2)*pow(18*(k+1)**3,-1,m)%m
        z=z*inv2%m
    return W

def check(p):
    m=p**3;r=(p-1)//6;inv2=pow(2,-1,m)
    c=[1]
    for k in range(p-1):
        c.append(c[-1]*(6*k+1)*(3*k+1)*pow(18*(k+1)**2,-1,m)%m)
    G=D=G0=D0=H=0;z=1
    for k in range(p):
        a,b,d=expansion(p,k);v=(a+p*b+p*p*d)%m
        assert v==c[k],(p,k,v,c[k])
        G=(G+v*z)%m;D=(D+k*v*z)%m
        if k<=2*r:G0=(G0+v*z)%m;D0=(D0+k*v*z)%m
        if k>2*r:H=(H+d*z)%p
        z=z*inv2%m
    assert H==far_hypergeom(p),(p,H,far_hypergeom(p))
    if p%24 not in (13,19):return {'p':p,'far':H}
    assert G%p==0
    A=G//p
    full=(12*A*(D%(p*p)))%(p*p)
    assert full%p==1
    assert G0%p==0
    low=(12*(G0//p)*(D0%(p*p)))%(p*p)
    assert low%p==1
    first=(full-1)//p
    lowcarry=(low-1)//p
    farcarry=12*(D0%p)*H%p
    assert (lowcarry+farcarry)%p==first%p
    W=weighted_original(p)
    diff=(W-G*G-12*G*D)%m
    assert diff%(p*p)==0
    E=diff//(p*p)
    square=A*A%p
    assert (first+square+E)%p==((W-p)%m)//(p*p)
    return {'p':p,'far':H,'lowmid_carry':lowcarry,'far_carry':farcarry,'first_carry':first,'square':square,'E':E,'W_mod_p3':W}

if __name__=='__main__':
    import sys
    limit=int(sys.argv[1]) if len(sys.argv)>1 else 1000
    ps=primes_upto(limit)
    rows=[check(p) for p in ps]
    target=[x for x in rows if x['p']%24 in (13,19)]
    print(json.dumps({'limit':limit,'p_1mod6':len(ps),'target_count':len(target),
        'checked_coefficient_positions':sum(ps),
        'samples':[x for x in rows if x['p'] in (7,13,19,37,43,373)]},indent=2))
