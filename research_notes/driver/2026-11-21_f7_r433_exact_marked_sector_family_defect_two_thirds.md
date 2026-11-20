# F7 Driver r433 — exact marked J-even sector construction with sharp defect 2/3

Date: 2026-11-21 (+08:00). Scientific contributor: Driver logical line `EM-DVR-DEBB5E`. Original F7 author `EM-CBRCF7-83A1D4` is credited for the mixed `UNARY_DROP` matrix and exact J-dropped ablation. Scope: **fixed-matrix quantitative approximate conservation on the free scalar `Z^2`**, not a new exact F7 solution or a Native Review.

## 1. Improvement and precise statement

Retain the original author's involutory, unimodular mixed matrix
```text
A = [[ 2,-2,-1, 2],
     [ 1,-1,-1, 2],
     [-1, 2, 2,-2],
     [-1, 2, 1,-1]],    det A = -1, A^2 = I.
```
The first elementary old coordinate has two nonzero output old coordinates `(2,-1)` (A0). Define for `1/2 <= alpha <= 1`, with `a=|n|`, `b=|m|`:
```text
q_alpha(n,m) =
    0       if (a,b)=(0,0);
    1/2     if a<=b OR a=2b;
    alpha   if b<a<2b;
    1       if a>2b.
```
These cases are disjoint after the origin exception. Every `q_alpha` is nonnegative, J-even under `(n,m)->(-n,m)`, centrally even, and `q_alpha(n,m)>=1/2` on every nonzero lattice pair. In addition,
```text
q_alpha(t,0)=1 (all t!=0);
q_alpha(2,1)=q_alpha(-1,-1)=1/2.
```
For `z=(n,m,p,l)`, set `D_alpha(z)=q_alpha((Az)_{1:2})+q_alpha((Az)_{3:4})-q_alpha(n,m)-q_alpha(p,l)`.

**Theorem (all integer inputs; sharp for the entire one-parameter family).**
```text
sup_{z in Z^4} |D_alpha(z)| = max{alpha, 2(1-alpha)}
min_{alpha in [1/2,1]} sup |D_alpha| = 2/3,
with unique minimizing alpha = 2/3.
```
This improves the prior explicit exact-marked r432 construction's full-input bound `1` to `2/3`, while preserving J-evenness, full marked values, and even the stronger all-nonzero positive floor `1/2`.

## 2. Lower-bound witnesses (symbolic for all alpha)

- `z=(-3,-2,3,2)` maps to `Az=(-1,0,1,0)`. Inputs each contribute `alpha`; outputs each contribute `1`. Thus `D_alpha(z)=2-2alpha`.
- `z=(18,-9,20,-10)` maps to `Az=(14,-13,24,-6)`. Inputs each contribute `1/2`; output pairs contribute `alpha` and `1`. Thus `D_alpha(z)=alpha`.

These two exact integer examples establish the claimed lower envelope.

## 3. Universal upper bound: finite exact signed-arrangement certificate

The four forms on one slot are `n-m,n+m,n-2m,n+2m`. Apply them to the two input and two output slots to obtain sixteen integral linear forms `F_0,...,F_15` in `z in Z^4`. Their signs, including zero, determine each `q_alpha` exactly:
- all four signs zero: `q=0`;
- `sgn(n-m)sgn(n+m)<=0`: `q=1/2`;
- otherwise, `sgn(n-2m)sgn(n+2m)=0`: `q=1/2`;
- otherwise, that product is negative: `q=alpha`;
- otherwise: `q=1`.

For this integral rank-four central arrangement, enumerate rank-three intersections of triples of the 16 integer rows. Each nonzero integer cofactor null vector gives two oriented **cocircuit** sign vectors; the distinct cocircuits number **84**. Their sign compositions `(x∘y)_i=x_i if x_i!=0 else y_i`, together with the all-zero vector, close to exactly **1,225** sign covectors.

**Why this covers every integer input, not merely a bounded box:** every generated composition is realized by a sufficiently small positive rational perturbation of representing vectors and then integer scaling. Conversely, for any nonzero input sign covector, the corresponding closed pointed rational polyhedral sign cone has an extreme-ray decomposition. Because the 16 forms span the four-dimensional dual space, each extreme ray is determined by three independent active row equations and therefore belongs to the enumerated cocircuits. Composing their conformal signs recovers the input covector. The zero vector accounts for the origin. Thus the finite list is exactly complete for all real/rational/integer `z`.

The complete exact integer enumeration gives the following **15**, and only these, affine defect expressions (with the `+/-` signs separately realized):
```text
0, ±1/2, ±alpha, ±(alpha-1/2), ±(alpha-1),
±(2alpha-1), ±(2alpha-3/2), ±(2alpha-2).
```
For `1/2<=alpha<=1`, the absolute value of each expression is bounded by `max(alpha,2-2alpha)`. Together with §2 this proves the universal exact formula. The actual complete histogram of the 1,225 covectors, indexed by `k*alpha+h/2`, is:
```text
(k,h)       multiplicity
(-2,2/3/4)  26 / 20 / 2
(-1,0/1/2)   4 / 152 / 76
( 0,-1/0/1)120 / 425 / 120
( 1,-2/-1/0)76 / 152 / 4
( 2,-4/-3/-2) 2 / 20 / 26
```
The project checker `research_checks/CBRC_F7_R433_MARKED_SECTOR_EXACT_DEFECT_20261121.py` implements this via Python standard-library **exact integer** determinants, row products, sign compositions and assertions. Executed independently: `PASS: 16 integer forms; 84 oriented cocircuits; 1225 covectors; 15 exact affine defect classes; alpha=2/3 yields maximum 2/3`. The global argument rests on exact hyperplane completeness, not a box search. Witnesses independently attain the asserted bound.

## 4. Stronger comparison bound, and actual open minimum

For the wider class of all functions `q:Z^2 -> [0,infinity)` that are J-even, have `q(0,0)=0`, `q(t,0)=1` for every nonzero integer `t`, the two exact marks `q(2,1)=q(-1,-1)=1/2`, and the *additional* uniform floor `q(n,m)>=1/2` at every nonzero pair, let `E_*` be the infimum of the fixed-A global defect.

At `z=(1,-1,0,0)`, `Az=(4,2,-3,-3)`. J-evenness and the mark fix the input energy to `1/2`; the nonzero output pairs have total energy at least `1`. Hence `E_*>=1/2`, while `q_{2/3}` supplies `E_*<=2/3`:
```text
                 1/2 <= E_* <= 2/3.
```
The exact unrestricted `E_*` within this explicit uniformly positive class remains open. The original F7 task's exact-conservation no-go, blind-context restrictions, old standalone Lemma 3.3 retraction and ten ablations are unchanged.

## 5. Preservation, provenance and control status

- Original F7 author `EM-CBRCF7-83A1D4`: mixed matrix, exact J-dropped scalar and original frozen revision, owner commit `c9bf0811f8cc17af1fa116af75911ed70b1f26b9`.
- Driver r429 baseline: `research_notes/driver/2026-11-21_f7_J_symmetrized_GL4_exact_three_quarter_defect_r429.md@d1be8fbdecbc758e9cd61f35dbb06d58cd79e041`.
- Driver r432 prior exact-marked defect-one construction: `research_notes/driver/2026-11-21_f7_r432_exact_marked_J_even_finite_orbit_correction_defect_one.md@c47b50ce740856a67734f55ebf971ed521a5bef8`.
- This result's checker was independently executed, then published and read back as the identical byte content on main at `94499504a70f34d81a05667c695ad95e0363140e`, blob `89689b7d8c1b0410b969e7b572ce271f3059fe0a`.

Native F7 first Review remains rejected with `NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED`, documented in GitHub Issue #2874. Separately, two frozen Result manifest SHA256 fields conflict with actual original GitHub content. This note changes neither frozen byte claims nor formal author/reviewer authority.

**Layered outcome:** new mathematical exact construction/proof subunit +1; Native Review accepted +0; Native Result accepted +0; formal Task completed +0; mother Objective closed +0. Next: investigate whether a non-sector function reaches the universal floor `1/2`, and resume the original valid Review path only on a new, actually authorized control opportunity.
