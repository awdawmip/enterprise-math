#!/usr/bin/env python3
"""Self-contained exact rational verification: nine-dimensional R5 physical observer-fiber tube.
Depends scientifically on immutable PR #1927 for the 4845+1140 support exclusions.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
from sympy import Matrix, Rational, zeros

def Q(s): return tuple(F(v) for v in s.split())
R=Q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X0=Q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0=Q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
DY=Q('0 1 0 -1/4 -1/4 0 1/10')
H=F('17774559/17507527960')
p0=X0[:6]+(X0[6]+H/2,)+tuple(y+F(1,100000)*d for y,d in zip(Y0,DY))
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
    return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,
            *(a-b for a,b in zip(times(x),times(y))))
def rhs(p):
    mu,nu=mass(p[7:]),mass(p[:7])
    return mu+nu+tuple(R[j]*nu[j] for j in range(7))
def jac(fun):
    z=(F(0),)*14; f0=fun(z)
    return Matrix([[Rational(fun(tuple(F(i==j) for i in range(14)))[k]-f0[k]) for j in range(14)] for k in range(len(f0))])
Jc=jac(restrictions); Jb=jac(rhs); N=Jc.nullspace()
assert Jc.rank()==5 and len(N)==9
P=Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
B8=Jb*P
assert B8.rank()==8

def slack(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def both_slacks(p):return slack(p[:7])+slack(p[7:])

K=Matrix([-98800,-98800,-98800,-33345,264290,-33345,591026]+[0]*7)
assert Jc*K==Matrix.zeros(5,1)
assert Jb*K==Matrix.zeros(21,1)
assert Matrix.hstack(P,K).rank()==9
S=jac(both_slacks)*P
SK=jac(both_slacks)*K
RHO=Rational(23,17050000)
base=Matrix(both_slacks(p0))
origzero=tuple(i for i,v in enumerate(base) if not v)
assert origzero==(4,15,23)
assert all(SK[i]==0 and all(S[i,k]==0 for k in range(8)) for i in origzero)

def tube(radius,vec,zeros,face_tangent_zero=()):
    entries=[]
    for i,v in enumerate(vec):
        remain=v-radius*sum(abs(S[i,k]) for k in range(8))
        if i in zeros:
            if i in face_tangent_zero:
                assert v==0 and SK[i]==0
            else:
                assert remain==0 and SK[i]==0
            continue
        assert remain>0,(i,remain)
        if SK[i]: entries.append((remain/abs(SK[i]),i,remain,abs(SK[i])))
    return min(entries)

rho=RHO/2
sigma,limiting,rem,dk=tube(rho,base,origzero)
assert sigma==Rational(6177,612560000000)
print('RANK_PHYSICAL_9',Matrix.hstack(P,K).rank(),'RANK_STATISTICAL_8',B8.rank())
print('K_5_EQUALITY_DERIVATIVES',list(Jc*K))
print('K_21_BLACKWELL_DERIVATIVES_ZERO',Jb*K==Matrix.zeros(21,1))
print('NINE_DIMENSIONAL_BASE_RADIUS',rho)
print('NINE_DIMENSIONAL_FIBER_RADIUS',sigma,'LIMITING_SLACK',limiting)
assert all(base[i]-rho*sum(abs(S[i,k]) for k in range(8))-sigma*abs(SK[i])>=0 for i in range(26))
assert min(base[i]-rho*sum(abs(S[i,k]) for k in range(8))-sigma*abs(SK[i]) for i in range(26) if i not in origzero)==0
print('PASS_ALL_26_PHYSICAL_CAPACITIES_FOR_EVERY_REAL_TUBE_POINT')
print('PASS_15_EDGE_MINIMUM_INHERITED_BY_EXACT_OBSERVER_INVARIANCE')

star=Matrix([0,0,0,-RHO,RHO,0,0,-RHO])
pstar=tuple(Rational(p0[i])+(P*star)[i] for i in range(14))
slstar=Matrix(both_slacks(pstar))
assert tuple(i for i,v in enumerate(slstar) if not v)==(4,15,19,23)
face_delta=Rational(63,151745000)
facezero=(4,15,19,23)
assert all(SK[i]==0 for i in facezero)
face_sigma,face_limiting,face_remaining,face_dk=tube(face_delta,slstar,facezero,face_tangent_zero=(19,))
face_sigma=face_sigma/2
assert face_sigma>0
assert all(slstar[i]-face_delta*sum(abs(S[i,k]) for k in range(8))-face_sigma*abs(SK[i])>=0 for i in range(26) if i!=19)
assert slstar[19]==0 and SK[19]==0
mu_grad=Matrix([0,0,0,Rational(1,80),-1,0,0,Rational(13,4)])
assert Matrix([S[19,k] for k in range(8)])==mu_grad
assert (Jb*K)[1]==0
print('FACE_BASE_CENTER',tuple(star))
print('FACE_7D_T_RADIUS',face_delta)
print('FACE_ADDED_FIBER_RADIUS',face_sigma,'LIMITING_SLACK',face_limiting)
print('FACE_MU1_EQUATION',tuple(mu_grad))
print('EIGHT_DIMENSIONAL_PHYSICAL_14_EDGE_FACET_RANK',Matrix.hstack(P,K).rank()-1)
print('PASS_14_IF_MU1_EQ_0_ELSE_15_ON_LOCALLY_LAWFUL_FACE_TUBE')
print('NOTE_FINITE_4845_AND_1140_SUPPORT_EXCLUSIONS_FROM_VERIFY_AND_VERIFY_FACET')
