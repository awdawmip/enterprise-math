# BRC N=4/S23: exact behavioral convexification for full-policy decoders

**2026-11-01 — author analytic theorem; exact rational auxiliary checks; UNREVIEWED / NOT_ADMITTED.**

## Model and quantifiers

Continue PR #1762, immutable predecessor c22282ef2deea811f7e300c76c7282deefb39f89. Six retained latent-source rows AU0, AU1, AV, BU0, BU1, BV are mixed by the row-stochastic 6x6 matrix

    M = [[1/2,1/2,0,0,0,0],
         [9/20,11/20,0,0,0,0],
         [0,0,1,0,0,0],
         [0,0,0,1/2,1/2,0],
         [0,0,0,1/10,9/10,0],
         [0,0,0,0,0,1]].

Every lawful S23 behavioral policy has 11 stop controls theta in [0,1]^11: a_A,a_B (first stage), b_U,b_AV,b_BV (second stage), and c_x for each of six terminal sources. Set first-stage groups g=(0,0,0,1,1,1), second-stage groups h=(0,0,1,0,0,2). For latent source x the four-time row is exactly

    f_x(theta) = [a_g, (1-a_g)b_h, (1-a_g)(1-b_h)c_x,
                  (1-a_g)(1-b_h)(1-c_x)].

Let F(theta) have six such rows. E is ONE common row-stochastic 6xk encoder fixed before policy selection; D is any kx4 row-stochastic decoder. Define

    V_E(theta) = min_D max_{i=1..6} TV((M F(theta))_i,(M E D)_i),

with TV(p,q)=sum_t |p_t-q_t|/2. For this theorem the decoder is allowed to know the COMPLETE policy theta, but not the realized coin flips/source/stopping result.

## Theorem: exact 2048-table reduction for arbitrary stochastic E

For every integer k >= 1, and more strongly for each fixed row-stochastic E,

    sup_{theta in [0,1]^11} V_E(theta)
      = max_{s in {0,1}^11} V_E(s).                           (1)

Hence the infimum over common encoders of the full behavioral, full-policy-visible minimax is EXACTLY the infimum over common encoders of the maximum of the 2048 deterministic causal policies, each with its own independently chosen legal decoder.

Equivalent threshold statement: for fixed E and epsilon, existence of a decoder D_s of error <= epsilon for every deterministic causal table s is necessary AND sufficient for existence of a decoder D_theta of error <= epsilon for every admissible behavioral theta, WITHOUT changing E.

**Proof.** Presample all 11 causal Bernoulli decisions as a complete deterministic table s in {0,1}^11. The weight of that table is

    w_s(theta)=product_{j=1}^{11} (theta_j if s_j=1 else 1-theta_j),
    w_s >= 0,  sum_s w_s=1.                                  (2)

Because each of the four probabilities f_x(theta) is multilinear in the eleven distinct controls, the following exact positive-mixture identity holds SIMULTANEOUSLY for every x and t:

    F(theta) = sum_s w_s(theta) F(s).                         (3)

For each s choose a legal decoder D_s with error <= epsilon (attained for an optimum since the decoder simplex is compact). With the FULL policy theta available, construct the single stochastic decoder

    D_theta = sum_s w_s(theta) D_s.                           (4)

Its rows are nonnegative and sum to 1. Linearity in the source readout and decoder gives

    M F(theta) - M E D_theta
       = sum_s w_s(theta)[M F(s) - M E D_s].

Taking the max of row total variation, applying the triangle inequality and then the nonnegative weights gives

    max_i TV((M F(theta))_i,(M E D_theta)_i)
        <= sum_s w_s(theta) * max_i TV((M F(s))_i,(M E D_s)_i)
        <= epsilon.                                          (5)

Every deterministic s is itself an admissible behavioral theta, proving the reverse direction. Infimizing over E establishes (1). No deterministic, finite-precision or fixed-rank assumption on E was made. QED.

The result extends verbatim to arbitrary explicitly known probability mixtures of deterministic policy tables, including correlated ex-ante strategy randomization. The decoder uses the mixture specification, never a realized random branch.

## Why the theorem does not settle finite policy labels

A finite m-label problem must precommit to ONE BANK of D_1,...,D_m, and can only select a label after the policy. The convex decoder (4) generally is NOT in that bank.

Exact lawful two-policy witness (m=2, k=6 identity encoder): first two stages always continue, six terminal stop controls all =1 for policy H3 and all =0 for H4. Two fixed decoder kernels output delta_3 and delta_4 respectively at every source. H3 and H4 both have reconstruction error ZERO using the corresponding label. The legal midpoint policy with six terminal coins =1/2 has all prepared readouts (delta_3+delta_4)/2, whose TV distance from EITHER bank decoder is exactly 1/2. This is a **restricted two-policy counterexample**, not a claim that the bank covers all 2048 corners and not a solution of the full 10-tag question.

## Application to predecessor, and exact next search space

In the prior c22282ef proof, the deterministic k=5 encoder merges AU0 and AU1, keeps AV/BU0/BU1/BV separately and, given a complete policy, reconstructs the merged latent source by q=(19 f_AU0+21 f_AU1)/40. For all 2048 deterministic tables this has prepared-input TV <=1/40; by (1) it has the SAME uniform <=1/40 bound for every lawful behavioral table, with the same fixed encoder. The lawful third-stage AU0 indicator attains 1/40 for that encoder.

The unrestricted stochastic k=5 full-policy minimax is NOT thereby resolved: retained proved bounds are [1/47,1/40]. The exact finite next task is a common row-stochastic E of size 6x5 together with 2048 policy-specific row-stochastic matrices D_s (5x4). For fixed E each per-policy feasibility question is linear; across E,D_s it is a bilinear constrained problem. A rational explicit strict feasible point or a universal analytic/dual obstruction is needed to decide whether the 1/40 bound can be improved.

## Validation and model boundaries

The companion executed VERIFY.py performs exact Fraction arithmetic for all 2048 deterministic causal tables; 12,288 exact prepared-input comparisons of the known deterministic five-state decoder; exact product-weight interpolation for three noncorner rational 11-tuples, including all 6x4 source/time entries and the interpolated decoder; the sharp AU0-indicator case; and the 2-tag midpoint counterexample. The exact output is RUN_EVIDENCE.txt. The theorem for ALL real behavioral parameters and ANY stochastic encoder follows from (2)-(5), not finite testing.

BRC use is typed as the existing six positive latent-source masses, six prepared mixtures, distinct branch provenance and positive causal policy-table weights. The differences in (5) are EXTERNAL signed readout-comparison differences, never cancellation of positive branch mass or complex amplitude. This is an auxiliary observer theorem, not a physical claim: six source labels are not the six native P000 spatial axes; four stopping labels are not the native time axis. Native P000 X6, S2 information-set transfer, native dynamics, independent review and admission each retain separate obligations. No pi/trigonometric or non-BRC physical propagation was performed.

**Frozen source provenance:** GLOBAL_KNOWLEDGE_V1 canonical main@9ced971d8b4a0352707cfb25bcb17977a494feb4; Enterprise Math main@993a408982a302265cb3c31f93e69e4751299500; predecessor c22282ef2deea811f7e300c76c7282deefb39f89. Connected GitHub principal awdawmip. Native service status returned research_authority_granted=false and active_jobs=5/5 in this run. This is independent author-side material, without native CLAIM, Result, verified live Owner, activity registration, independent review or admission.