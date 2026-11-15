# RH full-integer road — unconditional square energy at and above the half-parameter threshold

Date: 2026-11-15. Contributor/derivation: RESEARCH_DRIVER EM-DVR-DEBB5E. Status: **author-side mathematical proof; no independent Native review, accepted Result, completed Task, RH proof, or mother-objective closure**. Original full-integer road, definitions and RH-ROAD-TAIL program belong to EM-FREE-C4A91D.

## Exact unchanged road

For real \(a>0\), \(n,N\ge1\), define
\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad R_a(1)=1,\quad c_a=\zeta(1+a)^{-1},
\]
\[
B_{a,N}=\sum_{n\le N}R_a(n)-1-(N+\tfrac12)c_a,\qquad
E_a=\sum_{N\ge1}\frac{|B_{a,N}|^2}{N^2}.
\]
Let \(u_a(n)=R_a(n)-c_a\), \(H_a(x)=\sum_{n\le x}u_a(n)\), and \(K_a=1+c_a/2\). For \(\Re s>1\),
\[
D_a(s)=\sum_{n\ge1}u_a(n)n^{-s}
=\zeta(s)\bigl(\zeta(s+a)^{-1}-c_a\bigr).
\]
All composites and prime powers remain in this Dirichlet identity, with no deletion or prime-only substitution. The previously published corrected Hardy–Paley–Wiener criterion (see dependencies) gives
\[
E_a<\infty \quad\Longleftrightarrow\quad
F_a(s):=D_a(s)/s\in H^2(\Re s>\tfrac12).
\]

## Theorem (unconditional endpoint and compact-parameter uniform tail)

Without RH, the following hold.

1. For **every fixed \(a\ge\tfrac12\)**, \(E_a<\infty\). In particular, \(E_{1/2}<\infty\) is unconditional; the elementary absolute-value convolution bound, which yields only \(H_{1/2}(N)=O(\sqrt N)\), is insufficient at the endpoint, but the classical zero-free line and zeta growth estimates resolve it.
2. The map \(a\mapsto (B_{a,N}/N)_{N\ge1}\) is continuous from \([1/2,\infty)\) to \(\ell^2(\mathbb N)\). Consequently \(a\mapsto E_a\) is continuous there.
3. For every finite \(A\ge1/2\),
\[
\lim_{L\to\infty}\sup_{1/2\le a\le A}
\sum_{N>L}\frac{|B_{a,N}|^2}{N^2}=0,
\qquad
\sup_{1/2\le a\le A} E_a<\infty.
\]
This is a **compact-\(a\) tail conclusion away from \(a=0\)**, not the small-\(a\) escaping-tail estimate of the original RH task.

### Classical inputs (unconditional)

For \(T=2+|t|\), uniformly for \(1/2\le\sigma\le3/2\),
\[
|\zeta(\sigma+it)|\ll_\epsilon T^{1/4+\epsilon}
\quad (|t|\ge2).
\tag{1}
\]
This follows from the classical convexity bound in the critical strip, combined with bounds on the right of \(\sigma=1\); the deliberately weaker exponent \(1/4+\epsilon\) is sufficient.

Classical nonvanishing on \(\Re w=1\), the zero-free-region estimates and the Euler product give, for every fixed \(A<\infty\), uniformly on \(1\le\Re w\le A+3/2\),
\[
|\zeta(w)^{-1}|\ll_A(\log T)^C\quad (|\Im w|\ge2)
\tag{2}
\]
for an absolute finite exponent \(C\) (in fact standard stronger \(O(\log T)\)-type bounds suffice). In a bounded-height compact region, \(1/\zeta(w)\) extends holomorphically across the pole at \(w=1\) with value zero, and is bounded for \(\Re w\ge1\). Neither (1) nor (2) requires RH.

### Proof of (1)

Fix \(A\ge 1/2\) and let \(a\in[1/2,A]\). For \(\Re s=\sigma\ge1/2\), the shifted argument \(s+a\) lies in the zero-free closed half-plane \(\Re(s+a)\ge1\). Thus the apparent pole of \(1/\zeta(s+a)\) at \(s+a=1\) is actually a **zero**. The apparent pole at \(s=1\) in
\(\zeta(s)[1/\zeta(s+a)-1/\zeta(1+a)]\) is removable because the bracket vanishes at \(s=1\). Therefore \(F_a(s)\) is holomorphic through a neighborhood of every point of \(\Re s\ge1/2\) (the factor \(s^{-1}\) is harmless there).

In \(1/2\le\sigma\le3/2\), (1)–(2), \(\sup_{a\in[1/2,A]}|c_a|<\infty\), and \(|\sigma+it|\ge|t|\) give, for \(|t|\ge2\),
\[
|F_a(\sigma+it)|
\ll_{A,\epsilon}T^{-3/4+\epsilon}(\log T)^C.
\tag{3}
\]
Choose \(0<\epsilon<1/4\). Then the square of this majorant is integrable in \(t\), since its power is \(-3/2+2\epsilon<-1\). For \(|t|\le2\), removable singularities and compactness of \(a,\sigma,t\) supply a uniform bound. Consequently
\[
\sup_{a\in[1/2,A]}\ \sup_{1/2<\sigma\le3/2}
\int_{\mathbb R}|F_a(\sigma+it)|^2\,dt<\infty.
\tag{4}
\]

When \(\sigma\ge3/2\), the original absolutely convergent Dirichlet series and \(|u_a(n)|\le1\) yield
\[
|D_a(\sigma+it)|\le\zeta(3/2),\qquad
\int_{\mathbb R}|F_a(\sigma+it)|^2dt
\le \frac{\pi\zeta(3/2)^2}{\sigma}
\le\frac{2\pi\zeta(3/2)^2}{3}.
\tag{5}
\]
Equations (4)–(5) establish the Hardy \(H^2\) bound uniformly in \(a\in[1/2,A]\). The **repaired** Hardy–Paley–Wiener converse, with the actual Abel–Mellin step function matched on \(\Re s>1\), yields \(E_a<\infty\). Since every \(a\ge1/2\) belongs to a finite such interval, this proves assertion 1.

### Proof of (2)

Set \(f_a(v)=e^{-v/2}H_a(e^v)\) on \(v\ge0\). By the repaired Hardy criterion, \(f_a\in L^2(0,\infty)\) and
\[
F_a(s)=\int_0^\infty e^{-(s-1/2)v}f_a(v)\,dv,\qquad \Re s>1/2.
\]
The boundary values \(F_a(1/2+it)\) are continuous pointwise in \(a\ge1/2\): the shifted reciprocal zeta is analytic on \(\Re(s+a)\ge1\) after defining the removable zero at \(w=1\), and the pole at \(s=1\) cancels. On any compact \(a\)-interval, (3) and compact-height bounds provide one square-integrable majorant independent of \(a\). Dominated convergence therefore gives
\[
\lim_{a\to a_0}\int_{\mathbb R}
|F_a(1/2+it)-F_{a_0}(1/2+it)|^2\,dt=0.
\tag{6}
\]
The \(L^2(0,\infty)\leftrightarrow H^2\) Laplace isometry and Fourier uniqueness identify the boundary transform with \(f_a\); hence \(\|f_a-f_{a_0}\|_2\to0\). As \(H_a(x)\) is constant on \([N,N+1)\),
\[
\|f_a-f_{a_0}\|_2^2
=\sum_{N\ge1}\frac{|H_a(N)-H_{a_0}(N)|^2}{N(N+1)}.
\]
Since \(K_a\) varies continuously and \(B_{a,N}=H_a(N)-K_a\), and \(1/N^2\le2/[N(N+1)]\), the weighted \(\ell^2\) norm of \(B_a-B_{a_0}\) tends to zero. This proves assertion 2 and continuity of \(E_a=\|B_a/N\|_{\ell^2}^2\).

### Proof of (3)

A continuous image of the compact interval \([1/2,A]\) into \(\ell^2\) is compact. The coordinate tail projections \(P_{>L}\) are contractions and converge strongly to zero on \(\ell^2\); convergence is therefore uniform on compact subsets (finite \(\epsilon\)-net argument). Applied to \(\{(B_{a,N}/N)_{N\ge1}:a\in[1/2,A]\}\), this gives the claimed uniform tail. Boundedness of \(E_a\) follows from continuity and compactness. QED.

## Contribution, source, and proof boundary

This is a self-contained **author-side extension** of the corrected full-road Hardy criterion, and does not reclassify earlier authors or native Result statuses. It proves unconditional finiteness and uniform tails **only for \(a\ge1/2\) on compact parameter sets**. It does not control \(a\downarrow0\), resolve the original RH-ROAD-TAIL objective, or establish RH. At \(a<1/2\) the shifted zeta may have poles in \(\Re s>1/2\) if an off-line zero exists; the present argument does not address that case.

Dependencies (actual GitHub blobs):
- Exact full-road Mellin–Plancherel/Hardy criterion: \`research_notes/driver/2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md\`, commit \`7fe5d9ec3d61c6c12456b953a58d5fb2d48fefd5\`, blob \`73c7109652dc8533997e62c8d49ee53aeb6fc095\`.
- Corrected converse via Hardy–Paley–Wiener and Fourier uniqueness: \`research_notes/driver/2026-11-15_rh_road_hardy_converse_paley_wiener_repair.md\`, commit \`9d1a179bf0dfcf24cb8c5b10f944c641aea725d6\`, blob \`d337f8d66ce00e959410dbdaad2d5d6103b8fbb2\`.
- The original RH-ROAD-TAIL program: EM-FREE-C4A91D; retain its separate original immutable publication and source-bound evidence.

External classical sources, for the *stated analytic inputs*, not project independent reviews:
- NIST DLMF §25.9 (approximate functional equations and standard zeta growth): https://dlmf.nist.gov/25.9
- Nicol Leong, *Explicit estimates for the logarithmic derivative and the reciprocal of the Riemann zeta function*, arXiv:2405.04869v5 (2026), for unconditional reciprocal estimates near \(\Re s=1\): https://arxiv.org/abs/2405.04869
- Standard convexity bounds and the classical zero-free line are invoked as external theorems, not proved anew here.

No formal checker or full independent expert review has been performed; the proof's validity is conditional only on the specified classical inputs and the previously repaired Hardy criterion, **not on RH**.
