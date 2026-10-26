#!/usr/bin/env python3
"""Exact author-side Stage152 Bellman and ordered-history observer verification.
The model is external auxiliary ternary iid N14; no native X6 identification.
No external dependencies. Python 3.9+.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import product
import json
P=(F(1,8),F(1,24),F(5,6))
Q=(F(1,12),F(1,12),F(5,6))
PW=(3,1,20); QW=(1,1,10)
N=14
K=F(12844717560,36346217);L=F(12768141608,36346217)
B=(11,0,1); W=(8,3,3)
alpha151=F(18373001785623238325,52808422392537808896)
V151=F(318746112099955105013,26404211196268904448)

def child(s,i):
 n,a,b=s;return (n+1,a+(i==0),b+(i==1))
def states():
 for n in range(N+1):
  for a in range(n+1):
   for b in range(n-a+1):
    yield n,a,b

def ratio(s):
 n,a,b=s;return F(2**(a+b),3**a)
@lru_cache(None)
def dual(s):
 n,a,b=s
 acts={'P':K*ratio(s),'Q':L}
 if n<N: acts['C']=1+sum(P[i]*dual(child(s,i))[0] for i in range(3))
 v=min(acts.values()); return v,tuple(x for x,y in acts.items() if y==v), acts

infos={s:dual(s) for s in states()}
ties={s:info[1] for s,info in infos.items() if len(info[1])>1}
assert ties=={B:('Q','C'),W:('Q','C')},ties
pos=[v-u for s,(u,act,opts) in infos.items() for v in opts.values() if v>u]
assert len(infos)==680 and len(pos)==1238
assert min(pos)==F(204027667,1130512733568),min(pos)
assert dual((0,0,0))[0]==F(341463027624594134301829727,1327376472826305935572992)

# NOTE choose corner coin 0 = continue, coin 1 = Q stop at tie.
def action(s,b,w):
 if s==B:return 'Q' if b else 'C'
 if s==W:return 'Q' if w else 'C'
 return dual(s)[1][0]
ZERO=(F(0),)*4
@lru_cache(None)
def observer(s,b,w):
 a=action(s,b,w)
 if a=='P':return (F(0),F(1),F(0),F(0))
 if a=='Q':return (F(1),F(0),F(0),F(0))
 m=[observer(child(s,i),b,w) for i in range(3)]
 return (sum(P[i]*m[i][0] for i in range(3)),
         sum(Q[i]*m[i][1] for i in range(3)),
         1+sum(P[i]*m[i][2] for i in range(3)),
         1+sum(Q[i]*m[i][3] for i in range(3)))
M={(b,w):observer((0,0,0),b,w) for b,w in product((0,1),repeat=2)}
def vsum(*lst):return tuple(sum(values) for values in zip(*lst))
def vdiff(a,b):return tuple(x-y for x,y in zip(a,b))
m00=M[(0,0)];dB=vdiff(M[(1,0)],m00);dW=vdiff(M[(0,1)],m00)
assert vsum(m00,dB,dW)==M[(1,1)]

# independent ordered-prefix integer DFS. Direct tree paths, integer likelihood weights;
# denominators P=24^14, Q=12^14 for full lengths; do not merge prefixes.
# recurse actual branches; at a terminal t, eP and eQ numerator accumulates
# initial-history P mass and Q mass; sample-time accumulates depth.
# Time in caller's distribution remains sum_{prefixes} mass*depth.
def literal_dfs(b,w):
 vals=[F(0),F(0),F(0),F(0)]
 stack=[((0,0,0),1,1)]
 nodes=0
 while stack:
  s,pn,qn=stack.pop();nodes+=1
  n=s[0];assert n<=N
  act=action(s,b,w)
  if act=='C':
   for i in range(3):stack.append((child(s,i),pn*PW[i],qn*QW[i]))
  else:
   p=F(pn,24**n);q=F(qn,12**n)
   if act=='Q':vals[0]+=p
   else:vals[1]+=q
   vals[2]+=p*n; vals[3]+=q*n
 return tuple(vals),nodes
DFS={}
for bw in product((0,1),repeat=2):
 v,n=literal_dfs(*bw)
 assert v==M[bw],(bw,v,M[bw]);DFS[bw]=n
# First-hit of tie states under deterministic strict actions. Do not continue past any tie.
# We need ordered literal prefix path counts and probability masses under both P & Q.
def first_hits():
 stack=[((0,0,0),1,1)]
 hit={B:[0,F(0),F(0)],W:[0,F(0),F(0)]}
 while stack:
  s,pn,qn=stack.pop();n=s[0]
  if s in hit:
   hit[s][0]+=1;hit[s][1]+=F(pn,24**n);hit[s][2]+=F(qn,12**n)
   continue
  if dual(s)[1][0]=='C':
   for i in range(3): stack.append((child(s,i),pn*PW[i],qn*QW[i]))
 return hit
hits=first_hits()
# Equal error solve eP-eQ=D00 + b DB + w DW=0.
D00=m00[0]-m00[1]; DB=dB[0]-dB[1];DW=dW[0]-dW[1]
assert DB!=0
b0=-D00/DB; beta=-DW/DB
# b(w)=b0+beta*w; solve legal interval [0,1] in w as rational linear inequality.
lo=F(0);hi=F(1)
for a,c in ((b0,beta),(1-b0,-beta)):
 if c>0:lo=max(lo,-a/c)
 elif c<0:hi=min(hi,-a/c)
 else:assert a>=0
assert lo<=hi

def mix(w):
 b=b0+beta*w
 v=vsum(m00,tuple(b*x for x in dB),tuple(w*x for x in dW))
 assert v[0]==v[1]
 return b,v
left=mix(lo);right=mix(hi)
H=dual((0,0,0))[0]
def dual_eval(m): return m[2]+L*m[0]+K*m[1]

def jfrac(x):return str(x.numerator)+'/'+str(x.denominator)
def jvec(v):return [jfrac(x) for x in v]
result={
  'model':'EXTERNAL_AUXILIARY_IID_TERNARY_N14',
  'K':jfrac(K),'L':jfrac(L),'H_root':jfrac(H),
  'bellman_states':len(infos),'ties':{str(s):list(v) for s,v in ties.items()},
  'strict_gap_count':len(pos),'strict_gap_min':jfrac(min(pos)),
  'corners':{f'b={b},w={w}':jvec(M[(b,w)]) for b,w in product((0,1),repeat=2)},
  'corner_dfs_nodes':{str(bw):DFS[bw] for bw in DFS},
  'M00':jvec(m00),'dB':jvec(dB),'dW':jvec(dW),
  'mixed_fourvector':jvec(vdiff(M[(1,1)],vsum(m00,dB,dW))),
  'first_hits':{str(k):{'ordered_count':v[0],'P_mass':jfrac(v[1]),'Q_mass':jfrac(v[2])} for k,v in hits.items()},
  'compensation':{'b_intercept':jfrac(b0),'b_slope_w':jfrac(beta),'w_min':jfrac(lo),'w_max':jfrac(hi)},
  'endpoints':{'lower':{'w':jfrac(lo),'b':jfrac(left[0]),'M':jvec(left[1]),'dual_value':jfrac(dual_eval(left[1]))},'upper':{'w':jfrac(hi),'b':jfrac(right[0]),'M':jvec(right[1]),'dual_value':jfrac(dual_eval(right[1]))}},
  'stage151_bridge':{'alpha151':jfrac(alpha151),'V151':jfrac(V151),'matches_lower':left[1][0]==alpha151 and max(left[1][2:])==V151},
  'dual_equality_lower':dual_eval(left[1])==H,'dual_equality_upper':dual_eval(right[1])==H,
  'time_P_dominates_both_endpoints':left[1][2]>=left[1][3] and right[1][2]>=right[1][3]
}
with open('certificate152.json','w') as f:json.dump(result,f,indent=2,ensure_ascii=False)
print(json.dumps(result,indent=2))
