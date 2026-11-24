# EC49FZA — Exact adaptive lower-endpoint onset and all-phase eventual formula
2026-11-24. Frozen BRC16943 auxiliary Boolean observer: U in the 50-support family below, H a labeled subset of m physical columns with |H|<=h<m, W(r,j)=1[r in U]1[j not in H], unit noiseless adaptive queries, exact joint recovery. No native X6 attribution. Parent: FYZ rigidity at dce2ea422bf8cc45823046a966e0050b25fb8b3d, FYZ exact packed blocks at b0134fad8dc42d5da5edf016ae1bc12e92b36aea, FYX packed transport at 3a42e1a171d3db7c557d136d4256747ef0724aff, FYW stable law at b4b38aaa894b6e6906d6037f92b747a7a0dea182. These parent results are author-proved, not independently reviewed.

## Theorem
M_15=31, and M_(4+11a)=23a+8 for all integers a>=1. More generally, with c_h=ceil((15h+6)/11) and t=11c_h-15h-6, M_h=28h-19c_h+10 whenever h>=15 and h-15>=19t (including the empty block at h=15). Consequently this exact formula holds for ALL h>=195, and M_(h+11)=M_h+23 there. No remaining eventual binary phase offsets. Earliest all-phase onset and individual smaller h are separate open questions.

## Proof of base
At h=15,m=31,c=21, the FYZ lower endpoint is 31. Use the rigid 394 prefix with final masks S=(1,2,3,4,8,16,64,128,144,192,256,512) and multiplicities (4,2,4,5,1,2,2,3,0,0,4,4), totaling 31 columns and 35 probes. Fix physical labels 0..30 in this mask order. Use this exact all-zero schedule (row,column):
(0,0),(0,1),(0,2),(0,3),(0,7),(0,8),(0,9),(2,13),(2,14),(4,17),(6,19),(7,22),(8,25),(8,26),(9,29),(9,30),(7,21),(1,6),(2,12),(6,18),(9,28),(8,24),(4,16),(8,23),(1,5),(1,9),(1,8),(7,20),(1,4),(3,15),(2,11),(2,10),(1,7),(0,6),(9,27).
Stop at first positive, or use terminal tree if all zero.

For a positive at step i, known live column j, let P_l be preceding zero-row mask in column l, and b(U)=#{l:P_l intersects U}. A candidate support must contain the positive row, be disjoint from P_j, and have b<=h. After identifying U by row queries in j, forced holes are exactly known at those b locations. If b=h, all remaining labels are determined. If b<h, probe one row in U in each of the m-1-b remaining unforced columns other than j; this recovers every label. Thus a sufficient support decision tree has leaf-specific additional depth <= m+c-i - (0 if b=h else m-1-b). This is a typed sufficient construction, not a general necessary condition. For i<=16, support depth <=6 suffices since i+6+30<=52. For i=17..34, the finite support tree search below verifies the varying deadlines for every candidate. This handles arbitrarily many physical hole subsets without enumerating them. At i=35 enumerate exactly the 52 compatible labeled states and build a depth-17 tree; on the all-zero branch enumerate exactly 30 states and build a depth-17 tree. All 36 disjoint first-positive/terminal cases have total depth <=52. The verifier constructs and replays each finite support or full-state tree; no heuristic failure is required for the proof. The known universal lower bound gives Q15(31)=52 and M15=31.

## Transfer
For h=15+k, FYW gives c_h=21+ceil(15k/11). Let L=ceil(26k/11)=k+c_h-21. FYZ gives exact packed block B(k)=47k-19L if k>=19t, where t=11L-26k=11c_h-15h-6. FYX transports the base h=15,m=31,c=21 over this block with preserved labels, giving optimal observation cost on 31+B(k)=28h-19c_h+10 columns. FYX lower endpoint matches. For k=11(a-1), t=0 so this proves all a>=1. The largest k failing the static equality condition is 179 (FYZ), so all h>=195 are covered. For each t in 1..10 the sufficient onset in its own phase is h=15+19t; for t=0 it is h=15. These are sufficient thresholds, not claimed minimal.

## Executed exact certificate
Python 3, deterministic finite decision search and replay. The locally executed verifier used the same schedule, reconstructed by reverse mask deletion; its core is provided here with the schedule literal for independent reproduction.
```python
from functools import lru_cache
from itertools import combinations
F=(23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005)
M,H,C=31,15,21
order=((0,0),(0,1),(0,2),(0,3),(0,7),(0,8),(0,9),(2,13),(2,14),(4,17),(6,19),(7,22),(8,25),(8,26),(9,29),(9,30),(7,21),(1,6),(2,12),(6,18),(9,28),(8,24),(4,16),(8,23),(1,5),(1,9),(1,8),(7,20),(1,4),(3,15),(2,11),(2,10),(1,7),(0,6),(9,27))
assert len(set(order))==35
R=[sum(1<<i for i,u in enumerate(F) if u>>r&1) for r in range(10)]
def support(Cands,dl):
 @lru_cache(None)
 def rec(A,d):
  if not A:return ()
  if any(dl[i]<d for i in Cands if A>>i&1):return None
  if A.bit_count()==1:return ()
  for r,q in enumerate(R):
   B=A&q;E=A^B
   if B and E:
    a=rec(B,d+1);b=rec(E,d+1)
    if a is not None and b is not None:return (r,a,b)
  return None
 tree=rec(sum(1<<i for i in Cands),0);assert tree is not None
 depths=[]
 for i in Cands:
  node=tree;A=set(Cands);d=0
  while node:
   r,a,b=node;v=bool(F[i]>>r&1);A={j for j in A if bool(F[j]>>r&1)==v};node=a if v else b;d+=1
  assert A=={i} and d<=dl[i];depths.append(d)
 return max(depths,default=0)
def explicit(states,budget):
 n=len(states);qs={}
 for r in range(10):
  for j in range(M):
   q=sum(1<<i for i,(u,h) in enumerate(states) if u>>r&1 and not h>>j&1)
   if q and q!=(1<<n)-1:qs[q]=(r,j)
 @lru_cache(None)
 def rec(A,d):
  if A.bit_count()<=1:return ()
  if not d or A.bit_count()>1<<d:return None
  opts=[]
  for q in qs:
   B=A&q;E=A^B
   if B and E and max(B.bit_count(),E.bit_count())<=1<<(d-1):opts.append((max(B.bit_count(),E.bit_count()),q,B,E))
  for _,q,B,E in sorted(opts):
   a=rec(B,d-1)
   if a is not None:
    b=rec(E,d-1)
    if b is not None:return(q,a,b)
  return None
 tree=rec((1<<n)-1,budget);assert tree is not None
 mx=0
 for i,(u,h) in enumerate(states):
  A=(1<<n)-1;node=tree;d=0
  while node:
   q,a,b=node;r,j=qs[q];v=bool(u>>r&1 and not h>>j&1);A=A&q if v else A&~q;node=a if v else b;d+=1
  assert A==1<<i and d<=budget;mx=max(mx,d)
 return mx
def physical(prefix,positive=None):
 states=[]
 for u in F:
  if positive is not None:
   r,j=positive
   if not(u>>r&1) or prefix[j]&u:continue
  else:j=-1
  h=sum(1<<i for i,s in enumerate(prefix) if s&u);b=h.bit_count()
  if b>H:continue
  free=[i for i in range(M) if i!=j and not h>>i&1]
  for k in range(min(H-b,len(free))+1):
   for E in combinations(free,k):states.append((u,h|sum(1<<i for i in E)))
 return states
prefix=[0]*M
for i,(r,j) in enumerate(order,1):
 assert not prefix[j]>>r&1
 if i<=16:
  cand=[a for a,u in enumerate(F) if u>>r&1 and not prefix[j]&u]
  support(cand,{a:6 for a in cand});print(i,r,j,'early <=52')
 elif i<35:
  cand=[];dl={}
  for a,u in enumerate(F):
   b=sum(bool(s&u) for s in prefix)
   if u>>r&1 and not prefix[j]&u and b<=H:
    cand.append(a);dl[a]=M+C-i-(0 if b==H else M-1-b)
  mx=support(cand,dl);print(i,r,j,'support',len(cand),mx,min(dl.values()))
 else:
  states=physical(prefix,(r,j));mx=explicit(states,M+C-i);print(i,r,j,'explicit',len(states),mx)
 prefix[j]|=1<<r
assert sorted(prefix)==[s for s,n in zip((1,2,3,4,8,16,64,128,144,192,256,512),(4,2,4,5,1,2,2,3,0,0,4,4)) for _ in range(n)]
states=physical(prefix);mx=explicit(states,M+C-len(order));print('terminal',len(states),mx)
print('PASS: all 36 branches; analytic support/label recovery and exact labeled terminal replays')
```
Actual local execution (columns i,row,col,method,candidate count,max support depth,min deadline; early rows all passed):
```
17 7 21 support 26 6 8
18 1 6 support 26 6 8
19 2 12 support 26 6 8
20 6 18 support 27 7 7
21 9 28 support 18 6 7
22 8 24 support 22 6 5
23 4 16 support 22 6 6
24 8 23 support 17 5 4
25 1 5 support 16 5 4
26 1 9 support 8 4 4
27 1 8 support 8 4 4
28 7 20 support 15 5 4
29 1 4 support 13 5 4
30 3 15 support 15 5 4
31 2 11 support 10 4 3
32 2 10 support 7 4 3
33 1 7 support 5 3 2
34 0 6 support 3 2 1
35 9 27 explicit 52 17
terminal 30 17
PASS: all 36 branches; analytic support/label recovery and exact labeled terminal replays
```
Different leaves may have different deadlines; a larger maximum depth than minimum deadline in the output is valid because each leaf is individually checked. No full enumeration of the enormous original joint space is asserted. A second heuristic search also found a 673 prefix route, not needed for the certified theorem and not independently replayed here.

## Control and next
Historical researcher provenance EM-DIRECT-23537B, TASK_RESEARCH. Own original session recovery metadata shows registration SUCCEEDED, no run, session not closed, custody not revoked. Current em_control_result returned BACKEND_IDENTITY_CHECK_UNAVAILABLE (operation_sent=false); exact RS-EC49AS query r4-20261124-2130-ec49as-read-v1 returned UPSTREAM_OUTCOME_UNKNOWN (operation_sent=true). Preserve original ID for readback; no repeat, no shared CLAIM, no protected Activity mutation. Current owner status unknown. Independent scientific artifact only. AUTHOR_PROVED / EXACT_BRANCH_CERTIFICATE_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
Next: test earlier phase-specific onset candidates, starting with FYZ's two rigid vectors near z=t-1 and z=t; determine exact finite exceptions below h=195 using the leaf-deadline and explicit terminal strategy.
