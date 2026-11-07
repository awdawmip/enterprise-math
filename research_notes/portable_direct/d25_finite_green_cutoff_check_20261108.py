"""Exact rational finite Green cutoff and reciprocal Gauss tests."""
from fractions import Fraction
from math import comb

def add(a,b):
    z=dict(a)
    for k,v in b.items():z[k]=z.get(k,0)+v
    return {k:v for k,v in z.items() if v}
def mul(a,b):
    z={}
    for i,x in a.items():
        for j,y in b.items():z[i+j]=z.get(i+j,0)+x*y
    return {k:v for k,v in z.items() if v}
def sc(a,x):return {k:v*x for k,v in a.items() if v*x}
def D(a):return {k:k*v for k,v in a.items() if k*v}
def check(m):
    q={-i:Fraction(comb(m,i)*comb(2*m,i),2**i) for i in range(m+1)}
    c={1:Fraction(1,10)}
    for r in range(1,m):
        c[r+1]=c[r]*Fraction(36*r*r,(6*r+5)*(3*r+2))
    W=q; F=c; P=6*m+1
    L=lambda y:add(add(sc(D(D(y)),18),sc(mul({1:1},D(D(y))),-36)),
                   add(sc(D(y),-9),y))
    assert not add(L(F),{1:-1,m+1:36*m*m*c[m]})
    assert not add(add(L(W),sc(add(sc(D(W),9),sc(W,-2)),P)),sc(W,P*P))
    J=add(mul(W,D(F)),sc(mul(F,D(W)),-1))
    lhs=add(add(sc(D(J),18),sc(mul({1:1},D(J)),-36)),sc(J,-9))
    rhs=add(add(mul(W,{1:1,m+1:-36*m*m*c[m]}),
                sc(mul(F,add(sc(D(W),9),sc(W,-2))),P)),sc(mul(F,W),P*P))
    assert lhs==rhs
    return (m,len(lhs))
if __name__=='__main__':
    print([check(m) for m in (1,2,3,7,11,62)])
    print('PASS: finite forcing, reciprocal Hasse and full Laurent Green')
