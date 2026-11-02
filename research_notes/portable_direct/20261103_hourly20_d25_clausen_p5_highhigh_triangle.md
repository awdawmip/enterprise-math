# D25 | First high/high Gauss-pair source port at Clausen precision p^5

**2026-11-03, Asia/Hong_Kong.** AUTHOR-DERIVED / HAND-PROVED / FINITE EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Research lane `chatgpt-research-hourly-enterprise-math-20260923`, not maintenance nor the on-hour Research lane. Frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Original frozen mother remains open.

## P1 — Exact high/high component of the next digit (all primes p=6r+1>=7)

Reuse the original Gauss/Clausen coefficients `c_k=(1/6)_k(1/3)_k/(k!)²`, finite `G_p,F_p`, and `D_p(z)=F_p(z)-G_p(z)^2=-sum_{i+j>=p, 0<=i,j<p}c_i c_j z^(i+j)` from the previous new four-moment theorem (EM commit `8874c69882d7d3c697ee97c0f395d08a0aa8a918`). Put `theta=z d/dz`, `z0=1/2`, and raise the same observable to `E_p^[3]=[(1+6theta)D_p](1/2)/p² (mod p³)`.

Let `U0=1/10 (mod p)` (the previously proved upper Gauss unit), and for **0<=s<=4r-1** define

`A_s=(s!)²/[(11/6)_s(5/3)_s]`, `B_s=2^s A_s` in `F_p`.

All denominators in this extended range are p-units. Put the two high-tail prefixes `Lambda_m=sum_{0<=t<m}B_t`, `Gamma_m=sum_{0<=t<m}t B_t` for `0<=m<=4r), and `L(s)=min(4r-1,p-2-s)`.

Then the **complete high/high ordered-pair component**, and only that component, of `E_p^[3]` is

`P_HH = p²*U0²*sum_{s=0}^{4r-1} B_s [(11+6s)Lambda_(L(s)+1)+6Gamma_(L(s)+1)] (mod p³)`.  **[P1, proved]**

This is a genuinely new source direction at the higher precision: the mod-p² four-prefix formula discarded high/high only after a proven valuation bound; P1 restores its first visible digit.

### Proof

The exact coefficient valuation for the high band `2r+1<=k<=p-1` is `v_p(c_k)=2`. The substitution `k=p-1-s` identifies it with `0<=s<=4r-1`. The exact reverse ratio `c_(n-1)/c_n=n²/[(n-5/6)(n-2/3)]` has p-unit factors on all steps `n=p-1-t` with `0<=t<4r-1`. Reducing the products modulo p extends the upper reflection as

`c_(p-1-s)/p² = U0*A_s (mod p)`, all `0<=s<=4r-1`.

For two high indices `i=p-1-s,j=p-1-t`, the original Clausen support condition `i+j>=p` is exactly `s+t<=p-2`. Their product has valuation four; after dividing `D_p` by `p²`, the high/high contribution is `p²` times its mod-p unit. The signed Euler weight and powers reduce to

`6(i+j)+1 =12p-11-6(s+t) ≡-11-6(s+t) (mod p)`,

`2^(-(i+j)) ≡2^(s+t) (mod p)` by Fermat.

Thus, including the negative sign of the exact truncation difference,

`P_HH/p² = U0² sum_{0<=s,t<=4r-1; s+t<=p-2}(11+6s+6t)B_s B_t (mod p)`.

At fixed s, t runs from 0 to `L(s)`; summing its 0th and 1st moments proves P1. The double sum already counts **ordered pairs including diagonal terms**, so no extra factor 2 is permitted. QED.

### Independent exact calculation

Two actually executed standard-library integer algorithms agree on 11 specified primes `7,13,19,31,37,43,73,181,373,1171,1999`: (a) direct original high/high ordered pairs, with `c_i` independently computed modulo `p^4`, and (b) extended reflected `A_s` plus the two-prefix triangular formula. All 11 pass. The p=373 original pair enumeration checks **53,878 ordered pairs**, yielding `P_HH/p²=221 (mod373)`; hence `P_HH=221*373²=30747509 (mod373³)`. The coefficient is `12 (mod13)` at p=13 and `9 (mod19)` at p=19. The full Python checker, JSON result, execution log and SHA256 manifest accompany this run in `enterprise_math_D25_clausen_p4_p5_sources_20261103.zip`. The finite sample does not substitute for the general algebraic proof.

The complete `E_p^[3]` additionally requires second-order low/high and first-order middle/high data; P1 precisely isolates the previously invisible high/high channel rather than claiming the full new defect. BRC: **COMPOSE_APPLIED** with an exact joint ordered-pair triangular source predicate, p-adic valuation and two first-moment prefixes; information is not merged into a coarser old observer. This is ordinary original-coefficient arithmetic, not a native H0/B0 or X6 experiment.

**Next exact unit:** assemble the remaining low/high second-order and middle/high first-order carriers into the full mod-p³ defect, then compare with the Gauss/Hensel original216 carry. Universal target-class `12jh=1 mod p`, the all-prime original216 supercongruence, and the frozen `Delta_p-R_p=0 mod p` remain open. Formal native CLAIM/OPEN/checkpoint/review require repaired Source authority; control support #1558 and native p373 H0/B0 support #1559 remain separate.
