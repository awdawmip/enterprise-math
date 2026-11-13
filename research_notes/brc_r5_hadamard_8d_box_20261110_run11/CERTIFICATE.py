#!/usr/bin/env python3
"""R5 exact derivative correction and robust 8D Hadamard support certificate.
Frozen seven-LR physical model from PR #1902 / PR #1923.
Center 4845-case support exclusion and dual inequalities are inherited, not rerun.
Requires sympy; arithmetic is exact rational.
"""
from fractions import Fraction as F
from sympy import Matrix, Rational

def Q(s): return tuple(F(v) for v in s.split())
r=Q("1/10 1/2 3/4 1 5/4 3/2 19/10")
def mass(x):
    g,a,b,u,v,w,z=x
    return (
        F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
        F(13,40)*a+b/80-u, (g-a)/2,
        1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
        (g-b)/2,F(3,40)*a+F(21,80)*b-w,
        u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)
def restrictions(p):
    x,y=p[:7],p[7:]
    return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,
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
    b=rhs(p);return tuple(b[7+j]-b[j] for j in (1,2,3,5))
def jac(fun):
    z=(F(0),)*14; f0=fun(z)
    return Matrix([[Rational(fun(tuple(F(i==j) for i in range(14)))[k]-f0[k])
                    for j in range(14)] for k in range(len(f0))])
Jc=jac(restrictions);Jb=jac(rhs);N=Jc.nullspace()
assert Jc.rank()==5 and len(N)==9
P=Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
B8=Jb*P
assert B8.rank()==8
X0=Q("999/1000 1/6 999/1000 1/20 29/240 11/160 1/120")
Y0=Q("1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200")
DY=Q("0 1 0 -1/4 -1/4 0 1/10")
H=F(17774559,17507527960)
p=(X0[:6]+(X0[6]+H/2,))+tuple(y+F(1,100000)*d for y,d in zip(Y0,DY))
assert restrictions(p)==(F(0),)*5
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in(0,6) or i==j)
SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),
    (3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(edge):
    i,j=edge;a=[F(0)]*21;a[i]=1;a[7+j]=1;a[14+j]=r[i];return Matrix(a)
CB=Matrix.hstack(*(edgecol(e) for e in SB))
A=CB[list(I),:]
assert A.det()==Rational(-299,1600)
b0=Matrix(rhs(p))
Ai=A.inv()
EB=Ai*b0[list(I),:]; DB=Ai*B8[list(I),:]
assert CB*EB==b0 and CB*DB==B8
def bound(M): return max(sum(abs(M[i,j]) for j in range(M.cols)) for i in range(M.rows))
assert min(EB)==Rational(23,4000000) and bound(DB)==Rational(535,52)
S=jac(both_slacks)*P;G=jac(deficits)*P
sl0=both_slacks(p)
assert [i for i,v in enumerate(sl0) if v==0]==[4,15,23]
assert all(all(S[i,k]==0 for k in range(8)) for i in (4,15,23))
assert min(v for v in sl0 if v>0)==Rational(7,2000000)
assert bound(S)==27 and bound(G)==Rational(17,2)
assert min(deficits(p))==Rational(654982477,81785400000)
T=Matrix([[B8[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])
s=[sum(abs(T[i,k]) for k in range(8)) for i in range(15)]
assert max(s)==Rational(405,2)   # prior PR #1923 claimed 457/8
assert T[13,7]==-75
assert sum(v*v for v in s)==Rational(15396036457529,233280000)
assert sum(v*v for v in s)<260**2
D0=1148267016000000
U=D0*260*39**14
rho=Rational(1,10**40)
assert U<10**40
assert min(v for v in sl0 if v>0)>rho*bound(S)
assert min(EB)>rho*bound(DB)
assert min(deficits(p))>rho*bound(G)
# 10 mandatory-edge dual central bounds independently given in PR #1902/#1923
beta=Rational(18052765669,88328232000000)
delta_beta=Rational(585227,46800)
assert beta>rho*delta_beta
print("PASS physical rank 8; fixed 15-edge 21-row equations; lawful margins")
print("CORRECTED_SCALED_ROW_BOUND",max(s),"rather_than_457/8")
print("WITNESS_T[13,7]",T[13,7])
print("ROWSUM_SQUARED_NORM",sum(v*v for v in s),"< 67600")
print("CERTIFIED_U",U,"< 10^40")
print("CERTIFIED_8D_RADIUS",rho)
print("PASS new 8D all-real-point 15-edge certificate conditional on PR1902 center exclusions")
