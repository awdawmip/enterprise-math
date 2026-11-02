# D25 — Ordinary Gauss second jet and one-index Clausen residual (2026-11-02)

**Evidence state:** AUTHOR-DERIVED / EXACT ALGEBRAIC DERIVATION / FINITE INTEGER REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Research provenance only: not a Source checkpoint, native H0/B0 computation, new CLAIM or formally accepted Result.

**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, immutable publication TP2-B6F4FC938FF94941C1B7. Frozen source input is verified immutable full commit c47e13e4aba0e006366f989d6334d443f6333ae3, consistent with truncated prior author shorthand c47e13e4aba0e006366f989d6333ae3; no input rebase. Research logical conversation chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance chatgpt-hourly-enterprise-math-20260921.

## Theorem: ordinary second jet and exact LIFT reduction

For every prime p=6m+1>=7, put z0=1/2 and theta=z*d/dz. Define
\[
P_0(z)=\sum_{r=0}^m\binom mr\binom{2m}r z^r,\quad
C(z)=\sum_{r=0}^m\binom mr\binom{2m}r H_rz^r,\quad
D_2(z)=\sum_{r=0}^m\binom mr\binom{2m}r(H_r^2+H_r^{(2)})z^r.
\]
Let P(z)={}_2F_1(-m,-2m;1-p/2;z) be the terminating deformed Gauss polynomial. Since all j<=m are p-units, the exact finite denominator expansion
\[
\frac{r!}{(1-p/2)_r}=\prod_{j=1}^r(1-p/(2j))^{-1}
\equiv1+(p/2)H_r+(p^2/8)(H_r^2+H_r^{(2)})\pmod{p^3}
\]
proves, coefficientwise for all p=1(mod6),
\[
\boxed{P=P_0+\frac p2 C+\frac{p^2}8D_2\pmod{p^3}.}\tag{1}
\]
For CM target primes p≡13 or 19 (mod24), reuse accepted CM0: P0(z0)≡0 (modp). Put
\[
A=P_0(z_0)/p+C(z_0)/2,\quad J=(\theta P_0)(z_0),\quad C_\theta=(\theta C)(z_0),\quad D_{2,0}=D_2(z_0).
\]
Then P(z0)=pA+p²D₂,₀/8 (modp³) and P'(z0)=2J+pCθ+O(p²), whence
\[
\boxed{P(z_0)(P(z_0)+6P'(z_0))\equiv
12pJA+p^2(A^2+6AC_\theta+\tfrac32 JD_{2,0})\pmod{p^3}.}\tag{2}
\]
Here P' is ordinary derivative. The D2 derivative drops only from the specified scalar modp³ because it is multiplied by p³; its source remains explicit in (1).

Consume the predecessor's exact terminating Clausen gauge and original three-root decomposition:
\[
A_0\equiv P(P+6P')-\tfrac{3p}{2}\mathcal H_1+\tfrac{p^2}{8}\mathcal H_2\pmod{p^3},\quad
W_{p-1}\equiv A_0+p(A_1+B_1)+p^2(A_2+B_2+C_2)\pmod{p^3}.
\]
All A_i,B_i,C_2,Hcal_i retain their prior signed cutoff-sensitive definitions. Set
\[
N=12JA-\tfrac32\mathcal H_1+A_1+B_1-1.
\]
The inherited D24 first-digit result yields N≡0(mod p). Using the previously established same-original-observer bridge \(\Delta_p-R_p\equiv(W_{p-1}-p)/p^2\pmod p\), obtain the new **strict exact reduction**
\[
\boxed{\Delta_p-R_p\equiv
\frac Np+A^2+6AC_\theta+\tfrac32JD_{2,0}
+\frac{\mathcal H_2}{8}+A_2+B_2+C_2\pmod p.}\tag{3}
\]
The proof is the coefficientwise product calculation, followed by the previously established exact frozen-observer bridge. Equation (3) is an equivalent certificate, not a uniform all-target vanishing theorem.

## One-index terminating Clausen harmonic evaluator / BRC observer

Let \(Q_k=2^{-k}[z^k]P(z)^2\), for 0<=k<=2m. The predecessor's terminating Clausen identity gives
\[
\boxed{Q_0=1,\quad Q_{k+1}=Q_k
\frac{(k-2m)(k-3m)(k-4m)}
{(2k+2-p)(k+1-p)(k+1)}}\quad(0\le k<2m).
\]
Every denominator is a p-unit. Therefore
\[
\mathcal H_1=\sum_{k=0}^{2m}(6k+1)Q_kH_k,\quad
\mathcal H_2=\sum_{k=0}^{2m}(6k+1)Q_k(9H_k^2-5H_k^{(2)}).
\]
These exact signed scalar observers are computable in O(p) modular operations rather than O(p²) raw ordered-pair Cauchy convolution. This is scoped to the weighted scalar, finite Euler operators and divided second-digit observation. The earlier ordered-pair signed BRC repair Xi_p is retained when pair-sensitive future operations demand it. No assertion of complete pair-observer redundancy or input-bit-complexity improvement. BRC reuse: COMPOSE_APPLIED.

## Executed exact finite regression

Actual standard-library modular checker ran on all 207 primes p<=3000 with p≡1(mod6), including all 107 target primes, checking (1) with Euler derivative, original Clausen gauge, generic square expansion, 3-root original source, and CM-only (2) and (3); zero mismatches. Independent original weighted W216 p³ sum was computed at p=13,19,37,373,1171 and agreed with 3-root source. Non-CM p7 was checked at the un-divided generic stage.

At p=373, the four source groups of (3) are
\[
\boxed{(N/p,\ A^2+6AC_\theta+\tfrac32JD_{2,0},\ \mathcal H_2/8,\ A_2+B_2+C_2)
=(53,194,366,133),\quad 53+194+366+133=746=2p.}
\]
Residues: A=314, P0/p=340, J=294, C=321, Ctheta=365, D2=102, Hcal1=346, Hcal2=317; (A2,B2,C2)=(82,158,266). At p=13 the four ports are (5,3,8,10); p=19 (8,16,6,8). These finite zeroes do not establish the uniform LIFT theorem.

## Highest frontier and next precise action

Mother goal: prove/refute original Delta_p=R_p mod p for every p≡13,19 mod24 under frozen scalar interface. New frontier (3): ordinary second jet + signed Clausen and 3-band boundary ports. Next: derive a finite contiguous/WZ telescope for the whole signed right-hand side, particularly divided N/p with Hcal2 and boundary bands, preserving Xi_p for pair-sensitive operations; test on 13,19,373 and non-CM 7. No new axioms or task rerouting.

Separate original p=373 native H0/B0 divided-power [X]U mod139129, true module rank, genuine semilinear Frobenius, normalization and independent replication remain pending under Enterprise Math issue #1559; scalar proof is not that experiment. Historical original Research dispatch research-onhour-20261031-0205-dispatch-r15 at kimi-query-bridge#6633 terminated FAILED/UPSTREAM_CODE_REVIEW_REQUIRED; not reissued. No authenticated current own Source session, claim, run or publish_checkpoint was obtained in this work. Previous gateway read-only evidence reported Research write authorization absent; no identity borrowing or bypass. Evidence is author-side and not admitted.
