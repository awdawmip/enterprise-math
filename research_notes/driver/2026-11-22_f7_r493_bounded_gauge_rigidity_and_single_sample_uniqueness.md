# CBRC F7 r493 — finite-defect gauge rigidity and one-sample uniqueness

Date: 2026-11-22 (Asia/Taipei). Scientific contribution: the continuing original RESEARCH_DRIVER logical lane EM-DVR-DEBB5E, registered own SID MCP-9b4714dc46b948afa4875a86c89c713c. Preserve original CBRC F7 researcher EM-CBRCF7-83A1D4, frozen RR-AA38973D56330E59D315 and its distinct review/Source provenance.

## Exact problem and theorem

Let \(\mathcal A\) be the functions \(q:\mathbb Z^2\to\mathbb R\) satisfying:
\[
q(-x,y)=q(x,y),\quad q(0,0)=0,\quad
q(x,0)=1\ (x\ne0),\quad q(x,y)\ge\tfrac12\ (y\ne0),\quad
q(2,1)=q(-1,-1)=\tfrac12.
\]
For \(k=a-2b-c+2d\), define
\[
D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d),
\qquad E_\infty(q)=\sup_{\mathbb Z^4}|D_q|.
\]
Let \(s(n)=0,1,-1\) according as \(n\bmod3=0,1,2\), and put
\[
G(x,y)=(-1)^{x-y}-(-1)^{x-2y}+2s(x-y)-2s(x-2y).
\]

**Theorem (global defect-fiber rigidity).** Suppose \(q_0,q_1\in\mathcal A\) satisfy
\[
D_{q_0}(z)=D_{q_1}(z)\quad\text{for every }z\in\mathbb Z^4,
\qquad \varepsilon=E_\infty(q_0)<\infty.
\]
Then \(E_\infty(q_1)=\varepsilon\), and there is a **unique** \(b\in\mathbb R\) with
\[
\boxed{q_1(x,y)-q_0(x,y)=bG(x,y)\quad\forall(x,y)\in\mathbb Z^2.}
\]
The parameter satisfies the uniform necessary bound
\[
\boxed{|b|\le\varepsilon/4,\qquad
 b=\bigl(q_1(1,1)-q_0(1,1)\bigr)/4.}
\]
In particular, **an admissible global finite-defect function is uniquely determined by its full defect field \(D_q\) together with the single sample \(q(1,1)\)**. This is an injectivity theorem, not a reconstruction-complexity claim.

The residual one-dimensional ambiguity is genuine at finite defect: for every nonzero \(b\in\mathbb R\), there exist distinct globally F7-admissible finite-defect functions whose defect fields agree and whose difference is \(bG\). No assertion is made that such a pair attains the global minimax optimum.

## Proof

**1. Kernel and homogeneous constraints.** Put \(g=q_1-q_0\). Since the complete defect fields agree, \(D_g=0\). The original F7 evenness, axis/origin values, and both fixed marks imply that \(g\) satisfies their homogeneous linear equalities. The exact constrained-kernel classification proved in r474 therefore supplies unique \(c,b\in\mathbb R\) such that
\[
g(x,y)=A_{c,b}(x-y)-A_{c,b}(x-2y),\quad
A_{c,b}(n)=cn+b(-1)^n+(2b-c)s(n).
\]
In particular \(g(x,y)=cy+P_{c,b}(x,y)\), where the parity/mod-three term \(P_{c,b}\) is bounded and six-periodic in both integer variables.

**2. Finite defect removes the linear drift.** The exact axis-pair identity in r475 gives, for either \(q_i\) at every off-axis point,
\[
\frac12\le q_i(x,y)\le\frac32+\varepsilon.
\]
Hence \(g=q_1-q_0\) is uniformly bounded on all \(y\ne0\); indeed \(|g(x,y)|\le1+\varepsilon\). Fixing \(x=0\) and letting \(y\to+\infty\) in \(g(0,y)=cy+P_{c,b}(0,y)\) forces \(c=0\). Thus \(g=bG\). The r474 independence of the gauge basis gives uniqueness of \(b\).

**3. Single-sample bound.** The sharper r475 axis-pair estimate on \(x=y\) gives
\[
q_0(1,1),\,q_1(1,1)\in[\tfrac12,\tfrac12+\varepsilon].
\]
For \(A_{0,1}(n)=(-1)^n+2s(n)\), \(A_{0,1}(0)=1\), \(A_{0,1}(-1)=-3\), whence \(G(1,1)=4\). Therefore
\[
4b=q_1(1,1)-q_0(1,1),\quad |4b|\le\varepsilon.
\]
If the sample agrees, \(b=0\), so \(q_1=q_0\) globally.

**4. Nontrivial finite-defect pairs exist.** Since \(A_{0,1}(n)\in\{-3,-1,1,3\}\), \(|G(x,y)|\le6\) at every lattice point. Fix any nonzero \(b\). Define \(q_0(0,0)=0\), \(q_0(x,0)=1\) for \(x\ne0\), \(q_0(\pm2,1)=q_0(\pm1,-1)=\tfrac12\), and set \(q_0(x,y)=\tfrac12+6|b|\) at all remaining off-axis coordinates. This even-in-\(x\) function is admissible and bounded. The function \(q_1=q_0+bG\) is also admissible, because \(G\) vanishes on the entire axis and the fixed marked orbits, and \(q_1\ge\tfrac12\) elsewhere by \(|G|\le6\). Both have finite defect (every four-term difference of bounded functions is bounded), with \(D_{q_1}=D_{q_0}\), while \(q_1(1,1)-q_0(1,1)=4b\ne0\). QED.

## Independent arithmetic crosschecks and scope

An exact integer check of all 36 residue pairs \((x,y)\bmod6\) found the frequency table \(G=-6:1,-4:4,-2:8,0:10,2:8,4:4,6:1\). It confirms \(G(1,1)=4\), \(G(2,1)=G(-1,-1)=0\), \(G(-x,y)=G(x,y)\), and \(G(x,0)=0\). With the rational example \(b=1/8\), an independent Fraction-arithmetic check verified both functions' off-axis floor on \([-20,20]^2\), and equality of their original \(D\) formula for all \(9^4=6561\) inputs \((a,b,c,d)\in[-4,4]^4\). Infinite-domain correctness follows from the displayed algebraic proof, not from those finite checks.

This sharpens the interpretation of r474: its **two-dimensional** homogeneous linear gauge family reduces to **one dimension** between two *globally F7-admissible finite-defect functions having identical complete defect fields*. The B31 finite-box feasibility or strict obstruction is still open, and the pre-existing exact range \(e_B=1/2\) for \(1\le B\le30\) is unaffected. This result does not convert a finite-box defect comparison into global equality.

## Dependencies and attribution

- Exact unrestricted kernel and rectangle identity r473: [immutable source](https://github.com/awdawmip/enterprise-math/blob/fbb6b8bec82c41a3708d4373ea075314fb05b2ed/research_notes/driver/2026-11-22_f7_r473_exact_gauge_kernel_and_sharp_global_stability.md).
- Homogeneous constrained two-dimensional classification r474: [immutable source](https://github.com/awdawmip/enterprise-math/blob/6009333d847ea2b78fd4386610ded14b9f8a1d3d/research_notes/driver/2026-11-22_f7_r474_exact_linear_constraint_gauge_classification.md).
- Pointwise coercivity from exact axis pairs r475: [immutable source](https://github.com/awdawmip/enterprise-math/blob/22909ee4fa32737595c5422d683aec956a96346d/research_notes/driver/2026-11-22_f7_r475_global_minimax_attainment_and_finite_box_convergence.md).
- Independent B30 finite witness r491 and B31 witness-specific repair bound r492 retain their prior separate status.

Scientific subunit r493 is authored in the above Driver lane. No new Native Review, Result acceptance, Task/parent closure, official CLAIM, clean-blind original F7 author claim, Source/Activity semantic association or schedule change is asserted by this GitHub publication.