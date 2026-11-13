# R5: all 49 four-atom sharp edges inhabit one explicit 12-dimensional face

Date: 2026-11-11, Asia/Shanghai. Author-side exact theorem with complete rational finite computation certificate.
Researcher-ID: \`EM-DIRECT-DD0221 / TASK_RESEARCH\`; Research-Activity-ID: \`RA-BD2749C34A6F95132C288680\`; native identity/source activity source commit \`19575ab03ffe1d7fb1ea0ceba2d224a3b6e56ab8\`.
Scientific input pins retained: GLOBAL \`a01383f825ef9d43b4b754254303298c64041568\`; ENTERPRISE-MATH \`86149263e38c22292c9def1e0f69092efa1be77e\`. No scientific rebase or P000/worldview modification.

## Object, provenance and exact claim

The auxiliary seven-ratio P/Q–BRC observer fiber is the exact frozen one from [PR #2017](https://github.com/awdawmip/enterprise-math/pull/2017), not a stand-alone native X6 spatial model. The seven target ratio numerators are

\[
R=(2,10,15,20,25,30,38),\quad r_i=R_i/20.
\]

The 30 allowed labeled arcs \((i,j)\) comprise all seven targets \(i=0,\ldots,6\) at the four dynamic sources \(j\in\{1,2,3,5\}\), plus the obligatory singleton \((0,0),(6,6)\). The observer \(C\) has 21 rows: seven target marginals, seven source marginals, seven source first moments \(\sum_i R_iE_{ij}\); its exact rank is 15. Fix the exact 30-entry positive rational witness \(E^0\) stored in [PR #2017](https://github.com/awdawmip/enterprise-math/blob/fab8456e8587ce54b3727579d951d5c6c7bf172a/research_notes/brc_r5_six_edge_circuits_20261111/WITNESS.txt) and reproduced verbatim inside this bundle's checker. Let

\[
\mathcal F=\{E\in\mathbb R_{\ge0}^{30}:CE=CE^0\},\quad \dim\mathcal F=30-15=15.
\]

Previous [PR #2045](https://github.com/awdawmip/enterprise-math/pull/2045) classified 14,832 complete 14-arc signed circuits of \(K_4\) plus one doubled high-high target edge, which have minimal six-arc \(K_{2,3}\) atom word length four. Previous [PR #2049](https://github.com/awdawmip/enterprise-math/pull/2049) showed exactly 49 of these yield actual adjacent edges inside this one physical fiber, with 58 distinct 15-arc endpoint vertices.

### Theorem A — exact common face of all 49 sharp edges

**Every one of the 49 sharp adjacent edges**, including both endpoints and all their interior points, has source-3 positive target support exactly

\[
\boxed{\operatorname{supp}(E_{\bullet,3})=\{2,3,4,5\}}.
\]

Consequently all these edges lie inside the single exposed face

\[
\boxed{G=\{E\in\mathcal F:E_{0,3}=E_{1,3}=E_{6,3}=0\}}.
\]

Moreover **this face has affine dimension exactly 12**, and a fully explicit rational strictly positive-in-face witness is constructed below:

\[
\boxed{\dim G=12,\qquad \dim \mathcal F=15.}
\]

The statement concerns the entire set of 49 sharp edges in this exact frozen physical fiber; the preceding signed circuit classification is reused at its exact scope.

### Theorem B — exact four-target row-only comparison

Holding only the source-3 mass, target capacities and first moment fixed, and looking at four-target supports \(J\subseteq\{0,\ldots,6\}\), **exactly seven of the 35** four-label masks admit strictly positive allocations \(0<x_i<M_i\) at all four targets such that

\[
\sum_{i\in J}x_i=Q_3,\qquad
\sum_{i\in J}R_ix_i=T_3.
\]

These seven masks are

\[
\boxed{\{1,2,3,6\},\{1,2,4,6\},\{1,3,4,6\},
\{1,3,5,6\},\{1,4,5,6\},
\{2,3,4,5\},\{2,3,4,6\}.}
\]

Nine masks fail source-mass capacity; nineteen fail the source first-moment range. No tested four-label mask is a moment-boundary equality case. This is an exact **single-row** compatibility classification, not a claim that the six other masks extend to globally legal 30-arc transfers.

## Proof of Theorem A

### 1. Exhaustive exact feasible-edge support classification

For every choice of degree-three source pair \(p<q\) among \(\{1,2,3,5\}\) and all seven-label permutations with canonical repeated high-high labels \(F<G\), enumerate the \(6\cdot7!/2=15,120\) possible \(K_4\) plus doubled-high-pair graphs. Apply the signed seven-target circuit formula of PR #2045 to discard precisely 288 single-arc degeneracies. For each of the remaining 14,832 candidates, let \(A=pq,B=ph,C=pk,D=qh,E=qk,F=hk,G=hk\). The source-marginal and first-moment constraints uniquely make every pair split \(x_i(t)\) a rational affine function of the parameter \(t=x_A\); the exact formulas and implementation are in \`VERIFY_SHARP_FACE.py\`. An edge exists with this full fourteen-arc signed difference precisely if

\[
\max_i \inf\{t:0<x_i(t)<M_i\}<
\min_i \sup\{t:0<x_i(t)<M_i\}.
\]

All seven affine inequalities are compared in \(\mathbb Q\), including their exact boundary cases. This finds exactly 49 feasible edges. Reconstruct both endpoints by substituting the two rational interval endpoints into the 30-entry vector and checking \(CE=CE^0\), nonnegativity and 15 positive entries; deduplication yields exactly 58 endpoints. Crucially, all 49 successful cases have source 3 on exactly the target labels \(2,3,4,5\). The full domain and all-integer/Fraction comparisons establish the finite universal quantifier over these 49 edges.

### 2. A relative-interior witness for the face G

Let \(E^{(1)},\ldots,E^{(49)}\) be the 49 exact rational midpoint transfers in the open intervals of Step 1 and define

\[
B=\frac1{49}\sum_{k=1}^{49}E^{(k)}.
\]

Each \(E^{(k)}\) is feasible, so \(CB=CE^0\). Exact computation establishes that **all but four** of the 30 components of \(B\) are strictly positive. The only zero arcs are

\[
Z_B=\{(0,3),(1,3),(6,3),(6,1)\}.
\]

We now explicitly repair the fourth zero without changing any observer coordinate. Define the signed six-arc \(K_{2,3}\) kernel atom \(H\) on sources 1 and 2 and targets 4,5,6 by

\[
(H_{4,1},H_{5,1},H_{6,1})=(8,-13,5),
\qquad
(H_{4,2},H_{5,2},H_{6,2})=(-8,13,-5),
\]

and zero elsewhere. Both source-wise mass and first moments vanish because

\[
8-13+5=0,\qquad 25(8)-30(13)+38(5)=0.
\]

Each target marginal also vanishes since the coefficients on the two source ports are opposite, hence \(CH=0\).

Set the **explicit positive rational**

\[
\varepsilon=\min\left(\frac{B_{5,1}}{26},\frac{B_{4,2}}{16},\frac{B_{6,2}}{10}\right)
=\frac{227917436204790631}{867449622094929995520}.
\]

Then \(E^\star=B+\varepsilon H\) has \(CE^\star=CE^0\), is strictly positive on **all 27 coordinates outside** \(\{(0,3),(1,3),(6,3)\}\), and vanishes on precisely these three coordinates. The factor 1/2 safety in the definition of \(\varepsilon\) ensures every formerly positive coordinate subjected to subtraction remains strictly positive.

### 3. Exact dimension

For the full matrix and the 27-column submatrix excluding \((0,3),(1,3),(6,3)\), exact rational linear algebra gives

\[
\operatorname{rank}C=15,\qquad
\operatorname{rank}C_{\mathrm{allowed}\setminus\{(0,3),(1,3),(6,3)\}}=15.
\]

Since \(E^\star\) is strictly positive in every one of these 27 coordinates, \(G\) has nonempty relative interior in its equality affine hull. Thus

\[
\dim G=27-15=12.
\]

The supporting functional \(E\mapsto E_{0,3}+E_{1,3}+E_{6,3}\) is nonnegative on \(\mathcal F\) and attains zero at \(E^\star\), proving that \(G\) is an exposed face. QED.

## Proof of Theorem B

The exact frozen dynamic target capacities are \(M_i=\sum_{j\in\{1,2,3,5\}}E^0_{ij}\), the source-3 marginal is \(Q_3=1076926147/2548188300\), and its unscaled moment is \(T_3=20Q_3\). Fix a four-label set \(J\). When \(\sum_J M_i<Q_3\), feasibility fails by mass. Otherwise, for the constraint \(\sum_Jx_i=Q_3,\ 0\le x_i\le M_i\), the **minimum and maximum** of \(\sum_JR_ix_i\) are obtained by greedily filling capacities from smallest/largest \(R_i\), respectively; the exchange inequality \((R_b-R_a)\delta\ge0\) justifies optimality. If \(\sum_JM_i>Q_3>0\) and the required moment lies strictly between these extremes, a strictly interior \(x\) can be built: mix the extremizers slightly with \(x_i^0=Q_3M_i/\sum_JM_i\), which has all \(0<x_i^0<M_i\), then interpolate the resulting lower- and higher-moment interior points to reach \(T_3\). Thus strict inequalities are necessary and sufficient in this certified setting. Exact rational enumeration of all \(\binom74=35\) sets gives the stated seven masks, nine mass failures and nineteen moment failures.

## Why this matters for BRC and the next exact question

Carrier: all 30 labeled source-to-target nonnegative branch masses; signed \(H\) is an actual minimal BRC residual repair. Observer: target marginals, source marginals, first source moments. Permitted future operation for this theorem: same-observer transfer reconstruction, polytope face/edge adjacency and signed atom decomposition. The row-only observer leaves seven candidate four-target source-3 supports, but the actual joint 49-edge sharp dynamics select one. This is the original joint-relation preservation discipline: do not discard branch labels or infer global feasibility from a source-only projection. Exact reuse classification: \`REUSE_APPLIED\` for PR #2017's witness, #2045's circuits, #2049's fiber incidence and the six-arc \(K_{2,3}\) interface.

Verification: \`python3 VERIFY_SHARP_FACE.py\` (requires SymPy only for exact matrix rank, all branch/interval/greedy arithmetic from \`fractions.Fraction\`). Exact original code run in this research turn and complete stdout archived in \`EXACT_OUTPUT.txt\`; terminal marker \`PASS_R5_EXACT_SHARP_FACE_12_DIM\`. The finite exhaustiveness is explicit: 15,120 graph candidates and 35 four-target masks. Theorem status: author derivation + exact exhaustive run, awaiting independent mathematical review and Source Result admission. No formal R5 CLAIM or shared owner reassignment.

**Next research unit:** characterize full adjacency and vertex structure *inside this exact 12-dimensional face* \(G\), test which of the other six row-only four-target supports are actually realizable somewhere in \(\mathcal F\), and determine how the nine PR #2049 sharp-only trees are joined by non-sharp edges. Reuse immutable physical witness and exact BRC repair coordinates. Preserve frozen science pins.