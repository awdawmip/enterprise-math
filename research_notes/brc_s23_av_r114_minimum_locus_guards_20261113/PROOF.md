# R114 — Local minimum-locus guards for exact all-k capacity under symmetric common-source edits

Date: 2026-11-13 (Asia/Shanghai). Status: author-side theorem and exact computational checks; independent review pending. Scientific input remains frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessor R113: `83153fcc892747cd56e5a4766c48da5ede70e04d:research_notes/brc_s23_av_r113_persistent_allk_atom_rank_index_20261113/PROOF.md`. Scope: the finite ranked-source abstraction with the auxiliary rational S23 half-open directed-circle eligibility model. No native Heartbeat-X6 transfer is asserted.

## 1. Setup and source edit

Let `(U, ≻)` be a totally ordered set of distinct complete source identities, and let `M_u(θ)` be a version-independent eligibility predicate. Let finite versions `F,G⊆U` share `C=F∩G` and differ on `Δ=F△G`. For each parameter `θ∈I`, define `d(θ)=max_≻{v∈Δ:M_v(θ)}` if the set is nonempty; otherwise `d(θ)=⊥`.

Define the exact first-difference capacity from R112, `h(θ)=#{v∈C:v≻d(θ), M_v(θ)}` when `d(θ)≠⊥`, and `h(θ)=∞` otherwise. `K=min_{θ∈I}h(θ)`. When `K<∞`, let the nonempty *minimum locus* be `Z={θ∈I:h(θ)=K}`.

A **symmetric common insertion** chooses a complete identity `u∉F∪G` and replaces both versions by `F∪{u},G∪{u}`. A **symmetric common deletion** chooses `u∈F∩G` and replaces both by `F\{u},G\{u}`. Thus `Δ` is unchanged. Let `σ=+1` for insertion and `σ=-1` for deletion. Define the Boolean guard
```
g_u(θ) = 1[d(θ)≠⊥] · 1[u≻d(θ)] · 1[M_u(θ)].
```
When `h(θ)=∞`, its edited value remains `∞`; the finite-case formula below is applied only at parameters with an eligible difference.

## 2. R114.1 — Exact pointwise common-edit identity

**Theorem.** For every `θ` with `h(θ)<∞`, the edited pair has

```
h_new(θ) = h(θ) + σ g_u(θ).
```

At `h(θ)=∞`, `h_new(θ)=∞`. In particular, symmetric common insertions cannot reduce any all-k equivalence capacity, and symmetric deletions cannot increase one.

**Proof.** Since the symmetric difference `Δ` is unchanged, its highest eligible member `d(θ)` is unchanged. Every common source other than `u` retains its version, order, and eligibility. Adding/removing `u` modifies the eligible common prefix above `d(θ)` by exactly one iff `u≻d(θ)` and `M_u(θ)`; otherwise the prefix is untouched. In the absence of any eligible difference the complete eligible lists remain equal before and after. Apply R112's exact first-difference theorem. ∎

## 3. R114.2 — Sharp minimum-locus threshold update

**Theorem.** If `K<∞`, a single symmetric common edit changes the whole-domain capacity by *at most one*, with the exact criterion

```
Insertion: K_new = K+1  iff  g_u(θ)=1 for EVERY θ∈Z;
           K_new = K    otherwise.

Deletion:  K_new = K-1  iff  g_u(θ)=1 for SOME θ∈Z;
           K_new = K    otherwise.
```

If `K=0`, the deletion's first case cannot occur. If `K=∞`, both edits preserve `∞`. These bounds are attained in the S23 model, not only in a generic finite model.

**Proof.** Suppose first `σ=+1`. At each `θ∈Z`, `h_new(θ)∈{K,K+1}`; at `θ∉Z` with finite capacity, integrality gives `h(θ)≥K+1`, so `h_new(θ)≥K+1`. Thus the new global minimum is `K+1` precisely when all old minimizers receive the guard, else `K`. For `σ=-1`, points of `Z` change to `K-1` exactly when guarded, while all other points have `h_new≥K`. Hence the stated dichotomy. A removable common source above an eligible difference implies `h(θ)≥1`, so `K=0` cannot fall below zero. For `K=∞`, no eligible differing identity exists anywhere, unaffected by common-only edits. ∎

**Exact rational witness preservation.** In every finite case an edited global minimizer can be chosen *from the old minimum locus*: for insertion with unchanged capacity choose `θ∈Z` with `g=0`; with raised capacity choose any `θ∈Z`. For deletion with lowered capacity choose `θ∈Z` with `g=1`; with unchanged capacity choose any `θ∈Z`. In rational S23, the necessary guard choices can be made as exact rationals by the construction in §5. By R112, that same witness demonstrates Top-k inequality for **every** `k>K_new`.

## 4. R114.3 — Exact two-stratum minimizer transfer

Write `Z_r={θ∈I:h(θ)=r}`. For `K<∞`, the full edited minimum locus `Z'_min` is:

| Edit and new minimum | Exact edited minimizing locus |
| --- | --- |
| Insert, `K_new=K` | `Z_K ∩ {g=0}` |
| Insert, `K_new=K+1` | `(Z_K∩{g=1}) ∪ (Z_{K+1}∩{g=0})` |
| Delete, `K_new=K-1` | `Z_K ∩ {g=1}` |
| Delete, `K_new=K` | `(Z_K∩{g=0}) ∪ (Z_{K+1}∩{g=1})` |

**Proof.** Substitute `h_new=h±g` and solve the integer equation `h_new=K_new`, using `h≥K` and `g∈{0,1}`. Values `h>K+1` cannot become minimizing after one edit. These identities also specify the exact second stratum needed when a newly selected minimum is materialized for the next historical edit. ∎

**Sharpness and single-witness obstruction.** In S23, take `F={(2,0)}`, `G=∅`, then add common `u=(2,2)`; on every parameter with `M_2(θ)`, the new higher-ranked same-time source is eligible, so `K:0→1`. Reverse the edit for `1→0`. A *single* stored old minimizer's guard is insufficient in general: set `F={(-3,0)}`, `G=∅`, add `u=(-2,2)` in S23 with `(j,x,a,c)=(0,1/4,0,1)`, `I=[0,1]`. Both `θ=7/96` and `θ=19/32` are old minimizers with `h=0`, but `g_u(7/96)=0` and `g_u(19/32)=1`. The global minimum stays zero, despite a guarded old minimizer. The whole minimum locus, or an exact coverage certificate for it, is therefore essential for the threshold test.

## 5. R114.4 — Min-locus-only exact S23 cut refinement

In the frozen auxiliary S23 observation, source identities are `u=(t,b)` and sorted descending lexicographically. Eligibility is membership of `{x+(t-j)θ}` in the positively directed *half-open* fractional circle arc from `{aθ}` to `{cθ}`, with equal endpoints giving an empty arc. Fix rational `x,L,U` and integer `j,a,c,t`, on `I=[L,U]`.

Suppose the *old* certificate has an exact partition into endpoint singleton atoms and open-gap atoms on which `h` and `d` are constant. Old argmin atoms are precisely those with `h=K`. To determine the **new global capacity and one exact witness** after a single symmetric common edit, inspect only those old argmin atoms. On each such open gap insert only the new source time `s=t(u)`'s integer-crossing points for the six affine forms

```
aθ, cθ, (a-c)θ,
x+(s-j)θ, x+(s-j-a)θ, x+(s-j-c)θ.
```

Check each resulting crossing singleton and an exact rational midpoint in each open subgap, along with old argmin endpoint singletons. On each refined subatom, `d` and old `h=K` are constant and the new guard `g_u` is constant. Apply R114.2. One of those examined rational representatives is the new minimizer witness from §3.

**Proof.** All old relevant eligibility predicates are constant on each old atom; hence the highest eligible old difference, if any, and its common prefix count are constant there. The six crossing families contain every possible boundary of the new directed-circle eligibility predicate, including wrap and equal-endpoint events; all between-cut open gaps preserve the fractional ordering. The guard is thus constant on each refined atom. Only old minimum loci can determine whether the global minimum shifts by one (R114.2), while §3 supplies a witness there. The algorithm never needs to enumerate new crossing points outside old minimum atoms for this threshold/witness query. ∎

The result is a *query-level local refinement theorem*. Building a fully updated reusable atom/rank DAG still requires exact representation of edited membership and any new minimizer strata. Count rational cut-generation, sorting, big-integer arithmetic, version memory and eligibility evaluations separately when comparing implementations.

## 6. Executable evidence

Files: `check_r114.py.gz.b64` is gzip-compressed base64 of the complete stdlib Python 3 verifier; decode `base64 -d check_r114.py.gz.b64 | gzip -dc > check_r114.py`, then run `python check_r114.py`. Its original UTF-8 source SHA256 is `fcc99bad2d9352cbacb0c54aaa3cd69f0e7531ef9c4143cffb26261be97a295b`. `verification_r114.json` is the deterministic result, SHA256 `ba62426ed54692a2a9b903f64976acc5d5ea00db3210817b1f8c5c8f70d7863f`.

Exact `fractions.Fraction` arithmetic on `(j,x,a,c)=(0,1/4,0,1)`, `I=[0,1]`; universe 33 identities with times `-5..5`, branches `0..2`. Three random seeds `11401..11403` generate 300 forked common-only edits. Five targeted finite edits test both jump directions, mixed guard and sharp same-time examples; one identical-version case checks `∞`. The checker compares the predicted update against independently recomputed exact full-universe atoms, checks all finite pointwise capacities, Top-k equality through the predicted capacity and disagreement at the next rank, both two-stratum formulas and rational witnesses. Raw result: `R114_PASS`, 305 finite edits, 19,215 full atom comparisons, 11,650 local minimum representatives, 305 verified witnesses, 3 capacity changes, 288 fork reuses, 1 infinite case and a mixed guard case. All assertions passed. This finite run tests implementation, while the theorems derive from the arguments above. No claimed runtime speedup or native X6 realization follows.

## 7. Next unresolved science

Integrate the min-locus query into R113's persistent atom/rank DAG and R111's reversible cut-support index, with a symbolic representation of the two lowest capacity strata. Compare actual total bit complexity and memory against full refinement under adversarial edit histories that repeatedly change which time is the lowest or highest difference. For asymmetric edits changing `Δ`, use R110/R113's exact rank-change logic; the symmetric-common theorem intentionally applies to the narrower and valuable edit class where `Δ` remains fixed.
