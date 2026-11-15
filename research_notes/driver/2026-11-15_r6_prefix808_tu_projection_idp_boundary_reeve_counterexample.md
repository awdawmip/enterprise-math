# PREFIX-808 follow-up: TU coordinate-projection IDP and a sharp integrality obstruction

Date: 2026-11-15. New derivation: RESEARCH_DRIVER EM-DVR-DEBB5E. Original named bipartite-flow theorem (PREFIX-808): EM-DIRECT-4660FF, source commit e8329aaa77b5621dd252234925d922652039690d. Previous source-exposed IDP corollary: cc663aeb84771075e2f6b2810b772fd1f493151d. **Status:** source-exposed generalization and explicit boundary test; not an independent Native Result review, Task closure, or new native-X6 premise.

## Theorem: every coordinate projection of a bounded integral TU system has integer decomposition

Let \(A\in\mathbb Z^{m\times n}\) be totally unimodular, \(b\in\mathbb Z^m\), and \(l,u\in\mathbb Z^n\) with \(l\le u\). Fix any subset \(T\) of the named coordinates. Suppose
\[
P=\{x\in\mathbb R^n:Ax=b,\quad l\le x\le u\}\ne\varnothing,\qquad Q=\pi_T(P).
\]
For every positive integer \(k\), the scaling \(kP\) scales **all** margins and coordinate bounds together. Then
\[
\boxed{kQ\cap\mathbb Z^T=
\underbrace{(Q\cap\mathbb Z^T)+\cdots+(Q\cap\mathbb Z^T)}_{k\ {\rm summands}}.}\tag{TU-IDP}
\]
Also, for any fixed integral linear additive observer \(W:\mathbb Z^n\to\mathbb Z^d\), the sets of signatures of distinct integer aggregates satisfy
\[
\mathcal S_k:=\{WX:X\in kP\cap\mathbb Z^n\}
=\underbrace{\mathcal S_1+\cdots+\mathcal S_1}_{k\ {\rm summands}}.\tag{TU-SUPPORT}
\]
The latter is equality of **supports**, not equality of histogram coefficients or of named-provenance histories.

### Proof

**Integral lift.** For \(t\in kQ\cap\mathbb Z^T\), the system \(Ax=kb,\ kl\le x\le ku,\ x_T=t\) has a real solution. Appending a coordinate-unit row to a TU matrix preserves TU (expand each square determinant along that row), and so does appending multiple such rows. All RHS and bounds are integral. Hence this nonempty bounded polytope has an integral vertex \(X\in kP\cap\mathbb Z^n\), with \(X_T=t\).

**Decomposition.** Let \(k\ge2\) and \(X\in kP\cap\mathbb Z^n\). Define for each named coordinate
\[
L_e=\max\{l_e,\ X_e-(k-1)u_e\},\qquad
U_e=\min\{u_e,\ X_e-(k-1)l_e\}.
\]
The real \(X/k\in P\) lies between \(L,U\), because \(l\le X/k\le u\) and
\[
X/k-[X-(k-1)u]=(k-1)(u-X/k)\ge0,\quad
[X-(k-1)l]-X/k=(k-1)(X/k-l)\ge0.
\]
The bounded integral TU system \(Ax=b,\ L\le x\le U\) is therefore feasible and has an integral point \(x^{(1)}\). The chosen bounds ensure \(x^{(1)}\in P\cap\mathbb Z^n\) and \(X-x^{(1)}\in(k-1)P\cap\mathbb Z^n\). Induction yields \(X=\sum_{j=1}^k x^{(j)}\). Projection gives the decomposition of \(t\); conversely any sum of \(k\) legal projected integer points is in \(kQ\cap\mathbb Z^T\). Applying \(W\) to full decompositions gives TU-SUPPORT. QED.

This uses only classical integral bounded-TU polyhedra, and does not assert that appending **arbitrary integer observer rows** preserves total unimodularity.

## Exact obstruction: integrality alone does not imply IDP

Take the three-dimensional Reeve tetrahedron at height 2,
\[
P_R=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(1,1,2)\}\subset\mathbb R^3.
\]
Its only lattice points are those four vertices. Indeed a feasible integer point at \(z=1\) would have \(x=\tfrac12+\alpha,\ y=\tfrac12+\beta\) with \(\alpha,\beta\ge0,\ \alpha+\beta\le\tfrac12\), which permits no integer \(x,y\). At \(z=0,2\) one has only the displayed lattice vertices.

But
\[
(1,1,1)=2\cdot\frac14[(0,0,0)+(1,0,0)+(0,1,0)+(1,1,2)]
\in2P_R\cap\mathbb Z^3.
\]
Every vertex has even third coordinate (0 or 2), so any sum of two lattice points of \(P_R\) has even third coordinate and cannot be \((1,1,1)\). Thus this **integral** polytope fails IDP already at \(k=2\), even with no projection. A separate exact enumeration of lattice points in the bounding box \(\{0,1,2\}^3\) found just those four vertices, and the two-summand possible third coordinates \(\{0,2,4\}\); this merely corroborates the algebraic argument.

## Where the earlier PREFIX-808 proof transfers

The source PREFIX-808 finite named bipartite multigraph has integral row/column margins, integral edge capacities, optional frozen edge values and a selected coordinate set. Signing the column incidence rows makes its constraint matrix TU; frozen and selected edges add coordinate fixings. TU-IDP therefore recovers the specific transport projection theorem and extends it to integral **nonzero lower capacities** and general bounded integral TU systems.

It does **not** prove integer decomposition of an arbitrary integral projection, or of an unspecified native-X6/Port/Link relation that merely resembles a flow. For such a transfer one must first prove a lossless reduction to TU equations and coordinate bounds, preserving actual named sources, signs, orientations, multiplicity, readout and update constraints. Reeve's witness makes the logical necessity of an additional structural property explicit.

This is a standard TU/normality consequence, not a worldwide-novel theorem. Original PREFIX-808 authorship remains with EM-DIRECT-4660FF; Driver EM-DVR-DEBB5E contributes the generic proof, scope differentiation and counterexample in source-exposed shared context. No current Task owner is replaced, and no original Result or immutable review is altered.

**Completion:** mathematical subunit proved and GitHub-published; Native Result acceptance 0; formal Task completion 0; mother objective completion 0. Next discriminating mathematics: determine whether the exact named native signed-coupling constraint matrices are TU or admit a minimal non-TU/IDP counterexample, without assuming a native transfer.


## Stronger warning: a TU source can have a nonnormal integer linear image

The Reeve obstruction can occur **even when the source polytope itself has a TU description**. Let
\[
P_\Delta=\{x\in\mathbb R^4: x_i\ge0,\quad x_1+x_2+x_3+x_4=1\}.
\]
Its equation matrix \(A=(1,1,1,1)\) is TU, all data and bounds \(0\le x_i\le1\) are integral, and \(P_\Delta\cap\mathbb Z^4=\{e_1,e_2,e_3,e_4\}\). Define the integral **noncoordinate** readout
\[
W=\begin{pmatrix}0&1&0&1\\0&0&1&1\\0&0&0&2\end{pmatrix}.
\]
The continuous image \(W(P_\Delta)\) is exactly the Reeve tetrahedron \(P_R\). The lattice signature \(y=(1,1,1)\) lies in \(2W(P_\Delta)\cap\mathbb Z^3\), but no integral \(X\in2P_\Delta\cap\mathbb Z^4\) has \(WX=y\), since \(X\) is a sum of two basis vectors, and every \(W e_i\) has even third coordinate. Therefore
\[
W(2P_\Delta\cap\mathbb Z^4)
=\mathcal S_1+\mathcal S_1
\quad\subsetneq\quad
2W(P_\Delta)\cap\mathbb Z^3.
\]
This proves that an **arbitrary integral signed/additive readout of a TU source is not necessarily lattice-surjective at aggregate scale**, even while TU-SUPPORT and integer decomposition of the *full named source tables* remain exactly true.

A sufficient extension beyond coordinate projections is available if stacking the actual readout rows below the TU equation matrix still gives a TU matrix (including the bound rows): then every integral lattice point of \(kW(P)\) has an integral lift through the bounded augmented system, and the same full-source decomposition proves IDP of \(W(P)\). This is a **sufficient** condition, not asserted necessary.

For native signed-Port/Link reductions, it is essential to distinguish the three different sets: (i) integer full-source configurations, (ii) integer **attainable** observer signatures, and (iii) all integer points in the continuous observer image. Equalities of (i) and (ii) under scale do not imply equality with (iii) unless a separate integral-lift theorem applies.


### Even 0/1 observer weights suffice (a named-source duplication witness)

The preceding readout \(W\) had an entry \(2\), which could obscure the true boundary. The same Reeve phenomenon occurs when **every named observer coefficient is \(0\) or \(1\)**. Introduce two distinct named copies \(z_4,z_5\) constrained to equal \(x_4\). Let \(P'\subset[0,1]^6\), with variable order \((x_1,x_2,x_3,x_4,z_4,z_5)\), be defined by the integral equality system
\[
A'=\begin{pmatrix}
1&1&1&1&0&0\\
0&0&0&-1&1&0\\
0&0&0&-1&0&1
\end{pmatrix},\qquad A'v=(1,0,0)^\mathsf T.
\]
The six columns of \(A'\) are three repetitions of \(e_1\), followed by \(e_1-e_2-e_3,e_2,e_3\). Any square minor has determinant \(0,\pm1\) (in particular, the 83 square minors across orders 1–3 were all checked by exact integer arithmetic), so \(A'\) is TU. The lattice points of \(P'\) are precisely the four lifted simplex vertices, the fourth having \(x_4=z_4=z_5=1\).

Use the **0/1-valued** linear readout
\[
W'=\begin{pmatrix}
0&1&0&1&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix}.
\]
The four vertex images are again \(0,(1,0,0),(0,1,0),(1,1,2)\), hence \(W'(P')=P_R\). The lattice value \((1,1,1)\in 2W'(P')\) still has no lifted **integer** aggregate in \(2P'\). The two replicated named witnesses contribute height \(2\), despite every individual readout weight being only \(0\) or \(1\).

Precisely as expected, stacking the observation rows destroys TU. Rows 2,3 of \(A'\) and row 3 of \(W'\), restricted to columns \((x_4,z_4,z_5)\), give
\[
\begin{pmatrix}-1&1&0\\-1&0&1\\0&1&1\end{pmatrix},
\qquad\det=2.
\]
Thus **even nonnegative unit observation weights** do not ensure that a TU source remains integral after readout; the structural augmented-matrix or fiber-integrality condition must be checked. This counterexample has separately named copies and keeps their equality provenance explicit; it does not identify distinct sources or assert any native-X6 correspondence.
