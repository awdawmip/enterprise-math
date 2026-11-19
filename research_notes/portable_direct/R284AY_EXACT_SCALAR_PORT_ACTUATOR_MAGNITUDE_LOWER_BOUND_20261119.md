# R284AY — Exact actuator magnitude lower bounds for scalar determinant Port observers

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_INTEGER_BOUND_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AT (formal Port probes) → R284AU-PACK → R284AW (single-entry readings) → R284AX (one simultaneous-star reading). Historical frozen science input: R284AT source blob 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Setup

Fix integers n≥2 and H≥1. The unknown matrix C has all n² entries in {1,...,H}. A scalar response is an exact integer determinant

    y(C)=det(D−C−Z),

where D is a programmable integer diagonal and Z is a programmable off-diagonal edit matrix. The total setting on *each entry*, not merely each underlying actuator, must obey |D_ii|≤K and |Z_ij|≤K (for a simultaneous row-star observer, 0≤D_ii,z_v≤K and at most one edit per entry). The instrument may select settings nonadaptively or adaptively. This is an auxiliary named-Port observation, not a native Heartbeat-X6 dynamic.

The entries of D−C−Z have absolute value at most H+K. Let M=n!(H+K)^n. Leibniz's determinant formula implies |y(C)|≤M for every C and permitted setting.

## AY1 — universal exact dynamic-range lower bound

If **one** such exact integer scalar reading identifies all H^(n²) possible matrices, then

    2 n! (H+K)^n + 1 ≥ H^(n²).                          (1)

Indeed, y takes at most 2M+1 integer values in the interval [−M,M]. Injectivity needs at least H^(n²) distinct values. An exact necessary integer setting bound is therefore

    K ≥ max{0, ceil(((H^(n²)−1)/(2n!))^(1/n)) − H}.     (2)

The n-th root ceiling in (2) is the least nonnegative integer t with t^n ≥ (H^(n²)−1)/(2n!), computed by exact integer comparisons.

For each fixed integer H≥2, Stirling's formula gives, as n→∞,

    K ≥ (e+o(1)) H^n/n − H.                            (3)

This means that single-reading discrimination of all bounded-height matrices requires exponentially large *instrument magnitudes* in n, even if these magnitudes require only polynomially many bits to specify. Equation (2) is a necessary lower bound, not an assertion that its value can be achieved.

## AY2 — adaptive q-read range/precision tradeoff

For an instrument whose admissible settings always obey the same per-entry K bound, every scalar response belongs to an alphabet of at most 2M+1 possible integers, irrespective of the previously observed adaptive transcript. A deterministic adaptive depth-q decision tree therefore has at most (2M+1)^q distinct leaves. Exact identification requires

    q log₂(2 n!(H+K)^n + 1) ≥ n² log₂ H.               (4)

This applies to simultaneous star edits or more general independently programmed edits as long as the summed edit on every entry obeys the K bound. It counts *determinant outputs*; the number of separately controlled actuators and settings must be accounted for in an implementation.

## AY3 — adversarial absolute output noise

If a scalar response is reported with unknown adversarial absolute error ≤δ, δ≥0 real, an exact one-reading decoder working for **all** such errors must assign disjoint closed error intervals to every different C. The integer-valued determinant centers thus need separation strictly larger than 2δ. Let Δ=floor(2δ)+1. Packing H^(n²) distinct integer centers in [−M,M] with gaps at least Δ yields

    2 n!(H+K)^n ≥ (H^(n²)−1)Δ.                          (5)

Accordingly,

    K ≥ max{0, ceil((((H^(n²)−1)Δ)/(2n!))^(1/n)) − H}.

The δ=0 case reduces to AY1. If δ<1/2, rounding the observed real output to the exact integer suffices for an already injective exact-integer scheme. At the closed boundary δ=1/2, a one-unit gap is insufficient for worst-case disambiguation. Noise affecting programmable inputs or relative measurement precision has a different model and is not bounded by this statement.

## Fully reproducible exact calculation

Companion checker: R284AY_dynamic_range_lower_bound_checker.py. It computes the least K satisfying the *necessary* cardinality inequality via exact integer n-th root and checks the inequality at K and at K−1 when positive. No floating-point power comparison is used.

Eight instances (n,H)=(2,2),(3,2),(4,2),(8,2),(16,2),(32,2),(8,3),(16,3) passed. The resulting minimum necessary K values respectively are 0,2,5,61,9227,328603591,1596,6061593. Four additional monotonicity comparisons checked that the closed half-unit adversarial error bound (Δ=2) never weakens the exact bound. The checker validates the implementation of the necessary inequalities; the theorem is the mathematical counting argument above. Independent review: NOT_REVIEWED.

## Relationship to BRC and the prior research

R284AX proves exact fiber separation for the specified simultaneous star Port observer by preserving signed, directed two- and three-channel coefficients in packed radix blocks. AY1–AY3 show an unavoidable quantitative cost in that exact compression: total integer output capacity depends on the instrument's allowed magnitude, so a nominally one-read observer can still have substantial resource demands. No deletion of joint, signed or provenance-bearing channels beyond the declared recoverable observer family is inferred; no P000, six-axis spatial or heartbeat dynamics axiom is modified.

## Unresolved units

1. Close the gap between the necessary actuator height Ω(H^n/n) and the very large sufficient height in R284AX, including input bit length, exact determinant computation and output decoding.
2. For bounded relative precision and bounded actuator range, derive achievable read–precision–actuation Pareto curves and concrete lower-bound instances.
3. Distinguish the mathematical scalar-read count from hardware actuator actions and calibration.
4. R284AW's adaptive single-entry integer alphabets H=2,3 remain an independent open lower-bound question.

Provenance: independent portable scientific source. Formal CLAIM/PROGRESS/Result/Review not asserted.
