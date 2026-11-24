# EC49FZD — Exact six-hole minimum inventory and last-positive obstruction
2026-11-25. Frozen BRC16943 auxiliary Boolean observer, exactly as FZC at 725a6c9d6695346a9a6dd762efa6587af10fd7dc: state (U,H), U in literal 50-support family F, H subset of m labeled columns with |H|<=h<m, unit noiseless queries W(r,j)=1[r in U]1[j not in H], exact joint recovery. Parent-dependent, author-proved, not independently reviewed; no new native X6 attribution.

## Main result
M_6=11 and Q_6(11)=20. The previous interval [10,13] is closed. The obstruction to m=10 is genuinely adaptive: a feasible static 10-column prefix exists and even its all-zero terminal is solvable, but every possible final positive branch is impossible within budget.

## Lower bound
Reuse the FZC/FYU all-zero prefix lemma with h=6,c=9,d=h+c-1=14. A winning strategy with budget m+9 has a feasible zero prefix of length <=14 whose distinct forced-hole cover b(U) is >=6 except at most one support with b=5. Redundant repeated observations can be discarded. For any nonnegative support weights, each column mask S contributes sum_{U:S intersects U}w_U <= A+q popcount(S), so hW-w_def <= A*m+q*d. If no deficient support, w_def=0.

First certificate A=1,q=3,W=9 has weights {86:1,101:1,299:1,394:1,460:1,602:1,673:2,788:1}. For m<=10, 54-w_def<=52 forces m=10, d=14 and unique deficient support 673. This also excludes earlier saturation or stopping. Second certificate A=18,q=46,W=140 and w_673=16 has weights listed in checker. Its inequality is tight: 6*140-16=824=18*10+46*14. Thus all 10 columns nonempty, all 14 distinct probes used, every positive-weight support has exactly its required cover, and every column mask is tight. The 18 possible tight masks are [1,2,3,4,5,6,8,9,12,16,17,64,128,144,192,256,320,512]. The equality system of 17 positive-weight support rows, total columns and total probes has rank 18 modulo 101 (hence over Q). Its unique solution is the multiset (1,1,2,4,12,144,192,256,320,512), up to physical labels. The checker verifies that solution meets all 50 cover constraints.

Any ordering of this multiset ends at one of its 14 distinct row-column probes. Remove that probe from its mask, leaving all other observations zero, and instead answer it positively. All compatible labeled states are generated exactly by the displayed observer. Their remaining budget is 19-14=5. Twelve of the fourteen branches have >32 states (information bound). The other two, (row 2,col 4) and (row 6,col 6) with zero-based column labels in the listed multiset, each have 30 states. Exact exhaustive binary decision search over all 100 allowed queries and all compatible states excludes both within depth 5. Recurrence: win(A,d)=true if |A|<=1; false if d=0 or |A|>2^d; otherwise OR over all nonconstant queries of win(A intersect Q,d-1) AND win(A minus Q,d-1). This is exhaustive by the first-query decomposition, with only safe cardinality pruning. All last-probe possibilities fail. Hence M_6>=11. The separate local all-zero terminal check found 28 compatible states solvable at depth 5, illustrating why static coverage and terminal-only analysis cannot establish the upper bound.

## Upper bound
At m=11 use the following fixed all-zero path, stopping at the first positive:
(9,10),(8,9),(8,8),(4,6),(2,4),(1,2),(0,1),(7,7),(6,9),(6,7),(0,0),(7,6),(3,5),(2,3).
For the first ten positive branches, use FZA's support-specific leaf deadlines. At step i, positive column j, candidate U contains positive row and avoids all preceding zero rows in j. Let b count distinct columns whose preceding mask intersects U. Then depth deadline for learning U by queries in the live column j is 20-i-(0 if b=6 else 10-b). Once U is known, the b forced holes are identified; if b=6 all other labels are live, otherwise probing one row of U in each of the 10-b remaining unforced columns other than j recovers exact labels. The checker reconstructs support decision trees and replays all candidate leaves with their own deadlines. For steps 11..14 use the explicit full-state recurrence, at budgets 9,8,7,6 respectively; terminal all-zero budget 6. All branches win. Therefore Q_6(11)<=20; parent stable lower law gives equality and M_6=11.

## Executed evidence
Local Python exhaustive branch checks and an independently implemented JavaScript BigInt exact verifier both passed. Both integer weight inequalities checked on every nonempty 10-bit mask (2046 inequalities); 18-column equality rank verified in SymPy and modulo 101. Last-probe branch state counts in order (row,col,count):
[0,0,87],[0,1,87],[1,2,59],[2,3,58],[2,4,30],[3,4,39],[4,5,39],[7,5,36],[6,6,30],[7,6,48],[8,7,60],[6,8,41],[8,8,40],[9,9,62]. All fail depth 5.
Upper branch results (step,method,candidate count,min support deadline or explicit budget):
[1,support,22,9],[2,support,27,8],[3,support,27,8],[4,support,28,6],[5,support,29,5],[6,support,26,4],[7,support,37,4],[8,support,26,4],[9,support,15,3],[10,support,15,3],[11,explicit,372,9],[12,explicit,120,8],[13,explicit,79,7],[14,explicit,40,6],[15,terminal,24,6]. All pass. Full labeled terminal/late-branch replay covers 635 states; early branches use exact analytical labeled recovery with all support leaves checked.

## Reproduction (Python 3; standalone exact checker, SymPy only for rank)
```python
from functools import lru_cache
from sympy import Matrix
F=(23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005)
D=[(1,3,[(86,1),(101,1),(299,1),(394,1),(460,1),(602,1),(673,2),(788,1)]),(18,46,[(23,2),(86,8),(101,14),(157,2),(243,7),(281,5),(299,9),(394,11),(410,2),(412,5),(460,11),(602,17),(646,8),(673,16),(697,2),(788,14),(833,7)])]
def weight(w,s):return sum(n for u,n in w if u&s)
for A,q,w in D:
    assert all(weight(w,s)<=A+q*s.bit_count() for s in range(1,1024))
assert [sum(n for u,n in w) for A,q,w in D]==[9,140]
A,q,w=D[1]
T=[s for s in range(1,1024) if weight(w,s)==A+q*s.bit_count()]
M=[1,1,2,4,12,144,192,256,320,512]
assert len(T)==18 and Matrix([[int(bool(s&u)) for s in T] for u,n in w]+[[1]*18,[s.bit_count() for s in T]]).rank()==18
assert all(s in T for s in M) and sum(s.bit_count() for s in M)==14
assert all(sum(bool(s&u) for s in M)>=6-int(u==673) for u in F)
assert all(sum(bool(s&u) for s in M)==6-int(u==673) for u,n in w)
def physical(p,pos=None):
    m=len(p);out=[]
    for u in F:
        if pos and (not(u>>pos[0]&1) or p[pos[1]]&u):continue
        req=sum(1<<j for j,s in enumerate(p) if s&u)
        for h in range(1<<m):
            if h&req==req and h.bit_count()<=6 and (not pos or not h>>pos[1]&1):out.append((u,h))
    return out
def explicit(states,m,budget):
    n=len(states);full=(1<<n)-1
    if n>1<<budget:return False
    qs={}
    for r in range(10):
        for j in range(m):
            q=sum(1<<i for i,(u,h) in enumerate(states) if u>>r&1 and not h>>j&1)
            if q and q!=full:qs[q]=(r,j)
    @lru_cache(None)
    def rec(A,d):
        if A.bit_count()<=1:return ()
        if not d or A.bit_count()>1<<d:return None
        opts=[]
        for q in qs:
            B=A&q;E=A^B
            if B and E and max(B.bit_count(),E.bit_count())<=1<<(d-1):
                opts.append((max(B.bit_count(),E.bit_count()),q,B,E))
        for _,q,B,E in sorted(opts):
            a=rec(B,d-1)
            if a is not None:
                b=rec(E,d-1)
                if b is not None:return(q,a,b)
        return None
    tree=rec(full,budget)
    if tree is None:return False
    for i,(u,h) in enumerate(states):
        A=full;node=tree;d=0
        while node:
            q,a,b=node;r,j=qs[q];v=bool(u>>r&1 and not h>>j&1)
            A=A&q if v else A&~q;node=a if v else b;d+=1
        assert A==1<<i and d<=budget
    return True
for j,s in enumerate(M):
    for r in range(10):
        if s>>r&1:
            p=M.copy();p[j]^=1<<r;st=physical(p,(r,j))
            assert not explicit(st,10,5);print('excluded',r,j,len(st))
assert explicit(physical(M),10,5)
R=[sum(1<<i for i,u in enumerate(F) if u>>r&1) for r in range(10)]
def support(cand,dl):
    @lru_cache(None)
    def rec(A,d):
        if not A:return ()
        if any(dl[i]<d for i in cand if A>>i&1):return None
        if A.bit_count()==1:return ()
        for r,q in enumerate(R):
            B=A&q;E=A^B
            if B and E:
                a=rec(B,d+1);b=rec(E,d+1)
                if a is not None and b is not None:return(r,a,b)
        return None
    t=rec(sum(1<<i for i in cand),0);assert t is not None
    for i in cand:
        node=t;A=sum(1<<a for a in cand);d=0
        while node:
            r,a,b=node;v=bool(F[i]>>r&1);A=A&R[r] if v else A&~R[r];node=a if v else b;d+=1
        assert A==1<<i and d<=dl[i]
order=[(9,10),(8,9),(8,8),(4,6),(2,4),(1,2),(0,1),(7,7),(6,9),(6,7),(0,0),(7,6),(3,5),(2,3)]
p=[0]*11
for i,(r,j) in enumerate(order,1):
    cand=[];dl={}
    for a,u in enumerate(F):
        b=sum(bool(s&u) for s in p)
        if u>>r&1 and not p[j]&u and b<=6:
            cand.append(a);dl[a]=20-i-(0 if b==6 else 10-b)
    if i<=10:
        support(cand,dl);print(i,'support',len(cand),min(dl.values()))
    else:
        st=physical(p,(r,j));assert explicit(st,11,20-i);print(i,'explicit',len(st))
    assert not p[j]>>r&1;p[j]|=1<<r
assert explicit(physical(p),11,6);print('terminal',len(physical(p)),'PASS')
```

## Transport consequences
Apply FZC's exact same witnessed B(k) for k=1..22 and compatible cost condition c_h-c_(h-k)=ceil(26k/11)-k. Initialize previous upper bounds, replace M_6 upper with 11, then iterate the min recurrence in increasing h=4..183. Actual integer JavaScript replay of the 82 previous exceptional rows yields improvements (h,new lower,new upper):
(6,11,11),(7,11,12),(10,16,17),(11,19,20),(13,22,23),(16,28,29),(18,31,32),(19,34,35),(21,37,38),(24,43,44),(29,52,53),(32,58,59).
No other previously unresolved h becomes exact from this transfer alone. FZC had 57 unresolved exceptions, now 56; all remaining intervals have width <=2. For reproduction, take the prior printed rows and B from FZC, set hi[6]=11 and recompute hi[h]=min(old_hi[h], hi[h-k]+B[k] for compatible k); exact lower-endpoint h use FZB formula and all other lower bounds unchanged.

## Control and next
Original session registration r4-20261124-0240-ec49fyh-own-session-v1 read SUCCEEDED, historical researcher EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76; private writer binding not established here. Current exact topic read r4-20261125-0030-ec49as-read-v1 SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY at 77e98fea29357c0dce95b71e200a897e9b95aefb, directory observation only, no native owner projection or shared CLAIM. Independent portable research only. Activity association pending. Next: h=5,7,8 and residual finite exceptions; use conditional prefix weights and last-positive obstruction, then explicit labeled branch certification where needed. AUTHOR_PROVED / EXACT_FINITE_BRANCH_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
