#!/usr/bin/env python3
"""Exact rational suffix-DP reference for Stage190 external N14; full-history DFS in portable bundle."""
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6));N=14
K=F(219205722106707916,1293441907677519)
L=F(72144743665153672,431147302559173)
H=F(27408936515658794949498678792123439,212566265355324633731370212917248)
X=(8,0,1); Y=(4,2,0)
alpha189=F(28110010813253777166137,80134219991312171532288)
V189=F(3460429309624219796220367,320536879965248686129152)
@lru_cache(None)
def h(s):
 n,a,b=s; vals={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:vals['C']=1+sum(P[i]*h((n+1,a+(i==0),b+(i==1)))[0] for i in range(3))
 best=min(vals.values());return best,tuple(z for z,v in vals.items() if v==best),[v-best for v in vals.values() if v>best]
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
ties={s:h(s)[1] for s in states if len(h(s)[1])>1}
gaps=[v for s in states for v in h(s)[2]]
assert h((0,0,0))[0]==H and len(states)==680 and len(gaps)==1238
assert ties=={X:('Q','C'),Y:('P','C')}
assert min(gaps)==F(8957179515094375931,362080953867613958784)
@lru_cache(None)
def obs(s,x,y):
 if s in (X,Y):
  v=go(s,x,y)
  if s==X:return tuple(x*a+(1-x)*b for a,b in zip((F(1),F(0),F(0),F(0)),v))
  return tuple(y*a+(1-y)*b for a,b in zip((F(0),F(1),F(0),F(0)),v))
 ac=h(s)[1]; assert len(ac)==1
 if ac[0]=='P':return (F(0),F(1),F(0),F(0))
 if ac[0]=='Q':return (F(1),F(0),F(0),F(0))
 return go(s,x,y)
def go(s,x,y):
 n,a,b=s; w=[obs((n+1,a+(i==0),b+(i==1)),x,y) for i in range(3)]
 return tuple(sum((P if j in (0,2) else Q)[i]*w[i][j] for i in range(3))+(j>=2) for j in range(4))
B=obs((0,0,0),0,0)
DX=tuple(a-b for a,b in zip(obs((0,0,0),1,0),B))
DY=tuple(a-b for a,b in zip(obs((0,0,0),0,1),B))
C=tuple(obs((0,0,0),1,1)[j]-B[j]-DX[j]-DY[j] for j in range(4))
assert C==(F(0),)*4  # disjoint reachable tie cones, also exact checked here
x0=-(B[0]-B[1])/(DX[0]-DX[1])
xslope=-(DY[0]-DY[1])/(DX[0]-DX[1])
assert x0==F(11602917512839349,44937930240000000)
assert xslope==F(1335288430137,6241379200000)
def O(y):return tuple(B[j]+DX[j]*(x0+xslope*y)+DY[j]*y for j in range(4))
assert O(F(0))[0]==alpha189 and O(F(0))[2]==V189
for y in (F(0),F(1)):
 o=O(y)
 assert 0<x0+xslope*y<1 and o[0]==o[1] and o[2]>o[3]
 assert o[2]+K*o[1]+L*o[0]==H
assert O(F(1))[0]==F(28137949158459611576537,80134219991312171532288)
assert O(F(1))[2]==F(3422790017676192400495567,320536879965248686129152)
assert -(O(F(1))[2]-O(F(0))[2])/(O(F(1))[0]-O(F(0))[0])==K+L
print('STAGE190_REFERENCE_EXACT_PASS',len(states),len(gaps),'alpha_end',O(F(1))[0],'V_end',O(F(1))[2])
