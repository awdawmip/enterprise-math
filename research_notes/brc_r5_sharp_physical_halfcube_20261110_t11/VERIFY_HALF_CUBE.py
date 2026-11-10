#!/usr/bin/env python3
"""Exact rational audit of the R5 sharp physical half-cube (frozen PR #1939 model).
No floating-point calculation; previous 4845+1140 support exclusions are cited, not rerun.
Dependencies: sympy.
"""
from fractions import Fraction as F
import sympy as S

def Q(s): return tuple(F(t) for t in s.split())
R = Q("1/10 1/2 3/4 1 5/4 3/2 19/10")

def mass(x):
    g,a,b,u,v,w,z=x
    return (F(509,900)*u + F(47,180)*z + F(67,162)*(v-z) + w/100,
            F(13,40)*a + b/80-u, (g-a)/2,
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

def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
            F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def phys(p): return slacks(p[:7])+slacks(p[7:])

def jac(fun):
    zero=(F(0),)*14
    f0=fun(zero)
    return S.Matrix([[S.Rational(fun(tuple(F(j==k) for j in range(14)))[i]-f0[i])
                      for k in range(14)] for i in range(len(f0))])

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
pstar=S.Matrix(p)+P*tstar
center=S.Matrix(phys(tuple(F(v) for v in pstar)))
A=jac(phys)*P
m=list((jac(lambda v:(mass(v[7:])[1],))*P)[0,:])
assert m==[0,0,0,S.Rational(1,80),-1,0,0,S.Rational(13,4)]
assert [i for i in range(26) if center[i]==0]==[4,15,19,23]
assert all(all(A[i,j]==0 for j in range(8)) for i in (4,15,23))
assert list(A[19,:])==m

def half_cube_cost(a):
    breaks={S.Rational(0)}
    for aa,mm in zip(a,m):
        if mm and aa/mm>0: breaks.add(aa/mm)
    return min((sum(abs(aa-lam*mm) for aa,mm in zip(a,m)),lam) for lam in breaks)

ratios=[]
for i in range(26):
    if center[i]<=0: continue
    h,lam=half_cube_cost(list(A[i,:]))
    if h: ratios.append((center[i]/h,i,lam,h))
ratios.sort()
rho,i,lam,h=ratios[0]
assert (rho,i,lam,h)==(S.Rational(273,225912500),25,S.Rational(4,13),S.Rational(159,104))
assert ratios[1][0]==S.Rational(17073,93775000)
assert center[25]==S.Rational(63,34100000)
assert list(A[25,:])==[0,0,0,S.Rational(9,40),0,-1,0,1]

x=S.Matrix([0,0,0,-1,-1,1,0,-S.Rational(79,260)])
assert S.Matrix([m])*x==S.zeros(1,1)
assert (A*x)[25]==-h
assert center[25]+rho*(A*x)[25]==0

# Compare to inherited exact, independently sourced support certificates (PR #1939).
positive14=S.Rational(50915668197609,1202833246639750000)
separator13=S.Rational(49948501046391,841518836618948125)
separator14=S.Rational(49948501046391,3920403670319950000)
forced=S.Rational(18052765669,423284426970000)
assert rho < min(positive14,separator13,separator14)
assert star+rho < forced

print("PASS R5 physical constraints Jacobian rank 5, active-zero indices [4,15,19,23]")
print("MU1_GRADIENT", m)
print("SHARP_CONDITIONAL_RHO",rho,"capacity_index",i)
print("SECOND_PHYSICAL_THRESHOLD",ratios[1][0])
print("ACTIVE_FACET_SLOPE",h,"lambda",lam)
print("JOINT_MU1_ZERO_AND_TARGET_CAPACITY_FACE",list(x))
print("RATIO_VS_PRIOR_1E-7",rho*S.Integer(10000000))
print("PASS inherited 13/14 exclusion, 14-basis positivity, mandatory-edge radii comparisons")
print("NOTE 4845+1140 support certificates inherited from PR #1939, not rerun")
