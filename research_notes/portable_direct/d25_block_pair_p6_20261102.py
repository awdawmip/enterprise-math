#!/usr/bin/env python3
"""Author-side exact check of D25 normalized block quotient to p^6.
All calculations are integer modular arithmetic; this is not a native H0/B0 experiment.
"""

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for j in range(2,int(n**.5)+1):
        if sieve[j]:
            sieve[j*j::j]=b'\x00'*(((n-j*j)//j)+1)
    return [j for j in range(7,n+1) if sieve[j]]

def prime_certificate(p):
    m=p**6
    # Independently constructed complete and paired half-range block carriers.
    num=den=1
    for j in range(1,p):
        num=num*(j+p)%m
        den=den*(j+3*p)%m
    q=num*pow(den,-1,m)%m
    half=1
    for j in range(1,(p-1)//2+1):
        numerator=(j*j-p*j-2*p*p)%m
        denominator=(j*j-p*j-12*p*p)%m
        half=half*numerator*pow(denominator,-1,m)%m
    assert q==half, ('pair identity',p)
    h2=sum(pow(j*j,-1,p**4) for j in range(1,p))%(p**4)
    h4=sum(pow(j**4,-1,p**2) for j in range(1,p))%(p**2)
    assert h2%p==0 and h4%p==0
    expectation=(1+5*p*p*h2 + (65*pow(2,-1,m))*p**4*h4)%m
    assert q==expectation,('six-digit harmonic formula',p,q,expectation)
    difference=q-1-5*p*p*h2
    assert difference % p**5 ==0
    res6=(difference//p**5)%p
    res6_predict=(65*pow(2,-1,p)*(h4//p))%p
    assert res6==res6_predict, ('sixth digit',p,res6,res6_predict)
    return (p,(q-1)//(p**3)%p,res6,(h2//p)%p,(h4//p)%p)

def main():
    ps=primes_upto(3000)
    results=[prime_certificate(p) for p in ps]
    print('prime range=7..3000 count=',len(ps))
    print('exact half-range paired factorization: PASS')
    print('mod p^6 harmonic formula: PASS')
    print('high-digit correction mod p: PASS')
    for row in results:
        if row[0] in [7,13,19,37,373,1171,2999]:print('certificate',row)
if __name__=='__main__':main()
