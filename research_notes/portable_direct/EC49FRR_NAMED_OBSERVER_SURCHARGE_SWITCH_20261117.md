# EC49FRR — Exact named BRC observer-price switching theorem

Date: 2026-11-17. Continuation of [EC49FRQ PR #2642](https://github.com/awdawmip/enterprise-math/pull/2642), immutable scientific evidence branch head \`350043ef311e2a3fe292f586657386e61ad2854a\`. The frozen original BRC scientific input remains \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Evidence level: **AUTHOR_PROVED / EXACT_FINITE_NATIVE_REPLAY / NOT_REVIEWED**.

## Exact BRC model and changed cost parameter

Preserve the predecessor's original 310 configurations and their 141 complete named-response profile classes, 228 named physical queries (terminal indices 0–143, root indices 144–227), response values, provenance and legal identifying-tree semantics. Every full identifying tree must distinguish all 141 profiles. Original terminal-query price is \`t>0\`; original root-query price is \`x*t\` for real \`x>=1\`. The original prior is

\[
p_i(\lambda)=(1-\lambda)/141+\lambda m_i/310,\quad 0\le\lambda\le1,
\]

where all multiplicities \`m_i\` are positive integers, summing to 310. Costs of a full original tree \`Q\` at the uniform prices obey

\[
C_Q(x,\lambda)/t=(1-\lambda)(U_T(Q)+xU_R(Q))/141+\lambda(M_T(Q)+xM_R(Q))/310.
\]

**New declared cost model:** for a *single named terminal physical observation* \`q\`, increase only its cost by \`\varepsilon*t\` with \`\varepsilon>0\`. No BRC response/relationship is changed. Let \`N_q(Q,i)\` count that named action on state \`i\`'s decision path. Then, exactly,

\[
C_Q^{(q,\varepsilon)}=C_Q+\varepsilon t\sum_{i=0}^{140}p_i(\lambda)N_q(Q,i)\ge C_Q.
\]

This is a decision-theoretic price perturbation on already reconstructed **native BRC actions**, not a new source physics calculation, projection, or quotient of joint-relation observers.

## Full original named witness certificate

The source \`evidence/x1-1_l0-1.json\` in the **complete EC49FRQ archive** contains all unrestricted x=1, lambda=0 Bellman-optimal first named physical actions, **exactly [32,34]**, and the entire corresponding original full trees. Set \`A=all_optimal_first_trees['32']\` and \`A'=all_optimal_first_trees['34']\`; B and C are the *unchanged* original complete named competitors from EC49FRQ's other saved endpoint certificates. Replaying every legal action and its original named response along all 141 state paths (310 configurations by multiplicity) gives:

| Tree | First named query | \`(U_R,U_T,M_R,M_T)\` | Occurrences of q32 (unweighted, weighted) | Occurrences of q34 (unweighted, weighted) |
|---|---:|---|---|---|
| A | 32 | (6,290,6,751) | (141,310) | (0,0) |
| A' | 34 | (6,290,6,751) | (0,0) | (141,310) |
| B | 140 | (5,293,5,704) | (0,0) | (0,0) |
| C | 16 | (5,295,5,685) | (0,0) | (0,0) |

All four complete identifying trees have maximal depth three. In particular A and A' retain **different named original observations** but have the exact same four-class aggregate cost vector. The source unrestricted original Bellman minimum at \`x=1, lambda=0\` is \`296t/141\`; original A/B/C costs at that point respectively are \`296t/141, 298t/141, 300t/141\`.

## Theorem 1 — The fixed named A/B/C optimal menu is fragile at arbitrarily small observation-specific surcharges

At \`x=1, lambda=0\`, for **every real** \`\varepsilon>0\`, if named original terminal action **q32 alone** is surcharged, then **A' is globally Bellman-optimal**, with exact minimum cost \`296t/141\`, and **none of the original fixed named A/B/C trees is optimal**. Under a surcharge instead on named original terminal action **q34 alone**, A is globally Bellman-optimal with the same value.

*Proof.* A nonnegative increase of one query price can never reduce the cost of a fixed tree, hence cannot reduce the unrestricted global optimum below the former \`296t/141\`. Native full-path replays show that A' never calls q32 and A never calls q34, so under the respective surcharges each original full tree attains this old lower bound. Under the q32 surcharge A rises by exactly \`\varepsilon t\` because all original 141 state paths call q32, while B and C already exceed the original optimum by \`2t/141\` and \`4t/141\`. Thus none of A/B/C is optimal for any \`\varepsilon>0\`. QED.

In consequence, the **three fixed named trees** A/B/C have **zero uniform positive stability radius** for unrestricted individual-observer price changes, even when evaluated at one original parameter point. The predecessor's Pareto result remains valid for the original **uniform two-category** price model, where other named trees with the same aggregate cost vector are indistinguishable by the objective.

## Theorem 2 — Exactly two fixed named trees are necessary and sufficient for these two surcharge scenarios

Fix \`(x,lambda)=(1,0)\`. Consider two observation-specific price scenarios, surcharge **q32** alone or surcharge **q34** alone, with arbitrary strictly positive surcharge size (potentially different for each scenario). A menu of the two original full named trees \`{A,A'}\` contains a globally optimal policy in each scenario. **No one-tree menu of a fixed original named full tree can cover both scenarios.**

*Proof.* Sufficiency follows from Theorem 1. As the perturbed optimum equals the *original* Bellman minimum, any tree optimal after a strictly positive surcharge must be original Bellman-optimal **and have zero uses of the charged action** (all 141 prior masses are positive). From the exhaustive original unrestricted Bellman certificate any baseline-optimal tree's first physical query lies in \`{32,34}\`. In the surcharge-q32 scenario an optimal tree cannot start with 32, so it must start with 34; in the surcharge-q34 scenario it must start with 32. No fixed full named tree has both first actions. QED.

This is an exact combinatorial **minimal observer-aware price-policy menu** of cardinality two for the stated pair of perturbation scenarios. It is not an assertion about the smallest possible menu for all 228-dimensional price vectors.

## Theorem 3 — Exact continuous price-prior region with invariant optimum under the two surcharges

Define, for real \`1<=x<=3\`,

\[
\gamma(x)=\frac{310(3-x)}{310(3-x)+141(x+47)}.
\]

On the **entire real parameter region** \`0<=lambda<=gamma(x)\`, both A and A' are optimal at the original uniform two-category price. For any real \`\varepsilon>0\`, surcharging **q32 alone** leaves A' exactly globally optimal with unchanged minimum, and surcharging **q34 alone** leaves A exactly globally optimal with unchanged minimum.

*Proof.* The original full-tree vectors yield

\[
(C_A-C_B)/t=(1-\lambda)(x-3)/141+\lambda(x+47)/310,
\]
\[
(C_C-C_B)/t=2(1-\lambda)/141-19\lambda/310.
\]

The first expression is nonpositive exactly for \`\lambda<=gamma(x)\`. The second is nonnegative for \`\lambda<=620/3299\`. The function \`gamma(x)\` decreases over \`[1,3]\` from \`gamma(1)=155/1847 < 620/3299\` to 0. Hence throughout this region \`A<=B<=C\`. By EC49FRQ's unrestricted original BRC Bellman theorem, \`A=min_Q C_Q\`; A' has identical original \`(U_R,U_T,M_R,M_T)\`. Under either positive surcharge, the corresponding avoiding witness retains the old optimum, and all other trees can only become more expensive. QED.

## Exact verification and dependency trace

Inputs frozen: \`frozen_original_master.txt\` SHA256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`; \`EC49FPG_PROFILE.csv\` SHA256 \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`. In the complete archive \`EC49FRR_named_cost_switch_verify.py\` checks these hashes, reuses the **actual original typed BRC response reconstruction code** from predecessor EC49FRQ, replays all four full original named decision trees on all 141 states, checks all q32/q34 action-incidence totals, maximal depths, original exact global Bellman value and unrestricted first-action set; it also checks several exact rational surcharge and parameter samples. The proof's general quantifiers follow from analytic algebra and monotonicity, not numerical sampling.

Full reproducible current-round archive: \`EC49FRR_NAMED_OBSERVER_PRICE_SENSITIVITY_FULL_EVIDENCE_20261117.tar.xz\`, **230,484 bytes**, SHA256 **\`6eb2a37918a0ab85276afb95b79517b0af3ab76552216833a65d5c52fa4d0f66\`**. This archive includes the inherited complete EC49FRQ raw input, two exact DP checkers, old proof, full original tree witnesses, plus the current full paper, executable verifier and exact JSON certificate. All 22 non-manifest files passed byte count + SHA256 verification after decompressing the final tar.xz.

## New representation requirement and next question

At uniform two-category pricing, the four aggregate counts \`(U_R,U_T,M_R,M_T)\` are sufficient to evaluate a tree. For action-specific prices, the incidence carrier \`N_q(Q,i)\` is indispensable: the four aggregate costs identify A and A', yet the new exact observer-specific costs separate them for every \`\varepsilon>0\`. This is an explicit information-loss witness *within the declared identification-cost future observer*. Preserve named physical observation identity and provenance; do not merge joint-relation actions merely because a coarser cost observer formerly agreed.

Next independent unit: construct a source-faithful integer Bellman oracle for nonuniform prices on all original 228 named observations, then compute the exact finite Pareto incidence vectors and minimal complete menu under a **specified** bounded perturbation polytope. Distinguish this parametric cost-optimization claim from any stronger native future-operation/state quotient, and retain P000, X6, source frozen pin and non-reviewed mathematical status.

Control: independent portable GitHub science; does not assert native Task publication, winning CLAIM, Activity checkpoint, Result, Review or independent mathematical admission.
