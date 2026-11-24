# EC49FZG — Tight conditional deficit mask rigidity and mandatory-column decision pruning
2026-11-25. Frozen auxiliary Boolean observer BRC16943, same 50 supports, rows and physical labels as FZF (113b09ca709d96aa871e07372f8ff58bf2228215:research_notes/portable_direct/EC49FZF_CONDITIONAL_DEFICIT_DUAL.md, blob fff6fb00e3e0667a2a367096848a2dafdeb5d64f). State (U,H), |H|<=h<m; observation W(r,j)=1[r in U]1[j not in H]. Reuse FZF conditional deficit and FZE/FZD prefix and explicit recovery lemmas. This is the auxiliary discrete observer, not native X6 attribution. Parent-dependent, author-checked, not independently reviewed.

## New results
At the proposed lower inventory endpoint, six h values (14,25,38,49,62,73) have exactly ONE necessary static zero-prefix mask multiset; three more (27,40,51) have exactly THREE. All nine retain the unique possible deficient support f=673. This is an exact classification of necessary static configurations up to column permutation, not of complete adaptive trees. For h=14,m=25, d=33, the 14 inequivalent last-probe types reduce to precisely four whose last-positive branch admits recovery with budget 12: (mask,row)=(3,1),(192,6),(320,6),(320,8). The other ten are rigorously excluded by finite exhaustive decision recursion with mandatory-column pruning; no cutoffs occurred on these 14 branches. The terminal all-zero history has 28 compatible labeled states and a verified 12-query tree. Full 25-column existence remains open, as do the 26/27 alternatives. No changes to the FZF inventory intervals or exact-value count are claimed.

## Proof of tight-deficit rigidity
Write x_s for the number of physical columns with zero-mask s, including s=0. Sum x_s=m and sum popcount(s)x_s=d=h+c_h-1. Let b_U=sum_{s intersects U}x_s. By the parent prefix lemma b_U>=h except one possible f with b_f=h-1. For each integer certificate (A,q,w) from the frozen FZF pool define g(s)=A+q popcount(s)-sum_{U intersects s}w_U>=0, including g(0)=A; define t_U=b_U-h+1[U=f]>=0, and sigma=A m+q d-h sum w+w_f. Exactly
sigma = sum_s g(s)x_s + sum_U w_U t_U.
Thus every occupied mask satisfies g(s)<=sigma; if sigma=0, all occupied masks have g=0 and all supports of positive weight have t_U=0. All terms are nonnegative integers, so the reduction is lossless for necessary feasibility. FZF conditional bounds show that only f=673 is possible at the nine endpoints; a no-deficit state would pass for every f, hence is excluded. Use all ten frozen certificates, restrict the mask columns, and add the exact equations from every zero-slack certificate. Solve over Q, retain only nonnegative integer x with all 50 support inequalities and exact b_f=h-1. Every static candidate satisfies these equations, and every retained vector meets the static conditions; integrality, rank and all coverage inequalities are checked exactly.

For h=14,m=25 the allowed masks [1,2,3,4,8,64,128,144,192,256,320,512] give rank 12, and the unique count vector is [4,2,2,4,1,0,0,2,2,3,2,3]. For the other five unique cases use mask order [1,2,3,4,8,16,64,128,144,192,256,320,512], rank 13:
25,47: [6,3,6,8,2,1,1,2,2,2,6,2,6]
38,71: [10,5,8,12,3,1,1,2,4,4,9,3,9]
49,93: [12,6,12,16,4,2,2,4,4,4,12,3,12]
62,117: [16,8,14,20,5,2,2,4,6,6,15,4,15]
73,139: [18,9,18,24,6,3,3,6,6,6,18,4,18].
For h=27,40,51 the restricted matrices have respectively 14,14,15 columns and ranks 12,12,13. Each solution has two free coordinates (actual x coordinates from RREF), bounded in [0,m]. Exhaustive integer enumeration and coverage filtering leave three vectors each. For h27 and h40 use order [1,2,3,4,8,17,48,64,128,144,192,256,320,512]:
27,49: [6,3,6,8,2,1,0,1,2,3,2,6,3,6]; [8,4,4,8,2,0,0,0,0,4,4,6,3,6]; [6,3,6,8,2,0,1,1,2,3,2,6,3,6].
40,73: [10,5,8,12,3,1,0,1,2,5,4,9,4,9]; [12,6,6,12,3,0,0,0,0,6,6,9,4,9]; [10,5,8,12,3,0,1,1,2,5,4,9,4,9].
51,95 uses [1,2,3,4,8,16,17,48,64,128,144,192,256,320,512]: [12,6,12,16,4,1,1,0,2,4,5,4,12,4,12]; [14,7,10,16,4,1,0,0,1,2,6,6,12,4,12]; [12,6,12,16,4,1,0,1,2,4,5,4,12,4,12].

## Mandatory-column residual lemma
In any compatible labeled state set X, for a state (U,H) let J_X(U,H) be the columns j for which (U,H xor {j}) also belongs to X. These neighboring states disagree only on probes in physical column j with row in U. On the true (U,H) path, at least one such probe per j in J is necessary. Hence with k remaining queries, |J|>k is impossible. If |J|=k, every next probe on that path must be a pair (r,j) with r in U and j in J. Before the next response the chosen probe is shared across all possible states, so intersect these conditions over all tight states. An empty intersection excludes the node. This bound preserves labeled joint residuals and is valid at arbitrary positive/negative transcripts, not merely the zero-prefix terminal. It is stronger than raw binary capacity when several tight states require incompatible first probes. It supplies a sound pruning rule for complete finite decision recursion; it does not assert that passing the rule suffices.

To test the last positive branch of h14,m25, remove one bit r from one occupied final mask s and constrain that probe to positive. The exact state set enumerates all U containing r and avoiding the earlier mask in that column, all forced holes in other columns, and every permitted extra subset with total holes <=h; the positive column is live. No ordering beyond the preceding zero-mask inventory is relevant. All physical labels remain distinct. Different columns with the same mask are equivalent under relabeling, so the 14 types cover every possible last probe. Test each at k=m-h+1=12, with exact recursive partition by all nonconstant response masks and the pruning lemma. Recursion strictly reduces k. A feasible tree is replayed on every state, and infeasibility follows only after exhausting all admissible queries. Equal query-response masks on the entire original branch can be represented once, because their partitions agree on every descendant subset. Retaining all matching row/column coordinates for tight-constraint checks is sufficient.

Actual Python integer-bitset run (s,r,states,result,distinct recursion calls):
1,0,169,False,15003
2,1,112,False,92226
3,0,118,False,11410
3,1,61,True,15738
4,2,75,False,12181
8,3,113,False,77148
144,4,75,False,3792
144,7,105,False,2950
192,6,50,True,1109
192,7,129,False,8774
256,8,97,False,46781
320,6,65,True,8279
320,8,73,True,10243
512,9,119,False,10955
All below the 200000-node cap. The four feasible branches replay 249 states total. The incompatible branches are exact negative results, not an optimizer verdict. Terminal 28-state tree was replayed by the parent-style explicit recursion. For last type (3,1), exploratory second-last checks with cap 20000 found feasible types (3,0) and (144,7); all other twelve types in that exploration hit the cap, no exclusions attributed to them. Other last types not fully explored at second-last depth. Exploratory backward construction on sampled static inventories h10/m16 and h11/m19 and on split-mask h14/m26 did not produce complete strategies; these limited searches establish no additional impossibility. 

## Reproduction
Python 3 + SymPy for exact rational linear algebra; no numerical solver used in the claimed exclusions. Literal inputs copied from the frozen FZF reproduction. The following compact checker implements the exact computations of the static classification and last-branch search (the optional cap returns None, never False). The finite domain includes every nonempty mask and mask zero, all 50 supports, all free RREF coordinates in [0,m], and every inequivalent last probe. 
```python
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
D=[[3,30,[[86,6],[91,1],[101,13],[243,1],[281,3],[299,1],[346,1],[394,14],[412,2],[460,2],[602,9],[673,14],[788,10]]],[27,64,[[23,6],[86,14],[101,19],[157,2],[243,9],[281,3],[299,12],[394,21],[412,6],[460,15],[602,22],[646,7],[673,22],[697,6],[788,22],[833,12]]],[1,3,[[86,1],[101,1],[299,1],[394,1],[460,1],[602,1],[673,2],[788,1]]],[5,36,[[23,1],[86,6],[101,16],[243,2],[281,3],[299,2],[346,2],[394,16],[412,3],[460,3],[602,12],[673,17],[788,12]]],[3,22,[[86,5],[101,9],[243,1],[281,2],[299,2],[346,1],[394,9],[412,2],[460,2],[602,7],[673,11],[788,7]]],[3,38,[[86,7],[91,2],[101,17],[243,1],[281,4],[346,1],[394,19],[412,2],[460,2],[602,11],[673,17],[788,13]]]]
E=[[1,19,[[86,4],[91,1],[101,8],[281,2],[346,1],[394,9],[412,1],[460,1],[602,5],[673,9],[788,6]]],[5,36,[[23,1],[86,6],[101,16],[211,2],[281,3],[299,2],[346,2],[394,16],[412,3],[460,3],[602,12],[673,17],[788,12]]],[3,38,[[86,7],[91,2],[101,17],[211,1],[281,4],[346,1],[394,19],[412,2],[460,2],[602,11],[673,17],[788,13]]],[3,22,[[86,5],[101,9],[211,1],[281,2],[299,2],[346,1],[394,9],[412,2],[460,2],[602,7],[673,11],[788,7]]]]
from itertools import product,combinations
from functools import lru_cache
from collections import Counter
import sympy as sp
D=D+E
C=lambda h:(15*h+16)//11
for A,q,w in D:
 assert A>0 and q>=0 and all(u in F and n>=0 for u,n in w)
 assert len(dict(w))==len(w)
 for s in range(1024):
  assert A+q*s.bit_count()>=sum(n for u,n in w if s&u)
cases=[(14,25),(25,47),(38,71),(49,93),(62,117),(73,139),(27,49),(40,73),(51,95)]
for h,m in cases:
 d=h+C(h)-1;f=673
 assert [u for u in F if all(h*sum(n for _,n in w)-dict(w).get(u,0)-q*d<=A*m for A,q,w in D)]==[f]
 allowed=list(range(1024));tight=set()
 for A,q,w in D:
  sigma=A*m+q*d-h*sum(n for u,n in w)+dict(w).get(f,0)
  assert sigma>=0
  allowed=[s for s in allowed if A+q*s.bit_count()-sum(n for u,n in w if s&u)<=sigma]
  if sigma==0:tight|={u for u,n in w if n>0}
 a=sp.Matrix([[1]*len(allowed),[s.bit_count() for s in allowed]]+[[int(bool(s&u)) for s in allowed] for u in sorted(tight)])
 b=sp.Matrix([m,d]+[h-int(u==f) for u in sorted(tight)])
 sol=next(iter(sp.linsolve((a,b))))
 params=sorted(set().union(*(x.free_symbols for x in sol)),key=str)
 good=[]
 for x in product(range(m+1),repeat=len(params)):
  y=[v.subs(dict(zip(params,x))) for v in sol]
  if any(v<0 or not v.is_Integer for v in y):continue
  if any(sum(v for s,v in zip(allowed,y) if s&u)<h-int(u==f) for u in F):continue
  if sum(v for s,v in zip(allowed,y) if s&f)!=h-1:continue
  good.append(list(map(int,y)))
 print(h,m,allowed,a.rank(),len(good),good)
 assert len(good)==(1 if h in [14,25,38,49,62,73] else 3)
 if h==14:ms=[s for s,n in zip(allowed,good[0]) for _ in range(n)]

def physical(p,h,pos=None):
 m=len(p);out=[]
 for u in F:
  if pos and (not(u>>pos[0]&1) or p[pos[1]]&u):continue
  req=sum(1<<j for j,s in enumerate(p) if s&u)
  if req.bit_count()>h:continue
  free=[j for j in range(m) if not req>>j&1 and (not pos or j!=pos[1])]
  for k in range(min(h-req.bit_count(),len(free))+1):
   for cc in combinations(free,k):out.append((u,req|sum(1<<j for j in cc)))
 return out

def exact(st,m,d,cap=200000):
 full=(1<<len(st))-1;idx={x:i for i,x in enumerate(st)};qs={}
 neigh=[[(j,1<<idx[u,b^(1<<j)]) for j in range(m) if (u,b^(1<<j)) in idx] for u,b in st]
 for r in range(10):
  for j in range(m):
   q=sum(1<<i for i,(u,b) in enumerate(st) if u>>r&1 and not b>>j&1)
   if q and q!=full:qs.setdefault(q,[]).append((r,j))
 calls=0
 class Limit(Exception):pass
 @lru_cache(None)
 def rec(X,k):
  nonlocal calls
  calls+=1
  if calls>cap:raise Limit
  if X.bit_count()<=1:return ()
  if not k or X.bit_count()>1<<k:return None
  tight=[];Y=X
  while Y:
   bit=Y&-Y;i=bit.bit_length()-1;Y^=bit
   J=sum(1<<j for j,b in neigh[i] if X&b);n=J.bit_count()
   if n>k:return None
   if n==k:tight.append((st[i][0],J))
  opts=[]
  for q,locs in qs.items():
   if tight and not any(all(u>>r&1 and J>>j&1 for u,J in tight) for r,j in locs):continue
   B=X&q;E=X^B
   if B and E and max(B.bit_count(),E.bit_count())<=1<<(k-1):opts.append((max(B.bit_count(),E.bit_count()),q,B,E))
  for _,q,B,E in sorted(opts):
   a=rec(B,k-1)
   if a is not None:
    b=rec(E,k-1)
    if b is not None:return (q,a,b)
  return None
 try:t=rec(full,d)
 except Limit:return None,calls
 if t is not None:
  for i,(u,b) in enumerate(st):
   node=t;X=full;k=0
   while node:
    q,a,e=node;r,j=qs[q][0];v=bool(u>>r&1 and not b>>j&1);X=X&q if v else X&~q;node=a if v else e;k+=1
   assert X==1<<i and k<=d
 return t is not None,calls

h,m=14,25
assert len(ms)==m and sum(s.bit_count() for s in ms)==33
# Main run used a parent-style explicit terminal recursion; this checker can use the same exact engine.
print('terminal',len(physical(ms,h)),exact(physical(ms,h),m,12))
expected={(3,1),(192,6),(320,6),(320,8)}
got=set()
for j,s in enumerate(ms):
 if j and ms[j-1]==s:continue
 for r in range(10):
  if not s>>r&1:continue
  p=ms.copy();p[j]^=1<<r
  st=physical(p,h,(r,j));v,n=exact(st,m,12)
  print(s,r,len(st),v,n)
  assert v is not None
  if v:got.add((s,r))
assert got==expected
```

## Control and continuation
Original own registration r4-20261124-0240-ec49fyh-own-session-v1 read SUCCEEDED, EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76 (historical identity; current private writer binding not yet verified). Current topic lookup r4-20261125-0330-ec49as-read-v1 SUCCEEDED at b7cbf514a6369c8fe09102a8c133c21d0e365837; NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. No shared CLAIM or formal Result/Review. Independent portable non-overwriting scientific publication. Next: continue from the four surviving h14 last-probe classes using tight-state pruning, not the ten excluded classes; use the six unique and three triple-static inventories as candidate sources for subsequent dynamic tests. FZF intervals unchanged. AUTHOR_PROVED / EXACT_FINITE_CONDITIONAL_RIGIDITY / EXACT_LAST_BRANCH_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
