# D25 — three-stratum p-adic expansion of signed original-216 Clausen sum

Date: 2026-11-05. Role: TASK_RESEARCH author-side. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Status: EXACT ALGEBRAIC IDENTITY / 611-PRIME FINITE CHECK / UNREVIEWED / NOT_ADMITTED; native H0/B0 NOT_RUN.

## Exact theorem for every prime p=6n+1 >= 7

In Z localized at p, work modulo p^3. Set

  a_k = (1/2)_k (1/3)_k (2/3)_k / [2^k (k!)^3],
  W_p = sum_{0<=k<p} (6k+1) a_k.

Let (m_1,m_2,m_3)=(3n,2n,4n), (beta_1,beta_2,beta_3)=(1/2,1/3,2/3). Exactly, alpha_j=-m_j+p beta_j equals (1/2,1/3,2/3).
For 0<=k<p let epsilon_j(k)=1 if k>m_j and 0 otherwise; v(k)=sum_j epsilon_j(k). Define

  D_k = [prod_j beta_j^{epsilon_j(k)} prod_{0<=r<k,r!=m_j}(r-m_j)]/[2^k(k!)^3],
  L_k = sum_j beta_j sum_{0<=r<k,r!=m_j} 1/(r-m_j),
  J_k = sum_j beta_j^2 sum_{0<=r<k,r!=m_j} 1/(r-m_j)^2.

All denominators are p-units. The following termwise identity holds mod p^3:

  a_k = p^{v(k)} D_k [1 + p L_k + p^2 (L_k^2-J_k)/2]   (mod p^3).

In particular, with the *signed* original 6k+1 weight,

  S0 = sum_{k=0}^{2n}   (6k+1) D_k [1 + p L_k + p^2 (L_k^2-J_k)/2],
  S1 = p sum_{k=2n+1}^{3n} (6k+1) D_k [1 + p L_k],
  S2 = p^2 sum_{k=3n+1}^{4n} (6k+1) D_k,

the exact finite certificate is

  W_p = S0 + S1 + S2  (mod p^3).

The terms 4n+1 <= k < p vanish at this precision because all three original Pochhammer factors have a p-factor.

**Proof.** In each product (-m_j+p beta_j)_k, the r=m_j factor is p beta_j (when present); each other factor equals (r-m_j)(1+p beta_j/(r-m_j)). Factor out all p's, expand the remaining product to second order, and use the quadratic elementary symmetric identity (L_k^2-J_k)/2. The three strata correspond exactly to v=0,1,2. The v=3 stratum vanishes mod p^3. All factors and denominators are p-integral and this proves the identity for every stated prime.

The exact integer base products are (-1)^k m!/(m-k)! for k<=m and (-1)^m m!(k-m-1)! for k>m. The reciprocal sums are -(H_m-H_{m-k}) when k<=m and -H_m+H_{k-m-1} when k>m; the square-reciprocal sums have corresponding positive harmonic formulas. Thus all three ports admit finite-factorial and harmonic forms.

## Executed independent finite checks

The companion standard-library script computes S0,S1,S2 by p-adic factor extraction and separately computes W_p by the original 3F2 recurrence, modulo p^3. All 611 primes p=1 mod 6 with 7<=p<=10000 satisfy the termwise regrouping and independent full-sum equality (611 PASS, 0 errors). All 611 also have W_p=p modulo p^3 in this *bounded* run, not an all-prime proof.

At p=13, (S0,S1,S2)=(780,1937,1690) mod 2197, summing to 13. At p=373, (S0,S1,S2)=(28094360,38687933,37008314) mod 51895117, summing to 373. Each port is nonzero; the global scalar depends on signed cancellation.

## BRC / source / continuation

BRC COMPOSE_APPLIED: retain source-labeled parameter factor j, p-valuation stratum, original sign/weight, and first-/second-jet information. The 3-port representation is sufficient only for the designated W_p modulo p^3 observer; it does not identify native crystalline Frobenius or give an all-prime supercongruence.

Another Research lane has already established source-typed R_frozen = signed Clausen T, author-side: research_notes/portable_direct/20261105_onhour_d25_original_R_clausen_T_exact_identification.md (current main). This unit consumes that result without recrediting it. Under the existing frozen interface, the mother target Delta_p-R_p=0 (mod p) for p=13,19 mod24 is now equivalent to proving W_p=p (mod p^3) on that domain. The next exact step is to prove cancellation S0+S1+S2=p uniformly, by a terminating creative-telescoping or parameter-derivative certificate, or produce an exact in-domain counterexample. Preserve original cutoff, native H0/B0, [X]U mod p^2, eta/kappa and independent review.

Source native checkpoint remains unchanged and author-side note is not admitted. Original close request research-hourly20-20261105-1230-close-stale-session SUCCEEDED in kimi-query-bridge#6655, closing only MCP-06f7ad61a8d841d9ba1ba1ef4d088d94. Read request research-h20-20261105-1318-current-continuation SUCCEEDED at Source 3537262a71d7cc40442326bf07fdee17375850fc, NO_LIVE_CLAIM, REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED. Successor session_start request research-hourly20-20261105-1318-successor-session-start remains to reconcile before any own CLAIM/open. Research conversation label requested: chatgpt-research-hourly-enterprise-math-20260923; excludes maintenance chatgpt-hourly-enterprise-math-20260921.
