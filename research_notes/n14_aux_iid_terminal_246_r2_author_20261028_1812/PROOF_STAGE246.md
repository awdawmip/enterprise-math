# Stage246: exact terminal regime by source-aware sequential coupling

**Date:** 2026-10-28. **Research status:** AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.
**Frozen inputs:** Stage245 at alpha=2/5, V=24/5, immutable PR #1571 commit 333d7a3a05675189c555285dae9c241e5fbe9c3e. GLOBAL_KNOWLEDGE_V1 main@ab8c7adcf8749ab86b6222a9a869423dce8abb54; Enterprise Math main@820e7c4afd18efbe031eaa226feb88ac8292e288.
**Model:** external ternary IID P=(3,1,20)/24, Q=(2,2,20)/24, ordered-history randomized stopping and binary classification, N=14 samples. Define eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V_N(alpha) = min max(tP,tQ) subject to both errors ≤ alpha.

## Theorem (entire right-hand regime, ALL real alpha)

For every real alpha ≥ 2/5, the exact optimal value is

\[
\boxed{V_{14}(\alpha)=\max\{0,24-48\alpha\}.}
\]

It is affine of slope −48 on [2/5,1/2] and zero for alpha ≥ 1/2. In fact the identical equality holds for **every integer horizon N≥9**, because the witness below takes at most nine samples and the lower bound is horizon-independent.

## Universal lower bound, with complete-ordered-history quantifier

**Sequential TV lemma.** For arbitrary two discrete IID sample laws P,Q with one-step total-variation distance d, and any common nonanticipatory randomized stopping/classification policy with finite horizon N, one has

\[
1-e_P-e_Q \le d\min\{t_P,t_Q\}.
\]

**Proof.** Under an IID maximal coupling of one-step P/Q observations, use exactly the same auxiliary policy random seeds on both experiments. Until the first observation mismatch, identical ordered histories induce identical continuation/stopping decisions. Let A_k be the event that both histories agree through k−1 and both policies are still taking sample k. Conditional on A_k, the next paired sample mismatches with probability d. First mismatches are mutually disjoint, and different final decisions require at least one mismatch while both are active. Thus

Pr(different decisions) ≤ d sum_{k=1}^N Pr(A_k).

Both inclusions A_k ⊆ {tau_P≥k} and A_k ⊆ {tau_Q≥k} hold. Since E(tau)=sum_{k=1}^N Pr(tau≥k), the right-hand side is ≤ d min(tP,tQ). Finally 1−eP−eQ=Pr_P(decide P)−Pr_Q(decide P)≤Pr(different coupled decisions). QED. The coupling does not suppress path identity after the first mismatch, and the quantifiers include every policy using entire ordered history or extra random bits.

For the current rational IID pair, the **positive rational source-labeled maximal coupling** consists of four atoms:

| Paired samples (P,Q) | Rational weight |
|---|---:|
| (0,0) matched | 2/24 |
| (1,1) matched | 1/24 |
| (2,2) matched | 20/24 |
| (0,1) mismatch | 1/24 |

Its marginals exactly reproduce the two hypotheses, and d=1/24. Consequently min(tP,tQ)≥24(1−eP−eQ), which implies V_N(alpha)≥max(0,24−48alpha) for ANY finite horizon N.

## Explicit sharp nine-sample policy at alpha=2/5

Let q=6−(6/5)^9=1641054/1953125, so 0<q<1. Observe until the first symbol not equal to 2, deciding P upon symbol 0 and Q upon symbol 1. If all first eight symbols are 2, stop and decide Q with probability 1−q; otherwise take a ninth sample and decide P on 0, Q on 1 or 2. No other observations are taken.

Both hypotheses assign probability 20/24=5/6 to symbol 2 and 4/24=1/6 to a non-2 signal. The signal event therefore has exact common probability

\[
s = 1-(5/6)^8 + q(5/6)^8/6 = 4/5.
\]

Conditional on the signal event, the P-error symbol (1) has P probability 1/4 while the Q-error symbol (0) has Q probability 1/2. With no signal the policy decides Q. Hence

\[
e_P=s/4+(1-s)=2/5,\qquad e_Q=s/2=2/5.
\]

The probability of a signal at each active sample is exactly 1/6 under both laws, and all no-signal exits occur after a string of 2s; the finite stopping-hazard identity gives tP=tQ=6s=24/5. This explicit policy attains the TV lower bound at alpha=2/5 and agrees with Stage245's archived endpoint without depending on the prior Bellman-polytope implementation.

## Optimality for all real alpha and the zero-time terminal regime

For arbitrary real alpha ∈ [2/5,1/2], choose w=5−10alpha ∈ [0,1]. Independently at time zero, with probability w run the nine-sample witness; otherwise stop immediately and make a fair P/Q guess. The errors are exactly

\[
e_P=e_Q=w(2/5)+(1-w)(1/2)=\alpha,
\]

and the expected times are

\[
t_P=t_Q=w(24/5)=24-48\alpha.
\]

These formulas hold for irrational alpha as well; a randomized strategy is permitted real-valued mixing probabilities. The universal lower bound proves this strategy is globally optimal among all randomized stopping rules. For alpha≥1/2, the time-zero fair guess is feasible with tP=tQ=0, proving the remaining case.

## Provenance, scope, and future problem

Stage245's archived exact left segment has slope −88 ending at (2/5,24/5). The right slope −48 is a true kink, conditional only on the pre-existing Stage245 author proof. At alpha=1/2 there is another kink into the constant-zero regime; no more nonzero-width positive-time stages occur to the right.

BRC method: REUSE_APPLIED for the positive branch/provenance typing of definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at the fixed Enterprise Math snapshot. The four source-labeled rational atoms are essential: the mismatch branch cannot be merged away before the final-decision observer and survival inequality are applied. The calculation is an external IID model; no native X6/P000 spatial dynamics, original BRC software call, signed/phase cancellation, or heartbeat calibration is claimed.

The actual local exact execution of STAGE246_COUPLING_EXACT.py enumerated 20 ordered decision leaves, separately retaining P/Q rational weights; it printed STAGE246_COUPLING_AUTHOR_EXACT_PASS. EXACT_RUN_STAGE246.txt contains the complete output. Four rational alpha points are checked as spot tests; the proof above supplies the all-real quantifier. The native gateway reported research_authority_granted=false, control CODE_REVIEW_REQUIRED, and BACKEND_IDENTITY_CHECK_UNAVAILABLE on a read-only source-list request. No native CLAIM, Result, independent Driver review or formal theorem admission is inferred.

**Next exact research problem:** characterize the asymmetric two-cap region (alphaP,alphaQ) where max(tP,tQ) reaches 24(1−alphaP−alphaQ) for N=9 and N=14, using exact positive rational provenance-preserving branch masses; give concrete boundary witnesses or separating rational certificates. A transfer to P000's X6 requires a separate embedding, observer, time evolution and joint preservation theorem.