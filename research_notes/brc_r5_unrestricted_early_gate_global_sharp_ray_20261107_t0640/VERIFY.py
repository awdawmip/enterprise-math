#!/usr/bin/env python3
"""R5 unrestricted early gates: exact primal/dual certificate (stdlib only)."""
from fractions import Fraction as F
q=lambda x:F(str(x))
r=list(map(q,['1/10','1/2','3/4','1','5/4','3/2','19/10']))
W=list(map(q,['161801/180000','6499/18000','267/80','137/40']))
H=F(16917,4642820)
def cap(a,b):return (F(13,40)*a+b/80,a/10+F(9,40)*b,F(3,40)*a+F(21,80)*b)
def mass(g,a,b,x):
 x0,x1,x2=x;v=cap(a,b);s=(94*a+335*b)/(90*(4*a+9*b)) if a+b else F(11,30)
 return (F(509,900)*x0+s*x1+x2/100,v[0]-x0,(g-a)/2,
         1-g+v[1]-x1+F(191,450)*(x0+x2)+(1-2*s)*x1,
         (g-b)/2,v[2]-x2,x0/100+s*x1+F(509,900)*x2)
def cert(g,a,b,x,e,h):
 m=mass(g,a,b,x);v=cap(a,b)
 A=(g+(a+b)/2+sum(x)+h,g+(3*a+5*b)/8+x[0]/2+x[1]+3*x[2]/2-h,
    sum(e)-h,sum(r[j]*e[j] for j in range(7))+h)
 C=(x[1]-v[1],e[0]-m[0],e[1]-m[1],-e[3],-e[5],-e[6])
 L=sum(a*b for a,b in zip((21126,-13604,-83401,114010),A))+sum(a*b for a,b in zip((18878,72000,26396,30609,87614,133218),C))
 D=(5005*(g-a)+2517*(g-b)+F(4213,2)*e[2]+F(118223,2)*e[4]
    -30400*(b-a)*x[1]/(4*a+9*b) if a+b else 7522*g+F(4213,2)*e[2]+F(118223,2)*e[4])
 return L,232141*h+D,C,D
def policy(g,a,b,x,e,h):
 m=mass(g,a,b,x);v=cap(a,b)
 assert 0<=a<=g<=1 and 0<=b<=g
 assert all(0<=x[j]<=v[j] for j in range(3))
 assert all(0<=e[j]<=m[j] for j in range(7))
 assert sum(m)==sum(r[j]*m[j] for j in range(7))==1
 actual=(1-sum(r[j]*e[j] for j in range(7)),sum(e),
         1+g+(3*a+5*b)/8+x[0]/2+x[1]+3*x[2]/2,
         1+g+(a+b)/2+sum(x))
 assert actual==tuple(W[j]+h*(1,1,1,-1)[j] for j in range(4))
 L,R,C,D=cert(g,a,b,x,e,h)
 assert L==R and D>=0 and all(c<=0 for c in C) and L<=232141*H
 return m,C,D
# Polynomial identity: after multiplying by (4a+9b), discrepancy has
# bidegree <=2 in a,b and is affine in 12 other coordinates. A 3x3
# tensor grid times an affine basis (13 points) proves it identically zero.
for a in map(F,[1,2,3]):
 for b in map(F,[1,2,3]):
  for j in range(13):
   y=[F(0)]*12
   if j:y[j-1]=F(1)
   L,R,_,_=cert(y[0],a,b,y[1:4],y[4:11],y[11])
   assert (4*a+9*b)*(L-R)==0
center=(F(77,80),)*3+((F(3,16),F(3,10),F(1,80)),
 (F(1297,6000),F(879,6400),F(0),F(563,144000),F(0),F(0),F(349,96000)))
t=F(31911,33163)
end=(t,t,t,(F(3199433,18571280),F(31911,102040),F(220131,18571280)),
 (F(886766809,4178538000),F(1415873,9285640),F(0),F(0),F(0),F(0),F(0)))
mc,_,_=policy(*center,F(0));me,Cend,Dend=policy(*end,H)
assert all(c==0 for c in Cend) and Dend==0
for s in map(F,['0','1/7','1/4','1/2','2/3','1']):
 state=tuple((1-s)*center[i]+s*end[i] for i in range(3))+(tuple((1-s)*center[3][i]+s*end[3][i] for i in range(3)),
       tuple((1-s)*center[4][i]+s*end[4][i] for i in range(7)))
 policy(*state,s*H)
for a,b in ((F(1,3),F(1,2)),(F(1,2),F(1,3)),(F(0),F(1,2)),(F(1,2),F(0))):
 g=max(a,b);x=(F(0),)*3;e=(F(0),)*7
 L,R,C,D=cert(g,a,b,x,e,F(0))
 assert L==R and all(c<=0 for c in C) and D>=0
print('dual_polynomial_identity=PASS; 117 exact interpolation checks')
print('both_primal_endpoints=PASS; sample_interpolations=PASS')
print('center_histogram=',tuple(map(str,mc)))
print('endpoint_histogram=',tuple(map(str,me)))
print('sharp_unrestricted_H=',H,'endpoint_t=',t)
print('upper_certificate_equalities=',all(c==0 for c in Cend))
print('ALL_REAL_RAY_INTERVAL=[0,16917/4642820]')
print('PASS_EXACT_R5_UNRESTRICTED_ALL_EARLY_GATES_SHARP_RAY')
