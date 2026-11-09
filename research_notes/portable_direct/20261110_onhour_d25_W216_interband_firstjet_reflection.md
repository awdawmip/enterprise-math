# D25 / Original W216: fourth-digit first-jet reflection across grades 1 and 2

Date: 2026-11-10 (+08:00). Status: AUTHOR_SIDE_EXACT_ALGEBRAIC_PROOF / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_PENDING.
Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3; research lane chatgpt-research-onhour-enterprise-math-20260923.

## Theorem (genuine mod-p² first jet, all primes p=6m+1>3)

Keep the original $A_k=(2k)!(3k)!/((k!)^5 216^k)$, original weight $6k+1$, and the same index involution $k\mapsto p-k$ proved in the preceding author-side reflection note (20261110_onhour_d25_W216_interband_reflection_reciprocity.md).

Set $k_0=2m+1$, $k_j=k_0+j$ for $0\le j<m$, and in $\mathbb Z/p^2\mathbb Z$ define the p-integral units
$$
L_j=\frac{A_{k_j}}p,\qquad
H_j=\frac{A_{p-k_j}}{p^2},\qquad
C_p=L_0H_0.
$$
Division occurs in $\mathbb Z_{(p)}$ before reduction. Each $L_j,H_j$ is a unit, so inverses below exist. Define in $\mathbb F_p$
$$
e_j=-\frac3{k_j}+\frac2{2k_j+1}+
\frac3{3k_j+1}+\frac3{3k_j+2},
\quad E_0=0,\quad E_j=\sum_{r=0}^{j-1}e_r.
$$
The denominators in $e_r$ are units for $0\le r<m-1$; $E_j$ only uses such $r$.

**Reflection-first-jet theorem:**
$$
\boxed{L_j H_j\equiv C_p\left(\frac{k_0}{k_j}\right)^3(1+pE_j)\pmod{p^2}.}\tag{J1}
$$
In particular, the entire fourth-digit grade-two observer is reconstructed from the existing grade-one first-jet sequence plus a *single* seed:
$$
\boxed{
\frac{W_{2,p}}{p^2}\equiv
C_p\sum_{j=0}^{m-1}(6(p-k_j)+1)
\left(\frac{k_0}{k_j}\right)^3
(1+pE_j)L_j^{-1}\pmod{p^2}.
}\tag{J2}
$$
The $6p$ weight correction, full original index and signed terms are explicitly retained. This is at the accuracy needed for a modulo-$p^4$ signed AF4 layer, beyond the preceding modulo-$p$ reciprocity.

## Proof

The exact original recurrence is
$$
R(k)=\frac{A_{k+1}}{A_k}=
\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
$$
For each interior $k=k_j$ with $0\le j<m-1$, the corresponding reverse ratio is
$$
\frac{A_{p-k-1}}{A_{p-k}}=
\frac{36(p-k)^3}{(2p-2k-1)(3p-3k-2)(3p-3k-1)}.
$$
The p-adic first-order expansions, with all original signs, are
$$
(p-k)^3=(-k)^3(1-3p/k)+O(p^2)
$$
and
$$
\prod(2p-2k-1,3p-3k-2,3p-3k-1)
=-(2k+1)(3k+2)(3k+1)
\left[1-p\left(\frac2{2k+1}+\frac3{3k+2}+\frac3{3k+1}\right)\right]
+O(p^2).
$$
Consequently, with $B_k=(A_k/p)(A_{p-k}/p^2)$,
$$
\frac{B_{k+1}}{B_k}\equiv
\left(\frac{k}{k+1}\right)^3
\left[1+p\left(-\frac3k+\frac2{2k+1}+\frac3{3k+1}+\frac3{3k+2}\right)\right]
\pmod{p^2}.
$$
Iterate from $k_0$ without stepping outside the grade-one/grade-two bijection. The first-order product is $1+pE_j$, proving (J1). Since $L_j$ is a p-unit, solve for $H_j$ and sum with the **original** weight $6(p-k_j)+1$; this proves (J2). Reducing (J1) modulo $p$ recovers the preceding exact theorem $L_jH_j=(36k_j^3)^{-1}$ because $C_p\bmod p=3/32$ and $k_0\bmod p=2/3$.

## Reuse, scope and numerical meaning

The prior grade-one terminating first jet supplies $L_j\bmod p^2$ (seed $u_0$, $g_j$ and harmonic correction $S_j$). The prior grade-two first jet supplies an independent $H_j\bmod p^2$ validation, while (J2) computes it alternatively from $L_j,C_p,E_j$. BRC resolution: COMPOSE_APPLIED. Exact paired carrier retains both original indices, grades 1/2, signed weights, units, first jets and $E_j$ repair coordinate. The reduction is lossless for the **declared** original $W_{2,p}/p^2\bmod p^2$ observer; it does not erase lower grade/cross-grade carry, 2304 signed terms, or native Frobenius and $\kappa$.

Standard-library integer modular recurrence checked (J1) and (J2) for every one of the 148 primes $p\le2000$, $p\equiv1\bmod6$, covering 22,952 paired coefficients. Independent original integer binomial computation modulo $p^4$ cross-checked all paired indices at $p=7,13,19,373$ (136 coefficient evaluations).

Selected exact $(C_p,W_{2,p}/p^2)\bmod p^2$: $p=13:(137,75)$, $p=19:(85,161)$, $p=373:(12041,68898)$, $p=997:(566078,374899)$. The $p=373$ second-layer readout agrees with the existing grade-two first-jet certificate, independently obtained by a forward recurrence.

## Scientific continuation

The mother target remains original $\Delta_p-R_p\bmod p$ in both $p\equiv13,19\bmod24$ classes. Next exact operation: insert the new one-seed grade-two first-jet port into the already completed grade-zero second jet and grade-one first jet; seek a signed finite WZ/Jacobi telescoper at mod-$p^3$ for W216 and the original 216/2304 AF4 at mod-$p^4$, respecting carry and cutoff. Original p373 native H0/B0 fixed-class divided-power $[X]U\bmod139129$, rank, semilinear direction/eta, signed odd observer, $\kappa$ and independent reproduction remain NOT_RUN / PENDING_OWNER, tracked at Issue #1559.

Native Source continuation read: onhour11-20261110-0705-current-continuation SUCCEEDED. Current Research lane has no own authenticated session capability, winning CLAIM or open run; this artifact is author-side and is not a canonical native checkpoint/Result.
