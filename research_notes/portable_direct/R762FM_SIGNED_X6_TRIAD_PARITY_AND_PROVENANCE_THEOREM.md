# R762FM — Signed X6 triad incidence: one-bit covariance repair and four-bit provenance obstruction

Date: 2026-11-19 (Asia/Shanghai). Formal mother task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen taskbook: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Frozen foundations: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. Author-side exact reasoning and finite checker: PASS; independent mathematical review: NOT_REVIEWED.

## Research scope

P000 fixes the six native axes, signed primitive ±E_i directions, pairwise PERP_E at the native 120° angle, minimal primitive stable force arity three, and the requirement for typed TRIADIC_CLOSURE_E incidence. The spatial foundation fixes the Cell torsor Z^6 and an S_6 axis-permutation rotation skeleton. It does not establish every signed coordinate reversal as a physically licensed native rotation.

This note investigates an *explicit candidate* extension of that skeleton to the signed relabeling group W_6=(C_2)^6 ⋊ S_6, and proves what information a selective closure needs if it is to be equivariant under that larger test symmetry. It does not replace the native closure or rotation-admission problem.

## Typed three-leg candidate and BRC history

A primitive token is f=(source_id,c,i,s,q), with Cell c in the native Z^6 torsor, native axis i∈{1,...,6}, direction s∈{−1,+1}, positive equal quantum q, and a separately named provenance ID. Its only primitive spatial leg is c→c+s e_i.

An incidence candidate t consists of three such tokens at one Cell, on three distinct axes I={i,j,k}, plus a local incidence charge ω∈{−1,+1}. Define the candidate closure predicate

    C(t) ⇔ ω=s_i s_j s_k.

When C holds, a *candidate* local update consumes the three named force tokens and appends one path-formal fan record containing (c,ω, all three source IDs, and all three separately named legs c→c+s_i e_i). It does not assert that summing three ordinary Euclidean vectors gives zero, or that the incident Cell must return. It carries three primitive paths and full source provenance. The branch fan is a typed BRC-style positive named-branch construction, not a signed-amplitude cancellation algorithm. One or two tokens cannot trigger it; larger stable configurations require decomposition into three-token events.

The charge is an additional **incidence binding**: a mismatched (t,ω) is an unbound candidate, not an assertion that a fully admitted canonical equal-quantum triad has failed P000.

## Theorem A — conditional sign-only no-go

Fix three distinct axes I. Let F:{−1,+1}^3→{false,true} depend solely on their three signs and be invariant under each independent axis-sign reversal belonging to the *candidate* W_6 action. Then F is constant.

Proof: the three sign flips generate (C_2)^3, which acts transitively on the eight sign triples. An invariant predicate is constant on its unique orbit. Thus a nonconstant closed/unbound classification requires additional incidence data if all these candidate reversals are to preserve event status. The established S_6 action alone does not imply this no-go. □

## Theorem B — sharp one-bit repair and Cell/path covariance

For g=(π,η)∈W_6, let its signed coordinate action send s_i e_i to s_i η_{π(i)}e_{π(i)}, act by that affine-linear relabeling on Cells and named legs, and transform the local charge by

    ω' = ω ∏_{i∈I} η_{π(i)}.

Then C(t) iff C(gt), and the three-branch fan update is exactly equivariant under every g∈W_6. The two orbits of the extended signed-incidence data over a fixed axis triple are distinguished by χ=ω∏s_i∈{−1,+1}; χ=+1 is closed. One extra binary label is minimal for a nonconstant equivariant closed/unbound predicate in this setting.

Proof: the product of transformed signs is (∏s_i)(∏η_{π(i)}), which changes by the same factor as ω; hence their equality is invariant. Each endpoint c+s_i e_i transforms exactly into gc+s_iη_{π(i)}e_{π(i)}. Individual source IDs, leg multiplicity, Cell incidence and the closure stamp are carried bijectively. Theorem A rules out zero extra labels, and the displayed construction uses two states. □

Scope: W_6 is a chosen *candidate* covariance group. The actual project admits S_6 as an axis-permutation skeleton; which signed reversals or other rotations are legitimate native operations remains to be determined.

## Theorem C — exact two-visible-leg lift count

Fix two visible signed legs with distinct axes at the same Cell and positive equal quanta; require the hidden third leg to use a new axis. If ω is known, there are exactly **four** typed closed lifts: choose one of the four remaining axes, and set s_k=ω s_i s_j uniquely. If ω is hidden, there are exactly **eight** lifts: for each hidden axis both values of ω provide one corresponding sign. Every lift carries a genuine third primitive branch, so a two-leg readout can arise from a closed three-leg event without any primitive two-force balance. □

## Theorem D — exact ten-to-one provenance collision and sharp four-bit memory

Take six differently named positive-axis force tokens f_1,...,f_6 at one Cell, one for each of the six axes, all equal quantum and positive sign. Give each three-token event charge ω=+1. The number of partitions into **two unordered closed three-token events** equals

    (6 choose 3)/2 = 10.

Every branch has the same unordered multiset of six primitive terminal legs, so the aggregate endpoint observer identifies all ten. However, the future query Q_1(history) asking for the two IDs sharing the triad with f_1 returns one of the (5 choose 2)=10 distinct partner pairs. Each partition is uniquely determined by that pair, so all ten histories are distinguishable. A fixed-length deterministic code preserving this query in addition to the shared endpoint readout requires at least ceil(log₂ 10)=**four bits**, and four bits suffice by enumeration.

Proof: choose exactly two of the remaining five tokens to share f_1's triad; the complement is the other triad. No two such choices produce the same partition or Q_1 answer. By the pigeonhole principle, fewer than ten codes cannot preserve all ten distinct answers, while sixteen codes can. □

In exact Path-FORMAL / named positive BRC terms, the branch family is Σ_P[b_P] over all ten partitions, with an endpoint-only pushforward 10·[same aggregate six-leg observation]. Weight ten preserves total multiplicity but not the event-grouping source relation. This four-bit bound is scoped to the stated ten branches and partner-query future operations, not all possible X6 states. Ordered event histories may carry further distinctions.

## Executed checker and coverage

The companion standard-library Python checker enumerates all 20 distinct three-axis selections, eight sign patterns and two incidence tags: **320 configurations**, exactly 160 closed. It checks the closure predicate and named three-leg endpoint covariance under six independent sign-flip and five adjacent-swap generators: **3520** generator checks. Those eleven generators generate W_6, hence the algebraic proof covers the entire candidate group. It checks all eight sign patterns are a single sign-flip orbit, all four/eight two-leg lifts, all ten six-force partitions, ten distinct partner queries and the four-bit inequality. The actual finite run output is R762FM_EVIDENCE.json, with checks=PASS. Computations are exact discrete typed BRC-branch incidence combinatorics; no π or classical trigonometric physics input.

## Source status and next discriminating steps

This note is an independent portable research candidate with a precise finite validation, NOT_REVIEWED; publishing its GitHub bytes does not establish a native source CLAIM, accepted Result/Review, or physically admitted TRIADIC_CLOSURE_E.

1. Compare the one-bit incidence charge and named three-branch fan with actual signed Cell/Link/Port operation licences; locate an explicit admissible map or the exact unmet port/incidence predicate.
2. Determine which actual native rotation generators beyond S_6 are permitted, rather than assuming W_6. Retain the conditional no-go at its established covariance scope.
3. Classify future queries under which the ten-event grouping may be safely quotiented, and characterize retained source fields for the remaining queries.
4. Preserve the parallel R762FL ramified positive q9 BRC character-period work under its separate observer and evidence scope.

Files in this PR: complete theorem/proof note, executable R762FM_VERIFY.py, and exact execution output R762FM_EVIDENCE.json. Frozen scientific inputs are unchanged.