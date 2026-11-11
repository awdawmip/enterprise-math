# D25/LIFT — p-adic two-port lift and exceptional order-two primes

2026-11-11. Status: AUTHOR_PROVED / EXACT_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-side portable evidence; no native Result or independent review.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3.

## All-precision corollary

For prime p>=5 write p=6m+1+4e (e=0 or 1). Define
K(X)=sum_{k=0}^m binom(m,k)binom(2m+e,k)X^k,
A=K(1/2), B=(1-6e)A+6K'(1/2).

Reuse the exact prior integer recurrence [inverse-free two-port theorem](https://github.com/awdawmip/enterprise-math/blob/905dc3189e5e18fbf2a741db1f38b37cf0270922/research_notes/portable_direct/2026-11-11_h40_d25_inverse_free_zero_port_author_portable.md), giving A=c^m U_m/Q_m, B=T_m/Q_m with integers U_m,T_m and c=5 (e=0) or 8 (e=1). The common Q_m equals 500^m (2m)! if e=0 and 2048^m (2m+1)! if e=1.

**For every p and every integer r>=1:**
A ≡ 0 (mod p^r) iff U_m ≡ 0 (mod p^r);
B ≡ 0 (mod p^r) iff T_m ≡ 0 (mod p^r).

**Proof.** For e=0, 2m<p; for e=1, 2m+1<p. Therefore the factorial factor in Q_m is prime to p. For p>=7 the constants c,500,2048 are also prime to p. When p=5, necessarily m=0,e=1, Q_m=c^m=1. The exact rational identities are equalities over the localization Z_(p); multiplication by units preserves divisibility by every p^r. Both residues may be reconstructed with one common inverse of Q_m. Zero-order tests require no modular inversions in the prior integer recurrence. □

The inverse-free scheme uses O(m) modular operations and O(1) residual words of O(r log p) bits at fixed r; its total bit cost remains explicit.

## Complete finite p² survey

Enumerated **all 5,131 primes 5<=p<=50000**. Exact coefficient recurrence in Z/p²Z rechecks unique p-zero port and the observed (-6/p) selector: 2,583 A-zero cases, 2,548 B-zero cases.

Exactly TWO zero ports have valuation greater than one:
- **p=149, e=1, m=24:** B ≡ 0 (mod p²), A ≡ 11022 (mod p²); B ≡ 278267334 (mod p⁴=492884401), so v_p(B)=2 and B/p² ≡ 18 (mod p).
- **p=211, e=0, m=35:** A ≡ 0 (mod p²), B ≡ 5146 (mod p²); A ≡ 1294715201 (mod p⁴=1982119441), so v_p(A)=2 and A/p² ≡ 174 (mod p).

The other 5,129 unique zero ports have valuation exactly one in this finite domain. The examples refute the stronger candidate universal simple-zero assertion but do not decide the original mod-p Legendre selector. All operations are integer/modular exact; selected factorial-binomial crosschecks and independent direct binomial checks at both exceptions agree with the recurrence.

The accompanying local portable ZIP contains the complete proof, executable Python checker and 5,131-record JSON certificate. Each record includes p, e, m, both port residues modulo p², zero-port label, and truncated valuation.

## BRC observer and native boundary

Retain the ordered observer (p,e,m,A mod p²,B mod p²,zero-port label,v_p), rather than only A*B mod p. This is an auxiliary finite Clausen-polynomial result, not the native crystalline H0/B0 Frobenius/eta or Delta_p-R_p computation. Native same-original-class p=373 second-digit comparison, signed Hesse/Green observer and independent Source review remain separate unfinished units.

Previously pending read requests h40-20261111-0949-exact-d25-continuation and h40-20261111-0946-canonical-tasks were reconciled as SUCCEEDED. Own native execution session and winning CLAIM are unavailable; this note is author-only and is not predecessor completed research for CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS.

Original UR V2 exact four-file object still requires 94687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. Already completed UR mathematics is not re-proved.


## Original W_p fourth-digit crosscheck: a precise non-implication

For the original D25 observation a_k=(2k)!(3k)!/[216^k(k!)^5], W_p=sum_{k=0}^{p-1}(6k+1)a_k, use two independent exact algorithms modulo p^4: recurrence
a_{k+1}/a_k=(2k+1)(2k+2)(3k+1)(3k+2)(3k+3)/[216(k+1)^5]
and factorial products. Both check all residue values at the two exceptional primes:

| p | chi_{-3}(p) | W_p mod p^4 | (W_p-chi_{-3}(p)p)/p^3 mod p |
|---|---|---|---|
| 149 | -1 | 287791414 | 87 |
| 211 | +1 | 1803634963 | 192 |

Thus W_p ≡ chi_{-3}(p)p (mod p^3) holds at both inputs, but W_p ≢ chi_{-3}(p)p (mod p^4). The suggested extra-lift implication "an auxiliary vanishing Clausen port with p-adic order >=2 forces the original W_p congruence to lift to p^4" is **refuted** by each of these exact finite examples. This remains a statement about the auxiliary port-to-W bridge, not a native Frobenius H0/B0 calculation.

The executable three-file portable ZIP includes a separate original-W factorial crosscheck and the 5,131-row full certificate; GitHub's compact prime checker concerns the two-port scan.