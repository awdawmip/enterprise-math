#!/usr/bin/env python3
"""Original-216 p^3 two-jet: independent original-integer coefficient regression.
No floats; never substitutes for native H0/B0 or proof/admission.
"""
from math import comb
import json

def primes_to(n):
    s = [True] * (n+1)
    s[0:2] = [False, False]
    for d in range(2, int(n**0.5)+1):
        if s[d]:
            for t in range(d*d, n+1, d):
                s[t] = False
    return [i for i in range(n+1) if s[i]]

def original_b(n, p):
    m = p**3
    return (comb(2*n,n)**2 * comb(3*n,n) * pow(216,-n,m)) % m

def check_prime(p):
    m = p**3
    q = ((pow(216, p-1, m)-1)//p) % (p*p)
    inv=[0]+[pow(t,-1,p*p) for t in range(1,p)]
    h=[0]*p; h2=[0]*p
    for i in range(1,p):
        h[i]=(h[i-1]+inv[i])%(p*p)
        h2[i]=(h2[i-1]+inv[i]**2)%p
    inv2=pow(2,-1,m)
    count=0
    for k in range(4):
        ck=original_b(k,p)
        for j in range((p-1)//3+1):
            cj=original_b(j,p)
            d=(2*h[2*j]+3*h[3*j]-5*h[j]-q)%(p*p)
            s=(4*h2[2*j]+9*h2[3*j]-5*h2[j])%p
            factor=(1+p*k*d+p*p*inv2*(k*k*(d*d-s)+k*q*q))%m
            left=original_b(p*k+j,p)
            assert left==ck*cj*factor%m,(p,k,j,"coefficient")
            w=6*j+1
            weighted=ck*cj*(w+p*k*(w*d+6)+p*p*inv2*(k*k*(w*(d*d-s)+12*d)+k*w*q*q))%m
            assert weighted == (6*(p*k+j)+1)*left%m,(p,k,j,"weighted")
            count+=1
    return count

if __name__=="__main__":
    ps=[p for p in primes_to(191) if p>=5]+[373]
    checks=sum(check_prime(p) for p in ps)
    print(json.dumps({"status":"PASS","primes_checked":len(ps),
        "triples_checked":checks,"domain":"5<=p<=191 primes plus 373; 0<=k<=3; 0<=j<=floor((p-1)/3)",
        "method":"original integer binomial coefficients, modular arithmetic"}))
