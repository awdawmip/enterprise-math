#!/usr/bin/env python3
"""Exact E7 transfer-edge rigidity in frozen P/Q–BRC seven-LR observer.
Pins: GK a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
Scientific model inherited from PR #2002 / R5_OPTIMIZE_FULL_POLYGON.py.
Uses SymPy Rational only for mathematical certificates (no floats).
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
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
 1+g+(a+b)/2+u+v+w)
def restrictions(p):
 x,y=p[:7],p[7:]
 return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))
def slacks(x):
 g,a,b,u,v,w,z=x
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
 F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def phys(p): return slacks(p[:7])+slacks(p[7:])
r=tuple(F(s) for s in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
def rhs(p):
 mu,nu=mass(p[7:]),mass(p[:7])
 return mu+nu+tuple(r[j]*nu[j] for j in range(7))
def edgecol(e):
 i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i]
 return S.Matrix(v)
def jac(fun):
 z=(F(0),)*14; origin=fun(z)
 return S.Matrix([[S.Rational(fun(tuple(F(k==j) for k in range(14)))[i]-origin[i])
  for j in range(14)] for i in range(len(origin))])

E=((0,0),(3,3),(4,3),(4,5),(6,5),(6,6),(0,3))
J=jac(restrictions);A=jac(rhs);K=S.Matrix.hstack(*(edgecol(e) for e in E))
M=S.Matrix.vstack(S.Matrix.hstack(J,S.zeros(5,7)),S.Matrix.hstack(A,-K))
zero=(F(0),)*14
b=S.Matrix([-S.Rational(s) for s in restrictions(zero)]+[-S.Rational(s) for s in rhs(zero)])
assert M.shape==(26,21) and M.rank()==18 and M.row_join(b).rank()==18
part=M.gauss_jordan_solve(b)[0]
null=M.nullspace()
assert len(null)==3
# Six linear identities for the seven coupling masses, with free u=e66, w=e43.
# This identity is verified on every vector of the full affine solution space.
def expected(t):
 u=t[14+E.index((6,6))];w=t[14+E.index((4,3))]
 return S.Matrix((u+S.Rational(13,9)*w,
                  1-2*u-S.Rational(479,90)*w,
                  w,S.Rational(8,5)*w,w,u,S.Rational(5,18)*w))
assert part[14:21,0]==expected(part)
assert all(v[14:21,0]==expected(v)-S.Matrix((0,1,0,0,0,0,0)) for v in null)
# The crucial b=d relation already follows from the 21 transport equations
# and the two physical time-matching equations alone.
Mt=S.Matrix.vstack(S.Matrix.hstack(A,-K),M[3,:],M[4,:])
delta=S.zeros(1,21);delta[0,14+E.index((4,3))]=1;delta[0,14+E.index((6,5))]=-1
assert Mt.rank()==Mt.col_join(delta).rank()
# Explicit fully physical E7 witness with seven strictly positive masses.
p=tuple(F(s) for s in (
 '156235560/159992239 156235560/159992239 156235560/159992239 '
 '105459003/319984478 0 0 0 1 1 54533236/159992239 '
 '421433145/1279937912 37904219/319984478 '
 '210515139/1279937912 1/10').split())
e=S.Matrix([F(s) for s in (
 '5964292503/31998447800 1274997718/3999805975 40561155/319984478 '
 '32448924/159992239 40561155/319984478 '
 '105459003/31998447800 22533975/639968956').split()])
assert restrictions(p)==(F(0),)*5
assert len(phys(p))==26 and all(s>=0 for s in phys(p))
assert all(v>0 for v in e)
assert K*e==S.Matrix(rhs(p))
assert e==expected(S.Matrix(list(p)+list(e)))
# The full lawful E7 physical region has quantitative positive diagonal masses.
# A feasible 21-vector is Z+N*t, where the three free coordinates t are real.
params=M.gauss_jordan_solve(b)[1]
Z=S.Matrix([ex.subs({q:0 for q in params}) for ex in part])
N=S.Matrix.hstack(*null)
G=S.Matrix.vstack(jac(phys)*N[:14,:], N[14:21,:])
h=S.Matrix(list(phys(tuple(F(x) for x in Z[:14])))+list(Z[14:21]))
assert G.shape==(33,3)
DUAL_BOUNDS={
 (0,0):({7:F(258866609,7999611950),9:F(6637059773,28798603020),11:F(67,162)}, F(5964292503,31998447800)),
 (3,3):({7:F(10760514869,35998253775),9:F(26982033,1599922390),25:F(67,81)}, F(6493976683,23998835850)),
 (6,6):({7:F(40746489481,71996507550),9:F(7504029773,28798603020),11:F(67,162)}, F(105459003,31998447800)),
}
for edge,(lam,bound) in DUAL_BOUNDS.items():
 j=E.index(edge)
 assert all(S.Rational(t)>=0 for t in lam.values())
 assert N[14+j,:]==sum((S.Rational(x)*G[i,:] for i,x in lam.items()),S.zeros(1,3))
 assert Z[14+j]-sum(S.Rational(x)*h[i] for i,x in lam.items())==S.Rational(bound)
 assert bound>0
# Consequently any lawful nonnegative E7 coupling has support 3 (w=0)
# or support 7 (w>0); all three diagonal masses are always positive.

# A genuine 3-edge point on the same fixed E7 support.
v=F(1,10);x=(F(1),F(1),F(1),F(27,80),v,F(27,80),F(1,10))
p3=x+x;e3=S.Matrix([mass(x)[0],mass(x)[3],F(0),F(0),F(0),mass(x)[6],F(0)])
assert restrictions(p3)==(F(0),)*5 and all(s>=0 for s in phys(p3))
assert all(v>0 for v in (e3[0],e3[1],e3[5]))
assert K*e3==S.Matrix(rhs(p3))
assert e3==expected(S.Matrix(list(p3)+list(e3)))
print('FROZEN_PIN_GLOBAL', 'a01383f825ef9d43b4b754254303298c64041568')
print('FROZEN_PIN_EM', '86149263e38c22292c9def1e0f69092efa1be77e')
print('RANK', M.rank(),'AUG_RANK',M.row_join(b).rank(),'NULLITY',len(null))
print('TIME_ONLY_FORCES_B_EQUALS_D',Mt.rank(),Mt.col_join(delta).rank())
print('PARAMETRIC_E7_MASSES','[u+13w/9,1-2u-479w/90,w,8w/5,w,u,5w/18]')
print('DIAGONAL_POSITIVE_LOWER_BOUNDS', {str(k):str(v[1]) for k,v in DUAL_BOUNDS.items()})
print('DIAGONAL_DUAL_MULTIPLIERS', {str(k):{str(i):str(x) for i,x in v[0].items()} for k,v in DUAL_BOUNDS.items()})
print('POSITIVE_PHYSICAL_E7_WITNESS', list(map(str,e)))
print('DIAGONAL_PHYSICAL_E3_WITNESS',list(map(str,e3)))
print('PASS_EXACT_ALL_21_BLACKWELL_5_PHYSICAL_EQUALITIES_26_PHYSICAL_CAPACITIES')
print('PASS_EXACT_E7_OFFDIAGONAL_RIGIDITY_AND_FULL_3_OR_7_SUPPORT_DICHOTOMY')
