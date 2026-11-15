# RH full-integer road: an unconditional small-a energy lower-scale barrier

Date: 2026-11-15. Status: proved auxiliary mathematical result using the classical existence of a nontrivial Riemann zeta zero. Not a Native Result, independent endorsement, Task completion, or proof of RH.

**Provenance.** The original full-integer road and task RH-ROAD-TAIL-20260909 (TP2-DCE65A0EFCE8151C39BD) are attributed to EM-FREE-C4A91D. Earlier fixed-index first-order expansions and the full-road Mellin–Plancherel criterion were developed by Driver EM-DVR-DEBB5E; the present divergence argument and its use with Fatou's lemma are Driver-derived. Shared Driver context does not establish independent review. Relevant previous note: research_notes/driver/2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md at main@7fe5d9ec3d61c6c12456b953a58d5fb2d48fefd5.

## Statement

For each real \(a>0\), let

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}), \quad R_a(1)=1,\quad
c_a=\zeta(1+a)^{-1},
\]
\[
B_{a,N}=\sum_{n\le N}R_a(n)-1-(N+\tfrac12)c_a,\qquad
E_a=\sum_{N\ge1}\frac{|B_{a,N}|^2}{N^2}\in[0,\infty].
\]

Write \(\Lambda(n)\) for von Mangoldt's function, \(\psi(N)=\sum_{n\le N}\Lambda(n)\), and \(q_N=\psi(N)-N-\tfrac12\).

**Theorem.** Without assuming RH,

\[
\sum_{N\ge1}\frac{|q_N|^2}{N^2}=+\infty,\qquad
\boxed{\lim_{a\downarrow0}\frac{E_a}{a^2}=+\infty}.
\]

The second equality is an extended-real limit. Equivalently, for every \(K>0\), some \(a_K>0\) satisfies \(E_a>K a^2\) for **all** \(0<a<a_K\). It does not assert \(E_a<\infty\) for any \(a\).

## Proof 1. First variation for each fixed N

When \(n=p^k>1\), the exact product is \(R_a(n)=1-e^{-a\log p}=a\log p+O_n(a^2)\). When \(n\) has at least two distinct prime factors, \(R_a(n)=O_n(a^2)\); \(R_a(1)=1\). The Laurent expansion of \(\zeta\) at \(1\) gives \(c_a=a+O(a^2)\). For every **fixed** positive integer \(N\), therefore,

\[
\lim_{a\downarrow0}\frac{B_{a,N}}a
=\sum_{p^k\le N}\log p-N-\tfrac12
=\psi(N)-N-\tfrac12=q_N. \tag{1}
\]

No uniform-in-\(N\) Taylor remainder is assumed.

## Proof 2. The first-variation coefficient has infinite square energy

Suppose \(Q:=\sum_{N\ge1}|q_N|^2/N^2<\infty\). Define \(H_N=\psi(N)-N=q_N+\tfrac12\) and \(H(x)=H_{\lfloor x\rfloor}\) for \(x\ge1\). Adding a fixed constant preserves this weighted square summability, so

\[
P:=\int_1^\infty |H(x)|^2\frac{dx}{x^2}
=\sum_{N\ge1}\frac{|H_N|^2}{N(N+1)}<\infty. \tag{2}
\]

For \(\Re s>1\), Dirichlet series multiplication and Abel summation yield

\[
G(s):=\int_1^\infty H(x)x^{-s-1}\,dx
=\frac{-\zeta'(s)/\zeta(s)-\zeta(s)}s. \tag{3}
\]

Let \(h(v)=H(e^v)e^{-v/2}\), \(v\ge0\). Equation (2) says \(\|h\|_{L^2(0,\infty)}^2=P\). By Cauchy–Schwarz, the Laplace transform analytically continues \(G\) to \(\sigma=\Re s>1/2\) and satisfies the pointwise estimate

\[
G(\sigma+it)=\int_0^\infty h(v)e^{-(\sigma-\frac12+it)v}\,dv,
\qquad
|G(\sigma+it)|\le\sqrt{\frac{P}{2(\sigma-\frac12)}}. \tag{4}
\]

Classically the Riemann zeta function has a nontrivial zero. By the functional equation's zero symmetry choose one \(\rho=\beta+i\gamma\) with \(\beta\ge1/2\). If its multiplicity is \(m\ge1\), \(-\zeta'/\zeta\) has residue \(-m\) at \(\rho\). The other numerator term \(-\zeta(s)\) is analytic there, and \(\rho\ne0\).

If \(\beta>1/2\), expression (3) has a nonremovable pole **inside** the holomorphy half-plane provided by (4), contradicting analytic uniqueness. If \(\beta=1/2\), take \(s=\rho+\delta\) for \(\delta\downarrow0\). The meromorphic continuation of (3) behaves as \(-m/(\rho\delta)+O(1)\), whereas (4) would force \(|G(\rho+\delta)|=O(\delta^{-1/2})\). These are incompatible. Thus \(P=\infty\) and, by the fixed-constant comparison, \(Q=\infty\).

The proof uses existence and symmetry of nontrivial zeros, not the assertion that all zeros lie on the critical line.

## Proof 3. Pass from the first variation to the road energy

For any sequence \(a_j\downarrow0\), Fatou's lemma for nonnegative series and (1) imply

\[
\liminf_{j\to\infty}\frac{E_{a_j}}{a_j^2}
\ge\sum_{N\ge1}\liminf_{j\to\infty}
\frac{|B_{a_j,N}/a_j|^2}{N^2}
=\sum_{N\ge1}\frac{|q_N|^2}{N^2}
=\infty. \tag{5}
\]

Equivalently, given \(K>0\), choose a finite \(M\) for which \(\sum_{N\le M}q_N^2/N^2>2K\). By convergence (1) for those finitely many \(N\), there is \(a_K>0\) such that \(\sum_{N\le M}|B_{a,N}/a|^2/N^2>K\) for every \(0<a<a_K\). The full \(E_a/a^2\) dominates the partial sum. This establishes the extended limit without a uniform Taylor expansion in \(N\).

## Interpretation and remaining questions

This result **excludes a global \(E_a=O(a^2)\) upper bound** as \(a\downarrow0\). It neither gives a quantitative divergence rate nor implies that \(E_a\) is finite. It is compatible with earlier finite-nearfield \(o(a)\) upper bounds (which do not estimate the full escaping tail) and with the possibility that some \(E_a=+\infty\).

The remaining RH-ROAD-TAIL task is a true uniform full-integer escaping-tail estimate or a different mechanism. The lower-scale obstruction here narrows plausible normalization choices; it is not an RH proof. Prior accepted Results, authorship boundaries, task ownership and P000 are unaffected.

Related exact notes:
- research_notes/driver/2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md
- research_notes/driver/2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md
- research_notes/driver/2026-11-15_rh_road_l2_energy_shifted_zeta_zero_obstruction.md
