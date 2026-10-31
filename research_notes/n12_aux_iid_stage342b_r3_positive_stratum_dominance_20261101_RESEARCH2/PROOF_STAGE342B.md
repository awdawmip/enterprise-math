# Stage342-B — complete exclusion of the positive `r3` branch in the tagged Bernoulli/BRC observer

**Date:** 2026-11-01. **Status:** PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a new author proof, not an independent review or Source Result.

## Authority and immutable input

Frozen GLOBAL_KNOWLEDGE_V1 `main@c93e80c23167c473471d7f4d0bf9716f84085a5c` (bootstrap, manual, project TASK_RESEARCH entry, P000 original V4, ACTIVE worldview, BRC and math/code policies); Enterprise Math `main@f8cc8141ca4c92b793ec694de7bfff9ad5e3bba6` (AGENTS, original P000 V5 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, joint observer-preservation, native time, BRC substrate, autonomous and portable protocols). The immediate prior unpublished-admission research frontier is Stage341-B at immutable Git commit `7ec17c620323ab6957da489ea956d42ff76aa42e`; Stage336-B zero-stratum author theorem is `b7937ab921ad44f8bc72bccaaffd293d1be79721`.

The native service status checked in this run was version 0.6.11; `research_authority_granted=false`, `executor_binding_configured=false`, active quota 5/5, `UPSTREAM_CODE_REVIEW_REQUIRED`, so no live owner, CLAIM, execution, formal Result, or independent Driver acceptance is asserted. GitHub storage is not native admission. All mathematics below concerns an **auxiliary 4-real-rate, two-source, three-visit Bernoulli observer**, not P000 X6 dynamics, its three-dimensional slice, native triadic closure, time, or Cell addresses.

## Preserved BRC carrier and model

Retain source identity (`q_1`,`q_2`), all four word-count classes `k=0..3`, multiplicity vector `w=(1,3,3,1)`, all 16 individually source-tagged Bernoulli comparisons, and the two distinct public/audit observers. No total-only quotient is used to erase a tagged source. Let

`B_k(z)=z^k(1-z)^(3-k)`, `m=(61,21,9,9)`,

`r_k(x,y)=(4 B_k(x)+B_k(y))/5 - m_k/160`,

`b(x,y)=(5/32) Σ_{k=0}^3 w_k |r_k(x,y)|`,

`D_3(a,z)=(1/2) Σ_{k=0}^3 w_k |B_k(a)-B_k(z)|`,

`c(x,y)=[63 D_3(1/4,x)+D_3(3/4,x)+9 D_3(1/4,y)+7 D_3(3/4,y)]/256`.

For two groups, `P=b(q_1)+b(q_2)` and `T=33/1024+c(q_1)+c(q_2)`. All derivatives below are for the **source-preserving** scalar observer, not an untagged surrogate.

## Theorem — every point with strictly positive `r3` is strictly dominated

Set `R=[21/100,6/25] × [1/2,2/3]`. For **every real** `(x,y)∈R` with `r_3(x,y)>0`, there exist points `(x',y')∈[0,1]^2` arbitrarily close to `(x,y)` with

`b(x',y') < b(x,y)` **and** `c(x',y') < c(x,y)`.

Indeed the competitor can be chosen by one of three explicit motions: increase `x` if `r0>0`; decrease `y` if `r0<0`; decrease `y` if `r0=0`, entering the `r0>0` chamber. Each motion is open for all sufficiently small positive step sizes, and the last motion is a one-sided boundary argument. Thus **no point with `r3>0` in `R` is single-source Pareto optimal**; no two-source global Pareto optimum can contain such a group because one may hold the other group fixed.

### Lemma 1 — exact high-y strip and common residual signs

For `x≤6/25`, `r3` is strictly increasing in both `x>0` and `y>0`. The exact rational endpoint value is

`r3(6/25,609/1000) = -87471/5000000000 < 0`.

Thus `r3(x,y)≥0` forces `y>609/1000`. On `x∈[21/100,6/25]`, `y∈[609/1000,2/3]`, the derivatives `r1_x=(4/5)(1-x)(1-3x)>0` and `r1_y=(1/5)(1-y)(1-3y)<0` imply

`r1(x,y) ≤ r1(6/25,609/1000) = -8649471/5000000000 < 0`.

Likewise `r2_x=(4/5)x(2-3x)>0`, `r2_y=(1/5)y(2-3y)≥0`, so

`r2(x,y) ≥ r2(21/100,609/1000) = 3120471/5000000000 > 0`.

The word-multiplicity identity `r0+3r1+3r2+r3=0` is exact. It will determine `b` on every sign chamber below.

### Lemma 2 — all sixteen source-tagged comparisons and positive derivative margins

On that entire strip (including the parameter edges), the signs of `B_k(a)-B_k(z)` for `k=0..3` are

- `(x,1/4): -+++`; `(x,3/4): --++`;
- `(y,1/4): ++--`; `(y,3/4): ---+`.

Each four-sign string is proved uniformly by strict same-sign degree-3 Bernstein coefficients over the relevant rational interval. In particular the tagged algebraic cusp `y_dagger=(1+sqrt(13))/8` lies **below** the strip; no point of this proof silently crosses it. Differentiation of all 16 comparisons gives

`c_x=-(1-x)(189-183x)/256 ≤ -68913/160000 < 0`,

`c_y=3y(18-25y)/256 ≥ 1/96 > 0`.

### Lemma 3 — strict improving motions for every r0 sign

The following cases are exhaustive, because Lemma 1 fixes `r1<0,r2>0,r3>0`.

**Case A: `r0>0`.** Only `r1` is negative. Conservation gives `b=-(15/16)r1`, so

`b_x=-(3/4)(1-x)(1-3x) ≤ -399/2500 < 0`.

For all sufficiently small `h>0`, `(x+h,y)` preserves the strict signs and satisfies `b(x+h,y)<b(x,y)` and `c(x+h,y)<c(x,y)`. It lies in the global square; the optional smaller-R constraint is not needed.

**Case B: `r0<0`.** The negative residuals are `r0,r1`, giving `b=-(5/16)(r0+3r1)` and

`b_y=(3/8)y(1-y) ≥ 1/12 > 0`.

For sufficiently small `h>0`, `(x,y-h)` stays in the sign chamber. Both `b` and `c` decrease strictly.

**Case C: `r0=0`.** Move `(x,y)` to `(x,y-h)` for sufficiently small `h>0`. As `r0_y=-(3/5)(1-y)^2<0`, the perturbed point has `r0>0`, while `r3>0,r1<0,r2>0` persist by continuity. Along this *right-side* public branch `b=-(15/16)r1`, and

`b_y=(3/16)(1-y)(3y-1) ≥ 827/16000 > 0`

throughout the strip. Also `c_y≥1/96`. Integrating these **one-sided** derivatives over the small segment, not evaluating a nonexistent single derivative at the `r0=0` cusp, proves strict simultaneous decrease. This completes the continuous-real theorem.

### Exact nonvacuity witness

For `q=(227/1000,617/1000)` and `q'=(227/1000,6169/10000)`, both preserve the strict residual sign string `(r0,r1,r2,r3)=(-,-,+,+)`, with

`b(q)=7206811/1600000000`, `b(q')=35963158191/8000000000000`;

`c(q)=1148355889/32000000000`, `c(q')=367454811471/10240000000000`.

Every fraction is exact and `b(q'),c(q')` are each strictly below their respective values at `q`. The start already satisfies `b(q)<61/10000`, so the newly excluded positive-`r3` stratum **actually intersects** the earlier low-error domain.

## Consequence and exact scope

Stage336-B already gave an **author-level** exact proof excluding the `r3=0` stratum in the same `R`, including `r0=r3=0`. Combining that inherited result with this independent positive-side theorem excludes **all `r3≥0` points in R** from Pareto optimality. If the distinct Stage332-B global enclosure `b≤61/10000 ⇒ (x,y)∈R` is accepted, then **no global low-error single-source Pareto point can have `r3≥0`**. This is a conditional corollary depending on previously unreviewed Stage332 and Stage336 author results; it is not a newly established global full-domain enclosure.

This resolves the *specific sign-reversal concern* introduced by Stage341: the visible rational `r3=0` crossing is genuine but is not by itself a candidate source of a Pareto transition, and its positive side is strictly dominated under the exact tagged cost. It does **not** prove that the Stage341 global optimal-allocation interval extends past `E=29/50000`; that still requires classifying the newly admitted `r3<0` portions, other zero strata and the Stage329 concavity scope.

## Reproduction, dependencies, and open question

`REPRO_STAGE342B.py` performs exact rational/SymPy checks of every displayed formula, all sixteen signs using cubic Bernstein coefficients across the **entire real intervals**, the exact strict witness, and uniform derivative margins. `REPRO_STAGE342B_EXECUTED_STDOUT.txt` is its executed output. An exact finite symbolic certificate supports the universal calculus argument; neither finite sampling nor formal theorem-prover admission is asserted.

**Next Stage343-B:** with `r3≥0` now excluded in the low-error region (conditional on inherited zero/enclosure results), derive a new exact semialgebraic/interval partition of the `r3<0` region admitted as `Q` increases past `109/25000`. Check the remaining `r0=0`, `r1=0` boundary and `(-,+)` chamber for a new constrained `c` minimizer, or find a strict tagged two-source rational competitor at a budget `E>29/50000`. Retain all source labels; re-prove any concavity statement outside Stage329's original verified box. Preserve P000 native-transfer obligations separately.
