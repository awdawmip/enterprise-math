#!/usr/bin/env python3
"""Two independent exact modular checks of the original W216 grade-2/3 jet.
AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.
"""
from math import comb

def coeff_binomial(p, bound):
    M=p**4; inv=pow(216,-1,M)
    return [comb(2*k,k)**2*comb(3*k,k)*pow(inv,k,M)%M for k in range(bound)]

def coeff_pfree(p, bound):
    M=p**4
    val=[0]*(3*bound+1); unit=[1]*(3*bound+1)
    for n in range(1,3*bound+1):
        x=n; t=0
        while x%p==0:
            x//=p; t+=1
        val[n]=val[n-1]+t
        unit[n]=unit[n-1]*x%M
    inv=pow(216,-1,M); out=[]
    for k in range(bound):
        v=val[2*k]+val[3*k]-5*val[k]
        assert v>=0
        if v>=4: out.append(0)
        else:
            u=unit[2*k]*unit[3*k]*pow(unit[k],-5,M)%M
            out.append(u*p**v*pow(inv,k,M)%M)
    return out

def L(x): return x[3]-5*x[2]+7*x[1]-3*x[0]

def check(p):
    assert p>=13 and p%6==1
    M=p**4; A=coeff_binomial(p,4*p)
    assert A==coeff_pfree(p,4*p)
    H=[0]*p
    for n in range(1,p): H[n]=(H[n-1]+pow(n,-1,p))%p
    fq=(pow(216,p-1,p*p)-1)//p
    C=[[0]*4 for _ in range(4)]
    W2=W3=J2=0
    for b in range(p):
        grade=2*b//p+3*b//p
        rows=[]
        for a in range(4):
            k=p*a+b
            z=A[k]*pow(A[a],-1,M)%M
            rows.append(z)
            C[grade][a]=(C[grade][a]+(6*k+1)*z)%M
        if grade==2:
            lam=(2*H[2*b-p]+3*H[3*b-p]-5*H[b]-fq)%p
            for a in range(4):
                P=(2*a+1)*(3*a+1)
                assert rows[a]==A[b]*P*(1+p*a*lam)%M
            W2=(W2+(6*b+1)*A[b])%M
            J2=(J2+A[b]*(6+(6*b+1)*lam))%M
        if grade==3:
            for a in range(4):
                P=(2*a+1)*(3*a+1)*(3*a+2)//2
                assert rows[a]==A[b]*P%M
            W3=(W3+(6*b+1)*A[b])%M
    ls=[L(row)%M for row in C]
    assert ls[2]==(-24*W2-56*p*J2)%M
    assert ls[3]==(-108*W3)%M
    m=(p-1)//6
    ref=sum((6*h-1)*pow(18*h**3*(A[h]%p),-1,p)
            for h in range(1,2*m+1))%p
    assert W3//p**3%p==ref
    assert sum(ls)%M==(ls[0]+ls[1]-24*W2-56*p*J2-108*W3)%M
    return p,ls[2],ls[3],W3//p**3%p,ls[3]//p**3%p,sum(ls)%M

if __name__=="__main__":
    for p in (13,19,31,37,43,61,67,73,109,373):
        print(check(p))
