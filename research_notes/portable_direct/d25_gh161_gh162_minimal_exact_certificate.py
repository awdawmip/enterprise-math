#!/usr/bin/env python3
"""Exact, dependency-free p3347 signed Psi-trace certificate; author-side only."""
from math import comb
p=3347
Z=(0,0); I=(1,0)
def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def neg(a): return ((-a[0])%p,(-a[1])%p)
def sub(a,b): return add(a,neg(b))
def mul(a,b): return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def scale(a,k): return (a[0]*k%p,a[1]*k%p)
def div(a,b):
    d=(b[0]*b[0]-2*b[1]*b[1])%p
    assert d
    return mul(a,scale((b[0],-b[1]),pow(d,-1,p)))
B=(pow(8,-1,p),pow(12,-1,p))
Bstar=(B[0],-B[1]%p)
u=470
assert u*u%p==p-2

def rhs(x,b=B): return add(add(mul(mul(x,x),x),mul(x,x)),mul(b,x))
def valid(T): return T is None or mul(T[1],T[1])==rhs(T[0])
def opposite(T): return None if T is None else (T[0],neg(T[1]))
def plus(A,C):
    if A is None: return C
    if C is None: return A
    x,y=A; s,t=C
    if x==s:
        if y!=t or y==Z: return None
        slope=div(add(add(scale(mul(x,x),3),scale(x,2)),B),scale(y,2))
    else: slope=div(sub(t,y),sub(s,x))
    xx=sub(sub(sub(mul(slope,slope),I),x),s)
    ans=(xx,sub(mul(slope,sub(x,xx)),y))
    assert valid(ans)
    return ans
def times(T,n):
    if n<0: return times(opposite(T),-n)
    r=None
    while n:
        if n&1:r=plus(r,T)
        T=plus(T,T);n//=2
    return r
def psi(T):
    x,y=T
    x=(x[0],-x[1]%p);y=(y[0],-y[1]%p)
    assert mul(y,y)==rhs(x,Bstar)
    X=add(add(x,I),div(Bstar,x))
    Y=mul(y,sub(I,div(Bstar,mul(x,x))))
    ans=(scale(X,-pow(2,-1,p)),scale(Y,-pow(2*u,-1,p)))
    assert valid(ans)
    return ans
P=((1,0),(1830,2856))
T=((2231,2510),(1662,765))
assert valid(P) and valid(T)
assert times(P,11208516//3)==T and times(T,3) is None
assert psi(T)==opposite(T) and psi(psi(T))==times(T,-2)
# GH-160: Tr(Psi) is +/-160. The mod-3 trace of Psi is 2*(-1)=1.
trace=next(t for t in (-160,160) if t%3==1)
H=(u*pow(2,-1,p)*trace)%p
# Control only: polynomial coefficient is NOT used to select the sign.
N=(p-1)//2;power=I; direct=Z
for j in range(N//2+1):
    direct=add(direct,scale(power,comb(N,j)*comb(N-j,j)))
    power=mul(power,B)
assert direct==(H,0)
print('PASS_GH161_GH162_TORSION_SIGN_MINIMAL',{'u':u,'T':T,'PsiT':psi(T),'tracePsi':trace,'H':H})
