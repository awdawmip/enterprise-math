#!/usr/bin/env python3
"""Original W216 signed-moment reduction; exact modular arithmetic.
AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
Only valid for primes p>3; no claims of a uniform LIFT proof.
"""
from math import isqrt

def is_prime(n):
    if n<2: return False
    return all(n%d for d in range(2,isqrt(n)+1))

def p_free_factorial(n,p,mod):
    product=1
    for x in range(1,n+1):
        while x%p==0: x//=p
        product=product*x%mod
    return product

def certificate(p):
    assert p>3 and is_prime(p)
    q=p**3
    mod=p**5  # enough to divide a_(p-1) by p^2
    inv36=pow(36,-1,mod)
    a=1; W=0; moments=[0,0,0]
    for k in range(p):
        if k:
            j=k-1
            a=a*(2*j+1)*(3*j+1)*(3*j+2)*inv36*pow(k,-3,mod)%mod
        W=(W+(6*k+1)*a)%q
        if k<p-1:
            inv=pow(k+1,-1,q)
            for index,power in enumerate((1,inv,inv*inv%q)):
                moments[index]=(moments[index]+a*power)%q
    assert a%(p**3)==0
    a_last=a
    ap=(p_free_factorial(2*p,p,q)*p_free_factorial(3*p,p,q)*
        pow(216,-p,q)*pow(p_free_factorial(p,p,q),-5,q))%q
    endpoint=(-12*p*ap)%q
    last_residue=((a_last//p**2)*(p-2)*(6*p-1)*pow(3,-1,q))%q
    assert (endpoint-last_residue)%q==0, 'the last val-3 boundary must cancel'
    s0,s1,s2=moments
    predicted=(-2*s0+pow(3,-1,q)*(13*s1-2*s2))%q
    assert predicted==W, 'three-moment identity fails'
    return dict(p=p,W=W,moments=moments,endpoint=endpoint,
                last_boundary=last_residue,observed_three_port=predicted)

def main():
    cases=[5,7,11,13,17,19,23,31,37,43,109,157,373]
    records=[certificate(p) for p in cases]
    r=records[-1]
    assert r['moments']==[9878159,48777891,27945670]
    assert r['W']==373
    assert r['endpoint']==19431435
    assert r['last_boundary']==19431435
    print('PASS',len(records),'distinct primes; no floating point')
    for r in records:
        print(r)

if __name__=='__main__': main()
