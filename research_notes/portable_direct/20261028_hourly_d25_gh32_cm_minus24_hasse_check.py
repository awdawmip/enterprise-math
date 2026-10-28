#!/usr/bin/env python3
"""Exact GH-32 finite-field checks; portable author-side evidence only."""
from math import comb
def primes(limit):
    s=bytearray([1])*limit;s[:2]=bytes(2)
    for i in range(2,int(limit**0.5)+1):
        if s[i]:s[i*i::i]=bytes(((limit-1-i*i)//i)+1)
    return [i for i in range(limit) if s[i]]
def add(a,b,p):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def mul(a,b,p):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def power(a,n,p):
    z=(1,0)
    while n:
        if n&1:z=mul(z,a,p)
        a=mul(a,a,p);n//=2
    return z
def hp(p,t):
    r=(p-1)//2;a=(-3*pow(2,-1,p)*(3*t+5))%p;b=(-9*t-7)%p;out=0
    for i in range(r+1):
        j=2*r-3*i;k=r-i-j
        if j>=0 and k>=0:
            out=(out+comb(r,i)*comb(r-i,j)*pow(a,j,p)*pow(b,k,p))%p
    return out
def leg_base(p,t):
    n=(p-3)//4;a,b=1,t%p
    if n==0:return 1
    for k in range(1,n):a,b=b,((2*k+1)*t*b-k*a)*pow(k+1,-1,p)%p
    return b
def hasse_f2(p):
    n=(p-3)//4;r=(p-1)//2
    a=(-15*pow(2,-1,p)%p,(-3)%p);b=((-7)%p,(-6)%p);val=(0,0)
    for i in range(n+1,(2*r)//3+1):
        j=2*r-3*i;k=r-i-j
        assert j>=0 and k>=0
        z=mul(power(a,j,p),power(b,k,p),p)
        c=comb(r,i)*comb(r-i,j)
        val=add(val,(c*z[0],c*z[1]),p)
    return val
def leg_f2(p):
    n=(p-3)//4;t=(0,2*pow(3,-1,p)%p);a=(1,0);b=t
    for k in range(1,n):
        z=mul((2*k+1,0),mul(t,b,p),p)
        z=add(z,(-k*a[0],-k*a[1]),p)
        a,b=b,mul((pow(k+1,-1,p),0),z,p)
    return b
def f_at_9(p):
    m=(p-3)//8;u=s=1
    for r in range(1,m+1):
        u=u*(r-1-m)**2*9*pow((2*m+r+1)*r,-1,p)%p;s=(s+u)%p
    return s
def check():
    total=0
    for p in [7,11,19,23,43,67,83]:
        ch=1 if pow(-6%p,(p-1)//2,p)==1 else -1
        for t in range(p):
            assert leg_base(p,t)==ch*hp(p,t)%p,(p,t);total+=1
    tested=[]
    for p in primes(2001):
        if p<11 or p%8!=3:continue
        ch=1 if pow(-6%p,(p-1)//2,p)==1 else -1
        h=hasse_f2(p);L=leg_f2(p)
        assert h[1]==L[1]==0 and L[0]==ch*h[0]%p
        m=(p-3)//8;f=f_at_9(p);D=comb(3*m+1,m)%p
        assert D and D*f%p==pow(9,m,p)*L[0]%p
        if p%24==19:assert f==L[0]==h[0]==0
        else:assert p%24==11 and f!=0 and h[0]!=0
        tested.append(p)
    print('PASS_GH32_SUN_POLYNOMIAL',total)
    print('PASS_GH32_CM24_HASSE_F',len(tested),'inert',sum(p%24==19 for p in tested),'split',sum(p%24==11 for p in tested))
if __name__=='__main__':check()
