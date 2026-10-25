"""Stage133 portable author exact Fraction Bellman and observer validator."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(717127668,1179001);L=F(675046888,1179001)
B=(11,0,1);T=(8,1,2);root=(0,0,0)
kids=lambda n,a,b:((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
H={};O={};positive=[]
for n in range(N,-1,-1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);offers={'P':K*F(2**(a+b),3**a),'Q':L}
   if n<N:offers['C']=1+sum(P[j]*H[k] for j,k in enumerate(kids(*s)))
   v=min(offers.values());H[s]=v
   O[s]=tuple(k for k,x in offers.items() if x==v)
   positive.extend(x-v for x in offers.values() if x>v)
assert len(H)==680 and len(positive)==1238 and min(positive)==F(129758627,4074627456)
assert {s:acts for s,acts in O.items() if len(acts)>1}=={B:('Q','C'),T:('Q','C')}
assert H[root]==F(36407190671104521664854919,86115052294916278321152)
plus=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda a,t:tuple(x*t for x in a)
PD=(F(0),F(1),F(0),F(0));QD=(F(1),F(0),F(0),F(0))
@lru_cache(None)
def M(s,w,z):
 if s==B:return plus(scale(QD,w),scale(cont(s,w,z),1-w))
 if s==T:return plus(scale(QD,z),scale(cont(s,w,z),1-z))
 x=O[s][0]
 return PD if x=='P' else QD if x=='Q' else cont(s,w,z)
def cont(s,w,z):
 c=[M(v,w,z) for v in kids(*s)]
 return (sum(P[j]*c[j][0] for j in range(3)),sum(Q[j]*c[j][1] for j in range(3)),
  1+sum(P[j]*c[j][2] for j in range(3)),1+sum(Q[j]*c[j][3] for j in range(3)))
C={(w,z):M(root,F(w),F(z)) for w,z in product((0,1),repeat=2)}
base=C[0,0];dB=sub(C[1,0],base);dT=sub(C[0,1],base)
assert C[1,1]==plus(plus(base,dB),dT)
assert dB==(F(4619140625,2229025112064),-F(751953125,417942208512),-F(25673828125,278628139008),-F(17939453125,104485552128))
assert dT==(F(1016684375,7925422620672),-F(120903125,1253826625536),-F(180971875,12230590464),-F(3572471875,104485552128))
err=lambda v:v[0]-v[1]
w0=-err(base)/err(dB);slope=-err(dT)/err(dB)
assert w0==F(3079578232623767,7403520000000000)
assert slope==-F(46161227,795300000)
assert 0<w0+slope<w0<1
curve=lambda z:plus(plus(base,scale(dB,w0+slope*z)),scale(dT,z))
a=curve(F(0));b=curve(F(1));eta=b[0]-a[0]
assert a[0]==a[1]==F(12234055251084235565,35205614928358539264)
assert a[2]==F(72989119067006060803,5867602488059756544)
assert b[0]==b[1]==F(36703010861169506695,105616844785075617792)
assert b[2]==F(656403116242184147227,52808422392537808896)
assert eta==F(25790646875,3223170312044544)>0
assert K+L==F(1392174556,1179001)
assert (a[2]-b[2])/eta==K+L
assert a[2]-a[3]==F(86558755630978696807,158425267177613426688)>0
assert b[2]-b[3]==F(88899829683689096807,158425267177613426688)>0
for v in (a,b):assert v[2]+L*v[0]+K*v[1]==H[root]
print("STAGE133 AUTHOR FRACTION BELLMAN PASS",len(H),len(positive),b[0],b[2])
