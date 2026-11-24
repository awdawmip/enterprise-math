# EC49FZB — Sharp lower-endpoint onset in every phase
2026-11-24. Same frozen BRC16943 auxiliary Boolean observer as FZA: U belongs to the specified 50 supports, H is a labeled subset of m columns, |H|<=h<m, W(r,j)=1[r in U]1[j not in H]. Noiseless unit-cost adaptive observation, exact joint recovery. No native X6 attribution. Parent provenance EM-DIRECT-23537B; current Sites identity check authenticates the client only, not a private researcher writer. Independent portable research, no CLAIM or formal Result/Review. FZA parent exact pin 6cd682de7b1300c7bbb191e859743cff3282cad5:research_notes/portable_direct/EC49FZA_EXACT_ADAPTIVE_LOWER_ONSET.md; FYZ rigidity dce2ea422bf8cc45823046a966e0050b25fb8b3d; FYZ packed block b0134fad8dc42d5da5edf016ae1bc12e92b36aea; FYX transport 3a42e1a171d3db7c557d136d4256747ef0724aff; FYW stable law b4b38aaa894b6e6906d6037f92b747a7a0dea182. These parents are author-proved, not independently reviewed.

## Theorem (parent-dependent)
For every integer h>=4, let c=ceil((15h+6)/11), t=11c-15h-6, z=(h-4-8t)/11, m0=28h-19c+10=23z+15t+8. Then
M_h=m0 if and only if z>=max(1,t-1).
Equivalently the earliest attainment in each phase t=0,1,2,...,10 occurs at h=(15,23,31,50,69,88,107,126,145,164,183), respectively; all later h in that phase follow in steps of 11. In particular the sharp all-phase onset is 173, improving FZA's sufficient 195. The largest failure is h=172, t=10,z=8; m0=342, so M_172>=343. The exact value at smaller nonattaining h is a separate problem.

## Proof
Necessity is FYZ rigidity: if m0>h, the only possible all-zero prefix types are D394 (feasible exactly z>=max(1,t-1)) and D673 (feasible exactly z>=t+1). If m0<=h, the defining domain m>h excludes equality directly. For sufficiency the t=0 base h=15,m=31,c=21 is FZA. New exact branch certificates below give Q23(46)=78 and Q31(61)=104; the universal observation and inventory lower bounds yield M23=46 and M31=61. These are z=1,t=1 and z=1,t=2. The certificates partition the original labeled joint state space by first positive index or the all-zero terminal. For a positive at (r,j), use the prior zero masks P_l, candidates U containing r and disjoint from P_j, and forced holes H_U={l:P_l intersects U}. Let b=|H_U|<=h. The remaining budget is m+c-i at step i. If b=h, a support decision tree suffices; otherwise after identifying U in the known live column j, query a row in U in each of the m-1-b other unforced columns, recovering every physical label. The per-support deadline for the support tree is m+c-i-(0 if b=h else m-1-b). On explicit branches the verifier enumerates all compatible labeled states and constructs and replays a binary tree. Thus the proof does not require a count of the entire huge joint space. Positive results are verified on all candidate supports or all enumerated compatible states; pruning used only in finding trees, not in replay.

FYZ's exact static packed block at k=19 has L=45 observations, 38 columns, and rounding remainder 11L-26k=1. For a base at t in 2..9, adding k=19 yields t'=t+1,z'=z+1,c'=c+26 (no modular wrap), and m0'=m0+38. FYX's packed transport applies since c>=6, and L-k=26, so the lower endpoint transfers exactly. By eight iterations the h=31 base proves all t=2..10 minimal thresholds h=19t-7. Separately the exact block k=11 (26 probes,23 columns) preserves t and increments z by one, with c increasing by 15. This proves every later h in every phase. For t=1 the threshold is 23; for t=0 it is 15. The previous element in phase t=10 is h=172; all other previous elements are smaller (t=9 last failure 153). Hence 173 is the least uniform onset in h>=4.

## Reproduction: exact Python 3 verifier
The reverse mask-deletion search found the two literal schedules, after 63 and 81 candidate branch tests respectively (seed 0). A separate local verifier reconstructed the decision trees with integer masks and replayed every support/explicit state against its own deadline. The full verifier as executed follows. Star pruning accelerates tree construction: a state and each one-hole extension differ only in that column, so if k such extensions remain, at least k queries are needed, all positive on the central state when k equals remaining depth. Two distinct states cannot both force the same all-positive terminal path. Replay verifies actual trees directly, so the positive result does not rely on pruning completeness.

```python
from functools import lru_cache
from itertools import combinations
F=(23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005)
S=(1,2,3,4,8,16,64,128,144,192,256,512)
D=(1,0,1,1,0,1,1,1,0,0,1,1)
ORDERS={1:'0:14 0:13 0:12 0:10 0:5 1:11 1:9 1:8 2:22 8:39 2:21 2:20 0:4 8:38 4:32 4:26 2:19 3:24 0:3 9:45 1:14 0:2 7:33 7:31 1:13 7:30 2:18 9:44 1:12 8:37 0:11 3:23 0:1 8:36 1:7 9:43 2:17 9:42 7:29 4:25 8:35 1:6 6:28 1:10 0:0 2:16 9:41 6:27 8:34 0:9 7:32 2:15 9:40 6:33',2:'2:30 2:29 2:28 2:27 2:26 0:19 8:52 9:60 8:51 0:18 9:59 0:12 2:25 1:17 0:7 7:43 1:16 0:6 1:15 2:24 1:14 0:5 1:13 2:23 0:4 0:3 7:42 9:58 1:19 1:18 9:57 2:22 8:50 0:17 0:2 0:16 8:49 7:40 0:15 1:11 8:48 9:56 0:1 9:55 0:14 4:41 4:35 6:44 2:21 8:47 8:46 0:13 0:0 1:10 8:45 1:9 7:39 3:33 3:32 1:12 9:54 4:42 2:20 1:8 6:37 3:31 7:38 6:36 4:34 7:41 7:44 9:53 6:43'}

def solve(states,queries,deadline):
 n=len(states);A0=(1<<n)-1
 # All masks retain the original state labels. No pruning based on a relaxed model.
 qs={}
 for q in queries:
  B=sum(1<<i for i,x in enumerate(states) if q(x))
  if B and B!=A0:qs[B]=q
 idx={x:i for i,x in enumerate(states)}
 stars=[sum(1<<idx[(u,h|1<<j)] for j in range(max((v.bit_length() for _,v in states),default=0)) if not h>>j&1 and (u,h|1<<j) in idx) for u,h in states] if states and isinstance(states[0],tuple) else None
 late=[sum(1<<i for i,d in enumerate(deadline) if d<k) for k in range(max(deadline,default=0)+2)]
 @lru_cache(None)
 def rec(A,d):
  if not A:return ()
  if A&late[min(d,len(late)-1)]:return None
  if A.bit_count()==1:return ()
  if d>=len(late)-2:return None
  ex=0
  if stars is not None:
   left=A;rem=deadline[0]-d
   if A.bit_count()>1<<rem:return None
   while left:
    low=left&-left;left^=low;k=(A&stars[low.bit_length()-1]).bit_count()
    if k>rem:return None
    if k==rem:
     if ex:return None
     ex=low
  choices=set()
  for q in qs:
   B=A&q;E=A^B
   if B and E and (not ex or B&ex):choices.add((max(B.bit_count(),E.bit_count()),B,E,q))
  for _,B,E,q in sorted(choices):
   x=rec(B,d+1)
   if x is not None:
    y=rec(E,d+1)
    if y is not None:return(q,x,y)
  return None
 tree=rec(A0,0);assert tree is not None
 mx=0
 for i,x in enumerate(states):
  A=A0;node=tree;d=0
  while node:
   q,p,e=node;v=bool(qs[q](x));A=A&q if v else A&~q;node=p if v else e;d+=1
  assert A==1<<i and d<=deadline[i];mx=max(mx,d)
 return mx

def verify(t):
 z=1;h=11*z+8*t+4;c=15*z+11*t+6
 n=(3*z+2*t,2*z+t,3*z+2*t,4*z+3*t,z+t,z,z,2*z,t,t,3*z+2*t,3*z+2*t)
 P=tuple(s for s,x,d in zip(S,n,D) for _ in range(x+d));m=len(P)
 order=[tuple(map(int,v.split(':'))) for v in ORDERS[t].split()]
 assert m==28*h-19*c+10 and len(order)==h+c-1 and len(set(order))==len(order)
 prefix=[0]*m;summary=[]
 for i in range(1,len(order)+2):
  positive=i<=len(order);r,j=order[i-1] if positive else (-1,-1)
  budget=m+c-min(i,len(order));cands=[]
  for u in F:
   if positive and (not(u>>r&1) or prefix[j]&u):continue
   H=sum(1<<l for l,s in enumerate(prefix) if s&u);b=H.bit_count()
   if b<=h:cands.append((u,H,b))
  explicit=not positive or (t==1 and i in (52,54)) or (t==2 and i==73)
  if explicit:
   states=[]
   for u,H,b in cands:
    free=[l for l in range(m) if l!=j and not H>>l&1]
    for k in range(h-b+1):
     for E in combinations(free,k):states.append((u,H|sum(1<<l for l in E)))
   mx=solve(states,[(lambda x,a=a,b=b:bool(x[0]>>a&1 and not x[1]>>b&1)) for a in range(10) for b in range(m)],[budget]*len(states))
   summary.append((i,len(states),mx,budget))
  else:
   dl=[budget-(0 if b==h else m-1-b) for u,H,b in cands]
   solve([u for u,H,b in cands],[(lambda u,a=a:bool(u>>a&1)) for a in range(10)],dl)
  if positive:prefix[j]|=1<<r
 assert tuple(prefix)==P
 print(t,h,m,c,len(order)+1,summary,'PASS',flush=True)
for t in (1,2):verify(t)
```

Actual local execution, columns t,h,m,c,number of exhaustive first-positive/terminal branches, list of explicit branches (index,state count,max depth,budget):
```
1 23 46 32 55 [(52, 952, 26, 26), (54, 144, 24, 24), (55, 37, 24, 24)] PASS
2 31 61 43 74 [(73, 186, 31, 31), (74, 46, 31, 31)] PASS
```
Total 129 partition branches, 1365 explicitly replayed labeled states, remaining branches supported by exact individual deadlines and analytical label recovery. The search also found a t=3 candidate; it is not needed for the proof and was not used as independent replay evidence.

## Control and next
Original FZA task query r4-20261124-2130-ec49as-read-v1 recovered SUCCEEDED, exact directory absence at Source 7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b (not native owner projection). Current Sites identity-only check succeeded but no writer binding established for historical EM-DIRECT-23537B. No CLAIM or protected writes. Next: determine the exact M_h above m0 for the smaller failing phases; distinguish finite resource lower bounds and constructive upper bounds. AUTHOR_PROVED / EXACT_BRANCH_CERTIFICATE_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
