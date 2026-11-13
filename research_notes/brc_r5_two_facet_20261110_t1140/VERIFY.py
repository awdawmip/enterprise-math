#!/usr/bin/env python3
"""R5 exact two-facet audit; inherited support exhaustions are NOT rerun."""
from fractions import Fraction as F
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
pstar=S.Matrix(p)+P*tstar
center=S.Matrix(phys(tuple(F(v) for v in pstar)))
A=jac(phys)*P
m=S.Matrix([list((jac(lambda v:(mass(v[7:])[1],))*P)[0,:])])
assert list(m)==[0,0,0,S.Rational(1,80),-1,0,0,S.Rational(13,4)]
assert [i for i in range(26) if center[i]==0]==[4,15,19,23]
assert all(all(A[i,j]==0 for j in range(8)) for i in (4,15,23))
assert list(A[19,:])==list(m)
def halfcube_slope(row):
    breaks={S.Rational(0)}
    for aa,mm in zip(row,m):
        if mm and aa/mm>0:breaks.add(aa/mm)
    return min((sum(abs(aa-lam*mm) for aa,mm in zip(row,m)),lam) for lam in breaks)
thresholds=[]
for i in range(26):
    if center[i]<=0:continue
    h,lam=halfcube_slope(list(A[i,:]))
    if h:thresholds.append((center[i]/h,i,lam,h))
thresholds.sort()
assert thresholds[0]==(S.Rational(273,225912500),25,S.Rational(4,13),S.Rational(159,104))
assert thresholds[1][0]==S.Rational(17073,93775000)
assert A.row(25)==S.Matrix([[0,0,0,S.Rational(9,40),0,-1,0,1]])
assert center[25]==S.Rational(63,34100000)
rho_plus=S.Rational(273,225912500)
R=S.Rational(49948501046391,3920403670319950000)
r=S.Rational(1,100000)
positive14=S.Rational(50915668197609,1202833246639750000)
sep13=S.Rational(49948501046391,841518836618948125)
forced=S.Rational(18052765669,423284426970000)
assert rho_plus<r<R
assert R<min(thresholds[1][0],positive14,sep13,forced-star)
x=S.Matrix([0,0,0,-1,-1,1,0,-S.Rational(79,260)])
e4=S.Matrix([0,0,0,0,1,0,0,0])
eps=S.Rational(1,10000000)
points={'interior_15':-eps*e4,'mu_facet_14':S.zeros(8,1),
        'capacity_facet_15':rho_plus*x-eps*e4,'joint_14':rho_plus*x}
for label,z in points.items():
    assert max(abs(v) for v in z)<=r
    actual=center+A*z
    others=[i for i in range(26) if i not in (4,15,19,23,25)]
    assert all(actual[i]>0 for i in others),label
    assert all(actual[i]==0 for i in (4,15,23)),label
    assert actual[19]==(m*z)[0] and actual[19]>=0 and actual[25]>=0
    expected={'interior_15':(eps,center[25]),
       'mu_facet_14':(0,center[25]),'capacity_facet_15':(eps,0),'joint_14':(0,0)}[label]
    assert (actual[19],actual[25])==expected,label
    assert restrictions(tuple(F(v) for v in (pstar+P*z)))==(F(0),)*5
    print('WITNESS',label,'mu1',actual[19],'capacity25',actual[25],
          'radius',max(abs(v) for v in z))
assert S.Matrix.vstack(m,A.row(25)).rank()==2
print('PASS exact original 5 physical equalities, 26 slack gradients; independent two facet normals')
print('PREDECESSOR conditional physical thresholds',thresholds[0],thresholds[1])
print('TWO_FACET_CERTIFICATE_RADIUS_STRICT',R)
print('TWO_FACET_EXPLICIT_CUBE_RADIUS',r)
print('CUBE_GAIN_OVER_PRIOR_ONE_FACET',r/rho_plus)
print('CERTIFICATE_SCOPE min(next_phys, positive14, sep13, sep14, forced-star) =',
      min(thresholds[1][0],positive14,sep13,R,forced-star))
print('PASS all four facet/interior rational witnesses and all 26 physical slacks')
print('NOTE: 4,845+1,140 prior support exclusions are inherited exactly from immutable PR #1939; not rerun.')
