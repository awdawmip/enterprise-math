# R5: Named-Set congruence quotient and positive hyperedge slack

Date: 2026-11-16 (Asia/Shanghai).
Frozen science pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Question and scope

Continue the previously published R5 source-labelled radius-two ring-of-triangles repair model, in particular the future-safe belief and dynamic integer-program work at research_notes/portable_direct/r5_slack2_future_safe_star_20261116/. That predecessor found unrestricted finite optima 4,8,16,32 for ring sizes 3,4,5,6 and left the universal unrestricted lower bound open. Here an exact all-size theorem is proved for the algebraically defined **homomorphic deterministic subclass**, and extended to finite nonnegative weighted hyperedge readouts. The original source-labelled common library L(r), P000, ACTIVE worldview and task scientific input remain unchanged.

Let X={0,1}^n; named Set_i(b) replaces input bit i by b∈{0,1}. A homomorphic controller is a surjective state abstraction π:X→Q with maps δ_i^b satisfying π(Set_i(b)u)=δ_i^b(π(u)) for every u,i,b. All concrete states in the full fiber π⁻¹(q) are possible inputs to abstract state q. This is a subclass of the previously used, more general transition-closed overlapping-belief controllers.

The original R5 ring readout is q(u)=Σ_{i mod k}u_i u_{i+1}, and its shared-source optimum for a nonempty raw-state set B is 5k+q(∨B), where ∨ is the bitwise OR. The optimum for an individual u is 5k+q(u). For a separate positive generalization, use a finite nonempty-hyperedge family H with weights w_A≥0 (rational allowed) and h(u)=Σ_{A∈H}w_A ∏_{i∈A}u_i; suppose its source-library readout is C+h(∨B) and its per-raw optimum is C+h(u). This last source-library assumption is explicit; the resulting combinatorial theorem applies whenever it holds.

## Theorem A — All reset congruences are coordinate projections

For every n≥1, an equivalence relation ≈ on X is respected by all named Set_i(0), Set_i(1) **if and only if** a unique fixed subset F⊆[n] exists with

    u≈v  ⇔  u_j=v_j for all j outside F.                  (1)

In particular, any homomorphic controller has exactly 2^(n−|F|) states.

**Proof.** Suppose u≈v and u_i≠v_i. Reset all coordinates other than i to their values in u. The two resulting masks are equivalent and differ only in bit i. Reset those other coordinates to arbitrary assigned values, showing that every pair differing only in bit i is equivalent. Let F consist of all such globally forgettable coordinates. Transitivity then equates any two masks agreeing outside F. Conversely, the defining choice of F ensures that an equivalent pair differs only within F. This establishes (1). Equality on coordinates outside any fixed F is visibly preserved by every Set operation. Uniqueness follows from precisely which one-bit flips are equivalent. QED.

## Theorem B — Exact worst-case source slack for a projection

Define c_h(F)=Σ_{A∈H:A∩F≠∅}w_A. For the projection forgetting exactly F, its exact maximum additive source penalty across all inputs and all finite named-Set words is **c_h(F)**.

**Proof.** In any projection fiber, the OR fixes forgotten coordinates F to 1. The difference h(∨B)−h(u), for u in B, receives contributions only from hyperedges meeting F, each between 0 and w_A by positivity. Hence the difference is at most c_h(F). Named Set operations map each complete projection fiber into a subset of another fiber, so the same bound applies to any sequence, with the source-labelled output L(OR of the destination fiber). To attain equality, set all outside-F coordinates to 1 and choose within that fiber a concrete state whose F coordinates are all 0. Every hyperedge meeting F then contributes exactly its weight to h(∨B)−h(u); every other hyperedge cancels. Thus the worst case equals c_h(F). QED.

## Corollary C — Exact homomorphic state complexity

For additive slack budget s≥0,

    N_hom(n,h,s) = 2^(n−d_h(s)),
    d_h(s) = max{|F| : F⊆[n], c_h(F)≤s}.                 (2)

The optimal controller stores the complement of a maximizing F, ignores resets on F, directly updates retained coordinates, and emits the inherited genuine source library for the completed OR mask. Equation (2) is a finite exact optimization formula. On arbitrary hypergraphs it asserts no general polynomial-time solver.

## Theorem D — Exact all-k ring answer, every slack budget

For k≥3 and unit-weight cycle edges, any proper nonempty F of size d induces at most d−1 edges. Therefore

    c_q(F)=2d−|E[F]|≥d+1,                              (3)

with equality for d consecutive vertices. The empty set has cost 0; the entire cycle has cost k. Consequently, for **integer s**,

    N_hom(k,s)=2^k                 for 0≤s<2;
               2^(k−s+1)          for 2≤s<k;
               1                   for s≥k.             (4)

For real s≥0, replace s by floor(s). The construction forgetting s−1 consecutive vertices attains the middle bound with a true source-labelled library; at s=2, every k≥3 has N_hom(k,2)=2^(k−1). At s=k−1 the homomorphic optimum is four states, while at s=k one state is sufficient. Equation (4) is an all-scale **homomorphic** theorem.

## Relation to the unrestricted open question

The predecessor's full future-safe belief MILP permits overlapping beliefs and transitions into proper supersets, so its states need not arise as fibers of one congruence π. This paper establishes the precise benchmark for that strong compositional subclass; the unrestricted all-k slack-2 lower bound remains unresolved. A productive next experiment is to decide whether every transition-closed family of radius-one-star beliefs can be transformed into a reset congruence without increasing state count. A counterexample would isolate the additional compression mechanism; a proof would settle the unrestricted conjecture.

## Reproducible exact evidence

Execute: node VERIFY_R5_CONGRUENCE_QUOTIENT.js (plain JavaScript, integer operations, no optimizer or numeric tolerances). It exhaustively enumerates all Bell(8)=4140 equivalence partitions of the 3-bit cube and finds exactly eight reset-compatible coordinate projections. It checks 39 ring/budget cases for k=3..8 and s=0..k with every forgotten mask and concrete fiber, and 2187 assignments of weights in {0,1,2} to seven nonempty hyperedges on three vertices, giving 17,496 exact hyperedge fiber checks. Output: EXACT_R5_CONGRUENCE_QUOTIENT_EVIDENCE.json with the PASS code and per-budget witness. General statements follow from the proofs; the finite tests are reproduction and regression evidence. Independent review NOT_REVIEWED.

Provenance: R5 prior notes r5_slack_dynamic_source_20261116, r5_shared_source_helly_20261116 and r5_slack2_future_safe_star_20261116; current global mathematical evidence and output rules; frozen input unchanged. Historical Researcher-ID EM-DIRECT-B78E55 and Activity RA-33C87C2B703418F0706695E9 are provenance rather than current CLAIM authority. The artifact is independent portable research and does not mutate protected Task, Result, Review or Foundation records.
