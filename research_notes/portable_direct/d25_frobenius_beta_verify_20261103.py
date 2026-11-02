#!/usr/bin/env python3
"""D25 finite Wronskian Frobenius-beta verifier, original 216 arithmetic.
Author-side exact checks; native H0/B0 is not executed.
"""
from math import comb, isqrt
import json

def primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[:2] = b'\x00\x00'
    for k in range(2, isqrt(limit) + 1):
        if sieve[k]:
            sieve[k*k::k] = b'\x00' * ((limit-k*k)//k + 1)
    return [p for p in range(7, limit + 1) if sieve[p] and p % 6 == 1]

def inverses(p):
    inv = [0]*p
    inv[1] = 1
    for n in range(2, p):
        inv[n] = -(p//n)*inv[p%n] % p
    return inv

def source(p, r, inv):
    a=[1]
    for n in range(2*r):
        a.append(a[-1]*(2*n+1)*(3*n+1)*(3*n+2) *
                 inv[18%p]*pow(inv[n+1],3,p)%p)
    return a

def core(p):
    r=(p-1)//6
    u=3*r
    inv=inverses(p)
    a=source(p,r,inv)
    S=[(9*n+4)*a[n]*inv[36%p]%p for n in range(2*r+1)]
    omega=[0]
    for n in range(u):
        s=S[n] if n<=2*r else 0
        omega.append((s-(u-n)*omega[-1])*inv[n+1]%p)
    assert omega[u]==(-1 if r%2 else 1)*inv[6]%p
    half=inv[2]
    zpow=1
    om=0
    for v in omega:
        om=(om+v*zpow)%p
        zpow=zpow*half%p
    C=pow(half,u+1,p)
    B=(1-C)*inv[u+1]%p
    zpow=half
    beta=inv[u+1]
    I=moment=0
    for n,s in enumerate(S):
        I=(I+s*B)%p
        moment=(moment+(9*n+4)*a[n]*beta)%p
        if n<2*r:
            denom=inv[n+u+2]
            B=((n+1)*B-zpow*C)*denom%p
            beta=(n+1)*beta*denom%p
            zpow=zpow*half%p
    assert moment==6%p
    chi=pow(2,u,p)
    assert chi in (1,p-1)
    assert om==2*chi*(I-inv[12%p])%p
    record={"p":p,"r":r,"chi_2":chi if chi==1 else -1,
            "omega_lead":omega[u],"omega_half":om,
            "beta_half":I,"complete_beta_moment":moment}
    if p%24 in (13,19):
        m=p*p
        L=[1]
        for k in range(r):
            L.append(L[-1]*(r-k)*(2*r-k)*pow((k+1)**2,-1,m)%m)
        h=pow(2,-1,m)
        v=d=t=0
        zpow=1
        for k,c in enumerate(L):
            v=(v+c*zpow)%m
            d=(d+k*c*zpow)%m
            zpow=zpow*h%m
        assert v%p==0
        g=v//p
        j=d%p
        carry=(4*g*j+8*I)%p
        assert carry==1
        record.update({"g":g,"j":j,"transformed_carry":carry})
    return record

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                c[i+j]=(c[i+j]+x*y)%p
    return c

def full_polynomial_check(p):
    r=(p-1)//6
    u=3*r
    inv=inverses(p)
    ell=[1]
    for k in range(r):
        ell.append(ell[-1]*(r-k)*(2*r-k)*pow(inv[k+1],2,p)%p)
    Q=[0]
    for k in range(1,2*r+1):
        s=((k-1)*inv[2]-2*r*inv[3])*ell[k-1] if k-1<=r else 0
        Q.append(((k-1-r)*(k-1-2*r)*Q[-1]+s)*pow(inv[k],2,p)%p)
    W1=mul(ell,[k*v%p for k,v in enumerate(Q)],p)
    W2=mul(Q,[k*v%p for k,v in enumerate(ell)],p)
    W=[(a-b)%p for a,b in zip(W1,W2)]
    S=[(9*n+4)*v*inv[36%p]%p for n,v in enumerate(source(p,r,inv))]
    left=mul([(-1)**k*comb(u+1,k)%p for k in range(u+2)],W,p)
    product=mul([(-1)**k*comb(u,k)%p for k in range(u+1)],S,p)
    I=[0]+[v*inv[k+1]%p for k,v in enumerate(product)]
    right=I+[0]*(p+1-len(I))
    right[p]=(right[p]-inv[6])%p
    assert len(left)==p+1 and left==right
    h=inv[2]
    actual=sum(v*pow(h,k,p) for k,v in enumerate(I))%p
    row=core(p)
    assert actual==row["beta_half"]
    return {"p":p,"coefficientwise_F1":"PASS","I_half":actual}

def main():
    ps=primes(10000)
    rows=[core(p) for p in ps]
    targets=[x for x in rows if x["p"]%24 in (13,19)]
    assert len(ps)==611 and len(targets)==312
    samples=[7,13,19,31,37,43,73,373,1171]
    proofs=[full_polynomial_check(p) for p in samples]
    print(json.dumps({
        "all_primes":len(ps),"beta_moment_pass":len(ps),
        "beta_vs_wronskian_pass":len(ps),"top_coefficient_pass":len(ps),
        "target_finite_carry_pass":len(targets),
        "full_polynomial_checks":proofs,
        "samples":[r for r in rows if r["p"] in samples],
        "proof_scope":"F1/F2/F3 and beta recursion exact; all-target second carry OPEN",
        "scientific_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
        "native_H0_B0":"NOT_EXECUTED"
    },ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
