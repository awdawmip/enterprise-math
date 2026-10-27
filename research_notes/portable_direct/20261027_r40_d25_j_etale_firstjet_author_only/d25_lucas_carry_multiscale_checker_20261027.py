#!/usr/bin/env python3
"""Exact binomial and valuation checks for D25 Lucas carry theorem; author-side, not native."""
import json
from math import comb

PRIMES=(5,7,11,13,19,31,37,43)
def digits(n,p):
    if n==0: return [0]
    out=[]
    while n:
        out.append(n%p)
        n//=p
    return out

def cmod(n,p,power=1):
    m=p**power
    return (comb(3*n,n)*pow(comb(2*n,n),2,m)*pow(216,-n,m))%m

def vp_fact(n,p):
    ans=0
    while n:
        n//=p
        ans+=n
    return ans

def valuation(n,p):
    return vp_fact(3*n,p)+vp_fact(2*n,p)-5*vp_fact(n,p)

def suffix(n,p):
    ans=0
    t=p
    while t<=3*n:
        r=n%t
        ans+=(3*r)//t+(2*r)//t
        t*=p
    return ans

def predicted(n,p):
    v=1
    for a in digits(n,p): v=v*cmod(a,p)%p
    return v

out={"schema":"D25_LUCAS_CARRY_AUTHOR_CHECK_V1","status":"AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_NATIVE","primes":[],"negative_control":{}}
total=0
for p in PRIMES:
    max_n=min(p*p,500)
    nonzero=0
    for n in range(max_n):
        x=cmod(n,p)
        assert x==predicted(n,p),(p,n)
        v=valuation(n,p)
        assert v==suffix(n,p),(p,n)
        sp=lambda n:sum(digits(n,p))
        assert v==(5*sp(n)-sp(3*n)-sp(2*n))//(p-1)
        assert (v==0)==(x!=0)==all(3*a<p for a in digits(n,p))
        nonzero+=bool(x)
        total+=1
    supported=((p-1)//3+1)**2
    if max_n==p*p: assert nonzero==supported
    assert valuation(p,p)==0
    assert cmod(p,p)==cmod(1,p)==pow(18,-1,p)
    assert all(valuation(k,p)==3 for k in range((2*p+2)//3,p))
    out["primes"].append({"p":p,"n_tested":max_n,"nonzero":nonzero,"full_p2_expected":supported if max_n==p*p else None})
for p in (5,7,13,19):
    lhs,rhs=cmod(p,p,2),cmod(1,p,2)
    assert lhs!=rhs
    out["negative_control"][str(p)]={"c_p_mod_p2":lhs,"c_1_mod_p2":rhs,"difference":(lhs-rhs)%(p*p)}
out["total_direct_binomial_checks"]=total
out["verdict"]="PASS"
print(json.dumps(out,ensure_ascii=False,indent=2))
