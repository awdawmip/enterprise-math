# R284V — Off-diagonal Port numerator-degree reduction via Hall-deficient cofactors

2026-11-18. **AUTHOR_PROVED / EXACT_FRACTION_AND_EXHAUSTIVE_SUPPORT_CHECK_PASSED / NOT_REVIEWED**. Scientific input fixed at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`; direct dependency R284U (observer-deletion SCC theorem), plus R281, R284R, R284S and R284T. Auxiliary named nonnegative-rational BRC Port models with finite additive single-edge edits; no X6-native transport asserted.

## 1. A graph-matching zero certificate for any scalar matrix entry

For a directed Port matrix `M(x)=I-W_0-sum_i x_i e_{u_i}e_{v_i}^T`, write `D=det M`. Fix **ordered** readout `(a,b)` meaning `F_ab=(M^{-1})_{a b}`. Its determinant numerator is the cofactor

`N_ab = adj(M)_{ab} = (-1)^(a+b) det M[rows != b, cols != a]`.      (1)

If `u_i=b` or `v_i=a`, the named edit is omitted from this minor and `[x_i]N_ab=0`. Otherwise let `r` be the position of row `u_i` after deleting row `b`, and `c` the position of column `v_i` after deleting column `a`, both zero-indexed. Ordinary determinant multilinearity yields

`[x_i]N_ab = (-1)^(a+b+r+c+1) det M(0,z)[rows != b,u_i; cols != a,v_i]`.  (2)

The right-hand matrix is `(n-2)x(n-2)` and includes all other named edits `z`.

Build its **potential-support bipartite graph**, with one left vertex for each remaining row and one right vertex for each remaining column. Include an edge `(r,c)` if the corresponding entry of `I-W_0-sum_j z_j E_j` can be nonzero: a diagonal identity entry, a positive baseline transition, or any available named edit. The support is evaluated over the **complete allowed edit language**, not only at the currently observed zero weights.

**Theorem R284V-A (Hall-deficiency numerator certificate).** If the bipartite support graph has **no perfect matching**, then `[x_i]N_ab(x_i,z)` vanishes identically for all rational values of the other edits. This holds for off-diagonal and diagonal readouts and all baseline coefficients, whenever the named edit enters `M` as one rank-one matrix unit.

**Proof.** A square determinant is a signed sum over bijections between its row and column positions. A nonzero summand requires a support edge for every row-column pair of that bijection, i.e. a perfect matching. If none exists, every summand is the zero polynomial, so the determinant in (2) is identically zero. The endpoint-exclusion case follows directly from (1). This proves the theorem without matrix inversion or assuming algebraic independence of numerical baseline weights. QED.

One ordinary bipartite maximum-matching test (equivalently Hall's condition) per candidate edit determines the structural certificate. A DFS augmenting-path implementation has polynomial time in the remaining support graph, with no exact rational determinant operations. Matching existence does **not** imply a nonzero polynomial: signed determinant cancellations may remain; it is a sufficient zero certificate, not a converse.

## 2. Paired-model implication and sampling cost

Apply the exact R281 output relevance reduction separately to each compared Port model before forming unnormalized `N_h,D_h`. In a matched output `(a_h,b_h)` with the same named edit `i`, if both reduced models satisfy the endpoint-exclusion or Hall-deficiency certificate, then `N_{h,i}'=0` for `h=1,2`. Since each `D_h` is affine in that rank-one edit, R284U's equation (2) applies unchanged:

`[x_i^2] (N_1 D_2 - N_2 D_1) = 0`.                     (3)

This is a global polynomial identity in all other edits. When it holds for every declared output, this coordinate uses **two** admissible comparison values rather than the **three** R284R/R284T require for an unclassified quadratic coordinate. Multiple certified coordinates reduce the product grid independently. Unlike diagonal R284U, this result covers non-diagonal `(a,b)` with a polynomial-time *sufficient* support test. The exact matrix method R284T can handle surviving matching-present cases. Existing p-adic interpolation hypotheses apply to a certified two-node grid exactly as in R284R.

## 3. Exact off-diagonal witness and obstruction

Use Ports `0,1,2`, readout `F_02` and common named edit `x:1->2`. Each model has baseline `0->2=d_h`, `2->1=gamma_h`. Model 1: `(d_1,gamma_1)=(1/4,1/8)`; model 2: `(d_2,gamma_2)=(1/5,1/4)`. All rows remain strictly substochastic for `0<=x<=1/4`. Edit `x` lies on a directed cycle `1->2->1`, and affects the denominators. Yet the `(n-2)` minor of (2) is the 1x1 entry `M[0,1]=0` for each model; its support has no perfect matching. Direct calculation gives

`N_1=1/4`, `D_1=1-x/8`; `N_2=1/5`, `D_2=1-x/4`,

`P(x)=N_1D_2-N_2D_1 = 1/20-3x/80`.                  (4)

Thus the graph-matching certificate reduces three comparison nodes to two **without any quadratic-minor numerical evaluation**.

For an exact nonzero obstruction, add baseline edge `0->1=1/8` **only** to model 2. Its complementary minor now has a perfect matching, its numerator becomes `N_2=1/5+x/8`, and

`P(x) = 1/20-13x/80+x^2/64`.                         (5)

The nonzero `1/64` quadratic coefficient shows why the previous support zero must be tested on the actual declared model.

## 4. Reproduction, evidence and next problem

Source: `research_notes/portable_direct/R284V_offdiagonal_hall_certificate.py`, importing the exact Fraction determinant helper from `R284U_observer_cut_scc_certificate.py` in the same directory. Executed evidence: `research_notes/portable_direct/R284V_offdiagonal_hall_verification.json`. Four exact points verify each of equations (4) and (5). An exhaustive *finite* support test covered **20,736** cases: all 9 ordered observer pairs `(a,b)`, all 9 directed edit endpoint pairs `(u,v)`, and all 256 subsets of the other eight baseline directed edges on three ports (baseline weight 1/16, edit test 1/8). In **14,592** cases the Hall/endpoint certificate was absent-matching and the independently calculated numerator difference was zero. The checker passed for all cases. This verifies the finite test domain; Theorem A has the separate Leibniz proof.

**Next problem.** Improve the sufficient Hall test to a stronger yet tractable path-cycle certificate for general off-diagonal outputs; characterize when matching-present minors cancel because of shared BRC structure or paired-model symmetry, and measure the full exact arithmetic costs relative to the R284T tensor certificate. Keep future-operation, named-edit and source provenance intact when considering any observer quotient.
