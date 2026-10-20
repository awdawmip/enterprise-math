# 辅助 BRC：共享静态核两轮辨识无增益半径提升至 5/96（UNREVIEWED）

2026-10-21 · 作者侧解析证明与精确整数有限证书；**未正式 CLAIM、未经独立 Driver 审阅、不属于 P000 原生 Cell 动力学定理**。

## 已固定来源

- GLOBAL_KNOWLEDGE_V1 main: `6b5030f2a8f7e616323a3e67687e4ff38c01e242`
- Enterprise Math main: `86a903f3769a1a6925faadf815a8615f6fe9384e`
- P000 projection's canonical blob SHA1 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` verified against original P000 file metadata.
- Applied current `docs/PORTABLE_RESEARCH_PROTOCOL.md` and positive-branch/Boolean observer typing in `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`.

## Theorem: universal row-TV radius 5/96

Consider six labels N={0,1,2,3,4,5}; threshold=5; weights
`w_star=(1,1,1,1,1,1)`, `w_dagger=(0,1,1,1,2,2)`.
The initial publicly protected label is 5, with certain safe feedback. Each secret action deletes one label v!=p, and repeated deletion is idempotent. Both hypotheses use the SAME strictly positive stationary row kernel K(p,v); secret actions are conditionally independent given the public protection rows. K is allowed to be real-valued.

Let U(p,v)=1/5 for legal v!=p and
`rho=max_p TV(K(p,.), U(p,.))`.
Let `Delta1_K(p)` be the difference of competitor versus target survival probabilities for secret action rows (5,p), and `Delta2_K(p,q)` the corresponding difference for (5,p,q). In every state target survival implies competitor survival; hence each Delta is precisely positive branch mass for the event "competitor safe, target failed".

For the observable first-failure location F1,F2,S^2, distribution TV for a two-word is
`TV_K(p,q)=max(Delta1_K(p),Delta2_K(p,q))`.
Define `V1(K)=max_p Delta1_K(p)` and `V2(K)=max_{p,q}TV_K(p,q)`.

**NEW RESULT.** For every such shared stationary K with rho<=5/96,

```
Delta1_K(5) - Delta2_K(p,q) >= 9191/55296000 > 0
for ALL 36 ordered pairs (p,q).
Consequently V2(K)=V1(K).
```

The preceding certified radius was 1/22. This raises the all-kernel no-gain radius by factor 55/48 (~1.1458). Combined with the previous author-side explicit counterexample family, the unknown true critical radius obeys
`5/96 <= rho_* <= (sqrt(745)-15)/130`.
Neither endpoint is claimed sharp in the full kernel space.

## Analytic proof: convex TV-row representation

Let r=5/96 and u=(1/5,...,1/5) on the five legal actions in a fixed public row. The entire probability simplex TV ball
`B_r={k: sum k_i=1, k_i>=0, sum |k_i-u_i|<=2r}`
is the convex hull of exactly the 20 transfer vertices
`u+r(e_i-e_j)`, where i!=j. Indeed write d=k-u; its positive and negative parts both have mass m<=r. Coupling these two parts expresses d as nonnegative transfers e_i-e_j of total mass m, and any remaining convex weight 1-m/r can be placed at 0, itself the mean of two opposite transfer vertices. All vertices stay positive since r<1/5. This proves equality of the real-valued feasible ball and that finite convex hull; this is NOT an approximation of real kernels by rational kernels.

Take integer scale s=480. The 20 vertex rows have numerators v^(ij) with entries
`v^(ij)_k=96+25(1_{k=i}-1_{k=j})`;
thus their entries are a permutation of (121,71,96,96,96) and sum to 480.

For any secret action path a, let D(a) be its set of distinct deleted labels. The event indicator is EXACTLY
`E(a)=1[ |D(a)|>=2 and sum_{v in D(a)}w_dagger(v)<=2 ]`.
This follows from total target mass 6 and competitor mass 7, both at safety threshold 5.

For vertex indices a,b,c and legal labels indexed relative to each row, define the following INTEGERS:
```
B[a,b] = sum_{x!=5,y!=5} v[a](x)*v[b](y)*E(x,y)
C[p,q][a,b,c] =
  sum_{x!=5,y!=p,z!=q} v[a](x)*v[b](y)*v[c](z)*E(x,y,z).
```
Then B/s^2 is the two-action reference at vertex rows and C/s^3 is the three-action witness at vertex rows.

**Critical repeated-row symmetrization.** Expanding the stationary distribution of each row K_r as a convex combination of vertices introduces independent vertex indices at EACH time occurrence of that SAME fixed row. The vertex indices are not hidden history-dependent kernels: their independent mixture is an exact polynomial expansion of repeated identical K_r factors. Since identical-row index samples have permutation-invariant mixing weights, symmetrizing across these indices is an exact identity. This avoids the invalid assertion that an arbitrary multi-degree stationary probability polynomial has its maximum at one row vertex.

For p,q!=5, use a,b for two copies of row5 and c,d for rows p and q (also independently sampled if p=q). The exact signed comparison `D=Delta2(p,q)-Delta1(5)` is the expectation of
```
T[p,q][a,b,c,d] = C[p,q][a,c,d]+C[p,q][b,c,d]-2*s*B[a,b]
```
divided by `2*s^3`. There are 25 such public words.

For p=5,q!=5, D is the expectation of
`T[5,q][a,b,c]=C[5,q][a,b,c]-s*B[a,b]`
divided by s^3.

For p!=5,q=5, D is the expectation of
`T[p,5][a,b,c]=C[p,5][a,c,b]-s*B[a,b]`
divided by s^3. There are 10 words with exactly one 5.

For p=q=5, D is the expectation of
`T[5,5][a,b,c]=3*C[5,5][a,b,c]-s*(B[a,b]+B[a,c]+B[b,c])`
divided by `3*s^3`. In every case all mixing coefficients are nonnegative and sum to one.

## Exact complete finite certificate

A separate Python-3 standard-library checker computes all E values on the legal finite path domain, contracts the above B/C tensors in Python arbitrary-precision INTEGER arithmetic, and checks the maximum of each T tensor. Its complete search domain is:

- 25 public words with p,q!=5: 25*20^4=4,000,000 integer comparisons.
- 10 public words with exactly one 5: 10*20^3=80,000.
- One word (5,5): 20^3=8,000.
- TOTAL: **4,088,000** symmetrized coefficients, 36/36 words, all strictly negative.

The maximum normalized coefficient among all 36 tensors is attained in the certificate for public word (4,4), vertex indices (16,16,3,3):
```
max T / applicable denominator
 = -36764/221184000
 = -9191/55296000 < 0.
```
Here index16 is vertex move (4->0), and index3 is (0->4) in the sorted row-local action list.

Every feasible real shared stationary kernel inside the radius ball induces convex mixing weights for each row. The exact symmetrized polynomial identities therefore make `D_{p,q}(K)` a convex combination of those all-negative tensor coefficients. This proves the universal inequality with the displayed uniform margin. The coefficient maximum is an upper envelope, **not** a claim that a real stationary kernel attains that upper bound.

Finally `TV_K(p,q)=max(Delta1_K(p),Delta2_K(p,q))<=V1(K)`, while a two-step first-failure observation contains its first-step outcome so `V2>=V1`. Hence V2=V1. At two steps adaptation has only one active continuation outcome after first-step safety, so this also covers adaptive choice within the stated absorbing first-failure observer.

An independent, distinct integer deletion-mask DP additionally checks 4 specified strictly positive rational stationary kernels x 36 words = 144 cases. This is a cross-check; the all-real-kernel theorem relies on the convex proof plus exhaustive signed-tensor certificate, not on sampling.

## Evidence, method and precise limits

Canonical checker specification: Python 3, standard-library integers, 20 transfer vertices per row, 36 words, 4,088,000 comparisons. Deterministic expected outputs: `max numerator=-36764`, denominator `221184000`, `word=[4,4]`, independently checked DP 144. Full author manuscript, exact code, machine-readable per-word certificate and manifest have been supplied as associated research artifacts; remote attachment persistence and canonical task registration require their own actual readback receipts.

This is a positive rational BRC path-probability/Boolean-observer calculation. The method reuses T0_BRC typed support/mass laws (`REUSE_APPLIED`) and adds a finite-domain specialized tensor certificate; it does not create or promote a new universal BRC theorem/tool family. The real-kernel claim follows from finite convex polynomial identities, not from hidden infinite-precision cell state. It does not cover history-dependent kernels, separate hypothesis-specific kernels, full path readout, three-or-more future rounds, independent resampled experiments, or P000 native X6 dynamics.

Status at preparation: native dispatch and task list operations returned `CONTROL_QUOTA`; session registration returned `STATIC_READONLY_SCOPE_DENIED`, operation_sent=false. Therefore active Owner and own native role session could not be verified and no formal CLAIM, Source Result, independent Driver acceptance or Foundation promotion has occurred. This file is author-side **UNREVIEWED** research provenance only.

### Smallest open question
Obtain a better bound by optimizing the repeated-row mixing coefficients jointly rather than taking the maximum of each tensor coefficient, especially at word (4,4), or exhibit a fully exact shared static kernel counterexample below the earlier upper radius 0.094574524. For an upper counterexample check all six single words and 36 two-words on exact rational actions and separate the observed TV from raw survival differences.

Reference prior author note: `research_notes/2026-10-20-brc-shared-static-global-tv-radius-1over22-UNREVIEWED.md`, commit `6762d5572474aad12fff9e090138153bb1a70062`.

**Source pin:** GLOBAL_KNOWLEDGE_V1 main@6b5030f2; Enterprise Math main@86a903f3.
