#!/usr/bin/env python3
"""Author-side exact original W216 upper-tail check, not native H0/B0."""
from math import comb
from fractions import Fraction
import json

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\0\0'
    for d in range(2,int(n**.5)+1):
        if sieve[d]:
            sieve[d*d:n+1:d]=b'\0'*len(sieve[d*d:n+1:d])
    return [p for p in range(5,n+1) if sieve[p]]

def check_one(p,independent=False):
    modulus=p**5; q=p**2; h=2*p//3; R=(p-3)//3
    b=[1]; b_k=1
    for k in range(p-1):
        b_k=(b_k*(2*k+1)*(3*k+1)*(3*k+2)
             *pow(36*(k+1)**3,-1,modulus))%modulus
        b.append(b_k)
    if p in (5,7,13,19):
        last=Fraction(comb(2*p-2,p-1)**2*comb(3*p-3,p-1),216**(p-1))
        ratio=Fraction(1)
        for r in range(R+1):
            k=p-1-r
            direct=Fraction(comb(2*k,k)**2*comb(3*k,k),216**k)
            assert direct/last==ratio
            if r<R:
                t=r
                ratio*=Fraction(2)*(p-t-1)**3/(
                    (Fraction(p)-t-Fraction(3,2))*
                    (Fraction(p)-t-Fraction(4,3))*
                    (Fraction(p)-t-Fraction(5,3)))
    if independent:
        for k in range(p):
            direct=comb(2*k,k)**2*comb(3*k,k)
            assert direct*pow(216,-k,modulus)%modulus==b[k]
    assert b[-1]%p**3==0
    A=-(b[-1]//p**3)%q
    assert A%p==1
    tail=sum((6*k+1)*b[k] for k in range(h+1,p))%modulus
    assert tail%p**3==0
    observed=tail//p**3
    d=1; H=0; reconstructed=0
    for r in range(R+1):
        k=p-1-r
        term=A*d*((6*r+5)+p*((6*r+5)*H-6))%q
        direct=(((6*k+1)*b[k])%modulus)//p**3
        assert term==direct,(p,r,term,direct)
        reconstructed=(reconstructed+term)%q
        if r<R:
            slope=(2*pow(2*r+3,-1,q)+3*pow(3*r+5,-1,q)
                   +3*pow(3*r+4,-1,q)-3*pow(r+1,-1,q))%q
            H=(H+slope)%q
            d=d*36*(r+1)**3*pow(
                (2*r+3)*(3*r+5)*(3*r+4),-1,q)%q
    assert reconstructed==observed,(p,reconstructed,observed)
    return {'p':p,'h':h,'terms':R+1,'A_mod_p2':A,
            'tail_div_p3_mod_p2':observed,
            'first_digit':observed%p,'second_digit':observed//p}

if __name__=='__main__':
    ps=primes_upto(3000)
    focus=[5,7,13,19,31,37,43,373,1171]
    rows=[]; terms=0
    for p in ps:
        row=check_one(p,p<=103 or p in (373,1171))
        terms+=row['terms']
        if p in focus: rows.append(row)
    print(json.dumps({'schema':'D25_ORIGINAL_216_UPPER_TAIL_P5_CHECK_V1',
       'claim':'author-side exact modular integers, finite verified range only',
       'primes_count':len(ps),'range':'all primes 5<=p<=3000',
       'ordered_tail_terms_checked':terms,
       'independent_binomial_primes':len([p for p in ps if p<=103 or p in (373,1171)]),
       'focus':rows,'status':'PASS'},ensure_ascii=False,indent=2))
