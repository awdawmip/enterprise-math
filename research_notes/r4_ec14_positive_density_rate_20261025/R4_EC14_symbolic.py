#!/usr/bin/env python3
"""Independent exact Laurent-grade generating-function certificates for R4-EC14."""
import sympy as sp
from R4_EC14_verify import STATES, TRANS, LOOKUP

def run():
    x,u=sp.symbols('x u')
    M=sp.zeros(8)
    for i,k,j,bit in TRANS:
        M[k,i]+=u**j
    v=sp.zeros(8,1);v[LOOKUP[(0,0,1)],0]=1
    Delta=1-(1+u)*x+2*u**2*x**4-u**3*x**6
    N=(1-u*x**2)*(1-u*x**3)
    K=1+u*x**2
    A=u*x-1;B=u*x**3+x-1;E=u**2*x**5-u*x**3-x+1
    H=sp.Matrix((-u*x**4*A,A*B,-u*x**3*A,u*x**2*E,
               -x**2*A,u*x*E,x*A*B,-u**2*x**5*A))
    residual=(sp.eye(8)-x*M)*H-K*Delta*v
    assert all(sp.expand(r)==0 for r in residual), [sp.expand(r) for r in residual]
    assert sp.expand(sum(H)-K*N)==0
    assert sp.cancel(Delta.subs({x:u*x,u:1/u},simultaneous=True)-Delta)==0
    L=(1+sp.sqrt(5))/2
    P=lambda l,t: l**6-(1+t)*l**5+2*t**2*l**2-t**3
    assert sp.simplify(P(L,1))==0
    PU=-L**5+4*L**2-3
    PL=6*L**5-10*L**4+4*L
    assert sp.simplify(-PU/(L*PL)-sp.Rational(1,2))==0
    # Analytic implicit eigenvalue λ(u)=1+u−2u²+7u³+O(u⁴).
    # This and α(u)=u∂_u log λ(u) yield I(α)=2α²+O(α³).
    s=sp.symbols('s')
    guess=1+s-2*s*s+7*s**3
    assert sp.series(P(guess,s),s,0,4).removeO().expand()==0
    print('PASS: 8-state polynomial certificate, Δ reciprocity, golden-ratio center, low-u λ expansion')

if __name__=='__main__':run()
