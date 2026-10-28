#!/usr/bin/env python3
"""Exact D25 prime-horizon weighted p^3 support check, author-only."""
import json
from math import isqrt

def vf(n,p):
    v=0
    while n:
        n//=p
        v+=n
    return v

def vu(j,p): return vf(2*j,p)-2*vf(j,p)
def vc(k,p): return vf(3*k,p)+vf(2*k,p)-5*vf(k,p)

def alive(j,k,p):
    K=(2*p+2)//3
    if k>=K: return False
    if p%6==1:
        r=(p-1)//6
        if 3*r+1<=k<=4*r and j==4*r+1-k: return False
    return True

def coefficients(p):
    q=p**3
    u=[1];c=[1]
    for k in range(p-1):
        inv=pow(k+1,-1,q)
        c.append(c[-1]*(3*k+1)*(3*k+2)*(2*k+1)*pow(36,-1,q)*pow(inv,3,q)%q)
        u.append(u[-1]*(2*k+1)*pow(4,-1,q)*inv%q)
    return u,c

def check(p):
    assert p>=5 and all(p%d for d in range(2,isqrt(p)+1))
    r=(p-1)//6 if p%6==1 else (p+1)//6
    K=(2*p+2)//3
    expected=(16*r*r+7*r+1) if p%6==1 else (16*r*r-2*r)
    n=0; baseline=0; n_oracle=0
    for k in range(p):
        ck=vc(k,p)
        for j in range(p-k):
            w=3*(j+k)-1
            x=vu(j,p)+ck
            baseline+=(x<3)
            if w%p==0:
                assert w in (p,2*p)
                x+=1
            assert (x<3)==alive(j,k,p),(p,j,k,x)
            n+=alive(j,k,p);n_oracle+=1
    assert n==expected
    assert baseline==K*p-K*(K-1)//2
    assert baseline-n==(r if p%6==1 else 0)
    u,c=coefficients(p)
    q=p**3;full=sparse=0
    for k in range(p):
        for j in range(p-k):
            term=(3*(j+k)-1)*u[j]*c[k]%q
            full=(full+term)%q
            if alive(j,k,p): sparse=(sparse+term)%q
            else: assert term==0,(p,j,k)
    assert full==sparse
    return dict(p=p,total=p*(p+1)//2,c_only=baseline,weighted=n,
                extra_weight_only=baseline-n,S_mod_p3=full,oracle_pairs=n_oracle)

def main():
    ps=(5,7,11,13,17,19,23,31,37,43,73,211,373,997)
    v=[check(p) for p in ps]
    assert sum(x["oracle_pairs"] for x in v)==595285
    assert next(x for x in v if x["p"]==19)["weighted"]==166
    assert next(x for x in v if x["p"]==373)["weighted"]==61939
    print(json.dumps({"status":"PASS","level":"AUTHOR_EXACT_CHECK_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE",
        "statement":"Exact signed termwise p^3 support for S_p and p mod 6 counts",
        "oracle_pairs":sum(x["oracle_pairs"] for x in v),"cases":v},indent=2))

if __name__=="__main__": main()
