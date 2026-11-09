#!/usr/bin/env python3
"""Exact-rational R5 physical 15-edge genericity and perturbation certificate.
Dependencies: sympy (rational matrices only); exhaustive integer flats: VERIFY_FLATS.cpp.
This file uses the frozen physical map reproduced in PR #1913.
"""
from fractions import Fraction as F
from functools import reduce
from math import lcm
from pathlib import Path
import sympy as s

def Q(t): return tuple(map(F, t.split()))
r=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u, (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2, F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def restrictions(p):
    x,y=p[:7],p[7:]
    return (x[0]-x[2], y[0]-1, y[6]-y[1]/10,
            *(a-b for a,b in zip(times(x),times(y))))
def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def both_slacks(p): return slacks(p[:7])+slacks(p[7:])
def rhs(p):
    mu,nu=mass(p[7:]),mass(p[:7])
    return mu+nu+tuple(r[j]*nu[j] for j in range(7))
def deficits(p):
    b=rhs(p)
    return tuple(b[7+j]-b[j] for j in (1,2,3,5))
def jac(fun):
    zero=(F(0),)*14; baseline=fun(zero)
    return s.Matrix([[s.Rational(fun(tuple(F(i==j) for i in range(14)))[k]-baseline[k])
                      for j in range(14)] for k in range(len(baseline))])

Jc=jac(restrictions); Jb=jac(rhs)
N=Jc.nullspace()
assert Jc.rank()==5 and len(N)==9
X0=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0=Q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
DY=Q('0 1 0 -1/4 -1/4 0 1/10')
H=F(17774559,17507527960)
X=X0[:6]+(X0[6]+H/2,)
Y=tuple(y+F(1,100000)*d for y,d in zip(Y0,DY))
p=X+Y
assert restrictions(p)==(F(0),)*5
b0=s.Matrix(rhs(p))
P=s.Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
B8=Jb*P
assert B8.rank()==8
W=s.Matrix.hstack(b0,B8)
assert W.rank()==9
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
        if j not in (0,6) or i==j)
SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),
    (3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
PIV=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(edge):
    i,j=edge; a=[F(0)]*21; a[i]=1;a[7+j]=1;a[14+j]=r[i]
    return s.Matrix(a)
C=s.Matrix.hstack(*(edgecol(e) for e in D))
CB=s.Matrix.hstack(*(edgecol(e) for e in SB))
A=CB[list(PIV),:]
assert A.det()==s.Rational(-299,1600)
Ai=A.inv()
Cr=Ai*C[list(PIV),:]
Wr=Ai*W[list(PIV),:]
assert CB*Cr==C and CB*Wr==W

CERT={
 (0,0):{7:"1"},
 (0,1):{1:"-5/13",8:"15/13",15:"-20/13"},
 (0,2):{1:"-5/9",2:"-5/18",9:"10/9",16:"-10/9"},
 (2,2):{0:"-18/5",1:"-2",7:"18/5",8:"54/13",9:"4",15:"-72/13",16:"-4"},
 (3,3):{0:"-11/5",1:"1",2:"3",3:"5",4:"5",5:"5",6:"5",7:"11/5",8:"3",9:"3",12:"-5",13:"-5",15:"-8",16:"-8",17:"-4"},
 (4,3):{0:"-9/10",1:"3/2",2:"3",3:"4",4:"6",5:"6",6:"6",7:"9/10",8:"3/2",9:"3/2",12:"-6",13:"-6",15:"-6",16:"-6",17:"-4"},
 (4,5):{0:"2/5",1:"2",2:"3",3:"4",4:"5",5:"4",6:"4",7:"-2/5",12:"-4",13:"-4",15:"-4",16:"-4",17:"-4"},
 (5,5):{0:"2/5",1:"2",2:"3",3:"4",4:"5",5:"6",6:"5",7:"-2/5",12:"-5",13:"-5",15:"-4",16:"-4",17:"-4"},
 (6,5):{0:"2/13",1:"10/13",2:"15/13",3:"20/13",4:"25/13",5:"25/13",6:"38/13",7:"-2/13",12:"-25/13",13:"-38/13",15:"-20/13",16:"-20/13",17:"-20/13"},
 (6,6):{13:"1"},
}



from itertools import combinations
from collections import Counter
# The predecessor formulas, physical source pins, and ten forced-edge duals above
# are reused byte-for-byte from PR #1923. The following is new exact work.
scale=lambda i:20 if PIV[i]>=14 else 1
ac=[[int(scale(i)*C[PIV[i],j]) for j in range(len(D))] for i in range(15)]
br=[F(scale(i)*b0[PIV[i]]) for i in range(15)]
bt=[[F(scale(i)*B8[PIV[i],k]) for k in range(8)] for i in range(15)]
forced=tuple(sorted(D.index(e) for e in CERT))
remaining=tuple(j for j in range(30) if j not in forced)
assert len(forced)==10 and len(remaining)==20

def exact_row_relations(cols):
    """For each dependent row, yield an exact rational annihilator y of C[I,cols]."""
    vectors=[]; pivots=[]; combinations_old=[]
    for i in range(15):
        a=[F(ac[i][col]) for col in cols]
        y=[F(int(i==j)) for j in range(15)]
        for k,h in enumerate(pivots):
            lam=a[h]  # stored pivot coefficient is one
            if lam:
                for j in range(len(cols)):a[j]-=lam*vectors[k][j]
                for j in range(15):y[j]-=lam*combinations_old[k][j]
        h=next((j for j,v in enumerate(a) if v),None)
        if h is None:
            assert all(sum(y[i]*ac[i][col] for i in range(15))==0 for col in cols)
            yield y
        else:
            scale=a[h]
            vectors.append([v/scale for v in a])
            combinations_old.append([v/scale for v in y])
            pivots.append(h)

case_count=0
rank_counts=Counter()
min_sep=None
min_case=None
for optional in combinations(remaining,4):
    cols=forced+optional
    obstructions=[]
    relations=list(exact_row_relations(cols))
    rank_counts[15-len(relations)]+=1
    for y in relations:
        c=sum(y[i]*br[i] for i in range(15))
        if not c:continue
        q=[sum(y[i]*bt[i][k] for i in range(15)) for k in range(8)]
        slope=sum(abs(x) for x in q)
        obstructions.append((None if slope==0 else abs(c)/slope,c,slope))
    assert obstructions,("missing exact witness",optional)
    # Larger ratio is the stronger certificate for a fixed support.
    obstructions.sort(key=lambda x:(x[0] is None,x[0]),reverse=True)
    ratio,intercept,slope=obstructions[0]
    if ratio is not None and (min_sep is None or ratio<min_sep):
        min_sep=ratio
        min_case=(optional,intercept,slope)
    case_count+=1
assert case_count==4845
assert dict(rank_counts)=={14:3669,13:1143,12:33}
assert min_sep==F(23,17050000)

def positive_constraint_radii(values, derivative):
    ratios=[]
    for i,v in enumerate(values):
        norm=sum(abs(F(derivative[i,k])) for k in range(8))
        v=F(v)
        assert v>=0
        if v==0:
            assert norm==0
        elif norm:
            ratios.append((v/norm,i,v,norm))
    return ratios

phys_sl=both_slacks(p)
physical=positive_constraint_radii(phys_sl,jac(both_slacks)*P)
eb=Ai*b0[list(PIV),:]
db=Ai*B8[list(PIV),:]
assert CB*eb==b0 and CB*db==B8
basis=positive_constraint_radii(eb,db)
assert all(v>0 for v in eb)
dual=[]
for edge,entries in CERT.items():
    yy=s.Matrix([s.Rational(F(entries.get(i,"0"))) for i in range(21)])
    assert all((yy.T*C[:,j])[0] <= int(D[j]==edge) for j in range(30))
    c=F((yy.T*b0)[0]); assert c>0
    norm=sum(abs(F((yy.T*B8)[0,k])) for k in range(8))
    if norm:dual.append((c/norm,edge,c,norm))
rstar=F(23,17050000)
assert min(physical)[0]==rstar
assert min(basis)[0]==rstar
assert min(dual)[0]>rstar
assert min_sep==rstar

# Exact boundary construction at which edge (1,3) drops to zero.
i=SB.index((1,3))
t=tuple(-rstar*(int(db[i,k]>0)-int(db[i,k]<0)) for k in range(8))
assert t==(F(0),F(0),F(0),-rstar,rstar,F(0),F(0),-rstar)
pst=tuple(F(v) for v in s.Matrix(p)+P*s.Matrix(t))
vst=eb+db*s.Matrix(t)
assert restrictions(pst)==(F(0),)*5
assert min(both_slacks(pst))>=0
assert all(v>=0 for v in vst)
assert vst[i]==0 and sum(v>0 for v in vst)==14
assert CB*vst==s.Matrix(rhs(pst))  # all 21 Blackwell equalities
print("EXACT_TOTAL_CASES",case_count,"rank_counts",dict(rank_counts))
print("FOUR_OPTIONAL_MIN_CASE",min_case[0],"center",min_case[1],"slope",min_case[2])
print("MIN_EXCLUSION_RATIO",min_sep)
print("MIN_PHYSICAL_RATIO",min(physical))
print("MIN_BASIS_RATIO",min(basis))
print("MIN_DUAL_RATIO",min(dual))
print("SHARP_CUBE_RADIUS",rstar)
print("BOUNDARY_T",tuple(map(str,t)))
print("BOUNDARY_ZERO_EDGE",(1,3),"POSITIVE_EDGE_COUNT",sum(v>0 for v in vst))
print("BOUNDARY_EXTRA_ZERO_SLACKS",tuple(i for i,v in enumerate(both_slacks(pst)) if not v))
print("PASS_UNIFORM_MIN_SUPPORT_15_FOR_ALL_REAL_LINF_CUBES_RHO_LT_RSTAR")
print("PASS_EXACT_PHYSICALLY_LAWFUL_14_EDGE_AT_RSTAR")
