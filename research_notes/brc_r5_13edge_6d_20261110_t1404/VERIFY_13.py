#!/usr/bin/env python3
"""Exact, replayable R5 13-edge witness and six-dimensional stratum.

Requires immutable predecessor research_notes/brc_r5_two_facet_20261110_t1140/VERIFY.py.
All proof-bearing checks use rational/integer arithmetic (SymPy & Fraction).
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sympy as S

root=Path(__file__).resolve().parent.parent
parent=root/'brc_r5_two_facet_20261110_t1140'/'VERIFY.py'
context={}
exec(compile(parent.read_text(),str(parent),'exec'),context)
p,P,tstar,center,A=(context[k] for k in ('p','P','tstar','center','A'))
restriction,mass=context['restrictions'],context['mass']
R=S.Rational(49948501046391,3920403670319950000)
zc=R*S.Matrix([-1,1,1,-1,-1,-1,-1,1])
n=S.Matrix([34101,-293725,-85599,42525,937899,293725,85599,-3287440])
ratios=tuple(F(t) for t in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
def rhs(u):
    mu,nu=mass(u[7:]),mass(u[:7])
    return mu+nu+tuple(ratios[j]*nu[j] for j in range(7))
E=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
force=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
other=tuple(e for e in E if e not in force)
basis14=force+((2,1),(3,2),(0,3),(1,5))
basis13=basis14[:-1]
rows=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edge_column(e):
    i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=ratios[i]
    return S.Matrix(v)
C21=S.Matrix.hstack(*(edge_column(e) for e in E))
C=S.Matrix([[C21[i,j]*(20 if i>=14 else 1) for j in range(30)] for i in rows])
CF=C[:,[E.index(e) for e in force]]
assert CF.rank()==10 and C.rank()==15
qbase=S.Matrix([rhs(tuple(F(v) for v in p))[i]*(20 if i>=14 else 1) for i in rows])
T0=context['jac'](rhs)*P
T=S.Matrix([[T0[i,k]*(20 if i>=14 else 1) for k in range(8)] for i in rows])
def q(z):return qbase+T*(tstar+z)

# Exact contact on the previous interior seven-dimensional 14-edge wall.
mu0=(center+A*zc)[19]
alpha=S.Rational(4*3287440,13*293725)*mu0
z13=zc-S.Matrix([0,0,0,0,0,alpha,0,S.Rational(293725,3287440)*alpha])
m=A[19,:]
assert (n.T*(z13-zc))[0]==0 and (m*z13)[0]==0
assert S.Matrix.vstack(n.T,m).rank()==2
M14=C[:,[E.index(e) for e in basis14]]
w14=M14.gauss_jordan_solve(q(z13))[0]
assert M14.rank()==14 and M14*w14==q(z13)
assert w14[-1]==0 and all(v>0 for v in w14[:13,:])
assert C21[:,[E.index(e) for e in basis13]]*w14[:13,:]==S.Matrix(rhs(tuple(F(v) for v in (S.Matrix(p)+P*(tstar+z13)))))
assert restriction(tuple(F(v) for v in (S.Matrix(p)+P*(tstar+z13))))==(F(0),)*5
phys=center+A*z13
assert all(v>=0 for v in phys)
assert [i for i,v in enumerate(phys) if v==0]==[4,15,19,23]

# Exact 15-row dual vectors; each C^T*y <= e_edge with y^T*q > 0.
# The vectors were located numerically but all mathematical checks here are exact.
DUAL={
 (0,0):'7:1',
 (0,1):'1:-5/13 8:15/13 12:-1/13',
 (0,2):'1:-5/9 2:-5/18 9:10/9 13:-1/18',
 (2,2):'0:-18/5 1:-2 7:18/5 8:54/13 9:4 12:-18/65 13:-1/5',
 (3,3):'0:-36/5 1:-4 2:-2 7:36/5 8:8 9:8 10:5 12:-2/5 13:-2/5 14:-1/5',
 (4,3):'0:-69/10 1:-9/2 2:-3 3:-2 7:69/10 8:15/2 9:15/2 10:6 12:-3/10 13:-3/10 14:-1/5',
 (4,5):'0:-18/5 1:-2 2:-1 4:1 7:18/5 8:4 9:4 10:4 12:-1/5 13:-1/5 14:-1/5',
 (5,5):'0:-23/5 1:-3 2:-2 3:-1 5:1 7:23/5 8:5 9:5 10:5 12:-1/5 13:-1/5 14:-1/5',
 (6,5):'0:-36/13 1:-28/13 2:-23/13 3:-18/13 4:-1 5:-1 7:36/13 8:38/13 9:38/13 10:38/13 11:1 12:-1/13 13:-1/13 14:-1/13',
 (6,6):'0:2/25 2:3/5 3:4/5 4:1 5:1 6:1 7:-2/25 11:-1 12:-1/25 13:-1/25 14:-1/25'
}
assert set(DUAL)==set(force)
bounds={}
for e,tokens in DUAL.items():
    y=S.zeros(15,1)
    for term in tokens.split():
        i,v=term.split(':');y[int(i)]=S.Rational(v)
    assert all((y.T*C[:,k])[0]<=int(E[k]==e) for k in range(30)),e
    low=(y.T*q(z13))[0]
    assert low>0,e
    bounds[e]=low

# Forced ten + two extra arcs gives at most twelve; exclude all 190 pairs.
L=S.Matrix.vstack(*(v.T for v in CF.T.nullspace()))
assert L.shape==(5,15)
V=L*C[:,[E.index(e) for e in other]]
qr=L*q(z13)
hist={}
for i,j in combinations(range(20),2):
    B=V[:,[i,j]]
    rank=B.rank();hist[rank]=hist.get(rank,0)+1
    assert B.row_join(qr).rank()>rank,(i,j)
assert hist=={1:3,2:187}

# The 13-column basis remains solvable on a codimension-two affine 6D sheet.
M13=C[:,[E.index(e) for e in basis13]]
assert M13.rank()==13
K=S.Matrix.vstack(n.T,m).nullspace()
assert len(K)==6
assert all(M13.row_join(T*v).rank()==13 for v in K)
print('CONTACT_ALPHA',alpha)
print('CONTACT_Z13',tuple(z13))
print('EXACT_13_EDGE_SUPPORT',basis13)
print('MIN_13_EDGE_MASS',min(w14[:13,:]))
print('MIN_NONSTRUCTURAL_PHYSICAL_SLACK',min(phys[i] for i in range(26) if i not in (4,15,19,23)))
print('MIN_FORCED_DUAL_BOUND',min(bounds.values()))
print('FORCED_DUAL_CERTIFICATES_PASS',len(bounds))
print('ALL_12_OR_LESS_SUPPORTS_EXCLUDED_BY_190_PAIRS',hist)
print('OBSERVATION_SHEET_DIMENSION',len(K),'RANK_13',M13.rank())
print('PASS_EXACT_PHYSICAL_13_EDGE_MINIMAL_AND_LOCAL_6D_STRATUM')
