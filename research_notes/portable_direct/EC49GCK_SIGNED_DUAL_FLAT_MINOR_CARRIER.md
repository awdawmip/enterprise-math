# EC49GCK — Componentwise signed dual-flat carrier and exact minor transition

2026-11-28. AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_TRANSITION_REPLAY / NOT_REVIEWED.
Continuation of GCJ, fixed 9e6241960b5c896bc77441d1a3563139d2dd276b:research_notes/portable_direct/EC49GCJ_MAXIMAL_ATOM_QUERY.md (blob 974cc45c0c1adc96e60126176260fae7ab490bf7). Auxiliary strict-Hall combinatorial observer, not native BRC arithmetic, physical transfer, or a priority claim in abstract matroid theory. The new construction uses standard matroid duality and direct sum and retains full labeled suffix independence, a stronger operation scope than port-only atom queries.

## 1. Label components may overlap in ports

Let N=(M/S)|F be the finite matroid on remaining labels after independent prefix S, with nonempty supports E_x. Write nu_N(X)=|X|-r_N(X) and F_U={x:E_x subset U}; GCJ's D(U)=nu_N(F_U).

Construct a basis B of N. For each x outside B, connect x with all y in B such that B-y+x is a basis. Isolated loops and coloops are singleton groups. Let C_j be the connected vertex sets of this graph. For each x outside B, its fundamental circuit is within its group, so x is spanned by B intersect C_j (loops are spanned by the empty set). Consequently r_N(C_j)=|B intersect C_j| and sum_j r_N(C_j)=r_N(F). This implies N is the direct sum of the restrictions N|C_j: for any X subset F, submodularity gives r_N(F)<=r_N(X)+sum_j (r_N(C_j)-r_N(X intersect C_j)) by adjoining the C_j one at a time; subadditivity gives the reverse rank inequality. The graph groups are precisely matroid components: any direct-sum partition must keep each fundamental circuit in one part, hence contains the graph groups.

Therefore
D(U)=sum_j nu_{N|C_j}(F_U intersect C_j)
for all port subsets U, irrespective of intersections of the port supports of different label components. All labels and their original supports are retained. Deletion and contraction commute with direct sums, so the components of any remaining minor refine the surviving components; they cannot merge.

For GCB's additive value p and saving s, exact local feasible Pareto pairs can be combined by Minkowski sum followed by Pareto filtering, recovering every budget optimum and one concatenated label witness. A dominated local pair stays dominated after addition of any other pair, which proves the filtering rule. The resulting global front can still grow exponentially; no end-to-end runtime bound claimed. This convolution is proved here but not implemented in the replay.

## 2. Dual-flat exact signed carrier

For a label component C, write P=N|C, d=|C|-r_P(C)=r_{P*}(C), and use dual rank
r*(Z)=|Z|-r_P(C)+r_P(C minus Z).
Then for every X subset C,
nu_P(X)=d-r*(C minus X).
For every proper flat L of P* define an integer w_L by descending inclusion:
w_L=d-r*(L)-sum_{H proper flat, L strictly subset H} w_H.
The full flat has weight zero. This is upper-zeta inversion on the flat poset; no positivity assumption. If K=cl*(C minus X), all flats containing C minus X are precisely flats containing K. Thus
nu_P(X)=sum_{L proper flat} w_L 1_{C minus L subset X}.
A proper flat has a basis of size at most d-1. Enumerate dual independent subsets of these sizes, close by rank queries, deduplicate masks, then invert. If d=0 there are no terms. The number of nonzero terms is at most sum_{i=0}^{d-1} binom(|C|,i). The global carrier is the sum of these per-component carriers; it needs at most the sum of the bounds, not a product. In particular fixed per-component nullity gives a polynomial entry bound even with arbitrarily many overlapping port components. Construction can require many rank queries and a quadratic flat-poset inversion; the entry bound is not a runtime guarantee. Each coefficient is an exact signed integer (bounded in absolute value by |C| 2^{|C|} via Boolean inversion). Use arbitrary-width masks and integer arithmetic for large inputs.

For port readout replace each label mask A=C minus L by support union E_A, combine equal port masks and omit zero coefficients:
D(U)=sum_A w_A 1_{E_A subset U}.
This is exact for every U, but the coalesced port form alone is not the transition state.

If d=1 and C is a component of positive nullity, the component is a circuit (including a loop); the dual is loopless rank one, the only proper flat is empty, and there is one positive term, w=1.
If d=2, the dual's bottom flat consists of loops, and its rank-one flats are the q parallel classes together with those loops. Each rank-one flat has weight +1, the bottom flat has weight 2-q. For a connected d=2 component there are no dual loops and q>=3 (q=2 is a direct sum of rank-one parts). This gives q+1 possible terms with a negative correction. The sign is algebraic, not physical amplitude or negative mass.

## 3. Exact closed signed-minor update, no rank recalculation

Preserve the labeled carrier nu_N(X)=sum_A c_A 1_{A subset X}, summing component carriers. Coefficients on the full labeled Boolean lattice are unique by ordinary zeta inversion: c_A=nu_N(A)-sum_{B strict subset A} c_B. Hence equality of these maps is equivalent to equality of the remaining labeled matroid. This is a canonical equality key at the fixed suffix. It does not rely on the component partition remaining unchanged.

Given disjoint R,D subset F, R independent (select), D skipped, let N'=N/R minus D and F'=F minus (R union D). For all X subset F', rank contraction gives
nu_N'(X)=nu_N(X union R) (since r_N(R)=|R|).
Therefore the exact child carrier is obtained by the following single scan:
- discard every term A intersecting D;
- replace each remaining A by A minus R;
- sum coefficients on equal new label masks and discard zero sums.

An empty-mask coefficient cancels exactly because nu_N(R)=0. No new masks beyond the images of existing ones can appear, so number of nonzero terms never increases under arbitrary legal insert/skip sequences. Selection legality is itself equivalent to sum_{A subset R} c_A=0. The child terms are the unique Boolean coefficients of the new nullity function, so no recomputation of dual flats, components, greedy ranks, cached bases, or support-closure normalization is necessary after initialization. For a same-support batch, keep explicit R and D labels; arbitrary mixed-support batches also work. Query and transition use O(a) subset/bitmask tests and exact integer additions with a current terms (dictionary aggregation under usual hash assumptions, otherwise sort or tree cost); multiword masks, integer bit complexity, allocation, construction, objective bookkeeping and global dominance comparisons cost extra. The bound is monotone per branch, not on the number of DP states. Equality merging with GCB p,s filters is exact; coordinatewise signed coefficient comparison is NOT asserted to be a dominance test. The original label IDs, supports, values/costs and witness are separately preserved. No arbitrary new labels, undo, physical state equality or external model transfer is claimed. Port-only signed readout must not replace label carrier for these updates.

## 4. Two decisive families

GCJ friendship k petals: the graphic matroid splits into k circuit components despite all cycles meeting the hub port. Thus the componentwise signed carrier has exactly k positive label terms, recovering D(U) for all U. GCJ's disjoint atom list has 2^k-1 elements. Minor update preserves at most k terms. This removes the specific exponential expansion, not every exponential case.

Theta K_{2,3}: endpoints 0,1, three internal vertices 2,3,4 and the six edges of three two-edge paths. Graphic forest matroid, one component, d=2. In port masks 0..4, the three cycle vertex sets are 15,23,27; the union is 31. Their deficits are respectively 1,1,1,2. Exact port formula is 1_{15 subset U}+1_{23 subset U}+1_{27 subset U}-1_{31 subset U}. Each proper query containing no full cycle has zero deficit. On the full Boolean port lattice the coefficients are unique by zeta inversion, so no nonnegative sum of support-containment indicators can represent this D. This disproves universal positive additive representation of that exact type; not the broader possibility of compact nonlinear positive carriers. It also explains why a signed correction is essential for some overlapping cycles.

## 5. Executed evidence (fresh synthetic input, separate from frozen physical data)

First replay, xorshift32 seed 20261128: 250 models, 2..6 ports, 4..10 labels, positive integer capacities 1..3. Reference enumerates all original label subsets; a nonempty chosen subset is independent iff its support union capacity strictly exceeds cardinality and all immediate subsets are independent. Rank is recursively the largest independent subset cardinality. At each visited minor check every labeled subset for component rank additivity; enumerate proper dual flats by independent generators, check rank/closure/zeta and every port query against original rank reference. Follow a deterministic random legal select/skip path. Independently graphic union-find reference for theta and friendship k=1..7 at all port masks.
250 models; 67526 original nonempty subsets; 1946 states (including theta); 135366 component rank checks; 10280 flat closure and 10280 flat zeta checks; 49368 port queries (includes theta, excludes separately listed friendship queries); 161096 component port checks; 107 rank-two component observations and 1088 rank-two query checks; 1695 refinement checks; 5596 component flat-count-bound checks; 0 disagreements. Friendship counts k terms vs 2^k-1 historical atom formula, all 43688 port queries verified. Theta coefficients exactly as above.

Second independent replay, xorshift32 seed 20261129 (seed label, not date), 200 fresh models of the same size ranges. Initial carrier by direct dual-flat enumeration and component factorization. Independently compare every visited state and every legal batch child against all labeled-subset reference nullities and direct Boolean coefficient inversion. Choose random nonempty processed blocks (not required same-support), check every R subset H, reject dependent R, follow a random legal child. 59848 original nonempty subsets; 1060 visited states; 3200 legal child transitions; 766 illegal selections; 140176 all-label query checks; 7553 nonzero canonical coefficient checks; 3200 term-count monotonicity checks; 0 disagreements. The largest carrier in this second replay had 537 terms, illustrating that signed carriers are not uniformly small. The first replay's maxTerms=5 counts *port-coalesced terms per component*, not directly comparable. Actual JS execution in tool isolate; no full Pareto DP integration, end-to-end timing or memory comparison yet.

Evidence:
- d48f6b2b76299198d30b76ab4096cb687a607e6c:research_artifacts/portable_direct/EC49GCK/dual_flat_replay.js (blob fed659649dacb2d342a91a56a58595a0ae88528c)
- 0ad937253fb6b9fef8ef903dfe614d51e8bf43a5:research_artifacts/portable_direct/EC49GCK/replay_output.json (blob c74ac849cb1d619e0b2914791c6b88ccbcce3349)
- a53084f6746afd5a73e776e17092961664783589:research_artifacts/portable_direct/EC49GCK/signed_minor_replay.js (blob f8edc679a3abaa4c23aeecde730c9f5abd37424f)
- bac9f5fdc8ab084494a3e8f461b599aaeb39fa17:research_artifacts/portable_direct/EC49GCK/signed_minor_output.json (blob 0e6f2cd5e3c6ecc4a0df1d455ada04659ab761d6)
Each actual executed code/output saved and read back with exact content equality. Reproduction: node dual_flat_replay.js; node signed_minor_replay.js.

## 6. Next and provenance

Integrate labeled signed maps with GCB all-budget solver; compare GCF/GCH/GCJ and this carrier using the exact same input, including initialization, state count, signed integer/label-mask memory and objective recovery. Develop exact cross-state dominance on signed carriers without unjustified coefficientwise comparison. Consider component-local Pareto convolution for independent label components. Keep full label carrier where future label operations matter; port projection is query-only.

Frozen BRC16943 bytes not recovered this round; no new physical computation. Inherited hashes witness_records.json c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7 and fourth.json 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923. Historical 25<=M14<=27 and next root 2046 not newly established.

Current canonical main entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613 matched immutable cbe61b01f36fe10031ffb0e9df7400dde74ed318. Read applicable global/Source P000 V4/V5, ACTIVE worldview, joint preservation, heartbeat, residual, continuation, portable and method. Current native exact-topic request r4-20261128-1326-ec49as-topic-read returned SUCCEEDED, Source 0010ddf1c341ac3d7db316e15fc65cb5b72ed507, NO_CANONICAL_PUBLICATION_DIRECTORY; native owner view not evaluated. Identity-only status succeeded but current private researcher session remains unconfirmed. Historical EM-DIRECT-23537B is provenance only. Independent portable informed work, new noncanonical branch based on immutable GCJ, no shared CLAIM, alternate identity, Task mutation, or schedule change. Activity association and canonical integration pending. No Drive fallback required for GitHub-saved evidence.
