from fractions import Fraction as F
from itertools import product
q=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
r2=(F(3,4),F(5,4));r3=(F(1,2),F(1),F(3,2));r4=(F(1,10),F(1),F(19,10))
q4=(((F(509,900),F(382,900),F(9,900)),(F(47,180),F(43,90),F(47,180)),(F(9,900),F(382,900),F(509,900))),
    ((F(509,900),F(382,900),F(9,900)),(F(67,162),F(14,81),F(67,162)),(F(9,900),F(382,900),F(509,900))))
u=F(57197,61903);h=F(145,495224);old=F(93519,349275680)
W0=(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
V=tuple((q[0][j]+u*q[1][j])/2 for j in range(3))
k=(94+335*u)/(90*(4+9*u));xa=(10*u-3)/40;xb=(4-3*u)/4
la=F(1787,9000);lb=F(13,80);Ma=F(509,900)*xa+k*xb;Mb=V[0]-xa
L=F(5411,900)-3*k
S={'X0':(xa,F(4)),'V0-X0':(V[0]-xa,F(4)),'X1':(xb,F(3)),
   'V1-X1':(V[1]-xb,F(3)),'la':(la,F(15,4)),'lb':(lb,F(11,4)),
   'Ma-la':(Ma-la,L),'Mb-lb':(Mb-lb,F(27,4))}
assert all(s>=n*h for s,n in S.values())
assert {key for key,(s,n) in S.items() if s==n*h}=={'V1-X1','Ma-la'}
assert (13*u-12)/40==h==(Ma-la)/L
assert h/old==F(6330621700,5789106657)
for i in range(2):
 assert sum(q[i])==1 and sum(q[i][j]*r3[j] for j in range(3))==r2[i]
 for j in range(3):
  assert all(t>0 for t in q4[i][j]) and sum(q4[i][j])==1
  assert sum(q4[i][j][z]*r4[z] for z in range(3))==r3[j]
def test(W):
 dp,dq,dtp,dtq=[W[i]-W0[i] for i in range(4)]
 X=(xa+2*(dtq-dtp),xb+2*dtp-dtq,F(0))
 la1=la+F(5,2)*dp+F(5,4)*dq;lb1=lb-F(5,2)*dp-dq/4
 assert all(0<=X[j]<=V[j] for j in range(3))
 x=tuple(tuple((F(1) if i==0 else u)*q[i][j]*X[j]/(2*V[j]) for j in range(3)) for i in range(2))
 m={r:F(0) for r in sorted(set((F(1),)+r2+r3+r4))}
 for i in range(2):
  m[r2[i]]+=(F(1)-(F(1) if i==0 else u))/2
  for j in range(3):
   m[r3[j]]+=(F(1) if i==0 else u)*q[i][j]/2-x[i][j]
   for z in range(3):m[r4[z]]+=x[i][j]*q4[i][j][z]
 assert m[F(1,10)]==F(509,900)*X[0]+k*X[1] and m[F(1,2)]==V[0]-X[0]
 assert min(m.values())>=0 and sum(m.values())==1 and sum(r*t for r,t in m.items())==1
 assert 0<=la1<=m[F(1,10)] and 0<=lb1<=m[F(1,2)]
 assert (1-la1/10-lb1/2,la1+lb1)==W[:2]
 assert (2+(3+5*u)/8+X[0]/2+X[1],2+(1+u)/2+sum(X))==W[2:]
 return la1/m[F(1,10)]
for s in product((-1,1),repeat=4):test(tuple(W0[i]+s[i]*h for i in range(4)))
for s in product((-1,F(-1,2),0,F(1,2),1),repeat=4):
 test(tuple(W0[i]+s[i]*h for i in range(4)))
assert test(tuple(W0[i]+s*h for i,s in enumerate((1,1,1,-1))))==1
print('OPT_U1',u,'MAX_RADIUS',h,'GAIN_FACTOR',h/old)
print('ACTIVE_SLACKS',sorted(key for key,(s,n) in S.items() if s==n*h))
print('EXACT_Q3_Q4_KERNELS_AND_LR_MOMENTS_OK')
print('EXACT_CORNERS',16,'GRID_POINTS',625)
print('PASS_EXACT_R5_ONEPARAM_OPTIMAL_CUBE')
