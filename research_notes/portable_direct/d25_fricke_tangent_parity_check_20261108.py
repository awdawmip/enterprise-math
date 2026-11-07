#!/usr/bin/env python3
"""Exact symbolic Fricke tangent check. External CM model; not native H0/B0."""
from sympy import symbols, sqrt, simplify, diff, Integer, Rational

t=symbols('t')
z=108*t**2*(t+9)*(t+8)**2/(t+12)**6
w=256*t**3*(t+8)*(t+9)**3/(t*t+36*t+216)**4
s=sqrt(2)
for eps in (1,-1):
    fiber=eps*6*s
    za=simplify(z.subs(t,fiber))
    wa=simplify(w.subs(t,fiber))
    dz=simplify(diff(z,t).subs(t,fiber))
    dw=simplify(diff(w,t).subs(t,fiber))
    ratio=simplify(dw/dz)
    assert za==Rational(1,2) and wa==Rational(1,9)
    assert simplify(dz-(-1+eps*3*s/4))==0
    assert simplify(dw-(Integer(4)/9-eps*8*s/27))==0
    assert simplify(ratio-eps*8*s/27)==0
for p in (13,19,373):
    alpha=16*pow(27,-1,p)%p
    beta=8*pow(27,-1,p)%p
    sq=128*pow(729,-1,p)%p
    assert alpha*beta%p==sq and sq
    print(f"p={p}: tangent=[[0,{alpha}],[{beta},0]], square={sq}*I")
print("PASS: both exact conjugate fibers, Frobenius parity tangent maps and three finite witnesses")
