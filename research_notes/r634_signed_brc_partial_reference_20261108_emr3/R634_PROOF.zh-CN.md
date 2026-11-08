# R634 — signed BRC 部分背景参照的最优方向歧义定理

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED.
Frozen R462 science pin: 18783e01e3646c72b7aab3b16d3f565e83e6446f; original signed K generator Git blob 7fa7a762f758b30c6090468ac43487daa34abad8; theta=0. Parent R633: 1cc630a021e9870ab15f95c0e9acb2f7698de962.

## Precise observer model

Six native X6 spatial axis labels remain intact. Let P_j=K_(2j-1), M_j=K_(2j), j=1,...,6, be the frozen signed BRC polynomial branches; their t-valuations are respectively 2j-2 and 2j-1, and leading coefficients are P=(2,-8,6,106,83,9), M=(-1,-11,53,119,36,1), all 5-units. For unknown pi in S6, spatial axis x uses j=pi^{-1}(x). Independently on each axis, observe

Y_x^+ = A_x^+ P_j + H_x,   Y_x^- = A_x^- M_j + H_x.

The unknown H_x in Z[t] is common to the two probes on the same axis, but may differ between axes. Its constancy is also a legal Newton-background degree-zero special case. The gain valuation a>=1 is known, nu_t(A_x^+)=a with mod-5-unit leading coefficient; independent A_x^- satisfies nu_t(A_x^-)>=a-1. Exactly r selected spatial axes additionally reveal an independent matched background reference R_x=H_x. Data consist of mod-5 polynomial jets to cutoff d>=0 of all 12 probes and the r references. Unknown nuisance parameters may depend on the candidate orientation pi, as is required for universal identifiability.

Define m=min(6,max(0,floor((d-a)/2)+1)), h=6-m, s=min(r,h) and (h)_s=h!/(h-s)!.

## Exact minimax fiber theorem

The maximum number of distinct orientation permutations compatible with a single legal observation transcript is exactly

    F(r,d,a) = (h)_s * (6-r)!,  0<=r<=6, d>=0, a>=1.

Upper bound: on each calibrated axis, Z_x=Y_x^+-R_x=A_x^+P_j has mod-5 t-valuation a+2j-2. If this valuation is <=d, the label j is unique. If it is >d, the d-jet is zero, allowing at most h as-yet-hidden labels. If s' calibrated axes have zero positive corrected jet, at most (h)_(s') ways remain to label those axes. The uncalibrated 6-r axes permit at most (6-r)! arrangements. Since s'<=min(r,h), the stated bound follows; the opposite-probe readout can only reduce the fiber.

Sharpness: on all calibrated axes choose H=0, R=0 and A^+=A^-=t^a. Their positive readouts distinguish each visible j; for any hidden j both positive and negative jets vanish by depth d. On each uncalibrated axis use the full exact zero-data witness from R633: P_j=t^(2j-2)U_j, M_j=t^(2j-1)V_j; take A^+=t^a V_j, A^-=t^(a-1)U_j, H=-t^(a+2j-2)U_jV_j. Then the full Z[t] identities Y^+=Y^-=0 hold, and all gain valuations and mod-5 leading-unit requirements hold. Place s hidden labels on calibrated axes, any remaining labels on uncalibrated axes; this creates precisely (h)_s*(6-r)! permutations yielding the identical transcript. QED.

## Sharp consequences

At d=a+8, m=5 and h=1, hence F(r,a+8,a)=(6-r)!. For r=0,1,2,3,4,5,6, the exact worst-case ambiguity is respectively 720,120,24,6,2,1,1. Therefore FIVE matched axis-specific background references are sufficient and necessary for uniform recovery of all 720 directions; a sixth reference is redundant under the S6 permutation constraint.

For r<=4, even infinite polynomial precision leaves at least (6-r)! orientations with the same data (via full-zero nuisance on uncalibrated axes). For r=5 and d<=a+7, put labels j=5 and j=6 on two calibrated axes with H=0, A^+=A^-=t^a; both signed probe jets vanish and swapping these labels leaves the transcript invariant. Thus d=a+8 is the sharp uniform cutoff for five references.

More generally, F(r,d,a) gives the exact depth-vs-reference-budget tradeoff, not just its full-recovery point. Reference count r is an observation-channel count, NOT a reduction of native spatial dimension.

## Verification, scope and next question

R634_VERIFY.py regenerates all twelve frozen signed K branches from the integer binomial K generator, tests valuation and the full-zero nuisance identities, and exhaustively groups all 720 S6 permutations for 3 gains a=1,2,4, 12 cutoffs d=a-1,...,a+10, and all seven reference counts r=0,...,6. It checks 196746 exact assertion units and writes R634_EVIDENCE.json, marker R634_PARTIAL_REFERENCE_MINIMAX_FIBER_PASS. The full quantified result is supported by the proof; these enumerations cross-check its frozen six-axis instance.

Reuse: T0_BRC signed provenance, T6_OPERATION_SAFE_QUOTIENT within the stated observer, T7_FINITE_SYMMETRY_EQUIVARIANCE and R633's exact zero-data witness. This is an auxiliary six-axis BRC observation construction. The Source registered native X6 field dynamics, joint-path source tags and heartbeat evolution have not yet supplied an authenticated matched-background reference operation. Preserve provenance, grade, paths, multiplicity, the native 6+1 typing and all P000 constraints. No physical heartbeat calibration or Task Result/Driver acceptance is claimed.

Next test: retrieve exact Source-registered joint-field operations to see whether FIVE axis backgrounds are observable in the same sense as their positive probes; alternatively propose a specific lower-rank cross-axis background law and prove its native admissibility and observer preservation.
