#!/usr/bin/env python3
"""Independent full 954-event randomized optimal-path recourse sanity check."""
import random
from VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE import *
random.seed(20261115)
x,cuts=frozen();tests=0

def full_cost(z,S):
 ds=[min(abs(z[t]-z[c]) for c in S) for t in range(len(z))]
 return max(ds),sum(ds)
for bit,k,other in [(25,223,0),(25,250,1<<27),(25,291,1<<27),(27,214,1<<3),(27,221,(1<<3)|(1<<8)|(1<<9)|(1<<10)),(27,222,0),(27,270,1<<25)]:
 mask=(1<<bit)|other;zn=close(x,cuts,mask);zo=close(x,cuts,other)
 out,C,D,J=paths_dp(zn,k);inc,_,pref,tail=graph(zn)
 for rep in range(8):
  best=J[k-1];j=random.choice([j for j in range(len(zn)) if C[k-1][j]+tail[j]==best]);S=[j]
  for t in range(k-1,0,-1):
   j=random.choice([i for i,w in inc[j] if C[t-1][i]+w==C[t][j]]);S.append(j)
  S=sorted(S); i=cuts[bit]; P=tuple(j for j in S if i-9<=j<=i+9)
  num,swap=repair(P,zn,zo,i)
  assert num in (0,1),(bit,k,num)
  if num==1:
   p,q=swap;T=(set(S)-{p})|{q}
  else:T=set(S)
  assert len(T)==k and full_cost(zn,S)==(2,best) and full_cost(zo,T)==(2,best),(bit,k,num,full_cost(zo,T),best)
  tests+=1
print('PASS_R5_FULL_PATH_RANDOM_CROSSCHECK',tests)
