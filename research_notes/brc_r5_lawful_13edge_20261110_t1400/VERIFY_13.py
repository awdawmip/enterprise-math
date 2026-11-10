#!/usr/bin/env python3
"""Exact lawful thirteen-positive-arc R5 Blackwell certificate.

Reuses the predecessor full 21-row physical family and the frozen 10 mandatory
arc dual witnesses. All calculations use SymPy Rational and exact integer rank.
Run from any working directory; predecessor scripts are included in the parent
research branch. This wrapper and its dependencies should be executed together
for repository-native reproduction.
"""
from pathlib import Path
import contextlib, io, runpy
from fractions import Fraction as F
from itertools import combinations
import sympy as S

root=Path(__file__).resolve().parent.parent
source=root/'brc_r5_first_contact_sheet_20261110_t1235'/'VERIFY_SHEET.py'
with contextlib.redirect_stdout(io.StringIO()):
    b=runpy.run_path(str(source))

C,D,FSET,OTHER,I,edgecol,rhs=(b[x] for x in ('C','D','FSET','OTHER','I','edgecol','rhs'))
P,p,tstar,zc,center,A=(b[x] for x in ('P','p','tstar','zc','center','A'))
restrictions=b['restrictions']
phys=b['loc']['phys']
mu=(center+A*zc)[19]
assert mu==S.Rational(16932541854726549,313632293625596000000)>0
normal=S.Matrix([34101,-293725,-85599,42525,937899,293725,85599,-3287440])
h=S.Matrix([0,S.Rational(937899,293725)*mu,0,0,mu,0,0,0])
assert (normal.T*h)[0]==0
z13=zc+h
p13=tuple(F(v) for v in (S.Matrix(p)+P*(tstar+z13)))
assert restrictions(p13)==(F(0),)*5
slacks=phys(p13)
assert len(slacks)==26 and all(x>=0 for x in slacks)
assert slacks[19]==0

support=FSET+((2,1),(3,2),(0,3))
assert len(support)==13 and len(set(support))==13
M=C[:,[D.index(e) for e in support]]
q=S.Matrix([rhs(p13)[i]*(20 if i>=14 else 1) for i in I])
assert M.rank()==13 and M.row_join(q).rank()==13
weights,params=M.gauss_jordan_solve(q)
assert params.rows==0 and all(x>0 for x in weights)
assert S.Matrix.hstack(*(edgecol(e) for e in support))*weights==S.Matrix(rhs(p13))

# Frozen ten-edge forcing certificates, exactly as in PR #1939 VERIFY_FACET.py.
# Each dual y_e satisfies y_e*C_f <= 1_(f=e) for all 30 possible arcs.
CERT={
 (0,0):{7:'1'},
 (0,1):{1:'-5/13',8:'15/13',15:'-20/13'},
 (0,2):{1:'-5/9',2:'-5/18',9:'10/9',16:'-10/9'},
 (2,2):{0:'-18/5',1:'-2',7:'18/5',8:'54/13',9:'4',15:'-72/13',16:'-4'},
 (3,3):{0:'-11/5',1:'1',2:'3',3:'5',4:'5',5:'5',6:'5',7:'11/5',8:'3',9:'3',12:'-5',13:'-5',15:'-8',16:'-8',17:'-4'},
 (4,3):{0:'-9/10',1:'3/2',2:'3',3:'4',4:'6',5:'6',6:'6',7:'9/10',8:'3/2',9:'3/2',12:'-6',13:'-6',15:'-6',16:'-6',17:'-4'},
 (4,5):{0:'2/5',1:'2',2:'3',3:'4',4:'5',5:'4',6:'4',7:'-2/5',12:'-4',13:'-4',15:'-4',16:'-4',17:'-4'},
 (5,5):{0:'2/5',1:'2',2:'3',3:'4',4:'5',5:'6',6:'5',7:'-2/5',12:'-5',13:'-5',15:'-4',16:'-4',17:'-4'},
 (6,5):{0:'2/13',1:'10/13',2:'15/13',3:'20/13',4:'25/13',5:'25/13',6:'38/13',7:'-2/13',12:'-25/13',13:'-38/13',15:'-20/13',16:'-20/13',17:'-20/13'},
 (6,6):{13:'1'}
}
beta={}
for e,sparse in CERT.items():
    y=S.Matrix([S.Rational(sparse.get(i,'0')) for i in range(21)])
    assert all((y.T*edgecol(f))[0]<=int(e==f) for f in D)
    v=(y.T*S.Matrix(rhs(p13)))[0]
    assert v>0
    beta[e]=v
assert len(beta)==10 and set(beta)==set(FSET)

# Given ten compulsory arcs, <=12 support needs at most two other arcs.
FC=C[:,[D.index(e) for e in FSET]]
assert FC.rank()==10
L=S.Matrix.vstack(*(v.T for v in FC.T.nullspace()))
assert L.shape==(5,15) and L*FC==S.zeros(5,10)
V=L*C[:,[D.index(e) for e in OTHER]]
qquot=L*q
excluded=0
for ids in combinations(range(20),2):
    pair=V[:,list(ids)]
    assert pair.row_join(qquot).rank()>pair.rank(), tuple(OTHER[i] for i in ids)
    excluded+=1
assert excluded==190

print('PASS_EXACT_13_EDGE_PHYSICAL_BLACKWELL_INSTANCE')
print('Z_DELTA_H',tuple(h))
print('TARGET_MU1',slacks[19])
print('PHYSICAL_5_EQUALITIES',restrictions(p13))
print('MIN_POSITIVE_PHYSICAL_SLACK',min(v for v in slacks if v>0))
print('MIN_13_EDGE_MASS',min(weights))
for edge,v in zip(support,weights):
    print('ARC',edge,'WEIGHT',v)
for edge,v in beta.items():
    print('FORCED_ARC_DUAL',edge,'STRICT_MARGIN',v)
print('TEN_FORCING_CERTIFICATES_VERIFIED',len(beta))
print('PAIR_QUOTIENT_SUPPORT_EXCLUSIONS',excluded)
print('MINIMUM_POSITIVE_TRANSFER_SUPPORT',13)
