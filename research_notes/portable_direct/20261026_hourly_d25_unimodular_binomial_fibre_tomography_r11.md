# D25/LIFT — Adaptive unimodular binomial-fibre tomography beyond quadratic Hasse moments

Date: 2026-10-26. TASK_RESEARCH: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** External finite algebra, not original-class CM computation, canonical checkpoint, Result or all-prime LIFT proof.

## Consumed source and new problem

Consume (do not re-credit) the three-channel p^4 source and the previously proved Pascal high-polar inverse in research_notes/portable_direct/20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md, commit a4483dc0fb56e7b29f8f85b131e28f08a65ba589. Previous high-polar reconstruction covered only moments of powers j^s, s=0,1,2. The exact corrected rank/Hasse recurrence (research_notes/portable_direct/20261025_hourly_d25_clausen_operator_rank_boundary.md) contains a quadratic shifted rank factor. This note proves (a) an integer-unimodular, complete labelled-cell recovery, and (b) a sharp obstruction to retaining only moments of degree <=2 after two quadratic rank actions. The new proof is independent of the missing original-class crystalline bridge.

Let m>=1, M=2m, N=2M-1. Let R be any commutative unital ring and let w_{j,ell} in R be arbitrary **signed labelled** cells, 1<=j,ell<=M. On oriented diagonal n=ell-j (1-M<=n<=M-1) set
\[
j_{\min}=\max(1,1-n),\qquad j_{\max}=\min(M,M-n),\qquad
d_n=M-|n|,\quad a_n=j_{\min}-1.
\]
These are d_n consecutive legal j-ranks. In the corrected Clausen three-channel application the cells are w^{ab}_{j,ell}=u_{a,j}u_{b,p-ell}, p=6m+1, (a,b)=(0,2),(1,2),(0,3). Assertions about arbitrary signed cells do NOT imply arbitrary perturbations within this constrained hypergeometric family.

## Theorem A — adaptive unimodular diagonal reconstruction

On diagonal n retain exactly d_n binomial moments:
\[
\boxed{B_{n,s}=\sum_{j=j_{\min}}^{j_{\max}}\binom{j-1}{s}w_{j,j+n},\qquad0\le s<d_n.}\tag{A1}
\]
Writing w_r=w_{j_min+r,j_min+r+n} (0<=r<d_n), define
\[
C_{n,k}=\sum_{h=0}^{k}\binom{-a_n}{h}B_{n,k-h},\quad
\boxed{w_r=\sum_{s=r}^{d_n-1}(-1)^{s-r}\binom{s}{r}C_{n,s}.}\tag{A2}
\]
Every coefficient in this inverse is an integer. The d_n-by-d_n matrix [binom(a_n+r,s)]_{s,r=0,...,d_n-1} has determinant +1, so (A1)-(A2) is valid over EVERY commutative unital ring, including rings of characteristic p and nonfields. It captures the full labelled array using
\[
\sum_{n=1-M}^{M-1}d_n=M^2
\]
moments, with no prime-dependent solving or division.

Proof. Define P_n(y)=sum_{r=0}^{d_n-1}w_r(1+y)^{a_n+r}. Its first d_n coefficients are precisely B_{n,s}. Divide formally by (1+y)^{a_n} mod y^{d_n}. The resulting polynomial is sum_r w_r(1+y)^r and has coefficient C_{n,k}=sum_{r>=k}binom(r,k)w_r. Binomial inversion yields (A2). The centering transform (multiplication by (1+y)^{-a_n}) and the latter binomial transform are triangular with diagonal 1, so the determinant is +1. The diagonal lengths sum to M². QED.

## Theorem B — compatible complete critical-polar interface

Now suppose 2 is invertible in R (for example R=Z_(p)/p^r for p=6m+1>=7). Reuse the existing finite corrected-Clausen factors
\[
F_a(z)=\sum_{j=1}^M2^{-j}u_{a,j}z^{-j},\qquad
G_b(z)=\sum_{\ell=1}^M2^\ell u_{b,p-\ell}z^\ell,\quad
\theta=z\,d/dz.
\]
There is one uniform binomial insertion, independent of n:
\[
F_{a,s}(z)=\binom{-\theta-1}{s}F_a(z)
=\sum_j\binom{j-1}{s}2^{-j}u_{a,j}z^{-j}.
\]
Consequently [z^n](F_{a,s}G_b)=2^nB^{ab}_{n,s}. Define the scaled critical-polar transfer
\[
\mathcal P^{ab}_s(z)=\frac{z^{2M}}{(1-2z)^{2M}}F_{a,s}(z)G_b(z),\qquad y=1-2z.
\]
The following is an EXACT FINITE POLYNOMIAL IDENTITY:
\[
\boxed{2^{2M}y^{2M}\mathcal P_s^{ab}((1-y)/2)
=\sum_{r=0}^{N-1}B^{ab}_{n_r,s}(1-y)^{M+1+r},\quad n_r=1-M+r.}\tag{B1}
\]
The N scaled Laurent high-pole coefficients (from y^{-2M} through y^{-2}) are
\[
\beta_{s,k}=(-1)^k\sum_{r=0}^{N-1}\binom{M+1+r}{k}B_{n_r,s},
\qquad0\le k<N.
\]
The previously established integer Pascal inverse applies exactly:
\[
D_{s,k}=\sum_{h=0}^k\binom{M+h}{h}\beta_{s,k-h},\qquad
\boxed{B_{n_r,s}=(-1)^r\sum_{k=r}^{N-1}\binom{k}{r}D_{s,k}.}\tag{B2}
\]
Compute s=0,...,M-1, recover the B values by (B2), retain only the adaptive s<d_n for each n, then apply (A2). This yields an explicit ring-valid left inverse of the entire M-by-M labelled-source array (over any 2-invertible ring). The high-polar inversion in (B2) is **reused prior work**; the new result is its compatibility with binomial insertion and the sharp full-cell recovery.

Proof. Each source cell of difference n contributes binom(j-1,s) 2^n w_{j,ell}z^{2M+n} to z^{2M}F_{a,s}G_b. Substituting z=(1-y)/2 cancels the factor 2^n to the common 2^{-2M}, proving (B1). Taking its N lowest Taylor coefficients and dividing by (1-y)^{M+1} gives the previous triangular Pascal inversion (B2). Apply A. QED.

This **retains** both orientations of the signed Clausen tail, original rank labels, finite cutoff and infinity port; it does not assert their cancellation, a new WZ telescoper, or Delta_p-R_p=0.

## Theorem C — a second quadratic action escapes the three-moment observer

For m>=2 take four diagonal cells (j,ell)=(1,1),(2,2),(3,3),(4,4) with signed perturbation delta=(1,-3,3,-1). It satisfies
\[
\boxed{\sum_{j=1}^4\delta_jj^s=0\quad(s=0,1,2).}\tag{C1}
\]
For the actual shifted quadratic rank polynomial Q_m(j)=(j-1-m)(j-1-2m), however,
\[
\boxed{\sum_{j=1}^4\delta_j Q_m(j)^2=36(m-1).}\tag{C2}
\]
For **every target prime** p=6m+1>=13 this is a nonzero p-unit: gcd(p,36)=1 and 0<m-1<p. At m=2,p=13 the gap is 36=10 mod13. The omitted binomial moment B_{0,3} changes by -1.

Proof. The delta pattern is the negative third forward difference, annihilating polynomials of degree <=2. Expand Q_m(j)=j²-(3m+2)j+(m+1)(2m+1). Only the top j⁴ and j³ terms of Q_m² survive. Their delta-weighted sums are -60 and -6, respectively; therefore (C2) equals -60+12(3m+2)=36(m-1). The final binomial basis coordinate detects the fourth cell. QED.

Thus degree 0/1/2 source moments suffice for a single quadratic multiplication but **cannot be assumed closed after two** on an unrestricted signed array. This does not claim the corrected hypergeometric sequence admits the synthetic perturbation, nor that the actual differential operator acts as pure multiplication by Q_m twice. It supplies a precise compression-failure certificate for proposed general-purpose rankwise coupling.

## Exact author check, BRC and next action

The adjacent stdlib checker verifies 33 deterministic signed integer arrays (m=1..11, three arrays per m) by reconstructing every cell through the independent high-polar and adaptive inverse; independently recomputes the selected diagonal moments; verifies the third finite-difference witness for m=2..29 and its nonvanishing modulo the 27 target primes 13<=p<300. **6,127 exact counted assertions passed.** Finite checks are not an independent proof or mathematical admission.

BRC **COMPOSE_APPLIED**: the typed carrier keeps (j,ell,n), signs, Hasse channel, p-local precision and future rank actions. The old low-degree observer loses the signed fibre contrast (C2); the new adaptive binomial observer is fully reversible under an integer unimodular transform. z is an external auxiliary Laurent variable, not native six-dimensional Enterprise geometry. P000 remains fixed.

**Next exact research unit:** use the complete labelled carrier to derive a genuinely coupled corrected-Clausen WZ/adjoint identity reducing the adaptive binomial observations *for the constrained hypergeometric source* while retaining both boundaries, signs and oriented infinity port. An actual factorization/closure proof is required before discarding higher ranks. The D25/LIFT/JT2 mother objective remains OPEN: authenticated original-class H0/B0 and divided-power [X]U mod p², native Frobenius direction/normalization eta, kappa/Delta_p-R_p comparison and independent review remain absent. Native CM experiment NOT_RUN.

Research logical conversation chatgpt-research-hourly-enterprise-math-20260923 is separate from CONTROL_PLANE_MAINTENANCE. Latest exact Source continuation read is HANDOFF_READY/NEEDS_DISPATCH with a preserved SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED checkpoint, execution_authorized=false and last historical CLAIM MCP-d0d70cd041b01e5db192870a different from checkpoint claimant MCP-87631b892b41fa18d799f2d8. Issue #1558 owns that unresolved control repair. No new CLAIM, OPEN, Source checkpoint, Result or review is claimed here.
