#!/usr/bin/env python3
"""Symbolic epsilon family on fixed 16 supports with exact Bernstein positivity certificates."""
from fractions import Fraction as F
from itertools import product
from math import comb
from collections import Counter
import sympy as S
import VERIFY as V
E=S.Symbol('eps', real=True, positive=True)
e0=S.Rational(1,100000)
tau=S.Rational(3,4)+E/4
orig=V.SEEDS.splitlines()[0].split()
C=Counter();bad=[];proof=[]
U=S.Symbol('u', real=True)

def bernstein_positive(expr,name):
    expr=S.cancel(expr)
    a,b=S.fraction(expr)
    aval=a.subs(E,e0/2); bval=b.subs(E,e0/2)
    if not bval>0:
        a=-a;b=-b
    assert S.factor(b.subs(E,e0))>0, (name,'endpoint denominator')
    for label,f in [('numerator',a),('denominator',b)]:
        P=S.Poly(f.subs(E,e0*U),U)
        coeff=[P.nth(k) for k in range(max(0,P.degree())+1)]
        n=len(coeff)-1
        bcs=[S.factor(sum(coeff[k]*S.Rational(comb(i,k),comb(n,k)) for k in range(i+1))) for i in range(n+1)]
        C['max_bernstein_degree']=max(C['max_bernstein_degree'],n)
        C['polynomials_checked']+=1
        if not all(bc>=0 for bc in bcs):
            bad.append((name,label,n,bcs,expr))
        if all(bc==0 for bc in bcs):
            if label=='denominator':bad.append((name,'zero-denom',expr))
        proof.append((name,label,[str(v) for v in bcs]))

def solve_symbolic(x,seed):
    ss,sep,freeze=seed.partition('~')
    support=[V.ALPHABET.index(c) for c in ss]
    rows,rhs=V.build_system(x,tau)
    A=S.Matrix([[S.sympify(row[i]) for i in support] for row in rows]);b=S.Matrix([S.sympify(v) for v in rhs])
    if sep:
        col,sval=freeze.split(':',1)
        val=S.Rational(sval);base=S.Rational(21,80) if col=='r' else S.Rational(0)
        val=base+(val-base)*(E/e0)
        A=A.col_join(S.Matrix([[S.Integer(int(i==support.index(V.ALPHABET.index(col)))) for i in range(len(support))]]))
        b=b.col_join(S.Matrix([val]))
    ans=list(S.linsolve((A,b)))
    assert len(ans)==1
    sol=ans[0];assert not any(z.free_symbols-{E} for z in sol)
    vals={i:S.cancel(z) for i,z in zip(support,sol)}
    yy=V.target([vals.get(i,S.Integer(0)) for i in range(49,54)],tau)
    return vals,yy

for idx,(key,seed) in enumerate(zip(product((E/10,E),(S.Integer(0),S.Integer(1)),(S.Integer(0),S.Integer(1)),(S.Rational(3,4),S.Integer(1))),orig)):
    xx=V.source(*key)
    vals,yy=solve_symbolic(xx,seed)
    for i,z in vals.items():
        bernstein_positive(z,f'vertex {idx} variable {i}')
    g,a,b,u,v,w,z=yy
    for label,expr in [('g',g),('1-g',1-g),('a',a),('g-a',g-a),('b',b),('g-b',g-b),('u',u),('ucap-u',S.Rational(13,40)*a+b/80-u),('w',w),('wcap-w',S.Rational(3,40)*a+S.Rational(21,80)*b-w)]:
        bernstein_positive(expr,f'vertex {idx} {label}')
    Mx=V.masses(xx); My=V.masses(yy)
    for i in range(7):
        assert S.cancel(sum(vals.get(7*i+j,0) for j in range(7))-My[i])==0
    for j in range(7):
        assert S.cancel(sum(vals.get(7*i+j,0) for i in range(7))-Mx[j])==0
        assert S.cancel(sum(V.R[i]*vals.get(7*i+j,0) for i in range(7))-V.R[j]*Mx[j])==0
    for aa,bb in zip(V.stops(xx),V.stops(yy)):
        assert S.cancel(aa-bb)==0
    assert S.cancel(9*b*z-4*a*(v-z))==0
    print('vertex',idx,'symbolic equalities PASS',len(vals),'nonzero variables; positivity polynomials checked',C['polynomials_checked'],flush=True)
assert not bad, bad[:10]
print('PASS_UNIFORM_SYMBOLIC_16_VERTICES',16)
print('PASS_EXACT_BERNSTEIN_POSITIVITY_POLYNOMIALS',C['polynomials_checked'],'MAX_DEGREE',C['max_bernstein_degree'])
print('PASS_ALL_REAL_0_LT_EPS_LE_1_OVER_100000', 'AND_T_IN_EPS_OVER_10_TO_EPS')
