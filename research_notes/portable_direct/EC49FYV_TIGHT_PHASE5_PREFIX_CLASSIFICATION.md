# EC49FYV — exact terminal-prefix classification in phase 5

2026-11-24. Frozen auxiliary Boolean observer BRC16943: 50 distinct nonempty supports F on ten rows, labeled state (U,H), |H|<=h<m, W(t,j)=1[t in U]1[j not in H], unit noiseless adaptive probes. Parent pins actually read: 10f0597c6c988fc0adcfbc8fda748367587745bb:research_notes/portable_direct/EC49FYU_UNIQUE_DEFICIENT_PREFIX.md (unique deficient support and dual certificate); 438163ba045e2d3ea8d27bbb81004694f5069ae0:research_notes/portable_direct/EC49FYT_EVENTUAL_PERIODIC_EXCESS.md (transport and eventual period); ce7abff378aa77006334656fd9396bf9f8666bdf:research_notes/portable_direct/EC49FYQ_FINITE_EXCESS_GAME_THREE_HOLE_LAW.md (finite excess game). No new native X6 attribution.

## Theorem: rigid terminal row vectors and finite inventory obstruction

Let h=4+11a, a>=0. Assume a correct tree of worst depth m+6+15a, the bare multicover lower bound in this phase. At the all-zero prefix of length d=9+26a, FYU implies the unique deficient support u is 394 or 673, with exactly h-1 forced holes; all other supports force at least h. All eight weighted supports attain their prescribed bounds exactly, row 5 is absent and no weighted support counts two hits in the same physical column. Let x_t be the query multiplicity of row t. Then necessarily:

u=394: x=(6a+2,5a+1,4a+1,a,a+1,0,a+1,2a+1,3a+1,3a+1).
u=673: x=(6a+2,5a+2,4a+2,a+1,a,0,a,2a,3a+1,3a+1).

Proof: the eight linear equations are sum_{t in v}x_t=h-1[v=u] for v in W=(86,101,281,394,460,602,673,788); x5=0. The determinant of their coefficient matrix after removing column 8 is -11 (row order W then x5; ascending column order). Thus the solution with free parameter z=x8 is unique. Substitution gives
394: (6a+2,5a+1,7a-z+2,4a-z+1,a+1,0,z-2a,2a+1,z,3a+1);
673: (6a+2,5a+2,7a-z+3,4a-z+2,a,0,z-2a-1,2a,z,3a+1).
For both, the excess row counts over h on supports 346 and 412 are z-3a-1 and 3a+1-z. Actual forced-hole counts cannot exceed row counts; both supports are nondeficient, hence z=3a+1. This yields exactly the stated vectors. At a=0 the 673 vector fails support 721 (and 753); the 394 vector has all required row counts. For a>=1, both vectors meet all row-count requirements, by the affine integer certificate below.

Physical-column rigidity: define tight supports by row hits exactly h-1[v=u]. No pair of row probes on the same column can both belong to a tight support, because the actual distinct-column hit count would then be strictly smaller than required. Every used row belongs to a tight support, so repeated rows on a column are also excluded. At a=0 the 394 vector has tight supports (86,101,281,299,301,346,394,410,412,460,602,646,673,788,828); every pair of used distinct rows occurs together in some tight support. Thus all nine probes must occupy different physical columns.

For a>=1 the tight set for both vectors is (86,101,281,346,394,412,460,602,673,788). The only pair of used rows not co-contained in this set is (0,1). Therefore any repeated physical column has exactly these two probes. Write p for their number. Supports 91 and 123 contain both rows and have surplus 3a+1, so p<=3a+1. Conversely, the minimum surplus among all supports containing both is 3a+1, and both row inventories have at least that many copies of 0 and 1. Hence every integer p in [0,3a+1] is realizable by a static assignment of pairs and singleton columns with the required distinct-column hit counts (not a winning adaptive strategy). The exact minimum number of columns supporting the static terminal prefix is consequently 23a+8 for a>=1, and 9 for a=0.

Corollary (uniform finite-column strengthened lower bound): Q_4(m)>=m+7 for 5<=m<=8. For a>=1 and 4+11a<m<23a+8, Q_(4+11a)(m)>=m+7+15a. For m above these bounds, existence of the static prefix alone does not establish equality. This is a new finite-inventory obstruction, not a determination of c4 or the eventual offset.

## Exact residual game at the four-hole terminal prefix

Take a=0 and assign the nine row probes to distinct labeled columns with row list T=(0,0,1,2,4,6,7,8,9). By column symmetry the residual states after nine zeros are independent of query order. Exactly fourteen supports force four holes and each yields one labeled state; support 394 forces three holes and gives one state with just these holes plus m-3 states with one extra hole. Thus there are m+12 compatible states. Remaining depth for budget m+6 is m-3. Necessity of that depth follows from the no-extra-hole 394 target: every live column needs a positive probe to exclude its extra-hole competitor. Exact binary split search on all 21 states at m=9 succeeds in depth 6, using all legal physical row/column probes. For every m>9 extend that solution: run the nine-column decoder ignoring added columns; if it finds four holes, all extra columns are live; otherwise U=394 and only three holes were found, so test a row in U on each extra column to identify any extra hole. Depth <=6+(m-9)=m-3. Thus the terminal continuation has exact optimal depth m-3 for every m>=9. The obstruction to c4=6, if any, must now occur in an earlier positive branch or in assembling the compatible prefix order.

## Prefix order reduction

At a=0 there are 9!/2!=181440 row orders before checking intermediate residual bounds. Use a count-vector DAG because the zero prefix uses distinct columns, so the order itself affects no future conditional state other than its multiset; physical labels are retained by the assignment. At each vertex with d zero probes and each possible next row t, test the necessary bounds on both branches. For a support U compatible with the positive branch (t in U) or the all-zero branch, write b for forced holes from the zeros; if b<h, each other live column requires a positive, leaving excess e=6-d+b (one additional positive query cancels one confirmed live). Reject e<0. At most one support with e=0 can coexist: the respective minimal-hole target paths would share an entirely positive suffix. For every optional hole selection of maximal size <=h-1-b among the zero-probed misses, form N as the union of the retained live misses. Every strict superset V of U with V intersect N empty must be hit by an additional negative row in V\\U; otherwise the target with the same H and support V cannot be distinguished. The minimum hitting cost must be <=e. Maximal optional selection suffices by monotonicity. This is a necessary pruning rule, not a sufficient strategy test.

The count DAG has layers [1,8,29,63,88,86,58,26,5,1] and 109008 surviving orders. All retained vertices can reach the terminal vector. At the final ninth query only rows 0,2,4,6,9 can occur. A trial abstract-game search with an added exhausted-support uniqueness prune (FYR guided.cpp, bound(): count low-hole supports having ex=0, reject if >1) did not finish within a 20 s execution cap; log at 2,000,000 calls / 527,793 memo entries, 13.5466 s. No negative conclusion from this attempt.

## Reproduction (Python 3, exact integer arithmetic)

```python
from functools import lru_cache
from itertools import combinations
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
W=[86,101,281,394,460,602,673,788]
def vec(a,u):
    return (6*a+2,5*a+1,4*a+1,a,a+1,0,a+1,2*a+1,3*a+1,3*a+1) if u==394 else (6*a+2,5*a+2,4*a+2,a+1,a,0,a,2*a,3*a+1,3*a+1)
def slack(a,u,v):
    return sum(x for t,x in enumerate(vec(a,u)) if v>>t&1)-(4+11*a-int(u==v))
for u in (394,673):
    # Every slack is affine in a: checking value and slope certifies a>=1.
    assert all(slack(1,u,v)>=0 and slack(2,u,v)>=slack(1,u,v) for v in F)
    T=[v for v in F if slack(1,u,v)==slack(2,u,v)==0]
    assert T==[86,101,281,346,394,412,460,602,673,788]
    assert [(i,j) for i,j in combinations(range(10),2) if vec(1,u)[i] and vec(1,u)[j] and not any(v>>i&1 and v>>j&1 for v in T)]==[(0,1)]
    assert all(any(v>>i&1 for v in T) for i,x in enumerate(vec(1,u)) if x)
    assert all(slack(1,u,v)>=4 and slack(2,u,v)-slack(1,u,v)>=3 for v in F if v&3==3)
    assert (slack(1,u,91),slack(2,u,91))==(4,7)
X=vec(0,394);h=4;c=6
assert min(slack(0,394,v) for v in F)==0
assert slack(0,673,721)<0
T=[v for v in F if slack(0,394,v)==0]
assert all(any(v>>i&1 and v>>j&1 for v in T) for i,j in combinations(range(10),2) if X[i] and X[j])
@lru_cache(None)
def tau(u,N):
    dif=[v^u for v in F if v!=u and v&u==u and not v&N]
    if not dif:return 0
    return min(s.bit_count() for s in range(1024) if all(s&v for v in dif))
@lru_cache(None)
def valid(x,t):
    exhausted=[];d=sum(x)
    for u in F:
        if t>=0 and not(u>>t&1):continue
        b=sum(x[i] for i in range(10) if u>>i&1)
        if b>=h:continue
        e=c-d+b
        if e<0:return False
        if e==0:exhausted.append(u)
        if len(exhausted)>1:return False
        misses=[i for i in range(10) for _ in range(x[i]) if not(u>>i&1)]
        k=min(h-1-b,len(misses))
        for keep in combinations(misses,len(misses)-k):
            N=sum(1<<i for i in set(keep))
            if tau(u,N)>e:return False
    return True
layers=[{(0,)*10}];counts={(0,)*10:1}
for d in range(sum(X)):
    nxt=set()
    for x in layers[-1]:
        for t in range(10):
            if x[t]>=X[t] or not valid(x,t):continue
            y=list(x);y[t]+=1;y=tuple(y)
            if valid(y,-1):
                nxt.add(y);counts[y]=counts.get(y,0)+counts[x]
    layers.append(nxt)
assert list(map(len,layers))==[1,8,29,63,88,86,58,26,5,1]
assert counts[X]==109008
print('DAG',list(map(len,layers)),counts[X])
T=[0,0,1,2,4,6,7,8,9];u0=394
for m in range(9,15):
    states=[]
    for u in F:
        H=sum(1<<j for j,t in enumerate(T) if u>>t&1)
        if H.bit_count()==4:states.append((u,H))
        if H.bit_count()==3:
            assert u==u0
            states.append((u,H))
            states.extend((u,H|1<<j) for j in range(m) if not H>>j&1)
    N=len(states)
    q=sorted(set(sum(1<<i for i,(u,H) in enumerate(states) if u>>t&1 and not H>>j&1) for t in range(10) for j in range(m)))
    @lru_cache(None)
    def win(A,d):
        n=A.bit_count()
        if n<=1:return True
        if d<=0 or n>1<<d:return False
        opts=[]
        for a in set(A&r for r in q):
            b=A^a
            if a and b and max(a.bit_count(),b.bit_count())<=1<<(d-1):
                opts.append((max(a.bit_count(),b.bit_count()),min(a,b),max(a,b)))
        return any(win(a,d-1) and win(b,d-1) for _,a,b in sorted(set(opts)))
    ok=win((1<<N)-1,m-3)
    assert ok and N==m+12
    print(m,N,ok,win.cache_info().misses)
```

Executed evidence: symbolic exact Gaussian elimination determinant -11 (SymPy); affine slack and pair checks executed separately in integer JavaScript (both vectors pass a>=1, only (0,1) compatible, 91 surplus 4 at a=1 with slope 3; at a=0 only 394 passes). Python DAG output layers [1,8,29,63,88,86,58,26,5,1], 109008 orders. Binary search output (m,state count,success,visited): (9,21,True,41),(10,22,True,43),(11,23,True,45),(12,24,True,47),(13,25,True,49),(14,26,True,51). The analytic extension covers every m>=9. The above consolidated code combines the actual checks; no complete decision tree at root has been asserted.

## Continuation and authority

Next: exact abstract positive-branch feasibility at each edge of the reduced 4-hole DAG, working backward from the solved nine-zero continuation, with the FYQ finite-game theorem. A successful path with all positive branches and the terminal branch certified yields c4=6; failure of the complete abstract edge search excludes c4=6, but not by itself every later phase-5 index. Also study how the two affine prefix types at a>=1 change that question. Current c4 in {6,7}, eventual delta in {6,7,8,9,10}; no change to those stable intervals. New exact finite inventory lower and terminal suffix law. Status AUTHOR_PROVED / EXACT_FINITE_INTEGER_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.

Historical registration EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76, original receipt r4-20261124-0240-ec49fyh-own-session-v1 reread SUCCEEDED; recovery metadata shows unclosed/unrevoked, no runs. Current topic read r4-20261124-1630-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source e78c84e2516caff59d206123bdc5e348e9733a6a, observed 2026-11-24T08:30:55.845623Z; directory absence only, not a native owner projection. No shared CLAIM/Result/Review mutation. Own current authenticated writer binding for Activity not established. 
