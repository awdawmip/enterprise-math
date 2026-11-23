# R762JX — Full Euler lifting from quotient parity by a connected triple-color graph

Date: 2026-11-23 (Asia/Shanghai). Scientific class: **unsigned composite six-axis Port–Euler observer**. Author status: **PROVED CONDITIONAL STRUCTURAL LEMMA; EXACT FINITE WITNESSES 2,184/2,184; NOT_REVIEWED**.

## Frozen provenance and type boundary

- Underlying task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, immutable publication \`TP2-8B7E13C5904A2D6F1142\`, scientific P000 pins unchanged.
- Fixed earlier composite inputs: R762JT \`6fda34681d94d915894ec5f1c32d1e3654102865\`, and R762JW \`726e0089ddb4bbe0cfb7e64b967c356a4cb6a998\` (Draft PR #2997).
- This advances the residual **full-vertex connectivity and strict positive-degree lift** left open in R762JW. No signed primitive Cell, ordered path, rotation, time or BRC-fidelity theorem is asserted.

Let \(A=\{0,\ldots,5\}\), \(P=\binom A2\) (15 Ports), \(S=\binom A3\) (20 colors). Each \(s=\{a,b,c\}\) permits the three unoriented event edges between Ports \(ab,ac,bc\), with repetitions. Inactive Ports form a matching \(M\subset P\), \(V=P\setminus M\). Every color has 2 or 3 active Ports, hence at least one legal event edge. For an inventory \(n_s\in\{1,2,3\}\), put \(D=\{s:n_s=1\}\) and \(T=\{s:n_s=3\}\); remaining colors are double. A color with 2 active Ports is *forced* (its side is unique), while a 3-active color is *flexible*.

Construct \(G_F\) on \(V\) from **all three possible sides** of each non-singleton flexible color. Let its components be \(C_1,\ldots,C_c\); project the boundary of an event edge \(uv\) to \(\partial_C(uv)=e_{C(u)}+e_{C(v)}\in\mathbb F_2^c\). Let \(F_n\) be the multiset of all forced non-singleton sides, repeated \(n_s\) times.

## Theorem JX.1 (full-vertex lift with exact multiplicities)

Assume the following two *verifiable graph properties*:

1. **Quotient witness:** there is a choice of one legal side \(e_s\) for each \(s\in D\) such that
   \[
   \partial_C(F_n)+\sum_{s\in D}\partial_C(e_s)=0
   \]
   and the graph on \(C_1,\ldots,C_c\) formed by those singleton sides and the forced sides is connected.
2. **Triple spanning:** the union \(H_T\) of all three candidate sides of each \(s\in T\) having three active Ports is connected on the vertex set of **each** \(G_F\) component. A one-vertex component satisfies this condition vacuously.

Then there is an undirected connected multigraph having exactly \(n_s\) events of every color, zero degree on \(M\), and **strictly positive even degree on every vertex of \(V\)**. Therefore an Euler circuit exists from every prescribed \(p\in V\).

### Proof

Keep all forced non-singleton edges with their exact multiplicities and the singleton edges specified by property 1. For every flexible double color choose any *two distinct* sides of its triangle. For every flexible triple color choose the *three distinct* sides (a 3-cycle). Every such flexible color now connects all three of its active Ports; therefore their union realizes the connected components of \(G_F\) internally. Property 1 connects those components by forced and singleton edges. Hence this baseline multigraph is connected and has positive degree on all \(V\), with all color multiplicities exact.

Its degree parity vector \(r\in\mathbb F_2^V\) has even coordinate sum **in every** \(G_F\) component: the flexible-color edges have both endpoints in the same component, and property 1 cancels the quotient parity of all forced-plus-singleton edges. The collection of boundaries of all sides of \(H_T\) spans the direct sum of even-weight subspaces of those components because each component's \(H_T\) graph is connected (property 2). Consequently, for every component-parity vector \(r\) one can choose a boundary \(b_s\in\{0,\partial(ab),\partial(ac),\partial(bc)\}\) separately for each full flexible triple color so that \(\sum_s b_s=r\). Repeated vectors selected from one triangle combine to one of these four possibilities by its three-vertex even parity relation.

Realize \(b_s=0\) with its three distinct triangle sides. For \(b_s=\partial(uv)\), take **one** \(uv\) edge plus **two copies** of a different triangle side. These three events have precisely boundary \(\partial(uv)\), and their support graph still spans all three Ports of the triangle. Thus the corrections cancel \(r\) without disconnecting any flexible triangle or changing any multiplicity. The final connected graph has even degree everywhere, positive degrees on \(V\), and the desired support labels. Euler's criterion completes the proof. \(\square\)

This lemma is an exact constructive assertion conditional on two explicit finite graph properties. It does not require the universal JW.1 assertion as an axiom; JW.1 supplies a general route to property 1, while our finite certificates independently locate property-1 witnesses.

## Corollary JX.2 — New verified portions of the 44→42 terminal class

For the \((8,8,4,0)\) inventory (eight triples, eight doubles, four singletons, no zeros), choose a triple color \(j\) and reduce it by two. The resulting \((7,8,5,0)\) target has 42 events. Write \(D\) for its five singleton colors and \(T\) for the seven remaining triple colors.

For each of the following *four fixed, explicitly labeled* \((M,D)\) slices, enumerate all \(\binom{15}{7}=6,435\) choices of \(T\) among the 15 colors outside \(D\). The linked Python program checks property 2, then **constructs and checks actual 42-event connected Euler witnesses** (including property 1) in every passing case.

| Inactive Ports \(M\) | Five singleton colors \(D\) | \(c\) | Passing triple sets / 6,435 |
|---|---|---:|---:|
| none | 012, 013, 014, 015, 023 | 2 | 448 |
| 01 | 023, 024, 025, 034, 035 | 3 | 428 |
| 01,23 | 024, 025, 034, 035, 045 | 5 | 813 |
| 01,23,45 | 024, 025, 034, 035, 124 | 6 | 495 |
| **Total** | four fixed slices | — | **2,184 / 25,740** |

Each passing triple set gives one exactly verified 42-event Euler multigraph. Choosing any \(j\in D\) and adding two copies of its already selected event yields a valid marked 44-event source from which the same \(j\) is removable. Thus there are **10,920 verified marked compression instances** \((M,D,T,j)\) in these four labeled slices. The 23,556 remaining sampled-slice candidates fail **this sufficient triple-spanning condition**, and are not declared Euler-impossible.

## Exact algorithm and evidence

\`R762JX_FULL_LIFT_GENERATE_VERIFY.py\` enumerates all target inventories in the four slices. For each triple-spanning instance, it enumerates the at most \(3^5\) choices of singleton sides until a quotient-parity-cancelling connected selection is found. A GF(2) binary basis on the full-color triple-side boundaries solves the internal parity, and the three-edge constructions in JX.1 realize the correction. An independent-in-function verifier checks **every generated multigraph**: exact count 42, every color's count and allowed edge, every inactive degree zero, every active degree positive-even, and connectivity. No numerical tolerances, solvers, or floating-point operations enter.

All 25,740 triple-support conditions were tested, and all 2,184 resulting full graph constructions passed. The canonical length-framed serialized-certificate stream has SHA-256:
\`4ae7e97ce5cdc80c3ddd6fb6a08e8e2829f107d73534cfb4dceb367e10891b59\`.
This digest is a reproducibility identity, not an independent proof. The script recreates and verifies the complete stream; its evidence summary records each slice and four example certificates. The result is author-checked and **NOT_REVIEWED**.

## Next open direction

Remove or weaken the triple-component spanning condition by retaining a smaller connected backbone of flexible double-color triangles and assigning its parity jointly with triple colors. Test the \(c=6\) extremal singleton configurations where the current criterion fails, seeking either new exact 42 witnesses or a genuine no-42 obstruction. Resolve the earlier 44-event class only at its actual full scope, then pursue a separate provenance-preserving signed P000/BRC lifting theorem.
