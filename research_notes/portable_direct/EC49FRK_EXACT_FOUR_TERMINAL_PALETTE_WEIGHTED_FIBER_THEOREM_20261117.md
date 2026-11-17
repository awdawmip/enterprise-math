# EC49FRK: exact four-terminal observer palette and weighted fiber root-mass theorem

2026-11-17. Parent scientific frontier: EC49FRJ ([PR #2624](https://github.com/awdawmip/enterprise-math/pull/2624)). Frozen science commit: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Original native BRC model and fixed-palette objective

Class 16943 has 310 original configurations, represented by 141 complete original *named* response profiles, with integer multiplicities summing to 310. Original query IDs 0–143 are terminal observations T; IDs 144–227 are root observations R. We use their unmodified frozen response map V[q][i]. Full 144-terminal signatures have 139 distinct classes, exactly two non-singleton terminal fibers: P={8,139} and Q={46,140}, each member multiplicity one. The other 137 classes are singletons.

For a fixed subset J of terminal query IDs define s_J(i) as the vector of all V[q][i] for q in J. A fixed terminal palette is **equivalence-faithful** when s_J(i)=s_J(j) if and only if full terminal signatures of profiles i,j agree. This preserves the terminal information partition, not every numerical component or future operation outside this declared observation scope. This is a nonadaptive query-set cardinality problem, not an adaptive decision-depth claim.

## Theorem 1: Four queries are necessary and sufficient

The minimum cardinality of a fixed, equivalence-faithful subset of the 144 physical terminal queries is **four**. One exact witness is

**J* = {31, 36, 102, 142}.**

Proof: there are C(141,2)=9870 distinct unordered profile pairs, and precisely two are indistinguishable under all 144 terminals. Thus 9868 separated pairs must be retained. Associate to every terminal ID q a 9868-bit set S_q marking the originally separated profile pairs on which its outcomes differ. Exhaustively compare all C(144,3)=487344 triples of terminal IDs. The maximum size of S_a union S_b union S_c is **9866**, less than 9868. No three-query palette works (and no smaller one could work, since it could be enlarged to three). For the witness J*, the union of its four exact bitsets has size **9868**, so its terminal partition equals the full 139-class partition. All counts are exact integer computations over the frozen original responses.

A near-optimal triple {36,67,106} has only 137 signature classes: alongside the two genuinely indistinguishable pairs it retains the additional collisions {4,77} and {5,9}. This is a direct example explaining the two missing separated pairs at the best triple.

## Theorem 2: Five-query adaptive exact identifier with minimum root slope

Ask terminal observations 31, 36, 102 and 142, in any fixed order. All but four named states are then uniquely identified. When the four-tuple belongs to P or Q, ask original physical root observation 148, whose outcomes separate both pairs. This exact original-response decision tree uses exactly four terminals on every path and one root on precisely profiles 8,139,46,140. It identifies all 141 named profiles, with worst-case five observations.

For priors p_i(lambda)=(1-lambda)/141+lambda*m_i/310, terminal cost t>0 and root cost x*t, its cost is

C_simple(x,lambda)/t = 4 + x*(4*(1-lambda)/141 + 4*lambda/310).

The tree is a simple constructive information-complete witness. It is not asserted to beat the existing all-price optimal native five-tree envelope of EC49FRJ.

## Theorem 3: Exact weighted terminal-fiber root-only Bellman decomposition

Let Omega be any finite static-state model, T any finite collection of zero-root-price observations, R a finite collection of root observations with fixed labeled response maps, and w_i>0 any weights (uniformity and normalization are not required). Terminal-equivalence fibers C are defined by identical responses to every observation in T. Suppose observations in T union R jointly distinguish every state.

For every S contained in one terminal fiber, let W(S)=sum_{i in S} w_i. Define g_R(singleton)=0 and, for non-singleton S,

g_R(S) = min over root queries q splitting S of [ W(S) + sum over nonempty response children S_a of g_R(S_a) ].

Then among all complete finite adaptive identifying trees using T union R, the **minimum total weighted root-query count** is

**G_R(w) = sum over terminal fibers C of g_R(C).**

Proof of lower bound: restrict any complete tree to one fiber C. Every T-query is constant across C, even conditional on earlier root outcomes; prune T nodes and non-splitting root nodes. The restricted root-only decision tree identifies all states of C and its root mass is no larger than the original root mass on these paths. By the complete splitting-subset Bellman recurrence its cost is at least g_R(C). Sum over disjoint fibers.

Proof of upper bound: ask all T queries first (no root cost), identifying the terminal fiber, and then follow a root-only tree realizing g_R(C) in that fiber. This simultaneously attains every fiber lower bound. Splitting reduces subset size, so the finite recurrence terminates; an unseparable fiber would instead have infinite cost.

With normalized positive weights, common root price x*t and terminal price t, we obtain the exact bounds

x*G_R(w) <= V(x;w)/t <= x*G_R(w) + |T|,

and in particular lim_{x to +infinity} V(x;w)/(x*t)=G_R(w). No high-price Bellman instance is required for the slope, only the original static observer-fiber calculation. This formula is a theorem for the defined finite static observer model; it does not identify distinct X6 path/provenance carriers without an additional observation-preservation map.

For frozen class 16943, P and Q each have two members split by root ID 148, all other fibers are singletons, and the exact uniform/multiplicity weighted **integer** root-count minima both equal 4. For the original mixed prior,

G_R(p_lambda) = 4*(1-lambda)/141 + 4*lambda/310.

## Exact single-query robustness / re-priced observer sensitivity

All **144** possible removals of one original terminal physical query preserve the 139-class terminal equivalence and integer root-count floor 4. This is a tested one-deletion result, not an arbitrary-subset deletion assertion.

For the explicit *counterfactual* of changing exactly one native root observation's price class to terminal price, retaining its unchanged original response map, exactly **16** IDs (148,...,163) split both two-state residual fibers. They each make all 141 named profiles terminally distinguishable and reduce the minimum root-count floor to zero. The other 68 physical root IDs leave the two fibers and root floor unchanged. This is a price-menu experiment; no such re-pricing is claimed for the original frozen Bellman optimization.

## Sources, verification and recovery

Immutable scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original master frozen data SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Original named profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. The prior archive EC49FRJ_EXACT_ALL_PRICES_STRUCTURAL_FIBER_FULL_EVIDENCE_20261117.tar.xz supplies both original data files and the independently preserved EC49FQI_NATIVE_DATA.py loader. A new self-contained evidence archive, delivered to the user, contains this original input plus the EC49FRK_MINIMUM_TERMINAL_PALETTE.py checker, generated JSON certificate and execution log.

The checker reconstitutes all 228 native physical responses, checks the two frozen SHA256 inputs, tests all 487344 terminal triples and the four-query witness, checks 144 deletions, 84 re-pricing cases, the exact fiber Bellman recurrence, and the conditional root-148 tree over all 141 profiles. The full 144-input menu is not silently replaced by the four-query palette when discussing original task optimality.

The theorem is author-proved and locally exact-finite-checked, NOT_REVIEWED, with no formal Result/Review/Task CLAIM or Activity checkpoint asserted. P000 and the ACTIVE X6 worldview are not modified.

**Next independent problem:** derive a precise terminal-query cost/root-budget Pareto frontier inside the sharp root-mass constraint, then ask whether a mixed-cost fixed observer palette can beat the five-query identifier while retaining the exact named profile and provenance scope.
