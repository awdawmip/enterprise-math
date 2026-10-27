# D25/LIFT R45 — 原始 W/S 权重下的反射配对一阶证书与非恒定阻断

2026-10-27 (Asia/Hong_Kong). Portable author research; logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`. Exact task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`, parent D25/LIFT/JT2 OPEN. Scientific Source pin (unchanged): \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Inherited mathematics: R39–R42 three-regime source transport and R43–R44 reflected **unweighted** kernel at \`c91d798c220e09147713a2cfb7c5947deb2adb60\`.

Evidence status: \`AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY\`. This file does not claim native CLAIM/open/checkpoint/Result/review.

## Source and observer typing

Keep the **unchanged original source terms**
\[
w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5\,216^k},\quad
s_k=\frac{(8k+1)(4k)!}{(k!)^4\,2304^k},\quad
\tau_k=\frac{k!(4k)!}{(2k)!(3k)!}\left(\frac3{32}\right)^k .
\]
They obey the exact rational identity
\[
s_k/w_k=\frac{8k+1}{6k+1}\tau_k.
\]
For a prime \(p=6m+1\), define the auxiliary *multiplicative reflected-pair* observer
\[
E_{p,k}=\frac{s_ks_{p-k}}{w_kw_{p-k}}\in\mathbb Q_p^\times.
\]
The summation rank \(k\) is not a native X6 spatial axis. Original W/S source labels and individual weights remain recoverable; this auxiliary observer is not the required additive WZ sum.

## R45-A: complete first jet of the *weighted* reflected low band

**Theorem.** For every prime \(p=6m+1\ge19\) and integer \(1\le k<p/4\) with
\[
(1-36k^2)(1-64k^2)\not\equiv0\pmod p,
\]
write \(H_n=\sum_{j=1}^n1/j\), \(H_0=0\), and \(Q_*=q_p(3/32)=((3/32)^{p-1}-1)/p\pmod p\). Then, with every displayed denominator a \(p\)-adic unit,
\[
\boxed{ E_{p,k}\equiv
\frac3{16}\frac{1-64k^2}{1-36k^2}
\left[1+p\left(
Q_*+H_{k-1}+4H_{4k-1}-2H_{2k-1}-3H_{3k-1}
+\frac2{(1-8k)(1-6k)}
\right)\right]\pmod{p^2}. }\tag{R45-A}
\]

**Proof.** Retain the exact four source terms:
\[
E_{p,k}=\frac{(8k+1)(8(p-k)+1)}{(6k+1)(6(p-k)+1)}
       \tau_k\tau_{p-k}.
\]
R43–R44 yield in the stated band \(e_k=e_{p-k}=0\), \(C_{p,k}=3\), and
\[
\tau_k\tau_{p-k}\equiv\frac3{16}
\left[1+p(Q_*+H_{k-1}+4H_{4k-1}
-2H_{2k-1}-3H_{3k-1})\right]\pmod{p^2}.
\]
The *separate original linear weights* contribute
\[
\frac{(8k+1)(8p-8k+1)}{(6k+1)(6p-6k+1)}
=\frac{1-64k^2}{1-36k^2}
\frac{1+8p/(1-8k)}{1+6p/(1-6k)}.
\]
Its first correction is exactly
\(8/(1-8k)-6/(1-6k)=2/((1-8k)(1-6k))\).
Multiply to obtain (R45-A). QED.

**Source exceptions.** The stated unit condition specifically excludes the \(6k\pm1\) and \(8k\pm1\) singular source weights. Preserve their R40 p-adic valuations and their individual source ports; do not silently cancel them into units.

## R45-B: a universal scalar-pair no-go from the two lowest ranks

For **every** \(p=6m+1\ge19\), \(k=1,2\) meet the hypotheses. Direct harmonic identities give
\[
\begin{array}{c|c|c|c}
k & H_{k-1}+4H_{4k-1}-2H_{2k-1}-3H_{3k-1}
 & \text{weight correction}&\text{total}\\
1&5/6&2/35&187/210\\
2&359/420&2/165&267/308
\end{array}
\]
and therefore
\[
\boxed{E_{p,1}\equiv\frac{27}{80}[1+p(Q_*+187/210)]\pmod{p^2},}
\]
\[
\boxed{E_{p,2}\equiv\frac{765}{2288}[1+p(Q_*+267/308)]\pmod{p^2}.}
\]
In particular,
\[
\boxed{ E_{p,1}-E_{p,2}\equiv
\frac{27}{80}-\frac{765}{2288}
=\frac9{2860}\ne0\pmod p . }\tag{R45-B}
\]
The denominator \(2860=2^2\cdot5\cdot11\cdot13\) is a \(p\)-adic unit throughout the theorem's domain. Thus, **even allowing a different scalar \(\lambda_p\) for each prime**, the pair constraints
\(E_{p,1}\equiv\lambda_p\equiv E_{p,2}\pmod p\)
are impossible. This rigorously excludes a **rank-independent reflected-pair scalar correction** for the unchanged weighted W/S sources, despite the constant unweighted R43 band factor. It does not exclude rank-dependent compensation, nonlocal additive WZ telescoping, or the original W/S sum congruence.

A stronger explicit second-digit difference follows algebraically:
\[
E_{p,1}-E_{p,2}\equiv
\frac9{2860}(1+pQ_*)+\frac{188343}{17617600}p\pmod{p^2}.
\]

## Exact author evidence

Companion stdlib script \`20261027_hourly_d25_reflected_weight_obstruction_r45_check.py\` was executed on 2026-10-27: all 78 primes \(19\le p\le997\), \(p\equiv1\pmod6\); 156 independent modular \(p^2\) reflected-pair checks, plus 8 extra raw-original-term \`Fraction\` checks for \(p=19,31,37,43\); all PASS. The checker reconstructs p-free factorial kernels and original W/S weight factors, rather than evaluating R45 from its RHS alone.

Exact examples \((p,E_{p,1}\bmod p^2,E_{p,2}\bmod p^2,(E_{p,1}-E_{p,2})\bmod p)\):
\((19,59,193,18)\), \((181,32474,25732,45)\), \((373,3735,107029,27)\).

BRC \`COMPOSE_APPLIED\`: ordered rank and reflected rank, W/S original provenance, separate linear-weight and kernel valuations, multiplicative observer and the still-required **additive** Green/WZ observer are retained as distinct fields. This arithmetic auxiliary one-index result is not promoted to an unproved six-dimensional native-coordinate theorem.

## Next smallest research unit and control boundary

Test a **source-labelled cross-rank additive WZ** candidate that retains the original W/S inputs. Use R45's compulsory rank dependence as a boundary condition, the R23 low-half \(p^2\)-divided discrepancy, R36 finite Green adjoint, and R38/R41/R42 high-rank/terminal ports. Begin with an explicitly solved two-rank coefficient ansatz or a concrete low-prime obstruction; preserve the isolated \(p=181\) S-tail zero and fixed \(z=2\) six-channel Hasse J/E \(3+2+1\) ports.

Separate parent acceptance obligations: original H0/B0, \([X]U\bmod p^2\), semilinear Frobenius \(\eta/\kappa\), native \(p=373\), independent Driver review. Native predecessor/claim support remains tracked under existing issue #1558. No new role-bound control mutation is asserted in this portable result.
