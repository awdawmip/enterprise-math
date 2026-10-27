# R5 / EC48I-2 — An exact second supporting normal in the reverse-collision BRC tree

**2026-10-27. Author-side research; UNREVIEWED / NOT_ADMITTED.** This is an external, finite, strictly positive two-measure BRC observation problem, not native X6/Heartbeat mechanics or a formally accepted Enterprise Math Result.

## Authority and scientific sources

Global canonical knowledge snapshot fixed for this unit: awdawmip/chatgpt-global-knowledge **main@ad4f63878ca0534cdd52af1c5590bff3a777ab08**, whose P000 original Git blob is **770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc**. P000 (six native spatial axes, independent time, three-dimensional research slice, relation and residual preservation) stays locked and is not recast as an external two-measure tree.

Project source: awdawmip/enterprise-math **main@f3b1cff2be50a4c77576894d71562eb7fd78068f**; current portable research and ownership policies were consulted. Mathematical parent: immutable commit **a5e3add6096c1b2f9fc9adeb9c546acfd4db831e**, research_notes/r5_ternary_global_phase_20261027_t11/PROOF.md and NEXT_TASK.md. That proof gave an exact phase diagram for one signed normal but did not exclude (s_a,s_b)=(1/10,2/5). Newest R5 penultimate hinge theorem in main@f3b1cff is for *compulsory* arrival; it does not remove early-stop optimization in this model.

## Model, observer, and BRC interface

Root at t=0 has Q mass 1 and likelihood ratio L=P/Q=1. The nonterminal histories have (Q,L,t):

| h | Q | L | t |
|---|---:|---:|---:|
| a | 1/2 | 3/2 | 1 |
| b | 1/2 | 1/2 | 1 |
| ax | 1/4 | 1 | 2 |
| ay | 1/4 | 2 | 2 |
| bu | 1/8 | 1 | 2 |
| bv | 3/8 | 1/3 | 2 |

The only collision among distinct nonterminal physical histories with the same (t,L) is ax~bu. At ax and bu the terminal LR alphabet is (1/2,1,3/2) with conditional Q kernel K_s=(s,1-2s,s), with parameters s_a and s_b respectively; ay and bv have one terminal child of unchanged LR. For all 0<s_a,s_b<1/2, every terminal branch has positive Q and P mass. Both source measures conserve mass because sum K_s=1 and sum LR*K_s=1.

At any history a policy can stop and decide P or Q, or continue to the next observation. A full-history behavioral policy can distinguish ax from bu. A **seedless** time/LR policy must use a common action distribution at ax and bu, with fresh private local randomization and no persistently shared random seed.

Define the four observables
  O=(P[decide Q], Q[decide P], E_P[tau], E_Q[tau]).
BRC use is the actual positive weighted-branch interface, retaining predecessor provenance, two source masses, LR and future observer. This result does not identify positive mass with phase/amplitude cancellation. Native X6 transfer still requires an explicit typed embedding, third-slice-coordinate semantics, readout and relation-preservation proof.

## Theorem — a constant quarter-unit gap on an open rectangle

Let J(O)=298 O_1 + 376 O_2 + 37 O_3 - 17 O_4, and V_full,V_seedless be its respective minima. Then for **every real pair**

  0 < s_a < 19/71,     22/71 < s_b < 1/2,

the exact identities are

  V_full = 1135/4 - (71/8)s_b,
  V_seedless = 284 - (71/8)s_b,
  V_seedless - V_full = 1/4 > 0.

Consequently the full and seedless attainable four-vector sets have **different convex hulls** throughout this region. At the rational pair (s_a,s_b)=(1/10,2/5), the previous normal (298,375,37,-17) had a zero support gap, but the above neighboring normal separates strictly. One tested normal is not a hull-equivalence certificate.

### Complete backward proof

At a node with Q mass q, LR r and time t, a stop-Q decision costs

  q [298r + t(37r-17)],

while stop-P costs

  q [376 + t(37r-17)].

At final LR values (1/3,1/2,1,3/2,2), optimal terminal decisions are (Q,Q,Q,P,P), respectively. The terminal decision at a given LR is independent of predecessor and can therefore be shared by the compressed policy. Using those exact labels gives the complete t=2 local table:

| History | Best immediate stop | Continue to optimal terminal decision |
|---|---:|---:|
| ax | stop Q: 169/2 | 179/2 - (71/4)s_a |
| ay | stop P: 245/2 | 547/4 |
| bu | stop Q: 169/4 | 179/4 - (71/8)s_b |
| bv | stop Q: 135/4 | 32 |

For ax and bu, the other stop label costs 104 and 52 respectively and is dominated. In the claimed rectangle, ax strictly prefers stop Q (because s_a<19/71<20/71), bu strictly prefers continue (since s_b>22/71>20/71), ay stops P and bv continues.

At a, immediate stop P costs 829/4, whereas continuing with ax stopping Q and ay stopping P costs 207. Hence full history continues at a. At b, immediate stop Q costs 301/4, whereas continuing with bu and bv continued costs 307/4-(71/8)s_b. This is less than either b stopping or continuing with bu stopped Q throughout the rectangle. Therefore continuing root,a,b and applying the four optimal t=2 choices costs

  207 + 307/4-(71/8)s_b = 1135/4-(71/8)s_b.

Root stopping costs at least 298. This is the full-history Bellman minimum.

For a compressed policy, condition on the *single* shared ax~bu action. All other actions are separately Bellman-optimal:

| Shared action | Global optimum conditional on it | Relevant upstream actions |
|---|---:|---|
| stop Q | 1125/4 | a and b both continue |
| stop P | 565/2 | a stops P, b stops Q |
| continue | 284-(71/8)s_b | a stops P early, b continues |

For the third row, continuing at a would cost 212-(71/4)s_a, whereas stopping at a costs 829/4. Because s_a<19/71, stopping a is strictly cheaper; ax is never reached, which is allowed although the shared action remains assigned continue. Continuing b costs 307/4-(71/8)s_b. Since s_b>22/71, the third row beats 1125/4 as well as 565/2. Root stopping also loses. This proves the seedless optimum.

For a linear objective behavioral policies have the same minima as deterministic action tables. Each (time,LR) class occurs at most once on any path, so independently presampling fresh local actions expresses any behavioral *expected linear value* as an average of deterministic class-policy values. This does **not** assert that the raw behavioral attainable region is convex. The three shared-action cases therefore exhaust the support minimum. Subtracting the two formulas yields the gap 1/4. QED.

## Explicit rational separating certificate

At s_a=1/10, s_b=2/5 an optimal full policy continues root,a,b,bu,bv, stops Q at ax and P at ay, and at time 3 decides by the LR labels above. Its complete four-vector is

  O_full=(17/40, 3/10, 9/4, 5/2),  J(O_full)=1401/5.

An optimal seedless policy continues root,b,bu,bv, stops P at a, and assigns the shared ax~bu rule continue (unreached ax included consistently). Its four-vector is

  O_seedless=(7/40,11/20,3/2,2), J(O_seedless)=5609/20.

Every seedless policy has J>=5609/20, while a full policy attains 1401/5, with exact rational gap **1/4**. For previous normal (298,375,37,-17), independent Bellman recurrence gives both minima 2799/10 at this same pair. This is a strict four-observer **support** separation, not an unproved nonconvex-image argument.

## Reproducible exact checking and proof coverage

The accompanying actually executed standard-library Python file VERIFY.py uses fractions.Fraction and affine triples (constant,s_a coefficient,s_b coefficient). It symbolically checks all P/Q parent-to-child conservation identities, terminal Bayes label dominance, 2187 full-history and 729 seedless deterministic nonterminal action tables. Every strategy's objective is affine in s_a,s_b, because no path contains both variable collision kernels. For each of these 2916 tables the code checks the candidate analytic optimum inequality at all four rational vertices of the closed parameter rectangle [0,19/71] x [22/71,1/2], **11664 exact comparisons**. Affine nonnegative differences on every vertex imply nonnegative differences on the entire rectangle, so this is a complete continuum certificate rather than empirical parameter sampling. The actual strictly positive theorem concerns the *interior*, not endpoint positivity.

The executed script also independently sums P and Q stopping masses for both explicit four-vector witnesses and checks previous-normal equality. It prints a reproducible report to EXACT_OUTPUT.txt. This exact checker confirms the direct Bellman proof; program execution alone does not establish native physics, independent mathematical review or Source Result admission.

## Research continuation and administrative status

The pair (1/10,2/5) is **excluded** from convex-hull equality by a second exact support functional; full facet enumeration is unnecessary merely to reject that candidate. Outside the union of the known separating regions, the all-support-equality and raw-image equality questions remain open. The next task is in NEXT_TASK.md.

Research contribution is an author-side portable derivation. Connected GitHub persistence/readback, when completed, constitutes artifact storage only. This document is not a native Source activity registration, live owner CLAIM, frozen Result or independent Driver acceptance. Preserve existing task ownership and the immutable original evidence.