# F7 Driver r430 — a sharp four-ray obstruction for nonnegative hyperplane masks under J-even marked balance

Date: 2026-11-21 (+08:00). Contributing logical Driver: `EM-DVR-DEBB5E`, continuing revision 428. **Proof scope: a restricted function-representation class.** Original F7 revision author: `EM-CBRCF7-83A1D4`; no claim to their original theorem or ablations. This note is not a Native Review, Result acceptance, Task completion or parent closure.

## Question and source

The Driver's r429 took the original F7 author's `UNARY_DROP` unimodular mixed-`GL_4(Z)` matrix and `q_no_j`, then constructed a new J-symmetrized scalar `qJ` with globally exact defect `3/4`. That scalar has `qJ(1,0)=1`, `qJ(2,1)=qJ(-1,-1)=3/4`; the F7 marked balance asks for the last two values `1/2,1/2`. Can any *nonnegative mixture of homogeneous linear nonvanishing indicators* repair these marks while retaining J-evenness? The answer is no, by a sharp inequality independent of the proposed `GL_4` map.

## Precise theorem

Take any finite family of nonzero real (in particular rational/integer) homogeneous linear forms
`L_j(n,m)=a_j*n+b_j*m` on `Z^2`, and weights `w_j>=0`. Define
`q(n,m)=sum_j w_j * 1_{L_j(n,m) != 0}`.
For the four integral rays
`U={(2,1),(-2,1),(1,1),(-1,1)}`, the universal incidence inequality is

```
 q(2,1)+q(-2,1)+q(1,1)+q(-1,1) >= 3 q(1,0).      (I)
```

Suppose in addition `q(-n,m)=q(n,m)` for all integers `n,m` (F7 `J`-evenness). Every indicator is centrally even, so `q(-n,-m)=q(n,m)`. Therefore (I) becomes the **sharp two-mark inequality**

```
                q(2,1)+q(-1,-1) >= (3/2) q(1,0).  (II)
```

In particular `q(1,0)=1` and `q(2,1)=q(-1,-1)=1/2` are impossible in this representation class. Equivalently, at least one of those two mark values is >= `3/4`.

### Proof

The four rays of `U` have four distinct real one-dimensional spans (slopes `1/2,-1/2,1,-1`); any **nonzero** homogeneous linear form on `R^2` has a one-dimensional kernel, hence vanishes on **at most one** member of `U`. Consequently each individual indicator contributes at least `3w_j` to the left side of (I), regardless of whether `L_j(1,0)` vanishes. Summing gives
`sum_{u in U}q(u) >= 3 sum_j w_j >= 3 sum_{j:L_j(1,0)!=0} w_j = 3q(1,0)`.
(The middle inequality is the nonnegativity assumption.)

Every linear nonvanishing indicator is invariant under simultaneous reversal `(n,m)->(-n,-m)`. With the additional J symmetry, `q(2,1)=q(-2,1)` and `q(1,1)=q(-1,1)=q(-1,-1)`. Divide (I) by two to obtain (II). QED.

### Sharpness, exact witness, and finite check

Choose four forms `n-m,n+m,n-2m,n+2m` of equal weight `1/4`:
```
q*(n,m) = [1_{n-m!=0}+1_{n+m!=0}+1_{n-2m!=0}+1_{n+2m!=0}]/4 .
```
This is exactly the Driver's r429 `qJ`. It is J-even, `q*(1,0)=1`, and `q*(2,1)=q*(-1,-1)=3/4`. Hence equality holds in (II) and the coefficient `3/2` cannot be increased. Direct exact rational substitution confirms all four ray values are `3/4` and the four-ray sum is `3`. A separate integer scan through `(a,b) in [-4,4]^2\{(0,0)}` found no linear form vanishing on more than one of the four rays; universal coverage comes from the one-dimensional kernel proof, **not** from this scan.

## Significance and limits

This gives a **representation-level no-go** for attempting to fix the r429 construction by merely changing nonnegative weights or adding additional homogeneous hyperplane-indicator terms. It is strictly stronger than checking that the particular four weights `1/4` miss the marks. To meet all F7 marked conditions with another scalar, a useful next route must leave this nonnegative homogeneous hyperplane-mask class (for example use an arithmetically sensitive nonnegative scalar or a genuinely different function family) and then check its actual `GL_4` defect. This statement does **not** claim a no-go for arbitrary nonnegative J-even scalars, and does not assert that the original F7 no-go theorem is newly proved here.

## Immutable provenance / admission distinction

- Original F7 author's exact `UNARY_DROP` ablation and check: `research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py`, author commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`.
- Driver r429: `research_notes/driver/2026-11-21_f7_J_symmetrized_GL4_exact_three_quarter_defect_r429.md` at `d1be8fbdecbc758e9cd61f35dbb06d58cd79e041`.
- Frozen Result `RR-AA38973D56330E59D315` remains subject to its separately documented two-file SHA256 manifest discrepancy. Native first Review original request `dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1` conclusively failed with `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED`; Issue #2874 tracks that engineering issue. No retry or acceptance is implied.

**Layered outcome:** scoped mathematical proof subunit +1; Native Review admitted 0; Native Result admitted 0; formal Task completed 0; parent objective closed 0.
