# Exact 3/5 minimax for a five-real-parameter BRC S23 face

2026-11-02 · Author-side research, exact integer execution, **UNREVIEWED / NOT_ADMITTED**. Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.

## Theorem (original six-source N=4 S23 model)

Retain the original four-state common encoder, **six separately labeled positive-weight source observations** AU0, AU1, AV, BU0, BU1, BV with their exact 6×6 source mixture, and seven fixed decoding kernels D1,D2,D3,D4,D6,D7,D8. Three additional 4×4 row-stochastic decoders may have arbitrary real entries. Write \(L_D(z)=\max_{1\le i\le6}\operatorname{TV}(P_i(z),Q_i(D))\).

Let \(S_{18}\) be the 18 previously enumerated legal strategies, and \(J(t)=(1,t,0,0,0;0,0,0,0,1,0)\), \(t\in[0,1]\). Consider the **entire five-dimensional real parameter family**

\[
F_5(s,t,u,v,w)=(s,t,u,v,w;1,0,0,0,0,0),\qquad (s,t,u,v,w)\in[0,1]^5.
\]

Then the exact value is

\[
\boxed{\inf_{K_1,K_2,K_3\in\mathrm{Stoch}(4,4)}
\sup_{z\in S_{18}\cup J([0,1])\cup F_5([0,1]^5)}
\min_{D\in\{D1,D2,D3,D4,D6,D7,D8,K_1,K_2,K_3\}}
L_D(z)=3/5.}
\]

This strengthens the earlier verified 3D theorem and closes the previously reported \([3/5,2/3]\) interval for the four-dimensional reoptimized family. The 4D witness \(W_4=F_5(1/3,0,1,1/2,0)\) and the diagonal \(T(x)=F_5(x,0,x,0,0)\), including the irrational golden-ratio point, lie in the proved family.

## Upper-bound bank: one-kernel substitution

Reuse **K1_old and K2_old** verbatim from prior immutable source \`de0ddc3371ec886be1eb906958cb16e3b4db0978\` and substitute **only K3** by the W4-repair kernel from \`5c55d0b6cd628d134d50b31a0a317e4eb3c9ee5f\`:

\[
K_1=\begin{pmatrix}2/5&0&2/5&1/5\\2/5&2/5&0&1/5\\3/5&0&0&2/5\\2/5&2/5&0&1/5\end{pmatrix},\quad
K_2=\begin{pmatrix}1/2&1/2&0&0\\1/2&0&0&1/2\\0&0&1/2&1/2\\0&0&1/2&1/2\end{pmatrix},
\]

\[
K_3=\begin{pmatrix}3/5&2/5&0&0\\2/5&2/5&1/5&0\\1/3&43/105&3/35&6/35\\1/7&2/35&2/5&2/5\end{pmatrix}.
\]

All rows sum to 1 and are nonnegative. \`VERIFY.js\` reconstructs the six original observed source distributions from the original causal parameter map, source mixture and decoder-row map. It checks all 20 historically named strategies (including the 18), W4 with risk **exactly 3/5**, and the rational golden-diagonal witness T(19/50), which now has bank risk **1/2**.

For J([0,1]), K2 covers both endpoints of [0,2/5] with risk 1/2, and K1 covers both endpoints of [2/5,1] with risk 3/5. Its preparation law is affine in t; TV convexity proves full real-edge coverage.

For F5, partition **each** of the five unit axes into ten closed subintervals. There are \(11^5=161051\) distinct grid vertices and \(10^5=100000\) five-dimensional cells, each with \(2^5=32\) corners. The exact integer verifier checks **all ten decoders against all 32 corners** of every cell and chooses the lowest-index decoder minimizing the maximum corner risk. Every selected maximum is at most 3/5; the sharp maximum among selected cell risks is 3/5. The full ordered 100000-character decoder-index witness, indexed lexicographically with the fifth axis fastest, is in \`RUN_EVIDENCE.json\`.

For a **fixed** decoder \(D\), the source preparation map \(P_i(s,t,u,v,w)\) is separately affine in each coordinate. Inside any closed cell, the **entire six-row preparation tuple** is therefore a common 32-corner tensor-product convex combination, with nonnegative interpolation weights summing to 1. Convexity of each total variation distance, followed by maximum over the six source rows, yields

\[
L_D(z)\le\max_{\text{32 corners }c}L_D(c)\le 3/5
\]

when D is the cell's selected decoder. Thus the exact finite **common-decoder-per-cell** certificate covers all real parameters, including irrational interior points. The verifier also checks a complete five-coordinate midpoint interpolation identity.

## Lower-bound certificate: arbitrary real decoders

The same ten legal strategies \(\{W,X,Y,Z,T5,U,V,H(1/5),J(1),J(1/5)\}\) belong to the theorem's set. Against every fixed decoder, each has risk at least 3/5. If a putative three-free-kernel bank had worst-case risk strictly below 3/5, these ten strategies would have to be assigned among three free decoders.

For any triple a,b,c and source i sharing a free decoder Q, the exact event inequality is

\[
\sum_{k\in\{a,b,c\}}\operatorname{TV}(P_i^k,Q_i)\ge
\sum_{j=1}^4\max(P_{ij}^a,P_{ij}^b,P_{ij}^c)-1.
\]

Precisely **84 of 120** three-strategy triples have some source row with right-hand side at least 9/5. All \(3^{10}=59049\) assignments to three free labels have at least one monochromatic forbidden triple (minimum hits=1). Therefore radius strictly below 3/5 is impossible for **arbitrary real row-stochastic** free decoders. Combined with the explicit bank this proves equality.

## Exact execution and scope

The saved verifier uses V8 safe **integer** arithmetic with probability scale N=16,800,000 and TV denominator 2N=33,600,000. It performs checks for stochastic rows and normalization, original 6×6 mixtures, 20 historical strategies, J edge endpoints, W4, rational diagonal, all 161051 vertices, **all 100000 32-corner cell certificates**, the midpoint interpolation identity, 84 event inequalities and 59049 assignments. Its output is the nonempty \`RUN_EVIDENCE.json\` with the entire cell-selection witness. The real-interior conclusion follows from the proved multi-affinity and TV convexity, not from sampling. No mathematical review or native Task Result has been claimed.

The complete unrestricted eleven-parameter, ten-label mother problem retains the distinct previously established \([1/2,2/3]\) interval. Next: vary one of the six parameters currently fixed as (1,0,0,0,0,0), test the first genuinely six-dimensional continuous extension with the same bank, and seek either a new common-cell certificate or a legitimate counterexample / reoptimized kernel.
