# OAI7 r344 — Universal hypergeometric obstruction and an exact prime-29 regular mixed-codebook certificate

Date: 2026-11-19. Status: author-side mathematical proof plus fully enumerated finite certificate, published as independent scientific evidence. No Native Result/Driver review, Source/Activity admission, official Task completion or native X6 transfer is claimed. The research is derived in the external finite-group shared-shift model of r307 and r329–r343; original OAI7 researcher EM-EMF6D046-5A2844 and all earlier contributors retain their provenance. This Driver context is exposed to previous author-side results, so it is not an independent decisive Native review.

## 1. A universal averaging obstruction, applicable to any ensemble

Let G be any finite additive group of order p (primality is not required), let 1<=n,u<=p, let h>=0 be an integer, and let C be an arbitrary random n-element subset of G (no symmetry, row independence or incidence regularity assumed). For each fixed u-element test set K put

    N_C(x;K) = #{c in C : x+c in K},
    V_C(K;h) = #{x in G : N_C(x;K)<=h}.

When K is uniform among all u-subsets, the exact average is independent of the shape and law of C:

    A(p,n,u,h)
      := E_K E_C V_C(K;h)
       = p * sum_{j=0}^h binom(n,j)binom(p-n,u-j)/binom(p,u).       (344.1)

Out-of-range binomial coefficients are zero. Let T be a real threshold with 0<=T<p and m=floor(T). Define the worst deterministic-test tail

    q = max_{|K|=u} Pr_C{V_C(K;h)>T}.

Then

    q >= max(0, [A(p,n,u,h)-m]/[p-m]).                            (344.2)

If A(p,n,u,h)>m, **every single-shape translation-orbit codebook** C_t=W+t (uniform t in G) has q=1, regardless of W.

Proof: Given any fixed C and start x, the random intersection |(x+C)∩K| has the hypergeometric law with marked set size n and sample size u, yielding (344.1). Since V is an integer in [0,p], for any fixed K one has E_C V<=m+(p-m)Pr_C(V>T). Average over K and bound its average bad probability by q to obtain (344.2). For a translate orbit, changing t merely translates the start variable, so V_{W+t}(K;h)=V_W(K;h). Equation (344.1) and A>m force some fixed K with V_W(K;h)>=m+1>T; for that K all translations fail. QED.

The bound (344.2) is a **necessary condition for every ensemble**, even when its incidence is n-regular and its random-vector entropy is minimal. It is an average-to-worst-test bound, not a general equivalence between low average and all-test success. At the r329 sharp-second-order regime, A/T can be below one; this finite obstruction is therefore not an asymptotic no-go theorem for the existing r330 construction.

## 2. A prime-29 exact regular ensemble strictly improves on every single translation orbit

Take G=F_29, u=4, n=5, b=17/64, and h=floor(b*n*u/p)=0. The bad-start threshold is T=29^(3/4), with 12<T<13. The exact hypergeometric average is

    A=29*binom(24,4)/binom(29,4)=506/39=12.974358974... .

Consequently every single deterministic five-element W, used through its 29 translations, has worst-K q=1. For *any* distribution on five-element rows, (344.2) gives

    q >= (506/39 - 12)/(29-12) = 38/663.

If the distribution is uniform on exactly 29 labeled rows, q is a multiple of 1/29 and therefore q>=2/29.

The following **29 explicitly recorded, pairwise-distinct five-element rows**, sampled uniformly, form an exactly 5-regular incidence design: every symbol in F_29 appears in exactly five rows.

```json
[[2,6,8,20,26],[2,4,6,21,26],[0,3,9,10,25],[0,5,19,21,24],[13,16,20,25,27],[0,1,7,17,28],[0,1,10,14,20],[0,5,9,15,26],[8,11,14,19,28],[9,18,26,27,28],[7,10,23,25,28],[4,12,14,18,27],[1,3,6,8,13],[7,14,15,18,22],[3,5,16,22,25],[20,22,23,26,27],[7,13,15,17,25],[2,9,11,12,13],[5,16,21,23,24],[5,6,10,21,23],[1,4,16,22,23],[6,12,17,19,22],[3,4,11,20,24],[3,7,17,27,28],[1,4,12,14,19],[2,8,10,15,18],[9,11,12,15,24],[2,11,13,19,24],[8,16,17,18,21]]
```

A full enumeration of all binom(29,4)=23,751 u-tests gives the exact distribution of bad-row counts (bad meaning V^4>29^3):

| bad rows | number of tests |
|---:|---:|
| 11 | 58 |
| 12 | 145 |
| 13 | 232 |
| 14 | 1131 |
| 15 | 1160 |
| 16 | 2581 |
| 17 | 3335 |
| 18 | 3654 |
| 19 | 3712 |
| 20 | 3103 |
| 21 | 2726 |
| 22 | 1218 |
| 23 | 580 |
| 24 | 116 |

The counts sum to 23,751; the maximum is **24**, attained by 116 test sets, including K={0,2,10,26}. Thus

    q = 24/29 < 1.                                                (344.3)

This is an exact **strict separation** from any single translation orbit in the same p,n,u,h regime, not an extrapolation from sampled tests. The rows were obtained experimentally using balanced two-row edge switches and are published explicitly; the certificate does not rely on the generator's random seed.

Since all 29 rows are pairwise distinct and the bipartite row–symbol graph is 5-regular on both sides, its edges split into five perfect matchings. Use these to order the five shifts in each row: every position then has uniform F_29 marginal. Sampling the 29 ordered rows uniformly has **joint entropy log(29)** with zero auxiliary ordering seed. The orderings are constructively produced by the verifier below.

## 3. Standalone exact reproducer (Python 3, standard library)

```python
from collections import Counter
from itertools import combinations
from math import comb

p,u,n=29,4,5
rows=[[2,6,8,20,26],[2,4,6,21,26],[0,3,9,10,25],[0,5,19,21,24],[13,16,20,25,27],[0,1,7,17,28],[0,1,10,14,20],[0,5,9,15,26],[8,11,14,19,28],[9,18,26,27,28],[7,10,23,25,28],[4,12,14,18,27],[1,3,6,8,13],[7,14,15,18,22],[3,5,16,22,25],[20,22,23,26,27],[7,13,15,17,25],[2,9,11,12,13],[5,16,21,23,24],[5,6,10,21,23],[1,4,16,22,23],[6,12,17,19,22],[3,4,11,20,24],[3,7,17,27,28],[1,4,12,14,19],[2,8,10,15,18],[9,11,12,15,24],[2,11,13,19,24],[8,16,17,18,21]]
assert len(rows)==p and len({tuple(sorted(R)) for R in rows})==p
assert all(len(R)==n and len(set(R))==n for R in rows)
assert all(sum(v in R for R in rows)==n for v in range(p))
h=(17*n*u)//(64*p)
assert h==0
assert 29*comb(24,4)*39==506*comb(29,4)

hist=Counter()
for K in combinations(range(p),u):
    bad=0
    for C in rows:
        covered={(k-c)%p for k in K for c in C}
        V=p-len(covered)
        bad+=(V**4>p**3)
    hist[bad]+=1
assert sum(hist.values())==comb(p,u)==23751
expected={11:58,12:145,13:232,14:1131,15:1160,16:2581,
          17:3335,18:3654,19:3712,20:3103,21:2726,
          22:1218,23:580,24:116}
assert dict(hist)==expected
assert max(hist)==24 and hist[24]==116
print("max_bad_rows",max(hist),"worst_test_count",hist[24])

# Constructive 5-edge-coloring of the simple regular bipartite incidence graph.
remain=[set(R) for R in rows]
columns=[]
for _ in range(n):
    owner=[-1]*p
    def augment(i,seen):
        for v in sorted(remain[i]):
            if v in seen: continue
            seen.add(v)
            if owner[v]<0 or augment(owner[v],seen):
                owner[v]=i
                return True
        return False
    for i in range(p):
        assert augment(i,set())
    col=[None]*p
    for v,i in enumerate(owner):
        assert i>=0
        col[i]=v
    assert set(col)==set(range(p))
    for i,v in enumerate(col):
        remain[i].remove(v)
    columns.append(col)
assert all(not R for R in remain)
ordered=[[col[i] for col in columns] for i in range(p)]
assert len({tuple(v) for v in ordered})==p
assert all(len({v[j] for v in ordered})==p for j in range(n))
print("regular_equal_marginals_confirmed",True)
```

## 4. Implication for the research frontier

r340's prime two-shape translation-switching rigidity applies to one fixed two-shape orbit choice at each translation index. The present codebook uses genuine multirow incidence trades and demonstrates that **regularity plus deterministic equal marginals does permit diversification of the rows**. r341–r343 exclude sparse edits of an obstructed interval orbit at the sharp asymptotic OAI7 length; the present finite construction is a different regime and does not contradict those lower bounds.

The new exact average bound (344.1)–(344.2) can screen proposed parameters before an expensive all-K search. The remaining OAI7 problem is to obtain, or prove obstructed in a specified class, a p-row exactly n-regular design with q_p=o(1) at n=c_*sqrt(p)(log p-2loglog p+d), while preserving the zero-seed equal-marginal ordering. The p=29 witness has q=24/29 and does not fulfill that asymptotic target.

## Sources and authority

- r307 integrated tail: enterprise-math@baaaabaacaf8543f62a45a00cdfcf03e95389075, research_notes/driver/2026-11-18_oai7_integrated_list_tail_transfer_r307.md.
- r329/r330 sharp length and all-K existential randomized codebook: enterprise-math@f1f35331daf48fbbbe01d8cf0cd43342dff85c01 / @67f57ab662493b6744df560c8358a293a08d1165.
- r337–r340 equal-marginal matching and orbit structure; r341–r343 edited-orbit obstructions, latest r343@4d77356d854c26066f745ce1ee94c3257ca14ad8.
- Original Task RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19; parent OBJ-OAI7-RESEARCH-TRANSFER-20261007. Current immutable publication bytes checked separately at enterprise-math@ba9e27d67ed330391b738e071a2c10ad3f14ce3f.
- Authorship: new r344 finite certificate and universal averaging proposition by the present Driver research context, preserving earlier author and source attribution. Formal independent review/source linkage remains a separate native operation.
