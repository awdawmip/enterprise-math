# R762CVb — Sharp two-branch minority-Port BRC under signed-triad symmetries

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS. **Researcher:** EM-X6-3050F6. **Date:** 2026-11-17. **Status:** complete finite algebraic proof and author exact checks; independent review NOT_REVIEWED.

**Frozen source:** P000 V5 @a72226e2430ffa4786321ac86e7f0c599d5f0389; R762CU @15374751a4ce6931b5a4bc83f68c27f756320bb6. See the companion R762CV deterministic classification in the same PR for the exact signed-triad type and S6 action. No native TRIADIC_CLOSURE_E event licence is assumed.

## Theorem — two branches are necessary and sufficient for a changed mixed-sign triad

Restrict the 160 signed three-Port candidate structures to the 120 mixed-sign structures (one or two negative Ports). Require successor triads to preserve their exact three occupied axes and their number k of negative Ports, and require the nonnegative integer transition multiplicities to be S6-equivariant. For every mixed T, the stabilizer H=S_A×S_B×S_C acts on the same-support, same-k candidate successors in exactly two H-orbits: the singleton {T} and one two-element orbit consisting of the two triads obtained by moving the **unique minority sign** to either of the other two Port axes.

Therefore, if a successor law has no self-successor and produces any candidate at all, its number of distinct successors at each mixed state is at least **2**. The bound is attained by the canonical positive N-BRC kernel K(T,U)=1 precisely for the two minority-sign relocations U; K(T,U)=0 otherwise. The two successors carry distinct named Port provenance. In contrast, deterministic unmarked F:T→T cannot change a mixed-sign state under the same support/sign-count constraints (companion R762CV Theorem 2).

**Proof.** For k=1, the one negative axis a is fixed by H, while the positive pair {b,c} is transposed by the S2 subgroup of H. Among all same-support, one-negative targets, the only choices are to place the negative sign at a, b or c. These form the singleton {a} and the transitive H-orbit {b,c}. An H-invariant successor multiset must assign equal multiplicity to b and c. A nonempty no-self transition thus contains both, and two unit branches attain the lower bound. For k=2 reverse the signs and use the unique positive axis as the minority. S6 acts transitively on each Ω_k, proving the global assertion. ∎

## Exact graph and path-count theorem

For each of the 20 possible three-axis supports and each of the two mixed sign-count types k=1,2, there are exactly three placements of the minority Port. The canonical two-branch transition graph is therefore the disjoint union of **40 copies of K3**, with **120 states** and **240 directed edges**. Each component has adjacency matrix A=J3−I3.

The exact positive N-BRC branch count from minority position i after t steps is

\[
(A^t)_{ij}=
\begin{cases}
\displaystyle \frac{2^t+2(-1)^t}{3},&i=j,\\[5pt]
\displaystyle \frac{2^t-(-1)^t}{3},&i\ne j.
\end{cases}
\]

Both expressions are nonnegative integers for every integer t≥0. The full total is 2^t. The eigenvalues per component are 2,-1,-1, and after row normalization the two nontrivial eigenvalues are −1/2.

**Proof.** A=2P−(I−P), where P=J3/3 is the projection to constants; P and I−P are complementary idempotents. Hence A^t=2^tP+(-1)^t(I−P), yielding the formula. Nonnegative integrality follows independently from integer adjacency powers and combinatorial path counting. ∎

## Observer and source-provenance boundary

The k-only observer (or a total branch counter) reports 2^t from every state at depth t and loses the initial minority Port. A future operation allowed to ask for named-Port placement separates the three starting states immediately, so the port coordinate is a genuine source-provenance repair for that future language. The kernel is a **candidate** native transition, not a claim that actual Force-Port rotation transports follow it. A legal Cell/Link/Port event predicate, signed area and V17/V29/V39 path transport must be sourced before interpreting these N-BRC counts as heartbeat dynamics.

## Verification

Standard-library R762CV_MINORITY_BRC_VERIFY.py checks all 120 states, all 720 permutations (**86,400** equivariance equalities), 40 K3 components, 2 outgoing successors per state, all exact diagonal/offdiagonal path counts for horizons 0...30 (**11,160** path equalities), and the involution/sign-count/support properties; JSON results are in R762CV_MINORITY_BRC_EVIDENCE.json. The analytic proof covers every t≥0. Independent mathematical review NOT_REVIEWED.

**Next:** test the sourced TRIADIC_CLOSURE_E event law against deterministic rigidity versus two-branch minority relocation and compare its named-Port/path-area future observers with the retained BRC provenance.