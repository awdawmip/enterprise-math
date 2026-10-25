#!/usr/bin/env python3
"""Stage108 independent literal-history exact rational author verifier."""
from fractions import Fraction as F
from functools import lru_cache
P=(F(3,24),F(1,24),F(20,24))
Q=(F(2,24),F(2,24),F(20,24))
K=F(208946709,206588); L=F(50075544,51647)
A=(10,3,0); C=(11,5,4)
U0=F(1115808042440821,1479206400000000)
U1=F(159404052982303,211315200000000)
A0=F(91588670614917102449,263775056922062880768)
A1=F(13084095824621807507,37682150988866125824)
V0=F(13541383133505475882195,1055100227688251523072)
V1=F(1934483126570299962385,150728603955464503296)
def ch(z):
 n,a,b=z
 return ((n+1,a+1,b),(n+1,a,b+1),(n+1,a,b))
@lru_cache(None)
def choice(z):
 n,a,b=z
 costs={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:
  costs['C']=F(1)+sum(P[i]*choice(t)[0] for i,t in enumerate(ch(z)))
 m=min(costs.values())
 return m,tuple(act for act,v in costs.items() if v==m),costs
assert choice((0,0,0))[0]==F(495598934898928452760465,707312394011255242752)
states=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(states)==680
assert {z for z in states if len(choice(z)[1])>1}=={A,C}
assert sum(v>choice(z)[0] for z in states for v in choice(z)[2].values())==1238
assert all(v>=choice(z)[0] for z in states for v in choice(z)[2].values())
def dfs(u,w):
 eP=eQ=tP=tQ=F()
 stack=[((0,0,0),F(1),F(1))]
 hits={A:[0,F(),F()],C:[0,F(),F()]}
 visits=0
 while stack:
  z,mp,mq=stack.pop();visits+=1
  if z in hits:
   h=hits[z];h[0]+=1;h[1]+=mp;h[2]+=mq
  if z==A:
   eQ+=mq*u;ct=1-u
  elif z==C:
   eP+=mp*w;ct=1-w
  else:
   act=choice(z)[1][0]
   if act=='P': eQ+=mq;continue
   if act=='Q': eP+=mp;continue
   assert act=='C'
   ct=F(1)
  tP+=mp*ct;tQ+=mq*ct
  if ct==0:continue
  for i,zz in enumerate(ch(z)):
   stack.append((zz,mp*ct*P[i],mq*ct*Q[i]))
 return (eP,eQ,tP,tQ),visits,hits
root0,n0,h0=dfs(U0,F(0))
root1,n1,h1=dfs(U1,F(1))
assert root0[0]==root0[1]==A0 and root0[2]==V0
assert root1[0]==root1[1]==A1 and root1[2]==V1
assert root0[2]>root0[3] and root1[2]>root1[3]
assert h0[A]==[120,F(390625,5971968),F(390625,20155392)]
assert h0[C]==[2258,F(28225,195689447424),F(28225,92876046336)]
assert h1[A]==h0[A] and h1[C]==h0[C]
D=choice((0,0,0))[0]
assert D==root0[2]+(K+L)*A0==root1[2]+(K+L)*A1
assert (root0[2]-root1[2])==(K+L)*(A1-A0)
print('PASS_STAGE108_AUTHOR_LITERAL_ORDERED_DFS',n0,n1)
