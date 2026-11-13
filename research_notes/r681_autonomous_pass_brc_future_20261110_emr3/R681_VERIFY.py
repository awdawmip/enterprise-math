#!/usr/bin/env python3
"""R681 finite exact future observer quotient and autonomous local PASS scheduler."""
from itertools import combinations,permutations
from collections import Counter
TRIADS=tuple(combinations(range(6),3))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
PASS=((0,1),(1,2),(2,0))
BIASES=((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),(2,4,3,-10),(3,2,4,-10),(4,3,2,-10))
w=(-1,1,-2,-1)
def code(s,m):
 if any((a in s)+(b in s)!=1 for a,b in m):return 0
 return 1 if sum(b in s for a,b in m)%2==0 else -1
C={s:tuple(code(s,m) for m in MATCH) for s in TRIADS}
N={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(set(C.values()))==20 and all(len(N[s])==9 for s in TRIADS)
def score(u,M,S,T):
 return sum(u[i]*C[T][i] for i in range(4))+sum(C[S][i]*(M[i][j]-M[j][i])*C[T][j] for i in range(4) for j in range(4))
def step(u,M,e):
 a,b=PASS[e];v=list(u);v[a]+=1;v[b]-=1;L=[list(row) for row in M];L[a][b]+=1
 return tuple(v),tuple(tuple(row) for row in L)
def best(u,M,S):
 return max(N[S],key=lambda T:7*score(u,M,S,T)+sum(w[i]*C[T][i] for i in range(4)))
def Q(u,M,S,e):
 v,L=step(u,M,e);t=best(v,L,S)
 return 7*score(v,L,S,t)+sum(w[i]*C[t][i] for i in range(4))
def delta(e):
 a,b=PASS[e];return w[a]-w[b]
def auto(u0,S0):
 u=u0;M=tuple(tuple(0 for i in range(4)) for j in range(4));s=S0;history=[];ties=[]
 for k in range(3):
  options=[e for e,(a,b) in enumerate(PASS) if M[a][b]==0]
  v={e:Q(u,M,s,e) for e in options}
  top=max(v.values());tie=tuple(e for e in options if v[e]==top)
  e=max(options,key=lambda e:(v[e],delta(e)))
  ties.append(len(tie))
  u,M=step(u,M,e);s=best(u,M,s);history.append(e)
 return tuple(history),s,tuple(ties)
def prefix_trace(u0,s0,order):
 u=u0;M=tuple(tuple(0 for _ in range(4)) for _ in range(4));s=s0
 yield (u,M,s)
 for e in order:
  u,M=step(u,M,e);s=best(u,M,s)
  yield (u,M,s)
def certificate():
 legal_words=list(permutations(range(3)))
 stage_classes=[]
 for k in range(4):
  states=set()
  for bias in BIASES:
   for start in TRIADS:
    for order in legal_words:
     states.add(list(prefix_trace(bias,start,order))[k])
  stage_classes.append(len(states))
 assert stage_classes==[120,114,117,48]
 assert sum(stage_classes)==399

 # Exact suffix signatures test all repeated prefix states.
 signatures={}
 prefix_occurrences=0
 for bias in BIASES:
  for start in TRIADS:
   for order in legal_words:
    states=list(prefix_trace(bias,start,order))
    for k,(u,M,s) in enumerate(states):
     prefix_occurrences+=1
     remain=tuple(e for e,(a,b) in enumerate(PASS) if M[a][b]==0)
     sig=[]
     for tail in permutations(remain):
      x=u;H=M;t=s
      for e in tail:
       x,H=step(x,H,e);t=best(x,H,t)
      sig.append((tail,x,H,t))
     sig=tuple(sig)
     state=(u,M,s)
     if state in signatures:assert signatures[state]==sig
     else:signatures[state]=sig
 assert len(signatures)==399 and prefix_occurrences==2880

 counts=Counter();first_ties=Counter();second_ties=Counter();examples={}
 for bias in BIASES:
  for start in TRIADS:
   order,end,ties=auto(bias,start)
   assert sorted(order)==[0,1,2]
   assert ties[2]==1
   counts[''.join('ABC'[e] for e in order)]+=1
   first_ties[ties[0]]+=1
   second_ties[ties[1]]+=1
   initial_M=tuple((0,0,0,0) for _ in range(4))
   values={e:Q(bias,initial_M,start,e) for e in range(3)}
   assert order[0]==max(range(3),key=lambda e:(values[e],delta(e)))
   if start==(0,1,2):
    examples[str(bias)]={'word':''.join('ABC'[e] for e in order),'final_triad':''.join(map(str,end))}
 assert dict(counts)=={'BCA':40,'CBA':8,'BAC':45,'ABC':10,'ACB':6,'CAB':11}
 assert first_ties==Counter({1:59,3:51,2:10})
 assert second_ties==Counter({1:110,2:10})
 assert sorted(delta(e) for e in range(3))==[-2,-1,3]
 assert len(counts)==6
 s=(0,1,3)
 assert [auto(b,s)[0][0] for b in BIASES]==[2,0,0,1,1,1]

 return {'schema':'R681_EXACT_FINITE_CERTIFICATE_V1',
   'predecessor':'R680@151d820a1c776fe4b1401ab0a23b1d0867c13883',
   'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
   'population':{'biases':6,'initial_triads':20,'legal_pass_words':6,'histories':720,'prefix_occurrences':prefix_occurrences},
   'observer':{'state':'(u,M,S); fixed w and typed candidate encoding',
     'distinct_states_by_prefix':stage_classes,
     'total_distinct_future_states':399,'complete_suffix_signature_checks':prefix_occurrences},
   'scheduler':{'rule':'max_e (max_T(7 Phi_e(S,T)+w.c(T)),w[a_e]-w[b_e]) on unused PASS',
     'priority_edge_gradient':{'A':delta(0),'B':delta(1),'C':delta(2)},
     'autonomous_runs':120,'order_counts':dict(sorted(counts.items())),
     'candidate_ties_at_first_event':dict(sorted(first_ties.items())),
     'candidate_ties_at_second_event':dict(sorted(second_ties.items())),
     'initial_012_traces':examples,
     'bias_needed_witness':{'initial_S':'013','first_pass_by_bias':['ABC'[auto(b,s)[0][0]] for b in BIASES]}},
   'observed_scope':'declared three-PASS once-each grammar and R680 6 baseline biases; exact integer arithmetic'}
if __name__=='__main__':
 import json
 result=certificate()
 print(json.dumps(result,ensure_ascii=False,indent=2))
 print('R681_AUTO_SCHEDULER_FUTURE_QUOTIENT_EXACT_PASS')
