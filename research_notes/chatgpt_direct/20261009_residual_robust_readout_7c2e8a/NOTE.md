# Residual algebra: schedule-robust readouts with non-unique current relations

Progress-Event-ID: EM-20261009-RESIDUAL-ROBUST-READOUT-7C2E8A
Status: CONDITIONAL_PROOFS_AND_EXECUTED_BRC / UNREVIEWED / NOT_NATIVE_DYNAMICS
Logical-conversation: chatgpt-six-axis-minimal-perturbation-20261007-7c2e8a
Global-read: 7b9eb1223c4139523fa4abb0b663fdcbf02e9273
Source-read: a80c1772a95ed4705bb83e84b6c383aa6b88b71a
Activity: REGISTER_PENDING_PLATFORM_BLOCKED_NO_RETRY; no new RA/session/researcher ID
Parent: EM-20261009-RESIDUAL-ORDER-7C2E8A

## 1. Scope and unchanged inputs

This continues the previous order-dependent five-target example. It does not repeat the old order-commutation suite or treat old contributors as independent reviewers. On a finite occurrence inventory I, a current state J is a family of pairwise disjoint triples. reserve(D) adds D if all its members are unoccupied, otherwise keeps the state and a blocked outcome. release(b) removes the unique current triple containing b, or does nothing if b is free. All executed operations use the unchanged pinned membership kernel and its positive CWM BRC dependencies.

Occurrence IDs, modules, occupancy bits, library size and command counts are NOT native spatial axes, final Cell addresses, energy, force or physical time. The added triple K below is a declared extension of this TEST_ONLY library, not a new primitive update rule and not a proven native closure. P000, the six axes, PERP_E, 120 degrees, the specified squared-length readout and protected worldview remain unchanged.

The actual current source definition P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, blob f95fd7a935ce16c875ac2756b299dfe2b7d9c8e5, distinguishes triadic arity from the legality of concrete Cell/direction closures. It supplies no license to assert that this particular K is a physical force event. No repository-wide absence claim is made.

## 2. General target-blocking certificate

Fix an initial state J0 and a finite list H of distinct candidate triples, each attempted exactly once in arbitrary order, with no releases during the list. Remove candidates meeting U(J0); call the remaining initially available family H0. The inherited schedule theorem says that the possible selected families are exactly the maximal disjoint subfamilies of H0. Maximal means inclusion-maximal, not maximum cardinality.

Let t be initially free and H_t={h in H0:t in h}. Then:

Every complete ordering occupies t
iff
there is NO disjoint family M contained in H0\H_t whose union meets every h in H_t.

Proof. If a maximal selected family leaves t free, it contains no h in H_t. Each such h must meet a selected event, otherwise it could still be added. This gives M. Conversely, start with any such M and extend it to a maximal disjoint family using only H0\H_t. All h in H_t remain blocked by the original M, so the extension is maximal in all H0 and leaves t free. Attempt its selected events first to obtain an explicit failing order. If H_t is empty, the empty M is a valid certificate; if t is initially occupied, it is already robust under reserve-only updates.

A certificate can always be reduced to at most |H_t| events: for each h choose one intersecting event from M and retain only the selected witnesses. They remain disjoint. Thus only competitors that meet some target-containing candidate are needed for a failure certificate. This is a local input restriction for this theorem, NOT a general efficient algorithm or a spatial locality law.

For a finite set T of initially free targets, all targets are occupied in every complete ordering iff the above certificate is absent for every t in T. This exchanges two universal quantifiers; it is not an inference from positive marginal response probabilities.

The checker verifies the criterion for all 4,845 four-event libraries on six occurrences, with 29,070 target questions and independently represented maximal assemblies from the original BRC algebra. An additional occupied initial state checks initial availability filtering. This is a finite implementation test; the proof above provides the general statement.

## 3. One complementary triple repairs the old competition

The inventory is I={1,...,36}; the initial source event is A={1,2,3}. Targets are T=(7,13,19,25,31). The retained old candidates are:

G1={1,7,13}; G2={2,19,25}; G3={3,31,32}; H={1,7,19}.

A control keeps A; a treatment executes the same actual release(1) as before. Every subsequent candidate is attempted in the same order in both runs. In the control, every candidate meets the still occupied source A and is blocked.

The old treatment has a bad maximal family {H,G3}, leaving 13 and 25 free. Add exactly:

K={2,13,25}.

The four candidates G1,G2,H,K have two disjoint pairs: {G1,G2} and {H,K}. Every event in the first pair conflicts with every event in the second. G3 is disjoint from all four. Whichever of the four is first selects its side, whose other member remains available and will be selected; the opposite side is blocked. G3 is always selected.

Hence ALL complete orderings end in exactly one of:

J_L={G1,G2,G3}; J_R={H,K,G3}.

Their full occupied occurrence sets are identical:

U_*={1,2,3,7,13,19,25,31,32}.

Both have three active events and occupy all five targets. The control target vector is 00000; the treatment vector is 11111. Thus the paired joint response mask is 11111 for EVERY order. No uniform-order assumption is needed for this universal conclusion; any probability law supported on these complete orders gives theta=1.

All 120 orders were executed with complete paired intermediate traces. The uniform-order diagnostic uses each initial schedule weight once, not its square. Each internal terminal structure has C=60, W=1/2, M=1/120. The merged five-target response has C=120, W=1, M=1/120. Uniform scheduling is a diagnostic distribution, not a native probability law.

## 4. Minimality and uniqueness are precisely scoped

Keep the four old candidates, allow only additions, add one distinct triple from I, and require the new triple to meet A so that it remains source-gated in the control. Under these restrictions K is the UNIQUE repair, and one additional candidate is the minimum possible number.

Proof. Zero additions retains the old failure. Consider an order putting H and G3 before every other candidate. They are disjoint, so both form in the treatment. G1 and G2 are now permanently blocked, and targets 13 and 25 remain free. The one added triple must therefore contain BOTH 13 and 25 and be disjoint from H and G3. It must also meet A. Members 1 and 3 are occupied by H and G3 respectively, so its only possible source member is 2. Therefore it must be {2,13,25}. Section 3 proves sufficiency.

The original BRC assembly enumerator evaluated all 1,680 source-gated, nonduplicate single-addition candidates in the fixed 36-member inventory. K alone succeeds. Every other candidate has an explicit failing complete order, which was also executed. This does not prove minimal physical disturbance, energy, duration or edit distance under different allowed changes. Deleting H, changing the order rule or adding new primitive operations would be different optimization problems.

## 5. Stable readout does not erase the relation residual

J_L and J_R have the same entire occupation and event count, but they are not the same current state. Apply the SAME next command release(7):

J_L -> {G2,G3}, target readout 00111;
J_R -> {K,G3}, target readout 01011.

In the first case 13 is freed and 19 remains occupied; in the second 19 is freed and 13 remains occupied. Therefore the equal-occupation projection is safe for this completed forward target question, but not for the enlarged future language containing release(7) and target observations.

On just this two-element terminal family, a single binary relation label rho distinguishing J_L and J_R is sufficient to reconstruct the full current J and hence initialize any subsequent inherited operation. It is necessary because the above future experiment distinguishes the two states. This is one bit for this known terminal family, not a claim that arbitrary future states or all six-axis systems forever need only one residual bit.

So residual-aware algebra can have an exactly stable coarse readout while retaining nonzero relational distinctions. No scalar correction to integer multiplication or the given squared-length formula has been established or required by this example.

## 6. More candidate events is not automatically a repair

After adding K, add another source-gated candidate L={1,2,7}. The order L,G3,G1,G2,H,K reaches {L,G3}; the target vector is 10001. L blocks all four cross-pair candidates. The universal guarantee is lost even though another apparent route was added.

All 720 orders of this six-candidate library were executed. Under uniform diagnostic scheduling, 576 give full response and 144 give 10001. No claim is made that these artificial probabilities describe native physics. The point is structural: one must eliminate all relevant blocking certificates, not merely add connections.

## 7. Availability and scheduling uncertainty remain separate

Suppose K has a declared independent availability flag with probability q; when unavailable its scheduled attempt is skipped. The old candidates are all attempted. With uniform complete ordering of the five named attempts:

theta_uniform(q)=2/3+q/3.

Conditional on K available the response is always complete. Conditional on it unavailable, the relative order of the four old attempts is uniform, retaining the inherited 2/3 diagnostic. For any fixed ordering, response probability is either 1 or q; an H-first ordering attains q. Thus the worst fixed-order guarantee is q, not 2/3+q/3. This distinction requires the declared flag law and completeness assumptions; it is not a native reliability law or physical clock.

The checker evaluated q=0,1/4,1/2,3/4,1 by positive BRC branching, retaining missing-route and blocked branches. It also validates total W=1. At q=0 the coefficient is CWM_ZERO, not an illegal positive edge of weight zero.

## 8. Execution, source provenance and control limits

The completed checker has 83,224 assertions and 23,403 actual inherited full_step calls. BRC calls: cwm_edge 1,937; cwm_propagate 145,978; cwm_recoalesce 138,791. Source pins:

membership be1b60446e31c2c8489d1ce0db16cc1e952d11c8;
triad 662755ef82c2f433ca57da76b4ce44d63a407612;
packet_router 7465f5aa16cbb8fba61ba4be80f8a6884b879c53;
brc_weighted 3f205696709e847909958a153f8fe10d3f6b70f0.

All 19 files in the inherited order package manifest were checked before reuse. Only its dependencies were imported; no inherited main suite was run. The first new checker run encountered a typing error in its expected-value diagnostic when it tried to construct cwm_edge(0). The old kernel correctly rejected it. The new checker was corrected to use CWM_ZERO; no inherited kernel was changed. Two subsequent isolated successful runs (including a distinct hash seed) produced byte-identical results and logs. This is same-author replay, not independent review.

results.json: 661669 bytes; SHA256 dd15774dc2a947c268da82ed7eb823803d70fc88e549c4366ee4672c649bae00. It contains all 120 repair traces, every proposed single repair and a failure selected-family for each rejected candidate, plus criterion and larger-order summaries. Large complete test transcripts are regenerable; not every in-memory checker object was serialized.

The session_start attempt residual-robust-session-20261009-7c2e8a was blocked by the platform BEFORE creation of an Issue. It was not retried through another transport; no old session or RA was borrowed. Registration and native PRE_FINAL are pending, not passed. Scientific artifact preservation is separate and confers no Task, CLAIM, Result, mathematical admission or Working Truth.

## 9. External context and native next question

Official arXiv:2211.01945v1 (Balliu/Brandt/Kuhn/Olivetti) describes maximal hypergraph matchings and sequential greedy construction. Official arXiv:2103.00729v1 discusses causal dependencies, conflicts and abstract processes in Petri nets. Only metadata and abstracts were read. No unexamined full-text theorem, distributed-round bound or physical timing claim is imported. General matching/concurrency theory is not claimed as a new invention.

The dedicated query on Issue3522, batch cbba6ce2-8af9-4ca3-a7de-e406ef304753, completed with one arXiv metadata/abstract result. Its request digest 11ff5e64ed02f09789fa2eca893725e97af3f0e1c31270c7ad2fccdfddf5b155 matched intake and result; retrieval_verified=true, provider total unknown. Full-text access and independent verification were not established by this receipt.

Next native question is now narrower than merely asking for a generic force law: does a sourced native configuration support BOTH complementary triadic decompositions, with the required action/reaction and six-axis readout correspondence? If only one decomposition is legal, this repair cannot be imported. If both are legal, check that every permitted completion covers the targets and retain the relation choice for later operations. No new native triple, scheduler or release law has been inferred from a convenient test.
