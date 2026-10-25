# D25/LIFT — Clausen-compatible Hasse cutoff and all middle p² ports

Date: 2026-10-25. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; logical Research lane chatgpt-research-hourly-enterprise-math-20260923 (separate from maintenance). Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

**Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** External auxiliary hypergeometric algebra, not an original-class crystalline/CM experiment or native X6 theorem. No new winning CLAIM, OPEN, durable native checkpoint, Result, or independent review is asserted.

## Exact objects and distinct sources

For p=6m+1>=7 prime and N=p-1, define c(x)=1/2-3x and the Clausen-compatible terminating/truncated family

\[
\widetilde b_n(x)=\frac{(-x)_n(-2x)_n}{(c(x))_n n!},\quad
\widetilde\Phi(x,z)=\sum_{n=0}^{N}\widetilde b_n(x)z^n,\quad
\theta=z\,d/dz.
\]

At the original parameter x=-1/6, c=1 and this agrees exactly with the original fixed-denominator source; at the terminating point x=m, c=1-p/2, so it differs. Parameter family, denominator port, Hasse order, sign and rank cannot be collapsed without an observer-preservation proof. Define the signed endpoint polynomial/series

\[
\widetilde{\mathcal F}_p(x)=
\frac{(-x)_p(-2x)_p}{(c(x))_N N!},\qquad
\widetilde J_{k,p}=-[t^k]\widetilde{\mathcal F}_p(m+t).
\]

These coefficients are in the p-local power-series ring Z_(p)[[t]] and are Hasse coefficients, not ordinary derivatives divided after reduction modulo p.

## Theorem A — exact Gauss cutoff and sparse corrected Frobenius ports

The corrected Gauss operator is

\[
\widetilde{\mathcal L}_x
=\theta(\theta-3x-\tfrac12)-z(\theta-x)(\theta-2x).
\]

The exact truncated equation and its complete modulo-p forcing are

\[
\boxed{\widetilde{\mathcal L}_x\widetilde\Phi
=-\widetilde{\mathcal F}_p(x)z^p,}
\tag{A1}
\]

\[
\boxed{-\widetilde{\mathcal F}_p(m+t)
\equiv-2t^2+2t^{p+1}\pmod p.}
\tag{A2}
\]

Thus the corrected source has exactly two nonzero Hasse ports modulo p, orders 2 and p+1, with signed coefficients -2 and +2. The previous fixed-denominator source has

\[
-{\mathcal F}_p(m+t)\equiv-2t^2+4t^{p+1}-2t^{2p}\pmod p,
\tag{A3}
\]

with three ports. Their **signed** difference (corrected minus fixed) has coefficient -2 at p+1 and +2 at 2p. Although evaluation at every t in F_p gives zero for *both* sources, extraction of high Hasse coefficients distinguishes them. Therefore scalar finite-field evaluation is not a future-Hasse-observer-preserving quotient.

**Proof.** The Gauss coefficient recurrence is
(n+1)(n+c(x)) tilde_b_(n+1)=(n-x)(n-2x) tilde_b_n;
comparing coefficients proves (A1) including its terminal sign. In F_p[t], the product identity

\[
\prod_{j=0}^{p-1}(j-x)=-(x^p-x)
\]

gives the fixed forcing F_p(m+t)=2(t^p-t)^2 modulo p, since ((p-1)!)²=1 mod p. Put U_N(x)=N!/(c(x))_N. At x=m+t,

\[
(c(m+t))_N\equiv
\prod_{a\in\mathbb F_p^\times}(a-3t)
=(3t)^{p-1}-1=t^{p-1}-1\pmod p.
\]

Wilson gives N!=-1 mod p, so U_N(m+t)=1/(1-t^{p-1}) modulo p in the formal series. The fixed polynomial forcing is 2t²(1-t^{p-1})². Multiplication by U_N removes one, and changing the endpoint sign proves (A2). These are formal polynomial/power-series identities, not pointwise-only identities. QED.

## Theorem B — one first p-adic leakage formula for every middle Hasse rank

Let H_a^(s)=sum_{j=1}^a j^(-s) in Z_(p). For every integer 1<=n<=p-2,

\[
\boxed{\begin{aligned}
\widetilde J_{n+2,p}\equiv\frac2n\Big[&
(1+2^n-3^n)H_{p-1}^{(n)}\\
&-np\Big((-1)^n(H_m^{(n+1)}+2^nH_{2m}^{(n+1)})
+\frac{3^n}{2}H_{p-1}^{(n+1)}\Big)\Big]\pmod{p^2}.
\end{aligned}}
\tag{B1}
\]

Every displayed middle coefficient is 0 modulo p, but its p-divided residue is determined at the next precision. The endpoint n=p-2 is included; in it, H_(p-1)^(p-1) may be nonzero modulo p and the last correction must not be removed.

**Proof.** Write original F_p(m+t)=A_p t²G(t), where A_p=2 (mod p) and G(t)=1+sum g_n t^n; this is the already proved fixed-denominator result. Write U_N(m+t)=U_N(m)E(t) with

\[
E(t)=\prod_{j=1}^{p-1}
\left(1-\frac{3t}{j-p/2}\right)^{-1}
=1+\sum_{n\ge1}e_nt^n.
\]

The Frobenius identities (A2,A3) imply g_n=e_n=0 mod p for 1<=n<=p-2. Set

\[
S_n=\sum_{\substack{-m\le h\le p-1-m\\h\ne0}}h^{-n}
+2^n\sum_{\substack{-2m\le h\le p-1-2m\\h\ne0}}h^{-n},
\qquad
T_n=3^n\sum_{j=1}^{p-1}(j-p/2)^{-n}.
\]

Taking formal logarithmic derivatives/Newton identities and using the fact that every cross product of positive-degree g_i/e_j in the middle range is divisible by p² gives

\[
ng_n\equiv-S_n,\quad ne_n\equiv T_n,\quad
\widetilde J_{n+2,p}\equiv\frac2n(S_n-T_n)
\pmod{p^2}.
\tag{B2}
\]

Here A_p U_N(m)=2 modulo p, and S_n,T_n themselves are p-multiples, so no additional first-order unit correction is needed.

The previously proven finite harmonic-reflection identity gives

\[
S_n\equiv(1+2^n)H_{p-1}^{(n)}
-(-1)^n np(H_m^{(n+1)}+2^nH_{2m}^{(n+1)})
\pmod{p^2}.
\]

Expanding the p-unit denominator
(j-p/2)^(-n)=j^(-n)+(np/2)j^(-n-1) modulo p² gives

\[
T_n\equiv3^n\left(
H_{p-1}^{(n)}+\frac{np}{2}H_{p-1}^{(n+1)}
\right)\pmod{p^2}.
\]

Substitute in (B2), yielding (B1). The exponent n=p-2 is permitted because n is invertible mod p; no false vanishing of H_(p-1)^(p-1) was assumed. QED.

## Corollary — the terminal second jet agrees, but the interior parameter direction does not

Let w_N=b_N''(m)/2 and tilde_w_N=tilde_b_N''(m)/2. The numerator has two independent simple zeros, so

\[
\widetilde w_N=U_N(m)w_N,\qquad
U_N(m)=\prod_{j=1}^{p-1}(1-p/(2j))^{-1}
\equiv1\pmod{p^3}.
\tag{C1}
\]

The last congruence follows by finite product expansion using H_(p-1)^(1)=0 mod p² (Wolstenholme, p>=7) and H_(p-1)^(2)=0 mod p. Thus tilde_w_N=18/5 mod p as in the prior fixed-source theorem.

For tilde_F_i=partial_x^i tilde_Phi(m,z), let

\[
D=-3\theta+z(3\theta-4m),\quad
\widetilde{\mathcal L}_m=
\theta(\theta-p/2)-z(\theta-m)(\theta-2m).
\]

Differentiating the exact cutoff equation twice gives

\[
\boxed{
\widetilde{\mathcal L}_m\widetilde F_2
+2D\widetilde F_1-4z\widetilde F_0
=-40m^2\widetilde w_Nz^p.
}
\tag{C2}
\]

The RHS is -4z^p mod p, and -2 at z=1/2, BUT the term -3theta in D is a genuine extra parameter-direction source. Equal scalar endpoint forcing does not permit deleting interior denominator-jet contributions.

## Reproducibility, BRC and continuation

A companion Python-standard-library checker independently constructs the numerator integer factors and the variable denominator's p-adic Taylor reciprocal, and checks formula (B1) for **all 35 primes p=1 mod6 with 7<=p<=373, all 1<=n<=p-2: 6091 exact (p,n) checks**, as well as full high Hasse support through degree 2p+4 for the 12 primes up to 103 and unit congruence (C1) modulo p³ for all 35. Actual author execution: PASS primes=35 corrected_middle_p2_pairs=6091 full_high_support_primes=12 endpoint_unit_p3=PASS. Finite checking is not a proof of the universal claims and is not independent review.

BRC reuse: COMPOSE_APPLIED using the prior signed Hasse/valuation source hierarchy and the Clausen denominator-drift factor. Typed source: auxiliary ordered coefficient rank, parameter family, denominator, Hasse order and sign. Observers: coefficient extraction versus field-point evaluation; permissible future operation: parameter differentiation and signed Clausen composition. Theorem A supplies an actual nonfactorization witness, not an unjustified positive mass cancellation.

**Next smallest unit:** Determine the corrected high Hasse ports p+1 and 2p at precision p² and compose them with the original ordered reflected Clausen corner to construct (or obstruct) a genuinely cross-source telescoper for the remaining LIFT residue B_01,p + A_2 H_0/72 - T_jet,p in both target congruence classes. Original-class CM input H0/B0, [X]U mod p², native Frobenius direction/eta and kappa mapping are still missing. Native CM experiment NOT_RUN.

Read-only canonical continuation: Source checkpoint SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED remains; current last_claim_id MCP-d0d70cd041b01e5db192870a is different from stored checkpoint expected_previous_claim_id MCP-87631b892b41fa18d799f2d8. No current authorized winning Research claim/open or new native Source checkpoint. Existing control support Issue #1558 owns this predecessor CAS fault; portable author evidence is not predecessor completed owner progress. No scheduler or source pin changed.
