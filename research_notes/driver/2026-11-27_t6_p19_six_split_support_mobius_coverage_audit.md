# T6 p19 six-split independent support Möbius coverage audit

Driver EM-DVR-DEBB5E, 2026-11-27. Scoped nonblind mathematical review; shared control context disclosed. Original author EM-T6SM-B134BD, earlier input contributor EM-T6-BFF294 and original Driver EM-DVR-FBF223 retain their roles.

Exact frozen RR-C428294CF760BD8D99AA blob 62e50de0541fcb25492cffd9354afa8d3a3cda52, SHA256 4d2ebdb11a15bdc1a52a3baca99e8045188bc206414cb3e61b22153171359976. Source 6cdc7b061d6579d6993f2fbc30d396d9a5c29047: research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/PROOF.md blob 2928642008b2ea563954429ff7e5c8131aa4ce65; coverage_p19.json blob f61d29abe8ef850dfc50ea02a46a81dfc8da2d04; verify_coverage.py blob 46024ec08840f4f1ea777eafdec3840badadcd61. Exact review DR-0D8591E64A4073A61E6A and its paper blob 064d8e0969b97038a85bf37e4538a7462b7d16d9 read. Current own flow dvr-20261127-1900-t6-current-review-flow-v1 SUCCEEDED; no reference passes as of that receipt; immutable nonterminal RETURN_TO_OWNER retained.

## Independent count of complete normalized carrier, not affine execution

For p=19 use the original deliberately relaxed carrier of vertical atoms (q,r), q>=1, 1<=r<=18, weight 361q+19r-1, each side sum weights <=2331. Do not apply a new smoothness sieve. One-side order <=6 since 7*361+18>2331. For each q, enumerate all nondecreasing integer atom multisets with exact total order q; record their support S and multiplicity f_q(S) of *different multisets* with that support. Define F_q(T)=sum_{S superset T} f_q(S). For any support S, inclusion-exclusion gives the number of side-q multisets disjoint from S as sum_{T subset S} (-1)^|T| F_q(T). Thus N(a,b)=sum_S f_a(S) sum_{T subset S} (-1)^|T| F_b(T). If a=b divide by two: no support is empty at these positive orders, so every disjoint pair has distinct sides and swapping has no fixed points. This proves complete pair-domain counting independently of the author's pair loops; it does not enumerate or classify affine solutions. The recursion's nondecreasing indices give exactly one encoding of each multiset; all weights and orders are positive, so its pruning is exact.

Actual local Python execution returned the following:
| order | multiset count | distinct supports |
|---|---:|---:|
|3|1482|1329|
|4|8124|6841|
|5|8506|7223|
|6|262|242|

| split | independently counted primitive instances | frozen ledger |
|---|---:|---:|
|3,6|335374|335374|
|4,5|45287075|45287075|
|4,6|1724674|1724674|
|5,5|21405127|21405127|
|5,6|1513179|1513179|
|6,6|20265|20265|
|total|70285694|70285694|

These are pattern-indexed instances, not distinct quotient classes. All six counts match. This strengthens coverage-domain evidence beyond metadata arithmetic, without re-running any old affine census. Original frozen order0..8 inputs, source author affine rejection evidence, and separately reviewed p17 q0 static proof remain their original strengths. The six count checks do not certify that the producer visited each pair or executed its exact rejection; do not promote to independently executed global proof. The original p19 order<=6 side guard means these are all possible splits at orders9..12 up to sign. Common atom cancellation and global sign swap retain the observer equalities and weaken budgets. The independent algorithm is a task-local counting audit, not a novel general tool claim.

## Reproduction (actual executed standard-library Python)

```python
from collections import Counter
from itertools import combinations
p=19; B=2331
atoms=[(q,r,p*p*q+p*r-1) for q in range(1,7) for r in range(1,p) if p*p*q+p*r-1<=B]
def gen(q):
    c=Counter()
    def rec(i,Q,W,S):
        if Q==0:
            c[tuple(sorted(S))]+=1
            return
        for j in range(i,len(atoms)):
            a,r,w=atoms[j]
            if a<=Q and w<=W:
                rec(j,Q-a,W-w,S|{j})
    rec(0,q,B,set())
    return c
C={q:gen(q) for q in range(3,7)}
print([(q,sum(c.values()),len(c)) for q,c in C.items()])
def subsets(S):
    for k in range(len(S)+1):
        for T in combinations(S,k):
            yield T,(-1)**k
F={}
for q,c in C.items():
    f=Counter()
    for S,n in c.items():
        for T,_ in subsets(S):
            f[T]+=n
    F[q]=f
for a,b in [(3,6),(4,5),(4,6),(5,5),(5,6),(6,6)]:
    ordered=sum(n*sum(sign*F[b][T] for T,sign in subsets(S)) for S,n in C[a].items())
    assert a!=b or ordered%2==0
    print((a,b),ordered//(2 if a==b else 1))
```

## Review boundary

The original p19 census remains researcher-execution strength with independently confirmed roster/disjoint cardinalities; the p17 q0 static result retains prior review. Preserve nonterminal RETURN_TO_OWNER and open T6=2332; later p17/q13 science and tool advances are distinct. Do not republish the obsolete q14 task, disturb q13 owner or replay failed references. Auxiliary coefficient/support combinatorics only; no alteration of P000.
