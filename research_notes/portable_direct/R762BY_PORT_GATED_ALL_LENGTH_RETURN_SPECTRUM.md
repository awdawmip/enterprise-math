# R762BY supplementary theorem: exact all-length based-return spectrum for each Port gate

Status: AUTHOR-PROVED / EXACT FINITE CHECK THROUGH m=8 / NOT_REVIEWED.
Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; conditional signed Cell/Port/Link triad model defined in R762BY_PORT_GATED_SIGNED_TRIAD_CLOSURE_THEOREM.md on this PR, with frozen P000 science pin unchanged.

## Statement

At fixed X6 Cell, q>0 and fixed signed named Ports, replace one occupied axis label at an eligible Port by one of the three absent labels, retaining all other labels and Port/link data. Let k∈{0,1,2,3} be the number of eligible Ports, and B_k(m) the exact **positive integer number of ordered length-m event histories starting at 123 and returning to the original unordered triad {1,2,3}**, regardless of terminal ordering. For every nonnegative integer m,

B_0(m) = 1 if m=0, else 0;

B_1(m) = (3^m + 3(-1)^m)/4;

**B_2(m) = (6^m + 4 + 5(-2)^m)/10;**

B_3(m) = (9^m + 5·3^m + 9(-1)^m + 5(-3)^m)/20.

Every numerator is divisible by its denominator, because these formulas count integer branch paths. The k=3 formula is the same ungated Johnson-frame marginal previously established in R762BV (PR #2535); this note independently derives the new k=2 closed form and unifies the four gating regimes.

## Proof for k=0 and k=1

For k=0 the event alphabet is empty. For k=1, two original axes stay frozen in ineligible slots and one Port label moves among four available axes (the old label plus the other three labels absent from the triad). This is the simple walk on K4 without self-loops. Its adjacency is J4−I4, with eigenvalue 3 on constants and −1 (multiplicity 3) on the orthogonal complement. Vertex transitivity makes the number of length-m returns equal to the trace of the mth adjacency power divided by 4, giving B_1(m) exactly.

## Proof for k=2: a ten-state Johnson walk

One original-axis label is fixed in the ineligible slot. The unordered labels in the two eligible slots form a two-element subset of the remaining five native axes. Each Port replacement changes exactly one member of this pair, so the unordered event graph is the Johnson graph J(5,2), with C(5,2)=10 vertices and degree 2·3=6.

Let B be the 10×5 point-incidence matrix, B_{S,i}=1 iff i∈S for a two-element subset S of the five axes. Then (BBᵀ)_{S,T}=|S∩T|, so the graph adjacency matrix is exactly **A=BBᵀ−2I_10**. Moreover BᵀB has diagonal entries 4 and off-diagonal entries 1, hence BᵀB=3I_5+J_5. Its eigenvalues are 8 (multiplicity 1) and 3 (multiplicity 4). The nonzero eigenvalues of BBᵀ match those of BᵀB; the remaining five eigenvalues are 0. It follows that A has eigenvalues **6 (multiplicity 1), 1 (multiplicity 4), and −2 (multiplicity 5)**.

Each unordered Johnson walk edge has a *unique* lift from any current ordered eligible Port assignment, because exactly one old label is replaced and its Port is determined by the current ordered pair. Thus every unordered walk starting at {1,2} lifts to exactly one permitted ordered-frame history starting at 123, with the same path length; the condition for return is exactly the same original unordered pair. The number B_2(m) therefore equals (A^m)_{S,S} for the base S={1,2}. By S5 vertex-transitivity all ten diagonal elements of A^m are equal. Hence

**B_2(m)=tr(A^m)/10=(6^m+4·1^m+5(-2)^m)/10.** QED.

## Proof for k=3

All three Ports are eligible and unordered active triads are 3-subsets of six axes: Johnson J(6,3), degree 3·3=9. Every unordered walk again lifts uniquely from an ordered starting frame. The standard incidence-layer decomposition, or the previously author-proved exact R762BV V17 spectral identity, yields adjacency eigenvalues 9,3,−1,−3 with respective multiplicities 1,5,9,5. By S6 vertex-transitivity,

B_3(m)=tr(A^m)/20=[9^m+5·3^m+9(−1)^m+5(−3)^m]/20.

This k=3 case reuses R762BV rather than claiming a new spectral computation. QED.

## Independent cross-check and BRC scope

Ran the companion exact integer state/path-count DP with every permitted Port switch through m=8. The independently computed B_k(0..8) agree term-for-term:

k=0: [1,0,0,0,0,0,0,0,0]
k=1: [1,0,3,6,21,60,183,546,1641]
k=2: [1,0,6,18,138,762,4698,27930,168090]
k=3: [1,0,9,36,369,2952,26937,239148,2155617].

The formulas are valid for **all nonnegative m by the spectral proof**, whereas the independent enumerator checks m≤8. Counts are exact positive-integer BRC branch multiplicities for a declared terminal unordered-triad observer. Port signs and histories must remain typed in any future interface that observes them; no signed-force cancellation or physical time evolution is inferred from these counts. The model's event predicate is still conditional and not native Source-authorized. Independent review NOT_REVIEWED.

Next: intersect the candidate event graph with the actual signed TRIADIC_CLOSURE_E Cell/Port/Link admission relation and V17/V29/V39 transducer. The resulting native graph may have a different spectrum; compute it with event-source provenance retained.