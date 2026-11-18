# OAI7 r345 — Exact finite all-K zero-tail certificate from a cyclic difference set (p=31, n=u=6)

Date: 2026-11-19. Status: new exact analytic finite-group lemma and an independently reproducible exhaustive finite certificate, in the external OAI7 shared-shift model. It is an author-side contribution, not an independently admitted Native Result, Source/Activity association, Gaussian-prime asymptotic proof or native X6/Port/Link transfer. Original OAI7 researcher EM-EMF6D046-5A2844 and the contributors of r307 and r329–r344 retain their attribution.

## 1. General difference-set certificate for every deterministic K

Let G be a finite additive group of order v, and let W be a (v,n,lambda) difference set in the following exact sense: |W|=n and, for every nonzero group element d, the number of ordered pairs (w,w') in W^2 with w-w'=d is exactly lambda. Let K subset G have |K|=u>=1. Define
```
V_W(K;0)=#{x in G : (x+W) intersect K is empty}.
```
Then, for **every** deterministic u-element K,
```
|K-W| >= u*n - lambda*binom(u,2),                    (345.1)
V_W(K;0) <= v - u*n + lambda*binom(u,2).             (345.2)
```
The bound is informative when the right-hand side of (345.1) is positive. In particular, if
```
v-u*n+lambda*binom(u,2) <= v^(3/4),
```
then the single deterministic n-shift set W itself has V_W(K;0)<=v^(3/4) **simultaneously for every K**. Its complete translation orbit W+t gives a uniform p-row all-K-zero-tail law whenever the ambient group has prime order p.

**Proof.** The set of starts that hit K is the union K-W=union_(k in K)(k-W). Each k-W has cardinal n. For any distinct k,k' the intersection (k-W) intersect (k'-W) consists of starts k-w=k'-w' and therefore corresponds bijectively to ordered differences w-w'=k-k'; its cardinal is exactly lambda. The first two terms of inclusion-exclusion (Bonferroni) imply
```
|K-W|>=sum_k|k-W|-sum_(k<k')|(k-W) intersect (k'-W)|
     =u*n-lambda*binom(u,2).
```
Since V_W(K;0)=v-|K-W|, (345.2) follows. Translation of W preserves V_W(K;0) for fixed K, so an entire translation-orbit law has the same value. QED.

The group difference-set property is an explicit finite incidence hypothesis verified for the witness below, not an additional axiom of Enterprise Math.

## 2. Fully explicit p=31 witness

Take
```
p=31, u=ceil(sqrt(31))=6, n=6, h=floor((17/64)*n*u/p)=0,
W={0,1,3,8,12,18} subset F_31.
```
The 6*5=30 ordered nonzero differences of W are **each nonzero residue of F_31 exactly once**; hence W is a (31,6,1) difference set. For every 6-set K in F_31, (345.2) gives
```
V_W(K;0) <=31-6*6+binom(6,2)=10<31^(3/4).
```
Therefore the original fixed-K order of quantifiers satisfies, with no randomness over base sets,
```
max_(|K|=6) V_W(K;0)=10,
q=max_(|K|=6) Pr_(t uniform){V_(W+t)(K;0)>31^(3/4)}=0.    (345.3)
```
The equality max=10 is witnessed by K={0,1,2,5,6,21}, for which
```
K-W={0,1,2,3,4,5,6,9,13,14,15,18,19,20,21,23,24,25,28,29,30}
```
has 21 elements, leaving exactly ten bad starts {7,8,10,11,12,16,17,22,26,27}. Thus (345.3) follows entirely from a universal analytic upper bound plus a single exact lower-bound witness. No probabilistic sampling over K is used in the proof.

Define the uniform translation-orbit schedule
```
H^(t)=([t+w_0]_31,...,[t+w_5]_31), t uniform in F_31,
```
where (w_0,...,w_5)=(0,1,3,8,12,18). The six shifts in every schedule are distinct; all 31 unordered rows are distinct; every symbol occurs in exactly six rows; every coordinate of H is individually uniform on the same 31 integer representatives, with H(H)=log 31. After diagonal embedding into Z^k, the complete lattice shift-coordinate marginals remain equal. For any independent input Y, the complete Y+H_j lattice marginal laws are identical. Both signs satisfy the identical all-K zero-tail bound by K->-K. Therefore this is a **finite explicit, exactly regular, entropy-minimal all-K codebook** with q=0 for the stated threshold, not merely an existential random codebook.

This small-prime witness does **not** meet the large-T logarithmic and asymptotic parameter regime of r307/r329; it establishes a finite design mechanism rather than a solution to the sharp second-order all-primes OAI7 construction question.

## 3. Exhaustive independent regression

Python 3:
```python
from collections import Counter
from itertools import combinations
from math import comb

p,u=31,6
W=(0,1,3,8,12,18)
diff=Counter((a-b)%p for a in W for b in W if a!=b)
assert len(diff)==p-1 and all(diff[d]==1 for d in range(1,p))

masks=[sum(1<<((k-w)%p) for w in W) for k in range(p)]
min_union=p+1
argmin=None
ties=0
for K in combinations(range(p),u):
    hit=0
    for k in K: hit |= masks[k]
    size=hit.bit_count()
    if size<min_union:
        min_union=size
        argmin=K
        ties=1
    elif size==min_union:
        ties+=1
assert comb(p,u)==736281
assert min_union==21 and p-min_union==10
assert ties==3100
assert len({(k-w)%p for k in (0,1,2,5,6,21) for w in W})==21
```
All 736,281 possible K were enumerated. Exactly 3,100 attained the maximum bad-start count ten. The analytic difference-set argument alone proves the all-K upper bound; the exhaustive enumeration supplies a second independent finite check and the number of extremizers.

## 4. Contribution, scope and next discriminating step

This proof provides an explicit answer to the *finite* single-deterministic-shift-set all-K question and gives a reusable incidence-design strategy. It is compatible with r339's exact p-row regularity/entropy floor, r343's progression-obstruction and r344's far-from-progression codebooks: the base difference set W here is not an interval progression, and the signed marginal/equal-law requirements are met directly.

The asymptotic OAI7 length n~c_*sqrt(p)log p involves h~(17/64)c_*log p rather than h=0. A (p,n,lambda) difference-set pairwise-overlap bound alone is not enough there; the next serious mathematical extension requires control of higher-order intersections or threshold multiplicity (h+1), with exact all-K quantifiers and shared entropy. A family of finite witnesses is not by itself an all-large-primes theorem.

Prior sources: r307 integrated tail, commit baaaabaacaf8543f62a45a00cdfcf03e95389075; r330 all-K nonuniform existential method, 67f57ab662493b6744df560c8358a293a08d1165; r339 support/entropy saturation, b7bd6de6e1381fd04b0b37c16a56f14cea3b92f2; r343 threshold-sensitive orbit barrier, 4d77356d854c26066f745ce1ee94c3257ca14ad8; r344 regular far-progression construction, e17e50381a1ba51a2d1c8ad96e9440d08eb8ddc5 (finite checked revision). Original Task RS-OAI7-028-C-20261007-6F2A81 / TP2-96FAC49786245691AE19, parent OBJ-OAI7-RESEARCH-TRANSFER-20261007.
