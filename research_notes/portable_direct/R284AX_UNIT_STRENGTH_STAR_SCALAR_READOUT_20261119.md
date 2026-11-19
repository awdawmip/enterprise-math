# R284AX — Unit-strength star Port reconstruction with \(n-1\) exact scalar readings

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Role and provenance: independent portable research, historical researcher lineage EM-DIRECT-E6B1DD; recovered own session metadata MCP-8487128c846440d1952bfc6fa44aeb86; no formal CLAIM asserted.
Scientific input: the R284AT theorem and frozen source pin \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`, via R284AW source \`research_notes/portable_direct/R284AW_OPTIMAL_SINGLE_ENTRY_EXACT_SCALAR_PORT_READS_20261119.md\` (blob \`43d782dc445a780395c7b7eb47f95ca6575b1ab8\`). Retain those immutable scientific pins, not the latest behavioral-rule snapshot.
Observer domain: an auxiliary independently named Port matrix determinant observer. It is a typed algebraic observation model, not a derivation of native X6 Heartbeat World dynamics or a replacement for BRC arithmetic. Signs, directed paths and named joint terms are preserved until the exact reconstruction is certified.

## AX1. Unit-strength optimal count for every \(n\ge3\)

Fix integers \(n\ge3\) and \(H\ge1\), with \(H\) known. Let \(C=(c_{ij})\in\{1,\ldots,H\}^{n\times n}\) be unknown. There exists a *single, nonadaptive, explicitly computable, nonnegative integer diagonal* \(D\), independent of \(C\), such that the following \(n-1\) exact integer scalar values determine \(C\) entrywise:

\[
Y_v=\det(D-C-E_{0v}),\qquad v=1,\ldots,n-1.
\]

Every perturbation has **unit strength \(z=1\)**. All measurements use the *same* \(D\). Input diagonal, scalar outputs, reconstruction arithmetic and the total transferred bits are bounded polynomially in \(n\) and \(\log(H+1)\).

For all \(H\ge2\) the count is nonadaptive-optimal (R284AW/AW2). For \(H\ge4\) it is also adaptive-optimal (R284AW/AW2). In the previously open adaptive cases \(H=2,3\), it is also optimal for **\(n=3\)** (AX3 below). For \(H=1\), the matrix is known without observations.

### Encoding lemma (inherited and explicitly scoped)

Write
\(F(d)=\det(\operatorname{diag}(d)-C)\) and
\(P_v(d)=\det(\operatorname{diag}(d)-C-E_{0v})=F(d)+G_v(d)\).
For \(T\subseteq[n]\), let \(f_T,p_{v,T},g_{v,T}\) be the coefficients of \(\prod_{i\notin T}d_i\), with \(p_{v,T}=f_T+g_{v,T}\). All polynomials are multiaffine. Since the perturbation touches only \(0\to v\), \(g_{v,T}=0\) unless \(\{0,v\}\subseteq T\).

Use R284AW's positive 3-separating integer weights \(w_i=O(n^6)\), with distinct sums for all subsets of each fixed size 1, 2 or 3. Set \(W=1+\sum_i w_i\), \(D_i=B^{W+w_i}\), with \(B\) a power of two greater than twice the sum of the absolute coefficient bounds, e.g. choose \(A=2^{n+1}n!(H+1)^n\) and \(B>2A\). For any \(|T|\le3\), the balanced signed radix-\(B\) digit of \(Y_v\) at
\[
e(T)=\sum_{i\notin T}(W+w_i)
\]
is exactly \(p_{v,T}\). Different complement cardinalities occupy disjoint exponent bands; within the needed cardinalities distinct named subsets have distinct exponents. Unneeded collision aggregates have magnitude \(<B/2\), hence cannot cause carries into another digit. This uses no extra measurement and keeps signed path coefficients.

### AX1 proof for \(n\ge4\)

For any \(|T|\le3\), select a leaf \(v\in\{1,\ldots,n-1\}\) for which \(\{0,v\}\not\subseteq T\). Such a leaf exists: if \(0\in T\), then \(T\) contains at most two leaves while there are at least three. Therefore \(f_T=p_{v,T}\) is recoverable from an *unaffected* observation. All needed \(g_{v,T}=p_{v,T}-f_T\) follow.

Recover
\[
a_i=c_{ii}=-f_{\{i\}},\qquad
q_{ij}=c_{ij}c_{ji}=a_i a_j-f_{\{i,j\}}.
\]
The directed star cofactors give
\[
c_{v0}=-g_{v,\{0,v\}},\qquad
c_{0v}=q_{0v}/c_{v0}.
\]
For \(1\le i<j<n\) the named triple path identity is
\[
g_{i,\{0,i,j\}}=a_jc_{i0}-c_{ij}c_{j0}.
\]
Thus
\[
c_{ij}=(a_jc_{i0}-g_{i,\{0,i,j\}})/c_{j0},\qquad
c_{ji}=q_{ij}/c_{ij}.
\]
All denominators are strictly positive. Reconstruction is exact and unique.

### AX2 proof for \(n=3\): positive-root recovery replaces an unavailable baseline triple

Here two star edges \((0,1),(0,2)\) cover the triple \(\{0,1,2\}\), so its baseline coefficient \(f_{012}\) is **not separately observable** by choosing an unaffected edge. Nonetheless all diagonal entries \(a_i\), pair products \(q_{ij}\), and the directed star entries \(c_{10},c_{20},c_{01},c_{02}\) are recovered as above, using another unaffected edge for each pair.

Let \(x=c_{12}>0,\ y=c_{21}>0,\ xy=q_{12}>0\). The difference of the two *observed triple coefficients* cancels the unobserved baseline:
\[
\Delta=p_{1,012}-p_{2,012}
=g_{1,012}-g_{2,012}
=a_2c_{10}-xc_{20}-a_1c_{20}+yc_{10}.
\]
Set \(s=\Delta-a_2c_{10}+a_1c_{20}\), \(A=c_{20}>0\), \(B_*=c_{10}q_{12}>0\). Then
\[
s=-Ax+B_*/x,\quad
Ax^2+sx-B_*=0,\qquad
x=\frac{-s+\sqrt{s^2+4AB_*}}{2A}.
\]
For positive \(x\), the function \(-Ax+B_*/x\) is strictly decreasing, so there is exactly **one** positive root. Since the true integer \(x\) is a solution, the discriminant is an integer square and exact square-root/division arithmetic recovers \(x\); then \(y=q_{12}/x\). Positivity and the *joint* triple-path difference are essential here. This proves AX1 for \(n=3\).

### Polynomial bit complexity

The inherited explicit 3-separating weights obey \(w_i=O(n^6)\), hence \(\max_i(W+w_i)=O(n^7)\). Choose \(\log_2 B=O(n(\log n+\log(H+1)))\). The diagonal numbers and determinant outputs have polynomial bit lengths, conservatively bounded by \(O(n^9(\log n+\log(H+1)))\) as in R284AW. Exact Bareiss determinants, balanced-base extraction, integer arithmetic and the single \(n=3\) integer square root all run in polynomial bit time. The difference from R284AW is the elimination of its enormous first edit strength \(B^R\); **all perturbation strengths are 1** while the large diagonal encoding remains.

## AX3. Remaining adaptive bounded-integer lower bound resolved at \(n=3\)

For every \(H\ge2\), any deterministic adaptive algorithm with at most **one** single-entry measurement (or one diagonal-only measurement) on \(\{1,\ldots,H\}^{3\times3}\) fails to identify every matrix.

Proof: The first ordered queried edge \((u,v)\) is chosen before obtaining any answer. Let \(w\) be the third vertex, set a positive diagonal gauge \(T\) equal to 1 at \(u,v\) and 2 at \(w\). Choose \(C\) with \(c_{ij}=1\) when \(t_i=2,t_j=1\), \(c_{ij}=2\) when \(t_i=1,t_j=2\), and \(c_{ij}=1\) otherwise. Then \(C\) and \(TCT^{-1}\) are different \(\{1,2\}\)-valued matrices. The gauge commutes with all tested diagonal settings and with the single \(E_{uv}\) because \(t_u=t_v\). The exact scalar response is identical for all diagonal and strength choices. A diagonal-only read is likewise invariant. Hence one read is insufficient. AX1 supplies two unit-strength reads, proving the exact adaptive optimum \(2=n-1\) at \(n=3\), including \(H=2,3\).

The general adaptive bounded-integer lower bound for \(n\ge4\), \(H=2,3\) remains an open continuation unit.

## AX4. Sharp boundary at \(n=2\) for fixed unit strength

With only one \(E_{01}\) probe of strength 1, all responses to all diagonal settings are the same for
\[
C=\begin{pmatrix}1&1\\3&1\end{pmatrix},
\quad
C'=\begin{pmatrix}1&2\\2&1\end{pmatrix}.
\]
Indeed \(\det(D-C-E_{01})=\det(D-C'-E_{01})=(d_0-1)(d_1-1)-6\).
Both belong to \(\{1,2,3\}^{2\times2}\). Thus **one common-diagonal, unit-strength scalar read is not universally sufficient for \(n=2,H\ge3\)**. R284AW's programmable high-strength construction still supplies its one-reading optimum there. For \(n=2,H=2\), unit strength happens to distinguish all four possibilities for the off-diagonal pair once diagonals are read; the statement here is the \(H\ge3\) obstruction.

## Exact validation

Companion: \`R284AX_unit_star_scalar_checker.py\` and \`R284AX_unit_star_scalar_verification.json\`.
Python standard library only, exact integer Bareiss determinant and integer square root, random seed 2842823.
- 824 exact coefficient-vector reconstructions: all 512 matrices in \(\{1,2\}^{3\times3}\), plus 250 seeded \(n=4\), 50 \(n=5\), 12 \(n=6\) positive integer cases.
- 70 actual **single-integer-readout** reconstructions from balanced signed radix: 52 at \(n=3\), 14 at \(n=4\), 3 at \(n=5\), 1 at \(n=6\).
- The \(n=2,H=3\) exact collision is checked at every coefficient.
- Maximum observed diagonal bit length 1,345; scalar output length 6,636 bits; all checked cases passed.
These finite checks test the implementation and examples; AX1/AX3/AX4 have the independent algebraic proofs above. Independent project review remains NOT_REVIEWED.

## Next discriminating questions

1. For \(n\ge4\), settle or refute the adaptive \(n-1\) lower bound for finite alphabets \(H=2,3\), without extending the rational gauge argument beyond its actual integer orbit.
2. Replace generic 3-separating radix coding with a lower-dynamic-range readout that still preserves each named pair and triple path; measure full bit cost.
3. Study integer noise intervals for unit-strength readings. A large exact diagonal still demands high output precision; exact one-unit edits do not by themselves imply low-noise instrumentation.
4. Formalize the distinction between observer compression for the declared auxiliary Port experiment and transfer to native X6/BRC dynamics, preserving unreconstructed residual paths outside the declared observer family.
