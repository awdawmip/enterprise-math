#!/usr/bin/env python3
"""Exact author-side finite-field certificates for D25 GH-13/GH-14; stdlib only."""
from math import comb

def norm(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def add(a,b,p):
    return norm([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p
                 for i in range(max(len(a),len(b)))])
def neg(a,p): return [(-x)%p for x in a]
def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return norm(c)
def scale(a,k,p): return norm([(k*x)%p for x in a])
def shift(a,n,p):
    c=[0]*len(a)
    for i,x in enumerate(a):
        for j in range(i+1):c[j]=(c[j]+x*comb(i,j)*pow(n,i-j,p))%p
    return norm(c)
def division(a,b,p):
    a=norm(a[:]);b=norm(b[:]);q=[0]*max(1,len(a)-len(b)+1)
    inv=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b); k=a[-1]*inv%p;q[j]=k
        for i,t in enumerate(b):a[j+i]=(a[j+i]-k*t)%p
        norm(a)
    return norm(q),a
def gcd(a,b,p):
    while b!=[0]: a,b=b,division(a,b,p)[1]
    return scale(a,pow(a[-1],-1,p),p)
def ev(a,x,p):
    out=0
    for v in reversed(a):out=(out*x+v)%p
    return out
def resolvent(p):
    A=[9%p,108%p,432%p,576%p]
    B=[24%p,104%p,144%p,64%p]
    aa=[shift(A,j,p) for j in range(p-1)]
    bb=[shift(B,j,p) for j in range(p-1)]
    suffix=[[1] for _ in range(p)]
    for j in range(p-2,-1,-1):suffix[j]=mul(bb[j],suffix[j+1],p)
    numerator=[0];prefix=[1]
    for j in range(p):
        numerator=add(numerator,mul(mul(prefix,[(8*j+1)%p,8%p],p),suffix[j],p),p)
        if j<p-1:prefix=mul(prefix,aa[j],p)
    numerator=scale(numerator,pow(8,-1,p),p)
    g=gcd(numerator,suffix[0],p)
    N,r1=division(numerator,g,p); D,r2=division(suffix[0],g,p)
    assert r1==r2==[0]
    lhs=add(add(mul(mul(A,shift(N,1,p),p),D,p),
                neg(mul(mul(B,N,p),shift(D,1,p),p),p),p),
            neg(mul(mul(B,[1,8],p),mul(D,shift(D,1,p),p),p),p),p)
    assert lhs==[0],p
    pa,pb=[1],[1]
    for j in range(p):
        pa=mul(pa,shift(A,j,p),p);pb=mul(pb,shift(B,j,p),p)
    assert pa==scale(pb,9,p),p
    return N,D
def finite_T(p):
    d=(p-1)//4;c=1;total=0
    for r in range(d+1):
        total=(total+(8*r+1)*c)%p
        if r<d:
            v=(4*r+2)*(4*r+3)*(4*r+4)%p
            assert v!=0
            c=c*9*(4*r+1)**3*pow(v,-1,p)%p
    return total
def main():
    ps=[5,7,11,13,17,19,23,29,31,37,41,43,47]
    for p in ps:
        resolvent(p)
        assert finite_T(p)==0 # observations only; not a general proof
    N,D=resolvent(19)
    expected=[1]
    for k in range(5):expected=mul(expected,[(-k)%19,1],19)
    for k in range(1,5):
        f=[k,1];expected=mul(expected,mul(f,f,19),19)
    assert D==expected and len(D)==14 and len(N)==15
    assert N==[12,3,8,13,6,16,1,11,5,15,5,8,0,0,1]
    for k in list(range(5))+list(range(15,19)):
        assert ev(D,k,19)==0 and ev(N,k,19)!=0
    assert [ev(N,k,19) for k in range(5)]==[12,9,5,10,15]
    print("PASS_GH13_FROBENIUS_CYCLIC_IDENTITY",len(ps),"PRIMES")
    print("PASS_GH14_P19_GLOBAL_SOLUTION_POLES_TRUE_RANKS")
if __name__=="__main__":main()
