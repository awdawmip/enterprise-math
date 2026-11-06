from fractions import Fraction as F
from itertools import product
u=F(37,40); V0=F(1077,3200); V1=F(493,1600); V2=F(1017,3200)
k=F(359,986); h=F(93519,349275680)
c=(F(161801,180000),F(6499,18000),F(267,80),F(137,40))
xa=F(5,32); xb=F(49,160); la0=F(1787,9000); lb0=F(13,80)
ma0=F(509,900)*xa+k*xb; mb0=V0-xa
slacks={
'X0':(xa,F(4)),'V0-X0':(V0-xa,F(4)),
'X1':(xb,F(3)),'V1-X1':(V1-xb,F(3)),
'la':(la0,F(15,4)),'lb':(lb0,F(11,4)),
'Ma-la':(ma0-la0,F(15,4)+abs(2*k-F(1018,900))+abs(F(1018,900)-k)),
'Mb-lb':(mb0-lb0,F(27,4))}
assert ma0-la0==F(10391,7888000)
assert min(s/l for s,l in slacks.values())==h
assert all(s>=l*h for s,l in slacks.values())
def lr(W):
 p,q,tp,tq=(W[i]-c[i] for i in range(4))
 X0=xa+2*(tq-tp); X1=xb+2*tp-tq
 la=la0+F(5,2)*p+F(5,4)*q
 lb=lb0-F(5,2)*p-q/4
 J=k*X1
 M={F(1,10):F(509,900)*X0+J,F(1,2):V0-X0,F(3,4):F(0),F(1):V1+F(382,900)*X0-2*J,F(5,4):(1-u)/2,F(3,2):V2,F(19,10):X0/100+J}
 assert 0<=X0<=V0 and 0<=X1<=V1
 assert 0<=la<=M[F(1,10)] and 0<=lb<=M[F(1,2)]
 assert all(x>=0 for x in M.values())
 assert sum(M.values())==1 and sum(r*x for r,x in M.items())==1
 assert (1+1+(3+5*u)/8+X0/2+X1,1+1+(1+u)/2+X0+X1)==W[2:]
 assert (1-la/10-lb/2,la+lb)==W[:2]
 assert M[F(3,2)]==V2
 return la/M[F(1,10)],lb/M[F(1,2)]
for signs in product((-1,1),repeat=4):
 lr(tuple(c[i]+signs[i]*h for i in range(4)))
assert lr((c[0]+h,c[1]+h,c[2]+h,c[3]-h))[0]==1
for i,j in product(range(9),repeat=2):
 s=F(i,16)*h; t=F(j,16)*h
 W=(c[0]+s/10+t/2,c[1]-s-t,c[2],c[3])
 lr(W)
 assert W[0]+W[1]-1-F(10113,40000)>=F(15144537,2182973000)>0
 assert F(27,80)-V2==F(63,3200)
print('H=',h)
print('SLACK_RADII=',{n:str(s/l) for n,(s,l) in slacks.items()})
print('RECTANGLE_MIN_GAP=',F(15144537,2182973000))
print('FIFTH_MASS_GAP=',F(63,3200))
print('CORNERS=16 RECTANGLE_POINTS=81')
print('PASS_EXACT_R5_ROBUST_FOUR_OBSERVER_REPAIR_CUBE_AND_FIVE_OBSERVER_FIBER')
