#!/usr/bin/env python3
"""Stand-alone exact Stage189 Bellman/four-corner check; original DFS in portable pack."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6)); N=14
K=F(241967493,1388612); L=F(59424392,347153)
H=F(209137371682549614928313,1584768521683668566016)
X=(8,0,1);T=(13,6,4)
@lru_cache(None)
def b(s):
 n,a,c=s; ell=F(2**(a+c),3**a)
 d={'P':K*ell,'Q':L}
 if n<14:d['C']=1+sum(P[i]*b((n+1,a+(i==0),c+(i==1)))[0] for i in range(3))
 h=min(d.values());return h,tuple(k for k,v in d.items() if v==h),tuple(v-h for v in d.values() if v>h)
ss=[(n,a,c) for n in range(15) for a in range(n+1) for c in range(n-a+1)]
ties={s:b(s)[1] for s in ss if len(b(s)[1])>1}
gaps=[v for s in ss for v in b(s)[2]]
assert len(ss)==680 and len(gaps)==1238 and min(gaps)==F(66370340952961,3582466457075712)
assert ties=={X:('Q','C'),T:('Q','C')} and b((0,0,0))[0]==H
assert T[1]-X[1]>T[0]-X[0] # no X-to-T ancestry
@lru_cache(None)
def obs(s,x,t):
 n,a,c=s
 def cont():
  vs=[obs((n+1,a+(i==0),c+(i==1)),x,t) for i in range(3)]
  return tuple(sum((P if j%2==0 else Q)[i]*vs[i][j] for i in range(3))+(j>=2) for j in range(4))
 if s==X:
  v=cont();return tuple(x*u+(1-x)*w for u,w in zip((1,0,0,0),v))
 if s==T:
  v=cont();return tuple((1-t)*u+t*w for u,w in zip((1,0,0,0),v))
 ac=b(s)[1];assert len(ac)==1
 if ac[0]=='P':return (F(0),F(1),F(0),F(0))
 if ac[0]=='Q':return (F(1),F(0),F(0),F(0))
 return cont()
v={(x,t):obs((0,0,0),F(x),F(t)) for x,t in product((0,1),repeat=2)}
B=v[0,0];DX=tuple(v[1,0][i]-B[i] for i in range(4));DT=tuple(v[0,1][i]-B[i] for i in range(4))
assert tuple(v[1,1][i]-v[1,0][i]-v[0,1][i]+B[i] for i in range(4))==(F(0),)*4
d0=B[0]-B[1];dx=DX[0]-DX[1];dt=DT[0]-DT[1]
x0=-d0/dx;slope=-dt/dx
assert x0==F(1289209864733261,4993103360000000)
assert slope==F(6413,10030788000)
def O(t):
 x=x0+slope*t
 return tuple(B[i]+DX[i]*x+DT[i]*t for i in range(4))
A0=F(9370003598922725167379,26711406663770723844096)
V0=F(1153476444134184737662789,106845626655082895376384)
A1=F(28110010813253777166137,80134219991312171532288)
V1=F(3460429309624219796220367,320536879965248686129152)
assert O(F(0))[0]==A0 and O(F(0))[2]==V0
assert O(F(1))[0]==A1 and O(F(1))[2]==V1
assert F(0)<x0<x0+slope<F(1)
for t in (F(0),F(1)):
 eP,eQ,tP,tQ=O(t)
 assert eP==eQ and tP>tQ and tP+K*eQ+L*eP==H
assert (V0-V1)/(A1-A0)==K+L==F(479665061,1388612)
print('STAGE189_REFERENCE_RATIONAL_PASS',len(ss),len(gaps),A1,V1)
