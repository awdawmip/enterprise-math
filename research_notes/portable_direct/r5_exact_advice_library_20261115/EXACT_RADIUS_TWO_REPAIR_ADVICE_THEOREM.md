# R5: exact radius-two repair-library cardinality and cube-domatic classification

Date: 2026-11-15. Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Scope: auxiliary one-dimensional integer indexed-center observer, not native X6.

## Model and inherited dependency

For each integer m>=1 take event gaps \`(3,2,2,3,(2,1)^m)\`, radius 2 and K=m+3 selected event-index centers. Minimize total nearest-center integer distance, subject to radius-2 coverage. Closure a shortens gap 0 from 3 to 2; closure b shortens gap 3 likewise.

For t in {0,a,ab}, F_t(m) is the complete optimum center-set family. The all-m optimizer-product lemma, proved in PR #2427 commit \`669c96f388bb2d84ef297e9a2ee09a5751c97353\`, \`research_notes/portable_direct/r5_nonisolating_pair_block_20261115/COUPLED_21_UNBOUNDED_SWITCH_THEOREM.md\`, gives

\`F_t(m) = {C union H : C in G_t, H in {0,1}^ell}\`, ell=m-1,

with disjoint core and suffix supports, G_t=F_t(1). One suffix bit selects one index of its own designated event pair. For these equal-cardinality sets,

\`delta(C union H,D union J) = |C\D| + Hamming(H,J)\`.

In seven-event cores, \`G_0={0125,0135,0235,0245,0246}\`, where digit strings are index subsets. Enumeration of all 35 four-center combinations in each mask gives core optimum cost 5 and sizes |G_0|=5, |G_a|=12, |G_ab|=17.

Define the precommitted repair library size at radius 2:

\`kappa_t(m,2)=min{|L|: L subseteq F_0(m), forall S in F_t(m) exists T in L with delta(S,T)<=2}\`.

## Theorem 1 — exact cardinality for every m

For all integers m>=1,

**\`kappa_a(m,2)=kappa_ab(m,2)=max(2,2^(m-1))\`.**

Thus the values for m=1,2,3,4,5,... are 2,2,4,8,16,... . The previous asymptotic exponent 1 is sharpened to an exact finite-m formula.

**Lower bound.** Choose old cores \`D_L=0135\` and \`D_R=0246\`. The core \`C_*=1346\` belongs to both new families G_a and G_ab and has distances to the five old cores in the displayed order exactly \`(3,2,3,3,2)\`. An old configuration repairing \`C_* union H\` within two swaps must therefore be *exactly* \`D_L union H\` or \`D_R union H\`: even one suffix mismatch costs too much. There are 2^ell distinct suffixes, hence at least 2^ell old configurations are necessary.

For ell=0, no singleton suffices: to repair \`1346\`, an old core must be D_L or D_R. But D_L is distance 3 from the new core \`0246\`, while D_R is distance 3 from the new core \`0135\`. Both new cores belong to G_a and G_ab. Therefore kappa_t(1,2)>=2.

**Upper bound.** For ell>=1, store precisely one old configuration per suffix word H: use \`D_L union H\` if H's first bit is 0, and \`D_R union H\` if it is 1. This gives 2^ell members. The complete core distance table for *either* t=a or t=ab has only three possibilities for each new core C:

(A) \`delta(C,D_L)<=1\`; (B) \`delta(C,D_R)<=1\`; or (C) both distances equal 2.

In case (A), the library contains D_L with suffix H or with the first bit flipped, so replacement distance is at most 1+1=2. Case (B) is symmetric. In case (C), whichever of D_L and D_R is stored with suffix H is exactly two swaps from C union H. This covers every optimum new configuration. For ell=0 store both D_L and D_R, whose two-center core coverage follows from the same table. Lower and upper bounds coincide. QED.

The exact exhaustive core partition for t=a is:
- (A) \`0125,0135,0235,0345,1235,1345\`;
- (B) \`0245,0246,0346,1246\`;
- (C) \`1245,1346\`.

For t=ab it is:
- (A) \`0125,0135,0136,0145,0235,0345,1235,1345\`;
- (B) \`0146,0236,0245,0246,0346,1246\`;
- (C) \`1236,1245,1346\`.

## Theorem 2 — classify every minimum library for m>=2

Let ell=m-1>=1. Because the lower-bound core C_* forces at least one of \`D_L union H\` or \`D_R union H\` *for each H*, a library of minimal size 2^ell must choose exactly one of those two old cores for each suffix H. Therefore minimum libraries correspond to two-color functions \`f:{0,1}^ell -> {L,R}\`.

The common new cores \`C_L=1235\` and \`C_R=1246\` have respective distance pairs to (D_L,D_R) equal to \`(1,3)\` and \`(3,1)\`. Repairing C_L union H requires an L-colored suffix at Hamming distance <=1 from H; C_R analogously requires an R-colored suffix. The three-class core certificate in Theorem 1 proves that these two requirements suffice for every core.

Thus **the exact minimum libraries are in bijection with two-colorings of the binary ell-cube in which every closed Hamming radius-one ball contains both colors** (equivalently, a 2-domatic partition of the hypercube). Coloring by the first bit always works.

The count of such minimum libraries, from exhaustive color enumeration, for ell=1,2,3,4 is exactly **2, 6, 118, 29030**, respectively. These counts are finite claims, distinct from the all-m structural theorem.

## Verification and continuation

\`VERIFY_R5_EXACT_ADVICE_LIBRARY.py\` reconstructs the exact seven-event cores independently from all 35 candidate center sets per mask, tests the core distances and partition, constructs all-m witness libraries for ell=0..7 and checks all new core/suffix pairs for coverage. It tests the two-color characterization against actual library coverage for all colors with ell<=3 and a deterministic subset at ell=4; the graph condition itself is counted exhaustively for ell=1..4. All tested assertions pass. \`EXACT_R5_ADVICE_LIBRARY_SUMMARY.json\` records results, frozen pin and test coverage. All arithmetic is exact integer.

This refines the earlier \`BLIND_RECOURSE_AND_LIBRARY_COMPLEXITY_THEOREM.md\` and \`EXPONENTIAL_ADVICE_RATE_COROLLARY.md\` in PR #2427. The earlier exact \`kappa_b(m,1)=2^m\` remains valid. The same-suffix forcing witness is the newly identified *irreducible core residual* that invalidates the generic Hamming-sphere lower-bound scale for this case.

Next problem: find a corresponding forced-suffix certificate and a domatic-type characterization for finite-state *coupled*, non-product suffix kernels, and determine what compatibility condition replaces the free first-bit flip. Preserve P000 and frozen science as separate from the auxiliary integer observer. No formal Task/CLAIM/Review acceptance is asserted.
