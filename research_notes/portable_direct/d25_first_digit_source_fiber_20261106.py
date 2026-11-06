#!/usr/bin/env python3
"""D25 exact source-tangent observer certificate; standard library, no native CM."""
from math import isqrt

def primes(limit):
    z=bytearray([1])*(limit+1);z[:2]=b'\0\0'
    for d in range(2,isqrt(limit)+1):
        if z[d]:z[d*d:limit+1:d]=bytes((limit-d*d)//d+1)
    return [p for p in range(7,limit+1) if z[p] and p%6==1]

def derivative_row(p):
    m=(p-1)//6;s=(2*m,3*m,4*m)
    B=[1,1,1];D=[0,0,0];t=1;Z=0;T=[0,0,0]
    q=-pow(2,-1,p)%p
    for j in range(p):
        Z=(Z+t*B[0]*B[1]*B[2])%p
        for i in range(3):
            T[i]=(T[i]+(6*j+1)*t*D[i]*B[(i+1)%3]*B[(i+2)%3])%p
        if j==p-1:break
        f=pow(j+1,-1,p)
        for i in range(3):
            D[i]=(D[i]*(s[i]-j)+B[i])*f%p
            B[i]=B[i]*(s[i]-j)*f%p
        t=t*q%p
    return tuple(T),Z

def weighted_sum(p,v):
    # Independent evaluation of all p terms over Z/p², even at zero-base/carry indices.
    P=p*p;m=(p-1)//6;s=(2*m,3*m,4*m)
    B=[1,1,1];t=1;W=0;q=-pow(2,-1,P)%P
    for j in range(p):
        W=(W+(6*j+1)*t*B[0]*B[1]*B[2])%P
        if j==p-1:break
        f=pow(j+1,-1,P)
        for i in range(3):B[i]=B[i]*(s[i]+p*v[i]-j)*f%P
        t=t*q%P
    return W

def test():
    ps=primes(3000);assert len(ps)==207
    for p in ps:
        T,Z=derivative_row(p)
        v=(-pow(3,-1,p),-pow(2,-1,p),-2*pow(3,-1,p))
        W=weighted_sum(p,v)
        assert W==p,(p,W)
        for i in range(3):
            v2=list(v);v2[i]+=1
            assert ((weighted_sum(p,v2)-W)%(p*p))//p==T[i]
        assert (T[0]+T[2])%p==0
        if p in (13,19,373):
            assert T[0]
            basis=(((-T[1]*pow(T[0],-1,p))%p,1,0),(1,0,1))
            for delta in basis:
                for k in ((0,1,7) if p==373 else range(p)):
                    assert weighted_sum(p,tuple(v[i]+k*delta[i] for i in range(3)))==W
            response=((p-1)//2)*pow(2,-1,p)%p
            assert response
            print(p,T,Z,W//p,basis,response)
    print("PASS 207 primes: derivative rows vs 3 independent mod p² differences")
    print("PASS exact affine fibers at p13,p19,p373; T1+T3 observed 207/207")

if __name__=="__main__":test()
