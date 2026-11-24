# EC49FYT — multicover block transport, one-bit excess law and eventual period 11

2026-11-24. Frozen auxiliary Boolean observer BRC16943, identical 50 supports to EC49FYS. State (U,H), U in F nonempty, H subset of m labeled columns, |H|<=h, W(t,j)=1[t in U]1[j not in H]. Exact labeled recovery with unit noiseless adaptive bit probes; m>h>=1. Parent pins actually read: c537688c0ee8151c4a2d3d7bf133a86d22a60414:research_notes/portable_direct/EC49FYS_EXACT_ASYMPTOTIC_HOLE_EXCESS.md (K(k)=ceil(26k/11), lower Q_h(m)>=m+ceil(15h/11), post-positive row depths q_0=6 and q_t=5 for t!=0); ce7abff378aa77006334656fd9396bf9f8666bdf:research_notes/portable_direct/EC49FYQ_FINITE_EXCESS_GAME_THREE_HOLE_LAW.md (c_3=5, Q_3(m)=m+5 for m>=11, exact replay); 8bf5c694cf3ae07cbc70125b691fd6657aecc345:research_notes/portable_direct/EC49FYR_FINITE_COLUMN_REPAIR.md (10-column witness and raw replay, improves onset to 10). The current work is a proof in the frozen observer model, with no new native X6 attribution.

## General block transport theorem

Let K_F(k) be the minimum integer row multicover cost at strength k. Fix an optimal covering multiset of L=K_F(k) rows, order them as a sequence t_1,...,t_L, and choose L distinct physical columns, one per row. Suppose an old h-hole recovery algorithm works on n=m-L>h columns with worst depth n+c. Let q_t be an upper bound for identification of U in a known-live column after a positive read in row t. Define B=max over U in F and i with t_i in U of (number of j<i with t_j outside U)+q_(t_i). Then

Q_(h+k)(m) <= m+max{B,c+L-k}.

Proof: probe the L scheduled rows on distinct columns until first positive or all are zero. If first positive occurs at index i, identify U in that live column in q_(t_i) further queries. Exactly b of its i-1 earlier negative probes hit U, and those b physical columns are known holes. Of the m columns, one live and b holes are known. Test a row in U in each remaining column, thus recovering H with labels. Cost <= i+q_(t_i)+m-1-b = m+(i-1-b)+q_(t_i) <= m+B. If the whole block is zero, for the actual U the b scheduled rows in U identify b distinct holes, b>=k, so the n untouched columns have <=h holes. Apply the old algorithm there, ignoring the block's extra information; this recovers U and H restricted to the complement. Return to the L original columns: every scheduled row in U already certifies a hole; probe a row in U in each of the other L-b columns, keeping their labels. Cost <= L+(n+c)+(L-b)=m+c+L-b<=m+c+L-k. Both branches preserve all joint physical labels; no assumption of independent support/holes or of exactly h holes. If m is too small to reserve n>h this construction is not claimed.

## Specialization to BRC16943

Use FYS multicover vectors for all k, with K(k)=ceil(26k/11), and order all row-0 copies first. If a positive is in row 0, the earlier misses are zero and the excess is <=6. Otherwise q_t<=5 and misses <=L-k. Thus B<=max(6,L-k+5)=L-k+5 since k>=1. With c_h eventually constant for each h and c_h>=5 for h>=3 (FYS lower), we obtain for every h>=3,k>=1:

c_(h+k) <= c_h + ceil(15k/11).

Finite m version: if Q_h(n)<=n+c for every n>=M_h>h and c>=5, then Q_(h+k)(m)<=m+c+ceil(15k/11) whenever m>=M_h+ceil(26k/11). For h=1,2 the general specialization instead gives c_(h+k)<=ceil(15k/11)+max(5,c_h); do not omit the max.

## One-bit uniform excess law and infinite exact class

Take base h=3, c_3=5. For every integer h>=3,

ceil(15h/11) <= c_h <= 5+ceil(15(h-3)/11).

The same upper bound for Q_h(m)-m holds at m>=10+ceil(26(h-3)/11) using the FYR witness; the more conservative threshold 11+ceil(26(h-3)/11) follows solely from FYQ. With x=15h/11, the upper minus lower is 1+ceil(x-1/11)-ceil(x), which is 0 precisely when h=3 mod 11 and 1 otherwise (15 is invertible modulo 11). Consequently c_h=ceil(15h/11)+epsilon_h, epsilon_h in {0,1}, for every h>=3. In particular c_(3+11a)=5+15a for all integers a>=0, and Q_(3+11a)(m)=m+5+15a for m>=10+26a. Examples c4 in {6,7}, c5 in {7,8}, c6 in {9,10}, c11 in {15,16}, c14=20, c25=35, c36=50. This replaces the previous additive interval [0,7] with a one-bit interval; no search at growing h is required for these conclusions.

## Eventual exact period, with a single threshold parameter

Set s_h=1+((15h-1) mod 11) in {1,...,11}, with residue zero represented by 11. For any j>=3 with epsilon_j=0, and any h>j with s_h<=s_j, the transport inequality gives

c_h <= ceil(15j/11)+ceil(15(h-j)/11)=ceil(15h/11).

The ceiling identity holds because the sum of the first two ceilings minus the last equals the indicator of s_h>s_j; write 15j=11a+s_j and 15h=11b+s_h with 1<=s<=11. The FYS lower forces equality. Let s_* be the largest s_j among all exact indices j>=3; it exists since j=3 is exact and there are 11 possible values. Choose one such j_* with s_j_*=s_*. For every h>j_*, epsilon_h=0 iff s_h<=s_*: the forward direction follows from maximality of s_*, the reverse from transport. Thus for all sufficiently large h there exists a SINGLE integer offset delta=11-s_* in [0,10] such that

c_h=ceil((15h+delta)/11).

In particular c_(h+11)=c_h+15 eventually. The order of the eventual correction classes is constrained; arbitrary 11-bit patterns are impossible. This is an existence proof of eventual periodicity and the one-parameter shape, not an effective bound on the onset or determination of delta. A finite exact witness at h divisible by 11 would imply delta=0 and all later indices attain the bare multicover lower. If c5=7, s_5=9 and delta<=2; if c8=11, s_8=10 and delta<=1. These are high-leverage next tests. A failed finite search at one h does not by itself settle any eventual class.

## Exact computational crosscheck, Python 3 (executed)

The multicover and q_t evidence is inherited from FYS and independently recalculated here. The following code checks all frozen supports and all candidate first-positive positions for the 11 base blocks. It checks the finite arithmetic patterns as a crosscheck; the unbounded claims use the analytic argument above.

```python
from functools import lru_cache
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
V=[[0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,1,0],[1,1,1,0,0,0,0,0,1,1],[1,1,0,0,1,1,1,1,1,1],[1,1,1,0,1,1,1,1,2,1],[2,2,1,0,1,1,1,1,2,1],[2,2,2,0,1,1,1,1,3,2],[3,3,2,0,1,1,1,1,3,2],[4,3,2,0,1,0,2,2,3,2],[3,3,2,0,2,2,2,2,4,2],[4,4,2,0,2,2,2,2,4,2],[6,5,4,1,1,0,1,2,3,3]]
R=[sum(1<<i for i,u in enumerate(F) if u>>t&1) for t in range(10)]
@lru_cache(None)
def q(a):
    if a.bit_count()<=1:return 0
    return 1+min(max(q(a&r),q(a^(a&r))) for r in R if a&r and a^(a&r))
Q=[q(r) for r in R]; assert Q==[6]+[5]*9
print('k K minhits max_early_excess positive_pairs')
for k in range(1,12):
    S=[t for t,x in enumerate(V[k]) for _ in range(x)]; n=len(S); assert n==(26*k+10)//11
    mn=min(sum((u>>t)&1 for t in S) for u in F); assert mn>=k
    early=[sum(not(u>>x&1) for x in S[:j])+Q[t] for u in F for j,t in enumerate(S) if u>>t&1]
    assert max(early)<=n-k+5
    print(k,n,mn,max(early),len(early))
for h in range(3,1001):
    lo=(15*h+10)//11;hi=5+(15*(h-3)+10)//11
    assert hi-lo in (0,1) and (hi==lo)==(h%11==3)
for j in range(3,80):
    for h in range(j+1,100):
        sj=(15*j-1)%11+1;sh=(15*h-1)%11+1
        d=(15*j+10)//11+(15*(h-j)+10)//11-(15*h+10)//11
        assert d==(sh>sj)
print('bounds and residue-order identity PASS')
```

Actual output:

```text
k K minhits max_early_excess positive_pairs
1 3 1 7 90
2 5 2 8 141
3 8 3 10 218
4 10 4 11 274
5 12 5 12 337
6 15 6 14 415
7 17 7 15 478
8 19 8 16 547
9 22 9 18 611
10 24 10 19 674
11 26 11 20 749
bounds and residue-order identity PASS
```

No new exhaustive finite-m decision tree was generated. The proof uses exact block branching and the previously published three-hole strategy, not numerical fitting or an inferred physical law. The mathematical status is AUTHOR_PROVED / EXACT_FINITE_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Control and continuation

Prior registered researcher provenance EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76; original registration r4-20261124-0240-ec49fyh-own-session-v1 returned SUCCEEDED. Own metadata recovery confirms session not closed or revoked, no runs; current private writer binding not established by that metadata. Exact topic read r4-20261124-1430-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source 1f8ec5b1ed9525ed973dfabe63f4de2222cae485, observed 2026-11-24T06:30:42.630826Z. This is directory absence only, not a native owner projection. Preserve independent portable research, no new shared CLAIM, Result, Review or foundation modification. Activity association remains pending current own writer binding. Next: target c5=7 vs 8, c8=11 vs 12, c11=15 vs 16; alternatively derive a shifted lower bound sufficient to determine delta or establish an effective stabilization cutoff. Keep finite-column threshold optimization separate.
