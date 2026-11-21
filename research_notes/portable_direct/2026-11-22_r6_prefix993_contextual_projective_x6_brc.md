# PREFIX-993 — Context-stable projective BRC history compression on the native X6 positive-axis skeleton

Date: 2026-11-22 (Asia/Shanghai)
Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.
Research scope: independent portable continuation; no new shared CLAIM/Result/Review, no P000 modification.
Scientific frozen P000 pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`.
Previous exact frontier: PREFIX-992 at `78304654988b69ee8bc76fac272cfca9f98e5805`; current source foundations: WBRC-T30/T31 (recurrent Schur port context), WBRC-T36/T37 (exact positive-rational histogram), X6 native signed Cell torsor and joint observer preservation. Historical researcher `EM-DIRECT-FBEA5D` is attribution, not evidence of current session-key possession.

## Question and typed model

PREFIX-992 compressed six preceding ports into two positive projective weight-row classes for one frozen Schur kernel. We ask which *subsequent* WBRC-T31 permitted positive-rational port-to-port contexts retain those two classes.

Take `J={0,...,m-1}`, `m>=2`, and a strictly positive rational port kernel `W`. A preceding port `h` followed by a named edge with output port `j` receives weight `W[h,j]`. A projective history partition `κ:J→C` and scalars `ρ_h>0` mean
`W[h,j]=ρ_h f[κ(h),j]`.

The native X6 instantiation uses *actual positive primitive* Cell steps `c+z → c+z+e_j`, `j=0,...,5`, in the fixed six-dimensional affine Cell torsor `Z^6`. A step's BRC feedback weight is supplied by the separately typed finite recurrent port module; its history port is **not** a seventh spatial coordinate. A named word `j_1...j_n` has full native displacement `Σ e_j` and positive weight `∏_{r=1}^n W[j_{r-1},j_r]` with `j_0=h`. Declared observation: known path length, native full endpoint, terminal port, and full exact histogram in `H=N[Q_{>0}^×]`. No physical heartbeat period or triadic native force law is asserted.

WBRC-T31 allows a port context to add a nonnegative rational matrix `B` to `W_eff` while leaving the hidden block untouched. This is a BRC feedback update, **not** a zero-displacement native primitive action.

## Theorem 993.1 — exact fixed-normalization context lease

For a fixed factorization `W[h,j]=ρ_h f[κ(h),j]`, the update `W+B` admits the **same** partition `κ` and the **same** positive scalars `ρ`, with updated class templates, iff
`B[h,j]/ρ_h = B[k,j]/ρ_k`
for all `j` and all `h,k` with `κ(h)=κ(k)`. In that case
`f'[c,j]=f[c,j]+B[h,j]/ρ_h` (any `h` in class `c`).

*Proof.* Divide the proposed new factorization by `ρ_h` and subtract the original class template. The difference is exactly `B[h,j]/ρ_h`, so it must be class-constant. Conversely class constancy defines `f'` and gives the factorization. PREFIX-992's path-product telescoping then applies with `f'`: for any `n>=1`,
`K_n^{h,j}(s,t)=[ρ_h/ρ_j](M^{n-1}M_j)[(s,κ(h)),(t,κ(j))]`.
The equality is coefficientwise in the full histogram semiring and terminal-port gluing uses the actual port. QED.

If `ρ` is allowed to change, the broader criterion for retaining a given partition is that all updated row pairs in each class remain proportional (all their 2×2 column minors vanish). This differs from the fixed-normalization iff above. Minimality statements concern this declared projective factorization family, not arbitrary weighted automata.

## Theorem 993.2 — every fixed nontrivial class partition can split within stable WBRC contexts

Let `W∈Q_{>0}^{m×m}`, `m>=2`, and `R=max_h Σ_j W[h,j]<1`. For arbitrarily small positive rational `t`, the permitted diagonal port context `B=tI_m` keeps `W+B` strictly substochastic and makes **all m rows pairwise nonproportional**. Hence the only projective partition invariant under *all* such permitted contexts is the discrete one with m classes.

*Proof.* For distinct h,k originally proportional, their minor on columns h,k is zero at t=0. At t>0 it equals
`(W_hh+t)(W_kk+t)-W_hk W_kh=t(W_hh+W_kk)+t²>0`.
For a pair originally nonproportional, some 2×2 column minor is nonzero at 0 and remains nonzero for sufficiently small t by continuity of a polynomial. There are finitely many pairs; choose one common positive rational t small enough for all and also `t<1-R`. Updated row sums are `≤R+t<1`, an exact positive recurrence stability certificate. QED.

The theorem restricts **fixed, context-independent history identifications**, not the exact WBRC port signature `W_eff`, from which a new context-dependent projective partition can be recomputed.

## Explicit exact six-port Schur/X6 witness

Reuse PREFIX-992's two hidden states:
`A=diag(1/2,1/2)`, `X=(1/100)[[1,2,1,3,2,4],[2,1,3,1,4,2]]`,
`κ=(0,0,1,1,0,1)`, `ρ=(1,2,1,2,3,3)`, and `Y[h,:]=(ρ_h/100)e_{κ(h)}`.
The original direct port block is 0, so
`W_eff=Y(I-A)^(-1)X`, `W[h,j]=ρ_h Xnum[κ(h),j]/5000`.
Its exactly two projective history classes are `{0,1,4}` and `{2,3,5}`.

**Class-preserving context.** Add `B_safe[h,0]=ρ_h/5000` and all other entries zero. The normalized class templates become `f'[c,j]=(Xnum[c,j]+1_{j=0})/5000`; the two-class partition remains exact, and maximum row sum is `21/2500<1`.

**Class-splitting stable context.** Instead add `B_diag=I_6/5000`. Maximum row sum is `1/125<1`, but the updated row partition has **six singleton classes**. All 15 row pairs have a nonzero exact diagonal 2×2 minor (the accompanying JSON certificate enumerates each). Rows 0 and 1 previously shared a template; their updated entries at columns (0,1) are `[[2,2],[2,5]]/5000`, with determinant `6/5000²=3/12500000`. Their exact first-step axis-weight ratio has changed. Reusing the frozen 2-class history partition as-is is therefore an explicit wrong future weight calculation.

Consequently, safe fast projective compression has a **typed context lease**: constrain `B` by the class-homogeneous condition, or recompute the row classes after each permitted feedback update from the complete `W_eff`. Source labels, native primitive axes and terminal port remain separately retained.

## Theorem 993.3 — native X6 relative endpoint repair, not spatial-axis collapse

For positive-only X6 primitive steps, let n be the known number of steps and `z∈N_0^6` the full displacement, `Σ_i z_i=n`. Let `r=can6(z)=z-d·(1,...,1)`, `d=min_i z_i`. Then
`d=(n-Σ_i r_i)/6`, `z=r+d(1,...,1)`.
This is a lossless *fixed-length* endpoint observer. Without n or integral common depth, `can6` conflates native displacement 0 with `D=(1,1,1,1,1,1)`: both give relative r=0 but `L_E(D)^2=6`, and D is reached by six genuine positive primitive steps. Thus projective port compression can reduce port-history templates without erasing full X6 geometry; path order, BRC branch identity and signed history remain separately scoped observations.

*Proof.* Sum the six defining equations `z_i=r_i+d`, and use `Σ z_i=n`. The displayed zero/D witness proves the variable-length counterexample. QED.

## Exact reproducer and scope

The accompanying `PREFIX993_R6_CONTEXTUAL_PROJECTIVE_X6_CHECK.py` and `PREFIX993_R6_EXACT_RESULTS.json` implement exact `Fraction`/integer-`Counter` checks: reconstruct the Schur kernel, both BRC contexts, 15 pairwise nonzero rational minors, row-sum stability, and one-step violation of the old partition. For **all six initial history ports**, compare the full exact endpoint/terminal-port/weight histograms of direct X6 primitive positive-axis paths to projective delayed transfer at every length 0..7 for original W and to the updated singleton transfer after `B_diag`; check safe two-class update at lengths 0..5. Verify depth reconstruction for every reachable endpoint. At n=7, each initial port has exactly `6^7=279936` ordered named positive-axis words. From initial port 0, n=7 exact total mass is `7180818099/78125000000000000000000000` before the context and `9146381609/78125000000000000000000000` after it.

Theorem 993.2 has a general analytic proof; numerical verification is exact and covers this declared six-port example and lengths. This is a native **positive-coordinate X6 skeleton coupled to an explicit type-correct positive-rational BRC port module**, not a proof for full native Link/Port occupancy, signed-amplitude physics, or elapsed heartbeat time. No independent Review has been recorded.

## Next

Characterize the maximal exact context algebra preserving a projective partition when permitted future steps have state-dependent availability; test a native X6 Link/Port relation rather than the pure coordinate skeleton. Give a specific counterexample whenever a proposed state/history quotient discards the declared joint observer. The historical mother question `B_fix,odd(32)∈{19,20}` remains open.
