# X6 R14B — exact first distinguishing event depth and shell refinement of full signed-Port histories

Date: 2026-11-19 (Asia/Shanghai). Status: author-side **exact conditional theorem**, typed Boolean-BRC finite validation PASS, independent review NOT_REVIEWED. Research line RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3. Scientific input remains immutable awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000).

## Source relation and useful nonduplication

The previous canonical R14 `2026-11-19_x6_signed_multiaxis_interaction_components_r14.md` (commit e1b9c6dd39754da27abf362793212cf93650b85e) already proved that two fully signed six-axis source histories have the same future language to length h iff their nonzero relative displacement vectors agree within the signed step-distance h, or both are beyond that radius. R15 `2026-11-19_x6_horizon_two_factorial_hidden_source_order_r15.md` (commit 37198ebed52887e7b3676037708fc2beb9de7f18) already proved a factorial hidden-order family. The accompanying R14 independent reproduction `2026-11-19_x6_full_signed_port_radius_and_factorial_hidden_order_r14.md` **rechecks these facts and does not claim priority or a new R15 theorem**. Its checker expands the previous R14 finite pair sample to **all 84 nonzero signed six-component displacements within radius 2**, plus three distinct far configurations, rather than only a chosen two-coordinate projection. It reproduces the R15 q=1..5 factorial aliases.

This R14B adds a **sharp detection-time theorem** and a full finite pair-by-pair certificate, rather than restating the prior observational equivalence.

## Model and exact result

Two distinguishable source-labelled occupied Cells A,B lie in the six-native-axis signed relative X6 Cell chart. Every source may attempt a single signed-axis Port move `(source, ±e_i)`, i=1,..,6; the move is successful iff its destination is not occupied by the other source. Every successful future word includes its complete source and signed-Port order. This is the **conditional vacancy-only Boolean BRC operator**, with time = event order. Let `L_h(d)` denote the successful labelled words through h events from nonzero relative vector `d=p_B-p_A`.

Define for two **distinct** nonzero displacements `d≠d'` the first detectable language divergence

    δ(d,d') := min{ h≥0 : L_h(d) ≠ L_h(d') }.

**Theorem (exact first-witness length):**

    δ(d,d') = min( ||d||_1, ||d'||_1 ).

Here `||·||_1` is the minimum **declared signed-axis step count**, not the P000 enterprise geometric length. No finite horizon external precision or force law is inferred.

**Lower bound.** Put r=min(||d||_1,||d'||_1). In any successful or attempted source-labelled word of length h<r, a source collision is impossible from either initial configuration: moving either source one step changes relative displacement by one signed unit, hence at least its initial signed-step distance events are required to create an attempted collision. Thus `L_h(d)=L_h(d')` for every h<r.

**Matching witness.** Without loss let ||d||_1=r. Choose a shortest r-move signed-axis word moving A along a monotone path from its initial Cell to the *stationary* B Cell at relative vector d. Every proper prefix is legal in d; the final attempted move is blocked. Since d' has norm at least r and d'≠d, B in the d' configuration cannot occur at any path Cell of length below r (each proper prefix lies at signed-step distance <r from A), nor at the final Cell d. Therefore all r moves of the same word are legal from d'. The two length-r languages differ, proving equality.

This gives an **optimal constructive distinguisher** in O(6+r) event-listing time from the lower-norm vector and a proof of the absence of any shorter successful-language witness, without enumerating the exponential word tree.

## Exact horizon refinement shell counts

The earlier R14 class count C6(h) includes one pooled FAR class and all nonzero displacements of norm ≤h. As the horizon advances from h-1 to h, the **precisely new exposed distinguishable vectors** are the signed-integer shell of norm h:

    ΔC6(h)=C6(h)-C6(h-1)
           = Σ_{j=1}^{min(6,h)} 2^j binom(6,j) binom(h-1,j-1).

For h=1,2,3,4,5,6 these values are 12,72,292,912,2364,5336. A single FAR class splits into those explicit shell labels plus a renewed FAR class at each extension. This follows by assigning j nonzero axes, 2^j signs, and a composition of h into j strictly positive magnitudes.

The induced horizon filtration has a precise **first-witness depth** at which any two distinct relative states become observationally separated, not just an existence statement for eventual distinguishability. This supplies an exact stopping threshold for tests targeting a named pair of relative histories.

## Executed typed Boolean-BRC verification

The independent executable `x6_pair_first_divergence_brc_verify.py` imports the exactly saved/byte-verified `x6_full_signed_port_r14_brc_verify.py` Boolean support generator. It computes every successful labelled word at each depth, independently obtains the first depth at which the languages differ, and compares against the closed formula for every unordered pair of sampled displacements.

- Six-component X6 radius 2: all 84 nonzero near vectors plus three far representatives, 87 states, **3,741 unordered pairs**. Distinguishing depths 1: 966 pairs, 2: 2,772 pairs, beyond depth 2: 3 pairs.
- A two-coordinate auxiliary projection (not a native plane) radius 3: 24 nonzero near vectors plus three far representatives, **351 pairs**, at depths 1: 98, 2: 148, 3: 102, beyond: 3.
- All exact assertions PASS. The arbitrary-radius theorem is a symbolic proof; finite coverage is not extrapolated into a native physical law.

Companion result JSON: `x6_pair_first_divergence_brc_results.json`. Run the independent checker from `research_notes/portable_direct/` or with the directory on the Python module path.

## Boundaries and next scientific question

This observer records **successful source/Port-labelled words**, not rejected-event blocker identity, Link forces, signed amplitudes or physical time duration. A six-component Cell relation is retained; a two-coordinate auxiliary test is explicitly an embedded support projection, not a complete native three-dimensional slice. The native `TRIADIC_CLOSURE_E` event gate is still unverified and must be separately source-admitted before transferring this result to the full dynamics.

Next: characterize the minimum first distinguishability depth of two *multi-source* configurations under full signed vacancy moves. R15's factorial family proves that the first joint difference can occur at exactly two even when one-step event masks agree; R14B settles the two-source special case sharply. Compare an interaction-component sufficient state against the truly minimal joint future language quotient and investigate additional Link/Port memory required by genuine P000 triadic admissions.
