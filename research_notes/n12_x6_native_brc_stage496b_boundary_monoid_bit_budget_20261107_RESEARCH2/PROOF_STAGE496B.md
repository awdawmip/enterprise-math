# Stage496-B — Exact signed-X6 boundary algebra, dynamic edits, and Euler–BRC bit bounds

Date: 2026-11-07. Status: AUTHOR-SIDE PROVED DERIVATIONS / EXECUTED EXACT TESTS / UNREVIEWED.

Parent: Stage495-B commit 68a06c52d6ff034a1ab558bd59b9f8df3a4dd352 and author research PR #1736. Scientific frozen pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 Git Blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current 2026-11-07 normative rules were read independently. Authenticated GitHub principal: awdawmip. Native owner lookup: BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Thus this is independently executable author evidence rather than a claimed native RESULT or DRIVER acceptance.

## Exact carrier

Let Σ={A,...,L} represent the twelve signed native directions +E1,...,+E6,-E1,...,-E6 in the six-dimensional native X6 affine cell chart. They are 12 directions on six axes, not twelve axes. Write v(a)∈Z^6 for the corresponding distinct signed unit vectors. For each finite ordered history w=a1...am, define

D(w) = Σ_{i=1}^m v(ai),

E_ab(w) = #{ i∈{1,...,m−1}: ai=a, a_{i+1}=b }  (all 144 ordered pairs),

F(w)=(D(w),E(w)), with F(empty)=(0,0).

The length is determined by the full E for m≥1; all original letter order remains available in the data structure for future indexed edits. The positive unit BRC branch population counts distinct value-words, and neither its positive mass nor this combinatorial representation is a physical heartbeat amplitude law.

## Theorem 496.1 — First and last direction are encoded by (D,E)

For every nonempty word w of length m,

v(first(w)) = D(w) − Σ_{a,b∈Σ} E_ab(w) v(b),

v(last(w))  = D(w) − Σ_{a,b∈Σ} E_ab(w) v(a),

and m=1+Σ_ab E_ab(w). The 12 signed unit vectors are distinct, so the recovered vector uniquely identifies each endpoint. The empty word has D=0, E=0, whereas every singleton letter has D equal to a nonzero unit vector, hence emptiness is also distinguished.

Proof. In the first identity, the edge-target sum is v(a2)+...+v(am), which when removed from Σ_i v(ai) leaves v(a1). In the second, the edge-source sum is v(a1)+...+v(a_{m−1}), leaving v(am). The adjacency count sums to m−1. All terms are integer and exact. QED.

The argument requires the complete six signed components and 144 directed adjacency entries; it is invalid for a mere scalar length, absolute displacement or an unsigned total count without an appropriate repair.

## Theorem 496.2 — A closed exact associative concatenation law

For any words u,v define the product star on realizable F summaries by

F(u) star F(v) = (D(u)+D(v), E(u)+E(v)+[last(u),first(v)])

when both are nonempty; omit the last bracket if either word is empty. The bracket [a,b] is the one-hot 144-entry ordered edge vector. Its boundary letters are calculated from the factors alone using Theorem 496.1. Then

F(uv)=F(u) star F(v).

In particular star is associative on realizable summaries, F(empty) is identity, and for any fixed prefix x and suffix y,

F(u)=F(u') implies F(xuy)=F(xu'y).

Proof. Each adjacency in concatenated uv is either internal to u, internal to v, or the single new boundary pair joining last(u) to first(v). Displacements add. Both (F(u) star F(v)) star F(w) and F(u) star (F(v) star F(w)) equal F(uvw) by the displayed formula, proving associativity. Applying the same product to equal summaries gives the prefix/suffix congruence. QED.

Meaning: for an observer allowing only boundary concatenations of unchanged blocks, equal (D,E) carries a rigorous exact redundancy certificate. This is the required BRC observer-specific information-preservation argument, not a license to eliminate unknown interiors when future operations may edit indexed positions.

## Counterexample 496.3 — Global F cannot recover arbitrary indexed SET response

Over the native subset A=+E1, B=+E2, C=+E3, choose

u=AABA and u'=ABAA.

Both have D=3E1+E2 and the same multiset of adjacency types {AA,AB,BA}. Their F summaries agree. Applying the identical legal SET at 1-based position 2 with new value C gives respectively

SET(2,C)(u)=ACBA,  SET(2,C)(u')=ACAA.

Their signed displacements and ordered adjacency counts differ. A single global (D,E) aggregate thus loses information accessible to a positional edit. This directly answers the proposed over-aggressive compression candidate.

Minimality in the stated finite domain: the exact reproducer enumerated every three-letter word of length 1,2,3,4, grouped them by complete F, and compared all common fixed-index SETs with all three possible replacement tokens. All F-equivalent histories of length ≤3 have identical response to those operations, while the above pair at length 4 is distinguished. The minimality statement concerns precisely this complete three-letter finite search, with code supplying the exhaustive certificate.

Frozen native P/Q embedding: take T=ABGABA, W=GH and Q=TWAHA. Set H1=AABA and H2=ABAA. P=T is identical, the complete initial Q summaries agree by the concatenation law, and H's second letter lies at zero-based Q index 10. SET at this exact Q index to C distinguishes the resulting complete Q observers.

Two genuine successive edits can reveal an initially hidden distinction later: start with histories x=AAAABA, y=AAABAA, with F(x)=F(y). Apply SET at zero-based index 1 with B to both. They become ABAABA and ABABAA, with identical F. Now SET at zero-based index 2 with B to both. They become ABBABA and ABBBAA, with different F. The first edit leaves a hidden arrangement distinguishable by the second; the distinct local triple at the second probe is the retained missing information. This witness does not refute a stronger method that already retains every exact live edit-target triple.

## Theorem 496.4 — Exact compositional state for all finite legal dynamic-edit traces

Represent the current ordered native word in an implicit sequence tree (e.g. an implicit treap). Each leaf carries one actual signed X6 token, each internal node caches F of its exact contiguous in-order substring and its size, and cache recomputation is repeated application of the product star from Theorem 496.2.

Then after each finite legal sequence of indexed SET/INSERT/DELETE and suffix APPEND/POP — including interleaving, moving current indices, newly created joins and inserted public tokens — the root F equals the exact direct-scan F of the new current history.

Proof by induction. For one token, stored F is its singleton value. A concatenation node is exact by Theorem 496.2. Split at a valid current index separates the exact prefix from suffix in the tree's in-order word. Insertion adds one singleton, deletion removes one, and SET removes/replaces one singleton. APPEND and POP are the corresponding suffix operations. Merging contiguous fragments updates cached F by the associative product. Unchanged fragments preserve valid caches. By induction after each operation the full in-order token sequence is the exact current word and all node caches, including the root, equal their direct-scan F values. QED.

The scheme retains ordered tokens as leaves; it provides an exact future-safe carrier rather than a globally minimal history quotient. For the token-only F observer no extra original/public provenance labels are necessary to calculate the new aggregate once current tokens and current positions are retained. Other declared provenance-sensitive observers may require those labels.

For a treap with independent uniformly generated priorities, the expected number of changed nodes per edit is O(log(m+1)). At most 144 integer adjacency counters and six signed displacement components are combined for each node, giving expected O(144 log(m+1)) integer cache work per edit plus constant-size tree operations (and optional endpoint reconstruction using ≤144 counters), while stored cached integer cells total O(144m). Individual edge count and displacement coordinates are bounded by m in magnitude, requiring O(log(m+1)) bits. An adversarial treap priority arrangement may give linear tree height.

## Theorem 496.5 — Polynomial exact-integer bit budgets for Euler–BRC ranking

Let M=(m_ab) be a directed nonnegative multigraph inventory with n=Σ_ab m_ab edges and at most d≤12 active native signed letters. Let (s,t) permit at least one value-word Euler trail. Let o_v=Σ_b m_vb and let τ_t be the toward-t directed arborescence count from the reduced outgoing Laplacian. Then

1 ≤ τ_t ≤ Π_{v != t} o_v ≤ n^(d−1),       1 ≤ N(M;s,t) ≤ d^n.

Hence τ_t has O(d log(n+1)) binary digits; the exact complete Euler value-word population and a rank have at most 1+n log2 d bits (up to rounding). All integer cofactors and Cramer numerators of a reduced (d−1)×(d−1) Laplacian with entries bounded by n have O(d log(d(n+1))) bits by Hadamard's inequality. Factorial intermediates in the matrix-tree/BEST population formula have O(n log(n+1)) bits. Thus the determinant/cofactor/rational-solve and factorial method has polynomially bounded exact operand sizes; any complete selected history still emits n+1 signed tokens.

Proof. An in-arborescence to t chooses one outgoing edge instance for every nonroot vertex. There are at most Π_{v != t} o_v such choices, of which only some form an arborescence. Each Euler word with fixed first token has at most d options for each remaining letter, so N≤d^n. For a square matrix with entries of magnitude ≤n, Hadamard gives |det|≤(sqrt(d−1)n)^(d−1); Cramer column replacement by a unit vector satisfies a similar bound. The elementary factorial inequality log2(k!)≤k log2(k+1) gives the remaining bit bound. QED.

This theorem supplies precise bit-size constraints for the Stage495-B one-solve successor formula. Real wall-clock speed, memory allocator costs, source preprocessing and serialisation are measured separately. Any complexity claim must include actual multiplication/division costs, not merely the arithmetic-operation count.

## Executed exact evidence — independently reproducible source paths

REPRO_STAGE496B.py was executed locally using Python standard library exact integers: 14,641 exhaustive concatenation pairs from all words of length ≤4 over {A,B,C}; 64,000 exact associativity triples from words of length ≤3; full length-4 fixed-index SET separation search; 32 deterministic-seeded traces of 125 operations over all twelve X6 signed directions, totaling 4,000 indexed/append/pop/insert/delete/set operations. After every dynamic step, the implicit-treap root summary and in-order word were independently checked against direct scanning. Max random word length 40; all assertions passed. Complete actual output: REPRO_STAGE496B_EXECUTED_STDOUT.json.

REPRO_BIT496B.py was also executed with exact Python integers and fractions. Starting with all 144 directed types once, add 120 copies AA, 37 BB, 13 CC, and 22 copies each AD/DA to maintain Euler balance: 358 directed edges, 144 active relation types, maximum multiplicity 121. Exact population: 165 decimal digits and 546 binary bits; rooted arborescence determinant 39 bits, simple product bound 45 bits; selected midpoint rank serializes to 69 bytes. On eighteen consecutively selected viable prefixes, the Stage495-B one-solve successor-block oracle agreed exactly with a fresh determinant recount for every candidate edge. In this single Python execution, total observed fast oracle time 13.748 ms, fresh-recount reference 41.463 ms. Both methods include their shared count recomputation and arithmetic in the tested function, so the quoted measurement describes this specific implementation and inventory. Complete actual output with per-prefix timings: REPRO_BIT496B_EXECUTED_STDOUT.json.

## External comparison and continuation

The directed matrix-tree theorem and BEST enumeration formula are classical. Ben Bals, Solon P. Pissis and Matei Tinca, "Optimal Enumeration of Eulerian Trails in Directed Graphs", arXiv:2603.12894, first posted 2026-03-13; arXiv v3 revised 2026-08-11 (the PDF header is dated 2026-08-13), report O(m+z_T) compressed-output enumeration. Their enumeration objective differs from fixed-inventory *single-rank* selection, but is a relevant baseline. URL https://arxiv.org/abs/2603.12894. An implicit sequence tree with a monoid aggregate is an established data-structure method. The specialized X6 endpoint-recovery algebra here is an observer-specific derived interface; no external algorithm novelty or priority is claimed.

Next Stage497-B: characterize a **bounded-horizon exact deletion/summarization certificate** for hidden interior blocks using reachability of edit indices under public inserts/deletes/pops/appends; seek minimal counterexamples for h=1,2,3. Independently compare the Stage495-B ranking oracle with directed Euler trail enumeration using end-to-end parsing, factorial/preprocessing, exact bit/memory and output costs, including support-drop and skewed inventories. Native ownership, CLAIM, RESULT and independent Driver review require their actual service-authenticated records.
