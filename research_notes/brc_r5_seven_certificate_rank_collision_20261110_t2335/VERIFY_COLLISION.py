#!/usr/bin/env python3
"""Exact seven-certificate rank, physical collision and 2-observable recovery.
Scientific inputs stay pinned to previous PRs #1976/#2002."""
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
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,1+g+(a+b)/2+u+v+w)
def restrictions(p):
 x,y=p[:7],p[7:]
 return (x[0]-x[2],y[0]-1,y[6]-y[1]/10,*(a-b for a,b in zip(times(x),times(y))))
def slacks(x):
 g,a,b,u,v,w,z=x
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
 F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def phys(p):return slacks(p[:7])+slacks(p[7:])
def rhs(u):
 r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
 mu,nu=mass(u[7:]),mass(u[:7]);return mu+nu+tuple(r[j]*nu[j] for j in range(7))
def jac(fun):
 z=(F(0),)*14;f0=fun(z)
 return S.Matrix([[S.Rational(fun(tuple(F(j==k) for j in range(14)))[i]-f0[i])
 for k in range(14)]for i in range(len(f0))])

J=jac(restrictions);assert J.rank()==5
N=J.nullspace()
P=S.Matrix.hstack(*(N[i] for i in (0,1,2,4,5,6,7,8)))
B=jac(rhs)*P
I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)
T=S.Matrix([[B[I[i],k]*(20 if I[i]>=14 else 1)
 for k in range(8)] for i in range(15)])
r=tuple(F(v) for v in '1/10 1/2 3/4 1 5/4 3/2 19/10'.split())
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
 if j not in (0,6) or i==j)
def edgecol(e):
 i,j=e;v=[F(0)]*21;v[i]=1;v[7+j]=1;v[14+j]=r[i];return S.Matrix(v)
C=S.Matrix.hstack(*(S.Matrix([edgecol(e)[i]*(20 if i>=14 else 1)
 for i in I]) for e in D))
E7=((0,0),(3,3),(4,3),(4,5),(6,5),(6,6),(0,3))
M7=C[:,[D.index(e) for e in E7]]

source='''188243222214404826834936/188261165596929649956875
188243222214404826834936/188261165596929649956875
188243222214404826834936/188261165596929649956875
635320874973616290567909/1882611655969296499568750
3382124709305907675014711480339/106170260860719669952479570000000
217435298781768720561599/1026879085074161727037500
185740015/21009033552'''
target='''1
1
220096942483365833/294030275273996250
7864884099607268333/23522422021919700000
928115624721059763947477/9212164544517818510000000
2128739147931553331/7840807340639900000
1/10'''
p7=tuple(F(x) for x in (source+'\n'+target).split())
assert restrictions(p7)==(F(0),)*5 and all(v>=0 for v in phys(p7))
q7=S.Matrix([rhs(p7)[i]*(20 if I[ii]>=14 else 1) for ii,i in enumerate(I)])
assert M7.row_join(q7).rank()==7
DUAL={
'00':'7:1',
'33':'0:-36/5 1:-4 2:-2 7:36/5 8:8 9:8 10:5 12:-2/5 13:-2/5 14:-1/5',
'43':'0:-69/10 1:-9/2 2:-3 3:-2 7:69/10 8:15/2 9:15/2 10:6 12:-3/10 13:-3/10 14:-1/5',
'45':'0:-18/5 1:-2 2:-1 4:1 7:18/5 8:4 9:4 10:4 12:-1/5 13:-1/5 14:-1/5',
'65':'0:-36/13 1:-28/13 2:-23/13 3:-18/13 4:-1 5:-1 7:36/13 8:38/13 9:38/13 10:38/13 11:1 12:-1/13 13:-1/13 14:-1/13',
'66':'0:2/25 2:3/5 3:4/5 4:1 5:1 6:1 7:-2/25 11:-1 12:-1/25 13:-1/25 14:-1/25'}
Y=[]
for e,s in DUAL.items():
 y=S.zeros(15,1)
 for token in s.split():
  i,v=token.split(':');y[int(i)]=S.Rational(v)
 key={'00':(0,0),'33':(3,3),'43':(4,3),'45':(4,5),'65':(6,5),'66':(6,6)}[e]
 assert all((y.T*C[:,j])[0]<=int(D[j]==key) for j in range(30))
 Y.append(y)
ell=S.zeros(15,1);ell[3]=-S.Rational(5,23)
ell[10]=S.Rational(25,23);ell[14]=-S.Rational(1,23)
Y.append(ell)
A=S.Matrix.vstack(*(y.T*T for y in Y))
assert T.rank()==8 and A.rank()==6
relation=S.Matrix([0,0,-S.Rational(10,23),
 S.Rational(65,138),-S.Rational(52,69),0,1])
assert A.T*relation==S.zeros(8,1)
assert A.T.nullspace()==[relation]
comb=sum((relation[i]*Y[i] for i in range(7)),S.zeros(15,1))
assert (comb.T*q7)[0]==0
K=S.Matrix.hstack(*A.nullspace())
assert K.shape==(8,2) and A*K==S.zeros(7,2)
recover=S.Matrix.vstack(A[:6,:],T[0,:],T[1,:])
assert recover.det()==S.Rational(19799371,65505024)
assert recover.rank()==8

# A legal six-edge diagonal model and its mixture with the previous 7-edge model.
x=tuple(F(s) for s in ('1','1/2','1','1/10','1/10','1/10','1/20'))
u=x+x
assert restrictions(u)==(F(0),)*5
assert all(s>=0 for s in phys(u)) and mass(x)[4]==0
I6=((0,0),(1,1),(2,2),(3,3),(5,5),(6,6))
pi6=S.Matrix([S.Rational(mass(x)[i]) for i in (0,1,2,3,5,6)])
assert S.Matrix.hstack(*(edgecol(e) for e in I6))*pi6==S.Matrix(rhs(u))
assert all(v>0 for v in pi6)
pbar=tuple((F(a)+b)/2 for a,b in zip(p7,u))
assert restrictions(pbar)==(F(0),)*5
assert all(s>=0 for s in phys(pbar))
e7=M7.gauss_jordan_solve(q7)[0]
assert all(v>0 for v in e7)
C21_7=S.Matrix.hstack(*(edgecol(e) for e in E7))
qbar=S.Matrix(rhs(pbar))
assert qbar==(C21_7*e7+
 S.Matrix.hstack(*(edgecol(e) for e in I6))*pi6)/2

# Second legal model: its seven scores coincide, its full observation does not.
alpha=S.Matrix([S.Rational(1,10000),S.Rational(1,40000)])
dz=K*alpha;assert dz!=S.zeros(8,1)
pplus=S.Matrix([S.Rational(v) for v in pbar])+P*dz
pplus=tuple(F(v) for v in pplus)
assert restrictions(pplus)==(F(0),)*5
assert all(s>=0 for s in phys(pplus))
qplus=S.Matrix(rhs(pplus))
q15bar=S.Matrix([qbar[I[i]]*(20 if I[i]>=14 else 1) for i in range(15)])
q15plus=S.Matrix([qplus[I[i]]*(20 if I[i]>=14 else 1) for i in range(15)])
assert q15plus-q15bar==T*dz and q15plus!=q15bar
assert S.Matrix([(y.T*q15plus)[0] for y in Y])==S.Matrix([(y.T*q15bar)[0] for y in Y])
# Fixed LP-discovered support, but wholly exact rational recomputation here.
support=(0,2,8,9,10,11,17,18,19,26,27,28,29)
C13=S.Matrix.hstack(*(edgecol(D[i]) for i in support))
assert C13.rank()==13
w13=C13.gauss_jordan_solve(qplus)[0]
assert C13*w13==qplus and all(w>0 for w in w13)
assert len(phys(pplus))==26 and len(qplus)==21

print('FROZEN_SCIENCE_GLOBAL a01383f825ef9d43b4b754254303298c64041568')
print('FROZEN_SCIENCE_EM 86149263e38c22292c9def1e0f69092efa1be77e')
print('RANK_T',T.rank(),'RANK_7_CERTIFICATE_SCORES',A.rank())
print('DEPENDENCE ell=10/23*43-65/138*45+52/69*65')
print('KERNEL_BASIS',[[str(z) for z in list(K[:,j])] for j in range(2)])
print('AUGMENT_2_Q_ROWS',0,1,'RECOVERY_DETERMINANT',recover.det())
print('DELTA_Z',[str(v) for v in dz])
print('DELTA_Q0_Q1',[str(q15plus[i]-q15bar[i]) for i in (0,1)])
print('LAWFUL_5_PHYSICAL_EQUALITIES_AND_26_CAPACITIES',True)
print('EXACT_ORIGINAL_BLACKWELL_21_ROWS',True)
print('BASE_POSITIVE_ARCS',len(set(E7).union(I6)))
print('SECOND_POSITIVE_ARCS',len(support),'MIN_POS_MASS',min(w13))
print('SECOND_ARCS',[D[i] for i in support])
print('PASS_EXACT_LAWFUL_COLLISION_AND_TWO_OBSERVABLE_RECOVERY')
