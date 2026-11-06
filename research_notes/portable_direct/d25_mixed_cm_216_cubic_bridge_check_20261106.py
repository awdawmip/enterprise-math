#!/usr/bin/env python3
"""Exact Z and Z/p^4 verification. Author-side, not native H0/B0."""
from math import comb, isqrt
import json
def prime(n):
    if n<2: return False
    for d in range(2,isqrt(n)+1):
        if n%d==0: return False
    return True
def check(p):
    m=(p-1)//6; mod=p**4
    b=[1]
    for n in range(1,p+1):
        num=b[-1]*6*(6*n-5)*(3*n-2)
        assert num%(n*n)==0
        b.append(num//(n*n))
    g=[comb(2*k,k)**2*comb(3*k,k) for k in range(p+1)]
    def val(x):
        if x%p: return 0
        if x%p**2: return 1
        if x%p**3: return 2
        if x%p**4: return 3
        return 4
    assert val(b[p])==val(g[p])==0
    assert [val(g[k]*b[p-k]) for k in range(1,p)] == [2]*(2*m)+[3]*m+[4]*(2*m)+[3]*m
    low=sum(g[k]*b[p-k] for k in range(1,2*m+1))%mod
    middle=sum(g[k]*b[p-k] for k in range(2*m+1,3*m+1))%mod
    silent=sum(g[k]*b[p-k] for k in range(3*m+1,5*m+1))%mod
    upper=sum(g[k]*b[p-k] for k in range(5*m+1,6*m+1))%mod
    A=sum(g[k]*b[p-k] for k in range(p+1))%mod
    weighted=sum((6*k+1)*g[k]*b[p-k] for k in range(p+1))%mod
    assert silent==0 and A==(b[p]+g[p]+low+middle+upper)%mod
    assert weighted==((4*p+1)*A)%mod
    assert A==18%mod # finite test of attributed Shvets result, not proof
    if p in (13,19,373):
        # Independent direct triple Cauchy coefficient.
        bb=[x%mod for x in b]
        pair=[sum(bb[i]*bb[j-i] for i in range(j+1))%mod for j in range(p+1)]
        assert A==sum(pair[j]*bb[p-j] for j in range(p+1))%mod
    return {"p":p,"M_div_p3":middle//p**3,"U_div_p3":upper//p**3,"A":A}
if __name__=="__main__":
    ps=[p for p in range(7,998) if p%6==1 and prime(p)]
    out=[check(p) for p in ps]
    print(json.dumps({"scope":"7<=p<=997, p prime, p==1 mod6",
                      "tested":len(ps),"target":sum(p%24 in (13,19) for p in ps),
                      "samples":[x for x in out if x["p"] in (13,19,67,373)],
                      "status":"ALL_PASS"},indent=2))
