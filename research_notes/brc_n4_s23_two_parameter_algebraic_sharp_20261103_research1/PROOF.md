# BRC N=4 S23 — an exact quadratic-irrational two-parameter minimax witness

**Author date:** 2026-11-03. **Scientific frozen commit:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Ten-decoder bank:** `57a6db1d81068504cca2b3a6ea809a63555473d6`; most recent predecessor for this fixed bank: `48f470c7c7be8a5a555ad3f57e145c9ebb4379b5`. **Status:** AUTHOR_ANALYTIC_PROOF / EXACT_QUADRATIC_FIELD_EXECUTED / UNREVIEWED / NOT_ADMITTED. No native CLAIM, Result, or independent mathematical review is asserted.

## Exact theorem

Keep the original six **separately labeled** positive-weight causal preparations, the original nonuniform source-mixing matrix and seven fixed stochastic decoders `D1,D2,D3,D4,D6,D7,D8`, and the three *specific* rational stochastic decoders `K1_old,K2_old,K3_repair` from the predecessor. With the original eleven shared causal parameters define the lawful two-parameter face

\[
T(s,t)=(1/5,s,t,0,0;\ 1,1,0,1/5,1,0),\qquad (s,t)\in[0,1]^2.
\]

For the prescribed decoder bank \(\mathcal B\), let \(L_D(z)\) be the maximum of the six individual source total-variation errors, and \(m_\mathcal B(z)=\min_{D\in\mathcal B}L_D(z)\). Define

\[
\alpha=317-\sqrt{54489},\quad
s_*={\alpha\over250},\quad t_*={\alpha\over184},\quad
R_*={230-\alpha\over230}={\sqrt{54489}-87\over230}.
\]

Then the **complete two-real-parameter** result is

\[
\boxed{\sup_{(s,t)\in[0,1]^2}m_\mathcal B(T(s,t))=R_*\simeq0.636646913035431.}
\]

The explicit algebraic witness is \(T(s_*,t_*)\), where \(s_*\simeq0.334284840007404\), \(t_*\simeq0.454191358705711\). Compared with the predecessor's exact one-dimensional value \(7/11\), the strict increase for this concrete bank is

\[
R_*-{7\over11}={920-11\alpha\over2530}>0.
\]

## Lower certificate: exact ten-error vector

Writing \(R=R_*\), the exact risk vector at \(T(s_*,t_*)\), in bank order, is

\[
\boxed{\left(R,1,1,{250-\alpha\over250},{4\over5},
{250-\alpha\over250},R,R,R,{4\over5}\right).}
\]

Four labels (`D1,D8,K1_old,K2_old`) attain \(R\), and all others have error at least \(R\). All entries are checked in the *same* six-source causal model. This proves the global supremum is at least \(R\).

For clarity, the exact raw source typing and observation map in `VERIFY.js` are

\[
A=(0,0,0,1,1,1),\ B=(2,2,3,2,2,4),\ C=(5,6,7,8,9,10),\ G=(0,0,1,2,2,3),
\]

\[
M=\begin{pmatrix}10&10&0&0&0&0\\9&11&0&0&0&0\\
0&0&20&0&0&0\\0&0&0&10&10&0\\0&0&0&2&18&0\\0&0&0&0&0&20\end{pmatrix}.
\]

For raw source \(i\), put \(x=z_{A_i},b=z_{B_i},c=z_{C_i}\) and
\[
R_i(z)=\bigl(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c)\bigr);
\quad P(z)=(M/20)R(z).
\]
For decoder row kernel \(D\), \(Q_D=(M/20)(D_{G_i,*})_{i=0}^5\) and
\[
L_D(z)=\max_{i=0}^5 {1\over2}\sum_{j=0}^3|P_{ij}(z)-(Q_D)_{ij}|.
\]

## Upper certificate for *all real* points

The six-source tuple \(P(T(s,t))\) is **separately affine** in \(s\) and \(t\). Its only mixed dependence comes from the lawful shared causal products, of bidegree at most \((1,1)\). Choose each axis grid as the eleven rational nodes \(0,1/10,\ldots,1\) **plus its respective algebraic witness coordinate** \(s_*\) or \(t_*\). Each sorted axis then has 12 points, giving **144 exact field-valued vertices and 121 rectangles**.

For every one of these 121 closed rectangles, `VERIFY.js` checks that **one and the same pinned decoder** has \(L_D\le R_*\) on **all four** of its corners. The complete row-major decoder-index selection appears in `RUN_EVIDENCE.json`. Coverage by decoder index (0-based bank order) is
`[27,0,0,36,0,28,28,2,0,0]`; their sum is 121.

For any point inside a rectangle, the vector \(P(T(s,t))\) is the common nonnegative bilinear convex combination of the vectors at the four corners, using scalar weights
\((1-\lambda)(1-\mu),\lambda(1-\mu),(1-\lambda)\mu,\lambda\mu\), with \(\lambda,\mu\in[0,1]\). Total variation against a fixed decoder is convex in the source tuple; taking the maximum over the six sources preserves convexity. The decoder that bounds all four corners therefore bounds every real point of that rectangle by \(R_*\). The rectangles cover \([0,1]^2\), proving the upper bound and the theorem.

## Integer-exact arithmetic and reproduction

All comparisons take place in \(\mathbf Q(\alpha)\), with
\(\alpha^2-634\alpha+46000=0\) and \(\alpha=317-\sqrt{54489}\) the smaller root. Each quantity is normalized as \((a+b\alpha)/d\), \(a,b\in\mathbf Z\), \(d>0\). Addition and multiplication reduce by this minimal polynomial, without floating-point predicates. For comparisons, \(a+b\alpha=(a+317b)-b\sqrt{54489}\); determining its sign reduces to integer signs and comparison of squares against \(54489b^2\), using the sign quadrants. Decimal numbers above are display-only.

Run `node VERIFY.js > RUN_EVIDENCE.recomputed.json` from the research folder. The code reconstructs all four-state causal source rows, all ten decoder stochastic kernels, source mixing, field-valued total variation, the exact ten-error witness, the earlier \(7/11\) check and all 121 same-decoder rectangle certificates. `RUN_EVIDENCE.json` is the actual run of the same checker logic in the authenticated tool V8 isolate, with all 121 decoder choices recorded.

## Scope and continuing question

This is an exact, author-side theorem for the **specified ten-decoder bank** on the entire legal face \(T([0,1]^2)\). For the larger joint problem, three free kernels may be optimized again. The existing universal lower witness certificate for the previously studied union is \(3/5\), and the same concrete bank yields the enlarged union's author-side upper bound \(R_*\), provided the prior pinned F5/C6/J/S18 coverage certificates. Thus its current evidence-based interval is \([3/5,R_*]\). The next unit is a three-kernel joint reoptimization that covers the complete two-real-parameter face together with S18, J, F5 and C6, or a universal-in-kernels TV incompatibility lower certificate. This research changes neither P000/ACTIVE worldview nor task/Owner/CLAIM authority.
