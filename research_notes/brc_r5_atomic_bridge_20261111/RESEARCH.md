# R5 — exact sharp two-atom BRC bridge between the A and C minimum source-3 support faces

Date: 2026-11-11 (Asia/Shanghai). Classification: author-side exact auxiliary-model theorem with an independently executable rational certificate; formal Source CLAIM/Result and independent review pending. Native activity registration was requested during this run; its authoritative result should be checked separately.

## Frozen scientific object and dependency

Reuse the seven-ratio auxiliary P/Q–BRC Blackwell transfer fiber from R5 PRs #2063 and #2068; **do not repin the science**. The R5 preceding report lists frozen global source at \`a01383f825ef9d43b4b754254303298c64041568\` and Enterprise Math scientific source at \`86149263e38c22292c9def1e0f69092efa1be77e\`, with the original strictly positive rational 30-arc reference transfer from PR #2017, reproduced in the checker.

Integer ratios: \(R=(2,10,15,20,25,30,38)\). Dynamic arcs \(V=\{(i,j):i=0,\ldots,6,\ j\in\{1,2,3,5\}\}\) have 28 nonnegative rational masses \(x\). Two positive singleton arcs \((0,0),(6,6)\) remain unchanged. The 15-row linear observation system \(Ax=b\) comprises seven target marginals, four source marginals and four source first moments; \(\operatorname{rank}(A)=13\). The fixed fiber is \(\mathcal F=\{x\ge0:Ax=b\}\).

The previous exact support census proves the feasible four-target masks for source 3 are exactly \(A=\{1,3,4,6\}, C=\{2,3,4,6\}, B=\{2,3,4,5\}\), and the minimax source-3 support peak for \(A\to C\) is five. Here, an **elementary atom** is one signed six-arc \(K_{2,3}\) residual on source pair \(\{3,j\}\), \(j\in\{1,2,5\}\), and three targets, with both its source rows having opposite signed masses and satisfying the mass and \(R\)-first-moment conservation equations. A primitive move is the nonnegative line segment \(x\to x+tH\); the source and target arc labels remain explicit.

## Exact theorem

**There exist \(X\in F_A\), \(Y\in F_C\) and a two-move path \(X\to W\to Y\) inside \(\mathcal F\) such that the number of positive source-3 targets is at most five throughout, and no one-move elementary-atom path can connect any transfer in \(F_A\) to any transfer in \(F_C\).** Consequently the minimum number of elementary signed \(K_{2,3}\) residual moves in an optimal-support bridge \(A\to C\) is

\[
\boxed{N_{\mathrm{atomic}}(A,C;\max\operatorname{supp}_3\le5)=2}.
\]

### Upper bound: explicit exact two-move witness

Use 28-dimensional \(X\), in dynamic source-major order \(j=1,2,3,5\) and target-minor order \(i=0,\dots,6\), exactly as written in \`VERIFY_ATOMIC_BRIDGE.py\`. Every entry is rational and nonnegative; \(\operatorname{supp}_3(X)=\{1,3,4,6\}\).

Define \(H_j\) for \(j=1,2\) by its only nonzero entries:

\[
(H_j)_{1,3}=-23,\quad(H_j)_{2,3}=28,\quad(H_j)_{6,3}=-5;
\quad (H_j)_{i,j}=-(H_j)_{i,3}\quad(i=1,2,6).
\]

Because \(-23+28-5=0\) and \(10(-23)+15(28)+38(-5)=0\), both \(AH_j=0\). Let

\[
t_1=\frac{4023851}{1367527721}, \qquad
t_2=\frac{196521}{67951688},\qquad
W=X+t_1H_1,\quad Y=W+t_2H_2.
\]

The checker verifies, using Python \`Fraction\` only:

- all 15 observer equations for \(X,W,Y\), with exact common right-hand side \(b\);
- all 28 dynamic masses are nonnegative at each endpoint, and the two fixed singleton arcs are strictly positive and unchanged;
- source-3 masks \(\operatorname{supp}_3(X)=A\), \(\operatorname{supp}_3(W)=A\cup C=\{1,2,3,4,6\}\), \(\operatorname{supp}_3(Y)=C\);
- \(t_1,t_2>0\), exact atom identities and preserved target/source labeled provenance.

Convexity of the nonnegative orthant and of the observer fiber keeps each segment nonnegative. During either open segment the source-3 support has exactly five entries, establishing the sharp peak.

### Lower bound: nine exhaustive exact Farkas certificates

Any single elementary residual changing source-3 support from \(A\) to \(C\) must use source pair \(\{3,j\}\) for some \(j\in\{1,2,5\}\). Its triple must contain targets \(1,2\) (removed and introduced) and a third target \(u\) in the common mask \(A\cap C=\{3,4,6\}\): an additional external target would be nonzero at one endpoint. This gives exactly \(3\cdot3=9\) possibilities.

For each \((j,u)\), choose the unique normalization \(h_{1,3}=-1\) and write the target coefficients

\[
h_{2,3}=\frac{R_u-R_1}{R_u-R_2},\qquad
h_{u,3}=1-h_{2,3}.
\]

Let the starting nonnegative variables \(X_k\) be allowed only on mask \(A\), and \(t\ge0\) be the displacement. Introduce nonnegative slacks \(s_k=X_k+t h_k\) for the endpoint \(Y\), together with the endpoint zero \(Y_{1,3}=0\). This is a linear feasibility problem \(\mathsf Bz=d\) with **nonnegative** unknowns \(z=(X_{\mathrm{allowed}},t,s)\), 44 equality rows (15 observations, 28 endpoint-slack rows, one endpoint-zero row), and exact rational right-hand side \(d=(b,0,\ldots,0)\).

The checker embeds nine sparse integer dual vectors \(y_{j,u}\) and verifies, coefficient by coefficient,

\[
\mathsf B^{\mathsf T}y_{j,u}\ge0,\qquad d^{\mathsf T}y_{j,u}<0.
\]

For any \(z\ge0\), this would force \(0\le z^{\mathsf T}\mathsf B^{\mathsf T}y=d^{\mathsf T}y<0\), a contradiction. The nine exact negative values of \(d^{\mathsf T}y\), listed in \`EXACT_OUTPUT.txt\`, complete the proof for every possible single atom, without a numerical optimizer or an unbounded search.

## Structural interpretation

Both primitive atoms have the **same** target triple \(\{1,2,6\}\) and identical source-3 signed pattern \((-23,28,-5)\). Their compensation is split over source ports **1 and 2**. No **single** paired port can accommodate the required transition in the fixed observer fiber, as shown by the nine certificates; distributing the compensation over two ports makes it feasible. This is a specific, source-labeled BRC residual decomposition law; it is not a physical native X6 dynamics claim.

## Validation, provenance, and next research units

Run from the folder: \`python3 VERIFY_ATOMIC_BRIDGE.py\`. Expected terminal line: \`PASS_R5_EXACT_SHARP_TWO_ATOM_A_C_BRIDGE_9_NO_GO_CERTIFICATES\`. The exact checker was actually run locally before publication using standard-library \`Fraction\`; \`EXACT_OUTPUT.txt\` reproduces the observed run. The discovery step used floating-point linear programming and exact rational reconstruction, but **the delivered theorem is verified solely by the pinned rational primal witness and integer dual certificates**, independently of the discovery optimizer.

The R5 object is the original frozen auxiliary physical-transfer *observation* fiber, not an asserted native physical model. The new finding is an author-side proof/certificate and requires independent mathematical review and formal Source Result acceptance before promotion. Source-native activity/owner verification should be reconciled with the corresponding pending native request IDs; the GitHub-connected account's write permission is not a TASK claim.

Next: repeat the exact signed-atom minimum for \(C\to B\), and determine whether \(A\to B\) can be realized in three elementary moves while maintaining source-3 support at most five. Also classify source-port splitting as a general mechanism using a dual capacity certificate, without losing source/target identity.