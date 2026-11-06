#!/usr/bin/env python3
"""D25 source-fiber second digit: exact p-adic Taylor jets and independent p³ sums."""
from math import isqrt

def primes(limit):
    z=bytearray([1])*(limit+1);z[:2]=b'\0\0'
    for d in range(2,isqrt(limit)+1):
        if z[d]:z[d*d:limit+1:d]=bytes((limit-d*d)//d+1)
    return [p for p in range(7,limit+1) if z[p] and p%6==1]

def jets(p):
    P=p*p;m=(p-1)//6;s=(2*m,3*m,4*m)
    B=[1]*3;D=[0]*3;E=[0]*3;A=[0]*3;H=[[0]*3 for _ in range(3)]
    t=1;q=-pow(2,-1,P)%P
    for j in range(p):
        w=6*j+1
        for i in range(3):
            other=B[(i+1)%3]*B[(i+2)%3]
            A[i]=(A[i]+w*t*D[i]*other)%P
            H[i][i]=(H[i][i]+w*t*E[i]*other)%p
            for k in range(i+1,3):
                h=w*t*D[i]*D[k]*B[3-i-k]%p
                H[i][k]=(H[i][k]+h)%p;H[k][i]=(H[k][i]+h)%p
        if j==p-1:break
        f=pow(j+1,-1,P)
        for i in range(3):
            E[i]=(E[i]*(s[i]-j)+2*D[i])*f%P
            D[i]=(D[i]*(s[i]-j)+B[i])*f%P
            B[i]=B[i]*(s[i]-j)*f%P
        t=t*q%P
    return A,H

def direct(p,v):
    P=p**3;m=(p-1)//6;s=(2*m,3*m,4*m)
    B=[1,1,1];t=1;q=-pow(2,-1,P)%P;W=0
    for j in range(p):
        W=(W+(6*j+1)*t*B[0]*B[1]*B[2])%P
        if j==p-1:break
        f=pow(j+1,-1,P)
        for i in range(3):B[i]=B[i]*(s[i]+p*v[i]-j)*f%P
        t=t*q%P
    return W

def check(p):
    A,H=jets(p);P=p*p
    v=(-pow(3,-1,P),-pow(2,-1,P),-2*pow(3,-1,P))
    d=(1,0,1); L=sum(A[i]*d[i] for i in range(3))%P
    assert L%p==0,(p,L)
    lift=L//p
    cross=sum(v[i]*H[i][k]*d[k] for i in range(3) for k in range(3))%p
    quadratic=sum(d[i]*H[i][k]*d[k] for i in range(3) for k in range(3))*pow(2,-1,p)%p
    x=direct(p,v); y=direct(p,tuple(v[i]+d[i] for i in range(3)))
    diff=(y-x)%(p**3);assert diff%(p*p)==0
    digit=diff//(p*p)
    assert digit==(lift+cross+quadratic)%p
    return p,tuple(A),(H[0][0],H[0][2],H[2][2]),lift,cross,quadratic,digit,x

def test():
    for p in (13,19,373):print(check(p))
    ps=primes(3000);assert len(ps)==207
    rows=[check(p) for p in ps]
    assert all(r[6]!=0 for r in rows)
    print("PASS 207/207 independent source p³ vs second-jet formulas")
    print("Finite nonzero second digits 207/207, no universal claim")

if __name__=="__main__":test()
