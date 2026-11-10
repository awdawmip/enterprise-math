#!/usr/bin/env python3
"""Exact lawful 13-edge Blackwell couplings on the mu1=0 contact of the R5 14-edge sheet.
Uses the local standalone VERIFY_FACE.py; all arithmetic is exact rational.
Proves existence of 12 distinct positive 13-edge supports, NOT their global optimality.
"""
from pathlib import Path
from runpy import run_path
from fractions import Fraction as F
from itertools import product
import sympy as S
q=run_path(str(Path(__file__).with_name('VERIFY_FACE.py')))
normal=S.Matrix([q['normal']])
tangent=S.Matrix([-S.Rational(11579,421),0,0,0,1,0,0,0])
assert (normal*tangent)[0]==0
zc=q['zc']; p=q['p']; P=q['P']; tstar=q['tstar']; C=q['C']; D=q['D']
base=S.Matrix(p)+P*(tstar+zc)
mu1=q['mass'](tuple(F(v) for v in base)[7:])[1]
assert mu1==S.Rational(16932541854726549,313632293625596000000)>0
z13=zc+mu1*tangent
physical=S.Matrix(p)+P*(tstar+z13)
slacks=q['phys'](tuple(F(v) for v in physical))
assert all(s>=0 for s in slacks)
assert [i for i,s in enumerate(slacks) if s==0]==[4,15,19,23]
assert q['restrictions'](tuple(F(v) for v in physical))==(F(0),)*5
assert q['mass'](tuple(F(v) for v in physical)[7:])[1]==0
b=q['hsc']+q['T']*(tstar+z13)
seen=set();mins=[]
for choice in product(*q['choice_groups']):
    support=q['FSET']+tuple(choice)+(q['common'],)
    M=C[:,[D.index(e) for e in support]]
    w,params=M.gauss_jordan_solve(b)
    assert params.rows==0
    assert w[-1]==0 and all(v>0 for v in w[:-1]),(choice,list(w))
    full=S.Matrix.hstack(*(q['edgecol'](e) for e in support))
    assert full*w==S.Matrix(q['rhs'](tuple(F(v) for v in physical)))
    s13=tuple(e for e,v in zip(support,w) if v>0)
    assert len(s13)==13 and s13 not in seen
    seen.add(s13);mins.append(min(v for v in w if v>0))
assert len(seen)==12
print('CONTACT_NORMAL',tuple(q['normal']))
print('TANGENT',tuple(tangent))
print('PARAMETER_STEP',mu1)
print('TARGET_MARGINAL_mu1',q['mass'](tuple(F(v) for v in physical)[7:])[1])
print('ZERO_PHYSICAL_SLACK_INDICES',[i for i,v in enumerate(slacks) if v==0])
print('MIN_POSITIVE_PHYSICAL_SLACK',min(v for v in slacks if v>0))
print('EXACT_DISTINCT_13_ARC_SUPPORTS',len(seen))
print('MIN_POSITIVE_13_ARC_WEIGHT',min(mins))
print('FULL_21_MARGINAL_MARTINGALE_EQUATIONS_FOR_EACH',True)
print('SAMPLE_SUPPORT',next(iter(sorted(seen))))
print('PASS_EXACT_LAWFUL_13_ARC_CONTACT_CONSTRUCTION')
