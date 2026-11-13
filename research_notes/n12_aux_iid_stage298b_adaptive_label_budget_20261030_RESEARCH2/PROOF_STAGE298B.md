# Stage298-B — Adaptive future queries double the optimal two-label source-conditioned TV risk

**Research status (2026-10-30):** PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an external, finite, source-labelled, positive-rational BRC observer model. It is not a P000 native X6 theorem, physically calibrated heartbeat statement, Source Result or independent review.

**Fixed source inputs:** GLOBAL_KNOWLEDGE_V1 canonical main@a725c591052bc9f146a6f27abc75030181d6da26; Enterprise Math canonical main@b8853d39eeb8a38cff2ba77a0fc3d19a452cfeaf; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; ACTIVE residual-fidelity worldview, six native spatial axes plus separately typed time, joint-relation observer preservation, weighted BRC, current portable research protocol. The global P000 startup projection pins an older blob, so the original source was inspected. Previous Stage297-B frontier: e460996065ecbeba2b977cac717855297062ec47; existing Draft PR #1736.

## 1. Finite observer, information budget and full source model

Three original source identities S=0,1,2 have equal weight w_s=1/3. A deterministic compression map ell assigns at most k internal memory labels to these three identities before any observation. The simulator receives ell(S), its visible history and arbitrary private causal randomness, but never the original S. The examiner chooses each action solely from previously visible outputs/actions; its randomization is independent of S and of the simulator seed. The *scoring observer* preserves the original source identity as a provenance tag and the entire time-ordered public path. Here the horizon is one initial output A and one adaptive action a followed by output Y. Score:

R_pi(ell,Q) = (1/3) sum_{s=0}^2 TV(P_s^pi, Q_{ell(s)}^pi).

R_ad(k) = min_{ell,Q} max_{visible-history-adaptive pi} R_pi(ell,Q).
R_fixed(k) restricts the examiner to one fixed second action B or C, independent of A, with the same simulator class.

The complete original positive-rational path model is:

* For source 0: initial A=0 or A=1 with mass 1/2 each; either second action B or C deterministically emits Y=0.
* For source 1: initial A=0 or A=1 with mass 1/2 each; B emits Y=1 only when A=0, while C emits Y=1 only when A=1. All other second outputs are 0.
* For source 2: initial A=2 with mass 1; either second action emits Y=0.

The observable terminal path is the complete triple (A,a,Y). The original BRC-style branch tags are (source, initial U branch, action, output); all actual branch masses are strictly positive. In particular source 0 and 1 have the *same* initial observable A distribution.

## 2. Sharp theorem: adaptivity costs exactly 1/6 under a two-label budget

**Theorem.** For the finite model above, with all unrestricted causal randomized simulators and k=2 deterministic memory labels,

R_ad(2)=1/3,  R_fixed(2)=1/6,  R_ad(2)-R_fixed(2)=1/6.

The optimum is global over the complete simulator class, not just a parametric family or grid.

**Pairwise lower certificate.** Since three sources are assigned at most two labels, a distinct pair i,j must share one label. For every fixed examiner policy, the simulated visible path law Q is the same for these two sources. The triangle inequality yields

(1/3) TV(P_i^pi,Q^pi) + (1/3) TV(P_j^pi,Q^pi) >= (1/3) TV(P_i^pi,P_j^pi).

The third source contributes nonnegative error. This proof covers stochastic causal simulators of any internal memory size; it does not require Q to be deterministic.

**Simultaneous upper certificate for each pair+singleton partition.** Give the merged pair one label and the remaining source the other. The merged-label simulator samples a private fair persistent selector T in {i,j} before the first observation and thereafter uses the exact original source process of T under whichever public actions occur. This is *one* valid causal simulator for all adaptive policies, not a policy-by-policy fitted Q. For every policy its induced public law equals (P_i^pi+P_j^pi)/2. Hence TV(P_i^pi,Q^pi)=TV(P_j^pi,Q^pi)=TV(P_i^pi,P_j^pi)/2. The singleton is simulated exactly. The pairwise triangle lower bound is thus attained **simultaneously for all examiner policies**.

**Exact distances for the three possible merged pairs.** Sources 0,1 have identical A laws. With the nonadaptive action B their differences occur only on A=0, with source 0 reporting Y=0 and source 1 reporting Y=1, so TV=1/2; fixed action C similarly exposes TV=1/2 at A=1. With adaptive policy a(0)=B, a(1)=C (a(2) arbitrary), source 0 always reports second Y=0 and source 1 always reports Y=1. Their full path supports are disjoint, giving TV=1, which is maximal. Sources (0,2) and (1,2) already have disjoint A supports, because A is in {0,1} versus A=2, so their TV is 1 for every action policy.

Consequently, the three pair+singleton partitions have worst adaptive source-weighted errors (1/3,1/3,1/3), whereas their worst nonadaptive errors are (1/6,1/3,1/3). If all three sources merge into one label, a merged pair still yields the same rigorous lower bound. The explicit pair+singleton midpoint simulators reach the least of the three upper bounds. Therefore R_ad(2)=1/3 and R_fixed(2)=1/6. QED.

**Observer meaning.** Equality of the current A marginals is not future-equivalence: the action can route each A branch to a different hidden relationship. A source-blind or fixed-action compression that discards the joint A-to-B/C response table loses information measurable by adaptive future operations. The evaluation must keep the original source tag rather than pooling it away.

## 3. General exact finite LP for each fixed label assignment

**Proposition.** Fix a finite source set with rational weights, rational original source-conditional causal kernels on a finite action/output tree, a fixed deterministic label assignment ell, and arbitrary free randomized *causal* response kernels with full visible-history recall and hidden simulator randomness. For source-independent visible-history-adaptive examiners, the minimum worst-examiner original-source-weighted total variation is the value of a finite rational linear program. A worst examiner can be taken deterministic.

**Proof and explicit LP.** For each label l and counterfactual interleaved action/output prefix h, introduce q_l(h) as its probability when those actions are interventions. Impose q_l(empty)=1, q_l(h)>=0, and for every allowed action a at prefix h,

sum_{y in outputs(h,a)} q_l(h,a,y) = q_l(h).

This defines a finite polytope of *realization flows*. Conversely, for every positive q_l(h), ratios q_l(h,a,y)/q_l(h) define conditional response probabilities. At zero-mass prefixes set arbitrary normalized kernels. Thus the flow polytope is exactly the set of all allowed randomized causal simulator laws; it already includes persistent private simulator seeds, which can be integrated out without losing visible path consistency.

For each deterministic contingent examiner policy pi, let L_pi be its finite set of allowed terminal action/output paths. Let p_s(h) be the fixed rational original counterfactual probability of h in source s. Under pi, terminal probability for a compatible path h is q_{ell(s)}(h). Introduce nonnegative slack t_{s,pi,h} satisfying

t_{s,pi,h} >= p_s(h)-q_{ell(s)}(h);
t_{s,pi,h} >= q_{ell(s)}(h)-p_s(h).

For every deterministic pi impose

r >= (1/2) sum_s w_s sum_{h in L_pi} t_{s,pi,h}.

Minimize r, subject to the flow and slack constraints. At optimum the slacks can equal the exact absolute path differences, giving the precise TV value. Every randomized examiner can be realized by sampling in advance a full deterministic action policy independently of the two processes; both path laws then use the same mixing coefficients. Convexity of TV shows its weighted risk is bounded by the maximum risk of a deterministic policy. Therefore the program handles all randomized visible-history-adaptive examiners, not just a sampled subset. Finite rational LP data give an exact rational optimum/certificate (after standard rational primal-dual verification). QED.

For variable strict budget k, one exact finite method is to enumerate source-to-label maps with at most k labels and solve this LP for each. An equivalent mixed-integer representation can be used. No polynomial complexity, single small LP for variable labels or native BRC implementation is claimed.

## 4. Persistent seed does not itself force nonlinearity; constrained shared IID ports do

The previous LP permits unrestricted causal response kernels and private persistent seeds. In contrast, a **restricted** two-visit shared Bernoulli port first chooses Theta in [0,1], then emits two conditionally independent Bernoulli outputs with that same Theta. Arbitrary pre-randomization gives moments m1=E[Theta] and m2=E[Theta^2]. Their **exact** feasibility region is

0 <= m1 <= 1; m1^2 <= m2 <= m1.

Necessity follows from nonnegative variance and Theta^2<=Theta. For m1>0, choose t=m2/m1 and lambda=m1^2/m2. The distribution lambda*delta_t+(1-lambda)*delta_0 is well-defined, since t<=1 and lambda<=1, and has the required moments. For m1=0 the only possible second moment is m2=0. Thus all of the displayed region is feasible, including boundary cases.

Each point (t,t^2) for 0<t<1 is extreme: zero variance forces Theta=t almost surely and cannot be obtained as a nontrivial mixture of different feasible moment pairs. There are infinitely many such distinct extreme points, whereas a bounded polytope has only finitely many. Therefore the exact feasible shared-IID-port region is convex but **not polyhedral**, including after arbitrary global pre-randomization. No finite system of linear inequalities with finitely many auxiliary variables can project to exactly this whole set, because linear projections of polytopes are polytopes. This nonpolyhedral feasibility theorem alone is *not* a proof of a positive objective-value gap for the specific adaptive source model of §2.

The distinction resolves a tempting but incorrect shortcut: arbitrary hidden-seed causal simulation remains an LP at fixed labels, while conditional-IID restrictions impose moment geometry, not an inherently nonconvex random-seed problem.

## 5. Verification, BRC reuse, context and successor

The exact Python Fraction verifier REPRO_STAGE298B.py actually enumerated all 8 deterministic policies (2 actions after each of 3 A values), both fixed policies, all 3 merged-source pairs and 40 positive source-tagged leaf occurrences. It checks every policy's source-normalized mass, exact pairwise lower-vs-midpoint-upper equality, and the optimal values 1/3 vs 1/6. Its stdout ends STAGE298B_ADAPTIVE_TWO_LABEL_EXACT_PASS. Five rational IID moment points corroborate the algebraic boundary. The general LP proposition and infinitely-many-extreme-points result rest on proofs above, not on finite enumeration; no external mathematical checker was run.

BRC reuse: definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json, interpreted under the exact positive source-weight / branch / ordered history / provenance carrier, REUSE_APPLIED. The existing original-to-observer distinction and the Stage292-B/293-B preservation frontier are reused at their explicit model scope. No phase cancellation, native spatial reduction or X6 branch correspondence is asserted. The Fraction script is an example-specific checker, not a promoted shared toolbox family.

External methodological reference: Bernhard von Stengel, “Efficient Computation of Behavior Strategies,” Games and Economic Behavior 14 (1996) 220–246, DOI 10.1006/game.1996.0050, on sequence-form linear realization plans for perfect recall. Related mixed-vs-behavior strategy equivalence is classical (Kuhn). This note makes no novelty claim for general sequence-form theory, just the precisely specified finite BRC-style source-TV comparison.

Next open Stage299-B: optimize the same source-conditional adaptive TV objective when the simulator is restricted to a physically declared shared-Bernoulli parameter interface with arbitrary pre-randomization. Prove either a small strictly positive rational *risk* gap against the free-flow LP or a nontrivial exact no-gap class; include explicitly the policy's visibility of the hidden parameter or seed. Separately require a native X6 model bridge with signed one-axis steps, branch IDs/multiplicity, triadic closure, separately typed time and future-observer commuting tests. Stage278-A Bellman N=12 remains separate.

**Owner/authority verification (2026-10-30):** private Sites service 0.6.11 reported research_authority_granted=false, registered_session_count=0, CODE_REVIEW_REQUIRED and new control quota 5/5; the attempted read of em_control_tasks returned CONTROL_QUOTA. Active Owner and any current CLAIM therefore remain unverified. Source promotion, signed Result and independent Driver review were not performed. Github draft evidence is durable author work, not formal Task completion.
