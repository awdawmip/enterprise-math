# BRC S23 — sharp A-side release edge at 7/11 for a pinned ten-decoder bank

**Date:** 2026-11-02. **Evidence type:** author-side exact mathematical proof and executed BigInt rational checker. **Status:** UNREVIEWED / NOT_ADMITTED. **Scientific input pin:** \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`; **specific ten-decoder bank:** \`57a6db1d81068504cca2b3a6ea809a63555473d6\`; **predecessor:** \`c02114d77f9686730566fee07ea7b654acd171c0\`. No native CLAIM/Result or independent review is asserted.

## Theorem

Keep the original BRC N=4, S23 six-source model, the pinned seven fixed decoders \`D1,D2,D3,D4,D6,D7,D8\`, and three specific rational decoders \`K1_old,K2_old,K3_repair\`. With eleven common causal parameters written as

\[
z=(z_0,z_1,z_2,z_3,z_4;\ z_5,z_6,z_7,z_8,z_9,z_{10}),
\]

define the **legal A-side release edge**

\[
Z(t)=(1/5,1/3,t,0,0;\ 1,1,0,1/5,1,0),\qquad 0\le t\le1.
\]

Let \(L_D(z)\) be the maximum total-variation distance across the *six separately labeled* observations for decoder \(D\), and let \(m_{\mathcal B}(z)=\min_{D\in\mathcal B}L_D(z)\), where \(\mathcal B\) is exactly the pinned ten-decoder bank. Then

\[
\boxed{\max_{t\in[0,1]}m_{\mathcal B}(Z(t))=\frac7{11}},
\quad
\boxed{\operatorname*{arg\,max}_{t\in[0,1]}m_{\mathcal B}(Z(t))=\{5/11\}}.
\]

The new **rational adversary** is

\[
W_7=Z(5/11)=(1/5,1/3,5/11,0,0;\ 1,1,0,1/5,1,0).
\]

In bank order, its ten exact errors are

\[
(7/11,\ 1,\ 1,\ 2/3,\ 4/5,\ 2/3,\ 7/11,\ 526/825,\ 7/11,\ 4/5).
\]

The smallest is \(7/11\). The previously recorded W6 witness is \(Z(9/20)\) and has fixed-bank error \(19/30\). The sharp new increment for this bank is therefore

\[
\frac7{11}-\frac{19}{30}=\boxed{\frac1{330}}.
\]

## Source-preserving proof for the whole real interval

Maintain exactly the six source indices and source mixture from the pinned construction:

\[
A=(0,0,0,1,1,1),\quad
B=(2,2,3,2,2,4),\quad
C=(5,6,7,8,9,10),\quad G=(0,0,1,2,2,3).
\]

\[
M=\begin{pmatrix}
10&10&0&0&0&0\\
9&11&0&0&0&0\\
0&0&20&0&0&0\\
0&0&0&10&10&0\\
0&0&0&2&18&0\\
0&0&0&0&0&20
\end{pmatrix}.
\]

For raw source \(i\), put \(x=z_{A_i}\), \(b=z_{B_i}\), \(c=z_{C_i}\), and keep the full causal four-outcome row

\[
R_i(z)=\bigl(x,\ (1-x)b,\ (1-x)(1-b)c,\ (1-x)(1-b)(1-c)\bigr).
\]

The observed source tuple is \(P(z)=(M/20)R(z)\), while decoder \(D\) has observed tuple \(Q(D)=(M/20)(D_{G_i,*})_{i=0}^{5}\). The exact error is

\[
L_D(z)=\max_{0\le i<6}\frac12\sum_{j=0}^3
\bigl|P_{ij}(z)-Q_{ij}(D)\bigr|.
\]

Along \(Z(t)\), each \(R_i\) and hence each complete \(P_{ij}\) is affine in \(t\). For any fixed decoder \(D\), \(L_D(Z(t))\) is convex as a maximum of sums of absolute affine expressions.

The independent exact-rational checker obtains these four values:

\[
L_{D1}(Z(0))=\frac12,\qquad L_{D1}(Z(5/11))=\frac7{11},
\]

\[
L_{D8}(Z(5/11))=\frac7{11},\qquad L_{D8}(Z(1))=\frac12.
\]

On the left interval, D1's convex chord bounds its risk; on the right interval, D8's convex chord does so. As \(m_{\mathcal B}\) is the minimum over all decoders, for **every real \(t\in[0,1]\)**:

\[
m_{\mathcal B}(Z(t))\le
\begin{cases}
\frac12+\frac{3t}{10},&0\le t\le5/11,\\[3pt]
\frac34-\frac{t}{4},&5/11\le t\le1.
\end{cases}
\]

The left expression is strictly increasing to \(7/11\); the right expression strictly decreases from \(7/11\). The exact ten-risk vector at \(W_7\) supplies equality. This proves both the maximum and its unique attaining parameter on the **entire real continuum**, without a mesh-to-continuum inference.

## Positive-volume robust obstruction

Every global parameter \(z_j\) occurs at most once in each raw source law \(R_i\). If only one parameter varies by \(\delta\), its four-outcome TV distance changes by at most \(|\delta|\). Because \(M/20\) has nonnegative entries and each row sums to one, the observed mixture inherits the bound. Telescoping over coordinates and applying the 1-Lipschitz nature of the distance to a fixed decoder yields

\[
\bigl|m_{\mathcal B}(z)-m_{\mathcal B}(w)\bigr|
\le \sum_{j=0}^{10}|z_j-w_j|,\qquad z,w\in[0,1]^{11}.
\]

Therefore the following entire neighborhood of the new witness has error strictly larger than the previous \(19/30\) fixed-bank bound:

\[
\boxed{\left\{z\in[0,1]^{11}:
\sum_{j=0}^{10}|z_j-(W_7)_j|<\frac1{330}\right\}}
\quad\Longrightarrow\quad m_{\mathcal B}(z)>\frac{19}{30}.
\]

The intersection of the open \(\ell_1\)-ball with \([0,1]^{11}\) has positive eleven-dimensional Lebesgue measure, although \(W_7\) lies on boundary faces.

## Verification and next open problem

Execute \`node VERIFY.js > RUN_EVIDENCE.recomputed.json\` in this directory. The source uses reduced fractions with BigInt, reconstructs the seven half-half fixed decoders and three rational kernels, six causal source rows, and nonuniform mixing; checks all decoder stochastic rows, the exact four endpoint values, the ten witness values, the old W6 value and source-affinity at \(t=1/4\). \`RUN_EVIDENCE.json\` is the actual run output. The endpoint convexity proof supplies the universal real-parameter step.

The **joint reoptimized** problem with the prior \(S_{18}\), complete \(J\), complete \(F_5\), complete \(C_6\), and now this complete \(Z\) edge still allows three arbitrary real stochastic decoder kernels. Its existing lower certificate gives \(3/5\), while the concrete pinned bank supplies an upper certificate \(7/11\); the resulting author-side interval is

\[
\boxed{\frac35\le R_{\mathrm{joint}}\le\frac7{11}}.
\]

This is an interval for the reoptimized problem and an **exact theorem only for the stated fixed bank on the edge**. The next discriminating action is to repair \(W_7\) with three jointly reoptimized kernels without losing the previous entire real \(F_5/C_6\) cell-covering certificates, or derive a new universal-in-kernels TV incompatibility lower bound.

**BRC reuse:** The six labeled source probabilities retain their causal origin and positive weights; the TV observer and shared parameter equalities are explicitly preserved. P000/native spatial and time ontology remains a separate project foundation and is not altered by this decoder subproblem.
