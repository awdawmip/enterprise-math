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
kernel=s.Matrix.hstack(*Wr.T.nullspace()).T
assert kernel.shape==(6,15)
proj=kernel*Cr
assert proj.rank()==6
rows=[]
for i in range(6):
    d=lcm(*(int(x.q) for x in proj.row(i)))
    rows.append([int(x*d) for x in proj.row(i)])
data=Path(__file__).with_name('QUOTIENT_MATRIX.txt')
lines=[x for line in data.read_text().splitlines()
       if line.strip() and not line.lstrip().startswith('#')
       for x in [list(map(int,line.split()))]]
assert lines==rows

# Certificate: every possible 14-column span that could contain W is included
# in the seven hyperplanes of the exact exhaustive 5-subset quotient scan.
hyperplane_edges=[
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,27,29],
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,22,23,24,25,26,27,28,29],
[0,1,2,3,4,5,6,7,10,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],
[0,2,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],
[0,2,4,6,10,11,12,15,18,21,23,25,27,29],
[0,2,4,6,10,11,12,16,18,20,23,25,27,29],
[0,2,4,6,10,11,12,17,18,19,23,25,27,29]
]
expected=[(14,5,9)]*4+[(13,5,8),(12,5,7),(12,5,7)]
for k,(ix,(rankc,rankq,dim)) in enumerate(zip(hyperplane_edges,expected)):
    e=C[:,ix]; q=proj[:,ix]
    assert (e.rank(),q.rank(),e.rank()-q.rank())==(rankc,rankq,dim)
    if k<4:
        missing=[j for j in (1,2,3,5) if not any(D[z][1]==j and D[z][0]!=j for z in ix)]
        assert len(missing)==1

# All 30-positive rational transport and a coupled eight-direction correction.
tau=s.Rational(1,10**7)
E0=s.Matrix([tau]*30)
correction=Ai*(b0-C*E0)[list(PIV),:]
for e,v in zip(SB,correction): E0[D.index(e)]+=v
assert C*E0==b0 and min(E0)==tau
DE=s.zeros(30,8)
change=Ai*B8[list(PIV),:]
for row,e in enumerate(SB): DE[D.index(e),:]=change[row,:]
assert C*DE==B8
S=jac(both_slacks)*P
G=jac(deficits)*P
sl0=both_slacks(p); defect=deficits(p)
forced=[i for i,v in enumerate(sl0) if v==0]
assert forced==[4,15,23]
assert all(S[i,:]==s.zeros(1,8) for i in forced)
def rowbound(M):
    return max(sum(abs(M[i,j]) for j in range(M.cols)) for i in range(M.rows))
assert min(x for x in sl0 if x>0)==s.Rational(7,2000000)
assert min(defect)==s.Rational(654982477,81785400000)
assert rowbound(DE)==s.Rational(535,52)
assert rowbound(S)==27
assert rowbound(G)==s.Rational(17,2)
assert rowbound(P)==s.Rational(47,2)
assert rowbound(DE)<100 and rowbound(S)<100 and rowbound(G)<100
assert min(x for x in sl0 if x>0)>s.Rational(1,10**7)
assert min(defect)>s.Rational(1,10**7)
# Taking t=e/10**100 with 2<e<3 gives perturbation below 300/10**100;
# coefficients are rational and the eight projected vectors form a basis.
# The transcendence of e then avoids every proper rational affine chart.
print('PASS_5_PHYSICAL_EQUALITIES_AND_8D_OBSERVER')
print('PASS_6x30_QUOTIENT_AND_7_EXCEPTIONAL_FLAT_RANKS')
print('PASS_30_EDGE_TRANSPORT_AND_8_EXACT_RIGHT_INVERSE_DIRECTIONS')
print('PASS_EXPLICIT_PHYSICAL_TRANSCENDENTAL_WITNESS_BOUNDS')
print('THEOREM_GENERIC_PHYSICAL_MIN_SUPPORT_15')

# Stronger rational result: the original frozen, lawful p0 is excluded
# by all three 14-column quotient hyperplane supports. The four 24-column
# hyperplanes already contradict a strictly positive source-column deficit.
for k,ix in enumerate(hyperplane_edges[4:],start=4):
    sub=C[:,ix]
    assert sub.row_join(b0).rank()==sub.rank()+1
print('PASS_ORIGINAL_RATIONAL_PHYSICAL_P0_MIN_SUPPORT_EXACTLY_15')

# Additional eight-dimensional *all-point* interval proof.
# The exact center 4,845-case exclusion is from PR #1902 (VERIFY.py);
# this script checks the independently sufficient real-parameter margins.
from math import factorial
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

minbeta = None
maxdualchange = 0
for edge, sparse in CERT.items():
    y = s.Matrix([s.Rational(F(sparse.get(i,"0"))) for i in range(21)])
    assert all((y.T*C[:,k])[0] <= int(D[k]==edge) for k in range(30))
    beta = (y.T*b0)[0]
    assert beta>0
    changebound = sum(abs((y.T*B8)[0,k]) for k in range(8))
    minbeta = beta if minbeta is None else min(minbeta,beta)
    maxdualchange = max(maxdualchange,changebound)
assert minbeta == s.Rational(18052765669,88328232000000)
assert maxdualchange == s.Rational(585227,46800)
assert len(CERT)==10

EB=Ai*b0[list(PIV),:]
DeltaB=Ai*B8[list(PIV),:]
assert CB*EB == b0 and CB*DeltaB==B8
assert min(EB)==s.Rational(23,4000000)
assert rowbound(DeltaB)==s.Rational(535,52)

scaledB=s.Matrix([[B8[PIV[i],k] * (20 if PIV[i]>=14 else 1)
                   for k in range(8)] for i in range(15)])
L=rowbound(scaledB)
assert L==s.Rational(457,8)
D0=1148267016000000
radius=s.Rational(1,10**100)
assert D0*factorial(15)*38**14*L < 10**100
assert min(x for x in sl0 if x>0) > radius*rowbound(S)
assert min(defect) > radius*rowbound(G)
assert minbeta>radius*maxdualchange
assert min(EB)>radius*rowbound(DeltaB)
assert rowbound(S)==27
assert rowbound(G)==s.Rational(17,2)
assert (s.Matrix.hstack(*[C[:,D.index(e)] for e in SB])).rank()==15

# Counterexample to the rank-five-flat exhaustive claim in PR #1918.
projected_columns=(0,1,3,8,15,22)
assert s.Matrix(lines)[:,list(projected_columns)].det()==-294840000
S14=(0,1,2,3,4,5,6,7,8,9,10,11,15,22)
assert s.Matrix(lines)[:,list(S14)].rank()==6

print('PASS_8D_REAL_CUBE_RANK',B8.rank(), 'radius=1/10**100')
print('CAPACITY_SLACK_MIN', min(x for x in sl0 if x>0), 'MAX_ROWSUM_DERIVATIVE',rowbound(S))
print('TRANSPORT_BASIS_MIN',min(EB),'MAX_ROWSUM_DERIVATIVE',rowbound(DeltaB))
print('FOUR_DEFICITS_MIN',min(defect),'MAX_ROWSUM_DERIVATIVE',rowbound(G))
print('DUAL_BETA_MIN',minbeta,'MAX_ROWSUM_DERIVATIVE',maxdualchange)
print('AUGMENTED_MINOR_CENTER_MIN',s.Rational(1,D0),'MAX_ROWSUM_SCALED_RHS_DERIVATIVE',L)
print('INTEGER_D0_FACTORIAL_BOUND',D0*factorial(15)*38**14*L)
print('PASS_R5_EIGHT_DIMENSIONAL_CUBE_ALL_REAL_POINTS_REQUIRE_15_EDGES')
print('PASS_QUOTIENT_RANK_SIX_WITNESS_DETERMINANT',-294840000)
