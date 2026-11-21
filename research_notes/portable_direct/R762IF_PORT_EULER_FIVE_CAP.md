# R762IF — A universal five-per-support kernel for closed six-axis Port circuits

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_WITNESS_CHECKED / NOT_REVIEWED.

**Frozen scientific input:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, pin \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This is a theorem about the six-axis **composite** Port-transition observer only. It neither replaces nor proves native P000 TRIADIC_CLOSURE_E force/Cell/Link/time/rotation dynamics.

**Direct predecessor:** R762IE Port-component quotient, immutable source \`fd82084fb5f982e825ba7454e34821e723f0931e\`, and the Port definitions used in R762ID/R762IC. No exact finite obstructions from those results are used in the proof below.

## 1. Statement

Let \(X=\{0,\ldots,5\}\), \(V=\binom X2\) (15 Ports) and \(\mathcal S=\binom X3\) (20 three-axis support labels). Every \(S\in\mathcal S\) determines a triangle \(\Delta(S)\) on the three Ports \(\binom S2\). A named occurrence of type \(S\) chooses exactly one of the three **undirected** edges of \(\Delta(S)\); oriented ordering is subsequently supplied by an Euler tour. Let \(N_p(n)>0\) mean that the histogram \(n=(n_S)_{S\in\mathcal S}\) admits a connected, even-degree Port edge multigraph with exactly \(n_S\) named edges of each support and with a nonisolated starting Port \(p\); equivalently, a nonempty legal closed Port history based at \(p\).

Define the **cap-five parity kernel** \(n^{[5]}\) by

\[
n^{[5]}_S =
\begin{cases}
n_S,&0\le n_S\le5,\\
4,&n_S>5\text{ even},\\
5,&n_S>5\text{ odd}.
\end{cases}
\]

**Theorem (exact Port-Euler kernel).** For every integer histogram \(n\ge0\) with \(\sum_S n_S>0\), and every \(p\in V\),

\[
\boxed{N_p(n)>0\quad\Longleftrightarrow\quad N_p(n^{[5]})>0.}
\]

Furthermore \(n_S^{[5]}\equiv n_S\pmod2\), \(\operatorname{supp}(n^{[5]})=\operatorname{supp}(n)\), and \(\sum_S n_S^{[5]}\le100\). Thus a fixed-six-axis arbitrary-multiplicity **Boolean existence** question reduces exactly to one containing at most 100 named events, without fixing or truncating the original event count in its counted or temporal observables. Five is a proven sufficient cap; optimality of the cap is not claimed.

## 2. Constructive proof: original to capped

Start with any legal closed Port history for \(n\), and forget its order temporarily, retaining every edge's support label and its two endpoints. The resulting multigraph \(G\) is connected on its nonisolated vertex set \(U\subseteq V\), has all degrees even, and contains the prescribed starting Port \(p\).

Take a spanning tree \(F\) of \(G|_U\) using **actual named edge occurrences**. Then \(|F|=|U|-1\le14\). For each support \(S\), its possible Port edges form a triangle. A tree cannot contain all three distinct triangle edges, so **at most two tree occurrences have any one support label \(S\)** (and duplicated edges cannot both belong to a tree).

Let \(R=E(G)\setminus F\) be the remaining *occurrences*. For every occurrence \(a\) of type \(S(a)\), with Port endpoints \(u(a),v(a)\), form the binary column

\[
w(a)=(e_{u(a)}+e_{v(a)},\,e_{S(a)})
\in\mathbb F_2^{15}\oplus\mathbb F_2^{20}.
\]

The first component is its Port-degree boundary; the second records the **parity of its specific support label**. Every first component has even total coordinate sum. Therefore all columns lie in a space of dimension at most \(14+20=34\).

By elementary GF(2) basis elimination, there exists a subset of **actual occurrences** \(J\subseteq R\) whose columns are linearly independent and whose XOR equals \(\bigoplus_{a\in R}w(a)\). Such a \(J\) uses at most 34 events. More importantly, for any fixed \(S\), exactly three column types are possible, one for each triangle edge. Independence implies that \(J\) contains at most **three** events of any one support.

Consequently the retained set \(E_0=F\cup J\) contains **at most \(2+3=5\) occurrences of every support** and at most \(14+34=48\) occurrences overall. It has the same Port-degree parity as \(G\), hence even degrees, and the same parity of each support multiplicity. It is connected on exactly \(U\), because its spanning tree \(F\) remains present.

Write \(k_S=\#\{a\in E_0:S(a)=S\}\). We have \(k_S\le n_S^{[5]}\) because \(k_S\le5\), \(k_S\le n_S\), and \(k_S\equiv n_S\equiv n_S^{[5]}\pmod2\). Thus every difference \(n_S^{[5]}-k_S\) is a nonnegative even number.

For every \(S\) requiring additional occurrences, choose **one edge of support \(S\) that occurred in the original \(G\)**. Its endpoints belong to \(U\), since \(S\) occurred in \(G\). Insert \((n_S^{[5]}-k_S)/2\) copies of an identical **two-edge parallel pair** on those endpoints. Each pair contributes even Port degrees and remains attached to the connected component \(U\). The resulting multigraph is connected and Eulerian, contains \(p\), and has histogram exactly \(n^{[5]}\). Euler's theorem gives the desired labeled closed history.

## 3. Constructive proof: capped to original

Suppose a legal closed history exists for \(n^{[5]}\). For every \(S\) with \(n_S>5\), the capped multiplicity is either 4 or 5, so a support-\(S\) edge is already used. Attach \((n_S-n_S^{[5]})/2\) identical two-edge parallel pairs to **that existing edge**. Nothing is added for \(n_S\le5\). All added occurrences preserve the graph's even degrees and its connectivity, preserve the base Port \(p\), and restore the exact original histogram \(n\). An Euler tour produces the original-length named closed Port history. QED.

This proof is independent of the R762IB odd-core finite census and of the R762IC signability sufficiency theorem.

## 4. Exact binary rank and relation to the Port quotient

The complete 60 candidate columns \(w(S,e)\) have rank **exactly 34**. The upper bound was shown above. To see the lower bound, take one arbitrary base edge \(e_S\) of each triangle, giving 20 columns with independent support-coordinate projections. Differences \(w(S,e)+w(S,e_S)\) have zero support coordinate and span the two-dimensional Port-boundary subspace of that triangle. Together these pure boundaries generate the incidence space of the connected Johnson Port graph \(J(6,2)\), of dimension 14. Hence rank \(20+14=34\).

R762IE's \(\dim B_Q=15-\kappa(Q)\) computes which Port-degree boundary defects may be repaired by available support pairs. The present theorem is a **separate global connectivity-and-parity kernelization**: it retains a concrete spanning tree and the support-parity coordinates, so it handles the connected Euler-tour existence predicate that a boundary quotient alone does not decide. It gives a bounded exact input for any later connected-edge selection algorithm.

## 5. Reproducible verification

Checker: \`research_notes/portable_direct/R762IF_PORT_FIVE_CAP_CHECK.py\` (Python 3 standard library, deterministic). Invocation: \`python3 research_notes/portable_direct/R762IF_PORT_FIVE_CAP_CHECK.py\`.

It constructs all 15 Ports, 20 supports and 60 admissible edges; performs independent GF(2) Gaussian elimination for the full rank 34 and each support's local rank 3; constructs long connected even-degree example multigraphs including triple-edge triangle cycles; runs the actual spanning-tree + independent-subset + pair-reinsertion algorithm; asserts preservation of start-port membership, connectedness, even degrees and every capped support multiplicity.

Observed local stdout:

\`\`\`json
{"status": "PASS R762IF", "global_rank": 34, "per_support_rank": 3, "tests": [{"seed": 7, "cycles": false, "sizes": [14, 14, 1500, 80]}, {"seed": 11, "cycles": true, "sizes": [14, 13, 1599, 91]}, {"seed": 29, "cycles": true, "sizes": [14, 21, 1599, 89]}, {"seed": 41, "cycles": false, "sizes": [14, 14, 1500, 80]}]}
\`\`\`

Each \`sizes\` entry is \`[tree_edge_count, independent_extra_count, original_edge_count, capped_edge_count]\`. These are **four deterministic constructive checks**, not exhaustive computational proof for arbitrary multiplicities. The theorem's all-multiplicity scope follows from the preceding algebraic argument.

## 6. Precise observer and validity boundary

The exact preserved output is **existence** of a legal closed Port history at a specified start Port, together with original support-parity and support-presence predicates. The cap is **not** a lossless encoding of named history, path order, event count, the BRC positive mass \(N_p(n)\), a signed-source count \(C(n)\), exact zero-displacement probability, time evolution, force, Link, Cell, rotation, or P000's native \`TRIADIC_CLOSURE_E\`. For those observers the original histogram and/or ordered event provenance must be retained.

If the separately recorded, still \`NOT_REVIEWED\` R762IC implication is accepted, then for histories with all six axis incidences even, existence of a zero-signable Port circuit also passes between \(n\) and \(n^{[5]}\). That conditional corollary is **not** used to establish this theorem.

**Next unit:** Find a smaller sharp per-support cap (or construct a witness requiring cap five) and combine the bounded kernel with an exact parity-and-connectedness Port selector, providing a verifiable certificate or a returned Euler tour. Separately investigate typed lifting to P000, preserving the six-axis native Cell/Link/force/time/rotation relations.

## 7. Control and provenance

At this research read, the native continuation request \`r3-20261122-0123-x6-current-cont-v1\` failed with \`SOURCE_TREE_TRUNCATED\`; current CLAIM/owner and formal task execution authorization were therefore **not** established by that request. This portable research output does not assert a new CLAIM, protected PROGRESS, formal Result or independent review. Prior Researcher/Activity references in earlier turns are provenance only until a current original-session authority check succeeds.

The current frozen science remains \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Project and account instructions were read in the current run. Scientific evidence remains on this independent research branch pending PR integration.
