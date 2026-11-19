# R762GC — Odd-step Cell nonreturn, signed triad BRC fibres, and a one-rotation observer witness

Date: 2026-11-19. Research task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Author-side status: PROVED_WITH_EXACT_CHECK / NOT_REVIEWED.

## Exact frozen scope

Source pins: taskbook research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md at 857280d1012943290d141d1317179c40ec3cbdf8; P000 foundation and native signed X6 torsor at a72226e2430ffa4786321ac86e7f0c599d5f0389. Current behavioral rules are read separately. The spatial coordinate layer is a chosen-chart affine torsor over Z^6, with primitive signed coordinate transitions z -> z ± e_i, and with S6 as the exact axis-permutation rotation skeleton. A coordinate path is not automatically a force-closure event. Pairwise PERP_E among distinct axes and 120-degree native angle remain P000 definitions.

Earlier X6 foundation already establishes nonreturn for a three-positive-step STAR carrier triangle (H_S) and the positive-only common-depth repair. R762GB establishes conditional sign-forgetting invariance of a candidate oriented-cycle BRC marginal. The statements below extend those facts to all signed odd coordinate words, compute the signed three-axis BRC fibre exactly, and give a one-rotation loss-of-observer-sufficiency witness.

## Theorem 1 — No odd-length primitive signed coordinate path returns to its Cell

For any chosen Cell c, any integer odd m >= 1, any axis choices i_1,...,i_m in {1,...,6}, and any signs eps_t in {+1,-1}, the successive native primitive coordinate transitions

    c -> c + eps_1 e_(i_1) -> ... -> c + sum_{t=1}^m eps_t e_(i_t)

have nonzero full signed X6 displacement. In fact the primitive coordinate-neighbour graph is bipartite, with parity class

    chi(c + z) = [sum_{i=1}^6 z_i] mod 2

relative to the chosen Cell anchor. Every primitive edge toggles chi. An odd path cannot have the same initial and final chi.

Proof. For each unit signed coordinate step, sum_i z_i changes by ±1, hence toggles its residue modulo 2. After m steps the parity difference is m mod 2. If the endpoint were the initial Cell, the parity difference would be zero; contradiction for odd m. The difference in chi between two Cells is anchor-independent. QED.

Consequently a triad of three primitive signed coordinate movements never makes a native Cell loop, even with repeated axes and mixed signs. If a P000 primitive three-force closure is to be represented, its closure is a typed force-incidence, Link/Port, field, or other relation; equating it with a literal three-edge Cell-return loop is obstructed by the existing coordinate graph. This theorem makes no claim that primitive force quanta must be executed as three Cell translations.

## Theorem 2 — All-distinct-axis signed three-step BRC fibres

Restrict to three ordered primitive unit steps whose underlying three axes are pairwise distinct (so the selected axes satisfy the P000 pairwise PERP_E relation). Let W_3 be the set of signed ordered paths, with the starting Cell fixed.

1. |W_3| = 6*5*4*2^3 = 960.
2. Every endpoint is a vector z in {-1,0,1}^6 with exactly three nonzero entries. There are binom(6,3)*2^3 = 160 distinct endpoints, each reached by exactly 3! = 6 ordered paths.
3. Every such endpoint has squared native component displacement L_E(z)^2 = 3, and none is a Cell return. Its six paths are shortest signed-axis paths.
4. For exactly j negative selected-axis signs (j=0,1,2,3), there are 20*binom(3,j) endpoints and 120*binom(3,j) ordered histories: endpoint orbit sizes (20,60,60,20) and ordered-history counts (120,360,360,120).
5. If the word order is represented as a cyclic orientation of the three axis labels plus a marked starting position, each signed endpoint has two opposite cyclic orientations and three marked positions per orientation. This is a 2*3 fibre; orientation is preserved as BRC metadata rather than inferred from its endpoint.

Proof. Choose an ordered triple of distinct axes, then one sign for each: (6)_3*8 paths. The signed endpoint records precisely the three-axis support and its three signs. Ordering these selected signed steps changes the path trace but not their sum, yielding exactly six permutations. For every signed endpoint, the fixed component quadratic readout has three unit-square terms. Count the j-negative patterns and decompose S_3 into its two cyclic-orientation cosets of order three. QED.

This is an exact typed path-count theorem, not a theorem of native TRIADIC_CLOSURE_E legality or signed-force cancellation.

## Theorem 3 — Exact relative-observer loss and one-permutation recovery

Fix any ordered axis triple S=(i,j,k), with the other three native coordinates zero. Let W_S be the 48 signed, ordered, pairwise-distinct-axis paths supported on S. The full endpoint is z=(eps_i,eps_j,eps_k) on S. Let

    q_S(z) = (z_i,z_j,z_k) - min(z_i,z_j,z_k) * (1,1,1)

be the existing min-zero three-axis relative Cell observer, with fixed path length m=3.

(a) The eight raw signed endpoints produce exactly seven q_S readouts. The two endpoints +H_S and -H_S both map to (0,0,0), and all other signed endpoints have different readouts.

(b) The 48 words partition into seven q_S fibres: one fibre of size 12 over (0,0,0), and six fibres each of size six. Under the uniform positive BRC on the 48 words, the zero-observer probability is 1/4 and each nonzero-observer probability is 1/8. In particular path length three plus q_S does not recover signed common depth for this population.

(c) Let a be any selected axis in S, and b any omitted axis outside S. Let sigma be the coordinate-label transposition (a b) in the frozen S6 axis-permutation skeleton. Then the two presently indistinguishable endpoints separate under the endpoint query q_S(sigma z): up to the ordering of S,

    q_S(sigma (+H_S)) = (0,1,1),
    q_S(sigma (-H_S)) = (1,0,0).

The joint current-and-after-sigma observation therefore has exactly eight distinct endpoint classes, each with six full ordered path histories. A single fixed such swap suffices. Before the swap the endpoint-observer class count is 7; after adding its query it is 8.

(d) For the restricted future operation family generated by signed coordinate translations and permutations stabilizing S setwise, equality of q_S is preserved: if z' - z = k*(1,1,1) on S, then q_S(z'+t)=q_S(z+t), and q_S(pi z')=q_S(pi z) for every pi in Sym(S). Consequently +H_S and -H_S remain q_S-equivalent under this restricted family. An S-to-complement axis swap leaves that restricted family and gives the witness in (c).

Proof. Signed triples consist of two constant-sign triples (all positive and all negative), both normalized to zero, and six mixed-sign triples. For mixed signs the minimum is -1; the nonzero selected positions become 2, yielding six distinct binary patterns. The exact ordered-word multiplicity six per endpoint proves (a) and (b). A selected-to-omitted coordinate swap replaces the chosen coordinate value ±1 by zero in the selected readout; after normalization the displayed vectors differ. The six permutations of each fixed signed endpoint remain indistinguishable by endpoint-only queries, proving (c). Finally differences by a common diagonal shift are invariant under simultaneous translations and selected-coordinate permutations, proving (d). QED.

## Consequences and next discrimination

The exact minimal fixed-length encoding of 48 distinct signed ordered paths is ceil(log2(48)) = 6 bits. The endpoint alone has eight values (3 bits), with a six-word BRC order fibre (3 additional fixed bits). The current q_S observer has seven classes, requiring ceil(log2 7)=3 bits to label its values; its zero-readout fibre requires four bits to distinguish the 12 full words, while other fibres require three. The after-swap query splits only the zero-readout fibre, but does not determine path order.

Full spatial identity, carrier relative readout, 3-axis signed incidence, and BRC trace are distinct. The relevant 120-degree PERP_E rule is preserved: this work never identifies a 3-step geometric Cell loop with primitive three-force closure. If future native Cell/Link/Port permissions include the selected-to-omitted S6 rotation skeleton query, sign/common-depth residual is relevant at horizon one. If not, exact safety is determined by the actual allowed operations; the S-stabilizing family in (d) supplies a positive restricted-scope descent certificate.

Next: extract which of the frozen S6 axis permutations, signed Port interactions and Cell/Link updates are actually executable TRIADIC_CLOSURE_E events. For each admitted event, test the 48-word source bundle for whether it descends to (i) the signed endpoint, (ii) q_S, or (iii) the complete named BRC trace. Retain Source provenance while native authorization is checked separately.

## Reproducible evidence

Companion Node.js integer-only checker R762GC_VERIFY.js and R762GC_EVIDENCE.json. The independent checker enumerates all 960 distinct-axis signed words, all 20 supports, all 180 selected-to-omitted swaps, and all 12^1, 12^3, and 12^5 odd signed primitive-coordinate words (12, 1,728 and 248,832). Exact arithmetic and assertions; no tolerances or numerical approximation. Proven statements hold for all odd m by parity and for every choice of S by the proofs above. Review status: NOT_REVIEWED.