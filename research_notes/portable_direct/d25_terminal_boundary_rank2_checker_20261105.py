#!/usr/bin/env python3
"""Exact D25 two-prefix scalar boundary audit. Native H0/B0 NOT_RUN."""
import argparse, json

def primes(n):
    s=bytearray(b'\x01')*(n+1); s[:2]=b'\x00\x00'
    for d in range(2,int(n**.5)+1):
        if s[d]: s[d*d::d]=b'\x00'*((n-d*d)//d+1)
    return [p for p in range(7,n+1) if s[p] and p%6==1]

def check(p,double=False):
    n=(p-1)//6; m=p**3; inv36=pow(36,-1,m)
    b=1;g=h=1;R=1;power2=1;A=J=total=0
    low=[1] if double else None
    for i in range(1,p):
        b=b*(6*i-5)*(3*i-2)*inv36*pow(i*i,-1,m)%m
        g=(g+b)%m;h=(h+(12*i+1)*b)%m
        if i<=n:
            if i>1:
                r=i-1
                R=R*18*r*r*pow((6*r+5)*(3*r+2),-1,p)%p
            power2=power2*2%p;t=power2*R%p
            A=(A+t)%p;J=(J+i*t)%p
            total=(total+(b%p)*((6*i+1)*A-6*J))%p
            if double:low.append(b%p)
    assert b%(p*p)==0
    C=(b//(p*p))%p
    assert C!=0
    T=C*total%p
    W=original=1
    for k in range(1,p):
        original=original*(2*k-1)*(3*k-2)*(3*k-1)*inv36*pow(k**3,-1,m)%m
        W=(W+(6*k+1)*original)%m
    boundary=(g*h-W)%m
    assert boundary%(p*p)==0 and (boundary//(p*p))%p==T
    if double:
        R=1;rs=[0,1]
        for r in range(2,n+1):
            j=r-1;R=R*18*j*j*pow((6*j+5)*(3*j+2),-1,p)%p;rs.append(R)
        d=0
        for i in range(1,n+1):
            for r in range(1,i+1):
                d=(d+2*C*(6*(i-r)+1)*low[i]*pow(2,r-1,p)*rs[r])%p
        assert d==T
    target=p%24 in (13,19);delta=None
    if target:
        assert g%p==0 and (g*h-p)%(p*p)==0
        delta=((g*h-p)//(p*p))%p
        assert (delta-T)%p==((W-p)//(p*p))%p
    return {"p":p,"n":n,"C_p":C,"T_p":T,"delta":delta,"W_mod_p3":W,"double_checked":double}

if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--limit",type=int,default=10000);a.add_argument("--double-limit",type=int,default=250)
    args=a.parse_args();rows=[check(p,p<=args.double_limit) for p in primes(args.limit)]
    targets=[x for x in rows if x["delta"] is not None]
    out={"prime_count":len(rows),"double_checked":sum(x["double_checked"] for x in rows),
         "target_count":len(targets),"target_delta_equals_T":sum(x["delta"]==x["T_p"] for x in targets),
         "all_p_W_equals_p":sum(x["W_mod_p3"]==x["p"] for x in rows),
         "all_prime_claim":False,"native_H0_B0":"NOT_RUN","rows":rows}
    print(json.dumps({k:v for k,v in out.items() if k!="rows"},indent=2))
