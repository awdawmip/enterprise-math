# R5: active-source martingale sparsity, time–hinge conservation and a 14-edge physical witness

Date: 2026-11-09 (Asia/Shanghai). Scope: frozen seven-likelihood-node P/Q-BRC statistical observer, author-side proof and exact Fraction checks; independent mathematical admission pending. Predecessors: draft PR #1831 (all-flow author-side feasibility), #1835 (unrestricted 17-edge bound), #1837 (unrestricted 17-edge generic sharpness). Frozen science references remain those reported in #1837: global a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral rules were read separately from canonical main. This note neither changes P000 nor claims native X6 dynamics.

## 1. A source-support-sensitive theorem

Fix n distinct ordered ratios r_0 < ... < r_(n-1). Let nonnegative E satisfy

\[
\sum_j E_{ij}=\mu_i,\quad
\sum_i E_{ij}=\nu_j,\quad
\sum_i r_i E_{ij}=r_j\nu_j.
\tag{1}
\]

Write A={j: nu_j>0}, m=|A|, and e=|A∩{0,n-1}|. Then **every feasible pair (mu,nu)** has a coupling with

\[
\boxed{\#\{(i,j):E_{ij}>0\}\le n+2m-2-e.} \tag{2}
\]

Indeed, zero source columns vanish; an active lowest/highest column is forced to its diagonal by the extremal conditional mean. The resulting constraint matrix has n row-mass, m column-mass and m column-moment rows. Two global dependencies are total Q mass and total LR-weighted mass. Each active extreme column gives one further independent moment-vs-mass dependency. Hence rank≤n+2m-2-e. A bounded nonempty transport polytope has an extreme point whose positive constraint columns are independent; rational data admit a rational extreme-point certificate.

For n=7, R=(1/10,1/2,3/4,1,5/4,3/2,19/10). The frozen FULL_HIST mass formulas contain

\[
\nu_2=M_2(x)=(g-a)/2,\qquad \nu_4=M_4(x)=(g-b)/2.
\]

Consequently, **every feasible lawful FULL_HIST source with g=b has a seedless-target Blackwell coupling using at most 15 positive entries**, and **every feasible source with g=b=a has one using at most 13 entries**. The existence of a lawful seedless target for an arbitrary x invokes the author-side predecessor #1831; the new sparse bound itself is conditional only on a feasible coupling.

For abstract normalized common-grid marginal pairs with A containing both extreme columns and at least one interior column, the bound n+2m-4 is also **generically sharp** within the open chamber nu_j>mu_j for all active interior j. To prove this, the linear balanced marginal space with source zeros outside A has dimension n+m-3 (Q and P total equalities plus mean-one homogeneity). Signed couplings supported on any S with ≤n+2m-5 edges and representing that chamber satisfy m-2 independent interior-column moment equations, so their marginal image has dimension ≤n+m-3. The forced endpoint diagonal atom belongs to that image but not to the balanced mean-one space (r_0≠1), so the image cuts the latter in a proper linear subspace. The finite union over all supports S cannot cover an open feasible chamber; strict feasibility is obtained by sending every active interior column predominantly to the two extremes, while retaining tiny positive weights on all permitted edges, then balancing endpoint diagonal masses. This generic sharpness statement is about abstract marginals with specified zero columns, **not** a physical FULL_HIST sharpness theorem.

## 2. A formerly implicit exact time observable

Use the exact seven-node Q-mass map from the frozen checker #1831 and define

\[
C(f)=2M_0(f)+2M_1(f)+\frac{31}{18}M_2(f)+M_3(f)+\frac{5}{18}M_4(f).
\]

Direct coefficient comparison, valid for every real seven-component flow f=(g,a,b,u,v,w,z), gives

\[
\boxed{C(f)=1+\frac89\bigl(T_P(f)-T_Q(f)\bigr).} \tag{3}
\]

For two lawful flows x,y with the same two stopping times, C(x)=C(y). Let H_k(f)=sum_i (r_i-r_k)_+ M_i(f), k=1,...,5, and Delta_k=H_k(y)-H_k(x). Expressing the piecewise-linear coefficients of C on the LR grid yields slopes 0,-10/9,-26/9,-26/9,-10/9,0, hence

\[
\boxed{10\Delta_1+16\Delta_2=16\Delta_4+10\Delta_5.} \tag{4}
\]

This is an exact signed hinge conservation law for the matched-time source/target observers. It is compatible with strictly positive convex-order gaps; no additional vanishing hinge is required. The observer is the full seven-node Q histogram and its specified downstream terminal declarations, with the time-difference coordinate now explicitly reconstructed from the histogram. Any unobserved branch provenance remains outside this observer lease.

## 3. A new strict-Blackwell, lawful, 14-edge physical certificate

Exact source and F-face seedless target:

~~~
x=(999/1000, 1/6, 999/1000, 1/20, 29/240, 11/160, 1/120)
y=(871/1000, 9/40, 5/6, 273/4000, 21/100, 143/1000, 9/400)
~~~

Both satisfy all FULL_HIST physical inequalities, and y satisfies z'=a'/10 and v'-z'=9b'/40, thus 9b'z'=4a'(v'-z'). Both stopping times agree exactly. All seven masses of y and all six potentially active masses of x are strictly positive; M_4(x)=0 and M_4(y)>0. The interior deficit at LR index 1 is nu_1-mu_1=109/80000>0. The five strict hinge gaps are

\[
(\Delta_1,\ldots,\Delta_5)=
\left(\frac{12361}{675000},\frac{1270829}{43200000},
\frac{41353}{2400000},\frac{934829}{43200000},
\frac{20761}{675000}\right)>0.
\]

All omitted E entries below are zero. Each listed E_{ij} is strictly positive. Index i denotes target row, j source column.

| i | j | E_ij |
|---:|---:|---:|
|0|0|33553/432000|
|0|1|763/720000|
|1|1|367/24000|
|6|1|109/360000|
|0|2|25909/993600|
|2|2|323/1000|
|3|2|14339/216000|
|4|2|13/18400|
|3|3|3298/16875|
|0|5|926327/49680000|
|4|5|5003/276000|
|5|5|741/8000|
|6|5|82717/1080000|
|6|6|38053/432000|

Exact independent checks verify all seven target row masses, seven source column masses and seven source-weighted moment equations (1), all physical capacities, seedless condition, both stop times and (4). Minimum positive entry is 109/360000. This explicit construction shows a 14-edge coupling is possible for a nontrivial g=b physical instance with *five strictly positive* convex-order gaps. It does **not** establish a universal 14-edge bound.

## 4. An exact local dimension certificate

Fix source z=1/120 and source b=g. Select eight local physical parameters (g,a,u,v,w,G,A,B), target on F face with parameters (G,A,B) and its u',w' determined by the two stop-time equalities. Let

\[
\Phi=(M_0(y),M_1(y),M_2(y),M_3(y),M_4(y),
M_0(x),M_1(x),M_2(x)).
\]

This map is affine; its exact 8×8 determinant is

\[
\boxed{\det D\Phi=-1111424393/139968000000\ne0.}
\]

The above strict feasible rational witness has 0<g<1 and all inequalities strict relative to the stated g=b source/F-face target stratum, apart from the two face equalities. Therefore the physically attainable normalized marginal pairs locally fill an eight-dimensional region. This matches the dimension of the affine marginal space fixed by nu_4=0, P/Q normalization and the newly identified time-hinge equality (3). The best **uniform** physical edge bound, possibly 14 or 15, remains an exact next question; a full-dimensional physical image alone does not select its minimum support.

## 5. Executed checks and next discriminating question

Python -S, standard-library Fraction only:
- VERIFY_ACTIVE_COLUMNS.py: exact row-rank calculations for all 127 nonempty subsets A; ranks 17, 15 and 13 at the indicated full/end-column-omitted source supports; exact strictly feasible abstract couplings.
- VERIFY_TIME_HINGE.py: affine basis check of (3), exact strict-Blackwell physical witness, and identity (4).
- VERIFY_PHYSICAL_SHARPNESS.py: rational determinant certificate, lawful strict witness and the complete 14-edge matrix verified with all 21 equations.

See accompanying EXACT_OUTPUT_*.txt. The constructive sparse upper bounds are general linear-algebra proofs; the finite checks verify their specific implementation and witnesses. No independent Driver review, formal Task CLAIM, scientific checkpoint acceptance or theorem promotion is asserted.

**Next exact unit:** For the g=b physical/time-hinge slice, determine whether every feasible marginal pair has a ≤14-edge coupling, or find one exact lawful source/seedless-target pair that requires 15. A candidate 14-edge support or 15-edge lower-bound argument must be checked under the *physical* C-conservation identity and lawful capacities; the generic abstract sharpness theorem does not settle this. Separately verify predecessor #1831's multi-PR feasibility stitch before claiming mother-objective mathematical admission.

BRC reuse: the retained carrier is the Q edge-joint E, LR label, both marginals, and weighted column moment. Compression is permitted only by the exact 21 equalities for the declared terminal-declaration observer. Existing exact rational transport tools #1831/#1835 were reused conceptually; this note adds structural source-zero and time-observer laws.
