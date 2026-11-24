# EC49FZE — Exact small-hole inventories and terminal-capacity certificate
2026-11-25. Parent-dependent auxiliary Boolean observer of frozen BRC16943, continuing FZD (3255ac1617ac425d046fed5b6545fcb2b21af512:research_notes/portable_direct/EC49FZD_SIX_HOLE_EXACT_INVENTORY.md) and FZC (725a6c9d6695346a9a6dd762efa6587af10fd7dc:research_notes/portable_direct/EC49FZC_FINITE_EXCEPTION_INVENTORY_ENVELOPE.md). State (U,H), U in the literal 50-support family F, H subset of m labeled columns, |H|<=h<m; noiseless unit query W(r,j)=1[r in U]1[j not in H]. Exact joint recovery; no native X6 attribution.

## Results
M_5=9, M_7=11, M_8=13; Q_5(9)=17, Q_7(11)=22, Q_8(13)=25. Together with FZD's M_6=11, all h=4..8 are closed. Transport also closes M_13=22, M_18=31, M_21=37. Of 82 exceptional h from FZB, 32 exact, 44 width one, 6 width two; 50 unresolved.

## General terminal-capacity certificate
Take target budget m+c, depth d=h+c-1. Follow the all-zero path (without duplicate probes); if it terminates early, append unused probes arbitrarily to depth d, provided d<=10m. Such padding of a terminal or impossible transcript retains at most one state. Otherwise the remaining budget is m-h+1. For U define b_U=#columns whose zero-row mask intersects U. If b_U<h, the state with exactly these forced holes requires a positive query in every unforced column: otherwise adding that column as a hole gives an indistinguishable state. Thus b_U>=h-1 for a compatible support. A support at b_U=h-1 uses the entire remaining budget on positive answers, so at most one such support exists, since the same all-positive answer path cannot recover two different states. The statement also holds for the padded case: a compatible support with b_U<h alone supplies at least two states. For b_U>h there are no states.

Let T be the exact number of compatible labeled states after the zero prefix. It equals sum over U of sum_{k=0}^{h-b_U} binom(m-b_U,k), with empty sums zero. Put y_U=max(0,h+1-b_U), f_U=1[b_U=h-1]. Then T=sum_U (y_U+(m-h)f_U), with sum f_U<=1. A necessary condition is T<=2^(m-h+1), also valid after padding.

For any nonnegative integer weight pairs p_U,q_U and integers R>0, A,B,v>=0 satisfying q_U<=R, p_U<=(m-h)R+v and sum_{U:S intersects U}(p_U+q_U)<=A+B|S| for every nonempty row mask S:
p_U(h-b_U)+q_U(h+1-b_U)<=R[y_U+(m-h)f_U]+v f_U.
For b=h-1 this follows from p+2q<=(m-h+2)R+v, for b=h it follows from q<=R, and for b>=h+1 the left side is nonpositive. Sum over supports and use the per-column certificate (at most m nonempty columns, exactly d distinct probes). We get
T >= ceil((h sum(p)+(h+1)sum(q)-A m-B d-v)/R).
This upgrades the old weighted-cover certificate: it retains actual residual multiplicities, not just which supports remain. It is a necessary condition for exact adaptive recovery for any finite nonempty support family, not a sufficient strategy criterion.

For h=5,m=8,c=8,d=12, the weights below give R=23,A=237,B=465,v=28, sum(p)=684,sum(q)=769. All 1023 nonempty masks satisfy the integer inequality. Thus T>=ceil(530/23)=24, exceeding capacity 16. This excludes m=8; any smaller m>h achieving the stable cost would extend to m=8 by first recovering the old columns then observing a known positive row of U in each appended column. Hence M_5>=9. No reliance on numerical optimizer infeasibility. FZC's (A,q,W,v)=(27,64,198,22) certificate gives M_7>=ceil(276/27)=11 and M_8>=ceil(346/27)=13. Parent stable cost law c_h=ceil((15h+6)/11) gives the query lower bounds.

## Upper strategies
The exact zero orders below are indexed from row/column zero. Stop at first positive. In positive column j, eligible supports contain row r and avoid preceding zero mask in j. Given b_U forced holes, the support leaf deadline is m+c-i minus (0 if b_U=h else m-1-b_U). Identify U by row queries in live j within its individual deadline; after that, all forced holes and known-live j are known. If b_U=h, all other labels are live; otherwise query a row of U in each remaining unforced column other than j. This is a lossless label recovery proof, with no independence assumption. Late branches and zero terminal are solved by exact bitset recursion over all labeled states; replay each state to verify its unique leaf and budget. Distinct histories are covered by first positive position or zero terminal.

Actual local Python runs (standalone below) passed:
h=5,m=9: 13 branches, 202 support leaves, 474 labeled explicit replays.
h=7,m=11: 18 branches, 352 support leaves, 134 labeled explicit replays.
h=8,m=13: 20 branches, 403 support leaves, 159 labeled explicit replays.
Total: 51 branches, 957 support leaves, 767 explicit labeled replays. Each complete upper tree uses at most m+c. Lower + upper close all three.

## Reproduction: Python 3, integer-only checker
```python
from functools import lru_cache
from itertools import combinations
F=(23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005)
pw={86:35,101:81,299:29,394:97,412:30,460:22,602:97,646:62,673:97,788:97,828:22,833:15}
qw={23:23,86:23,91:4,101:23,123:23,157:23,175:12,203:18,211:23,243:23,281:23,299:23,301:23,327:23,346:23,371:13,389:6,394:23,410:23,412:23,457:23,460:23,486:13,602:23,613:23,646:23,673:23,697:23,718:23,721:23,753:23,788:23,828:23,833:23,857:13,867:23,980:23}
assert set(pw)|set(qw)<=set(F)
assert sum(pw.values())==684 and sum(qw.values())==769
assert max(pw.values())<=97 and max(qw.values())<=23
for s in range(1,1024):
 assert sum(pw.get(u,0)+qw.get(u,0) for u in F if u&s)<=237+465*s.bit_count()
assert 5*684+6*769-237*8-465*12-28==530>23*16
print('lower h5m8: 1023 mask inequalities pass; terminal >= ceil(530/23)=24>16')
R=[sum(1<<i for i,u in enumerate(F) if u>>r&1) for r in range(10)]
orders={
 (5,9):[(0,0),(2,2),(6,4),(8,6),(4,7),(7,5),(1,1),(9,8),(3,3),(0,1),(2,3),(8,7)],
 (7,11):[(0,9),(2,3),(0,1),(1,0),(8,8),(4,5),(7,7),(6,6),(9,10),(3,4),(2,2),(0,2),(1,1),(0,0),(8,9),(2,4),(3,3)],
 (8,13):[(0,2),(2,3),(0,1),(1,4),(8,11),(4,6),(7,9),(6,7),(9,12),(3,5),(0,0),(8,10),(2,5),(7,8),(4,9),(1,2),(0,6),(2,4),(1,1)]}
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
def explicit(st,m,d):
 full=(1<<len(st))-1;qs={}
 for r in range(10):
  for j in range(m):
   q=sum(1<<i for i,(u,b) in enumerate(st) if u>>r&1 and not b>>j&1)
   if q and q!=full:qs[q]=(r,j)
 @lru_cache(None)
 def rec(X,k):
  if X.bit_count()<=1:return ()
  if not k or X.bit_count()>1<<k:return None
  opts=[]
  for q in qs:
   B=X&q;E=X^B
   if B and E and max(B.bit_count(),E.bit_count())<=1<<(k-1):opts.append((max(B.bit_count(),E.bit_count()),q,B,E))
  for _,q,B,E in sorted(opts):
   a=rec(B,k-1)
   if a is not None:
    b=rec(E,k-1)
    if b is not None:return (q,a,b)
  return None
 t=rec(full,d)
 if t is None:return False
 for i,(u,b) in enumerate(st):
  node=t;X=full;k=0
  while node:
   q,a,e=node;r,j=qs[q];v=bool(u>>r&1 and not b>>j&1);X=X&q if v else X&~q;node=a if v else e;k+=1
  assert X==1<<i and k<=d
 return True
def support(p,h,c,r,j,i):
 m=len(p);dl={}
 for a,u in enumerate(F):
  b=sum(bool(s&u) for s in p)
  if u>>r&1 and not p[j]&u and b<=h:dl[a]=m+c-i-(0 if b==h else m-1-b)
 @lru_cache(None)
 def rec(X,d):
  if not X:return ()
  if any(dl[a]<d for a in dl if X>>a&1):return None
  if X.bit_count()==1:return ()
  for r,q in enumerate(R):
   B=X&q;E=X^B
   if B and E:
    a=rec(B,d+1)
    if a is not None:
     b=rec(E,d+1)
     if b is not None:return (r,a,b)
  return None
 X0=sum(1<<a for a in dl);t=rec(X0,0)
 if t is None:return None
 for a in dl:
  node=t;X=X0;d=0
  while node:
   r,b,e=node;v=bool(F[a]>>r&1);X=X&R[r] if v else X&~R[r];node=b if v else e;d+=1
  assert X==1<<a and d<=dl[a]
 return len(dl)
for (h,m),O in orders.items():
 c=(15*h+16)//11;p=[0]*m;total=0;leaves=0;records=[]
 assert len(O)==h+c-1
 for i,(r,j) in enumerate(O,1):
  n=support(p,h,c,r,j,i)
  if n is not None:leaves+=n;records.append((i,'support',n,m+c-i))
  else:
   st=physical(p,h,(r,j));assert explicit(st,m,m+c-i);total+=len(st);records.append((i,'physical',len(st),m+c-i))
  assert not p[j]>>r&1;p[j]|=1<<r
 st=physical(p,h);assert explicit(st,m,m+c-len(O));total+=len(st);records.append((len(O)+1,'terminal',len(st),m+c-len(O)))
 print(h,m,'budget',m+c,'branches',len(records),'support leaves',leaves,'labeled replay',total,'PASS');print(records)
```
Actual output:
```
lower h5m8: 1023 mask inequalities pass; terminal >= ceil(530/23)=24>16
5 9 budget 17 branches 13 support leaves 202 labeled replay 474 PASS
[(1,'support',37,16),(2,'support',29,15),(3,'support',29,14),(4,'support',27,13),(5,'support',28,12),(6,'support',26,11),(7,'support',26,10),(8,'physical',204,9),(9,'physical',135,8),(10,'physical',64,7),(11,'physical',31,6),(12,'physical',14,5),(13,'terminal',26,5)]
7 11 budget 22 branches 18 support leaves 352 labeled replay 134 PASS
[(1,'support',37,21),(2,'support',29,20),(3,'support',37,19),(4,'support',26,18),(5,'support',27,17),(6,'support',28,16),(7,'support',26,15),(8,'support',29,14),(9,'support',22,13),(10,'support',25,12),(11,'support',27,11),(12,'support',17,10),(13,'support',8,9),(14,'support',14,8),(15,'physical',59,7),(16,'physical',30,6),(17,'physical',21,5),(18,'terminal',24,5)]
8 13 budget 25 branches 20 support leaves 403 labeled replay 159 PASS
[(1,'support',37,24),(2,'support',29,23),(3,'support',37,22),(4,'support',26,21),(5,'support',27,20),(6,'support',28,19),(7,'support',26,18),(8,'support',29,17),(9,'support',22,16),(10,'support',25,15),(11,'support',37,14),(12,'support',25,13),(13,'support',15,12),(14,'support',21,11),(15,'support',11,10),(16,'support',8,9),(17,'physical',72,8),(18,'physical',33,7),(19,'physical',27,6),(20,'terminal',27,6)]
```

## Transport replay
Use the identical literal D and P in FZC (fixed commit above). Independent exact integer JS replay checked all 6*1023 mask inequalities, 22*50 support covers, block observation counts, and both envelopes on h=4..183. To reproduce, use FZC's Python loop with explicit known bases {5:9,6:11,7:11,8:13}: add (base[h],0) to choices and set lo=max(lo,base[h]) when present. Keep h4 and FZB exact lower-endpoint bases as before; no additional changes to B. Recompute ascending. Against FZD, changes [h,lower,upper] are [[5,9,9],[7,11,11],[8,13,13],[13,22,22],[18,31,31],[21,37,37]]. Counts by width old {0:26,1:48,2:8}, new {0:32,1:44,2:6}. All intervals remain consistent. These are constructive upper bounds with parent-dependent lower certificates.

## Control and next
Original own registration r4-20261124-0240-ec49fyh-own-session-v1 read SUCCEEDED; historical EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76. Current topic receipt r4-20261125-0130-ec49as-read read SUCCEEDED at c29aea95adca6f1055b5eaf4a9afd2d14bcf7127; NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection. A redundant task call hit BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; original successful receipt was consumed, not replayed further. Independent portable non-overwriting research; no shared claim, no formal Result/Review, current private writer binding not established, Activity association pending. Next: h=9..12 and other remaining cases. Use terminal-capacity duals to exclude lower endpoints before last-positive branch checks; seek constructions at remaining lower endpoints. AUTHOR_PROVED / EXACT_FINITE_BRANCH_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
