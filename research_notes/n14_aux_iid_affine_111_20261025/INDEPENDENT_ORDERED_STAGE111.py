#!/usr/bin/env python3
"""Stage111 second author implementation: top-down exact Bellman and literal ordered paths."""
from fractions import Fraction as F
from functools import lru_cache
p=(F(1,8),F(1,24),F(5,6));q=(F(1,12),F(1,12),F(5,6))
K=F(328788597439629,341261245318);L=F(155234629311000,170630622659)
A=(10,3,0);T=(4,0,2)
u0=F(159869038712303,211315200000000)
du=F(16351264081,88048000000)
a0=F(13084102571183753507,37682150988866125824)
eta=F(609395080925,43613600681558016)
v0=F(1934432098641265410385,150728603955464503296)
gamma=F(91322550865947,48751606474)
@lru_cache(None)
def dp(n,a,b):
 c={'P':K*F(2**(a+b),3**a),'Q':L}
 if n<14:c['C']=1+sum((p[j]*dp(n+1,a+(j==0),b+(j==1))[0] for j in range(3)),F(0))
 m=min(c.values())
 return m,tuple(k for k in c if c[k]==m)
assert dp(0,0,0)[0]==v0+gamma*a0
assert dp.cache_info().currsize==680
assert {(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(dp(n,a,b)[1])>1}=={A,T}
def act(z):return 'C' if z in (A,T) else dp(*z)[1][0]
def exhaustive(w):
 u=u0+du*w
 result=[F(0)]*4
 hit={A:[0,F(0),F(0)],T:[0,F(0),F(0)]}
 nodes=[0,0]
 def go(n,a,b,Pmass,Qmass):
  z=(n,a,b);nodes[0]+=1
  if z in hit:
   h=hit[z];h[0]+=1;h[1]+=Pmass;h[2]+=Qmass
  if z==A:
   result[1]+=Qmass*u
   result[2]+=Pmass*u*n;result[3]+=Qmass*u*n
   Pmass*=1-u;Qmass*=1-u;choice='C'
  elif z==T:
   result[0]+=Pmass*w
   result[2]+=Pmass*w*n;result[3]+=Qmass*w*n
   Pmass*=1-w;Qmass*=1-w;choice='C'
  else:choice=act(z)
  if Pmass==Qmass==0:return
  if choice=='P':
   result[1]+=Qmass;result[2]+=Pmass*n;result[3]+=Qmass*n;nodes[1]+=1
  elif choice=='Q':
   result[0]+=Pmass;result[2]+=Pmass*n;result[3]+=Qmass*n;nodes[1]+=1
  else:
   for j in range(3):go(n+1,a+(j==0),b+(j==1),Pmass*p[j],Qmass*q[j])
 go(0,0,0,F(1),F(1))
 eP,eQ,tP,tQ=result
 assert eP==eQ==a0+eta*w
 assert tP==v0-gamma*eta*w>tQ
 assert hit[A]==[120,F(390625,5971968),F(390625,20155392)]
 assert hit[T]==[6,F(25,3456),F(25,864)]
 print('INDEPENDENT_ORDERED_PASS',w,'nodes',nodes[0],'leaves',nodes[1],'moments',tuple(result),'first_hit',hit)
 return tuple(result),nodes
assert exhaustive(F(0))[1]==[903895,602597]
assert exhaustive(F(1))[1]==[889909,593267]
print('PASS_STAGE111_INDEPENDENT_LITERAL')
