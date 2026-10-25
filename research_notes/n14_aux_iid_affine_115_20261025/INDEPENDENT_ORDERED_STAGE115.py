#!/usr/bin/env python3
"""Independent literal ordered-prefix integer-mass DFS, no imports from primary."""
from fractions import Fraction as F
from functools import lru_cache
N=14; K=F(2533113,2734); L=F(1181272,1367)
D=(9,1,2);E=(12,4,1);PN=24**N;QN=12**N
pbr=(3,1,20);qbr=(1,1,10)
def move(s,i):
 n,a,b=s
 return n+1,a+(i==0),b+(i==1)
@lru_cache(None)
def B(s):
 n,a,b=s
 v=[K*F(2**(a+b),3**a),L]
 if n<N:v.append(1+sum(F(w,24)*B(move(s,i)) for i,w in enumerate(pbr)))
 return min(v)
act={};ties=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b)
   vals=[('P',K*F(2**(a+b),3**a)),('Q',L)]
   if n<N:vals.append(('C',1+sum(F(w,24)*B(move(s,i)) for i,w in enumerate(pbr))))
   q=[name for name,value in vals if value==B(s)]
   if len(q)>1:ties.append((s,q))
   act[s]=q[0]
assert ties==[(D,['Q','C']),(E,['P','C'])]
def run(w,v):
 EP=EQ=TP=TQ=0
 first={D:[0,0,0],E:[0,0,0]}
 leaves=nodes=0
 def dfs(s,px,qx):
  nonlocal EP,EQ,TP,TQ,leaves,nodes
  nodes+=1
  n,a,b=s
  if s in first:
   f=first[s];f[0]+=1;f[1]+=px*24**(N-n);f[2]+=qx*12**(N-n)
  action=('Q' if w else 'C') if s==D else ('P' if v else 'C') if s==E else act[s]
  if action!='C':
   leaves+=1
   pm=px*24**(N-n);qm=qx*12**(N-n)
   if action=='Q':EP+=pm
   else:EQ+=qm
   TP+=n*pm;TQ+=n*qm
   return
  assert n<N
  for i in range(3):dfs(move(s,i),px*pbr[i],qx*qbr[i])
 dfs((0,0,0),1,1)
 return ((F(EP,PN),F(EQ,QN),F(TP,PN),F(TQ,QN)),
         {s:(x[0],F(x[1],PN),F(x[2],QN)) for s,x in first.items()},leaves,nodes)
c={}
for w,v in ((0,0),(1,0),(0,1),(1,1)):
 m,first,leaves,nodes=run(w,v)
 c[(w,v)]=m
 print('corner',w,v,'first',first,'leaves',leaves,'nodes',nodes)
 assert first[D]==(172,F(671875,53747712),F(671875,20155392))
 assert first[E]==(3048,F(9921875,1146617856),F(9921875,2902376448))
b=c[(0,0)]
dw=tuple(c[(1,0)][i]-b[i] for i in range(4))
dv=tuple(c[(0,1)][i]-b[i] for i in range(4))
mixed=tuple(c[(1,1)][i]-c[(1,0)][i]-c[(0,1)][i]+b[i] for i in range(4))
assert mixed==(F(0),)*4
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert dv==(F(-9921875,660451885056),F(9921875,417942208512),F(-248046875,27518828544),F(-128984375,34828517376))
print('PASS_STAGE115_INDEPENDENT_INTEGER_LITERAL_DFS')
