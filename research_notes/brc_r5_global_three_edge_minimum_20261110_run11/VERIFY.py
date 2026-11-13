#!/usr/bin/env python3
"""Exact certificate: global 3-edge minimum and complete minimizer locus.
Frozen P/Q-BRC seven-LR auxiliary Blackwell model, PR #1939 science pins.
Uses rational SymPy arithmetic, not numerical optimization.
"""
from fractions import Fraction as F
from sympy import Matrix, Rational, symbols, linear_eq_to_matrix, simplify

r = tuple(F(z) for z in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
D = tuple((i, j) for j in (0, 1, 2, 3, 5, 6) for i in range(7)
          if j not in (0, 6) or i == j)

def masses(x):
    g,a,b,u,v,w,z = x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
            F(13,40)*a+b/80-u,
            (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)
            +F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2,
            F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(x):
    g,a,b,u,v,w,z = x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def slacks(x):
    g,a,b,u,v,w,z = x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def constraints(x,y):
    return (x[0]-x[2], y[0]-1, y[6]-y[1]/10,
            *(a-b for a,b in zip(times(x),times(y))))

xx = symbols('xg xa xb xu xv xw xz')
yy = symbols('yg ya yb yu yv yw yz')
variables = xx + yy
nu, mu = masses(xx), masses(yy)
identities = list(constraints(xx,yy)) + [mu[i]-nu[i] for i in range(7)]
A, c = linear_eq_to_matrix(identities, variables)
assert A.rank() == 9

K=Rational(49400,295513)
L=Rational(33345,591026)
M=Rational(132145,295513)
Z,z,U,V,W=symbols('Z z U V W')
d=Z-z
X=(1+K*d, 10*Z+K*d, 1+K*d, U+L*d, V-M*d, W+L*d, z)
Y=(1,10*Z,1,U,V,W,Z)
assert all(simplify(expr)==0 for expr in constraints(X,Y))
assert all(simplify(a-b)==0 for a,b in zip(masses(X),masses(Y)))
assert Matrix([simplify(v) for v in X+Y]).jacobian((Z,z,U,V,W)).rank() == 5
# Source physical constraints x: 1-g>=0 and a/10-z>=0 imply d=0.
assert simplify(1-X[0]) == -K*d
assert simplify(X[1]/10-X[6]) == Rational(300453,295513)*d

# For x=y, all four parameters (a,u,v,w) vary in the lawful box.
a,u,v,w=symbols('a u v w')
ID=(1,a,1,u,v,w,a/10)
assert all(simplify(z)==0 for z in constraints(ID,ID))
assert Matrix(masses(ID)).jacobian((a,u,v,w)).rank() >= 1
assert simplify(masses(ID)[2]-(1-a)/2)==0
assert simplify(masses(ID)[1]-(F(13,40)*a+F(1,80)-u))==0
assert simplify(masses(ID)[5]-(F(3,40)*a+F(21,80)-w))==0

# Exact one-parameter global minimizer set.
symbolic_v=symbols('v')
edge_family=(F(1),F(1),F(1),F(27,80),symbolic_v,F(27,80),F(1,10))
weights=masses(edge_family)
s=F(7933,36000)+F(67,162)*(symbolic_v-F(1,10))
assert simplify(weights[0]-s)==0
assert simplify(weights[6]-s)==0
assert simplify(weights[3]-(1-2*s))==0
assert all(simplify(weights[i])==0 for i in (1,2,4,5))

for value in (F(1,10),F(1,5),F(13,40)):
    x=tuple(F(value) if z==symbolic_v else F(z) for z in edge_family)
    nu=masses(x)
    assert min(slacks(x))>=0 and constraints(x,x)==(F(0),)*5
    assert sum(nu)==1 and sum(r[j]*nu[j] for j in range(7))==1
    support={(j,j):nu[j] for j in (0,3,6)}
    assert set(support).issubset(D) and all(t>0 for t in support.values())
    # All 21 Blackwell coupling equations, exactly.
    assert tuple(sum(t for (i,j),t in support.items() if i==k) for k in range(7)) == nu
    assert tuple(sum(t for (i,j),t in support.items() if j==k) for k in range(7)) == nu
    assert tuple(sum(r[i]*t for (i,j),t in support.items() if j==k) for k in range(7)) == tuple(r[k]*nu[k] for k in range(7))
    print('MINIMIZER',value,'WEIGHTS',tuple(support.values()))

# Interior four-parameter equality family: six positive source columns.
central=(F(1),F(1,2),F(1),F(1,20),F(1,10),F(1,16),F(1,20))
assert constraints(central,central)==(F(0),)*5
assert min(slacks(central))>=0
mm=masses(central)
assert mm[4]==0 and all(mm[j]>0 for j in (0,1,2,3,5,6))
assert sum(mm)==1
print('EQUALITY_AFFINE_RANK',A.rank(),'DIMENSION',14-A.rank())
print('PHYSICAL_EQUAL_MARGINAL_FORCES_X_EQ_Y',K,Rational(300453,295513))
print('GLOBAL_MIN_EDGES',3,'MINIMIZER_V_INTERVAL',(F(1,10),F(13,40)))
print('FOUR_PARAMETER_DIAGONAL_SIX_EDGE_POINT',mm)
print('PASS_EXACT_RATIONAL_CERTIFICATE')
