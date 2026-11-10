#!/usr/bin/env python3
"""Exact lawful 10-edge contact on the R5 11-edge physical sheet.
Requires sibling VERIFY_11.py; exact SymPy rationals and full 21-row check.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as S

source=Path(__file__).with_name('VERIFY_11.py')
ctx={}
with redirect_stdout(StringIO()):
    exec(compile(source.read_text(), str(source), 'exec'), ctx)
K=S.Matrix.hstack(*ctx['K11'])
direction=K*S.Matrix([-2,-2,-2,0,0])
C,D,T=ctx['C'],ctx['D'],ctx['T']
M11,weights=ctx['M11'],ctx['weights']
A,phys11=ctx['A'],ctx['phys11']
support,q11=ctx['support'],ctx['q']
weights_slope=M11.gauss_jordan_solve(T*direction)[0]
assert weights_slope[6]<0 and support[6]==(5,5)
step=weights[6]/(-weights_slope[6])
z10=ctx['z11']+step*direction
q10=q11+step*T*direction
w10=weights+step*weights_slope
phys10=phys11+step*A*direction
assert [support[i] for i,a in enumerate(w10) if a==0]==[(5,5)]
assert [i for i,a in enumerate(phys10) if a==0]==[4,15,19,21,23]
assert all(a>=0 for a in w10) and all(a>=0 for a in phys10)
E10=tuple(e for e in support if e!=(5,5))
M10=C[:,[D.index(e) for e in E10]]
x10=S.Matrix([w10[i] for i,e in enumerate(support) if e!=(5,5)])
assert M10.rank()==10 and M10*x10==q10 and all(a>0 for a in x10)
p10=tuple(ctx['F'](a) for a in S.Matrix(ctx['p'])+ctx['P']*(ctx['tstar']+z10))
assert ctx['restrictions'](p10)==(ctx['F'](0),)*5
C21=S.Matrix.hstack(*(ctx['edgecol'](e) for e in E10))
assert C21*x10==S.Matrix(ctx['rhs'](p10))  # all original 21 equations

# Eight previously published rational forcing vectors remain strictly positive,
# certified anew against all 30 columns at this exact 10-edge contact.
F8=tuple(e for e in ctx['F9'] if e!=(5,5))
assert set(F8).issubset(ctx['DUAL'])
forced={}
for e in F8:
    y=S.zeros(15,1)
    for item in ctx['DUAL'][e].split():
        row,value=item.split(':');y[int(row)]=S.Rational(value)
    assert all((y.T*C[:,k])[0]<=int(D[k]==e) for k in range(30))
    lower=(y.T*q10)[0]
    assert lower>0
    forced[e]=lower

# A <=9-edge solution must include all 8 forced edges and <=1 of the
# remaining 22. Exhaust all 22 singleton quotient supports exactly.
other=tuple(e for e in D if e not in F8)
CF8=C[:,[D.index(e) for e in F8]]
assert CF8.rank()==8
L8=S.Matrix.vstack(*(u.T for u in CF8.T.nullspace()))
assert L8.shape==(7,15)
V=L8*C[:,[D.index(e) for e in other]]
qb=L8*q10
assert all(V[:,[i]].row_join(qb).rank()>V[:,[i]].rank() for i in range(22))
# Ten-column 15-row annihilator has five dimensions, but only four
# independent pulled-back constraints on the eight physical parameters.
N10=S.Matrix.vstack(*(u.T for u in M10.T.nullspace()))
assert N10.shape==(5,15) and (N10*T).rank()==4
assert N10*q10==S.zeros(5,1)
for k in (N10*T).nullspace():
    assert M10.row_join(T*k).rank()==10
print('CONTACT_DIRECTION_COEFFS',(-2,-2,-2,0,0))
print('CONTACT_STEP',step)
print('CONTACT_Z10',tuple(z10))
print('TEN_POSITIVE_EDGES',E10)
print('PHYSICAL_SLACK_ZEROS',[i for i,a in enumerate(phys10) if a==0])
print('MIN_POSITIVE_EDGE_MASS',min(x10))
print('MIN_POSITIVE_PHYSICAL_SLACK',min(a for a in phys10 if a>0))
print('MIN_POSITIVE_FORCED_BOUND',min(forced.values()))
print('FORCED_ARCS',len(forced),'EXHAUSTIVE_ONE_EXTRA_EXCLUSIONS',len(other))
print('TEN_SUPPORT_RANK',M10.rank(),'PHYSICAL_PULLBACK_RANK',(N10*T).rank(),'LOCAL_MINIMUM_TEN_DIMENSION',4)
print('PASS_LAWFUL_EXACT_MINIMAL_10_ARCS_AND_LOCAL_4D_STRATUM')
