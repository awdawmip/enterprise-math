#!/usr/bin/env python3
"""R371 exact signed-K3 corank-3 phase theorem; SymPy rational/Sturm proof.
Run inside Enterprise Math PR #1592 checkout; uses existing R369/R346 code.
"""
from pathlib import Path
from sympy import Symbol, Poly, Rational, oo, expand
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
from R369_check import compute_rows,fd
x=Symbol('theta')
q=lambda a:Rational(a,1000)
def roots(f,a,b):return int(Poly(f,x).count_roots(a,b))
def negative(f,z):return bool(expand(f).subs(x,z)<0)
def positive(f,z):return bool(expand(f).subs(x,z)>0)
def main():
    rows,D=compute_rows(x,4)
    c=list(map(expand,rows[3]))
    # Verify every coefficient directly against seven original D determinants.
    v=[]
    for i in range(7):
        k=i+1;n=3+k
        m=expand(D(n,k)*D(n+1,k+1)-D(n,k+1)*D(n+1,k))
        v.append(expand(Rational(5)**(5-2*k)*m))
    assert all(expand(a-b)==0 for a,b in zip(c,fd(v)))
    T=[expand(c[j]**2-c[j-1]*c[j+1]) for j in range(1,6)]
    U=expand(5*c[1]**2-12*c[0]*c[2])
    assert [Poly(f,x).degree() for f in c]==[4,5,6,6,6,6,6]
    assert all(positive(f,0) and roots(f,-1,q(1232))==0 for f in c+T[1:])
    assert negative(U,0) and roots(U,-1,q(1232))==0
    # sigma3, the unique Turan root before rho1, has bracket (1.231,1.232).
    assert positive(T[0],q(1231)) and negative(T[0],q(1232))
    assert roots(T[0],q(1231),q(1232))==1
    assert roots(T[0],-1,q(1461))==1
    assert roots(T[0],q(1232),q(1461))==0
    # rho1, the first zero of c1, has bracket (1.460,1.461).
    assert positive(c[1],q(1460)) and negative(c[1],q(1461))
    assert roots(c[1],q(1460),q(1461))==1
    assert roots(c[1],-1,q(1461))==1
    # Beyond rho1 a negative coefficient covers every remaining parameter.
    cover=[(c[1],q(1461),Rational(11,5)),
           (c[3],Rational(11,5),Rational(221,100)),
           (c[4],Rational(221,100),Rational(37,10)),
           (c[2],Rational(37,10),Rational(5)),
           (c[1],Rational(5),oo)]
    for f,l,r in cover:
        assert roots(f,l,r)==0 and negative(f,l)
        if r!=oo:assert negative(f,r)
    assert negative(U,q(1232))
    assert q(1055)<q(1231)<q(1232)<q(1301) # R370 tau1<sigma3<tau2
    print('R371_EXACT_PASS: 7 raw D equalities; 7 coefficients; 5 Turan; 1 ULC; 5 negative-sign cover intervals')
    print('PF2 iff -1<theta<=sigma3 (T1 unique root in 1.231..1.232); PF-infinity never')
if __name__=='__main__':main()
