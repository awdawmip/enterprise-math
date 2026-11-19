# R762FT — Minimal oriented triad rotation and S6-equivariant signed BRC transport

2026-11-19; status: AUTHOR_PROVED / EXACT_FINITE_VALIDATION_PASS / NOT_REVIEWED.

Mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen taskbook: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Frozen P000 scientific premise: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json and corresponding P000 discrete direction/triadic balance and X6 Cell torsor definitions at that scientific pin. Behavior/current task authority read separately. Continuation: R762FM, FN, FO, FP, FQ, FR and FS; original results remain unchanged.

## Question and domain

The current P000 foundation provides six signed primitive spatial axes, a six-component affine Cell torsor X over Z^6, six-axis native component readout L_E^2=sum_i z_i^2 and an S6 *axis-permutation skeleton*. It fixes primitive stable nonzero balance at triad arity but does not already supply a full legal Cell/Link/Port balance update.

Ask whether a directed order-three generator can be selected from an unordered set of three **distinct** native axes without carrying extra information, while preserving the typed signed Link/Port and source-labeled ordered BRC path carrier.

No classical vector-sum-zero balance criterion is introduced. All formulas below are integral relabeling and typed BRC-path statements. In particular a three-step force closure need not return a spatial Cell.

## The exact candidate carrier

Let T={a,b,d} be an unordered 3-element subset of {1,...,6}. For sorted a<b<d define the two distinct order-three axis permutations
g_+(T)=(a b d), and g_-(T)=(a d b)=g_+(T)^(-1),
fixing the three other axes. An **oriented triad** is the coordinate-free pair (T,g) with g one of these two cycles. The + / - is only the orientation encoding relative to the sorted axis chart.

For σ in S6, act by
σ·(T,g)=(σT,σgσ^(-1)).
Thus the numerical orientation encoding may change under renaming.

Fix an arbitrary local Cell anchor c. Define the candidate rotation on any native Cell z by
R_(c,g)(z)=c+g(z-c).
For the signed primitive Link (c,c+s e_i, source_id), with s in {-1,+1}, transport to (c,c+s e_(g(i)),source_id). A typed BRC path-formal word is an ordered sequence of branches (source_id, signed_native_axis_i, positive_rational_weight, and optional other retained per-branch metadata). Relabel only the axis i->g(i), preserving sign, source IDs, order, multiplicity and weights. Its endpoint functor is end(w)=sum_j s_j e_(i_j), and end(g·w)=g·end(w). No signed cancellation is inferred from positive weights.

A separately typed *candidate* conditional incidence-closure predicate (from R762FM) is C(s,omega) iff omega=product_(i in T)s_i. The incidence bit omega is retained and direction signs follow axes under permutations. C is preserved by this S6 transport. This is one proposed model definition, **not** a proof that Source currently licenses this native event.

## Theorem A — deterministic equivariant selection is impossible without one orientation bit

For every three-subset T, there is no S6-equivariant deterministic map assigning one of its two nonidentity 3-cycle rotations using only the unordered set T. The two-sheeted oriented carrier provides the minimum repair: exactly one additional bit over known T.

Proof: fix T={a,b,d} and let tau swap a,b while fixing d and the remaining axes. tau stabilizes T but conjugates g_+(T) into g_-(T). If g(T) were equivariantly chosen, stabilizer invariance would require tau g(T) tau^(-1)=g(T), false for either candidate. Conversely the action by conjugation defines an S6-set on the exact two-element fiber, and a one-bit choice identifies the selected rotation. This holds even for the all-positive signed triad, so direction-sign asymmetry cannot give a universal deterministic selector. QED.

This bit is **not** R762FM's sign-product incidence bit: the all-positive triad with omega=+ is compatible with both g_+ and g_-.

## Theorem B — exact typed covariance

For every permutation σ in S6, every c,z in X and every oriented g,
σ R_(c,g)(z) = R_(σc, σgσ^(-1))(σz).
Proof: both sides expand to σc+σg(z-c). A permutation relabels each ±e_i into ±e_(σi), preserves sum_i z_i^2 on displacements and maps a signed primitive Link to the corresponding signed primitive Link. Acting letter-by-letter on typed BRC words preserves concatenation, signed flags, source identity, positive rational branch weights and endpoint pushforward. Therefore the finite candidate transport is S6-equivariant on Cells, Links, Ports and the full declared BRC word carrier. Since sign product is insensitive to relabeling, the candidate parity predicate is equivariant. QED.

The three-cycle has order 3 as a permutation and induces an order-3 invertible Cell map around c, but this is not a claim about elapsed heartbeat time or physical dynamical permission.

## Theorem C — sharp source counts and an observer-loss witness

There are C(6,3)=20 unoriented triads and 40 directed-orientation variants; an exact fixed-length label for an unconstrained oriented triad requires ceil(log2 40)=6 bits. Given one known participating axis, choose two among five plus orientation: 10*2=20 options, so 5 bits. Given an **unordered** participating pair, choose a third axis among four plus orientation: 4*2=8 options, so 3 bits. If an application exposes an ordered pair of Ports, that extra observation may already specify cyclic orientation; the above 3-bit statement is for unordered visible-pair data.

For T={a<b<d}, take the all-positive, source-labeled BRC word w=(a,b,d) with three distinct source IDs and retained order. Applying g_+ gives (b,d,a), while applying g_- gives (d,a,b). These ordered named-source words differ. Their endpoints are equal (e_a+e_b+e_d); branch count, positive weights as a multiset and incidence sign product also agree. Hence an observer retaining only T, endpoint and sign-product parity cannot predict the later ordered BRC-path result of the selected directed rotation. The orientation bit is a concrete structural residual relevant to the specified future operation. QED.

## Finite exact evidence

The executable R762FT_VERIFY.mjs covers all 20 three-subsets, both orientations and all 720 S6 permutations. It checks 28,800 conjugacy/orientation equations, 28,800 affine Cell covariance identities on a nontrivial full signed Cell/anchor sample, and 28,800 source-word/endpoint BRC relabeling identities. For each configuration it also enumerates eight sign assignments and two incidence bits: 460,800 closure-truth comparisons. It separately checks 20 subgroup-transposition no-go witnesses and 20 endpoint-equal / ordered-path-different witnesses. All checks PASS. R762FT_EVIDENCE.json records the integer counts; general theorems above have explicit proofs, while the finite evidence independently checks those formulas in six axes. Runtime was the connector's JS/V8 execution environment; source is standalone Node.js without external packages.

## Scope, non-repetition and next research unit

This is a fully specified candidate on the established S6 rotation skeleton and typed, source-retaining signed BRC path-formal carrier. The actual TRIADIC_CLOSURE_E primitive Cell/Link/Port permission, time ordering, failure visibility, and physically admissible rotation subgroup remain open. In particular do not infer from S6 symmetry that a 3-cycle is an automatically *legal dynamical update*. No π/trigonometric or classical propagation reference computation was executed. Author-side proof and exact finite check; independent review NOT_REVIEWED.

Next: inspect current native action/Link/Port authorization definitions and test whether a cyclic order already belongs to the real incidence record (then this orientation bit is stored, not newly required). Derive the actual legal event family and a proven Source-native to candidate-carrier morphism, or produce the minimal witnessed obstruction. Compare observable BLOCK/reset policies only after the legal failure mode is defined. Preserve frozen science pins, P000 and the existing R762FP–FS gate-model results.