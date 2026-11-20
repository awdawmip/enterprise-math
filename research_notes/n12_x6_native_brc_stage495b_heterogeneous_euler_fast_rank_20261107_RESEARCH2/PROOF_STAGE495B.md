# Stage495-B — One-solve Euler–BRC successor oracle for heterogeneous signed-X6 edge inventories

Status: AUTHOR-SIDE EXACT MATHEMATICAL DERIVATION / EXECUTED INTEGER TESTS / UNREVIEWED / NOT ADMITTED.

Parent: Stage494-B at `69859ba7d61676218a91aa7e53bfb9090426d232`, PR #1736. Frozen scientific source pins: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 original Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral norms read separately. The native alphabet has twelve **signed directions on six spatial axes**, not twelve axes.

## Problem and carrier

A value-word of native directions `w_0...w_n` gives an ordered directed-edge inventory `M=(m_ab)`; its unit positive BRC branch weight is one per distinct value-word. Fix starting direction `s` and terminal direction `t`. The observer records all 144 signed directional relation types, order, endpoint and original population; this is an exact *combinatorial* branch model, not a proposed physical heartbeat or amplitude law. The Stage494-B formula counts

`N(M;s,t) = tau_t(M) * o_t! * product_(v!=t) (o_v-1)! / product_(a,b) m_ab!`

for Euler-balanced, connected nonempty inventories, where `tau_t` is the toward-`t` arborescence determinant of the outgoing directed Laplacian on the actually active vertex set. Empty inventory: `N=1[s=t]`.

## Theorem 495.1 (all support-preserving next-letter blocks from one solve)

Assume `N(M;s,t)>0` and at least one edge. Let `V` be the exact active support including `s,t`, and let `L` be the directed outgoing Laplacian with the `t` row and column removed, indexed by `V\{t}`. Thus `tau=det(L)>0`. For a candidate edge `s→b` with `m_sb>0`, put `M'=M-e_sb` and suppose its exact active support including new source `b` and terminal `t` remains `V`.

The number of complete value-words in that next-letter block is exactly

`B_b=N(M';b,t)=N(M;s,t) * m_sb * tau'_t / (tau_t * (o_s-1+1[s=t]))`.

If `s=t` or `b=s`, `tau'=tau`. Otherwise let `y=L^{-1}e_s`, interpreted on `V\{t}`, with `y_t=0`. Then

`tau'=tau*(1-y_s+y_b)`.

The expression above is an exact nonnegative integer despite intermediate rational numbers. Candidate blocks in native letter order partition the original population:

`sum_(b:m_sb>0) B_b = N(M;s,t)`.

**Proof.** Removing `s→b` changes the outgoing Laplacian by `-e_s(e_s-e_b)^T` (the (b=s) loop changes no Laplacian row). After deletion of the terminal row/column, the matrix determinant lemma yields `det(L')=det(L)*(1-(e_s-e_b)^T L^{-1}e_s)`; when `s=t`, the affected row is absent and the determinant is unchanged. The directed Euler degree balances update from `(s,t)` to `(b,t)`. Take the ratio of the Stage494-B factorial formulas: the single multiplicity factorial contributes `m_sb`; lowering the outgoing degree at `s` contributes the denominator `o_s-1+1[s=t]`. The support-preserving hypothesis guarantees this denominator is positive in the `s!=t` case and that the same Laplacian vertex set is legitimate. The remaining ratio is `tau'/tau`. Each Euler word starts with exactly one candidate `s→b`, establishing the disjoint block partition and integrality.

## Boundary rule and algorithm

If deleting `s→b` changes the active support, recompute the exact Stage494-B population on `M'` with its new support. This happens for an actual viable continuation only when `s!=t`, `o_s=1`, `i_s=0`: the old current vertex disappears, leaving only one possible next edge. Across one completed trail at most `d-1` nonterminal vertices can disappear; hence support changes have a bounded explicit fallback rather than being silently misclassified as zero tree count. Empty residual and self-loops are handled separately.

At each chosen prefix, compute the current `N` and `tau`, solve one exact rational linear system `Ly=e_s` (unless `s=t`), derive all viable next-letter blocks from the formula, then use the usual lexicographic block-subtraction rank/unrank step. With `n` directed edges and `d<=12` active letters, cubic determinant/solve and an at-most-one-fallback-per-support-drop scheme use `O(nd^3+d^4)` arithmetic operations, plus factorial/multiplicity preparation and `O(nd)` block arithmetic. This is an arithmetic-operation bound, **not** a bit-complexity or wall-time speedup guarantee. The exact bit lengths of determinants, fractions, counts, and rank integers are part of the full cost. Output requires `n+1` direction tokens.

## Executed exact checking

Source: `REPRO_STAGE495B.py`. Actual deterministic output: `REPRO_STAGE495B_EXECUTED_STDOUT.txt`.

* All `3+3^2+...+3^7=3279` original value-words over three native directions, grouped in **1554** distinct inventory/endpoint keys, were exhaustively checked: closed-form count, all next-letter block sums, and each value-word rank/unrank against independent raw enumeration.
* A 12-signed-direction, heterogeneous-multiplicity inventory activates **all 144** possible relation types and has **213** edge occurrences. The exact population has **156 decimal digits / 517 bits**. Six boundary/middle ranks underwent full 214-token unrank/rank roundtrips; all reconstructed words exactly match the nonuniform inventory.
* All **213** next-letter block layers along the middle-ranked word were independently compared with direct Stage494-B determinant recounts; **11** support-shrink fallback layers occurred. Six unrank traversals used **1278** successor-oracle layers. Every assert passed.
* Exact integer counts and `fractions.Fraction` solve were used; timing fields are per-run context and are not an external benchmark.

Scientific reuse: existing Stage494-B directed-matrix-tree/BEST value-word population and lex ranking are `EXTEND_EXISTING_TOOL`; Stage495-B adds exact one-solve low-degree successor blocks without collapsing multiplicity or provenance. Exact Python integers in this *combinatorial BRC branch-count interface* do not claim any physical heartbeat residual attribution.

## Next unresolved question

Stage496-B: for two dynamic internal edits amid public INSERT/DELETE/POP/APPEND, decide whether transported initial triples plus changed-center token suffice when the second edit probes a newly created join. Formalize the provenance-aware boundary update and seek a shortest strict word counterexample, or establish a scoped compositional sufficiency theorem. Separately, characterize full integer-bit complexity and real wall-time benefits of the new one-solve oracle on skewed multiplicity inventories.

No native authenticated CLAIM, Result or independent Driver review is asserted by these author-side results.
