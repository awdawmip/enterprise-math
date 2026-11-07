# BRC N=4 S23: exact 3/5 finite-and-edge repair of W4, followed by a sharp golden-ratio diagonal obstruction

2026-11-02. Author-side exact mathematical construction and executed rational/integer verification. **UNREVIEWED / NOT_ADMITTED**, no native CLAIM or Result. Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. This note continues the exact 4D fixed-bank obstruction \`5493b5468968ef817732f2e235b8a9c550f785a5\`, without altering P000 or the original six-source model.

## Model and exact first result

Retain six separately labeled positive-weight source rows AU0, AU1, AV, BU0, BU1, BV; their original mixing matrix, common four-state encoder, shared causal parameters, and the seven fixed decoding kernels D1,D2,D3,D4,D6,D7,D8. For strategy z and decoder D let

\[
 L_D(z)=\max_{i=1}^6\mathrm{TV}(P_i(z),Q_i(D)),\qquad
 r_{\cal B}(z)=\min_{D\in{\cal B}}L_D(z).
\]

As in the previous exact notes, define \(J(t)=(1,t,0,0,0;0,0,0,0,1,0)\), \(F_3(s,t,u)=(s,t,u,0,0;1,0,0,0,0,0)\), and \(W_4=(1/3,0,1,1/2,0;1,0,0,0,0,0)\). Let S20 be the **20 explicitly defined historical policies** W,J,A,B,C,X,Y,Z,T1,...,T8,U,V,H(1/4),H(1/5), as specified verbatim in VERIFY.py. Let G20 be the **finite** set \(\{F_3(a/20,b/20,c/20):a,b,c=0,\dots,20\}\), containing 9261 strategies. Set \(\Omega=S20\cup J([0,1])\cup G20\cup\{W_4\}\).

**Exact theorem for this scope:**

\[
 \boxed{\inf_{K_1,K_2,K_3\in\mathrm{Stoch}(4,4)}
   \sup_{z\in\Omega}\min_{D\in\{D1,D2,D3,D4,D6,D7,D8,K_1,K_2,K_3\}}
   L_D(z)=\frac35.}
\]

The infimum permits **arbitrary real** stochastic entries. The source and preparation laws remain the original ones. In particular, the theorem covers the complete real J edge, the finite 20th-grid G20, and W4; it does **not** assert a complete real 3D F3 cube or 4D F4 cube bound.

### Explicit rational upper kernels

Use the following row-stochastic 4-by-4 kernels, displayed in the same row/column order as the source model:

\[
K_1^r=\begin{pmatrix}
53/80&0&27/80&0\\
1&0&0&0\\
1/15&1/15&2/5&7/15\\
1/15&0&2/5&8/15
\end{pmatrix},
\quad
K_2^r=\begin{pmatrix}
2/5&0&2/5&1/5\\
2/5&2/5&0&1/5\\
2/5&1/5&0&2/5\\
3/5&2/5&0&0
\end{pmatrix},
\]

\[
K_3^r=\begin{pmatrix}
3/5&2/5&0&0\\
2/5&2/5&1/5&0\\
1/3&43/105&3/35&6/35\\
1/7&2/35&2/5&2/5
\end{pmatrix}.
\]

All twelve rows are nonnegative and sum exactly to 1. VERIFY.py reconstructs the six original observations with source mixture M and decoder-row map G, checks S20 and W4, and exhaustively checks the 9261 points of G20. The maximum of the minimum decoder risks on each of S20, G20 and W4 is exactly 3/5. On J([0,1]), a single kernel covers **both endpoints of each closed interval** [a/5,(a+1)/5], with decoder indices 7,7,7,8,8 (0-based), corresponding to K1r for the first three intervals and K2r for the last two. J preparation is affine in t; convexity of each source's TV under one fixed decoder proves the bound at **every real** t in each interval. This is an analytic continuum argument, not a finite-grid extrapolation.

### Lower certificate (arbitrary real free kernels)

The ten legal policies W,X,Y,Z,T5,U,V,H(1/5),J(1),J(1/5) belong to Omega. Against each of the seven fixed kernels their risk is at least 3/5, so a hypothetical error strictly below 3/5 must assign every one of these ten policies to one of three free kernels. For any three policies a,b,c sharing one free decoder Q, at each prepared source i,

\[
\mathrm{TV}(P_i^a,Q_i)+\mathrm{TV}(P_i^b,Q_i)+\mathrm{TV}(P_i^c,Q_i)
\ \ge\ \sum_{j=1}^4\max(P_{ij}^a,P_{ij}^b,P_{ij}^c)-1.
\]

The exact source rows yield 84 forbidden triples out of 120 with the right-hand side at least 9/5 for some i. Every one of the \(3^{10}=59049\) three-label assignments has a monochromatic forbidden triple (minimum hit count 1). Thus risk strictly below 3/5 is impossible for **all real** free kernels. Together with the explicit bank, this closes the first theorem.

## Second exact result: the new repaired bank has an irrational hidden interior obstruction

Use **the particular bank** \(\mathcal B_r=\{D1,D2,D3,D4,D6,D7,D8,K_1^r,K_2^r,K_3^r\}\) just constructed, and consider the legal diagonal family

\[
 T(x)=F_3(x,0,x), \qquad 1/3\le x\le2/5.
\]

For this entire **real** interval, the six-source TV risks in the bank's displayed decoder order are **exactly**

\[
(2x-x^2,\ 1,\ 1,\ 1,\ 1-x,\ 1,\ 1-x,\ 1-x,\ 1,\ 1-x).
\]

Consequently,

\[
r_{\mathcal B_r}(T(x))=\min(2x-x^2,\,1-x),
\]

whose unique maximum on this closed interval is at

\[
 \boxed{x_*=(3-\sqrt5)/2,\qquad r_{\mathcal B_r}(T(x_*))=(\sqrt5-1)/2>\frac35.}
\]

The two candidate functions are respectively strictly increasing and strictly decreasing on [1/3,2/5]; their unique intersection is x*. A **completely rational** counterexample is T(19/50), whose exact bank risk is \(1539/2500=0.6156>3/5\). This demonstrates why the new bank's complete 21-by-21-by-21 grid coverage cannot be promoted into continuous 3D coverage.

The risk-vector identity is certified by 840 exact event-polynomial inequalities. For each of ten decoders, six source rows and fourteen nontrivial output subsets S, let \(E_{D,i,S}(x)=\sum_{j\in S}(P_{ij}(T(x))-Q_{ij}(D))\). Each E is a degree-2 rational polynomial, because the original causal source laws are polynomial of degree at most 2 on this diagonal. Its coefficients are recovered exactly from evaluations at 0,1,-1. For each row and subset, VERIFY.py proves \(E_{D,i,S}(x)\le R_D(x)\) for **all real** x in [1/3,2/5] by checking both endpoints and any interior quadratic stationary point using Fraction arithmetic. It also finds at least one exact polynomial identity \(E_{D,i,S}=R_D\) per decoder (26 such identities altogether). Since \(\mathrm{TV}(P_i,Q_i)=\max_S E_{D,i,S}\), the ten risk equalities above follow on the entire continuum. The ±1 evaluations are algebraic interpolation samples, not claimed legal strategies.

## Evidence, quantifiers and next dependency

Run \`python VERIFY.py\` (Python standard library only). The emitted JSON is saved as RUN_EVIDENCE.json. The executed source and its saved Git blob should match. It checks all six original rows, exact stochasticity, 20 old points, W4, five complete real-J edge intervals, 9261 **finite** F3 grid points, 84 forbidden triples, 59049 labelings, a rational diagonal counterexample, and 840 exact polynomial event inequalities. No floating point is used in the saved certificate; numerical MILP exploration was discovery only, not the mathematical proof.

The old bank's W4 risk was 2/3, whereas the **new** bank covers W4 at 3/5. Conversely, the new bank has a gold-ratio F3 interior obstruction above 3/5, whereas the **old** bank had an independently proved full F3 3/5 certificate. These are two different constructions. Neither implies a new lower bound for the **reoptimized** \(S18\cup J([0,1])\cup F_3([0,1]^3)\cup\{W4\}\) problem. Its currently justified interval remains [3/5,2/3]. A bank jointly covering both the whole F3 cube and W4 at 3/5, or an incompatibility certificate forbidding one, remains the next load-bearing question.

Author-side proof/computation, not a native Task Result, independent review, Working Truth or Foundation promotion.
