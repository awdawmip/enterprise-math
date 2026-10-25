#!/usr/bin/env python3
"""Exact Stage100 author checker for external N=14 iid ordered-history minimax.
Computes Bellman actions, genuine first-hit word masses, continuation suffixes,
and interior randomized policies with fractions. No native BRC/X6 transfer.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from math import factorial
import json
N=14; P=(F(1,8),F(1,24),F(5,6)); Q=(F(1,12),F(1,12),F(5,6))
K=F(177963480,134551); LP=F(72)+F(8,9)*K; Gamma=K+LP
A=(9,5,1); B=(12,0,1)
a0=F(2586555057332842327,7450150876955541504)
v0=F(751890958002985135,58204303726215168)
s0=F(17542569190345211,20889600000000000)
h=F(64118999,54400000000); eta=F(117732125,808393107308544)
def child(s,i):
 n,a,b=s; return(n+1,a+(i==0),b+(i==1))
@lru_cache(None)
def optimal(s):
 n,a,b=s
 d={'P':K*F(2**(a+b),3**a),'Q':LP}
 if n<N:d['C']=F(1)+sum((P[i]*optimal(child(s,i))[0] for i in range(3)),F())
 m=min(d.values()); z=next(x for x in ('C','P','Q') if x in d and d[x]==m)
 return m,z,d

def first_hits(target):
 out=[]
 def dfs(s,w,p,q):
  if s==target:out.append((w,p,q));return
  if s[0]>=target[0] or optimal(s)[1]!='C':return
  for i in range(3):dfs(child(s,i),w+(i,),p*P[i],q*Q[i])
 dfs((0,0,0),(),F(1),F(1))
 return out

def suffix(s):
 leaves=Counter(); ep=eq=tp=tq=F()
 def visit(v,p,q,d):
  nonlocal ep,eq,tp,tq
  z=optimal(v)[1]
  if z!='C':
   leaves[z]+=1
   if z=='Q':ep+=p
   else:eq+=q
   tp+=d*p;tq+=d*q;return
  for i in range(3):visit(child(v,i),p*P[i],q*Q[i],d+1)
 visit(s,F(1),F(1),0)
 return sum(leaves.values()),(ep,eq,tp,tq)

def metrics(u,s):
 @lru_cache(None)
 def value(v):
  if v==A:
   c=cont(v);return tuple((1-u)*c[i]+u*(F(1) if i==1 else F()) for i in range(4))
  if v==B:
   c=cont(v);return tuple((1-s)*c[i]+s*(F(1) if i==0 else F()) for i in range(4))
  z=optimal(v)[1]
  if z=='P':return F(),F(1),F(),F()
  if z=='Q':return F(1),F(),F(),F()
  return cont(v)
 def cont(v):
  vals=[value(child(v,i)) for i in range(3)]
  return (sum((P[i]*vals[i][0] for i in range(3)),F()),
    sum((Q[i]*vals[i][1] for i in range(3)),F()),
    F(1)+sum((P[i]*vals[i][2] for i in range(3)),F()),
    F(1)+sum((Q[i]*vals[i][3] for i in range(3)),F()))
 return value((0,0,0))

def main():
 root=optimal((0,0,0))[0]; gaps=[];ties=[]
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    st=(n,a,b);d,z,opts=optimal(st)
    for other,v in opts.items():
     if other==z:continue
     gaps.append(v-d)
     if v==d:ties.append((st,z,other))
 assert optimal.cache_info().currsize==680 and len(gaps)==1240
 assert sum(g>0 for g in gaps)==1238 and all(g>=0 for g in gaps)
 assert min(g for g in gaps if g>0)==F(12889,807306)
 assert set(ties)=={(A,'C','P'),(B,'C','Q')}
 assert root==v0+Gamma*a0
 AH=first_hits(A);BH=first_hits(B)
 assert len(AH)==336 and len(BH)==12
 pa=sum((x[1] for x in AH),F());qa=sum((x[2] for x in AH),F())
 pb=sum((x[1] for x in BH),F());qb=sum((x[2] for x in BH),F())
 assert (pa,qa)==(F(875,3538944),F(875,13436928))
 assert (pb,qb)==(F(48828125,725594112),F(48828125,362797056))
 SA=suffix(A);SB=suffix(B)
 assert SA==(49,(F(17611,3981312),F(122033,124416),F(191287,165888),F(4543,3456)))
 assert SB==(5,(F(63,64),F(1,144),F(9,8),F(13,12)))
 assert A[1]>B[1] and A[0]<B[0]
 X=pa*SA[1][0];Y=qa*(1-SA[1][1]);E=pb*(1-SB[1][0]);H=qb*SB[1][1]
 assert h==(X+Y)/(E+H) and eta==E*h-X==Y-H*h and eta>0
 assert 0<s0<s0+h<1
 checks=[]
 for u in (F(),F(1,29),F(1,7),F(1,3),F(1,2),F(4,5),F(1)):
  ep,eq,tp,tq=metrics(u,s0+h*u)
  assert ep==eq==a0+eta*u and tp==v0-Gamma*eta*u and tp>tq
  assert tp+LP*ep+K*eq==root
  checks.append([str(u),str(tp-tq)])
 assert metrics(F(),s0)[2]-metrics(F(),s0)[3]==F(1137415722727759775,1862537719238885376)
 assert metrics(F(1),s0+h)[2]-metrics(F(1),s0+h)[3]==F(1137198023932879775,1862537719238885376)
 return dict(status='PASS_EXACT_BELLMAN_ORDERED_DFS',states=680,gaps=1240,ties=str(ties),min_positive_gap=str(F(12889,807306)),first_hits_A=len(AH),mass_A=[str(pa),str(qa)],suffixes_A=SA[0],truncated=len(AH)*SA[0],first_hits_B=len(BH),h=str(h),eta=str(eta),alpha100=str(a0+eta),V100=str(v0-Gamma*eta),s100=str(s0+h),checks=checks)
if __name__=='__main__':print(json.dumps(main(),indent=2))
