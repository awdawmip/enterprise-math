#!/usr/bin/env python3
"""Author-side exact q² digit/carry verifier for D25/LIFT finite Clausen ports.
No native H0/B0 or Source experiment implied. All arithmetic is integer-exact.
"""
from math import comb, isqrt
from functools import lru_cache
import json

def prime(q):
    return q >= 2 and all(q % d for d in range(2, isqrt(q)+1))

@lru_cache(None)
def data(q):
    inv=[0]+[pow(i,-1,q) for i in range(1,q)]
    H=[0]*q
    for i in range(1,q): H[i]=(H[i-1]+inv[i])%q
    f=[1]*q
    for i in range(1,q): f[i]=f[i-1]*i%q
    return H,f

def binom_jet(q,n,k):
    """Return L,R,borrow with binom(n,k)=L+qR mod q²."""
    assert prime(q) and q>=5 and 0<=k<=n
    M,a=divmod(n,q); K,b=divmod(k,q)
    H,f=data(q)
    if b<=a:
        L=comb(M,K)*comb(a,b)%(q*q)
        R=L*(M*H[a]-K*H[b]-(M-K)*H[a-b])%q
        return L,R,0
    assert M>K
    c=b-a
    R=comb(M,K)*(M-K)*(-1 if (c-1)%2 else 1)
    R=R*f[a]*f[c-1]*pow(f[b],-1,q)%q
    return 0,R,1

def reconstructed(q,m,e):
    q2=q*q; inv2=pow(2,-1,q2)
    A=B=0
    parts={s:[0,0] for s in ("00","01","10","11")}
    core=[0,0]; jet=[0,0]; weight=[0,0]
    for k in range(m+1):
        K,b=divmod(k,q)
        L1,R1,c1=binom_jet(q,m,k)
        L2,R2,c2=binom_jet(q,2*m+e,k)
        L=L1*L2%q2; R=(L1*R2+R1*L2)%q
        xk=pow(inv2,k,q2)
        v=(L+q*R)*xk%q2
        w=1-6*e+12*k
        A=(A+v)%q2; B=(B+w*v)%q2
        key=f"{c1}{c2}"
        parts[key][0]=(parts[key][0]+v)%q2
        parts[key][1]=(parts[key][1]+w*v)%q2
        v0=L*xk%q2; v1=q*R*xk%q2
        core[0]=(core[0]+v0)%q2
        core[1]=(core[1]+(1-6*e+12*b)*v0)%q2
        jet[0]=(jet[0]+v1)%q2
        jet[1]=(jet[1]+(1-6*e+12*b)*v1)%q2
        weight[1]=(weight[1]+12*q*K*v0)%q2
    assert ((core[0]+jet[0])%q2,
            (core[1]+jet[1]+weight[1])%q2)==(A,B)
    assert (sum(v[0] for v in parts.values())%q2,
            sum(v[1] for v in parts.values())%q2)==(A,B)
    return (A,B),parts,{"base":core,"binomial_jet":jet,"weight_carry":weight}

def direct(q,m,e):
    q2=q*q; inv2=pow(2,-1,q2)
    A=B=0
    for k in range(m+1):
        t=comb(m,k)*comb(2*m+e,k)*pow(inv2,k,q2)%q2
        A=(A+t)%q2
        B=(B+(1-6*e+12*k)*t)%q2
    return A,B

def verify():
    ncheck=borrow=0
    for q in range(5,38):
        if not prime(q): continue
        for n in range(121):
            for k in range(n+1):
                L,R,c=binom_jet(q,n,k)
                assert (L+q*R-comb(n,k))%(q*q)==0,(q,n,k)
                ncheck+=1; borrow+=c
    tests=higher=0
    examples={}
    for q in range(5,998):
        if not prime(q): continue
        for r in range(1,12):
            N=q**r
            e=0 if N%6==1 else 1
            m=(N-1-4*e)//6
            if m>600: break
            pair,parts,channels=reconstructed(q,m,e)
            assert pair==direct(q,m,e),(q,r,pair)
            tests+=1; higher+=int(r>=2)
            if (q,r) in {(5,2),(5,4),(7,2),(7,3),(11,2),(13,2),(17,2),(29,2),(37,2)}:
                e1=int(q%6==5)
                m1=(q-1-4*e1)//6
                base=direct(q,m1,e1)
                examples[f"{q}^{r}"]={"N":N,"m":m,"epsilon":e,
                    "pair_mod_q2":list(pair),"pair_mod_q":[z%q for z in pair],
                    "base_pair_mod_q2":list(base),"carry_classes":parts,
                    "channels":channels}
    assert (ncheck,borrow,tests,higher)==(73810,30173,188,22)
    return {"coefficients":ncheck,"borrow_coefficients":borrow,
            "primepower_pairs":tests,"r_ge2":higher,
            "exact":True,"examples":examples}

if __name__=="__main__":
    print(json.dumps(verify(),indent=2))
