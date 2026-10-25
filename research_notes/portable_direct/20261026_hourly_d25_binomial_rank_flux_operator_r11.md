# D25/LIFT — Exact quadratic rank action and two oriented finite-boundary flux laws in the unimodular binomial observer

2026-10-26. TASK_RESEARCH, Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Exact finite algebra; no original-class CM evidence, native checkpoint, complete WZ telescoper or all-prime D25/LIFT proof.

## Prior theorem consumed, not re-credited

The new preceding adaptive integer-unimodular binomial-fibre tomography (commit \`4054b7038fa149bd116f741ac1039ebd66134a2a\`, \`research_notes/portable_direct/20261026_hourly_d25_unimodular_binomial_fibre_tomography_r11.md\`) reconstructs every signed labelled cell from diagonal binomial moments. The previously proven exact corrected-Clausen rank/Hasse recurrence includes the quadratic factor \`(r-1-m)(r-1-2m)\` and nearest-rank shifts. Transport these operators with finite boundaries; no imaginary cancellation.

Fix integer \(m\ge1\), \(M=2m\), any signed array \(w_{j,\ell}\) in a commutative unital ring \(R\), \(1\le j,\ell\le M\). The *oriented* fibre index is \(n=\ell-j\). Define
\[
\mathsf B_{n,s}(w)=\sum_{1\le j,j+n\le M}\binom{j-1}{s}w_{j,j+n},\quad s\ge0,
\]
with binomial coefficients zero for \(s<0\). Missing fibres have zero moment. Moment values \(s\ge d_n=M-|n|\) are **derived** from the preceding unimodular inverse and are not independent input.

## Theorem A — exact corrected quadratic rank operator

For \(Q_m(j)=(j-1-m)(j-1-2m)\), \((Q_mw)_{j,\ell}=Q_m(j)w_{j,\ell}\),
\[
\boxed{\mathsf B_{n,s}(Q_mw)=
(s-m)(s-2m)\mathsf B_{n,s}(w)
+(s+1)(2s+1-3m)\mathsf B_{n,s+1}(w)
+(s+1)(s+2)\mathsf B_{n,s+2}(w).}\tag{A}
\]
This identity is over \(\mathbb Z\), hence over every base ring, including \(\mathbb Z/p^k\mathbb Z\). Retain the high moments by reconstruction; merely retaining \(s=0,1,2\) without source recovery is not compositionally closed, as the first unit's nonzero four-cell \(36(m-1)\) witness shows.

**Proof:** Put \(x=j-1\), so \(Q=x^2-3mx+2m^2\). The binomial basis obeys
\[
x\binom{x}s=s\binom{x}s+(s+1)\binom{x}{s+1},\quad
x^2\binom{x}s=s^2\binom{x}s+(s+1)(2s+1)\binom{x}{s+1}
 +(s+1)(s+2)\binom{x}{s+2}.
\]
Substitute and sum over the signed labelled fibre. \(\square\)

## Theorem B — first-rank shift with terminal source

Define the zero-extended first-rank shift
\[
(\mathsf S_jw)_{j,\ell}=w_{j-1,\ell}\ (2\le j\le M),\quad
(\mathsf S_jw)_{1,\ell}=0.
\]
For each legal original \(1-M\le n\le M-1\), \(s\ge0\),
\[
\boxed{\mathsf B_{n-1,s}(\mathsf S_jw)=
\mathsf B_{n,s}(w)+\mathsf B_{n,s-1}(w)
-\mathbf1_{n\le0}\binom M s w_{M,M+n}.}\tag{B}
\]
**Proof:** A surviving cell \((j,\ell)\) maps to \((j+1,\ell)\), changing \(n\to n-1\); the new coefficient is \(\binom j s=\binom{j-1}s+\binom{j-1}{s-1}\). The only deleted cell is old \(j=M\), present on the fibre exactly for \(n\le0\); its new binomial weight would have been \(\binom M s\). Extreme output fibre \(n=-M\) is empty on both sides. \(\square\)

## Theorem C — second-rank shift with independent terminal source

Define the zero-extended second-rank shift
\[
(\mathsf S_\ell w)_{j,\ell}=w_{j,\ell-1}\ (2\le\ell\le M),\quad
(\mathsf S_\ell w)_{j,1}=0.
\]
Then
\[
\boxed{\mathsf B_{n+1,s}(\mathsf S_\ell w)=
\mathsf B_{n,s}(w)
-\mathbf1_{n\ge0}\binom{M-n-1}s w_{M-n,M}.}\tag{C}
\]
**Proof:** A surviving source cell keeps \(j\) and its binomial factor, and \(n\to n+1\). The only deletion is the old \(\ell=M\) cell, present for \(n\ge0\) at \(j=M-n\). Its old weight was \(\binom{M-n-1}s\). \(\square\)

## Scope, exact author test, information budget

The unitriangular reconstruction in the preceding work is a ring-module isomorphism, so (A)–(C) and any finite compositions of these signed finite rank actions are representable by the adaptive \(M^2\)-coordinate observer **when all resulting high moments and terminal labels are reconstructed**. This is a losslessness certificate, not a dimension reduction, WZ cancellation, or terminal boundary vanishing proof.

A companion Python-stdlib checker (independent array actions vs displayed binomial recurrences) ran **50,796 exact integer assertions, all PASS**: m=1,...,12, three seeded signed arrays for each, every original legal orientation n and s=0,...,M+1. This is an AUTHOR check only, not native CM experiment or independent review.

**BRC COMPOSE_APPLIED:** retain \((j,\ell,n)\) branch labels, Hasse channel, signed coefficient and p-local valuation when specializing; distinguish the two lost edge ports (\(j=M\), \(\ell=M\)), their opposing orientations, and scalar vs quadratic observable. The auxiliary Laurent parameter \(z\) is not native P000 X6 geometry. P000 remains unchanged.

**Next exact scientific unit:** insert the complete corrected-Clausen rank/Hasse recurrence with its \(k\to k-1\) and \(k\to k-2\) jet couplings into this finite-boundary operator interface and seek a *genuine* coupled source-faithful WZ/adjoint cancellation in the constrained hypergeometric source. The parent D25/LIFT/JT2 remains OPEN: authenticated original-class H0/B0, \([X]U\bmod p^2\), native Frobenius direction/eta, kappa and Delta_p-R_p bridge and independent review remain missing; native CM NOT_RUN.

Research logical conversation: \`chatgpt-research-hourly-enterprise-math-20260923\` (separate from maintenance). At latest fresh read, D25 Source checkpoint is SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED but Research execution_authorized=false; latest historical CLAIM \`MCP-d0d70cd041b01e5db192870a\` conflicts with expected predecessor claimant \`MCP-87631b892b41fa18d799f2d8\`. Issue #1558 owns repair. This is portable work, **not** an authorized native Source publish/Result/Review.
