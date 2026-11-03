# BRC N=4 / S23: a nine-event linear decoder and sharp uniform noise modulus

Date: 2026-11-03. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen scientific source: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Immediate predecessor (author-side, unreviewed): \`53dd28b185fb9e499a84b8f127c1d87a52809ec6\`, minimal scalar repair of one deleted source label.

## Statement, population and observers

Consider the frozen six-source/four-outcome S23 statistical model. Let \(z=(z_0,\dots,z_{10})\in[0,1]^{11}\); the six unprepared source laws are
\[
R(p,q,r)=\big(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r)\big)
\]
with source-index triples
\[
A=(0,0,0,1,1,1),\quad B=(2,2,3,2,2,4),\quad C=(5,6,7,8,9,10).
\]
The labeled prepared observations \(P_j\), \(j=0,\dots,5\), mix the six source laws with \(M/20\), where
\[
M=\begin{pmatrix}
10&10&0&0&0&0\\9&11&0&0&0&0\\0&0&20&0&0&0\\
0&0&0&10&10&0\\0&0&0&2&18&0\\0&0&0&0&0&20
\end{pmatrix}.
\]
Let \((N,E)\) be the two members of a mask pair \((3,31),(7,27),(11,23),(15,19)\), ordered so \(N\) omits bit 2 and \(E\) contains bit 2. Each mask overwrites the indexed coordinates among \(z_0,\dots,z_4\) by its known constant \(\beta_N,\beta_E\in[0,1)\), respectively. There is **no original observation**. The same labeled row \(j\) is missing in both views; the predecessor's minimum scalar repair is instrumented: measure \(P^E_{j,2}\) if \(j=0,1,3,4\), or measure \(P^{U_g}_{j,1}\) and \(P^{V_g}_{j,2}\) if \(j=2,5\). Here \(g=3\) for row 2 and \(g=4\) for row 5, \(U_g\) is the view not overwriting gate \(g\), and \(V_g\) is the view overwriting gate \(g\).

These measurements retain their source row, view, and outcome index; their declared future-operation horizon is precisely the stated two interventions. The target unknown is the nine-coordinate vector \(x=(z_2,\dots,z_{10})\); \(z_0,z_1\) are overwritten in both views.

## Theorem: a globally linear nine-feature coordinate system

Pick \(r=1\) if \(j=0\), and \(r=0\) otherwise. From retained rows and exactly the repaired scalars, extract nine event probabilities, **in this order**:
\[
\begin{aligned}
y_0 &=P^N_{r,1},&
y_1 &=P^{U_3}_{2,1},&
y_2 &=P^{U_4}_{5,1},\\
y_3 &=P^{V_3}_{2,2},&
y_4 &=P^{V_4}_{5,2},&
y_5 &=P^E_{0,2},\\
y_6 &=P^E_{1,2},&
y_7 &=P^E_{3,2},&
y_8 &=P^E_{4,2}.
\end{aligned}
\]
If the row in an entry is deleted, that entry is precisely one of the additional scalar measurements listed above. Otherwise it is a retained observation. This is true for all six possible deletions.

Put \(a_N=1-\beta_N,\ a_E=1-\beta_E,\ k=a_E^2\); for \(v=U_g,V_g\), put \(a_v=1-\beta_v\). Then **for every real state \(z\in[0,1]^{11}\)**,
\[
\begin{aligned}
y_0&=a_Nz_2,&y_1&=a_{U_3}z_3,&y_2&=a_{U_4}z_4,\\
y_3&=a_{V_3}^2z_7,&y_4&=a_{V_4}^2z_{10},\\
y_5&=k(z_5+z_6)/2,&y_6&=k(9z_5+11z_6)/20,\\
y_7&=k(z_8+z_9)/2,&y_8&=k(z_8+9z_9)/10.
\end{aligned}
\]
Hence \(y=F_{N,E,\beta}(x)\) is a globally **linear**, nonsingular map on nine coordinates, independent of \(z_0,z_1\). It has the inverse
\[
\begin{aligned}
z_2&=y_0/a_N,\ z_3=y_1/a_{U_3},\ z_4=y_2/a_{U_4},\\
z_7&=y_3/a_{V_3}^2,\quad z_{10}=y_4/a_{V_4}^2,\\
t_0&=y_5/k,\ t_1=y_6/k,\ t_3=y_7/k,\ t_4=y_8/k,\\
z_5&=11t_0-10t_1,\quad z_6=-9t_0+10t_1,\\
z_8&=(9t_3-5t_4)/4,\quad z_9=(-t_3+5t_4)/4.
\end{aligned}
\]

### Sharp uniform inverse modulus for the selected events

Define \(D(z,w)=\max_{0\leq i\leq8}|y_i(z)-y_i(w)|\). For all \(z,w\in[0,1]^{11}\),
\[
\|z_{2:10}-w_{2:10}\|_\infty \le C_{N,E}D(z,w).
\]
The **smallest possible** global constant for this selected nine-event observer is
\[
\boxed{
C_{3,31}=\max\left\{\frac{21}{(1-\beta_E)^2},\frac1{1-\beta_N}\right\}
}
\]
and
\[
\boxed{
C_{7,27}=C_{11,23}=C_{15,19}
=\max\left\{\frac{21}{(1-\beta_E)^2},\frac1{(1-\beta_N)^2}\right\}.
}
\]
The indexing of constants uses \(N,E\), not the displayed integer ordering in each pair.

**Proof.** The stopping law and \(M/20\) give all nine linear identities by direct multiplication; the two paired \(2\times2\) mean matrices have determinant \(1/20\) and \(2/5\), respectively, after writing their displayed normalizations. Their listed inverses follow by ordinary elimination. In the induced \(\ell_\infty\) operator norm, the inverse paired-block row sums are \((21,19)/k\) for \((z_5,z_6)\) and \((7/2,3/2)/k\) for \((z_8,z_9)\). The other five rows of \(F^{-1}\) have sums
\[
1/a_N,\quad 1/a_{U_3},\quad 1/a_{U_4},\quad
1/a_{V_3}^2,\quad 1/a_{V_4}^2 .
\]
For \((3,31)\) both \(U_g=N,V_g=E\); for each other scheme at least one \(V_g=N\). Since \(0<a_N,a_E\leq1\), the dominant sums simplify to the two boxed expressions. This establishes the upper bounds for all real pairs.

For sharpness, the linear isomorphism sends the open cube \(x\in(0,1)^9\) to an open subset of \(\mathbb R^9\). Start at \(x=(1/2,\dots,1/2)\), fix one maximal row of \(F^{-1}\), and perturb the nine features by \(h\) times the sign of each coefficient in that row (zero where the coefficient is zero). For sufficiently small \(h>0\), both the original and perturbed features are realized by admissible cube states and their ratio of output \(\ell_\infty\)-distance to input \(\ell_\infty\)-distance attains exactly the corresponding inverse row sum \(C_{N,E}\). The untouched \(z_0,z_1\) may both be \(1/2\). This proves the constant is global and sharp, including when the maximizing block changes with \(\beta_N,\beta_E\). \(\square\)

### Noise interpretation and a design separation

If each selected event probability is measured with absolute error at most \(\eta\), the linear estimator \(F^{-1}(\widehat y)\) obeys \(\|\widehat x-x\|_\infty\le C_{N,E}\eta\). For two independent states or repeated sets of measured events the analogous difference inequality above holds. This bound is valid for any real perturbations, including events whose noisy collection is not a coherent probability distribution. It is exactly optimal for feasible feature changes.

Example: \(\beta_E=0,\beta_N=9/10\) gives \(C_{3,31}=21\), whereas \(C_{7,27}=C_{11,23}=C_{15,19}=100\). Thus a design difference survives after repairing every missing source and letting all retained selected events carry noise. With \(\beta_E=\beta_N=1/2\), all four constants equal \(84\).

**Scope of sharpness.** The exact constant pertains to the nine explicitly selected scalar event coordinates and to its associated estimator. All other retained event probabilities can be used by an alternative estimator, potentially producing a smaller optimum under a metric over the complete observation bank. Determining the latter optimum remains a separate question. The current result is an exact, globally valid robustness guarantee when the noisy retained rows are not assumed equal.

## Executed evidence and further mathematical target

\`VERIFY.js\` executes an exact \`BigInt\` reduced-rational implementation of the complete six-source mixture, the selected features, and the analytic inverse. Tested: all four masks; beta pairs \((0,0),(1/2,1/4),(3/4,9/10),(9/10,3/4)\); all six deleted rows; 1,536 deterministic rational state-pair reconstruction/bound checks and 96 explicit feasible equality witnesses, with no floating-point comparisons. Actual output is in \`RUN_EVIDENCE.json\`. The displayed all-real-domain proof uses the linear inverse and maximal-row construction; finite tests are supplementary.

BRC reuse: preserve six distinct source labels and the joint prepared-row matrix. The statistic extraction has an explicit observer and fixed two-view horizon; its sufficiency is proved by the full inverse, rather than inferred from source-mass totals or an unlabeled quotient. P000's native six spatial axes and independent time are unchanged; this is a typed statistical-model statement.

The fixed original \`k=4/6\`, ten-decoder-bank minimax mother problem is still open under the previously recorded interval \([1/2,2/3]\); this repair/robustness result addresses an observation-design subsidiary problem, not that minimax endpoint.
