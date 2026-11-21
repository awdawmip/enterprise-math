# R762IG — Sharp uniform cap FOUR for six-axis composite Port-Euler existence

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED.

**Frozen scientific premise:** RS-X6-TRIADIC-CLOSURE-DYNAMICS at \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
**Direct predecessor:** R762IF, immutable GitHub commit \`dc33b2898330c34f1e8f2dcab4df055e311fbac6\`, \`research_notes/portable_direct/R762IF_PORT_EULER_FIVE_CAP.md\`.
**Typed claim:** Only the six-axis *composite Port-history observer*: 15 Ports \(\binom{[6]}2\), 20 support types \(\binom{[6]}3\). Each type \(S=\{i,j,k\}\) supplies an undirected edge between two of its three pair-Ports \(\{ij,ik,jk\}\), i.e. one of the three edges of a triangle. Each occurrence remains named; a valid closed history is an Euler circuit of an assigned connected even-degree Port multigraph starting at a specified non-isolated Port \(p\). The indicator is \(N_p(n)>0\).

## Result 1: Four is a sufficient universal per-support cap

For any nonnegative support histogram \(n=(n_S)\) with \(\sum_S n_S>0\), define
\[
n^{[4]}_S=
\begin{cases}
 n_S,&0\le n_S\le4,\\
 4,&n_S>4\text{ even},\\
 3,&n_S>4\text{ odd}.
\end{cases}
\]
Then for every prescribed base Port \(p\),
\[
\boxed{N_p(n)>0 \iff N_p(n^{[4]})>0.}
\]
The capped histogram has at most \(20\cdot4=80\) named events. Each support remains present or absent exactly as before, and \(n_S\bmod2\) is unchanged. This improves R762IF's five-per-support / 100-event theorem without using R762IB's odd-core classification.

### Proof: elementary triangle pair deletion

Fix an arbitrary connected Eulerian realization of the original histogram. For any support \(S\), let \((a,b,c)\) be the multiplicities assigned to the three edges of its Port triangle.

**Deletion lemma.** If \(a+b+c\ge5\), one can remove two parallel occurrences of *one* support-\(S\) edge without changing the set of non-isolated graph vertices, connectedness, or any vertex-degree parity.

If \(\max(a,b,c)\ge3\), delete two copies of such an edge: at least one copy remains, so the support-edge adjacency is unchanged. Otherwise every count is at most 2, and \(a+b+c\ge5\) forces *all three* edge types to be present and at least one to have multiplicity 2. Delete both copies of that edge; its two endpoints remain connected through the other two sides of the same support triangle. Thus the connectivity relation on all vertices is unchanged. In either case the two copies have equal endpoints, hence removing them changes each incident degree by 2 and preserves all degree parities. The number of this support's occurrences drops by 2.

Repeat independently for every support \(S\) while its count exceeds 4. This terminates at exactly \(n^{[4]}_S\) because parity is preserved. At every deletion the original active vertex set, base \(p\), connectedness, and even degrees persist; the resulting multigraph therefore admits a closed Euler tour. This proves the forward implication.

Conversely, given a connected Eulerian realization of \(n^{[4]}\), any support with original count \(n_S>4\) appears at least 3 times in the reduced realization. Choose one of its existing edges and add \((n_S-n^{[4]}_S)/2\) pairs of identical parallel edges there. This preserves connectedness, the active vertices, even degrees, and \(p\). An Euler tour of the expanded graph realizes \(n\). This proves the reverse implication. QED.

The algorithm processes the explicit occurrence list in linear time in its length for the fixed 15-Port/20-support model; this is a *witness conversion*, not a counting equivalence or a claim about compressed input bit complexity.

## Result 2: The universal cap four is SHARP

Let
\[
S=012,\quad T_1=013,\quad T_2=024,\quad T_3=125,
\]
and let the only nonzero support multiplicities be
\[
n_S=4,\qquad n_{T_1}=n_{T_2}=n_{T_3}=3.
\]

The triangles for \(T_1,T_2,T_3\) have pairwise disjoint Port-vertex sets, and intersect the central \(S\)-triangle in precisely one vertex each, respectively \(01,02,12\). Construct the following **13 named edge occurrences**:

- For each \(T_i\), take its three triangle edges once, giving a 3-cycle with all degrees 2.
- For \(S\), add two copies of the Port edge \(01-02\) and two copies of the Port edge \(02-12\).

The result is connected, every degree is even, and \(p=01\) lies on it; hence \(N_{01}(n)>0\).

Any uniform parity-preserving cap at most 3 takes \(n_S=4\) down to 2, keeping the other three support counts at 3. Consider an *arbitrary* Port-edge assignment of the reduced histogram. The two private Port vertices of each \(T_i\)-triangle occur in no other permitted support. Their even-degree constraints force the parities of that triangle's three edge counts to be equal. Their sum equals the odd multiplicity 3, hence all three counts must be odd; as they sum to 3, **each equals 1**. Each peripheral \(T_i\) therefore contributes an isolated 3-cycle before central edges and gives degree 2 at its unique shared Port.

For the central \(S\), two edges must now supply even degree at all three central vertices. Consequently the two edges have the same endpoints (the same triangle side twice). Such a double edge connects only two of the three peripheral triangle components, leaving the third disconnected. No connected Eulerian realization exists. Thus \(N_{01}(n^{[3]})=0\), while \(N_{01}(n)>0\).

This supplies a **13-event exact sharpness witness**, proving that the smallest uniform cap in the stated parity-preserving family is **4**.

## Exact independent verification

Run \`python3 research_notes/portable_direct/R762IG_PORT_SHARP_FOUR_CAP_CHECK.py\` (Python standard library, integer graph arithmetic). Observed local result: \`PASS R762IG\`.

- 15 Ports; 20 support types.
- Exhaustively inspect all \(6\cdot 10^3=6000\) unlabeled Port-edge multiplicity allocations for histogram \((2,3,3,3)\): exactly **3** have even Port degrees, **0** have a connected Eulerian graph. The 13-event original construction passes.
- Check the local pair-deletion lemma for every three-edge multiplicity triple of total 5 through 34: **7735** cases, no failures.
- Deterministic 20-support connected Eulerian example: 580 occurrence edges reduce to 60 while remaining Eulerian.

The all-length proof is the preceding graph argument; finite checks are auxiliary, and the negative search is exhaustive only for the explicitly finite \((2,3,3,3)\) witness.

## Scope, relation to P000, next problem

This exact predicate concerns only *existence* of a legal closed composite Port circuit from a specified start. It does **not** preserve \(N_p(n)\) counts, ordered histories, the positive-weight BRC total, signed zero-displacement counts, time/rotation trajectories, Cell/Link/force states, or native P000 \`TRIADIC_CLOSURE_E\`. The six native signed axes and time remain typed as in P000; the graph is a finite auxiliary observer with no automatic lifting.

**Next useful independent unit:** design a direct deterministic Port-edge selector that either returns a connected Euler tour or a checkable obstruction using the \(\le80\)-event kernel. Separately develop an explicit typed native lifting or a witness showing information lost by the composite projection. Review status is \`NOT_REVIEWED\`; no formal Result/Review or CLAIM follows from this note.

## Provenance and native control
Own earlier researcher session is recorded as \`MCP-773502d89b7a4bd58a37e97a2dd52ba5\` (historical Researcher \`EM-X6-A681A5\`), but current execution authority was NOT established. Read-only exact Task request \`r3-20261122-0216-x6-task-read-v1\` returned \`FAILED / SOURCE_TREE_TRUNCATED\`; recovery metadata reports \`execution_authorized=false\`. This standalone GitHub research note claims no protected PROGRESS, task owner succession, or RA update.