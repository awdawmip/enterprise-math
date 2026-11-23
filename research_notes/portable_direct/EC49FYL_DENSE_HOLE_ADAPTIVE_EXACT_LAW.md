# EC49FYL — exact maximal-hole adaptive law, fixed-hole stabilization, and two-hole finite atlas

Date 2026-11-24. Independent portable continuation of Research-4, registration provenance EM-DIRECT-23537B (original r4-20261124-0240-ec49fyh-own-session-v1 succeeded, own custody status active; no execution authorization or formal CLAIM). Frozen auxiliary BRC16943 50-support atlas, not a native X6 dynamics attribution or claim of new arithmetic realizability.

Sources:
- EC49FYK_MULTI_HOLE_EXACT_LAW.md at c92b88b5c5553d18217d4b4ccdfd1a747a232b43, path research_notes/portable_direct/EC49FYK_MULTI_HOLE_EXACT_LAW.md (exact fixed-observation multi-hole law and frozen support list).
- EC49FYJ_ALL_COLUMN_COUNT_ADAPTIVE_LAW.md at 5ae20314d4709ae4913154874de4ca5da7a874b1, same directory (one-hole adaptive base, particularly Q_1(2)=8, full support lower witness).
- Current task read r4-20261124-0634-ec49as-current-task-v1: SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY at a093e769efb9aca88ef3ad39dbbf7ab6a558d664; limited directory absence, not owner projection. No shared owner taken over.

## Model
For integer m>=1 and 0<=h<m, a state (U,Z) consists of U in the exact nonempty ten-bit family F below, and a labeled subset Z of columns with |Z|<=h. Query (t,j) returns bit_t(U)*1[j notin Z], unit cost, noiseless, exact labeled recovery; Q_h(m) is minimax depth. Full array identifies these states because at least one live column remains. No label or hole multiplicity is erased.

## Theorem A: maximal-hole exact adaptive law
For every m>=2,
Q_{m-1}(m)=3m+2.
Thus dense holes have a different slope from fixed h.

### Lower
Let A(T)={U in F: U&T=0}, where T is a set of queried row positions in a column on the all-zero transcript. The following finite properties follow from exhaustive enumeration of the 10 single rows and 45 pairs, reproduced below:
- |A(empty)|=50, min for one row is 13.
- Every two distinct rows leave at least 4 supports.
- Exactly two pairs attain 4: rows (0,2) give {346,394,410,602}, rows (0,8) give {86,602,646,718}; both contain 602.

Suppose a depth <=3m+1 tree exists. Ignore repeated or constant probes when present (they cannot help). Follow the all-zero transcript. As long as some column has at most two probes, at least four one-live states in that column are consistent (all other columns holes); hence this transcript cannot terminate or become impossible before every column has received its third probe. Consider the instant just after the penultimate column has received its third probe. The last column has k<=2 probes. At least 3(m-1)+k total queries have been used, leaving at most 4-k. If k=0, the 50 one-live states exceed 2^4; if k=1, at least 13 exceed 2^3. Hence k=2. Immediately before the penultimate third query, both last columns have exactly two probes, the other m-2 columns have at least three, and at least 3m-2 queries have been spent. Only three further queries are available, capacity 8. Let their two residual support sets be A and B. For each U in A or B there is a distinct one-live state in the corresponding column (the two lists of labeled states are disjoint), and for each U in A intersect B there is an additional state with both columns live and all others holes. Every one of these states is consistent with the all-zero prefix. Thus at least |A|+|B|+|A intersect B| states survive. If either set has >=5 then the count is >=9; otherwise both have size 4 and their intersection contains 602, again >=9. Contradiction. This uses the JOINT two-live residual, not only the union of the separate one-live fibres. It proves Q>=3m+2, including m=2.

### Upper
Single-column scan rows (1,2,0) in this order; their union hits every support. Three zeros certify a hole; if a positive is seen, the support is completely identifiable within at most six total probes in that column. The latter is an exact finite decision-tree fact: for each first-positive residual set, evaluate D(S)=1+min_t max(D(S intersect R_t),D(S minus R_t)), D=0 for |S|<=1, considering splitting rows only. The verified total depths for the three possible first-positive branches are at most 6 (code below). In the first m-2 columns, scan sequentially until a positive appears. If k complete hole columns precede the positive, identify U and read the remaining m-k-1 columns once at a known row in U. Cost <=3k+6+(m-k-1)=m+2k+5<=3m-1 since k<=m-3. If all first m-2 columns are holes, the last two columns have at most one hole and the exact FYJ depth-8 tree applies. Cost 3(m-2)+8=3m+2. All original labels are retained. For m=2 simply use FYJ. This proves upper and lower match for all m.

## Theorem B: extension and eventual slope for every fixed hole budget
For any nonempty distinct support family, m>h, Q_h(m+1)<=Q_h(m)+1: restrict to first m columns and run its full labeled tree. It identifies U and original holes; the new column is read once at a known support row (or inferred live if budget exhausted). Therefore Q_h(m)-m is nonincreasing in m. For this F and h>=1 the full U=833 state has m same-support single-hole competitors and three full supersets 857,867,965 with disjoint additions 24,34,132, requiring at least m+3 queries. Consequently the integer excess is eventually constant c_h>=3. Theorem A at m=h+1 gives Q_h(m)<=m+2h+4, hence 3<=c_h<=2h+4. This proves eventual exact slope one, not a numerical extrapolation, and yields lim_{m->infty} N_h(m)/Q_h(m)=3 for every fixed h>=1 using FYK. At maximal density h=m-1, FYK gives N=8m and the ratio tends instead to 8/3. All bounds refer to unit physical reads, not CPU time.
Other general lower bound: ceil(log2(50*sum_{i=0}^h binom(m,i))). The two-hole case below improves c_2<=5.

## Finite two-hole results
Exact labeled states with h=2:
m=3: Q=11 (Theorem A, also exhaustive infeasibility at depth 10 and constructive replay).
m=4: Q=10 (550 states, information lower bound 10, replay depth 10).
m=5: Q=10 (800 states, information lower bound 10, replay depth 10).
m=6: Q=11 (1100 states, information lower bound 11, replay depth 11).
m=7: 11<=Q<=12; depth 12 constructed, depth 11 search timed out (5 and 30 second bounded trials; no negative claim).
m=8: 12<=Q<=13; complete depth 11 search returned false; depth 13 constructed; depth 12 trial incomplete (no negative claim).
For every m>=5, Q_2(m)<=m+5 by extension. For every m>=3, Q_2(m)>=m+3. Thus c_2 in {3,4,5}. No claim that c_2 has been determined.

## Executed exact integer verification and reproducible Python
All computations use Python arbitrary-precision integers; no float arithmetic is used for the scientific conclusions. Search treats all labeled states explicitly; memo records valid lower/upper depth and successful query. At a node a binary tree with depth d cannot have more than 2^d leaves. All nonconstant probes with both branch sizes <=2^(d-1) are enumerated, except identical/complementary bipartitions (equivalent for feasibility). Failure after all possible splits is exhaustive. Successful tree is independently replayed against every raw state, without memo or pruning. The following code reproduces the finished cases; the original bounded attempts for m7 depth11 and m8 depth12 were not completed and are not included as negatives.

```python
from functools import lru_cache
from itertools import combinations, product
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
assert len(F)==len(set(F))==50
def rem(T): return {u for u in F if not u&T}
assert min(len(rem(1<<t)) for t in range(10))==13
pairs={p:rem(sum(1<<i for i in p)) for p in combinations(range(10),2)}
assert min(map(len,pairs.values()))==4
assert {p:sorted(s) for p,s in pairs.items() if len(s)==4}=={(0,2):[346,394,410,602],(0,8):[86,602,646,718]}
R=[sum(1<<i for i,u in enumerate(F) if u>>t&1) for t in range(10)]
A=(1<<50)-1
@lru_cache(None)
def depth(s):
    if s.bit_count()<=1:return 0
    return 1+min(max(depth(s&r),depth(s&~r)) for r in R if s&r and s&~r)
s=A; totals=[]
for k,t in enumerate((1,2,0),1):
    totals.append(k+depth(s&R[t]));s&=~R[t]
assert s==0 and max(totals)==6
print("scan depths",totals)

def run(m,h,d,expected):
    Z=[z for z in range(1<<m) if z.bit_count()<=h]
    S=list(product(F,Z));N=len(S);A=(1<<N)-1
    R=[sum(1<<i for i,(u,z) in enumerate(S) if u>>t&1 and not z>>j&1) for t in range(10) for j in range(m)]
    memo={};calls=0
    def solve(s,d):
        nonlocal calls
        calls+=1
        n=s.bit_count()
        if n<=1:return True
        if n>1<<d or d==0:return False
        lo,hi,q=memo.get(s,(0,999,-1))
        if lo>d:return False
        if hi<=d:return True
        opts=[];cap=1<<(d-1);seen=set()
        for i,r in enumerate(R):
            b=s&r;a=s^b
            if not a or not b:continue
            if a in seen or b in seen:continue
            seen.add(a)
            na=a.bit_count();nb=n-na
            if max(na,nb)<=cap:opts.append((max(na,nb),i,a,b,na,nb))
        opts.sort()
        for _,i,a,b,na,nb in opts:
            if na<nb:a,b=b,a
            if solve(a,d-1) and solve(b,d-1):
                memo[s]=(lo,d,i);return True
        memo[s]=(max(lo,d+1),hi,q);return False
    ok=solve(A,d);assert ok==expected
    print(m,h,d,N,ok,calls,len(memo))
    if not ok:return
    def tree(s,d):
        if s.bit_count()==1:return -s.bit_length()
        assert solve(s,d)
        _,_,i=memo[s];b=s&R[i]
        return [i,tree(s^b,d-1),tree(b,d-1)]
    T=tree(A,d);mx=total=0
    for i,(u,z) in enumerate(S):
        node=T;k=0
        while isinstance(node,list):
            r,j=divmod(node[0],m)
            node=node[1+int(bool(u>>r&1 and not z>>j&1))];k+=1
        assert node==-1-i;mx=max(mx,k);total+=k
    assert mx<=d
    print("verified",mx,total)
for m,d,ok in [(3,10,False),(3,11,True),(4,10,True),(5,10,True),(6,11,True),(7,12,True),(8,11,False),(8,13,True)]:
    run(m,2,d,ok)
```

Actual original search output (m,h,d,states,feasible,calls,memo; wall-clock omitted):
```
3 2 10 350 False 34115 13688
3 2 11 350 True 699 349
verified 11 3004
4 2 10 550 True 1099 549
verified 10 5046
5 2 10 800 True 1606 806
verified 10 7796
6 2 11 1100 True 22750 7410
verified 11 11307
7 2 12 1450 True 59371 10348
verified 12 15534
8 2 11 1850 False 4105 4105
8 2 13 1850 True 1173820 113799
verified 13 20938
```

## Scope and next
AUTHOR_PROVED / EXACT_FINITE_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. Dense proof needs only single/pair residual counts, single-column scan tree and previously verified FYJ two-column depth-8 base; no claim about altered Farey moduli, heartbeat arithmetic or native X6 correspondence. Next: exploit exact joint two-live residual for tighter two-hole lower bounds and compute c_2; preserve all completed single-/multi-hole nonadaptive and one-hole adaptive results without recomputing them. For h>=2 intermediate density, determine sharp Q_h(m), not only endpoint/asymptotic laws.
