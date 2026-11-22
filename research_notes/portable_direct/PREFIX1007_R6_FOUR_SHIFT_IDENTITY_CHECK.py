#!/usr/bin/env python3
"""Exact formal Laurent/differential identity certificate for PREFIX-1007.

This algebraically reduces eleven PREFIX-1005 marked orbit contributions to
four shifts of A_6(m). It imports its companion finite BRC post-observer
integer checker; SymPy is used only for rational-function polynomial identities.
"""
import json
from collections import defaultdict
from fractions import Fraction
import sympy as sp
from PREFIX1007_R6_COLLISION_HOLONOMIC_REDUCTION import ORBIT_POLYS, marked_a_only_operator, A_independent, marked_from_A

m=sp.symbols('m',integer=True,nonnegative=True)

def factorial_ratio(r,q):
    s=r-q
    first=sp.prod(m-j for j in range(q)) if q>=0 else sp.Integer(1)/sp.prod(m+j for j in range(1,-q+1))
    second=sp.Integer(1)/sp.prod(m+j for j in range(1,s+1))
    return first*second

def derive():
    out=defaultdict(lambda:sp.Integer(0))
    for delta,(a,b,c) in ORBIT_POLYS:
        polynomial=a*(m+4)**2+b*(m+4)+c
        for (r,q),v in marked_a_only_operator(delta).items():
            out[r-q]+=polynomial*sp.Rational(v.numerator,v.denominator)*factorial_ratio(r,q)
    return {k:sp.factor(v) for k,v in sorted(out.items())}

EXPECTED={
    0:6*(36*m+25)**2,
    1:12*(396*m**3+869*m**2+443*m+36)/(m+1),
    2:-2*(141*m**4+614*m**3+418*m**2-827*m-706)/((m+1)*(m+2)),
    3:2*(2*m+3)*(m**2+2*m-6)/(m+2)
}

def run():
    got=derive()
    assert set(got)==set(EXPECTED)
    for k in got:
        assert sp.cancel(got[k]-EXPECTED[k])==0,(k,got[k],EXPECTED[k])
    As=A_independent(70)
    checked=[]
    for n in range(5,51):
        mm=n-4
        rhs=sum(Fraction(int(sp.numer(sp.cancel(got[k].subs(m,mm)))),int(sp.denom(sp.cancel(got[k].subs(m,mm)))))*As[mm+k] for k in got)
        lhs=sum((a*n*n+b*n+c)*marked_from_A(mm,d,As) for d,(a,b,c) in ORBIT_POLYS)
        assert rhs==lhs
        checked.append(n)
    return {'schema':'PREFIX1007_R6_FOUR_SHIFT_SYMBOLIC_IDENTITY_V1',
            'theorem':'For m=n-4>=1, 36^n M^L_(n,1)=C0(m)A6(m)+C1(m)A6(m+1)+C2(m)A6(m+2)+C3(m)A6(m+3).',
            'coefficient_formulas':{str(k):str(sp.factor(got[k])) for k in got},
            'algebra':'SymPy exact rational-function simplification of all 11 PREFIX-1005 Laurent-orbit polynomials through the seven-state Bessel-like differential module; cleared-denominator identities equal zero for all m, not merely sampled',
            'crosschecks_n_first':checked[0],'crosschecks_n_last':checked[-1],
            'crosschecks_count':len(checked),
            'limitation':'Formal polynomial identity for a prior typed BRC terminal observer, not an independent native dynamics run or project Review'}

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
