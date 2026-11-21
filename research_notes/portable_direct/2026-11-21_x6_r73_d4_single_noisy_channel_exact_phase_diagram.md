# X6 R73 — 四阶正权 BRC：单一低精度通道的完整 Port–精度相图

Date: 2026-11-21 (Asia/Shanghai)
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED
Scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json` (frozen P000 V5).
Predecessors: R68 (weighted common-bias minimax), R72 (sharp all-weight saturation P4=125); R72 paper at `research_notes/portable_direct/2026-11-21_x6_r72_d4_sharp_saturation_125.md`.
Scope: conditional normalized positive-count BRC degree-histogram observer only; not native X6 Cell/Link/Port trajectories or `TRIADIC_CLOSURE_E` admission.

## Question

At D=4 and all integers p≥4, determine the optimal histogram-identification noise radius under one unknown shared additive bias and relative channel weights
`w=(1,t,1,1)`, with arbitrary real `t>0`. In particular determine exactly when the 125-Port residual class first improves upon the 11-Port class.

For counts `c0,...,c4≥0`, `sum c_d=p`, the measurements are
`Y_i = sum_{d=0}^4 c_d d^i + b + e_i`, `i=1,2,3,4`,
with unknown shared `b` and `|e_i|≤ηw_i`. Recover `(c2,c3,c4)`. For differences `a=(a2,a3,a4)∈Z³\{0}`, set
`q(a)=max(sum max(a_d,0),sum max(-a_d,0))`; `q(a)≤p` exactly characterizes histogram-difference realizability.
Set `z=(0,2a2+6a3+12a4,6a2+24a3+60a4,14a2+78a3+252a4)`.
Define `C(a)=max(|z2|,|z2-z3|,|z2-z4|)` and
`B(a)=max(|z3|,|z4|,|z3-z4|)`.
By the exact common-bias interval-intersection law from R68, for this weight family,
`η_pair(a;t)=max(C(a)/(2(t+1)), B(a)/4)`.
The requested threshold is `η*(p,t)=min_{a≠0,q(a)≤p} η_pair(a;t)`.

## Theorem — complete phase diagram (all p≥4, all t>0)

```text
η*(p,t) =
  max(6/(t+1), 7/2),                    p=4;
  max(4/(t+1), 3),                      p=5;
  3,                                    6≤p≤10;
  max(1/(t+1), 1/2),                    11≤p≤124;
  min(max(1/(t+1), 1/2), 12/(t+1)),    p≥125.
```

All equalities include boundary values. The only t-breakpoints are `1/3, 5/7, 1, 23` (for the corresponding Port bands). The smallest p needed for saturation *within this one-parameter family* is 125 when `t>23`, but is 11 for `0<t≤23`. More precisely, p=125 improves strictly over p=124 if and only if `t>23`. There is no intermediate improvement for any integer `12≤p≤124`, for any `t>0`.

## Proof

1. **Exact pair geometry.** Two noiseless moment lists, each allowing its own unknown scalar offset, are observationally compatible at noise radius `η` iff the four constraints on their relative offset have common intersection. Because these are real intervals, pairwise intersection is sufficient; thus `|z_i-z_j|≤2η(w_i+w_j)` for all `i<j`. With `w2=t` and all other weights one, the only denominator types are `1+t` (three gaps through channel 2) and `2` (three precise-channel gaps), giving the displayed formula. The coefficient matrix for `z2,z3,z4` has determinant 288, so C=0 implies a=0. Each `z_i` is even, hence every nonzero a has C≥2.

2. **Small-Port finite certificate.** For p=4,...,10, enumerate every triple `(a2,a3,a4)∈[-p,p]³`, except zero, retain `q(a)≤p`, and identify `a∼-a` by requiring its first nonzero component positive. Exactly 154, 280, 461, 707, 1028, 1434, 1935 unoriented triples occur respectively. The componentwise minima `(min C,min B)` are:
   - p=4: `(12,14)`, both achieved by `a=(1,0,0)`, q=1, z=(0,2,6,14);
   - p=5: `(8,12)`, both achieved by `a=(4,-4,1)`, q=5, z=(0,-4,-12,-4);
   - 6≤p≤10: `(6,12)`, both achieved by `a=(6,-1,0)`, q=6, z=(0,6,12,6).
   Because each coordinate's minimum occurs at the *same* feasible difference, this simultaneously minimizes `max(C/(2(t+1)),B/4)` for every positive real t. The accompanying stdlib-only Python program enumerates all 1,935 vectors at p=10 and independently checks each p-shell and its witness.

3. **All p≥11 without relying on the R72 atlas.** For any nonzero integer difference, C≥2. If B>0 then B≥2 (parity), and therefore `η_pair≥max(1/(t+1),1/2)`. The explicit `a=(10,-5,1)` has q=11, z=(0,2,0,2), C=B=2, and attains this bound.

   The only remaining case B=0 means `z3=z4=0`, i.e.
   `6a2+24a3+60a4=0`, `14a2+78a3+252a4=0`.
   Their primitive integer kernel is `Z(114,-56,11)`: the integer cross product is `(1368,-672,132)=12(114,-56,11)`, and gcd(114,56,11)=1. Its nonzero vectors have q=125|k| and z=(0,24k,0,0), so their minimum possible radius, when feasible, is `12/(t+1)`. For p<125 no nonzero kernel vector is feasible. For p≥125 the primitive ± vector attains the kernel minimum. Taking the minimum between the nonkernel and kernel classes proves the two large-p formulas.

4. **Sharp crossover.** At `t≤1`, `max(1/(1+t),1/2)=1/(1+t)`, which is below `12/(1+t)`. At `t≥1`, the nonkernel value is `1/2`. Compare `12/(t+1)` with `1/2`: equality exactly at t=23 and strict improvement exactly at t>23. This completes the global classification. QED.

## Exact verification and scope

The finite small-Port search is reproducible with `x6_r73_d4_single_noisy_channel_verify.py` (Python standard library, integer and Fraction arithmetic). The independent JavaScript integer enumeration in the research run gave the same shell counts and coordinate minima. The p≥11 result and t crossover are proved symbolically above; no finite experiment is extrapolated to all p or real t. Relative to R72, this is a new *weight-chamber* theorem with a separate direct high-p proof. R72's universal 28-candidate atlas is not required for the high-p derivation.

The BRC observer only distinguishes degree histograms at the stated measurement horizon. Distinct labeled source Ports, native time, joint triadic provenance and future Cell/Link operations are intentionally not quotiented without their own typed observer/future-operation descent certificate. No P000 mutation, Working Truth admission, formal Result or independent review is asserted.

## Next discriminating questions

- For arbitrary four positive channel weights, classify the truly active members of the R72 28-vector atlas and their exact semialgebraic weight chambers.
- Determine which rank-deficient precise-channel submatrices yield nontrivial primitive kernels with sharply delayed Port thresholds; extend to D≥5 and compare with R65–R70.
- Connect positive-count BRC observer output to Source-admitted triadic Cell/Link/Port event trajectories with an explicit provenance-preserving and future-operation-safe map; this mathematical observer theorem alone does not supply one.

Provenance: R68/R72 conditional author mathematics, and this run's exact verification; historical researcher source attribution `EM-X6-214D9C` is not claimed as current-session native capability. Formal execution remains subject to current canonical owner/CLAIM and independent Activity association.
