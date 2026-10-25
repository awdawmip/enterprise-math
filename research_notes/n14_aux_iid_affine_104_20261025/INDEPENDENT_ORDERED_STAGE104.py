#!/usr/bin/env python3
"""Independent author top-down Bellman and FULL ordered-word DFS for external iid Stage104.
Uses no state/policy table imported from CHECKER_STAGE104.py.
"""
from fractions import Fraction as R
from functools import lru_cache
h=(R(1,8),R(1,24),R(5,6))
g=(R(1,12),R(1,12),R(5,6))
K=R(4881384,4373);L=72+R(8,9)*K
A=(11,8,3);B=(12,0,1)
s0=R(16415412204181171,20889600000000000)
s1=R(4103853056103079,5222400000000000)
a0=R(2586593886011416687,7450150876955541504)
a1=R(646648471503178867,1862537719238885376)
t0=R(3004643576828511655,232817214904860672)
t1=R(6009287153480025269,465634429809721344)
@lru_cache(None)
def v(n,a,b):
 costs=[('P',K*R(2**(a+b),3**a)),('Q',L)]
 if n<14:costs.append(('C',1+h[0]*v(n+1,a+1,b)[0]+h[1]*v(n+1,a,b+1)[0]+h[2]*v(n+1,a,b)[0]))
 best=min(z for _,z in costs)
 return best,tuple(act for act,z in costs if z==best)
tie_states={ (n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1) if len(v(n,a,b)[1])>1 }
assert tie_states=={A,B}
def action(n,a,b):
 if (n,a,b)==A:return 'C'
 return v(n,a,b)[1][0]
# Explicit true ordered first hit prefix traversal (do not silently count non-reaching prefixes).
hits={A:[0,R(0),R(0)],B:[0,R(0),R(0)]}
def first(n,a,b,pw,qw):
 state=(n,a,b)
 if state in hits:
  z=hits[state];z[0]+=1;z[1]+=pw;z[2]+=qw;return
 if action(n,a,b)!='C':return
 for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
  first(n+1,aa,bb,pw*h[j],qw*g[j])
first(0,0,0,R(1),R(1))
assert hits[A]==[66,R(11,38654705664),R(11,123834728448)]
assert hits[B]==[12,R(48828125,725594112),R(48828125,362797056)]
# Explicit forced-continuation suffix word traversal.
def suffix(state):
 out=[R(0)]*4;terminal=[0]
 def dive(n,a,b,pw,qw):
  act=action(n,a,b)
  if act=='P':out[1]+=qw
  elif act=='Q':out[0]+=pw
  else:
   for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
    dive(n+1,aa,bb,pw*h[j],qw*g[j])
   return
  out[2]+=pw*(n-state[0]);out[3]+=qw*(n-state[0]);terminal[0]+=1
 n,a,b=state
 for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
  dive(n+1,aa,bb,h[j],g[j])
 return tuple(out)+(terminal[0],)
assert suffix(A)==(R(41,13824),R(569,576),R(69,64),R(167,144),9)
assert suffix(B)==(R(63,64),R(1,144),R(9,8),R(13,12),5)
# Enumerate every reached ORDERED observation prefix; sum true stopping outputs.
def full(u,s):
 sums=[R(0)]*4;nodes=[0];leaves=[0]
 def dfs(n,a,b,pw,qw):
  nodes[0]+=1
  state=(n,a,b)
  if state==A:
   sums[1]+=qw*u;sums[2]+=pw*u*n;sums[3]+=qw*u*n
   pw*=1-u;qw*=1-u;act='C'
  elif state==B:
   sums[0]+=pw*s;sums[2]+=pw*s*n;sums[3]+=qw*s*n
   pw*=1-s;qw*=1-s;act='C'
  else:act=action(n,a,b)
  if pw==0 and qw==0:return
  if act=='P':
   sums[1]+=qw;sums[2]+=pw*n;sums[3]+=qw*n;leaves[0]+=1;return
  if act=='Q':
   sums[0]+=pw;sums[2]+=pw*n;sums[3]+=qw*n;leaves[0]+=1;return
  for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
   dfs(n+1,aa,bb,pw*h[j],qw*g[j])
 dfs(0,0,0,R(1),R(1))
 return tuple(sums),nodes[0],leaves[0]
for u,s,a,t in [(R(0),s0,a0,t0),(R(1),s1,a1,t1),(R(1,2),(s0+s1)/2,(a0+a1)/2,(t0+t1)/2)]:
 result,nodes,leaves=full(u,s)
 assert result[0]==result[1]==a and result[2]==t and result[2]>result[3]
 print('PASS u=',u,'ordered nodes=',nodes,'terminal words=',leaves,'alpha=',a,'tP=',t,'tQ=',result[3])
print('PASS_INDEPENDENT_ORDERED_STAGE104')
