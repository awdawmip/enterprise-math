#!/usr/bin/env python3
"""Pure-Fraction certificate: generic 15-edge full-face rank and lawful mu1>0 R5 point.

All 21 equations are checked after solving a 15x15 rational subsystem.
"""
from fractions import Fraction as F

def q(s):
    return tuple(map(F, s.split()))

R = q('1/10 1/2 3/4 1 5/4 3/2 19/10')
X0 = q('999/1000 1/6 999/1000 1/20 29/240 11/160 1/120')
Y0 = q('1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200')
H = F('17774559/17507527960')
t = F('1/100000')
X = X0[:6] + (X0[6] + H/2,)
DY = q('0 1 0 -1/4 -1/4 0 1/10')
Y = tuple(y+t*d for y,d in zip(Y0, DY))

def mass(f):
    g,a,b,u,v,w,z=f
    return (F(509,900)*u + F(47,180)*z + F(67,162)*(v-z) + w/100,
            F(13,40)*a+b/80-u, (g-a)/2,
            1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
            (g-b)/2, F(3,40)*a+F(21,80)*b-w,
            u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(f):
    g,a,b,u,v,w,z=f
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def slack(f):
    g,a,b,u,v,w,z=f
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
            w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

D = tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
          if j not in (0,6) or i==j)
B = ((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),
     (3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))
PIVOT_ROWS = (0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
TAU = F('1/10000000')

def col(edge):
    i,j=edge
    z=[F(0)]*21
    z[i]=F(1)
    z[7+j]=F(1)
    z[14+j]=R[i]
    return tuple(z)

def square_solve_and_det(a,b):
    """Exact Gaussian elimination with simultaneous determinant calculation."""
    n=len(b)
    m=[list(a[i])+[b[i]] for i in range(n)]
    det=F(1)
    for k in range(n):
        p=next((i for i in range(k,n) if m[i][k]),None)
        assert p is not None
        if p!=k:
            m[k],m[p]=m[p],m[k]
            det=-det
        d=m[k][k]
        det*=d
        m[k]=[v/d for v in m[k]]
        for i in range(n):
            if i==k: continue
            d=m[i][k]
            if d:
                m[i]=[x-d*y for x,y in zip(m[i],m[k])]
    return tuple(row[-1] for row in m),det

assert X[0]==X[2] and Y[0]==1 and Y[6]==Y[1]/10
assert all(z>=0 for z in slack(X)+slack(Y))
assert [i for i,z in enumerate(slack(X)) if not z] == [4]
assert [i for i,z in enumerate(slack(Y)) if not z] == [2,10]
assert times(X)==times(Y)==q('17609/6000 33857/12000')
mu,nu=mass(Y),mass(X)
assert len(D)==30 and mu[1]==F('23/4000000') and nu[4]==0
assert sum(mu)==sum(nu)==1
rhs=mu+nu+tuple(R[j]*nu[j] for j in range(7))
columns={edge:col(edge) for edge in D}
residual=tuple(rhs[i]-TAU*sum(columns[edge][i] for edge in D)
               for i in range(21))
A=[[columns[e][i] for e in B] for i in PIVOT_ROWS]
w,det=square_solve_and_det(A,tuple(residual[i] for i in PIVOT_ROWS))
assert det==F('-299/1600')
assert min(w)==F('107/20000000')
E={e:TAU for e in D}
for edge,val in zip(B,w): E[edge]+=val
assert min(E.values())==TAU and len(E)==30
for i in range(21):
    assert sum((E[e]*columns[e][i] for e in D),F(0))==rhs[i]
assert sum(E.values())==1
print('PASS_LAWFUL_SEEDLESS_MU1_POSITIVE',mu[1], 'NU4_ZERO',nu[4])
print('PASS_EXACT_MATCHED_TIMES',*times(X))
print('PASS_ALL_30_STRICT_POSITIVE_COUPLING min=',min(E.values()))
print('PASS_21_BLACKWELL_EQUALITIES_AND_NORMALIZATION')
print('PASS_RANK_15_BY_NONZERO_MINOR det=',det)
print('FULL_NU4_FACE_GENERIC_MIN_SUPPORT_15 (linear algebra + finite-union argument)')
print('PHYSICAL_14_VS_15_QUESTION_PENDING_FOR_SPECIFIC_G_EQ_B_FAMILY')
