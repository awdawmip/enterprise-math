# R762AQ — Baseline-free adaptive reset diagnosis: exact three-query/three-letter bounds

**Status:** AUTHOR_PROVED_CONDITIONAL; exact finite author verification; NOT_REVIEWED / NOT_NATIVE_ADMITTED.
**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
**Researcher provenance:** EM-X6-3050F6 (original SID MCP-4b2d70a97f594366a7c94a0f8b45df38).
**Frozen scientific task input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
**Predecessors:** R762AM and R762AN at Draft PR #2421; R762AP at Draft PR #2429. Reuse the same AK4 auxiliary automaton, not an asserted native P000 Cell/Link/Port event.

## Statement

With no initial observer output, but with independently resettable, terminal-only experiments whose words may be chosen adaptively, the nine-state AK4 observer system has sharp worst-case diagnosis costs

\[
N_{\min}=3\ \text{nonempty reset queries},\qquad
L_{\min}=3\ \text{primitive event letters}.
\]

The same policy achieves both minima. The result holds for the eight live states alone and for the eight live states plus absorbing failure state U.

The exact finite optimal uniform-prior expected costs, calculated by full word-monoid closure and a complete subset dynamic program, are:
- Eight live states: 17/8 queries and 19/8 letters.
- Eight live states plus U: 19/9 queries and 21/9 = 7/3 letters.

The expectation optima are certified exhaustively for this nine-state model rather than claimed for arbitrary automata.

## Definitions and typed observer

Let E=012, c=120, t=102 be image-notation permutations in S3, with (pq)(i)=p(q(i)).
The eight live states are
\[
X_{\mathrm{live}}=\{(0,E),(1,E),(2,E)\}\cup
\{(0,h): h\in S_3\setminus\{E\}\}.
\]
Adjoin the absorbing state U. The partial source/frame actions totalized by U are
\[
S(s,E)=((s+1)\bmod3,E),\quad C(0,h)=(0,ch),\quad T(0,h)=(0,th).
\]
All unlisted applications go to U, as do all actions from U. The observer O distinguishes U; otherwise its source component is E at s=0 and C at s!=0, while its frame component is the frame cycle type E/C/T. Its entire terminal alphabet is precisely {EE,CE,EC,ET,U}, of cardinality five.

A probe is a nonempty, ordered word w over {S,C,T}, applied to a fresh reset copy of exactly the same unknown original x. It produces only O(wx), never an initial O(x). The next probe can depend on prior terminal symbols. Each probe costs one query and |w| primitive letters. All quantities and enumerations are exact finite integers.

## Optimal constructive policy

First query T. Its possible outputs and continuation rules are:

| T result | Original candidate set | New probes and terminal decisions |
|---|---|---|
| EE | one frame transposition (0,t) | Stop |
| U | (1,E), (2,E), U | Query S; CE, EE, U identify the respective originals |
| ET | (0,E), (0,c), (0,c²) | Query S; CE identifies (0,E); if U then query C; EC identifies (0,c), EE identifies (0,c²) |
| EC | the other two frame transpositions | Query CT on a fresh copy; its EE and EC outputs distinguish the pair |

The deepest branch uses three single-letter reset probes T,S,C. The other expensive branch uses T followed by the two-letter probe CT. Therefore the worst case is at most three queries and three primitive letters. The attached exact checker verifies every initial state's unique decision path.

## Analytic sharp lower bound for all finite query words

**Coset lemma.** Fix either the even permutations A3={E,c,c²} or the three odd transpositions. For any finite word w, the terminal observer O(w(0,h)) takes at most two distinct values as h varies over that parity coset.

*Proof.* Before a possible first S, only C and T act on the frame, by left multiplication by a fixed g in S3. This maps a parity coset bijectively onto one of the two parity cosets. If S never occurs, the final observer sees either three transpositions (one output ET) or one identity and two 3-cycles (two outputs EE and EC). If S occurs, at most one member of the original triple has identity frame immediately before S; the other two go to the absorbing state U. Subsequent actions can produce only one further terminal output for the possible survivor. Hence in all cases at most two outputs. QED.

**Theorem (at least three probes).** Assume, for contradiction, that some adaptive policy distinguishes all nine states with at most two nonempty reset probes. Let w be its first query.

**Case 1: w contains S.** If w starts with S, each of the five states with nonidentity frame, as well as the initial U, immediately maps to U: the first query has a terminal U fiber of at least six original states. If w first contains some C/T letters and then a first S, the source states (1,E),(2,E),U already map to U at the first letter; among the six states (0,h), at most one survives the first S because their frames have been permuted bijectively. Consequently at least eight original states have first output U. In either subcase the unresolved first-output fiber has more than five states. A single second terminal probe offers at most the five symbols of O and cannot distinguish that entire fiber.

**Case 2: w contains no S.** Then w consists only of C/T frame actions. They permute the six original states (0,h) bijectively, and precisely three have final frame a transposition. All three yield first output ET. Their original frames form exactly one of the two parity cosets of S3. By the coset lemma, every possible second probe yields at most two terminal symbols on this three-state first-output fiber. Thus a single second query cannot identify all three.

Both cases contradict two-query identification. Hence N_min >= 3. Each nonempty probe costs at least one letter, so L_min >= 3. The displayed construction meets both bounds. QED.

## Complete exact finite verification

The adjacent dependency-free JavaScript checker enumerates the entire monoid of maps on the nine states generated by S,C,T. It has 75 distinct maps and maximal shortest representative length seven. Those maps induce 43 distinct terminal observation vectors when the empty word is included, or 42 with nonempty queries.

For a candidate subset M and word-vector observation partition M_1,...,M_k, every informative query has k>=2 and strictly smaller fibers. Let D and A denote worst query and letter costs, and let D_sum and A_sum denote total costs summed over all equally weighted initial states in M. On singleton subsets all four costs are zero; otherwise
\[
D(M)=\min_w (1+\max_i D(M_i)),\quad
A(M)=\min_w (|w|+\max_i A(M_i)),
\]
\[
D_{\rm sum}(M)=\min_w (|M|+\sum_i D_{\rm sum}(M_i)),\quad
A_{\rm sum}(M)=\min_w (|M||w|+\sum_i A_{\rm sum}(M_i)).
\]
The minimization ranges over one shortest nonempty word for every observation-vector signature. Exhaustive transformation closure makes this sufficient for *all finite words*, not a truncated length search.

The returned exact integer certificate is:

| Initial universe | worst queries | worst letters | summed queries | summed letters |
|---|---:|---:|---:|---:|
| eight live | 3 | 3 | 17 | 19 |
| eight live plus U | 3 | 3 | 19 | 21 |

The checker additionally verifies the constructive policy for each initial state, its unique identification and the cost totals.

## Interpretation and next frontier

AQ identifies the minimal *adaptive reset interface resource* for the declared AK4 source/frame auxiliary model. Provenance consists of ordered query words, reset boundaries and branch-specific observer outputs; collapsing these to a commutative BRC mass would lose the policy's distinguishing history. This is exact combinatorial BRC-path bookkeeping, without any assertion of native physical residual or signed-force cancellation.

The frozen P000 ontology (signed X6, independent time, primitive three-force closure, pairwise native PERP_E) is unchanged. To transfer this theorem to actual TRIADIC_CLOSURE_E, establish source-typed Cell/Link/Port event updates, V29 PASS/TRANSFER provenance, V17/V39 frame/return transport, state-dependent repeated legality, and whether independent reset and terminal readout are admitted.

**Next concrete question:** On the exact native event alphabet, can three permitted source-typed macro-events be carried out from independent copies with the same initial provenance, and does a finite full-state observer distinguish the needed triad sources? Recompute the transition monoid and minimal decision tree for the actual reachable X6 fiber before claiming a native 3-query bound.

No native Result/Driver admission is asserted.
