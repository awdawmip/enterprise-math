# EC49FAF — Exact pairwise-relaxation obstruction for the frozen H8/M5 signed-X6 BRC problem

**Date:** 2026-11-04. **Status:** author-side exact finite mathematical certificate; Source-native CLAIM/Result and independent Driver review pending. Existing Draft PR #1730. Scientific source fixed at Enterprise Math \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\` and account scientific input \`773d538180bfb49e24cffeb35c3ee75eb0628e2e\`. Current behavioral rules read independently from canonical main.

## Theorem FA(F)-1: the five-fiber pairwise prefix-capacity relaxation is exact *as a relaxation*

Consider exactly the 12,356 double-collision fixed schedules of the immutable EC49EXY candidate TSV, each with five complete BRC-cache fibers, frozen h=2,...,8, and exact observer-admissible signed-X6 prefix capacity \`C_ij\` obtained as the maximum across the windows attached to fibers \`i,j\`. For each integer depth \`d>=1\`, let \`G_d\` have only live fibers (\`L_i>=d\`) as vertices and put an incompatibility edge \`ij\` precisely when \`C_ij<d\`.

**Result:** Every \`G_d\` from this complete finite catalog is **co-chordal** (its graph complement is chordal), hence perfect. Even without removing inactive fibers, thresholding the five full-fiber capacities never produces an induced \`C5\` or induced \`2K2\`. A complete independent threshold-interval test over all 12,356 schedules and all 12 cyclic orders / 15 two-edge matchings returned zero forbidden thresholds. The complementary depth-scan checked 236,896 active-depth instances and found zero \`C5\` and zero \`2K2\`, while finding 1,220 depth instances with an induced \`C4\` and 792 with an induced \`P4\`.

At a fixed depth let \`q_i\` be the conservative nonnegative integer number of distinct prefixes required from cache fiber \`i\` under EC49EXY's existing per-fiber observer bounds (inactive fibers have demand zero). A physical prefix may serve multiple fibers only if they are pairwise compatible. Its grouping therefore induces a coloring of the graph obtained by replacing each vertex \`i\` of \`G_d\` by a clique of \`q_i\` twins. Since \`G_d\` is perfect, repeated vertex replication retains perfectness. Hence its chromatic number equals its clique number, which is

\`\`\`
min number of colors allowed by only pairwise capacities and q_i
   = max_{J subset of active fibers, all pairs ij in J incompatible}
        sum_{i in J} q_i .
\`\`\`

This is exactly the **per-depth term already used in the EC49EXY incompatibility-clique lower bound**. Therefore replacing that clique calculation by an exact weighted multicoloring optimizer cannot improve the per-depth lower bound on this catalog. The claim concerns the *pairwise-capacity relaxation*: realizable paths have additional constraints, including triple-wise common-prefix existence, exact color/observer assignment, and consistency of a tree across depths. These remain fruitful sources of stricter bounds.

Proof of co-chordality: on at most five vertices, every induced cycle in the complement of length >=4 is either an induced \`C4\` (equivalent to \`2K2\` in the original graph) or an induced \`C5\` (self-complementary). Both are absent by exact finite enumeration. Chordal graphs and their complements are perfect. The weighted conclusion follows by vertex replication. For background the standard theorems are Lovasz's replication and perfect-graph theorem and Chudnovsky–Robertson–Seymour–Thomas (2006), *The strong perfect graph theorem*, Annals of Mathematics 164:51–229 (DOI 10.4007/annals.2006.164.51).

### Finite witness / checker completeness

1. Source input: EC49EXY \`EC49EXY_DOUBLE_CANDIDATES.tsv\`, Git Blob \`61ffbcdba1679479fade3cfd052c2d9d6bbf30ce\` (12,356 rows); paired with published \`EC49EXY_CAPS_TABLE.txt\`, 164 rows indexed by \`(h,u,v,w)\`.
2. Construct all five fiber/window groups from the four collision windows and three residual singleton windows; for each distinct cache pair take the maximum of the already exact observer-admissible capacities over its declared window cross-product.
3. For every one of the 12 Hamiltonian \`C5\` patterns check if \`max_{edge}C_ij < min_{nonedge} C_ij\`. Such a strict inequality is necessary and sufficient for that pattern to be a \`C5\` at **some integer depth**, before applying active-length restrictions. For every one of the 15 potential induced \`2K2\` patterns on four of the five fibers check the same strict inequality over its two edges and four nonedges. None succeeds. Their largest margins \`min_nonedge-max_edge\` are both zero.
4. Independently scan each active integer depth \`1<=d<=max_i L_i\` and construct the actual graph by \`C_ij<d\`, removing inactive fibers. Check induced subgraphs by degrees and edges. Outcome: 236,896 graphs, 0 induced \`C5\`, 0 \`2K2\`, 1,220 induced \`C4\`, 792 induced \`P4\`, 127 distinct labeled active-graph signatures.

The full exact checker is \`VERIFY_EC49FAF.js\` (Node.js, standard library only). Run \`node VERIFY_EC49FAF.js EC49EXY_DOUBLE_CANDIDATES.tsv EC49EXY_CAPS_TABLE.txt > EC49FAF_REPORT.json\`; compare with the published \`EC49FAF_REPORT.json\`. In this research execution the same \`audit\` function was actually evaluated in a JavaScript V8 isolate against the exact source table bytes fetched by the authenticated GitHub connector. This is an author-side exhaustive finite certificate; no independent Driver admission is asserted.

## Mother problem and next work

The existing exact 76-edge witnesses and prior exclusions are retained. At the verified EC49FAE frontier, **3,144 schedules / 1,572 symmetric pairs** remain unexcluded for a strict \`E<76\` construction; the author-side global range is still **\`63<=E*<=76\`**. This result prunes one algorithmic direction: an exact per-depth multicoloring replacement alone produces no new lower bound in this particular 12,356-case catalog.

**Next EC49FAG:** seek a *realizable* multi-fiber depth-d capacity refinement. In particular compute, on the smallest previously unresolved orbit representative, the set of joint observer-admissible common signed prefixes for triples of distinct BRC keys, and compare it with pairwise \`C_ij>=d\` compatibility. A triple that is pairwise compatible but has empty triple intersection yields a strictly stronger hypergraph obstruction. After verifying that concrete obstruction and its depth cost, recompute the strict-76 lower bound on the orbit and transfer any valid certificate by EC49FAE symmetry; otherwise pursue multi-depth consistency or exact trie DP for that representative. Preserve immutable input pin, rank-nine observers and exact signed native steps.

## Authority and storage

GitHub author identity is \`awdawmip\`; no native Researcher-ID is asserted. The Enterprise Math Sites connection is configured read-only with \`research_authority_granted=false\`; a bounded live owner query returned \`CONTROL_QUOTA\` on 2026-11-04. This Source research note is an author-side Draft-PR result, not a native CLAIM or Result. P000 / ACTIVE Heartbeat World unchanged.
