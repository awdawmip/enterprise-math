# PREFIX-607-R2 — One native nonnegative phase probe and exactly n scalar observations recover n BRC gate parameters

**Date:** 2026-11-09 (Asia/Shanghai). **Status:** AUTHOR-SIDE EXACT PROOF + EXECUTED CHECKS; INDEPENDENT REVIEW PENDING.  
**Frozen science pin:** f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged.  
**Dependencies:** PREFIX-602 (16D common image), PREFIX-604 (12+4 split), PREFIX-605 (four gate products), PREFIX-606 (sharp sampled-prefix gap theorem). No P000 mutation, formal CLAIM, Result or review.

## 1. Precise native observer and reproducible one-probe setup

Use the original frozen X6-BRC 48 STAR phases, 96 bit ports, 576 tagged actions and phase-level operator Q(z) at fixed axis weights (1,1,1,1,0,0). The 48-component nonnegative initial phase-sum source is **one fixed probe** \(v=\mathbf1_{48}\) (realizable with one unit in one of the two native ports for each phase, as a *phase-sum* preparation). A **known** two-step native-derived prefix \(y_0=Q(0)Q(1)v\) enters the common 16-dimensional image \(V\). Subsequent real nonnegative unknown gates \(q_1,\ldots,q_n\) generate
\[
y_t=Q(q_t)\cdots Q(q_1)y_0.
\]
At each observed \(t\) we permit reading specified individual **raw output phase coordinates** \(y_t[i]\), with zero-based phase indexing matching PREFIX-605. No full transfer matrix, arbitrary input probing, inferred tagged path history or physical-time calibration is required.

PREFIX-604 constructs exact matrices \(E\in\mathbb Q^{48\times16}\), \(K\in\mathbb Q^{16\times48}\), \(T=KQ(1)E\), \(H=K[Q(2)-Q(1)]E\), \(W\in\mathbb Q^{16\times4}\), \(L\in\mathbb Q^{4\times16}\), and \(P=WL\). They satisfy \(KE=I\), \(LW=I_4\), \(V=E(\operatorname{im}P\oplus\ker P)\), \(H(I-P)=0\), \((I-P)T P=PT(I-P)=0\), \(T^4=16I\), and
\[
L(T+(z-1)H)W=B(z)
=\begin{pmatrix}0&0&0&4(z+3)\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}.
\]
The executable reconstructs these matrices solely from the frozen STAR phase/axis/gate source, not from an assumed output matrix.

## 2. Theorem 607.1 — four fixed raw phase sensors reveal all four gate products

For the initial probe above, exact source calculation yields
\[
w_0:=LK y_0=(9/2,\,4,\,3/2,\,3/4)^\top,\qquad f=(I-P)Ky_0.
\]
The following **exact algebraic certificates** hold in the derived native 48-phase coordinates:
\[
(EW)_{\{3,4,17,26\},:}
=\begin{pmatrix}2&0&0&0\\0&0&0&8\\0&4&0&0\\0&0&8&0\end{pmatrix},
\]
and for all integers \(t\ge0\),
\[
(ET^t f)_{\{3,4,17,26\}}=(12\cdot2^t,\,0,\,12\cdot2^t,\,0)^\top.
\]
The latter holds for all \(t\) because direct exact calculation checks \(t=0,1,2,3\) and \(T^4=16I\). For arbitrary gate sequences, the 12D complement evolves as \(T^t f\) independent of gates; the 4D state \(w_t=B(q_t)\cdots B(q_1)w_0\). Therefore the four **raw native phase outputs** determine it exactly:
\[
\boxed{\begin{aligned}
w_{t,0}&=[y_t[3]-12\cdot2^t]/2,\\
w_{t,1}&=[y_t[17]-12\cdot2^t]/4,\\
w_{t,2}&=y_t[26]/8,\\
w_{t,3}&=y_t[4]/8.
\end{aligned}}
\]
All components of \(w_0\) are nonzero. By PREFIX-605's monomial formula, for each initial \(j\in\{0,1,2,3\}\), put \(r=(3-j)\bmod4\) and \(m_r(t)=|\{s\in\{0,\ldots,t-1\}:s\equiv r\bmod4\}|\). Then
\[
\boxed{p_r(t)=\frac{w_{t,(j+t)\bmod4}}{4^{m_r(t)}\,w_{0,j}}},
\quad
p_r(t)=\prod_{\substack{1\le k\le t\\k-1\equiv r\bmod4}}(q_k+3).
\]
Thus one fixed nonnegative native phase-sum input and only **four scalar raw-phase readings at a chosen checkpoint** determine the entire 4-product gate statistic. For \(t\ge4\) the four products are locally independent. The sensor phases are *fixed* for all horizons; calibration numbers depend only on known t and the known two-step prefix.

**Proof of the four displayed identities.** Reconstruct native STAR phases (4 triads, two signed branches and near relations) and Q(z). Choose pivot columns of \(Q(1)^2\) for E, pivot rows for K, and the rank-one H factorization \(u h\). Set \(W=[u,Tu,T^2u,T^3u]\), \(O=[h;hT;hT^2;hT^3]\), \(L=(OW)^{-1}O\). Exact rational multiplication gives \(w_0\), \(EW\) row values and the four residues of \(ET^t f\) above; the latter extends to all t using \(T^4=16I\). Invariance/intertwining gives \(y_t=E[Ww_t+T^t f]\). Reading four selected rows and inverting the displayed diagonal-permutation block yields the formulas. The monomial formula proves product recovery. QED.

## 3. Theorem 607.2 — one scalar reading per unknown gate, exactly optimal in the smooth setting

Let \(0=t_0<t_1<\cdots<t_m=n\) and each checkpoint gap have length at most 4. Assume previously reconstructed \(p_r(t_{\ell-1})\) are retained. At time \(t_\ell\), each of the \(d_\ell=t_\ell-t_{\ell-1}\) new unknown gates belongs to a different residue class. **Measure only the one raw phase coordinate associated with each such residue**, using the fixed lookup
\[
w_{t,0}\leftrightarrow y_t[3],\quad
w_{t,1}\leftrightarrow y_t[17],\quad
w_{t,2}\leftrightarrow y_t[26],\quad
w_{t,3}\leftrightarrow y_t[4].
\]
The known baseline (12\(\cdot2^t\) for the first two, zero for the others), known \(w_0\) and the formula in Theorem 607.1 give exactly the required new \(p_r(t_\ell)\). For the one index \(k\) in the gap of class r,
\[
q_k=p_r(t_\ell)/p_r(t_{\ell-1})-3.
\]
No unchanged residue class needs measuring. The total count is
\[
\boxed{\sum_{\ell=1}^{m}d_\ell=n}
\]
**raw scalar readings to recover n arbitrary nonnegative real gates**. Thus samples at times 4,8,...,n use four phase sensors for each complete four-gate block and only the required remainder sensors at the last checkpoint. The construction is exact on the closed nonnegative domain \(q_k\ge0\).

On the open domain \((0,\infty)^n\), any differentiable acquisition of \(k\) real scalar statistics with a differentiable exact decoder of *all* n independent gates must have \(k\ge n\): the derivative of the decoder–encoder identity has rank n, while its factorization through \(\mathbb R^k\) has rank at most k. Hence the n-scalar construction is sharp in this explicitly stated smooth measurement class. This is not a lower bound for arbitrary discontinuous encodings or one statistic whose numerical precision encodes multiple arbitrary independent reals.

## 4. Executed exact checks and known limitations

The standalone \`PREFIX607_R2_four_native_phase_sensor_checker.py\` reconstructs Q(z) from frozen STAR/axis/gate definitions. It verifies exact rank-16 pivoting, four-way intertwining, symbolic B(z) relation, the one-probe \(w_0\), the 4x4 sensor coefficient matrix, gate-free baseline at t=0..15 (the all-t derivation uses \(T^4=16I\)), and 45 full native-derived 48-phase vector updates from three distinct 15-step **integer/rational/zero-gate** words. Each step yields the exact 4D state and four products from the raw phase sensors; at t=4,8,12,15 each word is fully recovered using **exactly 15 scalar readings**. All assertions passed using SymPy integer/rational arithmetic.

The mathematical observation is phase-sum based; preserving original 96-port tagged source paths, branch multiplicities, historical provenance or intermediate process measurements remains a separate typed problem. The arbitrary gate values represent operator parameters, not automatically calibrated physical heartbeats. No independent Driver check, formal Result, Working Truth or Foundation promotion is claimed.

## 5. Next useful scientific unit

Investigate **unknown initial source and unknown transient**: what minimal additional calibration (extra probe, earlier sensor or source condition) makes the n-scalar gate reconstruction identifiable, and which exact degrees of freedom remain unobservable without calibration? Account for conversion of native 96-port inputs to phase sums and for exact integer bit costs in an end-to-end algorithm. The one-probe theorem is an operational candidate, not an implementation timing claim.
