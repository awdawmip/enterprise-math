"""Exact external N14 ternary IID Stage214/215 reference: full ordered integer-mass DFS vs independent Fraction suffix DP. Author-only, not native X6."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
Pnum,Qnum=(3,1,20),(2,2,20)
P,Q=[tuple(F(x,24) for x in v) for v in (Pnum,Qnum)]
S,Z=(0,0,0),(14,0,0)
rows=[
 (214,F(265549752,2687315),F(2351021677817497415171339,29442503241037913260032),(7,2,2),'Q',
  F(3747353537341061245,10517860061584293888),F(2068074187667448833,219122084616339456),
  F(3747415453078661245,10517860061584293888),F(2067819259905528833,219122084616339456),
  F(306764674289301629,819200000000000000),F(138881259,320000000000),125176),
 (215,F(15508584,157345),F(137345358024509431139809,1723888220197896585216),(9,3,1),'P',
  F(3747415453078661245,10517860061584293888),F(2067819259905528833,219122084616339456),
  F(3747711513430661245,10517860061584293888),F(2066603386919928833,219122084616339456),
  F(307120210312341629,819200000000000000),-F(127887501,64000000000),109534)]

def ch(s,j):return s[0]+1,s[1]+(j==0),s[2]+(j==1)
def rho(s):return F(2**(s[1]+s[2]),3**s[1])
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(states)==680
for stage,K,H,T,terminal,left_a,left_v,right_a,right_v,known_z0,known_zs,known_visits in rows:
 @lru_cache(None)
 def bell(s):
  acts={'P':K*rho(s),'Q':K}
  if s[0]<14:acts['C']=1+sum(P[j]*bell(ch(s,j))[0] for j in range(3))
  v=min(acts.values())
  return v,tuple(k for k,x in acts.items() if x==v),tuple(x-v for x in acts.values() if x>v)
 assert bell(S)[0]==H
 ties={s:bell(s)[1] for s in states if len(bell(s)[1])>1}
 assert ties=={T:(terminal,'C'),Z:('P','Q')},ties
 gaps=[x for s in states for x in bell(s)[2]]
 assert len(gaps)==1238 and min(gaps)>0
 def action(s,u,z):
  if s==T:return terminal if u else 'C'
  if s==Z:return 'P' if z else 'Q'
  a=bell(s)[1];assert len(a)==1
  return a[0]
 @lru_cache(None)
 def suffix(s,u,z):
  act=action(s,u,z)
  if act=='P':return F(0),F(1),F(0),F(0)
  if act=='Q':return F(1),F(0),F(0),F(0)
  cs=[suffix(ch(s,j),u,z) for j in range(3)]
  return tuple(F(k>=2)+sum((P if k%2==0 else Q)[j]*cs[j][k] for j in range(3)) for k in range(4))
 def dfs(u,z):
  mass=[0]*4;visits=0
  def go(s,pm,qm):
   nonlocal visits
   visits+=1;a=action(s,u,z)
   if a=='C':
    for j in range(3):go(ch(s,j),pm*Pnum[j],qm*Qnum[j])
   else:
    f=24**(14-s[0]);n=s[0]
    mass[0]+=(a=='Q')*pm*f;mass[1]+=(a=='P')*qm*f
    mass[2]+=n*pm*f;mass[3]+=n*qm*f
  go(S,1,1)
  return tuple(F(x,24**14) for x in mass),visits
 sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
 corner={};count=0
 for u,z in product((0,1),repeat=2):
  value,visits=dfs(u,z)
  assert value==suffix(S,u,z)
  count+=visits;corner[u,z]=value
 assert count==known_visits
 O=corner[0,0];D=sub(corner[1,0],O);E=sub(corner[0,1],O)
 assert sub(sub(corner[1,1],corner[1,0]),E)==(F(0),)*4
 diff=lambda v:v[0]-v[1]
 z0=-diff(O)/diff(E);zs=-diff(D)/diff(E)
 assert (z0,zs)==(known_z0,known_zs) and 0<min(z0,z0+zs)<max(z0,z0+zs)<1
 def balanced(u):return tuple(O[i]+u*D[i]+(z0+zs*u)*E[i] for i in range(4))
 L,R=balanced(F(0)),balanced(F(1))
 assert (L[0],L[2],R[0],R[2])==(left_a,left_v,right_a,right_v)
 assert L[0]==L[1] and R[0]==R[1] and L[0]<R[0]
 assert L[2]>L[3] and R[2]>R[3]
 assert L[2]+2*K*L[0]==R[2]+2*K*R[0]==H
 print('STAGE'+str(stage)+'_REFERENCE_FULL_REAL_PASS',count,'width',R[0]-L[0], 'right',R[0],R[2])
