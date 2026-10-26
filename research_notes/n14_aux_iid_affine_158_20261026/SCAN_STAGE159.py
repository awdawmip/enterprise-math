#!/usr/bin/env python3
"""Exact dual-only first-breakpoint scan after Stage158 (author evidence)."""
from fractions import Fraction as F
from functools import lru_cache
N=14;P=(F(1,8),F(1,24),F(5,6))
K0=F(26880449139504,86511167249);L0=F(26463665283720,86511167249)
DK=F(-1);DL=-F(25280,14751)
S=[(n,a,b) for n in range(N+1) for a in range(n+1) for b in range(n-a+1)]
assert len(S)==680

def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
@lru_cache(None)
def ray(s):
 n,a,b=s;acts={'P':(K0*ratio(s),DK*ratio(s)),'Q':(L0,DL)}
 if n<N:
  c=[ray(t)[0] for t in ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))]
  acts['C']=(1+sum(P[i]*c[i][0] for i in range(3)),sum(P[i]*c[i][1] for i in range(3)))
 winner=min(acts,key=lambda z:acts[z]);return acts[winner],winner,acts
roots=[];ties=[]
for s in S:
 (v,d),action,acts=ray(s)
 for z,(w,e) in acts.items():
  if z==action:continue
  gap=w-v;der=e-d
  assert gap>=0 and (gap>0 or der>=0)
  if gap==0:ties.append((s,action,z,der))
  elif der<0:roots.append((gap/-der,s,action,z))
assert set(s for s,_,_,_ in ties)=={(6,1,2),(10,2,0)}
t,st,old,new=min(roots);K=K0+DK*t;L=L0+DL*t
assert K>0 and L>0
@lru_cache(None)
def bell(s):
 n,a,b=s;acts={'P':K*ratio(s),'Q':L}
 if n<N:
  c=[bell(w)[0] for w in ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))]
  acts['C']=1+sum(P[i]*c[i] for i in range(3))
 v=min(acts.values());return v,tuple(z for z in acts if acts[z]==v),acts
T={s:bell(s)[1] for s in S if len(bell(s)[1])>1}
G=[v-bell(s)[0] for s in S for v in bell(s)[2].values() if v>bell(s)[0]]
assert T=={(9,5,4):('Q','C'),(10,2,0):('P','C')},T
assert len(G)==1238 and min(G)==F(20367756,1887912013)
assert t==F(43776221891215860882,12563497839079943249)
assert K==F(580027221414,1887912013) and L==F(566236422120,1887912013)
print('PASS Stage159 dual candidate only, no primal interval')
print('ray_t',t,'K159',K,'L159',L,'new_tie',st,old,new)
print('680 states; ties',T,'1238 positive gaps; min gap',min(G),'dual root',bell((0,0,0))[0])
