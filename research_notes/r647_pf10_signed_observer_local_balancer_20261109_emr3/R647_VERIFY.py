#!/usr/bin/env python3
"""R647 exact self-scheduled PF10 one-Cell PASS controller. Python stdlib integers."""
import json
from itertools import combinations, permutations
TRI=tuple(combinations(range(6),3))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
NEI={s:tuple(t for t in TRI if len(set(s)&set(t))==2) for s in TRI}
def code(m,s):
 z=set(s)
 if any((a in z)+(b in z)!=1 for a,b in m):return 0
 return 1 if sum(b in z for a,b in m)%2==0 else -1
C={s:tuple(code(m,s) for m in MATCH) for s in TRI}
def obs(cnt):
 M=[[0]*4 for _ in range(4)]
 for (i,j),n in cnt.items():M[i][j]+=n
 u=[sum(M[i])-sum(M[j][i] for j in range(4)) for i in range(4)]
 W=[[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
 assert sum(u)==0 and all(u[i]==sum(W[i]) for i in range(4))
 return u,W
def score(s,t,u,W):
 return sum(u[i]*C[t][i] for i in range(4))+sum(C[s][i]*W[i][j]*C[t][j] for i in range(4) for j in range(4))
def differences(s,t,u,W):
 return [score(s,t,u,W)-score(s,v,u,W) for v in NEI[s] if v!=t]
B=((0,1),(2,0),(2,3),(3,0))
S=((0,1,2),(0,2,4),(1,2,4))
uB,WB=obs({e:1 for e in B})
base=[min(differences(S[i],S[(i+1)%3],uB,WB)) for i in range(3)]
assert base==[1,1,3]
def selector(cnt,priority):
 _,W=obs(cnt)
 v={(a,b):W[a][b] for a,b in B}
 assert v==cnt
 return next(e for e in priority if v[e]==min(v.values()))
def run(m,word,steps=120):
 cnt={e:m for e in B};events=[];mins=[]
 for n in range(steps):
  u,W=obs(cnt);s,t=S[n%3],S[(n+1)%3]
  mins.append(min(differences(s,t,u,W)))
  e=selector(cnt,word);events.append(e);cnt[e]+=1
 return events,mins
classes={}
for m in (0,1,2,3,7):
 good=[];bad=[]
 for word in permutations(B):
  events,gaps=run(m,word)
  assert events==list(word)*30
  for n in range(120):
   k,r=divmod(n,12)
   assert gaps[n]>=gaps[r]+3*k*base[r%3]
  (good if min(gaps)>0 else bad).append(word)
 classes[str(m)]={"strict_priority_orders":len(good),"non_strict_priority_orders":len(bad),
                  "non_strict_priority_first_edges":sorted({w[0] for w in bad})}
assert classes["0"]["strict_priority_orders"]==0
assert classes["1"]["strict_priority_orders"]==18
assert classes["1"]["non_strict_priority_orders"]==6
assert classes["1"]["non_strict_priority_first_edges"]==[(0,1)]
assert all(classes[str(m)]["strict_priority_orders"]==24 for m in (2,3,7))
priority=((2,0),(0,1),(2,3),(3,0))
chosen,gaps=run(1,priority)
assert gaps[:12]==[1,1,3,1,2,7,2,2,9,3,3,8]
for word in permutations(B):
 _,g=run(2,word,12);assert min(g)>0
 _,g=run(1,word,12)
 assert (min(g)>0) == (word[0]!=(0,1))
# The all-n theorem follows from linear individual-competitor gaps, not
# a linearity claim about minima over different competitors.
for b in ((1,1,1,1),(0,1,2,3),(0,0,0,5),(2,3,4,5),(7,2,0,1)):
 cnt=dict(zip(B,b));T=max(b)
 for _ in range(4*T-sum(b)):
  edge=selector(cnt,priority);cnt[edge]+=1
  assert max(cnt.values())<=T
 assert all(v==T for v in cnt.values())
slots={v:i for i,v in enumerate(S[0])}
for s,t in zip(S,S[1:]+S[:1]):
 common=set(s)&set(t)
 left=next(iter(set(s)-common));enter=next(iter(set(t)-common))
 slots={**{j:slots[j] for j in common},enter:slots[left]}
hol=tuple(slots[v] for v in S[0])
assert hol==(1,0,2)
report={"marker":"R647_SIGNED_OBSERVER_LOCAL_BALANCER_ALL_INDEX_PASS",
 "source_pin":"V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d",
 "science_pin":"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",
 "controller":"argmin of 4 current signed Omega B edge values, with a fixed priority (no external periodic word)",
 "B":B,"chosen_priority":priority,"cycle":S+(S[0],),
 "classes":classes,"baseline_min_gaps":base,
 "chosen_first_12_min_gaps":gaps[:12],
 "proof_identity":"Each competitor gap(m,12k+r) = competitor gap(1,r)+(m-1+3k)*competitor gap_B; latter positive",
 "rebalancing_steps":"4 max(b)-sum(b) for any nonnegative four-vector b, with explicit triad alignment for recovery",
 "odd_holonomy":hol,
 "exact_sampled_scoring_states":24*5*120,
 "reviewed":False,"formal_claim":False}
print(json.dumps(report,ensure_ascii=False,indent=2))
