# R740 — X6 原生边流的路径恢复与 720 分支 BRC 精确分类

Date: 2026-11-12 (Asia/Shanghai). Scope: author-side exact combinatorial theorem; pending independent research review.

Parent Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen science: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`, specifically \`p000_reality_foundation.json\`, \`definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md\`, and \`definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md\`. Reuses R735 (PR #2132) and R738 (PR #2138); concurrent R739 (PR #2140) treats another conditional five-closure/V29 PASS construction.

## 1. Exact domain and typed BRC carrier

Fix a chosen Cell C in native X6, an affine torsor over signed Z^6. Choose three distinct native spatial axes A={a,b,c}. Form all six-step closed *coordinate* histories containing +a,-a,+b,-b,+c,-c exactly once each. There are 6!=720 histories. Every history is an independent positive-counted BRC branch retaining ordered primitive steps, identities, chosen anchor and signs. Signed edge flow defined below is an **observer of a branch**, not positive BRC weight or a physical signed-force cancellation operation. X6 remains six-dimensional; the selected three-axis affine sub-torsor is a three-dimensional research slice.

For one directed primitive step along axis i from position x to x+s e_i, let its canonical edge be (u,i), where u is the endpoint with lower i-coordinate, and assign +1 for s=+1 or -1 for s=-1. Let the integer *rooted oriented edge current* of w be

\[
j_w(u,i)=\#\{\text{positive traversals of }(u,i)\}-\#\{\text{negative traversals of }(u,i)\}.
\]

Here u is the signed relative coordinate with respect to C, not a newly designated universal origin. Define R735 circulation \`J_{ij}(w)=sum_t x_i(t-1) delta_x_j(t)\` for i<j; Q records each selected axis's first sign; epsilon is R738's first-appearance orientation-torsor bit. Let NB(A) be those six-token histories without two adjacent inverse steps.

## 2. Theorem: exact edge-current projection to signed circulation

For any closed native signed-axis coordinate path w and distinct axes i,j,

\[
\boxed{J_{ij}(w)=\sum_{u\in\mathbb Z^6}u_i\,j_w(u,j).}
\]

This is independent of the chart anchor, transforms naturally under S6 native-axis relabeling, and extends antisymmetrically: \`J_{ij}=-J_{ji}\`.

**Proof.** For a step on axis j, the i-coordinate of both endpoints of the traversed edge is equal when i!=j. Hence its contribution to the right-hand side is the pre-step value x_i times its signed j-increment delta_x_j. Summation yields the definition of J. Closed paths have zero total j-axis displacement, so shifting all coordinates by an anchor constant h changes this sum by h_i times zero. The discrete product identity for x_i x_j telescopes around a closed path; delta_x_i delta_x_j vanishes at each *primitive* one-axis step, proving J_ij+J_ji=0. Relabeling permutes all positions and edges on both sides. QED.

If a native V39 current were established to retain this exact oriented Cell-adjacent edge data, its J readout would follow from this explicit formula. Such identification is a separate dynamical correspondence obligation; this paper uses \`j_X6\` only for the newly defined primitive-edge observer.

## 3. Theorem: complete 720-path edge-current fiber census

Exactly **265 distinct** rooted edge currents occur, with complete observation-fiber multiplicities:

| Histories per current | Number of currents | Total histories |
|---:|---:|---:|
| 1 | 240 | 240 |
| 10 | 24 | 240 |
| 240 | 1 | 240 |
| **Total** | **265** | **720** |

The same classification refined by oriented current support:

| Current support | Histories | Distinct currents | Histories per current |
|---|---:|---:|---:|
| Zero flow j=0 | 240 | 1 | 240 |
| Oriented 4-edge square through C | 240 | 24 | 10 |
| Oriented 4-edge square displaced one third-axis step from C | 48 | 48 | 1 |
| Oriented 6-edge cycle through C | 192 | 192 | 1 |
| **Total** | **720** | **265** | — |

**Proof.** A six-step closed primitive-axis walk has signed net zero in each of its three active axes. Erasing any consecutive mutually inverse step pair preserves its edge current. After free reduction a nonzero graph-cycle flow has at least four edges because the native coordinate-adjacency graph is bipartite with no 2-edge nonbacktracking circuit or 3-cycle. With a six-step budget, its support can be a four-edge square or an oriented six-edge cycle; a square may be attached to the selected root by a twice-traversed one-step third-axis stem. Two separate nontrivial cycles would require at least eight steps. In particular an oriented six-edge support is a simple 6-cycle.

For zero flow, a length-six path cannot contain a forward and a reverse traversal of an entire square (eight steps would be required); thus all its steps reduce by successive adjacent inverse cancellations. The three pairs of identical axis symbols must form a noncrossing matching of six positions. There are Catalan C_3=5 such pairings; their three distinct labels have 3!=6 assignments and each axis's first step has two signs. Thus 5*6*8=240 zero-current histories, all in the same j=0 fiber.

For rooted square currents, choose the two axes (3 choices), one of the four signed square quadrants at C (4 choices), and the orientation of circulation (2 choices). This gives 24 distinct currents. The unused third axis contributes one positive and one negative step; they must be an immediate out-and-back spur placed in one of five slots in the rooted four-edge square traversal. There are 5*2=10 positive BRC histories per current, hence 240 histories total.

For displaced square currents, choose the square-axis pair (3 choices), stem direction on the remaining axis (+ or -, 2 choices), signed quadrant (4) and square orientation (2). This gives 3*2*4*2=48 currents. To cover this square from C in exactly six steps, the word must be the unique third-axis outward stem, the unique four-edge directed square cycle, then the reverse stem. Every such current has one rooted history.

The remaining 720-240-240-48=192 paths have six nonzero edge currents constituting an oriented simple 6-cycle. The chosen root C and oriented cycle determine its unique starting edge and complete traversal. Every such current has exactly one history. This exhausts the domain and proves the census. QED.

## 4. Nonbacktracking losslessness and a precise scope boundary

Among all 720 histories, exactly 240 have **no adjacent inverse steps**. They are exactly the 192 six-edge cycles and the 48 one-step-stem displaced squares. Consequently,

\[
\boxed{\forall w,w'\in NB(A):\ j_w=j_{w'}\Longrightarrow w=w'.}
\]

A decoder starting at C follows the unique oriented six-edge cycle, or, for a displaced square, traverses its unique third-axis stem, then the oriented square and the reverse stem. Thus the signed edge current \`(C,j_X6)\` exactly recovers the complete ordered primitive path in this declared nonbacktracking, six-step, three-axis carrier.

This contrasts with the **unrestricted** 720-branch carrier, in which the single observation j=0 collapses 240 positive-counted, provenance-distinct source histories. The same current may therefore be lossless for one declared future-operation domain and lossy for another.

R738 found the NB carrier's \`(Q,J)\` has 192 fibers (144 singletons, 48 doubles), and its orientation-torsor extension \`(Q,J,epsilon)\` has 240 singletons. The present stronger spatial observer \`(C,j_X6)\` also has 240 singletons, without separately storing epsilon; it retains the actual spatial support of native edge traversal.

A concrete separating pair is

\[
w=(0+,1+,2+,0-,2-,1-),\quad
w'=(0+,2+,1+,0-,1-,2-).
\]

They both have Q=(+,+,+), J=(1,1,0), and opposite first-appearance orientations. Their explicit nonzero edge-current lists differ: for w the six directed edge coordinates (lower endpoint,axis,flow) are
\`(000,0,+1),(000,1,-1),(010,2,-1),(011,0,-1),(100,1,+1),(110,2,+1)\`;
for w' they are
\`(000,0,+1),(000,2,-1),(001,1,-1),(011,0,-1),(100,2,+1),(101,1,+1)\`.
All coordinates are relative to the chosen Cell C.

## 5. S6 covariance and exact test certificate

For every pure axis-label permutation g in S6, the natural relabeling of step histories, coordinates and edge labels obeys

\[
j_{g w}(g u,g i)=j_w(u,i).
\]

This follows termwise from the edge definition; it does not assume any Euclidean 90-degree identification or novel primitive direction. The finite checker \`R740_X6_EDGE_CURRENT_VERIFY.py\` is an explicit positive-counted branch enumerator with signed integer edge-current readout. It verifies:

- every one of the 90 unsigned double-occurrence patterns and 8 first-sign choices (720 distinct closed paths);
- all 265 rooted currents and full (1:240,10:24,240:1) fiber census;
- all 240 NB histories, their 192 six-cycles and 48 stem-square paths, and complete j-injectivity;
- the projection identity j→J, integer divergence-free edge flow and R738's \`(Q,J,epsilon)\` exact recovery for all 720/240 applicable cases;
- all 20 selected X6 axis triples' NB injectivity;
- all 20 triples, all 720 paths and five adjacent transpositions generating S6: **72,000** coordinate/edge-covariance checks;
- the explicit above Q,J collision with distinct j supports.

No floating-point, classical pi/trigonometry, Euclidean three-force vector cancellation or non-BRC dynamics calculation is used. The machine assertion is \`R740_X6_EDGE_CURRENT_BRC_EXACT_PASS\`. See \`R740_X6_EDGE_CURRENT_RESULTS.json\` for exact data and provenance.

## 6. Next native scientific unit and control status

Read the actual *frozen scientific* V39 loop-flow j interface including Cell/Link/Port attachment, source identities, history aggregation, its update event and any loop-current conservation constraints. Build a typed map \`Phi:j_V39 -> j_X6\`, or an exact obstruction witness if one cannot preserve the required oriented edge data, for **one Source-supported legal TRIADIC_CLOSURE_E event**. Then test whether native V29 PASS and V39 current updates commute with the map and retain the R738/R740 event-level source distinction. The full X6 triadic force closure/rotation interlock remains the mother-task objective.

Native task read at this run: publication \`TP2-8B7E13C5904A2D6F1142\`, status \`HANDOFF_READY/NEEDS_DISPATCH\`, owner \`taskbook/unassigned\`, no active CLAIM. The current new-session issuance attempt returned \`SESSION_ISSUANCE_QUOTA\`; no R740 Researcher-ID, RA, authenticated CLAIM, formal frozen Result or Driver review exists. This proof and checker are authored research artifacts and do not modify P000 or the frozen scientific inputs.
