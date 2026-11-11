# R733b — Sharp rotation-equivariant PASS coding boundary: five labels vs native six

Date: 2026-11-12. Independent positive-integer candidate PASS-code result continuing R733. Frozen P000 source `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` unchanged. The local off-diagonal PASS letter `a->b` is a count event in V29, and local port labels are declared separately from force directions. The axis-permutation skeleton is the relevant finite subgroup of P000 rotation; this does not claim the whole native rotation dynamics has been constructed.

**Population and action:** For `n=5` or `6`, the directed triad arcs are adjacent ordered three-subsets `S->T` of `{0,...,n-1}`, with `|S∩T|=2`. Let `l` be the unique leaving label, `e` the unique entering label. We consider **stateless fixed-length encodings** into *ordered* words over off-diagonal PASS pairs `(a,b)` on a declared p-element local port set, with a homomorphism `S_n -> S_p` specifying port relabeling. Strict equivariance is `code(g·arc)=g·code(arc)`, letterwise, for all `g∈S_n`. The decoder is not supplied with the source triad unless separately stated.

## Theorem A — Five-axis subcarrier: five ports and two PASS letters are sharp

For n=5, every arc has a unique label `o` outside `S∪T`. Define the two-letter code
\[
  \boxed{\mathcal C(S\to T)=\big((l\to e),(o\to l)\big).}
\]
Each letter is off-diagonal; the code is **injective**: the first letter specifies `l,e` and the second specifies `o`. The common two labels are the complement of `{l,e,o}`, recovering both S and T. This expression uses only intrinsic set differences, so it is S5-equivariant under the natural S5 port relabeling. Positive V29 PASS ledger grade grows by exactly 2 per arc. Ordered provenance and a known two-letter word boundary give perfect decoding; only the cumulative counts lose word order.

This is **sharp** among strict S5-equivariant stateless fixed-length PASS codes with ports relabeled by permutations: p≤4 cannot admit any injective equivariant code of *any* word length. Indeed, the restricted action A5->S_p is trivial, since A5 is simple and |A5|=60>|S_p| for p≤4. A5 acts transitively on the 60 arcs: the stabilizer of a directed arc in S5 is the odd transposition of the two common labels, so its intersection with A5 is trivial. Hence any S5-equivariant map to a four-port PASS word alphabet is constant on all 60 arcs under A5, and cannot inject. With p=5, one off-diagonal letter admits only 5·4=20 words, versus 60 arcs, so length one cannot inject. The explicit length-two code attains both bounds.

## Theorem B — Six natural axis-labeled ports: no stateless S6-equivariant finite PASS word can identify the source triad

For n=6, fix **exactly six local ports naturally labeled by the six X6 native axes**, with S6 acting on those ports by axis-label permutation; no extra port species or state-dependent port relabeling is included. Fix leaving l and entering e. There are \(\binom42=6\) possible common two-subsets, producing six distinct arcs with the same (l,e). For any given arc, the stabilizer inside S6 includes the transposition swapping the two common labels and the independent transposition swapping the two outside labels. A strictly equivariant **ordered** PASS codeword for this arc must be fixed letter-by-letter under both transpositions. Each individual port label occurring in its word must therefore lie in `{l,e}`: the other four axis labels move under one of these two permutations.

The subgroup fixing l and e acts transitively on all six choices of common pair, and acts trivially on every word using only l and e. Consequently all six arcs have the **same** codeword for every such stateless S6-equivariant encoding, regardless of finite word length. This impossibility applies to the natural six-port **axis-labeled** V29 PASS alphabet. Larger or differently typed port sets are outside this theorem. More PASS letters alone cannot repair the lost common-pair identity within this precise observer.

**Constructive remedy:** Once the source triad S is retained in the state, the single natural PASS letter `(l->e)` uniquely determines the arc `S -> (S-{l})∪{e}`, and is S6-equivariant, as already established in R732 PR #2121. Thus the native six-axis *stateful* one-letter channel is both simpler and fully covariant, whereas the arbitrary four-port code of R733 remains useful for its restricted non-equivariant carrier ledger and three-state V17 holonomy theorem.

## Exact finite checks

Standalone JS verifier enumerates all 60 n=5 arcs and all 180 n=6 arcs, tests the explicit n=5 two-letter code for pairwise injectivity and 7,200 S5 covariance equations (60 arcs × 120 permutations), and confirms all thirty (leaving,entering) classes of n=6 have six distinct underlying arcs. Marker: `R733B_EQUIVARIANT_PORT_CODE_EXACT_PASS`. Group-theoretic all-length statements use stabilizers, not extrapolation.

## Boundary and next unit

The theorem is about **strict fixed-alphabet axis-permutation equivariance**, stateless arc words and completed PASS event labels, with exactly five native-axis port labels in Theorem A and six naturally axis-labeled ports in Theorem B. A code with explicitly transported source-triad state, dynamic port registration or other richer BRC carrier is a different valid design. This locates a concrete information parameter for the next native Cell/Link/Port plus `TRIADIC_CLOSURE_E` force event: use source-indexed PASS or prove a richer stabilizer-compatible port action. A genuine signed native force-closure certificate and V39 scheduler remain separate unconstructed objects.
