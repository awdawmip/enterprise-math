# Stage301-B — sharp simultaneous adaptive minimax under one shared-IID Bernoulli port

**Status:** PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED, 2026-10-30. External finite positive-mass BRC-style probability model only; neither native P000-X6 proof nor formally admitted Task Result.

## Pinned inputs and precise model

GLOBAL_KNOWLEDGE_V1 main `d81efb6ab014935b49d4da1d824b126ef82ad480`; Enterprise Math control main `1ee243ad797290c54983517c5d5bb22758c2133d`; full P000 original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches its startup projection. ACTIVE Heartbeat World X6/time, ACTIVE residual-fidelity worldview, current portable research and BRC typing rules read. Predecessor Stage300-B `e9fe8cfb1f119366d6621db2254518d5d7cb4a04` (PROOF_STAGE300B.md) fixes the following model.

Hidden source S is 0 or 1 with prior 1/2. The initial visible bit X is fair independent of S. At two subsequent rounds a visible-history examiner chooses H (a new independent fair bit) or F (a new independent bit with rate p_S, p_0=1/4, p_1=3/4). Source persists. Policy observes its previous actions and visible bits, not S. A proposed physically restricted simulator chooses one random real Theta in [0,1] at outset and draws X,Y1,Y2 **independently conditional on Theta, always at rate Theta irrespective of H/F labels**. One and the same Theta distribution mu must serve every adaptive policy. No source-revealing intervention is permitted in this port class.

For any policy pi, let P_s^pi denote the complete source-conditional **action-labelled** path law, M^pi=(P_0^pi+P_1^pi)/2 and Q_mu^pi the simulator law. TV(P,Q)=sum|P-Q|/2. Define
```
W_pool(mu) = sup_pi TV(M^pi,Q_mu^pi);
W_tag(mu)  = sup_pi (TV(P_0^pi,Q_mu^pi)+TV(P_1^pi,Q_mu^pi))/2.
```
These are two different observation objectives. Real mixing measures and randomized, history-adaptive policies are allowed. Positive branch weights and source labels are *not* signed amplitudes.

## Theorem 301.1 — pooled minimax is 3/32

`inf_{mu} W_pool(mu)=3/32`, attained by `mu_pool=(delta_(3/8)+delta_(5/8))/2`.

**Proof.** For any randomized examiner, pre-sample all its future contingent choices; total variation of the resulting mixture does not exceed the largest deterministic-plan TV. A deterministic plan chooses step-1 action separately for X=0,1 and step-2 action for each (X,Y1); therefore 2^(2+4)=64 outcome-distinct plans are sufficient. The map from each three-bit word to its complete (bits,deterministically chosen action labels) path is injective, preserving TV. Under the shared-IID simulator the three-bit distribution Q does not depend on the policy.

Complement all three visible bits and interchange S=0,1. The pooled source model and the examiner policy class are invariant; mu is changed to its pushforward under Theta->1-Theta. Both W's are convex in Q, so reflecting and averaging mu can only improve either W. A minimizer may thus have symmetric mu. For a symmetric mu, write each particular three-bit word's probability as `q_k` according to Hamming weight k: `32(q_0,q_1,q_2,q_3)=(a,b,b,a)`, `a+3b=16`, `0<=b<=4`. Every b in this interval is feasible by a symmetric mixture of delta_(1/2) and (delta_0+delta_1)/2.

For each prefix row (X,Y1) its two output-word probabilities, in units of 1/32, are (4,4) unless *both* selected actions are F, when they are (5,3) if Y1=0 and (3,5) if Y1=1. Any subset of the four rows can be put into the latter state. Taking the larger L1 distance independently for each row gives exactly
```
64 W_pool =
2 max(16-4b, |a-5|+|b-3|)
+2 max(8-2b, |b-3|+5-b), a=16-3b.
```
At b=15/4, a=19/4, edge-row maximum is 1 and interior-row maximum is 2; hence 64 W_pool=6. For b<=15/4, flag only the two interior rows: 64 W_pool>=36-8b>=6 (the flagged interior-row L1 distance is at least 2). For b>=15/4, choose FF throughout: 64 W_pool>=8b-24>=6. Thus all-real lower and upper coincide. The stated two-atom mu yields b=15/4 exactly. QED.

## Theorem 301.2 — source-tagged minimax is 17/64

`inf_mu W_tag(mu)=17/64`, attained by `mu_tag=(3/8)delta_(1/4)+(1/4)delta_(1/2)+(3/8)delta_(3/4)`. This has b=13/4, a=25/4.

**Continuum lower certificate.** Symmetrization above applies also to W_tag. Represent any policy by six H/F bits `(a1(x=0),a2(0,0),a2(0,1),a1(x=1),a2(1,0),a2(1,1))`, 1 for F. Two test policies are A=(1,0,1,1,1,0), B=(1,1,1,1,1,1). In lexicographic 000,001,010,011,100,101,110,111 order the exact source laws times 32 are
```
             S=0                         S=1
A     (6,6,3,1,9,3,2,2)           (2,2,3,9,1,3,6,6)
B     (9,3,3,1,9,3,3,1)           (1,3,3,9,1,3,3,9).
```
For any sign vectors epsilon in {-1,+1}^8 and each s, `|P_s-Q|>=epsilon_s*(P_s-Q)` termwise. Choose for A: `epsilon_0=(-,+,-,-,+,-,-,-)`, `epsilon_1=(-,-,-,+,-,-,+,-)`; for B: `epsilon_0=(+,-,-,-,+,-,-,-)`, `epsilon_1=(-,-,-,+,-,-,-,+)`. Evaluating the signed sums divided by four against `32q=(a,b,b,a)` gives two global affine lower certificates
```
W_tag >= 15/32 - b/16;    W_tag >= 1/16 + b/16.
```
Their maximum is >=17/64, with equality possible only at b=13/4.

**Exact finite upper certificate.** For b=13/4, the eight probabilities of Q multiplied by 128 are (25,13,13,25,13,13,13,25). For each prefix x and chosen step-1 action, maximize separately over step-2 H/F in each y branch. Below each [H,F] entry is `128 sum_{s,z}|P_s(x,y,z)-Q(x,y,z)|`:
```
                    y=0 [H,F]  y=1 [H,F]    max sum
x=0, first H         [24,34]    [12,32]        66
x=0, first F         [34,34]    [32,34]        68
x=1, first H         [12,32]    [24,34]        66
x=1, first F         [32,34]    [34,34]        68
```
Thus all 64 deterministic policies have total signed-absolute sum at most 68+68=136, and R_tag<=136/(128*4)=17/64. Convexity covers randomized policies. A and B attain the bound and the explicit mu realizes Q, proving sharpness. QED.

## Corollary 301.3 — exact physical-vs-free adaptive gaps

The Stage300-B Bayesian, source-blind **free causal** simulator realizes M^pi simultaneously for all policies, hence its pooled minimax is 0. For tagged risk, the fixed FF policy gives TV(P_0^FF,P_1^FF)=1/2, so free risk >=1/4. Every adaptive policy can be simulated by first drawing two latent independent F samples conditional on S, then passing them, plus source-independent fair H noises and X, through a common stochastic kernel implementing that policy. By TV data processing, TV(P_0^pi,P_1^pi)<=1/2. The same free Bayes-pooled process thus has tagged risk TV(P_0^pi,P_1^pi)/2<=1/4 for every pi. Consequently the free tagged optimum is **1/4**. The simultaneous shared-port gaps relative to free causal are exactly **3/32 pooled** and **17/64-1/4=1/64 tagged**.

The earlier fixed-FF pooled gap 1/12 and fixed-FF tagged no-gap result concern a *different quantifier order*; they are not contradicted.

## Computation and native-boundary status

The supplied Python standard-library Fraction verifier exhaustively checks 64 effective deterministic policies and 128 normalized strictly-positive source path laws, the exact finite-atom measures and dual supports. Actual stdout ends `STAGE301B_SIMULTANEOUS_MINIMAX_EXACT_PASS`. The infinite-mixing theorem is established by the proofs, not by finite parameter sampling. No X6 native path, third-coordinate semantics, Cell address codec, triadic closure E, native time, signed BRC amplitude or faithful functor has been constructed. Accordingly no native physical residual or BRC–Shor claim follows. Independent Driver review and Source admission remain pending.

**Actual identity/owner boundary:** Site-scoped gateway returned research_authority_granted=false and not live backend-verified at 2026-10-30 06:10 UTC; current control task listing returned CONTROL_QUOTA. This portable author proof does not borrow, supersede or assert another researcher's live CLAIM. Stage302-B is the next **proposal**, not a canonical taskbook change.
