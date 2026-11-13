#!/usr/bin/env python3
"""Exact 14-edge first-contact at the quotient support radius.

Uses VERIFY.py in same directory for the frozen seven-likelihood-ratio model,
then independently reconstructs full Blackwell 21-row equations, a 14-edge
positive rational solution, and all 1140 possible <=13-edge quotient supports.
All arithmetic exact SymPy rationals, no floating-point thresholds.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import sympy as S
root=Path(__file__).parent
loc=globals()
exec(compile((root/'VERIFY.py').read_text(),'VERIFY.py','exec'),loc)
R=loc['rho_certificate']; P=loc['P']; p=loc['p']; star=loc['star'];tstar=loc['tstar']
r=tuple(F(t) for t in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
mass=loc['mass']; jac=loc['jac']
def rhs(u):
    mu,nu=mass(u[7:]),mass(u[:7]); return mu+nu+tuple(r[j]*nu[j] for j in range(7))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in(0,6) or i==j)
FSET=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
OTHER=tuple(e for e in D if e not in FSET)
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(edge):
    i,j=edge;a=[F(0)]*21;a[i]=1;a[7+j]=1;a[14+j]=r[i];return S.Matrix(a)
C=S.Matrix.hstack(*(S.Matrix([edgecol(e)[i]*(20 if i>=14 else 1) for i in I]) for e in D))
FC=C[:,[D.index(e) for e in FSET]]
L=S.Matrix.vstack(*(vec.T for vec in FC.T.nullspace()))
assert FC.rank()==10 and L.shape==(5,15)
V=L*C[:,[D.index(e) for e in OTHER]]
hsc=S.Matrix([rhs(p)[i]*(20 if i>=14 else 1) for i in I])
B8=jac(rhs)*P
T=S.Matrix([[B8[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])
Q8=L*T
q0=L*hsc+Q8*tstar
normal=S.Matrix([0,-25,1,1,1])
a0=(normal.T*q0)[0]
slope=normal.T*Q8
assert a0==S.Rational(5549833449599,5577764280000000)
assert list(slope)==[S.Rational(421,800),-S.Rational(11749,2592),-S.Rational(9511,7200),S.Rational(21,32),S.Rational(11579,800),S.Rational(11749,2592),S.Rational(9511,7200),-S.Rational(41093,810)]
assert R==abs(a0)/sum(abs(v) for v in slope)
corner=S.Matrix([-1,1,1,-1,-1,-1,-1,1])
z=R*corner
assert (normal.T*(q0+Q8*z))[0]==0
m=(loc['m']*z)[0];s=loc['center'][25]+(loc['A']*z)[25]
assert m==S.Rational(16932541854726549,313632293625596000000)>0
assert s==S.Rational(3836062555208901,156816146812798000000)>0
physical=loc['center']+loc['A']*z
assert all(v>=0 for v in physical)
allp=S.Matrix(p)+P*(tstar+z)
assert loc['restrictions'](tuple(F(v) for v in allp))==(F(0),)*5
support=FSET+((2,1),(3,2),(0,3),(1,5))
assert len(support)==14 and len(set(support))==14
M14=C[:,[D.index(e) for e in support]]
req=hsc+T*(tstar+z)
assert M14.rank()==14 and M14.row_join(req).rank()==14
weights,params=M14.gauss_jordan_solve(req)
assert params.rows==0 and all(v>0 for v in weights)
full=S.Matrix.hstack(*(edgecol(e) for e in support))
assert full*weights==S.Matrix(rhs(tuple(F(v) for v in allp)))
# Any <=13 supported coupling must include the same 10 forced edges (PR1939
# dual certificate; valid at star+R<reported forcing radius) and <=3 OTHER.
forced=S.Rational(18052765669,423284426970000)
assert star+R<forced
q=q0+Q8*z
triples_checked=0
for triple in combinations(range(20),3):
    A3=V[:,list(triple)]
    assert A3.row_join(q).rank()>A3.rank(),tuple(OTHER[j] for j in triple)
    triples_checked+=1
assert triples_checked==1140
print('FIRST_CERTIFICATE_RADIUS',R)
print('FIRST_CORNER',tuple(corner),'MU1',m,'CAPACITY25',s)
print('FOUR_EXTRA_EDGES',support[10:])
print('MIN_14_EDGE_WEIGHT',min(weights),'MAX_14_EDGE_WEIGHT',max(weights))
for edge,w in zip(support,weights):print('EDGE_WEIGHT',edge,w)
print('PASS_FULL_21_BLACKWELL_EQUALITIES_AND_PHYSICAL_CAPACITIES')
print('PASS_EXACT_1140_TRIPLE_SUPPORT_EXCLUSIONS',triples_checked)
print('SHARP_UNIFORM_EXACT15_WITH_MU_POSITIVE_SUPREMUM',R)
print('NOTE inherited ten forced-edge dual certificates from PR1939; scientific pins unchanged.')
