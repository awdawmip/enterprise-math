# D25 — proved inert-prime slice of Ramanujan–Sato product congruence (2026-11-05)

**Status:** AUTHOR-SIDE EXACT PROOF / 45 PRIME EXACT AUDIT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; unchanged frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical conversation `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance.

## External theorem and target

Babei–Roy–Swisher–Tobin–Tu, *Supercongruences arising from Ramanujan-Sato Series*, arXiv:2408.08844v3 (2025-03-12), Table 1.1 row Ex 5.5 and Example (J), uses `b=(1/2,1/3,2/3)`, `alpha_N=3`, `d=3`, `lambda=1/2`. Their Conjecture 6.2 predicts `[F_{0,b} F_{6,b}]_{p-1}(1/2)=0 (mod p^3)` for supersingular primes, where the brackets truncate the *Cauchy product series* at degree p−1. Section 4 proves the corresponding statement only modulo p². External source: https://arxiv.org/abs/2408.08844 (v3 PDF, pp. 3, 16–17, 21–23). This note proves the supersingular **subcase** for all primes `p≡13,19 (mod 24)`, without claiming an unverified priority.

Define `F_{alpha,b}(z)=sum_{k>=0}(alpha*k+1)(1/2)_k(1/3)_k(2/3)_k*z^k/(k!)^3`.
**Scoped all-prime theorem.** For every prime `p>=13` with `p≡13 or 19 (mod 24)`,

```
[F_{0,b}(z) F_{6,b}(z)]_{p-1} evaluated at z=1/2 = 0 (mod p^3).
```

## Proof

Let `p=6n+1`. Put `a_k=(1/2)_k(1/3)_k(2/3)_k/[2^k(k!)^3]` and `b_k=(1/6)_k(1/3)_k/[2^k(k!)^2]` for `0<=k<p`. All denominators are p-units. Define `H=sum_{k<p}a_k`, `W=sum_{k<p}(6k+1)a_k` and `L=sum_{k<p}b_k`.

Consume two **already accepted** original-source inputs at these target primes: `L=0 (mod p)` (CM0 inert Hesse/Legendre) and `W=p (mod p²)` (first digit UR). We do not recredit these sources.

1. The formal Clausen identity `_2F1(1/6,1/3;1;z)^2=_3F2(1/2,1/3,2/3;1,1;z)` gives `H=sum_{i+j<p}b_i b_j` exactly as a rational equality. Thus `L²-H=sum_{i+j>=p; i,j<p}b_i b_j`. For indices `k<p`, `v_p(b_k)` equals 0 on `[0,n]`, 1 on `[n+1,2n]`, 2 on `[2n+1,p-1]`. Every omitted pair `i+j>=p` has `v_p(b_i b_j)>=2`. Therefore `H≡L²≡0 (mod p²)`.
2. Write the **actual product-truncation observable** `P=sum_{i+j<p}(6j+1)a_i a_j`. Then `E=H W-P=sum_{i+j>=p; i,j<p}(6j+1)a_i a_j` is the exact signed endpoint. The valuation of `a_k` equals 0 on `[0,2n]`, 1 on `[2n+1,3n]`, 2 on `[3n+1,4n]` and 3 on `[4n+1,p-1]`. For `i+j>=6n+1`, the valuation of `a_i a_j` is at least 3: if `i<=2n`, then `j>=4n+1`; if `2n<i<=3n`, then `j>=3n+1`; if `3n<i<=4n`, then `j>=2n+1`; if `i>4n`, its own valuation is already 3. Hence `p³|E`.
3. By Step 1 `p²|H` and inherited first-digit `W=p (mod p²)` entails `p³|HW`. Since `P=HW-E`, conclude `P≡0 (mod p³)`. QED.

This is a **new composition of accepted results** to answer a separately published hypergeometric product question. It does NOT assert the still-open single-series third-digit target `W=p (mod p³)`.

## Finite exact verification and sharpness

Reproducible independent script `research_notes/portable_direct/d25_clausen_sato_product_p3_20261105.py` evaluates a hypergeometric recurrence modulo p⁴, the truncated signed Cauchy product, the original integer-binomial formula independently at four anchors, and both omitted-tail valuations. 45/45 target primes p<=997 pass (0 failures). Every checked p has `v_p(H)=2` and `v_p(P)=3` (finite observation, not universal valuation theorem).

| p | H/p² mod p | W mod p³ | P/p³ mod p | (HW-P)/p³ mod p |
|---:|---:|---:|---:|---:|
| 13 | 11 | 13 | 2 | 9 |
| 19 | 8 | 19 | 4 | 4 |
| 139 | 53 | 139 | 62 | 130 |
| 373 | 71 | 373 | 268 | 176 |

The exact p=13 witness `P≡2*13³ (mod 13⁴)` refutes the **universal p⁴ strengthening of this product**. It is not a counterexample to LIFT.

## BRC observer typing, canonical continuation and debts

BRC carrier: two ordered indices (i,j) and original signed weight (6j+1); retain separate degree truncated convolution P and product-of-truncated-evaluations HW, their exact difference E, and valuation tier information. The condition `E=0 mod p³` is established for **this observer and modulus**, not for p⁴, the original frozen Delta-R observer, or native crystalline Frobenius. External algebraic/CM coordinates are auxiliary, not an unproved mapping to native X6 slice.

Mother objective remains `Delta_p-R_p=0 (mod p)`, p≡13,19 mod24, at the frozen scalar interface. The accepted native-source port identity (author-aligned but not admitted) is `Delta-R=(W-p)/p² mod p`; the third digit is still open. Next exact mathematical action: use a p-dependent finite terminal certificate for `W=p modp³` retaining the signed original cutoff; do not restart first-digit/Clausen or conflate this product with the single series.

Independently, fixed p=373 same-original-class H0/B0 divided-power `[X]U mod 139129`, actual rank, semilinear Frobenius/eta, signed odd Hesse/Green, kappa and independent replication remain **NOT_RUN / PENDING_OWNER** under issue #1559. This artifact does not supply native execution or a formal Result.

Source continuation request `onhour11-20261105-1203-d25-cont` returned `SUCCEEDED` at 2026-11-05T04:07:29.885693+00:00, `execution_authorized=false`; existing other-session Source claims are not adopted. No native CLAIM/open/run/Source checkpoint/Result is asserted. File status: AUTHOR PUBLISHED / REVIEW PENDING / NOT_ADMITTED.
