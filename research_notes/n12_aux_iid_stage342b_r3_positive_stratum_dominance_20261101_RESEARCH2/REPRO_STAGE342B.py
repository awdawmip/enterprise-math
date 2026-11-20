#!/usr/bin/env python3
"""Exact Stage342-B sign/descent checker for a tagged Bernoulli/BRC auxiliary model.
Finite symbolic equalities and rational interval bounds, NOT a native X6 proof.
"""
from fractions import Fraction as F
import sympy as S

W=(1,3,3,1)
M=(61,21,9,9)
lo_x,hi_x=F(21,100),F(6,25)
lo_y,hi_y=F(609,1000),F(2,3)
X,Y=S.symbols('x y')

def B(k,t):return t**k*(1-t)**(3-k)
def r(k,x,y):return (4*B(k,x)+B(k,y))/5-F(M[k],160)
def public(x,y):return F(5,32)*sum(W[k]*abs(r(k,x,y)) for k in range(4))
def dist(a,z):return F(1,2)*sum(W[k]*abs(B(k,a)-B(k,z)) for k in range(4))
def tagged(x,y):return (63*dist(F(1,4),x)+dist(F(3,4),x)+9*dist(F(1,4),y)+7*dist(F(3,4),y))/256

def bern_coeff(fun,z,lo,hi):
    f=S.lambdify(z,fun,'sympy'); df=S.lambdify(z,S.diff(fun,z),'sympy')
    a,b=S.Rational(lo.numerator,lo.denominator),S.Rational(hi.numerator,hi.denominator)
    return (f(a), f(a)+(b-a)*df(a)/3, f(b)-(b-a)*df(b)/3, f(b))

def check():
    xs=S.Rational(lo_x.numerator,lo_x.denominator)
    xe=S.Rational(hi_x.numerator,hi_x.denominator)
    ys=S.Rational(lo_y.numerator,lo_y.denominator)
    ye=S.Rational(hi_y.numerator,hi_y.denominator)
    # r3 >= 0 implies y > 609/1000; this is a global implication on the big R.
    assert r(3,hi_x,lo_y)==-F(87471,5000000000)<0
    # Thus r1<0 and r2>0, by derivative-monotone coordinate bounds.
    assert r(1,hi_x,lo_y)==-F(8649471,5000000000)<0
    assert r(2,lo_x,lo_y)==F(3120471,5000000000)>0
    assert S.simplify(S.diff(r(1,X,Y),X)-S.Rational(4,5)*(1-X)*(1-3*X))==0
    assert S.simplify(S.diff(r(1,X,Y),Y)-S.Rational(1,5)*(1-Y)*(1-3*Y))==0
    assert S.simplify(S.diff(r(2,X,Y),X)-S.Rational(4,5)*X*(2-3*X))==0
    assert S.simplify(S.diff(r(2,X,Y),Y)-S.Rational(1,5)*Y*(2-3*Y))==0
    assert S.simplify(sum(W[k]*r(k,X,Y) for k in range(4)))==0
    # Certify all sixteen *source-labelled* sign comparisons on full strip.
    signs={('x',F(1,4)):(-1,1,1,1),('x',F(3,4)):(-1,-1,1,1),
           ('y',F(1,4)):(1,1,-1,-1),('y',F(3,4)):(-1,-1,-1,1)}
    for (variable,anchor),sg in signs.items():
        v,low,high=(X,xs,xe) if variable=='x' else (Y,ys,ye)
        a=S.Rational(anchor.numerator,anchor.denominator)
        for k,required in enumerate(sg):
            co=bern_coeff(B(k,a)-B(k,v),v,F(low),F(high))
            assert all(required*t>0 for t in co), (variable,anchor,k,co)
    def dtag(v,a,sg):
        aa=S.Rational(a.numerator,a.denominator)
        return S.Rational(1,2)*sum(W[k]*sg[k]*(B(k,aa)-B(k,v)) for k in range(4))
    cx=(63*dtag(X,F(1,4),signs['x',F(1,4)])+dtag(X,F(3,4),signs['x',F(3,4)]))/256
    cy=(9*dtag(Y,F(1,4),signs['y',F(1,4)])+7*dtag(Y,F(3,4),signs['y',F(3,4)]))/256
    assert S.simplify(S.diff(cx,X)+(1-X)*(189-183*X)/256)==0
    assert S.simplify(S.diff(cy,Y)-3*Y*(18-25*Y)/256)==0
    # Derivative margins throughout high-y strip, including outer endpoints.
    assert (1-hi_x)*(F(189)-183*hi_x)/256==F(68913,160000)>0
    assert 3*hi_y*(18-25*hi_y)/256==F(1,96)>0
    assert 3*F(1,4)*(1-hi_x)*(1-3*hi_x)==F(399,2500)>0
    assert F(3,8)*hi_y*(1-hi_y)==F(1,12)>0
    assert F(3,16)*(1-hi_y)*(3*lo_y-1)==F(827,16000)>0
    # all three b-derivatives on their correct smooth sides, no early tag merge
    b0=-S.Rational(15,16)*r(1,X,Y)  # r0>=0, r1<0, r2>0, r3>0
    bm=-S.Rational(5,16)*(r(0,X,Y)+3*r(1,X,Y)) # r0<0, r3>0
    assert S.simplify(S.diff(b0,X)+S.Rational(3,4)*(1-X)*(1-3*X))==0
    assert S.simplify(S.diff(b0,Y)-S.Rational(3,16)*(1-Y)*(3*Y-1))==0
    assert S.simplify(S.diff(bm,Y)-S.Rational(3,8)*Y*(1-Y))==0
    # Actual strict rational witness in the r0<0,r3>0 region.
    x=F(227,1000); ya=F(617,1000); yb=F(6169,10000)
    assert [S.sign(r(k,x,ya)) for k in range(4)]==[-1,-1,1,1]
    assert [S.sign(r(k,x,yb)) for k in range(4)]==[-1,-1,1,1]
    assert public(x,yb)<public(x,ya)<F(61,10000)
    assert tagged(x,yb)<tagged(x,ya)
    print('R3_UPPER_POSITIVE_STRATUM_CERTIFIED=TRUE')
    print('STRIP_Y_LOWER=609/1000')
    print('TAGGED_ATOM_SIGNS=x(1/4):-+++;x(3/4):--++;y(1/4):++--;y(3/4):---+')
    print('CASE_R0_POSITIVE_PUBLIC_X_DECREASE_AT_LEAST=399/2500')
    print('CASE_R0_NEGATIVE_PUBLIC_Y_INCREASE_AT_LEAST=1/12')
    print('CASE_R0_ZERO_PUBLIC_Y_INCREASE_AT_LEAST=827/16000')
    print('COST_DECREASE_X_MARGIN_AT_LEAST=68913/160000')
    print('COST_INCREASE_Y_MARGIN_AT_LEAST=1/96')
    print('WITNESS_START_PUBLIC='+str(public(x,ya)))
    print('WITNESS_FINISH_PUBLIC='+str(public(x,yb)))
    print('WITNESS_START_TAGGED='+str(tagged(x,ya)))
    print('WITNESS_FINISH_TAGGED='+str(tagged(x,yb)))
    print('STAGE342B_R3_POSITIVE_STRATUM_STRICT_PARETO_DOMINANCE_EXACT_PASS')

if __name__=='__main__':check()
