#!/usr/bin/env python3
"""Exact external Stage176 author reference. stdlib only. No Source admission."""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F

N=14
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
K=F(1696807920718753587,7487608294325270)
L=F(168348947995801752,748760829432527)
H=F(1733492029996286794626721771839535,10254377114019668494551279992832)
W,T=(4,1,2),(8,2,0)
A=('P','Q','C')
def nxt(s,i):return s[0]+1,s[1]+int(i==0),s[2]+int(i==1)
def ratio(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
@lru_cache(None)
def bell(s):
    v=[K*ratio(s),L]
    if s[0]<N:v.append(1+sum((P[i]*bell(nxt(s,i))[0] for i in range(3)),F(0)))
    m=min(v)
    return m,tuple(a for a,x in zip(A,v) if x==m),v
strict,ties,gaps={},{},[]
for n in range(N+1):
 for a in range(n+1):
  for b in range(n-a+1):
   s=(n,a,b);v,w,options=bell(s)
   if len(w)>1:ties[s]=w
   else:strict[s]=w[0]
   gaps.extend(x-v for x in options if x>v)
assert len(strict)+len(ties)==680
assert ties=={W:('Q','C'),T:('P','C')}
assert len(gaps)==1238 and min(gaps)==F(152464420746873000396113,4292712684503529027010560)
assert bell((0,0,0))[0]==H

def decision(s,w,t):
 if s==W:return 'Q' if w else 'C'
 if s==T:return 'P' if t else 'C'
 return strict[s]

def suffix(w,t):
 @lru_cache(None)
 def rec(s):
  act=decision(s,w,t)
  if act=='P':return F(0),F(1),F(0),F(0)
  if act=='Q':return F(1),F(0),F(0),F(0)
  ch=[rec(nxt(s,i)) for i in range(3)]
  return (sum((P[i]*ch[i][0] for i in range(3)),F(0)),
          sum((Q[i]*ch[i][1] for i in range(3)),F(0)),
          1+sum((P[i]*ch[i][2] for i in range(3)),F(0)),
          1+sum((Q[i]*ch[i][3] for i in range(3)),F(0)))
 return rec((0,0,0))

def dfs(w,t):
 sums=defaultdict(int)
 first={W:[0,F(0),F(0)],T:[0,F(0),F(0)]}
 nodes=0
 def walk(n,a,b,p,q):
  nonlocal nodes
  nodes+=1;s=(n,a,b)
  if s in first:
   h=first[s];h[0]+=1;h[1]+=F(p,24**n);h[2]+=F(q,12**n)
  op=decision(s,w,t)
  if op=='C':
   assert n<N
   for i in range(3):walk(n+1,a+(i==0),b+(i==1),p*(3,1,20)[i],q*(1,1,10)[i])
  else:
   sums[n,'mp']+=p;sums[n,'mq']+=q;sums[n,'tp']+=n*p;sums[n,'tq']+=n*q
   sums[n,'ep' if op=='Q' else 'eq']+=p if op=='Q' else q
 walk(0,0,0,1,1)
 m=lambda tag,d:sum((F(sums[n,tag],d**n) for n in range(N+1)),F(0))
 assert m('mp',24)==m('mq',12)==1
 return (m('ep',24),m('eq',12),m('tp',24),m('tq',12)),first,nodes

corners={};nodes={};first=None
for w in (0,1):
 for t in (0,1):
  v,h,n=dfs(w,t)
  assert v==suffix(w,t)
  corners[w,t]=v;nodes[w,t]=n
  if first is None:first=h
  else:assert first==h
assert W[2]>T[2] and W[0]<T[0]
assert first[W]==[8,F(5,3456),F(5,1296)]
assert first[T]==[28,F(109375,746496),F(109375,1679616)]
assert nodes=={(0,0):282916,(0,1):279052,(1,0):267580,(1,1):263716}
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
M=corners[0,0];dW=sub(corners[1,0],M);dT=sub(corners[0,1],M)
assert sub(sub(corners[1,1],corners[1,0]),dT)==(F(0),)*4
D=lambda v:v[0]-v[1]
t0=-D(M)/D(dT);ts=-D(dW)/D(dT)
assert t0==F(1768756796217217,3860125696000000)
assert ts==F(4588038935639,193006284800000)
assert 0<t0<t0+ts<1
obs=lambda w:tuple(M[i]+w*dW[i]+(t0+ts*w)*dT[i] for i in range(4))
left,right=obs(F(0)),obs(F(1))
assert left[0]==left[1]==F(5147935054057228427975,14750257906470044565504)
assert right[0]==right[1]==F(5148159682306058186075,14750257906470044565504)
assert left[2]==F(338938781942537717887145,29500515812940089131008)
assert right[2]==F(338735964098497111620725,29500515812940089131008)
assert left[2]>left[3] and right[2]>right[3]
assert all(v[2]+K*v[1]+L*v[0]==H for v in (left,right))
width=right[0]-left[0]
assert width==F(18719020735813175,1229188158872503713792)>0
assert K+L==F(3380297400676771107,7487608294325270)
assert right[2]-left[2]==-(K+L)*width
print('STAGE176_FULL_REAL_REFERENCE_PASS')
