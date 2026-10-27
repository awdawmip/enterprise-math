#!/usr/bin/env python3
# Finite exact external probability tree / not native X6 computation.
from fractions import Fraction as R
from itertools import product
import json
L=(298,375,36,-17)
def pos(x): return max(x,R(0))
def tree(sa,sb):
 q={'':R(1),'a':R(1,2),'b':R(1,2),'ax':R(1,4),'ay':R(1,4),'bu':R(1,8),'bv':R(3,8)}
 r={'':R(1),'a':R(3,2),'b':R(1,2),'ax':R(1),'ay':R(2),'bu':R(1),'bv':R(1,3)}
 ch={'':('a','b'),'a':('ax','ay'),'b':('bu','bv'),'ax':('axL','axM','axH'),'ay':('ayT',),'bu':('buL','buM','buH'),'bv':('bvT',)}
 for h,s in [('ax',sa),('bu',sb)]:
  for v,rr,pb in zip(ch[h],(R(1,2),R(1),R(3,2)),(s,1-2*s,s)):
   q[v]=q[h]*pb;r[v]=rr
 for h in ('ay','bv'):
  v=ch[h][0];q[v]=q[h];r[v]=r[h]
 p={h:q[h]*r[h] for h in q}
 assert 0<sa<R(1,2) and 0<sb<R(1,2) and len(q)==15
 assert all(q[h]>0 and p[h]>0 for h in q)
 assert all(sum(q[v] for v in ch[h])==q[h] and sum(p[v] for v in ch[h])==p[h] for h in ch)
 return q,r,p,ch
def best(sa,sb,force=None):
 q,r,p,ch=tree(sa,sb);memo={};actions={}
 def V(h):
  if h not in memo:
   rr=r[h];cand={'P':R(L[1]),'Q':R(L[0])*rr}
   if h in ch: cand['C']=L[2]*rr+L[3]+sum(q[v]/q[h]*V(v) for v in ch[h])
   a=force if force is not None and h in ('ax','bu') else min(cand,key=cand.__getitem__)
   memo[h]=cand[a];actions[h]=a
  return memo[h]
 val=V('')
 return val,actions
def full_closed(a,b):return R(2231,8)-pos(18*a-R(19,4))-pos(9*b-R(19,8))
def compressed_closed(a,b):return min(R(2231,8),R(281)-pos(18*a-4)-pos(9*b-1))
grid=[R(1,100),R(1,12),R(1,6),R(1,4),R(19,72),R(5,18),R(1,3),R(2,5),R(49,100)]
for a,b in product(grid,repeat=2):
 f,_=best(a,b);c=min(best(a,b,act)[0] for act in 'PQC')
 assert f==full_closed(a,b) and c==compressed_closed(a,b)
 assert (c>f)==((a-R(19,72))*(b-R(19,72))<0)
a,b=R(1,6),R(1,3)
f,policy=best(a,b);fo={act:best(a,b,act)[0] for act in 'PQC'};c=min(fo.values())
assert (f,c,c-f)==(R(1113,4),R(2231,8),R(5,8))
q,r,p,ch=tree(a,b)
time={h:0 if not h else (1 if h in ('a','b') else (2 if h in ('ax','ay','bu','bv') else 3)) for h in q}
def observer(h):
 act=policy[h]
 if act=='C':return tuple(map(sum,zip(*(observer(v) for v in ch[h]))))
 return (p[h] if act=='Q' else R(0),q[h] if act=='P' else R(0),p[h]*time[h],q[h]*time[h])
v=observer('')
assert v==(R(7,16),R(7,24),R(9,4),R(5,2))
assert sum(x*y for x,y in zip(v,L))==f
print(json.dumps({'status':'PASS_EXACT_FRACTION','checked_grid_pairs':81,
 'full_min':str(f),'seedless_min':str(c),'gap':str(c-f),
 'forced_common_min':{k:str(z) for k,z in fo.items()},
 'full_witness_vector':[str(z) for z in v],
 'strict_iff':'(sa-19/72)*(sb-19/72)<0'},sort_keys=True,indent=2))
