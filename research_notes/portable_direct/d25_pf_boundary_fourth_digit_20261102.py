#!/usr/bin/env python3
"""Exact fourth-digit Picard--Fuchs boundary unit and cross-stream coefficient."""
from math import isqrt

def primes_upto(n):
    composite=bytearray(n+1)
    for d in range(2,isqrt(n)+1):
        if not composite[d]:
            composite[d*d::d]=b'\x01'*((n-d*d)//d+1)
    return [p for p in range(5,n+1) if not composite[p]]

def check_one(p,label):
    M=p**4
    if label=="A":
        numerator=lambda k:(2*k+1)*(3*k+1)*(3*k+2)
        norm,zden=18,2
        alpha=((1,2),(1,3),(2,3))
        sym=((3,2),(13,18),(1,9))
        endpoint_den=18
    else:
        numerator=lambda k:(4*k+1)*(2*k+1)*(4*k+3)
        norm,zden=32,9
        alpha=((1,4),(1,2),(3,4))
        sym=((3,2),(11,16),(3,32))
        endpoint_den=96
    z=pow(zden,-1,M)
    c=1
    moments=[0]*4
    for k in range(p):
        w=1
        for j in range(4):
            moments[j]=(moments[j]+c*w)%M
            w=w*k%M
        if k<p-1:
            c=c*numerator(k)*z*pow(norm*(k+1)**3,-1,M)%M
    # c includes z**(p-1); remove it to obtain the original c_(p-1).
    bare=c*pow(z,-(p-1),M)%M
    assert bare%p**3==0,(p,label,"valuation")
    assert bare//p**3==p-1,(p,label,"normalized coefficient")
    s1,s2,s3=[a*pow(b,-1,M)%M for a,b in sym]
    f0,f1,f2,f3=moments
    L=((1-z)*f3-z*(s1*f2+s2*f1+s3*f0))%M
    endpoint_prod=1
    for a,b in alpha:
        endpoint_prod=endpoint_prod*((p-1)*b+a)*pow(b,-1,M)%M
    rhs=-bare*endpoint_prod*pow(z,p,M)%M
    assert L==rhs,(p,label,"exact finite PF endpoint")
    assert L%p**3==0,(p,label,"p3 boundary")
    endpoint_unit=L//p**3
    expected=(-pow(endpoint_den,-1,p))%p
    assert endpoint_unit==expected,(p,label,"normalized boundary",endpoint_unit,expected)
    return endpoint_unit

def main():
    primes=primes_upto(3000)
    chosen=(5,7,11,13,19,37,61,73,373,1171,2999)
    print("THEOREM_CHECK: PF_P3_BOUNDARY_AND_CROSS_STREAM_16_OVER_3 = PASS")
    print("DOMAIN: all primes 5<=p<=3000; original finite sums and full p^4 modular PF residual")
    print("PRIME_COUNT:",len(primes))
    print("CHECKS: c_(p-1)/p^3=-1 mod p; exact endpoint; (L_AF_A)/p^3=-1/18; (L_BF_B)/p^3=-1/96; 3A-16B=0 mod p")
    for p in primes:
        a=check_one(p,"A")
        b=check_one(p,"B")
        assert (3*a-16*b)%p==0,(p,a,b,"cross source")
        if p in chosen:
            print(f"CERT p={p} unit_A={a} unit_B={b} cross={(3*a-16*b)%p}")
    print("ALL_PASS")

if __name__=="__main__":
    main()
