#!/usr/bin/env python3
"""Exact finite-field test for D25 Clausen tangent-square and second-jet defect.
Author-side portable evidence; no native Enterprise Math experiment is implied.
"""
from math import isqrt

def primes_to(n):
    return [p for p in range(5,n+1) if all(p%d for d in range(2,isqrt(p)+1))]

def check(p):
    eps=1 if p%6==1 else -1
    m=(p-eps)//6
    delta=(1-eps)//2
    a,b,c=2*m-delta,3*m-delta,4*m-delta
    assert a+c==p-1 and 2*b==p-1
    i2=pow(2,-1,p);i4=i2*i2%p
    inv=[0]+[pow(k,-1,p) for k in range(1,p)]
    # Original 3F2 0,1,2 Taylor coefficients and Clausen-matched denominator.
    M=[[0]*p for _ in range(3)]
    C=[[0]*p for _ in range(3)]
    M[0][0]=C[0][0]=1
    for j in range(p-1):
        x,y,z=(j-a)%p,(j-b)%p,(j-c)%p
        n0=x*y*z%p
        n1=-(x*y+x*z+y*z)%p
        n2=(x+y+z)%p
        v=inv[j+1];scale=i2*pow(v,3,p)%p
        r0=n0*scale%p
        r1=(n1+3*n0*v)*scale%p
        for arr,quadratic in ((M,9),(C,7)):
            r2=(n2+3*n1*v+quadratic*n0*v*v)*scale%p
            u0,u1,u2=(arr[d][j] for d in range(3))
            arr[0][j+1]=u0*r0%p
            arr[1][j+1]=(u1*r0+u0*r1)%p
            arr[2][j+1]=(u2*r0+u1*r1+u0*r2)%p
    # 2F1((-a-t)/2,(a+1-t)/2;1-t;z) with t Taylor degrees 0,1,2.
    G=[[0]*p for _ in range(3)]
    G[0][0]=1
    A=-a*i2%p
    B=(a+1)*i2%p
    for j in range(p-1):
        x,y=(A+j)%p,(B+j)%p
        n0=x*y%p
        n1=-(x+y)*i2%p
        n2=i4;v=inv[j+1];scale=v*v%p
        r0=n0*scale%p
        r1=(n1+n0*v)*scale%p
        r2=(n2+n1*v+n0*v*v)*scale%p
        u0,u1,u2=(G[d][j] for d in range(3))
        G[0][j+1]=u0*r0%p
        G[1][j+1]=(u1*r0+u0*r1)%p
        G[2][j+1]=(u2*r0+u1*r1+u0*r2)%p
    zpow=1;H2=0
    for j in range(p):
        t0=t1=t2=0
        for k in range(j+1):
            l=j-k
            t0+=G[0][k]*G[0][l]
            t1+=G[0][k]*G[1][l]+G[1][k]*G[0][l]
            t2+=G[0][k]*G[2][l]+G[1][k]*G[1][l]+G[2][k]*G[0][l]
        assert (t0*zpow%p,t1*zpow%p,t2*zpow%p)==tuple(C[d][j] for d in range(3)),(p,j,"Clausen")
        assert M[0][j]==C[0][j] and M[1][j]==C[1][j],(p,j,"first-jet")
        assert (M[2][j]-C[2][j]-2*H2*M[0][j])%p==0,(p,j,"quadratic-defect")
        zpow=zpow*i2%p
        if j<p-1:H2=(H2+inv[j+1]**2)%p
    Z=sum(M[0])%p
    L=sum((6*j+1)*M[0][j] for j in range(p))%p
    S=sum((6*j+1)*M[1][j] for j in range(p))%p
    defect=sum((6*j+1)*(M[2][j]-C[2][j]) for j in range(p))%p
    branch=None
    if eps==1:
        assert all(G[0][k]==0 for k in range(m+1,p))
        assert all(G[1][k]==0 for k in range(2*m+1,p))
        assert 3*m<p
        g=gp=dg=dgp=0
        for k in range(p):
            g=(g+G[0][k]*pow(i2,k,p))%p
            dg=(dg+G[1][k]*pow(i2,k,p))%p
            if k:
                gp=(gp+k*G[0][k]*pow(i2,k-1,p))%p
                dgp=(dgp+k*G[1][k]*pow(i2,k-1,p))%p
        assert g*g%p==Z and g*(g+6*gp)%p==L
        assert ((2*g+6*gp)*dg+6*g*dgp)%p==S
        if L==0:
            if g==0:
                assert (S-6*gp*dg)%p==0
                branch="G_ZERO"
            else:
                assert (g+6*gp)%p==0
                assert (S-g*(dg+6*dgp))%p==0
                branch="G_NONZERO"
    return dict(p=p,Z=Z,L=L,S=S,weighted_quadratic_defect=defect,branch=branch)

if __name__=="__main__":
    pp=primes_to(211)+[373,1009]
    out=[check(p) for p in pp]
    print(f"CLAUSEN FIRST JET & QUADRATIC DEFECT: {len(out)}/{len(pp)} PASS")
    for row in out:
        if row["p"] in (5,7,11,13,17,19,31,73,127,211,373,1009):
            print(row)
