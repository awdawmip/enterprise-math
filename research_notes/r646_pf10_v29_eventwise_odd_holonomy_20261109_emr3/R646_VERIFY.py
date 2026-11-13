#!/usr/bin/env python3
"""R646 exact 24-permutation source-V29 single-PASS-per-step selector certificate."""
import json
from itertools import combinations,permutations
TRI=tuple(combinations(range(6),3))
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
NEI={s:tuple(t for t in TRI if len(set(s)&set(t))==2) for s in TRI}
def code(m,s):
 z=set(s)
 if any((a in z)+(b in z)!=1 for a,b in m):return 0
 return 1 if sum(b in z for a,b in m)%2==0 else -1
C={s:tuple(code(m,s) for m in MATCH) for s in TRI}
def obs(E):
 M=[[0]*4 for _ in range(4)]
 for a,b in E:M[a][b]+=1
 u=[sum(M[i])-sum(M[j][i] for j in range(4)) for i in range(4)]
 om=[[M[i][j]-M[j][i] for j in range(4)] for i in range(4)]
 assert sum(u)==0
 return u,om
def score(S,T,u,om):
 return sum(u[i]*C[T][i] for i in range(4))+sum(C[S][i]*om[i][j]*C[T][j] for i in range(4) for j in range(4))
B=((0,1),(2,0),(2,3),(3,0))
S=((0,1,2),(0,2,4),(1,2,4))
U,W=obs(B)
base=[]
for p in range(3):
 s,t=S[p],S[(p+1)%3]
 D=min(score(s,t,U,W)-score(s,v,U,W) for v in NEI[s] if v!=t)
 base.append(D)
assert base==[1,1,3]

valid=[];failed=[]
for word in permutations(B):
 d=[]
 for r in range(12):
  E=B+word*(r//4)+word[:r%4]
  u,om=obs(E)
  s,t=S[r%3],S[(r+1)%3]
  d.append(min(score(s,t,u,om)-score(s,v,u,om) for v in NEI[s] if v!=t))
 if min(d)>0:valid.append((word,d))
 else:failed.append((word,d))
assert len(valid)==18 and len(failed)==6
assert all(w[0]!=(0,1) for w,d in valid)
assert all(w[0]==(0,1) and d[1]==0 for w,d in failed)

# All-index proof: n=12*k+r means M_n=(3*k+1+floor(r/4))*M(B)+prefix(word,r%4).
# Each competitor gap is phase-r gap plus 3*k times its positive base gap.
# Consequently 12 exact phase checks settle every future step, not only samples.
chosen=next((w,d) for w,d in valid if w==((2,0),(0,1),(2,3),(3,0)))
assert chosen[1]==[1,1,3,1,2,7,2,2,9,3,3,8]
for word,d in valid:
 for k in range(25):
  for r in range(12):
   n=12*k+r
   E=B+word*(n//4)+word[:n%4]
   u,om=obs(E);s,t=S[n%3],S[(n+1)%3]
   true_gap=min(score(s,t,u,om)-score(s,v,u,om) for v in NEI[s] if v!=t)
   assert true_gap>=d[r]+3*k*base[r%3]>0

result={'marker':'R646_V29_EVENTWISE_18_OF_24_STRICT_ODD_CYCLE_PASS',
        'source':'V23/V27/V17/V29@b62110008321d9147212cb89f2627ff613c2550d',
        'frozen_R462':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'initial_seed':B,'active_cycle':S+(S[0],),
        'selector':'one V27 unique argmax THEN one V29 PASS after EVERY step',
        'external_event_word_4_periodic':True,'word_permutations_checked':24,
        'strict_successful_orders':18,'failing_orders':6,
        'failing_orders_characterization':'word[0] is (0,1), score tie at n=1',
        'chosen_word':chosen[0], 'chosen_phase_min_gaps_r0_to11':chosen[1],
        'base_min_gaps_by_triad_phase':base,
        'all_n_certificate':'n=12k+r; each competitor gap = gap_r + 3k*positive_base_gap; r=0..11',
        'exact_samples_per_good_order':25*12,
        'holonomy_after_3':[1,0,2], 'holonomy_after_6':[0,1,2],
        'network_Q':0, 'full_native_scheduler_claimed':False,
        'independent_driver_review':False}
print(json.dumps(result,ensure_ascii=False,indent=2))