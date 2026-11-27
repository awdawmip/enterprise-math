# EC49GBH — fundamental exchange components and exact subset-rank decomposition

2026-11-27. AUTHOR_PROVED / EXACT_FINITE_COMPONENT_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED. Informed portable continuation of GBG at 4f716e6075647bfff29d79a052d93601096f7ec4:research_notes/portable_direct/EC49GBG_BOUNDED_SLACK_CLOSURE.md. Same BRC16943 frozen labeled static integer matching observer, no change to physical inputs, P000 or geometry. This is an application of classical matroid component theory with a concrete capacitated matching construction and finite replay, not a claim of novelty for the abstract matroid theorem.

## Theorem and construction

After GBB tight-cut contraction, let U be the fully matchable exclusive targets, X the labeled additional targets, C integer-capacity resources. Let r(Q)=H(U union Q)-|U|. This is the contraction by the independent U of the transversal matroid obtained by splitting each resource into c_j labeled slots. The matching independence axiom follows by alternating-path augmentation; contraction has the stated rank. Keep original labels and masks. Build a maximum matching of U plus X by first matching U and then inserting X, using GBD Dynamic; B is the matched subset of X, hence a basis of r.

For each unmatched x in X minus B start at its neighboring resources; whenever a resource is reached, visit all its matched occupants, then all their neighboring resources, including edges through U. A free slot cannot be reached because B is maximal. Let D_x be x together with the reached matched targets in B. Then D_x is precisely the fundamental circuit of x relative to B (a loop gives {x}). Proof: a reached b can be removed and replaced by x along a simple alternating path, preserving U and all other basis elements. Conversely, if B-b+x is independent, compare a matching for U+B-b+x with the fixed matching of U+B on cloned resource slots. Their symmetric difference contains an alternating path from x to b or a formerly free slot. The free-slot alternative contradicts maximality; hence b is reached. This exchange characterization uniquely specifies the fundamental circuit.

Union the labels of each D_x, leaving all other labels as singletons; denote the resulting partition by P. Each part A is spanned by B intersect A: every x outside B lies in a circuit wholly contained in (B intersect A)+x. Thus r(A)=|B intersect A|, and sum_A r(A)=r(X). For every Q subset X, subadditivity gives r(Q)<=sum_A r(Q intersect A). Submodularity gives r(X)-r(Q)<=sum_A (r(A)-r(Q intersect A)), by adding each A in turn to Q. Combining yields the exact identity

r(Q)=sum_{A in P} r(Q intersect A).

Consequently |Q|-r(Q)=sum_A (|Q intersect A|-r(Q intersect A)) simultaneously for all labeled Q. Every circuit must be contained in one part by rank additivity (otherwise each intersection is independent, contradicting circuit dependence). Conversely any partition having rank additivity must keep each D_x intact. Hence P is the unique finest rank-additive partition, independent of basis or matching choice. This is the usual matroid connected-component decomposition, now constructed from the existing matching without resource-cut enumeration. Loops and coloops appear as singleton components, and all non-singleton components are dependent. In particular the union of dependent components is the unique smallest subset attaining full nullity: removing a coloop preserves nullity, removing any noncoloop reduces full nullity by one, and nullity is monotone. The set is independent of order. No claim that the list of fundamental circuits alone determines all ranks inside a component.

For rank-two group searches in the simple observer after GBE loop/parallel simplification, every dependent triple is a circuit, hence confined to a single component. It is sufficient to query seed pairs inside dependent components, or if a component has rank two and size >=3 the whole component is itself a rank-two flat (an outside element in another component adds one to rank by additivity). This gives a direct shortcut without pair queries in those components. More generally independence, bounded-rank queries and full-nullity certificates can be resolved separately in parts, retaining labels. The representation preserves rank/deficit under arbitrary subsets of fixed X, not arbitrary new edges, capacities or physical configurations. No raw joint information is discarded.

After the maximum matching, for d=|X|-r(X) unmatched targets, explicit traversal costs O(d(E+m+n)) plus union-find and output incidence cost, where E is adjacency count, m resources and n targets. This upper bound includes traversals through matched U. Matching, input contraction, representative choice, verification and bit widths must be charged separately. The implementation uses GBD Dynamic, exact masks and original Hall reference; no end-to-end speed claim.

## Executed evidence

Archive EC49GBG_reproduction.zip SHA256SUMS verified before use. Frozen witness_records.json SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7; fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923. Same hashes as GBG. Run python exchange_components.py in extracted archive root with previous GBG dependencies. Code SHA256 7df3e7beba3985ce23eb24252e20fc246eca9884255014bb939567243c22c6aa, blob 814eb08a43b8e6710c0c80f0ab67a63c25e20924 at cce63d1d3a3e5cad69c62298c428fc53022578a8. Output SHA256 988f4906d8c8b9202d3f9f530549e4e4a653db6cdd66ead3646928b7f7261721, blob 9a7fd13d4211580230ef64e536d4913386cec14d at f5b6a7330ea4001245a57add7425311d4d4a4db3. Both remote readbacks exactly match local Git blobs.

Random seed 492611270826; 1600 graphs, width 1..7, capacities 1..3, 0..11 exclusive targets and 0..8 additional targets. 94488 exhaustive labeled subset rank decompositions, 3423 fundamental circuit comparisons via individual basis exchanges, 1600 reverse-order partition checks; zero mismatches. Original exact Hall reference. On 14498 frozen records, checked full rank and component rank sums both before and after GBE simplification; no full subset enumeration on frozen records. Raw additional targets 44221; 99 fundamental circuits, 44182 components, 135 elements in dependent components, 40 visited resource vertices summed over circuit traversals. After simplification 44125 targets, 44120 components, 3 fundamental circuits, only 7 elements in dependent components, 6 resource visits. Exactly two dependent cases, 1591 (3 labels 16,512,16384) and 10703 (4 labels 8,128,2048,32768). Both rank two. GBG pair closure queries reduced from 225 to 9 by restricting to these components (actually executed), exact line families agree. Direct rank-two shortcut to zero queries follows by theorem, not separately timed/executed. No full conflict reconstruction. 96% pair query reduction is not an end-to-end acceleration.

## Physical roots

Unmodified GAK: python fourth_input.py 2020 2022 600000 > gbh_roots.in; g++ -O3 -std=c++17 gak_solver.cpp -o /tmp/gbh_gak; /tmp/gbh_gak < gbh_roots.in > gbh_base.csv; EM_WORD=1 /tmp/gbh_gak < gbh_roots.in > gbh_word.csv. Input SHA256 6553eb663ee19356bd24fc4a471f51e0ff584f51a052455f46ec9c2d16ca93f5. Base SHA256 5e48724f706c63b73fd303b025d9b5cb0ed7889d03594481e96370667a6c9e44; word SHA256 1c360859d799ead48ecf7994e58a40efe1df1cf43252e6e08229b1e41e2f7a7d.

Base:
2020,1822,-1,179698,3554,58,0,0,0,0,0,0,0,0
2021,1823,1,116371,2505,54,0,0,0,0,0,0,0,0

Word:
2020,1822,-1,116703,0,14,0,0,0,0,0,0,116399,101184
2021,1823,1,76821,0,16,0,0,0,0,0,0,76547,63432

2020 NO, both below cap, 2021 YES with built-in labeled replay; each mode reads 3645 states. From GBG reported evidence frontier 1981 YES / 54 NO / 358 other of 2393, M14 remains [25,27]. No GBH integration into C++.

## Control and next

Exact topic lookup r4-20261127-0826-ec49as-read SUCCEEDED at Source 9b379b336f3e3c0eb6c16fc20446110995618aee, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. Historical EM-DIRECT-23537B only; current private identity binding unconfirmed. No new identity, claim, Result or Review. Global main entries read and checked against immutable 44e5ff0747cecb20044e308640f44d63f3fd4027; project rules read from current main. Activity association, canonical integration and GAR/GAS historical evidence remain pending. Next: test direct component-rank shortcut before unit-block and rank-two enumeration, compare end-to-end cost to existing bankwise algorithm; preserve full component internal masks, not just circuits. Continue unprocessed physical roots 2022 onward. 
