# EC49FQO — Four additional exact BRC prior sections and an eleven-price global error certificate

**Date:** 2026-11-16. **Scientific source:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Provenance:** exact seven-section EC49FQN (PR #2555), EC49FQM, EC49FQL, EC49FQI.

## Statement and native observational scope

The frozen class 16943 contains 310 original configurations grouped into 141 complete named-root observational profiles. There are exactly 228 physical observations: 144 terminal queries (indices 0–143) and 84 named-root queries (144–227). These have 209 distinct response partitions, where two queries are deduplicated only when their full response partition and price type coincide. The finite adaptive decision tree must correctly identify all 141 complete profiles. Every response fiber and multiplicity is retained.

Let the terminal-query price be `t>0`, root-query price be `r>0`, and `x=r/t`. Let the profile multiplicities satisfy `m_i>=1` and `sum m_i=310`. Define a continuum of priors on the **unchanged** profile population:

`p_lambda(i)=(1-lambda)/141+lambda*m_i/310`, with `0<=lambda<=1`.

Let `v(lambda,x)` be the unrestricted optimal expected identification cost divided by `t`. The following functions are exact costs of three previously constructed, completely replayed native decision trees:

```
A(lambda,x) = (1-lambda)*(6*x+290)/141 + lambda*(6*x+751)/310
B(lambda,x) = (1-lambda)*(5*x+293)/141 + lambda*(5*x+704)/310
C(lambda,x) = (1-lambda)*(5*x+295)/141 + lambda*(5*x+685)/310
F(lambda,x) = min(A,B,C)
beta       = 620/3299
gamma(x)   = 310*(3-x)/(7557-169*x)
```

## Theorem 1 — Four previously unclassified full-prior price sections

For **each** `x in {7/6, 7/4, 9/4, 17/6}` and **all real** `lambda in [0,1]`,

`v(lambda,x)=F(lambda,x)`.

All optimal first **physical observation indices** are classified as follows:

| Exact prior region | All and only optimal first indices |
|---|---|
| `0<=lambda<gamma(x)` | `{32,34}` |
| `lambda=gamma(x)` | `{32,34,140,142}` |
| `gamma(x)<lambda<beta` | `{140,142}` |
| `lambda=beta` | `{16,23,140,142}` |
| `beta<lambda<=1` | `{16,23}` |

The exact first transitions are `gamma(7/6)=3410/44159`, `gamma(7/4)=310/5809`, `gamma(9/4)=310/9569`, and `gamma(17/6)=310/42469`.

**Complete proof.** For each fixed price perform unrestricted exact integer Bellman optimization at four prior anchors `0, gamma(x), beta, 1`, using the full native responses, every admissible splitting observation in each recursive fiber, and the full 141-profile state space. At all 16 anchors, the exact optimum is `min(A,B,C)` and all 228 physical initial actions are exhaustively classified with optimal equality sets matching the table at those endpoints. The 16 complete machine certificates in the attached evidence archive record all first-action costs, explicit decision trees, and original frozen data fingerprints. A second Bellman implementation independently regenerates and checks these values and replays all stored optimal first-index witnesses.

For fixed `x`, any particular finite adaptive tree has an expectation affine in `lambda`. If a fixed A/B/C witness is optimal at both ends of a closed subinterval, the cost difference of any competing tree minus this witness is affine and nonnegative at both ends, hence is nonnegative everywhere inside. By the four certificates and the known fixed native witness trees, A is optimal on `[0,gamma(x)]`, B on `[gamma(x),beta]`, and C on `[beta,1]`. An action optimal in an **open** interval must appear in both endpoint optimal-first sets (otherwise the affine cost gap cannot vanish in its interior). The stored native witness trees show attainability of each index in those intersections. At boundaries the exact stored first-action equality sets apply. Finally,

```
A-B = (1-lambda)*(x-3)/141 + lambda*(x+47)/310
C-B = 2*(1-lambda)/141 - 19*lambda/310
```

give the stated strict phases and exact transitions. This extends the finite certificates to **every real prior**.

## Theorem 2 — Uniform error bound over the entire two-parameter half-strip

Combine the four new sections with seven already verified full-prior price sections to obtain

`G11={1,7/6,4/3,3/2,7/4,2,9/4,5/2,8/3,17/6,3}`.

At **each** price `x in G11`, the formula `v(lambda,x)=F(lambda,x)` holds for **every real** `lambda in [0,1]`. For **all** real `lambda in [0,1]` and `x>=1`, the explicit A/B/C policy on `1<=x<=3`, together with the previously proven high-price optimal policy for `x>=3`, satisfies

`0 <= C_policy(lambda,r,t)-V(lambda;r,t) <= (25/57076)*t < 0.000438013*t.`

This strictly improves the previous guaranteed `25*t/28538` by a factor of **two**. The upper bound is a certified worst-case guarantee, not a claim that a counterexample to exact optimality exists.

**Complete continuum proof.** Fix `lambda`. The exact optimal value is the pointwise infimum over feasible decision-tree costs, each affine in `x`; hence `v(lambda,x)` is concave in `x`. For each successive grid pair `a<b`, the chord

`L_ab(lambda,x)=((b-x)*F(lambda,a)+(x-a)*F(lambda,b))/(b-a)`

is a valid **lower bound** on `v` for all `x in [a,b]`. The A/B/C witnesses give the upper bound `v<=F`. On the pre-proven right-prior strip `lambda>=beta`, exact equality `v=C` holds for `1<=x<=3`. For `lambda<=beta`, `F=min(A,B)`; their crossing is

`s(lambda)=(930-7557*lambda)/(310-169*lambda)`,

and the slope difference is the positive, decreasing function

`d(lambda)=(1-lambda)/141+lambda/310`.

Where `s` lies outside `[a,b]`, F is affine and the chord closes exactly. Otherwise the *maximum* chord discrepancy in that interval is `d(lambda)*(s-a)*(b-s)/(b-a)`, bounded by `d(lambda)*(b-a)/4`. The condition `a<=s<=b` implies `lambda>=gamma(b)` and thus `d(lambda)<=d(gamma(b))`. Therefore the entire interval has gap no larger than the exact rational `d(gamma(b))*(b-a)/4`. The ten such bounds are:

| Price interval | Certified rational upper bound |
|---|---|
| `[1,7/6]` | `25/88318` |
| `[7/6,4/3]` | `5/17596` |
| `[4/3,3/2]` | `25/87642` |
| `[3/2,7/4]` | `5/11618` |
| `[7/4,2]` | `25/57752` |
| `[2,9/4]` | `25/57414` |
| `[9/4,5/2]` | **`25/57076`** |
| `[5/2,8/3]` | `25/85276` |
| `[8/3,17/6]` | `25/84938` |
| `[17/6,3]` | `1/3384` |

The maximum is `25/57076`. For `x>=3`, earlier EC49FQM exact high-price theorem identifies the optimum for **every** prior, so the gap is zero there. This proves the stated universal half-strip bound.

## Source, computations, and unresolved question

Frozen original data: `frozen_original_master.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv` SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Complete archive: `EC49FQO_BRC_ELEVEN_PRICE_SLICES_HALVED_GAP_EVIDENCE_20261116.tar.xz`, SHA256 `73a534b0d137c0c1146df0f17f47d5cedb0d1e00e360cb83d902abf17181e1f7`; 41 complete rational Bellman certificates (25 inherited, 16 new), two algorithms, original frozen input data, proof, run logs, SHA256 manifest and full native decision-tree replays. The GitHub publication includes the proof, the independent verifier, and a complete hash-index of the new certificates; the attached archive contains the full 41 machine certificates.

**What remains open:** whether `v(lambda,x)=F(lambda,x)` throughout the continuous interior `0<=lambda<=1, 1<x<3`, notably between proved price sections. Any strict improvement must produce a *native complete* correct decision tree and a rational input whose exact cost beats F, with preserved profile and response-fiber semantics. A positive theorem needs a parameterized global Bellman lower bound. The remaining possible improvement is bounded by `25/57076` terminal-price units.

**Control/provenance:** Independent portable research on a pinned frozen scientific model; `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`. Historical researcher and Activity provenance are not current execution CLAIM. At 2026-11-16 04:29:59 UTC, native read-only lookup of `RS-EC49AS` returned `NO_CANONICAL_PUBLICATION_DIRECTORY` on pinned control Source `f947bb5df96669b8c6f080287e212654890f9438`. No Task/CLAIM/Result/Review is asserted by this scientific note.
