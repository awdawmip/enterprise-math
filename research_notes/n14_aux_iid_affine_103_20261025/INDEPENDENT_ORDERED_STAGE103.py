#!/usr/bin/env python3
"""Independent author cross-check: top-down recursive Bellman + explicit ordered DFS.
External iid N=14 only; exact rational arithmetic. No shared policy table imported.
"""
from fractions import Fraction as F
from functools import lru_cache
P=(F(1,8),F(1,24),F(5,6));Q=(F(1,12),F(1,12),F(5,6))
K=F(152847928260,128768917);L=72+F(8,9)*K
C=(6,2,3);B=(12,0,1)
S0=F(16418222843481211,20889600000000000)
S1=F(16415412204181171,20889600000000000)
A0=F(2586593746940986327,7450150876955541504)
A1=F(2586593886011416687,7450150876955541504)
T0=F(751163408448101635,58204303726215168)
T1=F(3004643576828511655,232817214904860672)
@lru_cache(None)
def value(n,a,b):
 costs=[('P',K*F(2**(a+b),3**a)),('Q',L)]
 if n<14:costs.append(('C',1+P[0]*value(n+1,a+1,b)[0]+P[1]*value(n+1,a,b+1)[0]+P[2]*value(n+1,a,b)[0]))
 v=min(x for _,x in costs)
 return v,tuple(t for t,x in costs if x==v)
state_count=0;tied=[]
for n in range(15):
 for a in range(n+1):
  for b in range(n-a+1):
   _,ops=value(n,a,b);state_count+=1
   if len(ops)>1:tied.append(((n,a,b),ops))
assert state_count==680 and {x[0] for x in tied}=={B,C}

# DFS enumerates genuinely ordered observation words to the first tie or strict stop.
hits={C:[0,F(0),F(0)],B:[0,F(0),F(0)]}
def prefix(n,a,b,wp,wq):
 v=(n,a,b)
 if v in hits:
  z=hits[v];z[0]+=1;z[1]+=wp;z[2]+=wq;return
 if value(n,a,b)[1][0]!='C':return
 for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
  prefix(n+1,aa,bb,wp*P[j],wq*Q[j])
prefix(0,0,0,F(1),F(1))
assert hits[C]==[36,F(5,147456),F(5,41472)]
assert hits[B]==[12,F(48828125,725594112),F(48828125,362797056)]

# Ordered suffix DFS enumerates every stopping path after forcing continue at a tie.
def suffix(v):
 n,a,b=v; res=[F(0)]*4;num=[0]
 def dive(n,a,b,wp,wq):
  op=value(n,a,b)[1][0]
  if op=='P':res[1]+=wq;res[2]+=wp*(n-v[0]);res[3]+=wq*(n-v[0]);num[0]+=1;return
  if op=='Q':res[0]+=wp;res[2]+=wp*(n-v[0]);res[3]+=wq*(n-v[0]);num[0]+=1;return
  for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
   dive(n+1,aa,bb,wp*P[j],wq*Q[j])
 for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
  dive(n+1,aa,bb,P[j],Q[j])
 return tuple(res)+(num[0],)
assert suffix(C)==(F(1352536571,1358954496),F(381917,429981696),F(267429265,169869312),F(47809387,35831808),279)
assert suffix(B)==(F(63,64),F(1,144),F(9,8),F(13,12),5)

# Independently enumerate all ordered stopping histories (including randomized tie action).
# Probabilities wp/wq are exact prefix word probabilities times survival factors.
def total(u,s):
 res=[F(0)]*4;nodes=[0];leaves=[0]
 def dive(n,a,b,wp,wq):
  nodes[0]+=1
  v=(n,a,b)
  if v==C or v==B:
   t=u if v==C else s
   res[0]+=wp*t;res[2]+=wp*t*n;res[3]+=wq*t*n
   wp*=1-t;wq*=1-t
   if wp==0 and wq==0:return
   act='C'
  else:act=value(n,a,b)[1][0]
  if act=='P':res[1]+=wq;res[2]+=wp*n;res[3]+=wq*n;leaves[0]+=1;return
  if act=='Q':res[0]+=wp;res[2]+=wp*n;res[3]+=wq*n;leaves[0]+=1;return
  for j,(aa,bb) in enumerate(((a+1,b),(a,b+1),(a,b))):
   dive(n+1,aa,bb,wp*P[j],wq*Q[j])
 dive(0,0,0,F(1),F(1))
 return tuple(res),nodes[0],leaves[0]
for u,s,alpha,tt in [(F(0),S0,A0,T0),(F(1),S1,A1,T1)]:
 got,nodes,leaves=total(u,s)
 assert got[0]==got[1]==alpha and got[2]==tt and got[2]>got[3]
 print('PASS endpoint',int(u),'ordered_prefix_nodes',nodes,'stopping_histories',leaves,'alpha',alpha,'tp',got[2])
print('PASS_INDEPENDENT_ORDERED_STAGE103; first-hit and suffix DFS confirmed')
