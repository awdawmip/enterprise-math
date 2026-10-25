#!/usr/bin/env python3
"""Independent N14 Stage99 rational Bellman minimization and ordered-word DFS audit."""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from math import factorial
import json
N=14;P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(6696,5);LP=F(6312,5);G=K+LP
A=(11,3,0);B=(12,0,1)
a0=F(2586269937332842327,7450150876955541504)
v0=F(757686022002985135,58204303726215168)
s0=F(12366057190345211,20889600000000000)
h=F(26961,108800);eta=F(107421875,2806920511488)
def child(s,i):
 n,a,b=s;return n+1,a+(i==0),b+(i==1)
@lru_cache(None)
def optimal(s):
 n,a,b=s
 d={'P':K*F(2**(a+b),3**a),'Q':LP}
 if n<N:d['C']=F(1)+sum((P[i]*optimal(child(s,i))[0] for i in range(3)),F())
 m=min(d.values());z=next(x for x in ('C','P','Q') if x in d and d[x]==m)
 return m,z,d

def hits(target):
 words=[]
 def go(s,p,q,word):
  if s==target:words.append((word,p,q));return
  if s[0]>=target[0] or optimal(s)[1]!='C':return
  for i in range(3):go(child(s,i),p*P[i],q*Q[i],word+(i,))
 go((0,0,0),F(1),F(1),())
 return words

def suffix(s):
 leaves=Counter(); eP=eQ=tP=tQ=F()
 def go(v,p,q,dt):
  nonlocal eP,eQ,tP,tQ
  z=optimal(v)[1]
  if z!='C':
   leaves[z]+=1
   if z=='Q':eP+=p
   else:eQ+=q
   tP+=dt*p;tQ+=dt*q;return
  for i in range(3):go(child(v,i),p*P[i],q*Q[i],dt+1)
 go(s,F(1),F(1),0)
 return sum(leaves.values()),(eP,eQ,tP,tQ)

def metr(u,s):
 @lru_cache(None)
 def rec(v):
  if v==A:
   c=continuation(v)
   return ((1-u)*c[0],u+(1-u)*c[1],(1-u)*c[2],(1-u)*c[3])
  if v==B:
   c=continuation(v)
   return (s+(1-s)*c[0],(1-s)*c[1],(1-s)*c[2],(1-s)*c[3])
  z=optimal(v)[1]
  if z=='P':return F(),F(1),F(),F()
  if z=='Q':return F(1),F(),F(),F()
  return continuation(v)
 def continuation(v):
  assert v[0]<N
  kids=[rec(child(v,i)) for i in range(3)]
  return (sum((P[i]*kids[i][0] for i in range(3)),F()),
   sum((Q[i]*kids[i][1] for i in range(3)),F()),
   F(1)+sum((P[i]*kids[i][2] for i in range(3)),F()),
   F(1)+sum((Q[i]*kids[i][3] for i in range(3)),F()))
 return rec((0,0,0))

def main():
 root=optimal((0,0,0))[0];gaps=[];ties=[]
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    v=n,a,b;d,z,choices=optimal(v)
    for zz,w in choices.items():
     if zz==z:continue
     gaps.append(w-d)
     if w==d:ties.append((v,z,zz))
 assert optimal.cache_info().currsize==680 and len(gaps)==1240
 assert len([x for x in gaps if x==0])==2 and sum(x>0 for x in gaps)==1238
 assert min(x for x in gaps if x>0)==F(12889,699840) and all(x>=0 for x in gaps)
 assert set(ties)=={(A,'C','P'),(B,'C','Q')}
 assert root==v0+G*a0
 AH=hits(A);BH=hits(B)
 assert len(AH)==165 and len(BH)==12
 pa=sum((p for w,p,q in AH),F()); qa=sum((q for w,p,q in AH),F())
 pb=sum((p for w,p,q in BH),F()); qb=sum((q for w,p,q in BH),F())
 assert (pa,qa)==(F(21484375,286654464),F(21484375,967458816))
 assert (pb,qb)==(F(48828125,725594112),F(48828125,362797056))
 SA=suffix(A); SB=suffix(B)
 assert SA==(9,(F(41,13824),F(569,576),F(69,64),F(167,144)))
 assert SB==(5,(F(63,64),F(1,144),F(9,8),F(13,12)))
 X=pa*SA[1][0];Y=qa*(1-SA[1][1]);E=pb*(1-SB[1][0]);H=qb*SB[1][1]
 assert h==(X+Y)/(E+H) and eta==E*h-X==Y-H*h and eta>0
 assert 0<s0<s0+h<1
 checks=[]
 for u in (F(),F(1,101),F(1,10),F(1,4),F(1,2),F(3,4),F(1)):
  ep,eq,tp,tq=metr(u,s0+h*u)
  assert ep==eq==a0+eta*u
  assert tp==v0-G*eta*u and tp>tq
  assert tp+LP*ep+K*eq==root
  checks.append([str(u),str(tp-tq)])
 return dict(status='PASS_EXACT_INDEPENDENT_BELLMAN_DFS',states=680,comparisons=1240,ties=str(ties),min_positive_gap=str(F(12889,699840)),A99_nominal=factorial(11)//(factorial(3)*factorial(8)),A99_firsthits=165, A99_masses=[str(pa),str(qa)],A99_suffixes=9,A99_truncated=165*9, A99_suffix_vector=list(map(str,SA[1])),B_masses=[str(pb),str(qb)],h=str(h),eta=str(eta),alpha99=str(a0+eta),V99=str(v0-G*eta),checks=checks)
if __name__=='__main__':print(json.dumps(main(),indent=2))
