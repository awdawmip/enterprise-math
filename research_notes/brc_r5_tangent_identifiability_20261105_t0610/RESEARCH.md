# R5 — Tangent Bellman identifiability and local first-gate rigidity (2026-11-05)

**Status:** AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Researcher `EM-DIRECT-597517`; activity `RA-6A0C63A77ECC99540ACEE683`. Frozen scientific input: global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate predecessor: `e2a0caf52713929b0bb6a6a249f6cdaa4bd15178:research_notes/brc_r5_timing_threshold_pair_20261105_t0538/RESEARCH.md`.

## Definitions
Time-1 hidden source h has P and Q mass w_h>0, Σw=1, and likelihood ratio 1. FULL sees h; seedless LR only observes (time, P/Q ratio). At t1,t2 legal actions are STOP/P, STOP/Q and CONTINUE; free P/Q terminal declaration is available at t3. Continuing at t1 produces r_j>0 with source-specific strictly positive Q kernels K_h(j), ΣK_h=Σr_j K_h=1. Continuing at t2 produces s>0 from strictly positive Q kernels M_hj(s) with ΣM=1, ΣsM=r_j. All supports finite. The observer is O4=(eP,eQ,TP,TQ) with eP=P(declare Q), eQ=Q(declare P), and T terminal decision time.

## Theorem 1 (all-real tangent-sign obstruction)
Suppose t∈(0,1) is not equal to any r_j, and at this **common lower timing-indifference face** every source satisfies

  (t−1)+Σ_j K_h(j)(t−r_j)_+=0.                                        (1)

Define J_+={j:r_j<t}, p_h=Σ_(j∈J_+)K_h(j), L_h=1+p_h, and the **effective terminal Q ratio measure**

  μ_h=Σ_(j∈J_+) K_h(j)M_hj + Σ_(j∉J_+) K_h(j)δ_(r_j).                (2)

Each μ_h is a probability distribution with first moment 1. Put I_h(k)=min(1,k)−∫min(s,k)dμ_h(s) for k>0. If the *complete four-dimensional convex hulls* of O4(FULL) and O4(seedless LR) agree, then for every k>0, I_h(k)/L_h is independent of h. Equivalently, all signed finite measures (μ_h−δ_1)/L_h coincide.

**Proof.** Fix any k>0 and δ∈R. Take signed normal n_ε=(−ε,−εk,−1,t+εδ), ε>0. At ratio s, the optimal terminal classification reward is −ε min(s,k); no history-dependent terminal declaration improves on this. At t2, when ε=0 the CONTINUE−STOP timing reward is t−r_j. Since t≠r_j and the finite kernels are bounded, for all sufficiently small ε>0, the optimal time-2 action is CONTINUE exactly on J_+, even if M_hj depend on h. Thus LR and FULL have the same optimal t2 action at every shared key.

Time-1 STOP has score S_ε=t−1+ε(δ−min(1,k)). The optimized CONTINUE−STOP difference for source h is, **exactly** for sufficiently small ε,

  Z_h(ε)=(t−1)+Σ K_h(j)(t−r_j)_+
              +ε[δ(1+p_h)+min(1,k)−∫min(s,k)dμ_h(s)]
        =ε[δ L_h+I_h(k)].                                           (3)

Consequently the Bellman supports for *all real behavioral strategies* are

  h_FULL(n_ε)=S_ε+Σ_h w_h(Z_h(ε))_+,
  h_LR(n_ε)=S_ε+(Σ_h w_h Z_h(ε))_+.                                (4)

Linear support optimization admits deterministic policies, including at both decision times. Because w_h>0, the Jensen gap between (4) vanishes iff all nonzero Z_h have one sign. If the zeros −I_h(k)/L_h differed, choosing δ strictly between two zeros would give opposite Z signs, hence strict FULL/LR separation. Therefore normalized I profiles coincide for every k>0.

Finally min(1,k)−∫min(s,k)dμ=∫(k−s)_+dμ−(k−1)_+. Its second distributional derivative on (0,∞) is μ−δ_1. Therefore equality of normalized I for all k is equivalent to equality of signed measures (μ_h−δ_1)/L_h, proving the claim. □

## Theorem 2 (identifiable-path rigidity)
Under Theorem 1, assume the r_j are pairwise distinct. For each j with r_j≠1, suppose a measurable set E_j of effective terminal ratio values excludes 1, the E_j are disjoint, and μ_h(E_j)=K_h(j) for *every* h. This holds, for example, if all continued branches have distinguishable terminal ratio supports disjoint from 1 and stopped branches, while distinct stopped ratios remain distinguishable.

Then equality of complete four-dimensional FULL/LR convex hulls forces **K_h identical for every source**.

**Proof.** Theorem 1 gives equality of (μ_h−δ_1)/L_h. Restricting to E_j excludes δ_1 and yields K_h(j)/L_h independent of h, for every r_j≠1. Because t<1, all j∈J_+ have r_j≠1. Therefore p_h/L_h=p_h/(1+p_h) is common. This function is injective on p≥0, so p_h, hence L_h, is common. Each K_h(j) with r_j≠1 is common, and mass normalization fixes the at-most-one r_j=1 entry. □

This is an exact obstruction for the declared identifiable-path subfamily. If source/branch supports overlap, the normalized signed-measure necessary condition still holds, while identification of individual K entries requires new work.

## A new exact tangent witness
Reuse the positive 5-key previous model: r=(1/4,1/2,1,3/2,7/4), w_A=w_B=1/2, K_A=(209,184,214,184,209)/1000, K_B=(191,216,186,216,191)/1000. They have common timing indifference t=23/28, although K_A≠K_B. At t2 each r_j CONTINUE leads with conditional Q probabilities (1/2,1/2) to s_j±=r_j(99/100,101/100); the P probabilities are s_j±/(2r_j)>0. All 10 s are distinct; the two low-j terminal supports avoid the high stopped ratios and 1. Theorem 2 therefore applies.

Take k=3/4, ε=1/100. The set J_+ is {r=1/4,1/2}, whose terminal s remain below k, so I_h(k) agrees with the one-gate Bayes gain. Exact values:

  L_A=1393/1000, L_B=1407/1000;
  I_A=301/2000, I_B=299/2000;
  θ_A=−I_A/L_A=−43/398, θ_B=−I_B/L_B=−299/2814.

Choose δ=(θ_A+θ_B)/2=−60001/559986. Then Z_A=1/80400>0, Z_B=−1/79600<0 for n=(−1/100,−3/400,−1,45938849/55998600). Exact Bellman calculation gives

  h_FULL=−13972523/74664800,
  h_LR=−20959481/111997200,
  **gap = 1/160800**.

A legal FULL witness continues at t1 only for A, at t2 continues only when r<t, and declares Q if the final ratio is below 3/4, P otherwise. B stops/P at t1. Its exact vector is

  W=(577/8000,1607/2000,12577/8000,3393/2000).

It attains h_FULL, hence W is outside conv(O4(LR)), and

  dist∞(W,conv O4(LR)) ≥ (1/160800)/||n||₁ = 1393/411669698.

## Checks and next frontier
Python standard-library Fraction executed exact positive P/Q kernel normalization, Bellman maximization, the witness, signed distance, and 148 direct rational directional checks on 74 k grid points. Code/checker and execution output are in the companion files. Universality follows from the analytic proof, not finite enumeration.

NEXT: make source-dependent second-stage kernels M_hj with **overlapping** ratio outputs so (μ_A−δ_1)/L_A=(μ_B−δ_1)/L_B despite K_A≠K_B. Preserve positivity, conditional P/Q moment and full free declarations. Check whole R⁴ support equality; only for a hull-equal model test actual real behavioral-image nonmembership. P000, ACTIVE worldview, scientific pins and Source admission unchanged. No formal CLAIM, Result, or independent review is claimed.