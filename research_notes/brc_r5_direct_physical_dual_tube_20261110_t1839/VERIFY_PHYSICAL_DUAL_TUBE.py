#!/usr/bin/env python3
"""Independent exact-rational computation of direct 8D dual stability radius.
Source frozen mathematical model: PR #1976 at b9d0da58b74a18fe45f4b29bb238b70df79b96bc.
Theorem source: PR #1982 at d78d5bcbb1d8d038d59740b3231a4fd2559050ee.
All Fraction/Sympy exact; no network access or unresolved floating-point decisions.
"""
from fractions import Fraction as F
import sympy as S

def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
      F(13,40)*a+b/80-u,(g-a)/2,
      1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
      (g-b)/2,F(3,40)*a+F(21,80)*b-w,
      u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w, 1+g+(a+b)/2+u+v+w)

def restrictions(p):
    x,y=p[:7],p[7:]
    return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))

def rhs(u):
    r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
    mu,nu=mass(u[7:]),mass(u[:7])
    return mu+nu+tuple(r[j]*nu[j] for j in range(7))

def jac(fun):
    z=(F(0),)*14
    f0=fun(z)
    return S.Matrix([[S.Rational(fun(tuple(F(j==k) for j in range(14)))[i]-f0[i]) for k in range(14)] for i in range(len(f0))])

J=jac(restrictions)
assert J.rank()==5
N=J.nullspace()
P=S.Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
B=jac(rhs)*P
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
T=S.Matrix([[B[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])
assert T.shape==(15,8)
assert max(sum(abs(T[i,k]) for k in range(8)) for i in range(15))==S.Rational(405,2)

# All 6 duals reproduced directly from the frozen PR #1976 VERIFY_7.py.
DUAL={
(0,0):'7:1',
(3,3):'0:-36/5 1:-4 2:-2 7:36/5 8:8 9:8 10:5 12:-2/5 13:-2/5 14:-1/5',
(4,3):'0:-69/10 1:-9/2 2:-3 3:-2 7:69/10 8:15/2 9:15/2 10:6 12:-3/10 13:-3/10 14:-1/5',
(4,5):'0:-18/5 1:-2 2:-1 4:1 7:18/5 8:4 9:4 10:4 12:-1/5 13:-1/5 14:-1/5',
(6,5):'0:-36/13 1:-28/13 2:-23/13 3:-18/13 4:-1 5:-1 7:36/13 8:38/13 9:38/13 10:38/13 11:1 12:-1/13 13:-1/13 14:-1/13',
(6,6):'0:2/25 2:3/5 3:4/5 4:1 5:1 6:1 7:-2/25 11:-1 12:-1/25 13:-1/25 14:-1/25',
}
# Confirm the duals against original 30 columns, preserving exact transport indexing.
r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
def edgecol(e):
    i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i];return S.Matrix(v)
C=S.Matrix.hstack(*(S.Matrix([edgecol(e)[i]*(20 if i>=14 else 1) for i in I]) for e in D))
assert C.shape==(15,30)
BETA={
(0,0):S.Rational(570031933801575355927,3025154085489542635200),
(3,3):S.Rational(9386098186912477,52340117054042400),
(4,3):S.Rational(5506094603075,179341701138288),
(4,5):S.Rational(95758167010,1245428480127),
(6,5):S.Rational(239395417525,4981713920508),
(6,6):S.Rational(16939155808730941927,3025154085489542635200),
}
M=[]
for e in DUAL:
    y=S.zeros(15,1)
    for token in DUAL[e].split():
        i,v=token.split(':');y[int(i)]=S.Rational(v)
    assert all((y.T*C[:,j])[0]<=int(D[j]==e) for j in range(len(D)))
    l1_q=sum(abs(v) for v in y)
    trow=y.T*T
    l1_t=sum(abs(trow[k]) for k in range(8))
    assert BETA[e]>0
    M.append((e,BETA[e],l1_t, (BETA[e]/l1_t if l1_t else S.oo),l1_q,trow))

ell=S.zeros(15,1)
ell[3]=-S.Rational(5,23);ell[10]=S.Rational(25,23);ell[14]=-S.Rational(1,23)
F6=tuple(DUAL)
assert (ell.T*C[:,[D.index(e) for e in F6]])==S.zeros(1,6)
assert (ell.T*C[:,D.index((0,3))])[0]==1
beta7=S.Rational(1196977087625,89670850569144)
tr=ell.T*T
m7=sum(abs(tr[k]) for k in range(8))
M.append(((0,3),beta7,m7,beta7/m7 if m7 else S.oo,sum(abs(v) for v in ell),tr))
old=S.Rational(500554054825,148898447370063612)
new=min(x[3] for x in M)
assert new>=old
print('PINNED_PRIOR_SEVEN_ARC_POLYGON_VERTEX_MINIMA_SOURCE PR1976')
print('EXACT_T_SHAPE',T.shape,'EXACT_T_INFINITY_NORM',max(sum(abs(T[i,k]) for k in range(8)) for i in range(15)))
for e,b,n,rad,nq,trow in M:
    print('EDGE',e,'BETA',b,'DIRECT_8D_DUAL_NORM',n,'RADIUS',rad,'15D_L1_NORM',nq,'ROW',list(trow))
print('NEW_EXACT_8D_RADIUS',new,'DECIMAL',float(new))
print('PREVIOUS_8D_RADIUS',old,'DECIMAL',float(old))
print('IMPROVEMENT_FACTOR',S.factor(new/old),'DECIMAL',float(new/old))
print('BINDING',[(x[0],x[3]) for x in M if x[3]==new])
print('PASS_DIRECT_EIGHT_DIMENSIONAL_DUAL_STABILITY_CERTIFICATE')
