"""Stage133 author separate algorithm: integer-weight literal ordered-history DFS."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
N=14;WP=(3,1,20);WQ=(1,1,10);DP=24**N;DQ=12**N
K=F(717127668,1179001);L=F(675046888,1179001)
B=(11,0,1);T=(8,1,2)
@lru_cache(None)
def optimum(n,a,b):
 offers={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<N:
  offers['C']=1+sum(F(WP[j],24)*optimum(n+1,a+(j==0),b+(j==1))[0] for j in range(3))
 v=min(offers.values());return v,tuple(k for k,x in offers.items() if x==v)
assert optimum(0,0,0)[0]==F(36407190671104521664854919,86115052294916278321152)
assert optimum(*B)[1]==('Q','C') and optimum(*T)[1]==('Q','C')
def traverse(w,z):
 sumv=[0,0,0,0];hits=defaultdict(lambda:[0,0,0]);counts=[0,0]
 def walk(n,a,b,wp,wq):
  counts[0]+=1;s=(n,a,b)
  if s in (B,T):
   x=hits[s];x[0]+=1;x[1]+=wp*24**(N-n);x[2]+=wq*12**(N-n)
  act=('Q' if w else 'C') if s==B else ('Q' if z else 'C') if s==T else optimum(n,a,b)[1][0]
  assert act in optimum(n,a,b)[1]
  if act=='C':
   for j in range(3):walk(n+1,a+(j==0),b+(j==1),wp*WP[j],wq*WQ[j])
  else:
   counts[1]+=1;pn=wp*24**(N-n);qn=wq*12**(N-n)
   if act=='Q':sumv[0]+=pn
   else:sumv[1]+=qn
   sumv[2]+=n*pn;sumv[3]+=n*qn
 walk(0,0,0,1,1)
 return (tuple([F(sumv[0],DP),F(sumv[1],DQ),F(sumv[2],DP),F(sumv[3],DQ)]),
  counts, {s:(x[0],F(x[1],DP),F(x[2],DQ)) for s,x in hits.items()})
C={str(w)+str(z):traverse(w,z) for w,z in product((0,1),repeat=2)}
assert C['00'][2][B]==(11,F(107421875,1451188224),F(107421875,725594112))
assert C['00'][2][T]==(112,F(21875,2239488),F(21875,839808))
assert [C[k][1] for k in ('00','01','10','11')]==[[747778,498519],[736690,491127],[747646,498431],[736558,491039]]
plus=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
scale=lambda a,x:tuple(t*x for t in a)
M=C['00'][0];dB=sub(C['10'][0],M);dT=sub(C['01'][0],M)
assert C['11'][0]==plus(plus(M,dB),dT)
err=lambda x:x[0]-x[1]
w0=-err(M)/err(dB);slope=-err(dT)/err(dB)
assert w0==F(3079578232623767,7403520000000000)
assert slope==-F(46161227,795300000)
point=lambda z:plus(plus(M,scale(dB,w0+slope*z)),scale(dT,z))
a=point(F(0));b=point(F(1))
assert a[0]==a[1]==F(12234055251084235565,35205614928358539264)
assert a[2]==F(72989119067006060803,5867602488059756544)
assert b[0]==b[1]==F(36703010861169506695,105616844785075617792)
assert b[2]==F(656403116242184147227,52808422392537808896)
assert 0<w0+slope<w0<1
for x in (a,b):
 assert x[2]>x[3] and x[2]+L*x[0]+K*x[1]==optimum(0,0,0)[0]
assert b[0]-a[0]==F(25790646875,3223170312044544)
print("STAGE133 AUTHOR LITERAL INTEGER DFS PASS")
print("first-hits",C['00'][2],"prefix visits",[C[k][1] for k in ('00','01','10','11')])
