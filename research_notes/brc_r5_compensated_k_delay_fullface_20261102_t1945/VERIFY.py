#!/usr/bin/env python3
"""Exact Fraction verifier: R5 compensated K delay/answer face and mixed separation.
This is an auxiliary finite two-law stopping model, not an X6 experiment.
"""
from fractions import Fraction as Q
from itertools import product, combinations

p = (Q(1,4), Q(1,3), Q(1,2), Q(2,3))
q = tuple((8*v-1)/9 for v in p)
u = tuple(Q(2,5)*(1+v) for v in p)
v = tuple(Q(1,3)*(1+z) for z in p)
aB, aI, bB, bI = Q(3,5), Q(1,2), Q(2,5), Q(1,2)
normal = (125, 0, 1806, -1854)
checks = 0

def check(pred, msg):
    global checks
    checks += 1
    if not pred:
        raise AssertionError(msg)

def obs(x, jB, jI, ks):
    # x,jB,jI,kC,kI,kBJ,kIJ in [0,1]; all arithmetic is exact.
    DB = (1-jB)/8
    DI = (1-x)*(1-jI)/8
    ws = (Q(1,4), (1-x)/4, DB, DI)
    Cs = tuple(ws[i]*(1-ks[i]) for i in range(4))
    R = sum((1+p[i])*Cs[i] for i in range(4))
    base = Q(5,2)-Q(3,4)*x+2*(DB+DI)
    eP = 1-aB*DB-aI*DI-sum(u[i]*Cs[i] for i in range(4))
    eQ = bB*DB+bI*DI+sum(v[i]*Cs[i] for i in range(4))
    TP = base+sum((1+p[i])*Cs[i] for i in range(4))
    TQ = base+sum((1+q[i])*Cs[i] for i in range(4))
    return (eP,eQ,TP,TQ)

def score(n,vec):
    return sum(n[i]*vec[i] for i in range(4))

def determinant(A):
    A = [list(row) for row in A]
    n = len(A)
    det = Q(1)
    for col in range(n):
        pivot = next((i for i in range(col,n) if A[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            A[pivot], A[col] = A[col], A[pivot]
            det = -det
        value = A[col][col]
        det *= value
        for i in range(col+1,n):
            fac = A[i][col]/value
            for j in range(col,n):
                A[i][j] -= fac*A[col][j]
    return det

for z in p+q+u+v+(aB,aI,bB,bI):
    check(0 < z < 1,'strict nature kernel positivity')
for i in range(4):
    check(9*(1+q[i])==8*(1+p[i]),'base-face time cancellation')
    check(u[i]==Q(2,5)*(1+p[i]),'P answer/time compensation')
    check(v[i]==Q(1,3)*(1+p[i]),'Q answer/time compensation')

FULL = []
for bits in product((0,1),repeat=7):
    o=obs(*map(Q,bits[:3]),tuple(map(Q,bits[3:])))
    FULL.append((bits,o))
    B=-8*o[2]+9*o[3]
    DB=Q(1-bits[1],8)
    DI=Q((1-bits[0])*(1-bits[2]),8)
    check(B==Q(5,2)-Q(3,4)*bits[0]+2*(DB+DI),'B identity FULL')
    check(B<=3,'FULL maximal face bound')

LR=[]
for bits in product((0,1),repeat=3):
    o=obs(Q(bits[0]),Q(bits[1]),Q(bits[1]),(Q(bits[2]),)*4)
    LR.append((bits,o))
    check(-8*o[2]+9*o[3]<=3,'LR maximal face bound')

faceFULL=[(bits,o) for bits,o in FULL if -8*o[2]+9*o[3]==3]
faceLR=[(bits,o) for bits,o in LR if -8*o[2]+9*o[3]==3]
check(len(faceFULL)==16 and len(faceLR)==2,'complete face cardinalities')
check(all(bits[:3]==(0,0,0) for bits,o in faceFULL),'exposed FULL source identifiers')
check(all(bits[:2]==(0,0) for bits,o in faceLR),'exposed LR identifiers')

m=(Q(1,4),Q(1,4),Q(1,8),Q(1,8))
Rtotal=sum(m[i]*(1+p[i]) for i in range(4))
check(Rtotal==Q(25,24),'total compensated mass')
# Every face FULL vertex has an exactly matching real-behavior LR policy:
# z=1-R/Rtotal is a valid probability, not necessarily deterministic.
for bits,o in faceFULL:
    R=sum(m[i]*(1+p[i])*(1-bits[3+i]) for i in range(4))
    z=1-R/Rtotal
    check(0<=z<=1,'matching LR k probability')
    check(obs(Q(0),Q(0),Q(0),(z,)*4)==o,'whole four-vector face equality')

hFULL=max(score(normal,o) for _,o in FULL)
hLR=max(score(normal,o) for _,o in LR)
check(hFULL==Q(1239,16),'FULL exact optimum')
check(hLR==Q(1221,16),'LR exact optimum')
check(hFULL-hLR==Q(9,8),'exact strict separation')
Witness=(0,1,0,0,0,0,0)
W=next(o for bits,o in FULL if bits==Witness)
check(W==(Q(143,240),Q(25,72),Q(173,48),Q(379,108)),'explicit FULL witness')
check(score(normal,W)==hFULL,'witness saturates')
check(Q(hFULL-hLR,sum(map(abs,normal)))==Q(9,30280),'dual L1 distance certificate')

# Full affine rank of conv(LR) from 5 independent exact LR vertices.
V0=LR[0][1]
index=(1,2,4,6)
mat=tuple(tuple(LR[i][1][j]-V0[j] for j in range(4)) for i in index)
det=determinant(mat)
check(det==-Q(5,36864),'LR four-dimensional affine rank')

# Full real-behavior image local four-rank is certified analytically by
# det dO/d(x,jB,jI,kC)=(1-x)/24576, holding other k fixed.
# Independent Fraction finite-difference verification at interior x=1/2.
x=jB=jI=kC=kI=kBJ=kIJ=Q(1,2)
state=(x,jB,jI,kC,kI,kBJ,kIJ)
step=Q(1,100)
central=obs(x,jB,jI,(kC,kI,kBJ,kIJ))
columns=[]
for key in (0,1,2,3):
    s=list(state);s[key]+=step
    changed=obs(*s[:3],tuple(s[3:]))
    columns.append(tuple((changed[i]-central[i])/step for i in range(4)))
Jac=tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))
# This multi-affine coordinate slice gives exact finite-difference derivatives.
check(determinant(Jac)==Q(1,49152),'FULL Jacobian local 4-rank at interior point')

# A non-corner test of the source-flow reduction and B statistic.
for j in range(9):
    z=Q(j+1,11)
    o=obs(Q(1,3),Q(2,7),Q(3,8),(z,Q(2,5),Q(4,9),Q(1,6)))
    DB=Q(1-Q(2,7),8)
    DI=(1-Q(1,3))*(1-Q(3,8))/8
    check(-8*o[2]+9*o[3]==Q(5,2)-Q(3,4)*Q(1,3)+2*(DB+DI),'interior time cancellation')

print('PASS_EXACT_R5_COMPENSATED_K_TIME_ANSWER_FACE_AND_MIXED_SEPARATION')
print('exact_assertions=',checks)
print('FULL_vertices=',len(FULL),'LR_vertices=',len(LR))
print('FULL_max_face_vertices=',len(faceFULL),'LR_max_face_vertices=',len(faceLR))
print('Rtotal=',Rtotal)
print('normal=',normal)
print('full_support=',hFULL,'lr_support=',hLR,'gap=',hFULL-hLR)
print('witness=',','.join(str(z) for z in W))
print('Linf_distance_lower_bound=',Q(hFULL-hLR,sum(map(abs,normal))))
print('LR_affine_det=',det,'FULL_interior_Jacobian_det=',determinant(Jac))
