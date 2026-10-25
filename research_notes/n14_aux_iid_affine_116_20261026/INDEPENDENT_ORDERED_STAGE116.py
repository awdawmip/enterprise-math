#!/usr/bin/env python3
"""Independent exact integer-weight DFS of literal ordered prefixes (N14)."""
from fractions import Fraction as F
from functools import lru_cache
N=14;K=F(37550061,41440);L=F(3296576,3885);D=(9,1,2);T=(14,7,4)
p=(3,1,20);q=(1,1,10);PN=24**N;QN=12**N
def child(s,j):
 n,a,b=s;return (n+1,a+(j==0),b+(j==1))
@lru_cache(None)
def B(s):
 n,a,b=s;c=[K*F(2**(a+b),3**a),L]
 if n<N:c.append(1+sum(F(p[i],24)*B(child(s,i)) for i in range(3)))
 return min(c)
act={};ties=[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);c=[('P',K*F(2**(a+b),3**a)),('Q',L)]
   if n<N:c.append(('C',1+sum(F(p[i],24)*B(child(s,i)) for i in range(3))))
   names=[name for name,v in c if v==B(s)]
   act[s]=names[0]
   if len(names)>1:ties.append((s,names))
assert ties==[(D,['Q','C']),(T,['P','Q'])]
def run(w,z):
 ep=eq=tp=tq=nodes=0
 first={D:[0,0,0],T:[0,0,0]}
 def dfs(s,px,qx):
  nonlocal ep,eq,tp,tq,nodes
  nodes+=1;n=s[0]
  if s in first:
   c=first[s];c[0]+=1;c[1]+=px*24**(N-n);c[2]+=qx*12**(N-n)
  action=('Q' if w else 'C') if s==D else ('P' if z else 'Q') if s==T else act[s]
  if action!='C':
   pm=px*24**(N-n);qm=qx*12**(N-n)
   if action=='Q':ep+=pm
   if action=='P':eq+=qm
   tp+=n*pm;tq+=n*qm
   return
  assert n<N
  for i in range(3):dfs(child(s,i),px*p[i],qx*q[i])
 dfs((0,0,0),1,1)
 return (F(ep,PN),F(eq,QN),F(tp,PN),F(tq,QN)), \
     {s:(a[0],F(a[1],PN),F(a[2],QN)) for s,a in first.items()},nodes
c={}
for w,z in ((0,0),(1,0),(0,1),(1,1)):
 m,h,n=run(w,z);c[w,z]=m
 assert h[D]==(172,F(671875,53747712),F(671875,20155392))
 assert h[T]==(9830,F(614375,75144747810816),F(614375,80244904034304))
 assert n in (862459,854719)
base=c[0,0]
dw=tuple(c[1,0][i]-base[i] for i in range(4))
dz=tuple(c[0,1][i]-base[i] for i in range(4))
mix=tuple(c[1,1][i]-c[1,0][i]-c[0,1][i]+base[i] for i in range(4))
assert dw==(F(593265625,5283615080448),F(-430671875,5015306502144),F(-34607609375,1981355655168),F(-17355203125,417942208512))
assert dz==(F(-614375,75144747810816),F(614375,80244904034304),F(0),F(0))
assert mix==(F(0),)*4
print('PASS_STAGE116_LITERAL_WORD_INTEGER_CHECK')
