#!/usr/bin/env python3
"""D25 E3(lambda=1/2) CM comparison model; NOT native H0/B0."""
import json
from math import comb

def prime(q):
    return q >= 2 and all(q % i for i in range(2, int(q**0.5)+1))

def mul(u, v, modulus):
    a, b = u; c, d = v
    iv = pow(8, -1, modulus)
    return ((a*c-b*d*iv) % modulus, (a*d+b*c+b*d) % modulus)

def polynomial_value(coeffs, modulus):
    power = (1, 0); out = (0, 0)
    for coefficient in coeffs:
        out = ((out[0]+coefficient*power[0]) % modulus,
               (out[1]+coefficient*power[1]) % modulus)
        power = mul(power, (0, 1), modulus)
    return out

def hasse_binomial(p, modulus):
    r=(p-1)//6
    iv27=pow(27, -1, modulus)
    coeffs=[comb(3*r, m)*4**m*comb(6*r-2*m, m)*pow(iv27,m,modulus)
            for m in range(2*r+1)]
    return polynomial_value(coeffs, modulus)

def hasse_literal_power(p, modulus):
    iv27=pow(27, -1, modulus); a=(0, iv27)
    terms=[mul(a,a,modulus), (0,2*iv27 % modulus), (1,0),(4,0)]
    poly=[(1,0)]
    for _ in range((p-1)//2):
        nxt=[(0,0)]*min(len(poly)+3,p)
        for i, u in enumerate(poly):
            for j, v in enumerate(terms):
                if i+j>=len(nxt):break
                w=mul(u,v,modulus); old=nxt[i+j]
                nxt[i+j]=((old[0]+w[0])%modulus,(old[1]+w[1])%modulus)
        poly=nxt
    return poly[p-1]

def legendre_recurrence(p,modulus):
    r=(p-1)//6
    inv2=pow(2,-1,modulus); prev=current=1
    for m in range(1,2*r):
        factor=inv2 if (m&1) else 1
        nxt=((2*m+1)*factor*current-m*prev)*pow(m+1,-1,modulus)%modulus
        prev,current=current,nxt
    return current

def legendre_binomial(p,modulus):
    r=(p-1)//6
    coeffs=[(-1)**m*comb(2*r,m)*comb(2*r+m,m) for m in range(2*r+1)]
    return polynomial_value(coeffs,modulus)


def gauss_legendre_first_jet(p):
    r=(p-1)//6; modulus=p*p
    G=sum(comb(r,k)*comb(2*r,k)*pow(2,-k,modulus)
          for k in range(r+1))%modulus
    h=0; correction=0
    for k in range(1,r+1):
        h=(h+pow(k-1-2*r,-1,p))%p
        w=comb(r,k)*comb(2*r,k)*pow(2,-k,p)%p
        correction=(correction+w*h*pow(2,-1,p))%p
    L=legendre_recurrence(p,modulus)
    assert (L-G)%modulus==(p*correction)%modulus, (p,G,L,correction)
    return (G,L,correction)

if __name__=="__main__":
    groups={1:[0,0],7:[0,0],13:[0,0],19:[0,0]}
    for p in range(7,2001):
        if not prime(p) or p%6!=1:continue
        a=hasse_binomial(p,p)
        l=legendre_recurrence(p,p)
        assert a==(l,0),(p,a,l)
        group=groups[p%24];group[0]+=1;group[1]+=int(l==0)
        assert (l==0)==(p%24 in (13,19)),p
    print("class counts and zero counts",json.dumps(groups,sort_keys=True))
    for p in (13,19,37,373):
        modulus=p*p
        a=hasse_binomial(p,modulus)
        assert a==hasse_literal_power(p,modulus),(p,a)
        l=legendre_recurrence(p,modulus)
        assert legendre_binomial(p,modulus)==(l,0)
        assert all(z%p==0 for z in a) and l%p==0
        print(json.dumps({"p":p,"Hasse_mod_p2":a,
              "Hasse_divided_p_mod_p":[v//p for v in a],
              "Legendre_mod_p2":l,"Legendre_divided_p_mod_p":l//p}))

if __name__=="__main__":
    for p in range(7,2001):
        if prime(p) and p%6==1:
            gauss_legendre_first_jet(p)
    for p in (13,19,37,373):
        print("GAUSS_LEGENDRE_JET",p,gauss_legendre_first_jet(p))
