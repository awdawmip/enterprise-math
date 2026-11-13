# R762S — Typed V29 three-PASS lift of R762R, exact BRC phase fibers

Status: **AUTHOR-SIDE EXACT CANDIDATE / NOT_REVIEWED / NOT_ADMITTED**. Date: 2026-11-14 (Asia/Shanghai). Parent task RS-X6-TRIADIC-CLOSURE-DYNAMICS; inherited publication TP2-8B7E13C5904A2D6F1142. Scientific input frozen at awdawmip/enterprise-math commit a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5). No ownership or frozen science change.

## Exact model and typing

Fix a Cell c in the signed native X6 affine Z^6 torsor and a three-port set T={p,q,r} of distinct-axis native signed unit directions. There are 160 such T. Preserve T, all three separate nonzero equal-quantum source identities and a declared bijection beta_T from its three source tokens to three **local V29 passage ports** C_T={0,1,2}. The bridge is explicitly chosen and transported under axis relabeling; no identification of all six PF-10 channels with X6 spatial axes is inferred.

Reuse R762R: each order ell=(a,b,d) has a candidate six-step native Cell path (a,-a,b,-b,d,-d). It visits all ports, returns to c with zero rooted directed edge current, and the proposed completed-event successor is F(ell)=(b,d,a).

New *chosen candidate* lift: each completed triadic spatial event is accompanied by three completed V29 internal PASS occurrences

PASS(a->b), PASS(b->d), PASS(d->a).

These are passage-port events rather than six primitive Cell hops; they increment one nonnegative M[x,y] apiece, perform no inter-Cell TRANSFER, and leave Rin/Rout unchanged. Their 3x3 adjacency matrix is C(ell). Define Omega=C-C^T and u=Omega*1. For ell=(0,1,2):

C = [[0,1,0],[0,0,1],[1,0,0]];
Omega = [[0,1,-1],[-1,0,1],[1,-1,0]].

These port matrices are observers over native X6, not substitute space coordinates.

## Theorem S1: cost, local skew and conservation

For every ell, the candidate lift performs exactly three V29 PASS increments, changes u by 0, preserves V29 scalar network charge, and has rank_Q(Omega)=2. Exactly three PASS operations are **necessary and sufficient** under V29's nonnegative count grammar to realize the specified three-edge C from zero passage counts; TRANSFER cannot replace any.

Proof: C is an oriented directed 3-cycle, with one outgoing and incoming unit at each vertex. V29 gives Delta u=e_a-e_b per PASS; summing around the cycle gives zero. The displayed nonzero skew matrix has constant vector kernel, and a nonzero 2x2 principal minor, so rational rank is exactly 2. Every one of the three distinct positive entries of C requires its own entry-incrementing PASS, while TRANSFER changes only boundary Rin/Rout; all three suffice. Each PASS preserves the scalar sum of u by V29's exact conservation theorem. QED.

Project V27 already exhibits the rank-two atomic directed cycle. Novel work here is its source-typed interface with R762R's signed X6 order fiber, and the exact observer behavior. The three-PASS minimum is a ledger target cost, not a claim about native force arity or Cell path length.

## Theorem S2: threefold completed-event BRC residual

Fix T and its token bridge. The six possible orders ell have **exactly two** different completed V29 matrices C (equivalently Omega), each with **exactly three** preimages. The two C correspond to the two opposite orientations of the same directed 3-cycle; u is identically zero and has one six-element fiber. Across all 160 signed T, retaining T gives 960 ordered states, 320 (T,C) or (T,Omega) signatures with three-element fibers, and 160 (T,u) signatures with six-element fibers.

Proof: C depends on the oriented 3-cycle edge set, invariant precisely under the three cyclic rotations of its starting token. Reversing order transposes C, negating its nonzero Omega. The six orders split into the two C3-orbits of size three, and no other equality occurs. Multiply by 160 independently retained signed-T populations. QED.

## Theorem S3: sharp one-event provenance repair

Within each fixed oriented-C fiber, recording the **first source** of the event separates the three source phase origins. Thus, conditional on the completed Omega, two fixed binary repair bits are both sufficient and necessary: ceil(log2 3)=2.

More strongly, a single **first directed V29 PASS increment (a->b)**, recorded *during* the event, determines the complete order ell=(a,b,d), since the third token d is the unique remaining element of T. Among the six orders there are six distinct first directed PASS edges with singleton fibers. Thus one within-event directed-PASS observation is enough for full order recovery, whereas the completed-event cumulative C alone leaves a threefold ambiguity.

Proof: The directed C has three starting-source choices. Given C and first a, its unique directed successor b and final d are fixed. A binary code cannot encode three remaining choices in one bit. Given just the first directed ordered edge (a,b), the third token d is fixed from T, and every possible ordered pair yields a distinct one of six orders. QED.

R762R's first-source-only observer has two preimages per single observation and needs two event rounds; the richer first-directed-PASS prefix resolves the entire order in one event.

## Theorem S4: repeated completed-event blindness

For R762R's candidate successor F(ell)=rotate(ell), one has C(F(ell))=C(ell). Therefore after k>=1 completed candidate events:
M_k = k*C(ell), Omega_k = k*Omega(ell), u_k=0.

Consequently, **any length of time series of completed-event cumulative M or Omega measurements** is identical for the three cyclic starting phases of any fixed oriented C. Future queries about the first source can distinguish them: completed counts alone are not predictive-complete for source-order-sensitive futures.

Proof: The cyclic shift preserves all three oriented PASS edges. By V29's additive update, induction yields k times the same matrix, and all contrasts follow linearly. The three initial orders in one cyclic orbit have distinct first sources but identical kC for every k. QED.

## Relation to V39

The genuine V39 based network-loop port is (j,h), where j is inter-Cell conservative transfer current and h is the **actual V17 S3 active-frame transport**. This candidate contains zero TRANSFER and its transfer-chain j is zero. Its internal source-order F is not automatically the V17 h.

A model-pair underdetermination witness: independent of V29's nonnegative PASS counts, one may choose a purely formal compositional frame decoration h_k=id or h_k=rho^k for a fixed S3 3-cycle rho. Both give the same M_k=kC but distinct group readouts. This proves the V29 count grammar alone does not determine an S3 frame transport; neither decoration is claimed to satisfy actual V17 connection/physical admission. The missing law is the real event-to-frame connection.

## Exact test, scope and next step

R762S_V29_TYPCYCLE_VERIFY.py uses Python stdlib exact integers to enumerate all 20*8=160 signed X6 distinct-axis triads and their 6 source orders. It verifies the two 3-order orientation fibers, u=0, first-pass singleton fibers, 960/320 signatures, and k=1..7 cumulative invariance. Full machine evidence is R762S_V29_TYPCYCLE_EVIDENCE.json. The finite population is exhausted, and S1-S4 also have the elementary general proofs above. No native TRIADIC_CLOSURE_E evaluator, native V17 frame transport, or original project V29 benchmark has been executed.

In the current run the native Sites status and exact continuation requests both returned BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false. Live Task owner/CLAIM and new service-issued identity are unconfirmed. This research artifact is an independent author-side candidate; it asserts no formal Task CLAIM, native PROGRESS, frozen Result or Driver review.

Next discriminating experiment: read the true TRIADIC_CLOSURE_E Cell/Link/Port admission predicate and V17 source-slot connection, check whether this specific PASS atomization is admissible; for actual accepted events compute first/repeated V29 ledger and V39 (j,h), or derive a typed exclusion witness and test an alternative lifted coupling.

## Source provenance

Frozen P000 V5, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md and definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json at a72226e2430ffa4786321ac86e7f0c599d5f0389. R762R predecessor research_notes/R762R_TYPED_TRIADIC_INCIDENCE.md at 018a7bc84de6c73cefc88379ec0c9a4247aa6be2, PR #2333. Earlier V27 research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md; V29 research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md; V39 research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md, fetched at current main. Current docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; docs/PORTABLE_RESEARCH_PROTOCOL.md; research_priorities/research_method.json; GLOBAL_KNOWLEDGE_V1 math policy.
