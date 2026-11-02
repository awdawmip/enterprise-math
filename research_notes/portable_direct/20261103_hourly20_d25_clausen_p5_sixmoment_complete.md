# D25 | Complete p^5 finite-Clausen source reconstruction: six moments plus a high/high triangular port

**2026-11-03 (Asia/Hong_Kong).** AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Own TASK_RESEARCH logical conversation `chatgpt-research-hourly-enterprise-math-20260923`. The maintenance `chatgpt-hourly-enterprise-math-20260921` and distinct on-hour Research session are not used. Frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Original mother `Delta_p-R_p=0 (mod p)`, `p mod24 in {13,19}`, remains open.

## Precise statement and definitions

Fix any prime `p=6r+1>=7`. All rational expressions below lie in `Z_(p)` after exact division by the displayed powers of p. Set

`c_k=(1/6)_k(1/3)_k/(k!)²`, `G_p(z)=sum_{k=0}^{p-1}c_k z^k`,

`a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³`, `F_p(z)=sum_{k=0}^{p-1}a_k z^k`,

`theta=z d/dz`. The exact finite Clausen truncation identity is

`F_p(z)-G_p(z)^2=-sum_{0<=i,j<p, i+j>=p}c_i c_j z^(i+j)`.

Define the **new full third-digit** finite defect

`E_p^[3]=[(1+6theta)(F_p-G_p²)](1/2)/p² (mod p³)`.

Here the previously proved H4 and four-moment `E_p^[2]` equal the reductions modulo `p` and `p²`, respectively. The present result is about the original finite Gauss/216 scalar, and does not identify the native X6 H0/B0 object.

For `0<=s<=2r-1` put

`A_s=(s!)²/[(11/6)_s(5/3)_s]`,

`H_s=sum_{t<s}(1/(t+11/6)+1/(t+5/3)-2/(t+1))`,

`J_s=sum_{t<s}(1/(t+11/6)²+1/(t+5/3)²-2/(t+1)²)`, and

`Q_s=(H_s²+J_s)/2`.

Define the **six typed prefix moments** for `i=1,...,2r`:

`Lambda_i^(v)=sum_{s<i}2^s A_s T_v(s)`, `Gamma_i^(v)=sum_{s<i}s 2^s A_s T_v(s)`, for `v=0,1,2`,

where `T_0=1,T_1=H_s,T_2=Q_s`. They are evaluated modulo `p³`. Set `B_i^(v)=(6i-5)Lambda_i^(v)-6Gamma_i^(v)`.

The exact high-edge unit is `U_p=c_(p-1)/p² (mod p³)`; **only its mod-p digit** `U_p=1/10 (mod p)` was proved in inherited U1, so the higher unit digits are retained as genuine original coefficient data.

## Theorem C3 — Complete precision p^5 carrier (all prime p=6r+1>=7)

The full defect is congruent modulo `p³` to the sum of two distinct valuation-typed parts:

`E_p^[3] = P_LM + P_HH (mod p³)`,

with **all low/high and middle/high ordered pairs included** through

`P_LM=-2 U_p 2^(-(p-1)) sum_{i=1}^{2r}c_i 2^(-i) [B_i^(0)+p(B_i^(1)+6Lambda_i^(0))+p²(B_i^(2)+6Lambda_i^(1))] (mod p³)`.

For the **high/high** port, extend `A_s` to the finite range `0<=s<=4r-1` (the Pochhammer denominators remain p-units in this precise range), set `X_s=2^s A_s (mod p)`, and define `Lbar_m=sum_{t<m}X_t`, `Gbar_m=sum_{t<m}tX_t`. Let `m(s)=min(4r,p-1-s)`. Then

`P_HH=p²/100 * sum_{s=0}^{4r-1}X_s[(11+6s)Lbar_(m(s))+6Gbar_(m(s))] (mod p³)`.

All denominators in C3 are p-units; `p²/100` denotes `p²*(100^(-1) mod p)`. No factor of two is appended to the high/high sum: its triangular index set counts both ordered permutations and the diagonal exactly once each. Thus **six low/middle-to-high prefix moments, one high/high triangular 0th/1st-moment carrier, and the original Gauss boundary unit determine this exact third digit**. The formula uses `O(p)` modular operations with moduli `p³`; its bit cost additionally includes input construction, modular inversion and `O(log p)`-bit operands.

### Proof

1. **High-edge expansion to two extra powers.** The exact Gauss backward quotient is
   `c_(n-1)/c_n=n²/[(n-5/6)(n-2/3)]`.
   Substituting `n=p-1-t` gives
   `A_(t+1)/A_t * (1-p/(t+1))²/[(1-p/(t+11/6))(1-p/(t+5/3))]`.
   Multiplying factors to depth `s` and expanding formally in the p-local ring gives
   `c_(p-1-s)/p²=U_p A_s[1+pH_s+p²(H_s²+J_s)/2] (mod p³)`, for `0<=s<=2r-1`. The degree-two term follows from the elementary product/log-coefficient identity over a ring where 2 is a unit, not an analytic convergence assumption.
2. **Exhaustive source valuation partition.** For `k=0,...,p-1`, `v_p(c_k)=0` on `[0,r]`, `=1` on `[r+1,2r]`, `=2` on `[2r+1,p-1]`. Since `4r<p`, any pair `i+j>=p` contains at least one high index. The disjoint support is low/high, middle/high, or high/high, with coefficient-product valuations 2,3,4 respectively. There are no other pairs.
3. **Low/high and middle/high.** Orient each non-high index as `1<=i<=2r`, its high mate `j=p-1-s`, where `0<=s<i`; count the two ordered permutations. The original Euler weight and power are exactly
   `6(i+j)+1=(6i-5)-6s+6p`, and
   `2^(-(i+j))=2^(-i)2^(-(p-1))2^s`.
   Insert the second-order high-edge expansion and collect the coefficients of `1,p,p²`. This gives precisely the six-moment expression `P_LM`. For middle/high, its coefficient contains one more p factor, so the same expression automatically truncates at the right precision.
4. **High/high.** Orient both original high indices as `i=p-1-s, j=p-1-t` with `0<=s,t<=4r-1`. The exact cutoff is `s+t<=p-2`. Their product has valuation four; after dividing by p² only the `mod p` units remain. The inherited `c_(p-1)/p²=1/10 (mod p)` and extended backward reflection imply `c_(p-1-s)/p²=A_s/10 (mod p)`. The negative sign of the finite Clausen defect and the signed weight
   `6(i+j)+1=12p-11-6(s+t)`
   yield `P_HH/p²=1/100*sum_{s+t<=p-2}(11+6s+6t)X_sX_t (mod p)`. Summing the t moment to `t<m(s)` gives the explicit triangular P_HH. The disjoint supports cover the exact finite defect, proving C3. QED.

## Actually executed finite exact verification

A new author-side Python standard-library checker `d25_clausen_p5_sixmoment_full_20261103.py` actually executed on all **148 primes** `7<=p<=2000`, `p≡1 (mod6)`. One algorithm evaluates the **original** finite `F_p`, `G_p`, `theta G_p` modulo `p^5` from their distinct coefficient recurrences, forming the exact `p²` quotient of `[(1+6theta)(F_p-G_p²)](1/2)`. Another algorithm reconstructs the `p³` quotient from the six moments and the separate high/high triangle. **148/148 PASS**. This is a finite consistency check, not an independent review or universal proof by enumeration.

At `p=373`:

- `E_373^[3]=20,942,635=73,285+150*373² (mod 373³)`. Its earlier digits are `177+196*373`; **150 is the new third digit of this specific finite-Clausen defect**.
- `P_LM(low/high)=9,731,747`, `P_LM(middle/high)=32,358,496`, and `P_HH=30,747,509=221*373²` modulo `51,895,117`. Their sum is `20,942,635` modulo that modulus.
- `U_373=36,237,435 (mod 373³)`; the new coefficient retains original upper Gauss digits, not a fitted normalized unit.

At `p=13`, `E^[3]=2,093=65+12*13² (mod 13³)`, with `P_HH=12*13²` nonzero. These witnesses make the precision extension and the new high/high source direction observable.

## Exact frontier, BRC and permission scope

BRC status **COMPOSE_APPLIED**: original pair indices and order, Gauss valuation bands, p-adic unit digits, six typed moments, the distinct high/high triangular port and the original signed Euler observer remain explicit. The compression is proved **for the declared scalar Euler-Clausen defect**, not a universal observer equivalence or native X6 identity. This theorem reuses rather than reproves the already published two-moment H4, Gauss unit 1/10, and two-prefix high/high P1.

**Next mathematical unit:** feed C3's finite defect through the already proved Hensel second/third-carry relations for the original 216 series, keeping the Gauss derivative-unit and integer-lift digits distinct; search for a uniform CM/WZ cancellation certificate or an in-domain counterexample to the target `12*j*h=1 (mod p)` in classes 13,19. The frozen parent `Delta_p-R_p=0 (mod p)` is a separately typed observer and needs an actual connecting proof. Independently, the exact native p=373 same-original-class H0/B0 experiment remains pending responsible executor at #1559.

**Control observation:** Gateway 0.6.11 on 2026-11-03 reported `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, native quota `5/5`. Existing own #6637 is historical read-only recovery and #6638 definitive failed continuation; neither was replayed. Source support #1558 remains open; earlier neutral staging is not completed research. No new formal session, CLAIM, OPEN, Source checkpoint, freeze, review or mathematical admission is claimed.
