#!/usr/bin/env python3
"""R5 first-contact 14-edge interior sheet: exact rational certificates.
Requires the immutable predecessor's research_notes/brc_r5_two_facet_20261110_t1140/VERIFY.py.
Runs full 4,845 quartet rank classification and 1,140 triple exclusions
at a genuinely new rational 14-edge physical instance.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from functools import reduce
from math import gcd
import sympy as S
root=Path(__file__).resolve().parent.parent
loc={}
exec(compile((root/'brc_r5_two_facet_20261110_t1140'/'VERIFY.py').read_text(), 'frozen_VERIFY.py','exec'),loc)
p=loc['p']; P=loc['P']; tstar=loc['tstar']; R=loc['R']; zc=R*S.Matrix([-1,1,1,-1,-1,-1,-1,1])
center=loc['center']; A=loc['A']; jac=loc['jac']; mass=loc['mass']; restrictions=loc['restrictions']; star=loc['star']
r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
def rhs(u):
    mu,nu=mass(u[7:]),mass(u[:7]);return mu+nu+tuple(r[j]*nu[j] for j in range(7))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
FSET=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
OTHER=tuple(e for e in D if e not in FSET)
S4=((2,1),(3,2),(0,3),(1,5));support=FSET+S4
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(e):
    i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i];return S.Matrix(v)
C=S.Matrix.hstack(*(S.Matrix([edgecol(e)[i]*(20 if i>=14 else 1) for i in I]) for e in D))
FC=C[:,[D.index(e) for e in FSET]]
L=S.Matrix.vstack(*(t.T for t in FC.T.nullspace()))
V=L*C[:,[D.index(e) for e in OTHER]]
M=C[:,[D.index(e) for e in support]]
assert FC.rank()==10 and L.shape==(5,15) and M.rank()==14
hsc=S.Matrix([rhs(p)[i]*(20 if i>=14 else 1) for i in I]);B=jac(rhs)*P
T=S.Matrix([[B[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])
normal=S.Matrix([S.Rational(421,800),-S.Rational(11749,2592),-S.Rational(9511,7200),S.Rational(21,32),S.Rational(11579,800),S.Rational(11749,2592),S.Rational(9511,7200),-S.Rational(41093,810)])
q0=hsc+T*(tstar+zc)
assert M.row_join(q0).rank()==14
w=S.Matrix([S.Rational(11749,2592),S.Rational(421,800),0,0,0,0,0,0]);assert (normal.T*w)[0]==0
delta=S.Rational(1,10**12);zn=zc+delta*w
q1=hsc+T*(tstar+zn)
assert M.row_join(q1).rank()==14
wt0,_=M.gauss_jordan_solve(q0);wt1,_=M.gauss_jordan_solve(q1)
assert all(v>0 for v in wt0) and all(v>0 for v in wt1)
for z,weight in ((zc,wt0),(zn,wt1)):
    phys=center+A*z
    assert all(v>=0 for v in phys)
    assert all(phys[i]>0 for i in range(26) if i not in (4,15,23))
    real_p=S.Matrix(p)+P*(tstar+z)
    assert restrictions(tuple(F(v) for v in real_p))==(F(0),)*5
    assert S.Matrix.hstack(*(edgecol(e) for e in support))*weight==S.Matrix(rhs(tuple(F(v) for v in real_p)))
# All 4,845 support tests by exact rational-linear integer elimination.
qcontact=L*q0;qnew=L*q1
den=S.ilcm(*[a.q for a in list(V)+list(qcontact)+list(qnew)])
cols=[[int(den*V[i,j]) for i in range(5)] for j in range(20)]
qc=[int(den*qcontact[i]) for i in range(5)];qn=[int(den*qnew[i]) for i in range(5)]
def rank(cols):
    rows=[[col[i] for col in cols] for i in range(5)]; k=0
    for c in range(len(cols)):
        pi=next((j for j in range(k,5) if rows[j][c]),None)
        if pi is None:continue
        rows[k],rows[pi]=rows[pi],rows[k]; pv=rows[k][c]
        for i in range(k+1,5):
            if rows[i][c]:
                a=rows[i][c]
                for j in range(c+1,len(cols)):rows[i][j]=pv*rows[i][j]-a*rows[k][j]
                rows[i][c]=0
                g=reduce(gcd,rows[i][c+1:],0)
                if g>1:rows[i][c+1:]=[v//g for v in rows[i][c+1:]]
        k+=1
        if k==5:break
    return k
assert all(rank([cols[j] for j in comb]+[qn])>rank([cols[j] for j in comb]) for comb in combinations(range(20),3))
matching=[];positive=[];normals=set()
for comb in combinations(range(20),4):
    mc=[cols[j] for j in comb]
    if rank(mc+[qc])>rank(mc):continue
    matching.append(comb)
    fullsupport=FSET+tuple(OTHER[j] for j in comb)
    mat=C[:,[D.index(e) for e in fullsupport]]
    assert mat.rank()==14
    wt,_=mat.gauss_jordan_solve(q0)
    if all(x>0 for x in wt):positive.append(comb)
    v=list(mat.T.nullspace()[0].T*T)
    den2=S.ilcm(*[x.q for x in v]); nv=[int(x*den2) for x in v]
    h=reduce(gcd,nv,0);nv=[x//h for x in nv]
    if next(x for x in nv if x)<0:nv=[-x for x in nv]
    normals.add(tuple(nv))
assert len(matching)==28 and len(positive)==12 and len(normals)==1
assert normals=={(34101,-293725,-85599,42525,937899,293725,85599,-3287440)}
print('R',R)
print('NORMAL_INTEGER',next(iter(normals)))
print('TANGENT_W',tuple(w),'DELTA',delta)
print('MIN_POS_WEIGHT_NEW',min(wt1))
print('MIN_NONSTRUCTURAL_SLACK_NEW',min((center+A*zn)[i] for i in range(26) if i not in (4,15,23)))
print('FOUR_SUPPORT_CLASSIFICATION',4845,'exact matches',len(matching),'positive',len(positive),'distinct normals',len(normals))
print('TRIPLE_NEW_POINT_EXCLUSIONS',1140)
print('PASS_EXACT_R5_INTERIOR_14EDGE_HYPERSURFACE_AND_15EDGE_GENERIC_COMPLEMENT')
# Two distinct 15-edge bases give feasible couplings on both sides of the local wall.
nq=S.Matrix([0,-25,1,1,1]);v=(nq.T*L*T)
assert list(v)==list(normal)
for extra,sgn,den_extra in (((5,1),1,5),((1,1),-1,-15)):
    j=OTHER.index(extra)
    assert (nq.T*V[:,j])[0]==den_extra
    sup15=support+(extra,)
    M15=C[:,[D.index(e) for e in sup15]]
    assert M15.rank()==15
    ze=zc+sgn*delta*S.eye(8)[:,0]
    rr=hsc+T*(tstar+ze)
    ww,_=M15.gauss_jordan_solve(rr)
    assert all(a>0 for a in ww)
    assert ww[-1]==(v*S.Matrix([sgn*delta]+[0]*7))[0]/den_extra
    assert all((center+A*ze)[i]>0 for i in range(26) if i not in (4,15,23))
    print('SIDE_15',sgn,'ADDITIONAL_BRANCH',extra,'WEIGHT',ww[-1],'MIN_MASS',min(ww))
print('PASS_BOTH_SIDES_15_AND_INTERIOR_7D_14_WALL')
