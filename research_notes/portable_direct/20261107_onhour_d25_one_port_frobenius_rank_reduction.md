# D25 — Exact one-port Frobenius rank reduction for finite Fricke two-jets

2026-11-07 · TASK_RESEARCH author-side. Status: AUTHOR_SIDE_PROVED_ALGEBRA / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. On-hour prior frontier 22538312c7d022d773dd09562273e724d23af290. Science-only independent prior 05f75b399746c5b749e857e13c8b1bfccae658b1 (other hourly20 author's CM first jet/301-prime check) was consumed, not reproduced or treated as shared identity.

## New exact theorem: a single scalar suffices (all integer cutoffs n >= 1)

Define two original rational coefficient streams a_k=binom(2k,k)^2 binom(3k,k)/216^k and b_k=binom(2k,k)^2 binom(4k,2k)/2304^k. For 0<=k<n, keep A_n=sum a_k, J_n=sum k*a_k, B_n=sum b_k and K_n=sum k*b_k separately. Then W_n=A_n+6J_n and V_n=B_n+8K_n. On the exact positive Fricke parameter t=6s, s^2=2, the established cutoff defect has E_n=A_n-(3s/4)B_n and E'_n=u_n+s v_n, where

u_n=-2J_n+7B_n/8+4K_n,
v_n=3J_n/2-5B_n/8-3K_n.

**Theorem 1:** For every n>=1, without modular hypotheses,

3u_n+4v_n=B_n/8,

E_n+(24+18s)E'_n=A_n-3u_n+9B_n/8=W_n-3V_n/2.

Proof: 3(-2J+7B/8+4K)+4(3J/2-5B/8-3K)=B/8, with both J and K contributions cancelling exactly. Therefore the coefficient of s in E+(24+18s)E' is -3B/4+18u+24v=0. The scalar component equals A+24u+36v=A-3u+9B/8. Substituting u gives W-3V/2. The negative conjugate port follows by s→-s. Thus a two-quadratic-jet value/derivative reconstruction has only one independent derivative scalar after the original coefficient-source coordinates A,B are retained.

## Prime-dependent single-port missing Frobenius digit

For p>3 prime let chi_p=(-3/p), and Phi_p=2V_p-W_p-p chi_p. Theorem 1 gives the **exact unconditional identity**

Phi_p=V_p/2-A_p-9B_p/8+3u_p-p chi_p.

Suppose the two explicitly stated p-adic base hypotheses hold:
V_p=p chi_p (mod p^3), W_p=p chi_p (mod p^3).
Then define in F_p
eta_p=((V_p-p chi_p)/p^3) mod p,
gamma_p=((u_p - p chi_p/6 - A_p/3 - 3B_p/8)/p^3) mod p.
Divisions by 2,3,6,8 are in Z_(p); gamma is defined only under the displayed divisibility condition.

**Theorem 2 (conditional exact equivalence):**
Phi_p/p^3 = eta_p/2+3 gamma_p (mod p), so Phi_p=0 (mod p^4) if and only if gamma_p=-eta_p/6 (mod p).

Proof: from u=-W/3+V/2+A/3+3B/8, put W=p chi+p^3 omega, V=p chi+p^3 eta. Then gamma=-omega/3+eta/2 and Phi/p^3=2eta-omega=eta/2+3gamma. The known 2304 full-sum Guo–Zudilin supercongruence supplies V=p chi (mod p^3) for p>3; the W base hypothesis is part of the open mother target and is checked finitely below. These identities reduce the still-missing fourth digit to the one real Fricke/Frobenius scalar gamma, rather than prescribing an entire quadratic two-jet.

## Finite evidence and observer semantics

The companion Python standard-library checker independently accumulates the two rational hypergeometric streams modulo p^4 by coefficient ratios and verifies the identities and conditional normalized formula for **all 301 primes 5<=p<2000**. Five cases p=13,19,43,67,373 have a second independent raw-binomial evaluator. All 301 observed Phi_p=0 (mod p^4); this is exact finite evidence, not a proof for all primes.

| p | chi_p | eta_p | gamma_p | eta/2+3gamma mod p |
|---:|---:|---:|---:|---:|
| 13 | 1 | 11 | 9 | 0 |
| 19 | 1 | 6 | 18 | 0 |
| 43 | 1 | 31 | 2 | 0 |
| 67 | 1 | 61 | 1 | 0 |
| 373 | 1 | 114 | 354 | 0 |

BRC interface COMPOSE_APPLIED: the invariant 3u+4v=B/8 is a lossless derivative-rank reduction only when the original B port is preserved. Preserve both coefficient streams, index and valuation ports, the s-conjugate label, A,J,B,K and u; use gamma as a derived signed/Frobenius readout, not as a replacement for original native H0/B0 data.

## Parent, next precise unit, native reconciliation

Mother objective Delta_p-R_p=0 (mod p) for p=13,19 (mod24), equivalently W_p=p (mod p^3), remains OPEN. Next action: derive gamma_p from the genuine CM/Dwork homogeneous normalization and the existing separate 216/2304 valuation-stratum and Hasse p-th source formulas; prove the p^3 base W congruence before invoking Theorem 2 unconditionally. Discriminating residues: (p,gamma,eta)=(19,18,6),(43,2,31),(67,1,61),(373,354,114). The same-original-class p373 native H0/B0 divided-power Frobenius Hesse-kappa and independent replication remain specifically open at issue #1559; portable sums do not complete them.

Stable logical Research lane: chatgpt-research-onhour-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 is excluded. Read-only native reconcile for target_request_id onhour11-20261106-1400-exact-research-lane-continuation returned QUEUED with EVENT_COLLECTION_IO/Error. The Site gateway is CONFIGURED_NOT_LIVE_VERIFIED, and no Source Researcher session/claim/run is verified. Preserve the original request, REGISTER_PENDING/SYNC_DEBT and scientific evidence as author-side only. Native session/Result/review/admission remains pending and no previous mutation was replayed.
