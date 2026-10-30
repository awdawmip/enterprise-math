"""Exact rational certificate for four static 5-Port phase-source orbits at t=1/16.
No native X6/BRC heartbeat execution. Candidate centers are untrusted proposals.
"""
from math import comb
import sympy as s
I=s.I;R=s.Rational;u,v=s.symbols('u v');t=R(1,16)
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B=s.simplify(A[3:,:]*A[:3,:].inv())
assert A[:3,:].det()!=0
Q=[34000+204144*t,3200+56336*t,58250+1286*t,46600+12936*t,31525+28011*t]
r=[s.cancel(q/Q[0]) for q in Q]
assert r==[1,R(6721,46759),R(466643,374072),R(94817,93518),R(532411,748144)]
F=[]
for j in range(2):
 b=list(B.row(j));h=b[0]+b[1]*u+b[2]*v
 hb=s.conjugate(b[0])+s.conjugate(b[1])*r[1]/u+s.conjugate(b[2])*r[2]/v
 F.append(s.Poly(s.cancel(u*v*(h*hb-r[j+3])),u,v,extension=I).as_expr())
P=s.Poly(s.cancel(s.resultant(*F,v)/u),u,extension=I)
assert P.degree()==6 and P.TC()!=0 and s.gcd(P,P.diff()).degree()==0
cs=list(reversed(P.all_coeffs()));fac=s.cancel(cs[6]/s.conjugate(cs[0]))
for k in range(7):assert s.cancel(cs[k]-fac*r[1]**(6-k)*s.conjugate(cs[6-k]))==0
(a,b,c),(d,e,f)=[s.Poly(z,v).all_coeffs() for z in F]
D=s.Poly(s.expand(d*b-a*e),u,extension=I)
E=s.Poly(s.expand(d*c-a*f),u,extension=I)
for z in (D,E,s.Poly(a,u,extension=I),s.Poly(d,u,extension=I)):
 assert s.gcd(P,z).degree()==0
for aa,bb,cc in ((a,b,c),(d,e,f)):
 n=s.Poly(s.expand(aa*E.as_expr()**2-bb*D.as_expr()*E.as_expr()+cc*D.as_expr()**2),u,extension=I)
 quotient,remainder=s.div(n,P)
 assert remainder.is_zero and s.gcd(P,quotient).degree()==0
# Each row: proposed Gaussian-rational u root center and its unique v lift.
rows=[
(-377672048073067810,-33179190554807625,-1024551038755984257,444706162301618834),
(-356409585780010685,-129264232275208610,-996054577075402787,505315427522394764),
(-352894576312037190,-138572914348820846,-712359837804994165,860239422072391724),
(50087969218036839,375803445861251879,-1103871278550833250,170107619451771814),
(94355598915408067,-239135968680029203,-1071591667086383081,791600183848787844),
(205214119154923474,-520097140339574159,-753139307078148413,556354843228499389)]
rad=R(1,10**12);v_rad=R(1,10**6);centers=[];vs=[];kind=[]
def l1(z):return abs(s.re(z))+abs(s.im(z))
def lb(z):return max(abs(s.re(z)),abs(s.im(z)))
def derivs(poly,z):
 cc=list(reversed(poly.all_coeffs()))
 return [s.expand(sum(cc[j]*comb(j,k)*z**(j-k) for j in range(k,len(cc)))) for k in range(len(cc))]
for xr,xi,vr,vi in rows:
 z=R(xr,10**18)+I*R(xi,10**18)
 w=R(vr,10**18)+I*R(vi,10**18)
 p=derivs(P,z)
 assert 100*(l1(p[0])+sum(l1(p[k])*rad**k for k in range(2,7)))<lb(p[1])*rad
 dd=derivs(D,z);ee=derivs(E,z)
 delta_d=sum(l1(dd[k])*rad**k for k in range(1,len(dd)))
 delta_e=sum(l1(ee[k])*rad**k for k in range(1,len(ee)))
 lower=lb(dd[0])-delta_d
 assert lower>0 and l1(ee[0]+w*dd[0])+delta_e+l1(w)*delta_d<v_rad*lower
 centers.append(z);vs.append(w)
 lo=(max(0,abs(s.re(z))-rad))**2+(max(0,abs(s.im(z))-rad))**2
 hi=(abs(s.re(z))+rad)**2+(abs(s.im(z))+rad)**2
 kind.append('INNER' if hi<r[1] else 'OUTER' if lo>r[1] else 'PHYSICAL')
assert kind==['PHYSICAL']*4+['INNER','OUTER']
for i,z in enumerate(centers):
 for j,w in enumerate(centers):
  if i==j:continue
  assert abs(s.re(z-w))>2*rad or abs(s.im(z-w))>2*rad
  if kind[i]=='PHYSICAL':
   assert abs(s.re(z)*s.im(w)-s.im(z)*s.re(w))>rad*(l1(z)+l1(w))+2*rad**2
# Unique ray + antiholomorphic inversion => exactly four physical u roots;
# unique v lift and complexified involution => each has |v|^2=r3.
low,high=vs[1],vs[2]
assert s.re(high)-v_rad>-R(713,1000)
assert s.re(low)+v_rad<-R(995,1000)
assert s.im(high)-v_rad>R(859,1000)
assert s.im(low)+v_rad<R(506,1000)
assert R(282,1000)**2+R(353,1000)**2>R(1,5)
diff=centers[1]-centers[2]
assert (abs(s.re(diff))+2*rad)**2+(abs(s.im(diff))+2*rad)**2<R(1,10000)
q1=Q[0]/59536
assert 2*q1*(s.re(high)-s.re(low)-2*v_rad)>R(2,5)
assert 2*q1*(s.re(high)-v_rad+R(7,8))>R(1,8)
assert 2*q1*(-R(7,8)-s.re(low)-v_rad)>R(1,8)
print('PASS_PREFIX362_EXACT_FOUR_PHYSICAL_SOURCES_AND_ROBUST_TWO_LABEL_SEPARATION')
