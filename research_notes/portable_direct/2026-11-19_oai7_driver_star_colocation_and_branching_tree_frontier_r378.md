# OAI7 r378 — Star co-location rigidity and the remaining prime-29 branching-tree search domain

Date: 2026-11-19. RESEARCH_DRIVER author-side proof and synthesis, preserving original OAI7 researcher EM-EMF6D046-5A2844, Task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19, and Driver historical EM-DVR-DEBB5E. Not an independent Native review or formal Result acceptance.

## New exact lemma: contracted stars force connector translation equivalence

Use the r360 assumptions: G=Z/pZ, p>=3, gcd(N,p)=1, m>=p-1 strictly positive integer-numerator profile masses n_x/N, S=m+p-1 positive supported atoms, exactly p-1 degree-two connector profiles and all other profiles singletons; all d coordinates have uniform p-residue marginals. Suppose the first-coordinate contracted residue tree is a star with center a and p-1 leaves.

**Lemma.** Every degree-two connector profile has the same ordered relative-offset vector (w_(x,2)-w_(x,1),...,w_(x,d)-w_(x,1)). Thus whenever at least two connector profiles must be pairwise inequivalent under common translation, a uniformly marginal sharp-support star is impossible.

**Proof.** Let e_x^c be the labeled atom of connector profile x placed at the first-coordinate center a, and e_x^\ell the atom at that profile's leaf. Deleting e_x^c from the full bipartite incidence tree leaves its degree-two profile attached to exactly one residue vertex, so c(e_x^c)=1. Deleting e_x^\ell leaves the profile attached to the center and the other p-2 leaves, so c(e_x^\ell)=p-1.

By r360 every other uniform coordinate is another bipartite spanning tree preserving each atom's c value. Suppressing the degree-two profiles gives a tree T_i on p residues, where every connector has an atom whose opposite-side residue count is 1. Hence every edge of T_i is a leaf edge. Every finite tree with p>=3 vertices all of whose edges are leaf edges is a star. Moreover the center-labeled atom e_x^c of every connector must lie at the center a_i of this new star, because it is the atom with c=1 (the opposite component consists of the single leaf residue).

Every e_x^c was originally at the same a and must be at the same a_i in coordinate i, so its profile-specific relative offset is a_i-a, independent of x. This holds in every coordinate, proving the lemma. QED.

The proof does not assume p odd; it complements the odd-p universal path no-go in r377 and the separately established double-star classification in r371.

## Necessary remaining graph class for p=29, S=378

For the exact OAI7 finite law, p=29, m=350, gcd(N,p)=1 and all 350 profile shapes are pairwise translation-inequivalent. At support 378 and with exactly 28 degree-two connector profiles, their contracted residue graph T is a tree with 29 vertices.

The following already verified implications can now be synthesized with the new star lemma:

* T is **not a path**, by the central pair obstruction r377 for any odd p.
* T is **not a star**, by the lemma above, for any p.
* T is **not a proper double-star** (tree diameter exactly 3, with two adjacent hubs bearing leaves), by r371's established exact odd-order hub-gap obstruction; every nonzero g in Z/29Z has odd additive order 29.

Since a nontrivial tree has diameter 2 exactly when it is a star and diameter 3 exactly when it is a proper double-star, every surviving degree-two-only contracted graph must satisfy

\[
\boxed{\Delta(T)\ge3,\qquad \operatorname{diam}(T)\ge4,}
\]

where \Delta(T) denotes maximum vertex degree. These are **necessary structural conditions**, not existence certificates. The other remaining S=378 alternative is one or more profiles of supported translation degree >=3, to which the degree-two-only tree classification does not directly apply.

### Reusable forced-co-location pruning criterion

Fix one first-coordinate labeled tree T and two distinct connector profiles x,y having atoms at the same first-coordinate residue a. Consider the **entire** set of allowable other-coordinate labeled connector placements satisfying the exact individual r360 residue-cut counts, connector endpoint-difference constraints and connected residue-tree condition (a stronger input filter may also enforce full integer cut sums and strict weights).

If those two originally co-located labeled atoms remain co-located for **every** allowable placement, then every uniform coordinate has identical relative offsets for x and y. Consequently W_x and W_y are common translates and this first-coordinate tree is excluded when the shapes are pairwise translation-inequivalent.

This criterion is a necessary exclusion test for a proposed tree, not a claim that any arbitrary edge relabeling is geometrically realizable. r377's middle path atoms and the star-center atoms are two exact instances. It suggests testing forced co-location groups on smaller non-star, non-double-star branching trees before applying the expensive 350-profile cut-numerator check.

## Preserved scientific frontier and provenance

The global OAI7 exact five-uniform support question remains 378 <= S_min <= 490. No mathematical statement here declares the entire endpoint impossible. The next useful exact branch is **degree-two contracted branching trees with maximum degree >=3 and diameter >=4**, and separately the higher-translation-degree support allocations; both require the actual 350 profile offsets and masses for positive feasibility.

r371 fixed hub-gap double-star classification: https://github.com/awdawmip/enterprise-math/blob/05b19e2ff943a13749cf6033437dfd000ba5e578/research_notes/portable_direct/2026-11-19_oai7_driver_arbitrary_gap_double_star_order_classification_r371.md

r377 universal odd-path no-go: https://github.com/awdawmip/enterprise-math/blob/7ef629095246e2a54625f19504812e4724d96886/research_notes/portable_direct/2026-11-19_oai7_driver_universal_odd_path_skeleton_no_go_r377.md

r360 simultaneous tree-cut signatures: https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md

This is saved scientific evidence; no new Native Result/Review, Source/Activity association, CLAIM, formal Task DONE, or mother-objective closure is asserted.
