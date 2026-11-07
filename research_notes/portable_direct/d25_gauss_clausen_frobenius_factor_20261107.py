"""Exact finite-field test of the 2304 Frobenius/Clausen square factorization."""
from math import comb

def primes(n):
    return [x for x in range(5,n) if all(x%d for d in range(2,int(x**0.5)+1))]

def mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%p
    return out

def ev(a,z,p):
    v=0
    for x in a[::-1]: v=(v*z+x)%p
    return v

def check(p):
    assert p%8==5
    r=(5*p-1)//8; s=(7*p-3)//8; t=(p+1)//2; k=(p-5)//8
    g=[comb(r,i)*comb(s,i)%p for i in range(r+1)]
    for d in range(t):
        assert sum(comb(r,i)*comb(s,i)*comb(i,d) for i in range(d,r+1))%p==0
    assert sum(comb(r,i)*comb(s,i)*comb(i,t) for i in range(t,r+1))%p!=0
    # Taylor coefficients of G/(1-z)^t through degree k.
    h=[sum(g[j]*comb(t+i-j-1,i-j) for j in range(min(i,r)+1))%p for i in range(k+1)]
    factor=[(-1)**i*comb(t,i)%p for i in range(t+1)]
    assert mul(factor,h,p)==g
    hh=mul(h,h,p); q=[0]*(len(hh)+1)
    for i,x in enumerate(hh):
        q[i]=(q[i]+x)%p; q[i+1]=(q[i+1]-x)%p
    g2=mul(g,g,p)
    assert len(g2)==p+len(q)
    expect=[0]*len(g2)
    for i,x in enumerate(q):
        expect[i]=(expect[i]+x)%p; expect[p+i]=(expect[p+i]-x)%p
    assert g2==expect
    z=pow(9,-1,p)
    Q=ev(q,z,p); dQ=ev([i*q[i]%p for i in range(1,len(q))],z,p)
    H=ev(h,z,p)
    if p%24==13: assert H==0 and Q==0 and dQ==0
    if p%24==5: assert H!=0 and Q!=0
    return p,k,t,Q,dQ,H

if __name__=="__main__":
    results=[check(p) for p in primes(500) if p%8==5]
    assert len(results)==24
    print("GAUSS_CLAUSEN_FACTOR_EXACT",len(results),"PASS p<500")
    for row in results:
        if row[0] in (5,13,29,37,61,109,373): print(row)
