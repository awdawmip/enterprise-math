# R5 — a second source-sensitive terminal split cannot repair the symmetric-upstream two-key hull

**Date**: 2026-11-01, Asia/Shanghai. **Classification**: `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. **Mother question**: find a strictly positive finite two-law time/likelihood-ratio stopping model whose LR observation image in `(eP,eQ,TP,TQ)` has affine dimension four, whose FULL and LR **convex hulls** coincide, but whose actual real behavioral images differ. This paper **excludes the next natural two-parameter extension**; it does not solve the mother question.

## Frozen sources and exact scope

- GLOBAL_KNOWLEDGE_V1 `main@cf04d177ada891258543cb6263de1ea72c1d5f00`, canonical `00_BOOTSTRAP.md` and `OPERATING_MANUAL.md` read at that snapshot; project router, P000 original/projection, ACTIVE HEARTBEAT_WORLD and residual-fidelity position, joint-relation observer constraint, TASK researcher entry, and portable research protocol were examined.
- Enterprise Math canonical `main@15009ebc884193a7713c4e81e2ad9f007068bd74`. Prior **author-side portable** R5 mathematical result: [`RESEARCH_UPSTREAM.md`](https://github.com/awdawmip/enterprise-math/blob/3fa70365642a28dc3ea2f4f1a968a2cfb8f0eb9a/research_notes/brc_r5_time_marginal_answer_invariant_20261101_t1440/RESEARCH_UPSTREAM.md) and [`NEXT_TASK.md`](https://github.com/awdawmip/enterprise-math/blob/3fa70365642a28dc3ea2f4f1a968a2cfb8f0eb9a/research_notes/brc_r5_time_marginal_answer_invariant_20261101_t1440/NEXT_TASK.md), explicitly recommending a second source-sensitive tail split or a new coupled key.
- This is an **auxiliary classical finite probability model**. It keeps all origin, path, terminal-answer and two-measure labels until the declared four-observer projection. It is not a native HEARTBEAT_WORLD X6 calculation, a native BRC arithmetic run, physical time calibration, independent scientific review, or a Foundation theorem. P000 and the protected ACTIVE worldview remain untouched. Its exact rational computations are about this auxiliary model only.

## Definition — genuine two-key law and two independently source-sensitive tails

Fix `t=1/4`, `alpha1=2/5`, `delta1=1/2`. Introduce **arbitrary real** `a=alpha2`, `d=delta2` with `0<a,d<1`. Each tuple below gives the origin/branch, time, decision result, and conditional probability under the respective law. Initially origin masses are:

| Origin | P mass | Q mass |
|---|---:|---:|
| A1 | 1/8 | 1/8 |
| A2 | 1/8 | 1/8 |
| B | 1/4 | 1/8 |
| C | 1/2 | 5/8 |

At time 1, A1 and A2 reach one common **true `(time, P/Q likelihood ratio)=(1,1)`** decision key `I`, with independent FULL stop probabilities `p1,p2`. Stopping answers **P**. Continuing draws a strictly positive nature branch: under P/Q, low probabilities `(2t,t)=(1/2,1/4)` and high `(1-2t,1-t)=(1/2,3/4)`. The high branch stops at time 2, answering **Q**. The low branch reaches the second common real decision key `J=(2,2)` along with B. At J, FULL has stop probabilities `(q1,q2,qB)` and stopping answers **P**. All continuing J paths stop at time 3. The B continuation answers P.

A1's continuing tail produces an answer-P branch with conditional P probability `alpha1=2/5` and conditional Q probability `1-delta1=1/2`, plus an answer-Q branch with probabilities `(1-alpha1,delta1)=(3/5,1/2)`. A2's continuing tail is **independently modified**: answer-P branch has conditional P/Q probabilities `(a,1-d)` and answer-Q branch `(1-a,d)`. Origin C independently stops at time 1 answering Q with probability `r`, otherwise at time 3 answering P. All decisions use identical randomized rules under the two laws; FULL can condition on origin, while LR must tie `p1=p2=p` and `q1=q2=qB=q`. LR retains free `r`. Each decision key is visited at most once along any path, making LR's four-observer map multi-affine.

The two-laws' terminal likelihood ratios are computed from **P and Q branch mass**, rather than assigned by labels. At time 1, I has ratio 1/P and C has 4/5/Q; at time 2, J has ratio 2/P and A-high has ratio 2/3/Q. At time 3, A1 gives 8/5/P and 12/5/Q, B gives 2/P, C gives 4/5/P; A2 gives `2a/(1-d)`/P and `2(1-a)/d`/Q. We restrict to the **admissible locus** where no two terminal branches with identical `(time,ratio)` require conflicting answers. This is a genuine nonempty open subset of `(0,1)^2`: `a=1/3, d=1/4` yields A2's ratios 8/9/P and 16/3/Q, with no conflict. On this locus all exogenous branch probabilities under P and Q are strictly positive. The formulas below also have a continuous algebraic extension over the square `[0,1]^2`; that extension is **not** used to assert every boundary or answer-collision instance is a lawful model.

Define `eP=Pr_P(answer P)`, `eQ=Pr_Q(answer Q)`, `TP=E_P(stop time)`, `TQ=E_Q(stop time)`. Probabilities sum to one under each law. Source and branch labels are retained in `VERIFY.py::stream` and projected only for these explicitly named observers.

## Theorem — all-real two-parameter exclusion, with a uniform separation bound

For **every admissible real** `(a,d)` in the above model:

1. The LR observation image has full affine rank **4** and is nonconvex.
2. The convex hull of the FULL four-observer image strictly contains the LR four-observer convex hull.
3. An explicit FULL witness `W` has L-infinity distance at least `27/6832` from the entire LR convex hull, **uniformly in the whole admissible parameter locus**. For `(a,d)=(1/3,1/4)`, a sharper lower bound is `1241/190480`.

Thus varying the second source's terminal P/Q answer split alone, with the current positive upstream probabilities and stop-time/key skeleton held fixed, never repairs all-signed FULL/LR convex-hull equality. In particular, a four-dimensional LR observer image and nonlinear actual-observer obstruction do not suffice for the original mother target.

### Proof 1 — exact LR multiaffine observer chart

Write `O_LR(p,q,r)=O0+p B+q C+pq D+r E` with vectors ordered `(eP,eQ,TP,TQ)`. Exact probability-flow accounting gives

```
O0 = ( 31/40 + a/16,          13/64 + d/32,        23/8,  45/16 )
 B = (  9/40 - a/16,         -13/64 - d/32,        -3/8,  -5/16 )
 C = (  1/10 - a/16,          -1/64 - d/32,        -3/8,  -3/16 )
 D = ( -1/10 + a/16,           1/64 + d/32,         1/8,   1/16 )
 E = ( -1/2,                   5/8,                 -1,    -5/4  )
```

This identity follows by expanding the source/path probabilities in the preceding definition. Direct exact determinant expansion produces

`det[B C D E] = (199 - 140 a - 50 d)/40960 >= 9/40960 > 0`

for `0<=a,d<=1`. The eight deterministic LR points are `O_LR(p,q,r)` with `p,q,r` binary. Every actual real LR point has the **unique** invertible-affine chart coefficients `(u,v,s,w)=(p,q,pq,r)`. Hence the image has rank four. It is nonconvex because the midpoint of the points with `(p,q,r)=(0,0,0)` and `(1,1,0)` has chart `(1/2,1/2,1/2,0)` while every real LR point with `u=v=1/2` has `s=1/4`.

### Proof 2 — the exact global halfspace and a source-specific FULL witness

Define `N=199-140a-50d>0` and the row vector

```
L(a,d) = 1/(140a+50d-199) *
         [ 80(2d+43),  -32(10a-91),  -20(40a+14d-63),  32(15a+5d-29) ].
```

An elementary multiplication using the four columns above gives

`L·B=0`, `L·C=0`, `L·D=1`, `L·E=0`.

Therefore the affine functional `s(O)=L·(O-O0)` satisfies `s(O_LR(p,q,r))=pq>=0` for **all real** `p,q,r∈[0,1]`. By linearity, every point of the **complete LR convex hull** also satisfies `s>=0`; no support-direction sampling or finite-hull enumeration is involved in this inequality.

Take the lawful deterministic FULL strategy

`(p1,p2,q1,q2,qB,r)=(0,0,1,0,0,1)`.

It treats the two origins separately at J while respecting every individual physical stop branch. Exact source-flow accounting gives

`W=( (5+a)/16, 13/16+d/32, 29/16, 49/32 )`.

Substituting into the affine row yields the **exact all-real identity**

` s(W) = -(160a+74d+135)/(4(199-140a-50d)) < 0`.

Consequently `W∉conv(O_LR)` and the FULL/LR convex hulls differ for **every** lawful `(a,d)` in this two-parameter family. The scalar `-s` is an explicit real signed support direction; its gap is at least `-s(W)`. This is a direct counterexample to the hope that adding only A2's tail signal would close all six prior convex-hull facets.

### Proof 3 — uniform L-infinity separation

Because `N>0`, `40a+14d-63<0` and `15a+5d-29<0` on the closed unit square, the L1 norm of the normal is exactly

`||L||_1=(8540-1600a-280d)/(199-140a-50d)`.

For any `Z∈conv(O_LR)`, `L·(Z-O0)>=0`. Hölder's inequality implies

```
||W-Z||_inf >= -s(W)/||L||_1
               = (160a+74d+135)/[4(8540-1600a-280d)]
               >= 135/(4*8540) = 27/6832 > 0.
```

The last bound covers the whole closed **algebraic** parameter square and therefore every admissible positive model. At `(a,d)=(1/3,1/4)`, exact substitution gives `det=839/245760`, `W=(1/3,105/128,29/16,49/32)`, `s(W)=-1241/3356` and `||W-Z||_inf>=1241/190480` for all LR convex combinations. These are exact lower bounds, not claims of equality with the true minimum distances. QED.

## Computational evidence and validation limits

`VERIFY.py` is a standalone Python standard-library `fractions.Fraction` verifier. It computes terminal **P and Q masses separately by labeled path**, checks two-law normalization, derives the LR chart, checks the explicit 4×4 determinant and inverse-row identities, checks 27 rational LR behavior triples for each of 25 pairs in an algebraic grid, and checks the FULL witness, signed separation and norm bound for those exact pairs. The rational strictly positive point `(1/3,1/4)` independently checks the same-time likelihood-ratio answer consistency. `EXACT_OUTPUT.txt` contains the actually executed stdout. The universal statement is justified by **the displayed symbolic determinant and inverse-row polynomial/rational identities**, not by interpolation from 25 parameter choices.

## Relation to active project constraints and open problem

The source/branch flow ledger preserves provenance and signed observer relation before the declared four-dimensional readout. P000/native X6 claims and native heartbeat BRC execution require their own embedding and observer-preservation certificate; nothing in this auxiliary lemma supplies one. The result narrows the finite LR candidate search without changing P000 or assigning theorem acceptance. The next useful perturbation must change the **stop-time/decision-key coupling or upstream information structure**, not merely the now-excluded A2 terminal split. The mother target remains OPEN, and any future candidate must first pass complete all-signed convex-hull equality.

**Current authority boundary:** Gateway v0.6.11 read reported `research_authority_granted=false`, `executor_binding_configured=false`; the bounded current owner query returned `CONTROL_QUOTA`. Prior source reports a distinct own session-start attempt denied `STATIC_READONLY_SCOPE_DENIED`; it was not replayed for this same refusal scope. This paper is author-side, not a registered Source CLAIM, frozen Result, independent Driver review or admission.
