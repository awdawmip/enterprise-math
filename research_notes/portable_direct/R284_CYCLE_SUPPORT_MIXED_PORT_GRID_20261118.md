# R284 — Cycle-support mixed grids for labeled BRC Port observer equivalence

Date: 2026-11-18. **AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED**.
Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Direct predecessor: R283 at \`2f1fe5486edac9ffa88b52a562c33981785bd036\`, \`research_notes/portable_direct/R283_RESONANCE_STRATIFIED_PORT_GRID_CERTIFICATE_20261118.md\`.
Scope: finite strictly substochastic nonnegative-rational **labeled BRC Port** systems, matched additive single-edge edits, a declared finite collection of matched Port observations, and all future admissible simultaneous/prefix edits. This is an algebraic Port result; transferring it to native X6 requires an actual provenance- and operation-preserving map.

## 1. Problem, transfer graph, and the cycle set

For each model \`h=1,2\`, set \`A_h=I-W_h\` and \`S_h=A_h^{-1}\`. For the same \`m\` named additive edits \`E_i=e_{u_i}e_{v_i}^T\`, define \`W_h(x)=W_h+sum_i x_i E_i\`; allow model-specific endpoints only if the declared interface supplies their matching, as in R282. Let \`U_h=(e_{u_1},...,e_{u_m})\`, \`V_h=(e_{v_1},...,e_{v_m})\`, \`X=diag(x_1,...,x_m)\` and \`G_h=V_h^T S_h U_h\`.

Define a directed transfer graph \`T_h\` on edit types \`{1,...,m}\` with \`i -> j\` when \`(G_h)_{ij}=(S_h)_{v_i,u_j}>0\`. The graph is derived from the original, **unchanged** Port carrier and the declared future edits. Since \`W_h>=0\` and is strictly substochastic, entries of \`S_h=sum_{n>=0}W_h^n\` are nonnegative; this graph records actual positive path reachability, not a cancellation heuristic.

Let \`C_h\` be the set of edit indices lying on at least one directed cycle of \`T_h\` (including self-loops), and \`C=C_1 union C_2\`, \`c=|C|\`. Only the declared outputs and edit language are in scope; other Port sources, branch provenance, signed data and X6 relations are not silently erased.

## 2. R284-A: a mixed 2/3-point exact certificate

**Theorem.** Choose, for each \`i notin C\`, two distinct admissible rational test weights, and for each \`i in C\`, three distinct admissible rational test weights, such that their Cartesian grid lies in the common strictly stable edit domain. For any finite declared family of matched readout pairs \`(a,b)\`, equality of all readouts at the

\[
\boxed{2^{m-c}3^c}
\]

grid points is **equivalent** to equality of their rational response functions at every common admissible edit vector. The equality then covers every admissible intermediate prefix readout of the same additive-edit language.

**Proof.** The determinant lemma / Woodbury identity over rational functions gives
\[
D_h(x)=\frac{\det(A_h-U_h X V_h^T)}{\det A_h}
       =\det(I-G_hX),\qquad D_h(0)=1,
\]
and \`F_h(x)=[(A_h-U_hXV_h^T)^{-1}]_{ab}=N_h(x)/D_h(x)\`. Both \`N_h\` and \`D_h\` are individually affine in every \`x_i\` (a single named rank-one edit contributes rank one when all other edits are fixed).

In the determinant expansion of \`det(I-G_hX)\`, a nonconstant monomial is supported on a family of vertex-disjoint directed cycles of \`T_h\`. Therefore if \`i\` lies on no directed cycle of \`T_h\`, **no monomial of \`D_h\` contains \`x_i\`**. For \`i notin C\`, both denominators are independent of \`x_i\`. Consequently the cross-product
\[
P_{ab}=N_{1,ab}D_2-N_{2,ab}D_1
\]
has degree at most **one** in such \`x_i\`, and at most **two** in coordinates \`i in C\`. The two-point/three-point tensor interpolation theorem now shows that vanishing of \`P_{ab}\` on the stated grid implies \`P_{ab}\equiv0\`. All tested denominators are nonzero by stability, so readout equality is precisely \`P_{ab}=0\`. Therefore \`F_1=F_2\` as rational functions. The reverse implication is immediate. Repeat for each declared output. QED.

The theorem uses the **union** of the two graphs' cycle supports; using only one graph can underestimate the degree of the cross-product. A graph vertex outside \`C\` may still be essential to a future observer, so it is sampled at two points rather than deleted.

**Consequence.** If both transfer graphs are acyclic, the certificate has exactly \`2^m\` tests. For \`c<m\`, it is strictly smaller than R283's \`3^m\` grid. This is a sufficient structural reduction, not a general claim that this cardinality is minimal.

## 3. R284-B: resonance-stratified p-adic certificate with fewer binary losses

Let \`p\` be any prime. Use p-integral numerator/denominator presentations for each output, as in R283. Write \`s(u)=v_p(D_1(u)D_2(u))\`, and assume all evaluated denominators nonzero. For each \`i\`, use \`d_i+1\` p-integral nodes \`t_{ij}\`, where \`d_i=1\` outside \`C\`, \`d_i=2\` inside \`C\`. Define
\[
\kappa_i=\max_j\sum_{\ell\ne j}v_p(t_{ij}-t_{i\ell}),\qquad
\kappa=\sum_i\kappa_i .
\]

**Theorem.** If, on the mixed grid, for a chosen integer \`M\`,
\[
v_p(F_1(u)-F_2(u))\ge M+\kappa-s(u)
\]
at each node \`u\`, then every coefficient of \`P=N_1D_2-N_2D_1\` has valuation at least \`M\`. At every p-integral admissible target \`x\`,
\[
v_p(F_1(x)-F_2(x))\ge M-s(x).
\]
For a target stratum \`s(x)\le T\`, setting \`M=k+T\` certifies agreement modulo \`p^k\`.

**Proof.** Tensor Lagrange interpolation in the coordinatewise degree bounds \`(d_i)\` has coefficients in \`p^{-\kappa}Z_{(p)}\`, because each nodal numerator is p-integral and each denominator has valuation at most the corresponding \`kappa_i\`. The sample hypothesis gives \`v_p(P(u))\ge M+\kappa\`. Thus every coefficient of \`P\` has valuation at least \`M\`. Evaluating at any p-integral target and dividing by nonzero \`D_1D_2\` proves both conclusions. QED.

For any sufficiently large integer \`q\` prime to \`p\`, take nodes \`{0,1/q}\` for indices outside \`C\`, and \`{0,1/q,2/q}\` for indices in \`C\`; sufficiently large \`q\` makes the whole grid strictly stable. If \`p>=3\`, then \`kappa=0\`. If \`p=2\`, then \`kappa=c\`, **not** the general R283 bound \`m\`. In the acyclic case \`c=0\`, even the binary finite-resolution interpolation certificate loses no digits. The valuation bound depends on the declared denominator-normalization and target stratum, precisely as in R283.

## 4. Exact BRC Port witnesses

**Two edits, no feedback cycle.** On Ports \`0,...,4\`, take baseline \`0->1=a,\ 2->3=1/4\`, add edits \`A:1->2=x\`, \`B:3->4=y\`, and read \`(0,4)\`. There is no transfer-graph cycle. For \`a=1/4\` and \`a=1/5\`, respectively,
\[
F_1(x,y)=xy/16,\qquad F_2(x,y)=xy/20.
\]
The \`{0,1/7}^2\` grid has four points, and \`F_1(1/7,1/7)=1/784\`, \`F_2(1/7,1/7)=1/980\`. This is a genuine mixed-path observation: dropping either edit makes both outputs zero.

**One feedback edit, one acyclic edit.** Baseline edges \`0->1=1/4,\ 2->0=1/4,\ 0->3=b\`, with the same two edits \`A:1->2=x,\ B:3->4=y\` and observer \`(0,4)\`. For \`b=1/4\` and \`b=1/5\` the exact responses are
\[
F_1(x,y)=\frac{y/4}{1-x/16},\qquad
F_2(x,y)=\frac{y/5}{1-x/16}.
\]
Here \`C={A}\`; the six-point grid \`x in {0,1/7,2/7}\`, \`y in {0,1/7}\` suffices. At \`(x,y)=(1/7,1/7)\` the outputs are \`4/111\` and \`16/555\`. All displayed baseline and sampled systems are nonnegative-rational and strictly substochastic.

## 5. Verification, provenance, boundaries and next question

Checker: \`R284_mixed_port_grid_checker.py\`, standard-library \`fractions.Fraction\`, exact permutation-determinants, polynomial cross-products, baseline inverse and transfer-cycle closure. It checked \`72\` deterministic seeded model pairs with \`n in {3,4}\`, \`m in {1,2,3}\`; each check established the stated per-coordinate degree bound and denominator independence for acyclic indices. It also checked \`20\` exact model/observer evaluations in the two explicit witnesses and \`p=2,13\` node losses. Saved result \`R284_verification.json\` reports \`PASS\`. The universal claims are established by the determinant and interpolation proofs above; finite tests cover only the stated models and arithmetic identities.

The result preserves named edit types and all joint interactions detectable by the declared future operation and Port output language. The graph classification is a certificate about a **typed auxiliary positive-rational BRC Port carrier**, not an exhaustive native X6 event-history quotient. Existing P000, the six-dimensional X6 basis, provenance-preserving future operation requirements and the frozen scientific pin are unchanged.

**Next:** compute an output-specific graph-reachability interpolation module that can also omit genuinely invisible edits with an exact all-future observer factorization certificate; test whether p=2 losses for cycle-bearing coordinates may shrink further under transfer-graph structure. A native X6 application needs an explicit branch/source/Port history map and a proof that the native updates descend through it.
