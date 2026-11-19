# X6 R27 — Hyperedge-arity filtration and exact Boolean-BRC future-language quotient

Date: 2026-11-19 (Asia/Shanghai). Scope: RS-X6-NATIVE-TIME-DYNAMICS; publication TP2-91D4A7C2F63805BE21A3. Author-lineage attribution: EM-X6-214D9C; current live write authorization is a separate native-control question.
Status: CONDITIONAL_AUTHOR_PROOF / FINITE_EXACT_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED / NATIVE_TRIADIC_ADMISSION_OPEN.

## Frozen science and prior frontier

P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Immutable taskbook: awdawmip/enterprise-math@f41c2690daba467ecbde99615a1337e67be46ffd:research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md. R26 predecessor: research_notes/portable_direct/2026-11-19_x6_pairwise_link_guard_graph_quotient_r26.md. Current active worldview distinguishes six native signed Cell axes and time as relational-event order; a specified signed Port move is a single axial step, not a seventh spatial axis. Joint-relational observers require explicit future-language safety before compression.

The user-locked primitive stable force relation is the *three-quantum TRIADIC_CLOSURE_E*. P000 specifies its arity and canonical equal-quantum condition, but leaves the detailed Cell/Link/Port event-admission dynamics open. The hyperedge guards below are explicit CONDITIONAL composite controls; hyperedge cardinality three is not by itself a native primitive-closure certificate.

## Exact declared controller

Let V={0,...,m−1} be a finite labeled source set, m≥1. A finite hypergraph H=(V,F) has distinct hyperedges e⊆V with cardinality |e|≥2. Mixed edge arities are allowed.

Each i∈V carries a complete triadic source B_i in its own disjoint two-Cell lane, embedded in the signed X6 affine Cell torsor. The successful labeled events B_i^+ and B_i^− alternate, moving B_i by +E1 and −E1 respectively; all lanes are disjoint by distinct offsets along another existing signed axis. The first completed B_i return reveals a persistent typed link flag l_i=θ_i, where θ_i∈{0,1} is a conserved hidden internal history bit. Eligibility of B_i events is independent of θ. Each e∈F has a separate complete triadic one-use consumer A_e, which moves along its own signed-axis lane; its uniquely labeled event A_e^+ is enabled exactly when every i∈e has completed its first return, every such θ_i=1, and A_e has not been used. A_e neither changes source lanes, return flags, θ, nor other consumers. No failed attempt is in the observation alphabet.

Initially all public Cell, phase, returned and consumer-used data agree. The observer L_h(θ) records every successful *fully labeled source/Port word of length at most h*, with its order and identity. It observes neither hidden θ nor link flags directly. No timing or precision-refinement coordinate is identified with the event count. Define S(θ)={i:θ_i=1}. For any integer r (including r<0, when the family is empty) define F_≤r={e∈F:|e|≤r} and the active hyperedge signature A_r(S)={e∈F_≤r:e⊆S}.

## R27 theorem — Exact horizon filtration

For every h≥0, write r(h)=floor((h−1)/2). For all θ,η:

**L_h(θ)=L_h(η) if and only if A_r(h)(S(θ))=A_r(h)(S(η)).**

The shortest word containing the labeled consumer event A_e^+ has length exactly 2|e|+1. The truth of e⊆S may be inferable at shorter horizons from other, lower-arity hyperedges; the theorem precisely accounts for that redundancy through A_r(S). Edges with larger guard arity cannot directly occur within the horizon-h language. No later than the finite horizon h_* = 2 max_{e∈F}|e|+1 (h_*=0 when F is empty), this filtration equals the full infinite-future initial-fiber quotient. The actual stabilization horizon may be earlier when larger conjunctive guards are already determined by smaller guards. For a fixed k-uniform hypergraph with at least one edge, all histories have equal languages for h≤2k and the full quotient first appears at h=2k+1.

**Necessity.** For any e={i_1,...,i_k}, the length-(2k+1) signed-Port word
B_{i_1}^+ B_{i_1}^- ... B_{i_k}^+ B_{i_k}^- A_e^+
is legal precisely when e⊆S(θ). If 2k+1≤h this membership is directly recoverable from L_h.

**Sufficiency.** Any successful word containing A_e^+ must include all k distinct earlier B_i^+ and B_i^- return events and hence has length ≥2k+1. Thus words of length ≤h can use only e∈F_≤r(h). Couple controllers with the same public phase, first-return and used-consumer bits, preserving all labeled B transitions and the availability of every A_e with |e|≤r(h) from equality of A_r(h). Every continuation within the remaining event budget uses only these edges, so the labeled successful-word languages agree. The same coupling with all F proves the unlimited-horizon assertion.

## R27 quotient-class and exact fiber formulas

Let F_h=F_≤r(h). Define W_h(S)= union of all e∈F_h with e⊆S; take W=∅ if there are no such e. Then A_r(h)(S)=A_r(h)(W_h(S)), and the union of edges in A_r(h)(S) recovers W_h(S). Therefore W_h is an EXACT sufficient AND minimal initial-fiber state coordinate for the declared observation and horizon.

A subset W⊆V is realizable iff every v∈W lies in at least one hyperedge e∈F_h with e⊆W (empty W is valid). Thus

C_h(H)=#{W⊆V: for all v∈W, there exists e∈F_h such that v∈e⊆W};
b_h=ceil(log2 C_h(H)).

The closed-fiber count has a useful hypergraph independence form. For a realizable W put U=V\W and define residual edges

R_W={e\W: e∈F_h and e is not a subset of W}.

Then the exact number of original supports S with W_h(S)=W is the number I(U,R_W) of subsets I⊆U that contain no residual edge r∈R_W in full. This is a standard combinatorial hypergraph independent-set count, now typed to the declared future observer. Proof: S=W∪I has no additional activated edge iff for every e∉F_h[W] the difference e\W is not contained in I. This bijection proves the formula. It reduces at arity 2 to the R26 ordinary graph neighborhood/independent-set fiber law.

For the complete 3-uniform hypergraph on m≥3 vertices, C_h=1 for h≤6, while for every h≥7:

C_h(K_m^(3))=1+sum_{j=3}^m binom(m,j),
b_h=ceil(log2 C_h).

All supports of size 0,1,2 merge into one language class, and every support of size ≥3 is uniquely identified. At m=3,4,5,6,7,8, the counts are 2,6,17,43,100,220 respectively, requiring 1,3,5,6,7,8 fixed-length bits.

For a mixed-arity example, m=4 with F={{0,1},{1,2,3}}, the class counts are C_4=1, C_5=C_6=2 and C_h=4 for h≥7. The four h≥7 fiber sizes are 11,3,1,1. This is an exact source-sensitive joint-residual example: the three-way relation becomes visible at step seven even after the two-way relation has stabilized.

## Exact checking and boundaries

The accompanying independent Boolean-BRC verifier compares exact recursively interned labeled successful-word signatures against the predicted hyperedge filtration, and checks each quotient class and each residual-hypergraph fiber. It exhausts all labeled three-uniform hypergraphs on m=1..4, all mixed (2,3)-arity hypergraphs on m=3, and eight representative mixed/other graphs on m=5, for horizons 0..8 (m≤4) or 0..7 (m=5): 44 hypergraphs, 53,623 pairwise signature comparisons, 586,261 memoized recursion states; all PASS. Complete-3-uniform counts are independently checked through m=8. Results belong to this finite test corpus; universal statements follow from the above symbolic argument.

What this theorem does NOT yet establish is a native event embedding for TRIADIC_CLOSURE_E. The P000 primitive stable-force predicate does not currently expose a complete dynamical rule for translating hidden θ, the l_i updates, multi-source Link conjunctions, irreversible consumer action or resource regeneration into admitted native Cell/Link/Port transitions. The typed witness to seek next is a total or precisely domain-restricted event morphism preserving source identity, signed Port, complete three-quantum closure, path provenance, guards and observer words. If the actual native gate differs, recompute its quotient from its exact transition system rather than importing this conditional one.

## Next mathematical step

Investigate feedback in which a fired A_e changes eligibility of another hyperedge consumer or modifies a source's return flag. Identify a minimal counterexample to the arity-only quotient and derive a repaired residual coordinate; separately locate a genuine frozen-scope TRIADIC_CLOSURE_E transition specification and test the morphism on exact bytes.
