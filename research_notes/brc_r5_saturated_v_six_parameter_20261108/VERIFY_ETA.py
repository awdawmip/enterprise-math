#!/usr/bin/env python3
"""R5 exact rational checker for 1/2 <= b/a <= 1 full saturated-v physical capacities."""
from fractions import Fraction as F
from itertools import product
import BASE_CERTIFICATES as low
import BASE_ETA1_CERTIFICATES as high
Z,O=F(0),F(1)
E0=(Z,)*7
E1=(O,Z,Z,Z,Z,Z,Z)
def mix(terms):return tuple(sum(c*f[k] for c,f in terms) for k in range(7))
def matmix(terms):return tuple(tuple(sum(c*M[i][j] for c,M in terms) for j in range(7)) for i in range(7))
def diag(x):
 m=low.mass(x)
 return tuple(tuple(m[i] if i==j else Z for j in range(7)) for i in range(7))
def test(g,s,t,p,q,theta,h):
 assert Z<=s<=g<=O and all(Z<=v<=O for v in (t,p,q,theta,h))
 eta=F(1,2)+t/2
 lambdas=((O-p)*(O-q),p*(O-q),(O-p)*q,p*q)
 source=[(O-g,E0),(g-s,E1)]
 target=[(O-g,E0),(g-s,E1)]
 transport=[(O-g,diag(E0)),(g-s,diag(E1))]
 for ix,weight in enumerate(lambdas):
  c=mix(((O-t,low.source(low.U*(ix%2),low.W*(ix//2))),(t,high.XS[ix])))
  y=mix(((O-t,low.TARGET[(ix%2,ix//2)]),(t,high.YS[ix])))
  Q=matmix(((O-t,low.Q[(ix%2,ix//2)]),(t,high.QS[ix])))
  assert low.legal(c) and low.legal(y) and low.residual(y)==Z
  plus=list(c);plus[4]+=F(1,10);plus[6]+=F(1,10);plus=tuple(plus)
  assert low.legal(plus) and low.residual(plus)==Z
  source.extend(((s*weight*(O-theta),c),(s*weight*theta,plus)))
  target.extend(((s*weight*(O-theta),y),(s*weight*theta,plus)))
  transport.extend(((s*weight*(O-theta),Q),(s*weight*theta,diag(plus))))
 x=mix(source);y=mix(target);Q=matmix(transport)
 u=s*(F(13,40)+eta/80)*p
 w=s*(F(3,40)+F(21,80)*eta)*q
 z=s*theta/10
 assert x==(g,s,eta*s,u,F(9,40)*eta*s+z,w,z)
 assert low.residual(x)==F(9,10)*eta*s*s*(theta-O)
 assert low.legal(x) and low.legal(y) and low.residual(y)==Z
 assert y[6]==y[1]/10 and y[4]-y[6]==F(9,40)*y[2]
 assert low.times(x)==(O+g+(15+34*eta)*s/40+u/2+F(3,2)*w+z,
                        O+g+(20+29*eta)*s/40+u+w+z)
 low.check_transport(x,y,Q)
 xh=mix(((O-h,x),(h,y)))
 Qh=matmix(((O-h,Q),(h,diag(y))))
 low.check_transport(xh,y,Qh)
 for d in ((Z,)*7,(O,)*7,(Z,F(1,7),F(2,7),F(1,2),F(5,7),F(6,7),O)):
  my=low.mass(y); mx=low.mass(xh)
  dp=tuple(sum(Qh[i][j]*d[j] for j in range(7))/my[i] if my[i] else Z for i in range(7))
  assert all(Z<=v<=O for v in dp)
  assert sum(my[i]*dp[i] for i in range(7))==sum(mx[i]*d[i] for i in range(7))
  assert sum(low.R[i]*my[i]*dp[i] for i in range(7))==sum(low.R[i]*mx[i]*d[i] for i in range(7))
 return x,y
n=0
for g in (Z,F(1,2),O):
 for s in (Z,g/2,g):
  for t,p,q,theta,h in product((Z,F(1,2),O),repeat=5):
   test(g,s,t,p,q,theta,h);n+=1
assert n==2187
print('PASS_2187_EXACT_G_S_ETA_P_Q_THETA_H_CHECKS',n)
x,y=test(O,O,F(1,2),O,O,F(1,2),Z)
print('ETA_3_4_SOURCE',','.join(map(str,x)))
print('ETA_3_4_TARGET',','.join(map(str,y)))
print('ETA_3_4_STOP_TIMES',','.join(map(str,low.times(x))))
print('ETA_3_4_RESIDUAL',low.residual(x))
print('PASS_R5_FULL_PHYSICAL_SATURATED_V_ETA_HALF_TO_ONE_ALL_REAL')
