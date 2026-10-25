#!/usr/bin/env python3
"""Independent author implementation: explicit ordered-word DFS, exact Fraction arithmetic.

Unlike CHECKER.py's count-weight propagation, this directly traverses each reached
ordered word and propagates P/Q probabilities separately. Not an independent
Research Driver review.
"""
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(17496,13);LP=F(16488,13);N=14
A=(13,6,4);B=(12,0,1)
alpha97=F(2586269934456514327,7450150876955541504)
V97=F(757686080746453135,58204303726215168)
s97=F(12365744850625211,20889600000000000)
h=F(2602831,174080000000)
eta=F(4993625,12934289716936704)
def child(v,i):
 n,a,b=v;return n+1,a+(i==0),b+(i==1)
@lru_cache(None)
def bell(v):
 n,a,b=v
 opts={'P':K*F(2**(a+b),3**a),'Q':LP}
 if n<N:opts['C']=1+sum(P[i]*bell(child(v,i))[0] for i in range(3))
 val=min(opts.values())
 z=next(x for x in ('C','P','Q') if x in opts and opts[x]==val)
 return val,z
def walk(u):
 s=s97+h*u
 metrics=[F(),F(),F(),F()]
 hitsA=set();hitsB=set();leaves=0
 def visit(v,p,q,word,seen):
  nonlocal leaves
  n,a,b=v
  if v==A:
   assert 'B' not in seen
   hitsA.add(word)
   metrics[0]+=p*(1-u)
   if u==0:return
   p*=u;q*=u
   seen=seen+('A',)
  elif v==B:
   assert 'A' not in seen
   hitsB.add(word)
   metrics[0]+=p*s
   if s==1:return
   p*=1-s;q*=1-s
   seen=seen+('B',)
  else:
   z=bell(v)[1]
   if z=='P':metrics[1]+=q;leaves+=1;return
   if z=='Q':metrics[0]+=p;leaves+=1;return
  assert n<N
  metrics[2]+=p;metrics[3]+=q
  for i in range(3):
   visit(child(v,i),p*P[i],q*Q[i],word+str(i),seen)
 visit((0,0,0),F(1),F(1),'',())
 assert len(hitsA)==18438 and len(hitsB)==12 and not hitsA.intersection(hitsB)
 return tuple(metrics),len(hitsA),len(hitsB),leaves
if __name__=='__main__':
 for u in (F(),F(1,5),F(1,2),F(1)):
  (ep,eq,tp,tq),na,nb,leaves=walk(u)
  assert ep==eq==alpha97+eta*u
  assert tp==V97-(LP+K)*eta*u and tp>tq
  print('PASS u=',u,'e=',ep,'tP=',tp,'P-Q time=',tp-tq,
        'A/B first hits=',na,nb,'terminal words=',leaves)
