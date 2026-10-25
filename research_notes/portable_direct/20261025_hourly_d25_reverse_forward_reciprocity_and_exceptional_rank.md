# D25/LIFT — exact forward/reverse reciprocal pairing and the exceptional rank

Date: 2026-10-25. Role: TASK_RESEARCH, own logical research lane chatgpt-research-hourly-enterprise-math-20260923. Formal Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

Research status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No native CM/divided-power experiment or new Source checkpoint is claimed.

## Exact inherited input and new question

Consume the verified author derivation of the original signed hypergeometric sum W_p, its four p-adic rank bands and fourth-band reverse hypergeometric kernel from research_notes/portable_direct/20261025_hourly_d25_original_four_band_p4_reverse_tail.md (source commit df85f54d1a1477cbbbcdd54742b1913c0f33166a). That earlier work proved e_0=5 and the formula for e_k, but did not establish the present multiplicative forward/reverse pairing. No earlier theorem is re-credited.

Let p=6m+1 >=7 be prime. Work in the source-marked field F_p and the localization Z_(p). For 0<=k<=2m-1, define the first-band *unweighted* original coefficient

A_k = (1/2)_k (1/3)_k (2/3)_k / [2^k (k!)^3] in F_p^×,

and the fourth-band reverse coefficient

e_k = d_(p-1-k) = d_(6m-k) in F_p^×.

Here d_n is exactly the original-p^(r_n) extracted coefficient from the inherited four-band theorem, not an unrelated normalized CM variable. The inherited original signed coefficient is a_k=(6k+1)A_k. The distinct source ranks are retained.

## Theorem: all-prime reciprocal forward/reverse pairing

For EVERY odd prime p=6m+1>=7 and EVERY integer 0<=k<=2m-1,

e_k A_k = Phi(k) = 2(6k+5) / [(2k+1)(3k+1)(3k+2)]  (mod p).

Every factor in the displayed denominator is invertible modulo p in the stated window. So is A_k; Phi(k) is nonzero there. Therefore the *signed fourth-band scalar* admits a forward-source-only reciprocal representation:

B3/p^3 = SUM_{k=0}^{2m-1} e_k
       = SUM_{k=0}^{2m-1} Phi(k)/A_k  (mod p).

This is a new exact finite-field coupling of distinct original rank branches. It is NOT an all-prime identity proving W_p=p (mod p^3), and it is not a formula for native Frobenius or kappa.

### Proof

The earlier *source-bound finite reverse* formula, valid for this complete finite window without a pole, is

e_k = 5 (11/6)_k (1)_k^3 2^k /
      [(5/6)_k (5/3)_k (3/2)_k (4/3)_k].

Multiply by the original forward A_k above, preserving the reverse index p-1-k. The 2^k and (1)_k^3 factors cancel. Applying the finite Pochhammer shift identity

(a)_k/(a+1)_k = a/(a+k)

gives

e_k A_k
= 5 [(11/6)_k/(5/6)_k] [(1/2)_k/(3/2)_k]
    [(1/3)_k/(4/3)_k] [(2/3)_k/(5/3)_k]
= (6k+5) * [(1/2)(1/3)(2/3)] /
  [(k+1/2)(k+1/3)(k+2/3)]
= 2(6k+5)/[(2k+1)(3k+1)(3k+2)].

For 0<=k<=2m-1, all k!, 2, 3 and the three displayed denominator factors are nonzero modulo p. Neither 6k+5 nor a parameter of A_k vanishes in this window (6k+5=p would require k=m-2/3, not an integer). Thus no accidental division by a zero factor occurs. Summation proves the signed band identity. QED.

## Two universal cross-rank certificates

At the exceptional original index k=m, the factor 6m+1 equals p *exactly*:

a_m = (6m+1) A_m = p A_m in Z_(p).

Although the signed original term a_m vanishes modulo p, the marked pre-factor A_m remains a unit. Substituting m=-1/6 (mod p) into Phi gives

e_m * (a_m/p) = d_(5m) A_m = Phi(m) = 16 (mod p).

Thus a dangerous observer quotient a_m modulo p would erase a source coordinate that has a nonzero, universal fourth-band reciprocal partner. This is a specific BRC provenance/valuation information-loss witness, not an inference about physical residuals.

At the other edge, k=2m-1 gives

d_(4m+1) A_(2m-1) = Phi(2m-1) = 3/5 (mod p).

Both endpoint constants are exact all-prime statements, not finite-sample guesses.

## Independent author exact checks

The companion code computes A_k from the forward Pochhammer recurrence, computes d_(6m-k) from the original factorial source extraction rather than this reciprocal theorem, and independently generates the reverse tail from the prior finite hypergeometric recurrence. For every k it checks the displayed product, the reciprocal sum, exceptional k=m and both endpoints. All 80 primes p=1 (mod 6) below 1000, plus 1327 and 19963, passed. This is author finite arithmetic checking; the universal theorem is supported by the algebraic proof.

Selected exact fourth-band scalar B3/p^3 (mod p):
- p=7: 6
- p=13: 5
- p=19: 4
- p=373: 278
- p=1327: 0 (all fourth-band terms remain individually nonzero; signed cancellation)
- p=19963: 16527

Reproducer: research_notes/portable_direct/20261025_hourly_d25_reverse_forward_reciprocity_check.py (same atomic commit).

## BRC / Enterprise-coordinate use and boundary

Concrete composition state: COMPOSE_APPLIED. Inputs are source-labelled forward (k,A_k) and reverse (p-1-k,e_k) ports, the rank valuation a_m=pA_m, and signed sum B3/p^3. The multiplication law Phi(k) retains both ports before the final signed observation; substituting positive branch mass, Boolean support or a quotient by 6k+1 loses the k=m information. BRC source/valuation and signed-observer laws are applied mathematically. No native BRC executable was run; local Python is exact author checking, not an Enterprise X6 native dynamical transfer.

## Remaining scientific frontier and exact next action

Seek a signed finite-field/finite-hypergeometric certificate coupling the reciprocal mirror SUM Phi(k)/A_k to the FIRST THREE original p-adic bands at the p^3 observer, without dividing by (6m+1)=p or guessing cancellations from finite samples. Such a certificate, if obtained, still requires a separate argument for the specified full supercongruence. The parent D25/LIFT/JT2 task remains OPEN pending authenticated same-original-class H0/B0, [X]U mod p^2, actual Frobenius rank/semilinear direction/normalization, and a proved kappa / Delta_p-R_p source bridge. Native CM experiment NOT_RUN. Keep the formal Source checkpoint and predecessor contribution history intact; these portable notes do not claim canonical owner progress or independent review.
