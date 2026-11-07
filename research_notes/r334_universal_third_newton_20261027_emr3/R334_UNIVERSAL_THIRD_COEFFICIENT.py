#!/usr/bin/env python3
"""Symbolic exact rational certificate for the all-r third-from-top BRC Newton coefficient.

Relies on the explicitly conditional author-side R330 coefficient-extraction lemma.
Constructs low Taylor coefficients directly from complete signed K_i/J_s sources.
"""
from __future__ import annotations
import argparse
import json
from math import comb
import sympy as s

def C(n,k): return comb(n,k) if 0 <= k <= n else 0

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def monomial(n,coeff,degree):
    return [0]*degree + [coeff*C(n,j) for j in range(n+1)]

def K(i):
    d=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    a=[0]
    for j,v in enumerate(d,1):
        if v:a=add(a,monomial(i+1-j,-v,i-1))
    return a

def J(q):
    a=[0]
    for v,n in ((-C(3,q-1),q),(-C(6,q-1),q-1),(C(8,q-2),q-2)):
        if v:a=add(a,monomial(n,v,q))
    return a

def run():
    y,z=s.symbols('y z');a=s.Rational(4,5)
    X=(1-y)/2;t=y*z
    Ktot=sum(sum(s.Integer(c)*t**k for k,c in enumerate(K(i)))*X**i for i in range(1,13))
    Atot=1+t+sum(sum(s.Integer(c)*t**k for k,c in enumerate(J(i)))*X**i for i in range(1,11))
    KP=s.Poly(s.expand(Ktot),y);AP=s.Poly(s.expand(Atot),y)
    E=[s.factor(-KP.nth(i+1)) for i in range(4)]
    N=[s.factor(AP.nth(i)) for i in range(3)]
    assert s.simplify(E[0]-(1-s.Rational(5,4)*z))==0
    assert s.simplify(E[1]-z)==0
    assert s.simplify(E[2]-z*(11*z*z-16*z+4)/16)==0
    assert s.simplify(E[3]-z*z*(3*z-8)*(3*z-2)/8)==0
    assert N[0]==1 and N[1]==0
    assert s.simplify(N[2]+z*(5*z-2)/2)==0
    assert E[2].subs(z,a)==-s.Rational(11,125)
    assert s.diff(E[2],z).subs(z,a)==-s.Rational(3,100)
    assert E[3].subs(z,a)==-s.Rational(112,625)
    assert N[2].subs(z,a)==-s.Rational(4,5)

    j,r=s.symbols('j r',integer=True,nonnegative=True)
    p=lambda v: -1-s.Rational(69,80)*(v-1)
    h=s.factor((4761*j*j-6685*j-9354)/6400)
    h2=s.Rational(-23,40)
    assert s.simplify(h.subs(j,2)-h2)==0
    recur=s.expand(-2*p(j-1)+s.Rational(11,40)*p(j-2)-s.Rational(31,40))
    assert s.simplify(h-h.subs(j,j-1)-recur)==0
    base=s.Rational(25,8)*N[2].subs(z,a)+2+s.Rational(5,2)*s.diff(E[2],z).subs(z,a)
    assert base==h2
    for jj in range(2,9):
        # Higher E_l (l>=4) have a zero of order >=3 at the pole;
        # higher N_j (j>=3) likewise do not affect derivatives up to order 2.
        g=[s.Integer(1)]
        for k in range(1,jj+1):
            Nk=N[k] if k<len(N) else s.Integer(0)
            gk=s.expand(Nk*E[0]**k-sum(E[ell]*g[k-ell]*E[0]**(ell-1) for ell in range(1,min(k,3)+1)))
            g.append(gk)
        assert s.simplify(s.diff(g[jj],z,2).subs(z,a)-(-a)**(jj-2)*h.subs(j,jj))==0

    n=r-j
    T=s.factor(j*(j+1)/2 - j*n/2 - n*(n-1)/4)
    Sconst=s.factor(j*(j+1)*(2*j+1)/6 + (n*j*j+j*n*(n-1)+n*(n-1)*(2*n-1)/6)/4)
    W=s.factor(T*T-Sconst-2*j*(j-T)*p(j)+j*(j-1)*h)
    residual=s.expand(W)
    falling=[]
    for k in range(4,-1,-1):
        ck=s.Poly(residual,j).nth(k)
        falling.append((k,s.factor(ck)))
        residual=s.expand(residual-ck*s.prod(j-i for i in range(k)))
    assert residual==0
    Ew=s.factor(sum(ck*s.prod(r-i for i in range(k))*s.Rational(-2,3)**k for k,ck in falling))
    assert s.simplify(Ew-r*(r-1)*(243*r*r-95*r-3542)/2700)==0

    # H_r(q-r) leading q coefficients, scaled by 6**r/r!.
    L=s.Integer(1)
    A=-s.Rational(3,10)*r*(r-1)
    B=s.factor(Ew/2)
    P=s.factor(r*r*L+A)
    R=s.factor(s.binomial(r,2)*r*r*L+r*(r-1)*A+B)
    Srr2=s.binomial(r,3)+3*s.binomial(r,4)
    Cscaled=s.factor(s.expand_func(R+s.binomial(r-1,2)*P+Srr2*L))
    claimed=s.factor(r*(r-1)*2*(243*r*r-245*r-182)/675)
    assert s.simplify(Cscaled-claimed)==0
    return {
      'schema':'R334_UNIVERSAL_NEWTON_ANTEPENULTIMATE_SYMBOLIC_V1',
      'status':'PASS',
      'assumption':'R330 Eq.(4) exact rational extraction / deg H_r<=r, author-side',
      'low_order_E':['1-5*z/4','z','z*(11*z**2-16*z+4)/16','z**2*(3*z-8)*(3*z-2)/8'],
      'N2':'-z*(5*z-2)/2',
      'gpp_ratio':'(4761*j**2-6685*j-9354)/6400 for j>=2',
      'third_monomial_coefficient_ratio':'r*(r-1)*(243*r**2-95*r-3542)/5400',
      'universal_newton_coefficient':'c[r,r-2]=2*6**r*(243*r**2-245*r-182)/675 for all integers r>=2',
      'lower_bound_polynomial_at_r2':'300',
      'signed_convolution_falling_terms':[[k,str(ck)] for k,ck in falling],
      'arithmetic':'SymPy exact rationals / polynomial identities',
      'role':'AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED'
    }

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',default='R334_SYMBOLIC_EVIDENCE.json')
    arg=parser.parse_args()
    result=run()
    with open(arg.out,'w',encoding='utf8') as fh:
        json.dump(result,fh,ensure_ascii=False,indent=2);fh.write('\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
