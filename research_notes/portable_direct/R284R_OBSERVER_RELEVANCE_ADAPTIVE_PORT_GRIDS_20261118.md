# R284R — Observer-relevance-adaptive Port grids (one/two/three samples per named edit)

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_RATIONAL_EXAMPLE_CHECKED / NOT_REVIEWED**.
Scientific input frozen at **43ec6098b1330ae86d0a7863be336c5d97f6ef34**.
Immediate frontier: R281 at ea9d315ceaab0e29cc963de8c31b9b008388e5a5, R282 at the same immutable source, R283 at 2f1fe5486edac9ffa88b52a562c33981785bd036, and R284 at c595fada9b7f3f5e7822cf6804c9e6be7eae307a.

**Research type and boundary.** This is an exact theorem within the finite strictly substochastic, nonnegative-rational, *named visible-BRC Port* auxiliary subsystem with additive rank-one edits. Port labels, readout declarations and allowed future operations remain typed. The ambient P000 Heartbeat World is six-dimensional in space, with one separate time dimension; nothing here changes P000, selects an X6-native three-dimensional layer or asserts an unconstructed dynamics/provenance map. Only the explicitly declared Port observation interface is compared.

## 1. The gap after R284

R284 uses the union \(C=C_1\cup C_2\) of edit-transfer graph cycle supports, and gives a \(2^{m-|C|}3^{|C|}\) exact response-equivalence grid. A cyclic edit can be **invisible for a declared observer in both models**, or can be visible in only one model. Neither case needs three samples to compare the two declared outputs. R281 already characterizes model/output-specific visibility exactly; combining it with the R284 determinant proof gives a stronger interpolation module.

Fix two models indexed \(h=1,2\). Model \(h\) has a finite nonnegative-rational baseline \(W_h\) with row sums strictly below one, \(m\) named, matched additive rank-one edit types \(E_{hi}=e_{u_{hi}}e_{v_{hi}}^T\), and a finite nonempty collection \(\mathcal O\) of declared matched scalar output interfaces \(q=(a_h,b_h)\). Endpoints and matrix sizes may be model-specific when the matched Port interface explicitly specifies them. For each jointly admissible nonnegative rational edit vector \(x\), write

\[
 F_{h,q}(x)=\bigl[I-W_h-\sum_{i=1}^{m}x_iE_{hi}\bigr]^{-1}_{a_hb_h}.
\]

For each \(h\), compute \(S_h=(I-W_h)^{-1}\) and the R281 edit-transfer graph \(H_h\): its arcs are \(i\to j\) exactly if \((S_h)_{v_{hi},u_{hj}}>0\). Its initial vertices for output \(q\) are those \(i\) with \((S_h)_{a_h,u_{hi}}>0\), and its terminal vertices those \(i\) with \((S_h)_{v_{hi},b_h}>0\). Let \(R_{h,q}\) be all vertices on an initial-to-terminal directed walk, and \(C_h\) all vertices on a directed cycle of \(H_h\), self-loops included.

R281 proves the exact statement that \(F_{h,q}\) is independent of \(x_i\) throughout the stable admissible domain precisely when \(i\notin R_{h,q}\). No current-output-only approximation is used: future *simultaneous and prefix* additive edits are included in this rational-function identity.

For each output \(q\), define

\[
 U_q=R_{1,q}\cup R_{2,q},\qquad
 B_q=R_{1,q}\cap R_{2,q}\cap(C_1\cup C_2).
\]

For a shared grid serving all outputs, set \(U=\bigcup_{q\in\mathcal O}U_q\), \(B=\bigcup_{q\in\mathcal O}B_q\). Thus \(B\subseteq U\subseteq\{1,\ldots,m\}\).

## 2. Theorem R284R-A: exact 1/2/3-point observer-equivalence certificate

**Statement.** For every \(i\notin U\), use one test weight (chosen as zero). For every \(i\in U\setminus B\), use two distinct rational test weights. For every \(i\in B\), use three distinct rational test weights. Choose the weights so that the full product grid is jointly stable and admissible. Such a grid always exists by using sufficiently small nonnegative weights. Then agreement of the two models at every declared output on all

\[
\boxed{\,2^{|U|-|B|}3^{|B|}\,}
\]

grid points is equivalent to equality of their complete rational response functions on the whole common admissible edit domain. It consequently certifies every admissible additive-edit prefix under the same declared Port observer language.

This specializes to R284 when every edit is observer-relevant and the cycle-support classification requires the same 2/3 sampling. It is strictly smaller whenever a formerly sampled edit is invisible in both models, or a cycle-bearing edit is visible in at most one model.

**Proof.** For each model and output, the determinant/cofactor construction in R282 gives a fraction \(F_{h,q}=N_{h,q}/D_h\) with numerator and denominator separately affine in each \(x_i\) and \(D_h(0)=1\). A variable absent from the cycle support \(C_h\) does not appear in \(D_h\), because each nonconstant determinant monomial of \(\det(I-G_hX)\) is supported on directed cycles of \(H_h\), as in R284.

Let \(Z_{h,q}\) denote the edit labels outside \(R_{h,q}\). Define the *observer-reduced presentation* \(N^*_{h,q},D^*_{h,q}\) by setting all variables with indices in \(Z_{h,q}\) to zero **in the original multiaffine numerator and denominator**. Since R281 establishes that \(F_{h,q}\) is independent of every such variable as a rational function, the resulting fraction is still exactly \(F_{h,q}\) on the entire admissible edit domain. Both reduced polynomials remain separately affine, and both are independent of the variables in \(Z_{h,q}\).

Now form
\[
 P_q=N^*_{1,q}D^*_{2,q}-N^*_{2,q}D^*_{1,q}.
\]
Its degree in \(x_i\) can be bounded by examining three exhaustive cases:

1. If \(i\notin U_q\), both reduced fractions are independent of \(x_i\); hence \(\deg_i P_q=0\) or \(P_q=0\).
2. If \(i\in U_q\setminus B_q\), then either only one model is relevant, in which case the other reduced numerator/denominator are independent of \(x_i\); **or** both models are relevant but \(i\notin C_1\cup C_2\), in which case both denominators are independent of \(x_i\). In both subcases \(\deg_i P_q\le1\).
3. If \(i\in B_q\), every reduced factor is separately affine, and thus \(\deg_i P_q\le2\).

Taking the union across outputs gives common degree bounds \(d_i=0,1,2\) for \(i\notin U,\ i\in U\setminus B,\ i\in B\), respectively. At each stable grid node both denominators are nonzero, so equality of responses is \(P_q=0\). Tensor-product interpolation for the degree box \(\deg_i P_q\le d_i\) at \(d_i+1\) distinct nodes proves \(P_q\equiv0\). Therefore every declared pair of rational responses is identical wherever the common stable edit operations are defined. The converse follows by restriction. QED.

**Observer factorization detail.** The simultaneous replacement of every irrelevant coordinate by zero in the same model/output presentation is valid because R281 proves *rational-function independence* coordinatewise; composing these coordinate substitutions retains equality. In a nonnegative edit language, zeroing edits from a stable matrix also retains stability. This argument is stronger than removing an edge based only on its baseline scalar observation.

## 3. Theorem R284R-B: sharper p-adic resonance certificate

Fix a prime \(p\), precision \(k\ge1\), and a declared output \(q\). Choose \(p\)-integral rational numerator/denominator presentations of the reduced responses \(N^*_{h,q}/D^*_{h,q}\), multiplying numerator and denominator of each by the same nonzero scalar as necessary. They remain of coordinate degrees at most one, with the bounds from R284R-A for their cross-product \(P_q\).

For each sampled coordinate \(i\in U\), choose \(d_i+1\) distinct points \(t_{ij}\in\mathbb Z_{(p)}\); for \(i\notin U\) take the single point zero. Define
\[
 \kappa_i=
 \begin{cases}
 \max_j\sum_{\ell\ne j}v_p(t_{ij}-t_{i\ell}), & d_i\ge1,\\
 0, & d_i=0,
 \end{cases}
 \qquad \kappa=\sum_i\kappa_i.
\]
At a grid/target vector \(u\) with nonzero denominators set \(s_q(u)=v_p(D^*_{1,q}(u)D^*_{2,q}(u))\).

**Statement.** If each sample \(u\) satisfies
\[
 v_p(F_{1,q}(u)-F_{2,q}(u))\ge M+\kappa-s_q(u),
\]
then **every coefficient** of \(P_q\) has valuation at least \(M\). Consequently every admissible \(p\)-integral target \(x\) with nonzero denominators satisfies
\[
 v_p(F_{1,q}(x)-F_{2,q}(x))\ge M-s_q(x).
\]
Thus \(M=k+T\) gives full mod-\(p^k\) agreement on the declared resonance stratum \(s_q(x)\le T\). Apply this separately to each output (its denominator normalization and \(s_q\) may differ).

**Proof.** The tensor Lagrange basis on the selected degree box has coefficient valuations at least \(-\kappa\), since every node is \(p\)-integral and the product of its interpolation denominator differences has valuation at most \(\kappa\). The sample hypothesis and \(P_q(u)=(F_{1,q}(u)-F_{2,q}(u))D^*_{1,q}(u)D^*_{2,q}(u)\) give \(v_p(P_q(u))\ge M+\kappa\). Interpolation shows all coefficients of \(P_q\) have valuation at least \(M\). Evaluate at \(p\)-integral \(x\) and divide by the nonzero denominator product. QED.

Choose a sufficiently large integer \(Q>0\) prime to \(p\), with nodes \(0\) (one-point), \(0,1/Q\) (two-point), or \(0,1/Q,2/Q\) (three-point). All are physically small and admissible. For odd \(p\), every selected difference is a \(p\)-adic unit, so \(\kappa=0\). For \(p=2\), the two-point coordinates still have \(\kappa_i=0\), and each three-point coordinate has \(\kappa_i=1\); hence the **binary interpolation loss is \(|B|\)**. This improves R284's \(|C|\) bound and R283's general \(m\) bound for this observer-relevance-adapted certificate.

## 4. Exact six-Port witness and sample reductions

Consider Ports \(0,\ldots,5\), declared observer \((0,0)\), and three *named* edit labels
\(A:1\to2\) with weight \(x\), \(B:3\to4\) with weight \(y\), and \(C:5\to5\) with weight \(z\).

- Model 1 baseline: \(0\to1=1/4,\ 2\to0=1/4,\ 0\to3=1/8,\ 4\to0=1/8\); all other baseline edges zero.
- Model 2 baseline: \(0\to1=1/4,\ 2\to0=15/64,\ 2\to1=1/4\); all other baseline edges zero.

For jointly admissible edits (in particular \(0\le x\le1/2,\ 0\le y,z\le1/4\)), exact inversion gives
\[
 F_1(x,y,z)=\frac1{1-x/16-y/64},\qquad
 F_2(x,y,z)=\frac{1-x/4}{1-79x/256}.
\]
Thus \(C\) is invisible to the observer in both models, while \(B\) is visible only in model 1 despite being cycle-bearing there. \(A\) is visible and cycle-bearing in both. Exact Green-matrix graph evaluation yields
\[
 R_1=\{A,B\},\quad R_2=\{A\},\quad
 C_1=\{A,B,C\},\quad C_2=\{A,C\}.
\]
Therefore \(U=\{A,B\}\) and \(B_{\rm three}=\{A\}\). R282's general grid uses \(3^3=27\) nodes and R284's cycle-support grid also uses \(3^3=27\); **R284R uses \(3\times2\times1=6\)** nodes:
\[
 x\in\{0,1/101,2/101\},\quad y\in\{0,1/101\},\quad z=0.
\]
The same equality/inequality conclusion holds for every admissible \(z\), regardless of how often edit \(C\) is applied, under the specified additive language.

At \(x=y=1/4\), exact outputs are \(F_1=256/251,\ F_2=64/63\). The need for three points in the general cycle-relevant case is supported by the inherited R282 single-edit counterexample: when \(y=0\), these models coincide at \(x=0\) and \(x=1/4\) (both \(1\) and \(64/63\)), but at \(x=1/2\) their outputs are \(32/31\) and \(448/433\), respectively. This is a counterexample to a universal two-node rule in a both-relevant cycle coordinate; it is not a claim of global minimum node counts for all graph classes.

For the indicated grid, the binary interpolation penalty is \(\kappa=1\) (three samples for \(A\), two for \(B\), one for \(C\)); the R284 cycle-only sampling would lose three binary digits. For \(p=13\), the selected interpolation penalty is zero. The actual denominator resonance stratum must still be specified for a modulus claim.

## 5. Reproducibility and proof status

- Standalone exact Fraction checker: [R284R_output_relevance_grid_checker.py](R284R_output_relevance_grid_checker.py).
- Captured actual standard-output result: [R284R_output_relevance_grid_verification.json](R284R_output_relevance_grid_verification.json).
- The checker recomputes both six-by-six rational inverse matrices, exact observer formulas, full edit transfer digraph reachability/cycle supports, the two-node obstruction and the \(p=2,13\) interpolation penalties. It passed **48** direct inverse/closed-form checks (24 edit tuples, two models), plus explicit graph, interpolation and witness assertions. All finite model updates were checked strictly row-substochastic.
- The universal propositions are proven by R281's exact relevance characterization, R282's multiaffine determinant quotient and tensor interpolation, and R284's cycle-support factorization. The enumerated numerical/rational checks cover the stated witness, not all Port systems.
- Reuse is explicit: this is a new combination of existing R281–R284 components, not a claim that matrix resolvents, interpolation or p-adic valuations are newly discovered mathematics. No independent scientific Review, Result admission, formal Task CLAIM or native X6 provenance map is asserted.

## 6. Next mathematical question

Find a **cross-product-specific** interpolation module that detects further degree collapse *after* forming the two observer-reduced fractions. In the six-Port witness, although \(A\) belongs to \(B_{\rm three}\), the cross-product simplifies strongly, so the 1/2/3 grid is still conservative. A defensible next step is to compute the coordinatewise degrees of the actual reduced cross-products for every declared output, give a finite coefficient certificate that those degrees are exact, then interpolate on the smaller joint degree box; include coefficient valuation and denominator normalization for mod-\(p^k\) resonance strata. Investigate how much of this compression remains exact when the declared update algebra includes sequential non-additive Port rewrites or branch-sensitive provenance. Those extensions need their own operation-preserving certificates.
