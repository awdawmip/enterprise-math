# R4-EC37 — Causal coupling of label-dependent BRC source kernels

**Status:** AUTHOR_SIDE_PROOF_AND_EXACT_FINITE_CHECK. This is an auxiliary positive-source BRC theorem and counterexample; no native X6 heartbeat program was run, and no independent Driver acceptance is claimed.

**Read pins.** GLOBAL_KNOWLEDGE_V1 canonical main `43639a1bd021e9c6e90e699fbb7b5021855fbef7`; Enterprise Math canonical control main `e5f859b01b76e84cb6b68b899cbe7d6390eb5b83`. P000 is ACTIVE_LOCKED; X6 has six native spatial axes and a separately typed time, and fixed_heartbeat_program is null. The tested state labels below are supplementary memory states, not extra spatial axes, and step index means source-operation order, not calibrated heartbeat time. Native owner and CLAIM remained unverified because the native task/owner read returned CONTROL_QUOTA.

**Frontier reused.** EC36 exact deterministic history-projection theorem: enterprise-math commit `898b56be4415f62b5bd4c09d1a564b7cba6ff156`, path research_notes/r4_ec36_composition_20261026/EC36_COMPOSITION.md. EC33 positive labelled source transition code: `0f84db42704c6e107adb9fd99d5e64cb77589e9d`, path research_notes/r4_ec33_label_fibre_20261026/EC33_verify.py. Neither predecessor is an independently reviewed native X6 theorem.

## 1. Model and exact question

Let S and Z be finite, separately typed internal state sets. At time/operation position t, a positive integer micro-source kernel has outcomes (observed source label l, successor state s') with integer multiplicity w_t(s;l,s')>=0. Its row sums are the SAME constant integer M>=1 for every state, t, and both compared models. Write

P_t(s;l,s')=w_t(s;l,s')/M,   Q_t(z;l',z')=v_t(z;l',z')/M.

The one-step **joint** outcome (label, successor state) is retained. Successor state may depend on the emitted label. The observable is the complete length-n labelled path and optionally a terminal port. If microscopic branch IDs are to be observed, their identities must be included in the label alphabet; merely retaining the positive R/B macro-label counts does not prove microscopic provenance fidelity. Declare a relation R_t between the two state sets at each t. Initial (s0,z0) belongs to R_0.

The question: How can the complete observable path-law total variation be controlled by exact local **joint-source-kernel** discrepancies under repeated, possibly stochastic and label-dependent updates?

## 2. Theorem EC37.1 — sharp general causal path-space upper bound

Let Gamma(P_t(s),Q_t(z)) denote the finite transportation polytope of all couplings of the two joint output distributions. For related (s,z) define

alpha_t(s,z) = max_{gamma in Gamma} gamma{ l=l' AND (s',z') in R_(t+1) },
delta_t(s,z) = 1-alpha_t(s,z).

Suppose for all (s,z) in R_t there is an exact rational defect budget 0<=delta_t(s,z)<=epsilon_t<=1, for each t=0,...,n-1. Denote the observed length-n source-label-word distributions by mu_n and nu_n. Then

**TV(mu_n,nu_n) <= 1 - PRODUCT_(t=0)^(n-1)(1-epsilon_t).**       (EC37.1)

If terminal port readouts coincide on R_n, the same bound holds for the JOINT observation (complete label word, terminal port). For the integer micro-source word counts C_n(w)=M^n mu_n(w), D_n(w)=M^n nu_n(w),

**SUM_w |C_n(w)-D_n(w)| = 2 M^n TV(mu_n,nu_n).**               (EC37.2)

*Proof.* All finite transport polytopes are compact, hence every alpha maximum is attained. Construct an online coupling by using a maximizing joint-kernel coupling while all previous labels matched and all previous state pairs were related. On survival through t, the state pair belongs to R_t. The conditional probability of another good step is at least 1-epsilon_t. On first failure choose any coupling with the correct two marginals. The probability that every step is good is at least the product of the conditional lower bounds. On that event, complete labels match; if terminal ports are included, their declared relation also ensures matching readouts. The finite coupling inequality TV <= P(observed outputs differ) proves (EC37.1). The constant identical outgoing micro-source total M makes each model's depth-n source count sum equal to M^n, yielding the exact count/TV identity (EC37.2). QED.

**Exact finite certificate.** At every state pair build a bipartite flow network. A source points to each first-model joint outcome (l,s') with capacity P_t(s;l,s'); second-model joint outcomes (l',z') point to a sink with capacity Q_t(z;l',z'); a left-right edge of capacity 1 exists exactly when labels agree and successor states are in R_(t+1). Its rational max-flow value equals alpha_t. Restricting any coupling to good edges gives a feasible good flow; conversely a maximum good flow can be completed to a coupling of all residual marginals, and any additional good mass would contradict maximum flow. Thus rational max-flow/min-cut gives an exact checkable certificate without floating-point approximation. EC37_verify.py executes a Fraction-valued augmenting-path implementation.

## 3. Theorem EC37.2 — optimal finite-horizon adapted coupling value

For fixed n, terminal relation and required terminal port match define h_n(s,z) to be 1 if (s,z) is admissible and terminal ports agree, otherwise 0. For t<n set

h_t(s,z) =
  1_{(s,z) in R_t} MAX_(gamma in Gamma(P_t(s),Q_t(z)))
  SUM_{(l,s'),(l',z'): l=l'} gamma((l,s'),(l',z')) h_(t+1)(s',z').

This rational finite-dimensional Bellman recurrence equals the largest probability of preserving the declared relation, complete labels and terminal port under **causal co-adapted couplings**: the coupled transition choice at t depends only on current state pair and operation position. Therefore TV(mu_n,nu_n) <= 1-h_0(s0,z0). For each pair, the maximum is a finite rational transportation LP.

*Proof.* The boundary n is exactly the required terminal port/relation event. At each prior time choose the first-step coupling gamma. On a label match the optimal continuation probability is h_(t+1) at the successor pair; other transitions cannot contribute to success. Maximize the resulting linear expectation over gamma. Backward induction proves optimality among adapted couplings and rational computability. QED.

**Strength boundary:** In general 1-h_0 is a sound bound, NOT equal to true label-only TV. Strong relation preservation can reject a coupled pair whose one-step coarse labels agree. The verifier implements the Bellman recurrence exactly for kernels with at most two aggregated outcomes per row (164 exact cases); a generic large LP solver is not claimed executed.

## 4. Sharpness EC37.3 — every rational defect and every horizon

Fix integers M>=2 and 1<=a<=M. One-state model A contains M distinct micro-source edges, all labelled R. One-state model B has M-a edges labelled R and a edges labelled B. All edges return to their sole state, so alpha=1-a/M. For every n>=0,

**TV_n = 1-(1-a/M)^n**, exactly,

because A gives probability 1 to R^n, whereas B gives it probability ((M-a)/M)^n. Thus EC37.1 is sharp for every n and rational epsilon=a/M, not merely asymptotically. Corresponding exact count distance is

**SUM_w |C_n(w)-D_n(w)| = 2 [M^n-(M-a)^n].**

In particular with any fixed 0<a<M the whole-path error approaches 1 as n grows; single-step error less than 1 by itself gives no uniform small error for unlimited compositions.

## 5. Correlation no-go EC37.4 — identical separate marginals, maximal error after two steps

Let both models have states {O,U,V} and outgoing micro-source total M=2. At O, model A has one R edge to U and one B edge to V. At O, model B instead has one R edge to V and one B edge to U. In both models, U has two R-source edges returning to U; V has two B-source edges returning to V.

The first-step label marginal is R/B = (1/2,1/2) in both models. The first-step successor marginal is U/V = (1/2,1/2) in both models. Yet the JOINT (label,successor) supports are disjoint:

A={(R,U),(B,V)}, B={(R,V),(B,U)}.

Two-step integer source-word counts are

A: C_2(RR)=2, C_2(BB)=2, all others 0;
B: D_2(RB)=2, D_2(BR)=2, all others 0.

Therefore TV_1=0, **TV_2=1**, and TV_n=1 for all n>=2. For the diagonal successor-state relation, alpha_0(O,O)=0, correctly detecting the unsafe information loss. This shows one-step labels and one-step next-state marginals may each be EXACT, while losing their correlation leads to maximal future source-label discrepancy.

## 6. Why the constant source-mass hypothesis matters

Even full normalized-label-word equality for every n does not imply unnormalized source-count equality without a multiplicity invariant. A one-state model with one microscopic R edge and another with two distinct microscopic R edges have identical normalized label path laws (both concentrated on R^n), but source counts are 1 and 2^n respectively. For state-dependent row totals, retain the product of microbranch multiplicities along paths; do not use EC37.2 without the equal constant M hypothesis.

## 7. Actual exact checks, evidence, and reuse

The project note's executed local Python exact verifier is EC37_verify.py, report EC37_REPORT.json. Its computation checks:

- **EC33 actual source reuse:** 2,555 source-label words, H=1..5 and depths 0..8, agreeing with the unmodified pinned EC33_verify.py (the local copy is not treated as a new native source).
- **Rational sharp family:** 35 parameter pairs M=2..8, a=1..M, and 385 depth checks through n=10.
- **Label-successor correlation counterexample:** complete integer word counts and exact total variation for n=0..8.
- **General exact Fraction max-flow:** 140 deterministic-seed random model pairs, 2 states, equal M=6, 980 exact path-TV/product-bound checks through depth 7; 945 were strict inequalities, and all 980 upper bounds were below 1.
- **Exact two-event Bellman endpoint LP:** 164 successful finite-domain checks, including the case where coarse label TV is zero at depth 1 but the more demanding causal relation certificate is conservative.
- **Independent project GitHub JS BigInt run:** EC37_GITHUB_VERIFY.js was run locally and yielded EC37_GITHUB_REPORT.json, PASS; 35 sharp cases, 385 horizon checks, 9 correlation depths, 140 additional kernel pairs, 980 exact bound checks (948 strict). All calculations are integer or exact rational; the JS model pairs are a distinct deterministic family from the Python sample.

The infinite-horizon mathematical assertions are proved by the finite-state coupling and constructive witnesses above, NOT inferred from bounded experiments. Neither full native X6 dynamics, physical heartbeat-time propagation, an unrestricted generic Bellman LP implementation, nor independent mathematical admission is established. This is a finite-state auxiliary BRC observer result conditional on explicit source kernels.

**Next precise problem EC38:** For general finite positive microscopic labelled kernels, construct explicit exact LP dual certificates for h_t (not only the unweighted one-step good flow), and identify structural sufficient conditions under which the optimal adapted coupling bound 1-h_0 equals true label-path TV. A native X6 application must first supply an authorized exact update and microbranch source map, third-coordinate semantics for any declared embedded three-dimensional slice, separately typed time readout, and future-operation-preserving observer bridge.

**Research Activity:** RA-EMR4-20261026-1030-EC37KERNEL. This provenance registration does not grant an active Task CLAIM, Driver review power, or Foundation acceptance.
