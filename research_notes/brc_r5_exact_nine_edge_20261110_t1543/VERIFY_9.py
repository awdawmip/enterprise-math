#!/usr/bin/env python3
"""Self-contained exact rational 11-arc Blackwell physical witness and 5D local stratum.
Frozen scientific precursor: PR #1950 at c8a0ade3904507cf4dda38bfa888bdb490b1ea87.
Uses no floating point and no network; tests all 21 original equations and 21+210 finite exclusions.
"""
from fractions import Fraction as F
from itertools import combinations
from functools import reduce
from math import gcd
from collections import Counter,deque
import sympy as S

def Q(s): return tuple(F(t) for t in s.split())
def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
      F(13,40)*a+b/80-u,(g-a)/2,
      1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
      (g-b)/2,F(3,40)*a+F(21,80)*b-w,
      u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,1+g+(a+b)/2+u+v+w)
def restrictions(p):
    x,y=p[:7],p[7:]
    return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))
def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
       F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def phys(p):return slacks(p[:7])+slacks(p[7:])
def jac(fun):
    zero=(F(0),)*14
    f0=fun(zero)
    return S.Matrix([[S.Rational(fun(tuple(F(j==k) for j in range(14)))[i]-f0[i])
         for k in range(14)]for i in range(len(f0))])
J=jac(restrictions)
assert J.rank()==5
N=J.nullspace()
P=S.Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
X=Q("999/1000 1/6 999/1000 1/20 29/240 11/160 1/120")
Y=Q("1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200")
DY=Q("0 1 0 -1/4 -1/4 0 1/10")
H=F(17774559,17507527960)
p=tuple(X[:6]+(X[6]+H/2,))+tuple(y+F(1,100000)*d for y,d in zip(Y,DY))
assert restrictions(p)==(F(0),)*5
star=S.Rational(23,17050000)
tstar=S.Matrix([0,0,0,-star,star,0,0,-star])
R=S.Rational(49948501046391,3920403670319950000)
zc=R*S.Matrix([-1,1,1,-1,-1,-1,-1,1])
pstar=S.Matrix(p)+P*tstar
center=S.Matrix(phys(tuple(F(v) for v in pstar)))
A=jac(phys)*P
r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
def rhs(u):
    mu,nu=mass(u[7:]),mass(u[:7]);return mu+nu+tuple(r[j]*nu[j] for j in range(7))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
FSET=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
OTHER=tuple(e for e in D if e not in FSET)
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
def edgecol(e):
    i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i];return S.Matrix(v)
C=S.Matrix.hstack(*(S.Matrix([edgecol(e)[i]*(20 if i>=14 else 1) for i in I]) for e in D))
FC=C[:,[D.index(e) for e in FSET]]
assert FC.rank()==10
L=S.Matrix.vstack(*(t.T for t in FC.T.nullspace()))
V=L*C[:,[D.index(e) for e in OTHER]]
hsc=S.Matrix([rhs(p)[i]*(20 if i>=14 else 1) for i in I]);B=jac(rhs)*P
T=S.Matrix([[B[I[i],k]*(20 if I[i]>=14 else 1) for k in range(8)] for i in range(15)])

# 11-arc contact: explicitly rational tangent displacement of the lawful 13-arc point.
alpha=S.Rational(53523764802790621389,287880142016181828437500)
z13=zc-alpha*S.eye(8)[:,5]-S.Rational(293725,3287440)*alpha*S.eye(8)[:,7]
k5=S.Matrix([S.Rational(14343940,34101),0,0,-260,0,0,0,1])
h=S.Rational(-2110010319589186676373085701,21647807832978109719298700000000)
z11=z13+h*k5
p11=tuple(F(v) for v in S.Matrix(p)+P*(tstar+z11))
assert restrictions(p11)==(F(0),)*5
phys11=center+A*z11
assert [i for i,v in enumerate(phys11) if v==0]==[4,15,19,23]
assert all(v>=0 for v in phys11)
q=hsc+T*(tstar+z11)
F9=((0,0),(0,1),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))
S2=((2,1),(0,3))
support=F9+S2
M11=C[:,[D.index(e) for e in support]]
assert M11.rank()==11 and M11.row_join(q).rank()==11
weights,_=M11.gauss_jordan_solve(q)
assert all(v>0 for v in weights)
C21=S.Matrix.hstack(*(edgecol(e) for e in support))
assert C21*weights==S.Matrix(rhs(p11))  # All original 21 equations.
# Explicit exact duals inherited as candidate vectors from PR #1963; verified again
# against all thirty columns and the new right-hand side.
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
assert set(F9).issubset(DUAL)
dual_lower={}
for e in F9:
    y=S.zeros(15,1)
    for term in DUAL[e].split():
        row,v=term.split(':');y[int(row)]=S.Rational(v)
    assert all((y.T*C[:,j])[0]<=int(D[j]==e) for j in range(30))
    lower=(y.T*q)[0]
    assert lower>0
    dual_lower[e]=lower
assert len(dual_lower)==9

# Complete one-extra-edge finite exclusion (any <=10-arc coupling uses 9 forced
# arcs and at most one of the other 21). The vector q is not in any span.
CF9=C[:,[D.index(e) for e in F9]]
assert CF9.rank()==9
other=tuple(e for e in D if e not in F9)
L9=S.Matrix.vstack(*(v.T for v in CF9.T.nullspace()))
assert L9.shape==(6,15)
V9=L9*C[:,[D.index(e) for e in other]]
qr=L9*q
assert all(V9[:,[j]].row_join(qr).rank()>V9[:,[j]].rank()
           for j in range(len(other)))

# All 210 possible two-extra-edge supports: precisely one subspace contains
# the new right-hand side, namely the explicit positive basis.
matched=[]
for i,j in combinations(range(len(other)),2):
    M2=V9[:,[i,j]]
    if M2.row_join(qr).rank()==M2.rank():
        matched.append((other[i],other[j]))
assert matched==[S2]

# Codimension-three affine local minimal-11 sheet inside the 8D physical family.
# One of the four left annihilator rows of M11 vanishes after pulling back to
# the physical parameter directions, leaving three independent equations.
N11=S.Matrix.vstack(*(v.T for v in M11.T.nullspace()))
assert N11.shape==(4,15)
G=N11*T
assert G.rank()==3
assert N11*q==S.zeros(4,1)
K11=G.nullspace()
assert len(K11)==5
assert all(M11.row_join(T*v).rank()==11 for v in K11)
# The nine dual bounds, 11 weights, 22 nonstructural physical slacks, and
# 209 rank exclusions are strict at z11; finite continuity yields a common
# open relative neighborhood in this 5D affine plane with minimal=11.
print('MODEL', 'frozen seven-likelihood-ratio P/Q-BRC Blackwell auxiliary transport')
print('SCIENTIFIC_PIN_GLOBAL', 'a01383f825ef9d43b4b754254303298c64041568')
print('SCIENTIFIC_PIN_EM', '86149263e38c22292c9def1e0f69092efa1be77e')
print('CONTACT_SCALAR',h)
print('CONTACT_PARAMETER',tuple(z11))
print('SUPPORT_11',support)
print('FULL_21_EQUATIONS',True,'PHYSICAL_5_EQUALITIES',True,'PHYSICAL_26_SLACKS',True)
print('MIN_POS_MASS',min(weights))
print('MIN_POS_PHYSICAL_SLACK',min(v for v in phys11 if v>0))
print('MIN_FORCED_DUAL_LOWER',min(dual_lower.values()))
print('FORCED_DUALS',len(dual_lower))
print('EXHAUSTIVE_ONE_EXTRA_EXCLUSIONS',len(other))
print('EXHAUSTIVE_TWO_EXTRA_MATCHES',len(matched),'FROM',len(other)*(len(other)-1)//2,'MATCHED',matched)
print('LOCAL_PARAMETER_NORMAL_RANK',G.rank(),'LOCAL_DIMENSION',8-G.rank())
print('LOCAL_TANGENT_BASIS',tuple(tuple(v) for v in K11))
print('PASS_EXACT_LAWFUL_MINIMAL_11_ARCS_AND_LOCAL_5D_STRATUM')


# ---------------------------------------------------------------------------
# Exact nine-arc continuation of the preceding frozen eleven-arc certificate.
# The eight surviving duals are rechecked against all 30 original columns.
# ---------------------------------------------------------------------------
K9=S.Matrix.hstack(*K11)
W9=S.Matrix.hstack(*(M11.gauss_jordan_solve(T*v)[0] for v in K11))
assert M11*W9==T*K9
initial=S.Matrix([S.Rational(1,100),S.Rational(1,100),
                  -S.Rational(1,100),-S.Rational(1,100),0])
tau=-(weights[1]+(W9.row(1)*initial)[0])/W9[1,4]
assert tau==S.Rational(
  32588385367342445179133179624463329,
  10293597568004590105855689746100000000)
delta=initial+S.Matrix([0,0,0,0,tau])
z9=z11+K9*delta
weights9=weights+W9*delta
physical9=center+A*z9
assert all(v>=0 for v in physical9)
assert [i for i,v in enumerate(physical9) if v==0]==[4,6,15,19,23]
assert [support[i] for i,v in enumerate(weights9) if v==0]==[(0,1),(2,1)]
assert all(v>=0 for v in weights9)
p9=tuple(F(v) for v in S.Matrix(p)+P*(tstar+z9))
assert restrictions(p9)==(F(0),)*5
assert phys(p9)==tuple(F(v) for v in physical9)
E9=tuple((e,v) for e,v in zip(support,weights9) if v>0)
assert len(E9)==9 and all(v>0 for e,v in E9)
assert S.Matrix.hstack(*(edgecol(e) for e,v in E9))*S.Matrix([v for e,v in E9])==S.Matrix(rhs(p9))
q9=hsc+T*(tstar+z9)
assert M11*weights9==q9

forced8=tuple(e for e in F9 if e!=(0,1))
assert len(forced8)==8
for e in forced8:
    y=S.zeros(15,1)
    for term in DUAL[e].split():
        row,value=term.split(':')
        y[int(row)]=S.Rational(value)
    assert all((y.T*C[:,j])[0]<=int(D[j]==e) for j in range(30))
    assert (y.T*q9)[0]>0

CF8=C[:,[D.index(e) for e in forced8]]
assert CF8.rank()==8
L8=S.Matrix.vstack(*(v.T for v in CF8.T.nullspace()))
assert L8.shape==(7,15)
q8=L8*q9
others=tuple(e for e in D if e not in forced8)
matching=[]
for e in others:
    v=L8*C[:,D.index(e)]
    if v.row_join(q8).rank()==v.rank():
        matching.append(e)
assert matching==[(0,3)]
# For any transport the eight strict duals force eight distinct edges.
# At most eight edges would consist only of those eight, but quotient q8
# is nonzero (indeed it belongs to the unique ninth-column span).
assert q8!=S.zeros(7,1)
print('NINE_EDGE_TAU',tau)
print('NINE_EDGE_DELTA',tuple(delta))
print('NINE_EDGE_Z',tuple(z9))
print('NINE_EDGE_SUPPORT',tuple(e for e,v in E9))
print('NINE_EDGE_WEIGHTS',tuple(v for e,v in E9))
print('NINE_EDGE_PHYSICAL_ZERO_SLACKS',[i for i,v in enumerate(physical9) if not v])
print('NINE_EDGE_MIN_POSITIVE_WEIGHT',min(v for e,v in E9))
print('NINE_EDGE_MIN_POSITIVE_PHYSICAL_SLACK',min(v for v in physical9 if v>0))
print('EIGHT_STRICT_FORCING_DUALS',len(forced8))
print('EXACT_SINGLETON_QUOTIENT_TESTS',len(others),'MATCHES',matching)
print('PASS_EXACT_LAWFUL_GLOBAL_MINIMUM_NINE_ARCS_AT_EXPLICIT_POINT')
