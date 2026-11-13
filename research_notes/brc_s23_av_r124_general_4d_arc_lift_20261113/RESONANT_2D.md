# R124.3 — Exact two-integer resonant S23 signature oracle

Date: 2026-11-13 (Asia/Shanghai). Follows [R124.2](RELATIVE_3D_REFINEMENT.md); same frozen scientific-input pin \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Work is in the S23 auxiliary ranked Boolean observer.

## Theorem

Fix the R124.2 data \(j,a,c,N,d,m,x,J\) with \(d\neq0\), \(m\ge2\), and **resonance \(c-a=d\) or \(c-a=-d\)**. For any fixed prescribed \(m\)-bit signature, membership feasibility on a rational open parameter atom reduces to **two integer variables** \(n,k\), one real \(\theta\) eliminated by rational affine bounds, and at most \(2|P_m|\) fixed-dimensional ILP feasibility calls. The signed magnitudes of all parameters affect coefficient bit length, not the number of floor cells enumerated. A feasible system gives a rational parameter witness. All half-open endpoint and coincident-endpoint cases are exact.

## Proof

Write \(R_i=x+(N+id-j-a)\theta\), \(\beta=d\theta-\lfloor d\theta\rfloor\), \(n=\lfloor R_0\rfloor\), \(k=\lfloor d\theta\rfloor\), and \(q_i=\lfloor\alpha+i\beta\rfloor\) for \(\alpha=R_0-n\). Then \(z_i=R_i-n-ik-q_i\in[0,1)\) and, by the R124.2 circle-rotation identity,

\[
M_{N+id}(\theta)={\bf1}\{z_i<\delta\},
\qquad\delta=\operatorname{frac}((c-a)\theta).
\]

When \(c-a=d\), \(\delta=\beta\) identically. There is no third floor variable.

When \(c-a=-d\), the fractional-part identity gives the **exact disjoint cases**

\[
\delta =
\begin{cases}
0,&\beta=0,\\
1-\beta,&0<\beta<1.
\end{cases}
\]

The \(\beta=0\) case makes every bit 0, while the positive-\(\beta\) case uses the affine threshold \(1-\beta\). Include both, preserving \(\beta=0\) as an equality constraint rather than discarding it as a measure-zero boundary. Each selected \(q\in P_m\) now provides one system for positive resonance, or at most two for negative resonance:

\[
l<\theta<h,\quad 0\le\beta<1,\quad 0\le z_i<1,\quad
z_i<\delta\ (b_i=1),\quad z_i\ge\delta\ (b_i=0).
\]

These are rational affine constraints in real \(\theta\) and integers \(n,k\), with the required branch guards. Eliminate \(\theta\) by pairwise lower/upper bound comparison, retaining strictness. Fixed-dimension integer feasibility (dimension 2) decides the remaining system in polynomial binary-input cost and reconstructs rational \(\theta\) by the original affine interval. Every original \(\theta\) belongs to one of the systems, and every recovered point satisfies the original directed arc. QED.

For a fixed target pattern there are at most \(2|P_m|=O(m^3)\) two-integer problems, and a factor \(2^m\) suffices to enumerate all target patterns. This extends the structural two-integer advantage of the earlier R123 floor-sum family to arbitrary \(j,a,c\) under the exact resonance condition. It does **not** assert that R123's specific floor-sum implementation directly solves every new resonant instance without adaptation.

## Exact finite tests

[check_r124_resonant.py](check_r124_resonant.py) imports the original independent six-phase critical-point evaluator and the rational affine primitives from [check_r124.py](check_r124.py). It performs exhaustive small integer-lift enumeration for both resonance signs, preserves the \(\beta=0\) case and compares all Boolean signatures to the complete original phase-cut atomization.

Actual execution: \`R124_RESONANT_2D_PASS\` — 112 cases (32 targeted combinations plus 80 deterministic random signed cases), 684 complete signature tests, 609 reachable signatures, 3,334 candidate two-integer conjunctions. See [verification_r124_resonant.json](verification_r124_resonant.json). This is finite checker evidence; the binary-input complexity claim follows from the two-integer projection and classical fixed-dimensional integer feasibility theorem.

## Next

Implement a shared large-coefficient constructive 3D/2D integer-feasibility engine for R124.2 and this resonant case; compare original-input conversion, bit operations, memory, witness quality and residual provenance with R123's specialized 2D floor-sum implementation. Explicitly test \(\beta=0\) singleton fibers, wide rational J, negative time coefficients and disconnected signature sets.

Independent mathematical review and canonical Task/CLAIM remain separate. P000 and native Cell/Link/Port licensing are unchanged.
