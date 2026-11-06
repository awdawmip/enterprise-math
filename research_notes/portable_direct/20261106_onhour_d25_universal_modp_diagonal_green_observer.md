# D25 — Mod-p universal diagonal Green kernel for original 216 observers

2026-11-06 | SECOND-DIGIT-LIFT TP2-B6F4FC938FF94941C1B7 | Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 | Research conversation chatgpt-research-onhour-enterprise-math-20260923. Status AUTHOR-PROVED / FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED. New purpose-scoped coefficientwise corollary of the prior exact full-source 216 weighted-prefix transfer (d45b65a2b2455475ae97760ce51130a5451c1d30); consumes the separate exact full-216 p-unit cubic endpoint result at b83a4371ef96a681a6450b0ce7a13762cc1d4945. No re-crediting of these already finished theorems.

## Finite-field theorem (source-sensitive)

For any prime p=6m+1>3 let a_0=1 and
```
a_k/a_(k-1)=(2k-1)(3k-2)(3k-1)/(36k^3),  1<=k<=m
P_t=sum_(k=0)^(t-1)(6k+1)a_k
d_0=1, d_(i+1)/d_i=(6i+1)(3i+1)/(36(i+1)^2)
e_1=1/10, e_(r+1)/e_r=36r^2/((6r+5)(3r+2)).
c_k=sum_(r=1)^(m-k)d_(k+r)e_r, 0<=k<m.
```
Define a **prime-independent** rational sequence
```
h_1=1/24,
h_(t+1)/h_t=t^2(6t+1)/((t+1)(2t+1)(3t+2)), t>=1.
```
All quantities displayed at 1<=t<=m have p-unit denominators. Then **for every k individually**
```
c_k = a_k * sum_(t=k+1)^m h_t   (mod p).                   (1)
```
Consequently **for any** function q:{0,...,m-1}->F_p, putting Q_t=sum_(k=0)^(t-1) q(k)a_k,
```
sum_(k=0)^(m-1) q(k)c_k = sum_(t=1)^m h_t Q_t   (mod p). (2)
```
For the frozen signed Clausen triangle (q(k)=1+6k):
```
J_p = sum_(t=1)^m h_t P_t     (mod p).                    (3)
```
There is also an explicit original-index binomial kernel
```
h_t = (-1)^t * C(m,t)/(12*t^2*C(3m,t)*C(4m,t)) (mod p).  (4)
```
The p-indexed Gauss complementary e_r is no longer required to **evaluate this mod-p observer**; its labeled source remains available for independent readback and is necessary at the higher p-adic digit.

## Exact derivation

The already-proved exact finite source recurrence for 1<=k<=m is
```
36k^3*c_k-(2k-1)(3k-2)(3k-1)c_(k-1)
 = -3k*d_k - A*(3k-2m-2)*e_(m+1-k),
A=p(3m+1)d_m, c_m=0.
```
The complementary-top source of the full Laurent equation has support k<=0 and is absent on this strictly positive-k interval. For a prime p=6m+1 the A source vanishes modulo p, while a_k and all stated denominators are units. The defining 216 recurrence yields
```
c_k/a_k - c_(k-1)/a_(k-1)=-d_k/(12*k^2*a_k)=-h_k (mod p).
```
Backward summation from c_m=0 gives (1); finite summation interchange gives (2) and (3). Direct exact Pochhammer expressions give
```
a_t=(1/2)_t(1/3)_t(2/3)_t/(2^t(t!)^3)
d_t=(1/6)_t(1/3)_t/(2^t(t!)^2)
h_t=d_t/(12t^2a_t)=t!(1/6)_t/(12t^2(1/2)_t(2/3)_t).
```
The latter formula proves the **rational** prime-independent recurrence, and h_1=1/24. Reducing (1/6,1/2,2/3) to (-m,-3m,-4m) mod p and expanding falling factorials proves (4). All denominators are p-units because t<=m and 4m<p. This proves the full quantifiers claimed, with no experimental interpolation.

## Frozen mother condition and computational evidence

The previously established exact signed Clausen truncation gives
```
W_p = S_p(S_p+12T_p)-2p^2 J_p (mod p^3).
```
Thus the **remaining**, not yet proved, uniform target W_p=p (mod p^3) on p=13,19 mod24 is equivalent to
```
S_p(S_p+12T_p)=p+2p^2*sum_(t=1)^m h_t P_t (mod p^3).  (5)
```
This original-prefix interface preserves nonzero J_19=6 and J_373=98 mod p and is the appropriate BRC observer after scope-typed first-digit reduction. The full-216 p-unit residual at b83a4371... is an independent original-W readout for the next joint cancellation test. At mod p^2 the A source is generally nonzero (see p19, p373 two-source splits at d45b65a2...), so this finite-field reduction is **not** an instruction to erase p-adic low-endpoint provenance.

The companion standalone Python standard-library checker independently constructs original 216 coefficients, Gauss labeled pairs and the universal recurrence, then verifies every c_k and five observers. Executed: all 148 primes p=6m+1 <=1999; 77 target primes, 22,952 coefficient positions and 740 observer checks. Exact modular arithmetic: zero failures. Samples [p,J,c_0,sum(k*c_k),sum(k^2*c_k)]:
```
[13,0,3,6,6]
[19,6,9,9,0]
[67,44,10,28,8]
[373,98,66,254,277].
```
This numerical check corroborates the algebraic theorem and does not certify (5).

Original same-class native p373 H0/B0 divided-power [X]U mod139129, Frobenius rank/eta/direction, odd Green/Hesse, kappa and independent replication remain NOT_EXECUTED/PENDING_OWNER at https://github.com/awdawmip/enterprise-math/issues/1559. The original Source continuation request onhour11-20261106-1400-exact-research-lane-continuation was reconciled under its original ID after EVENT_COLLECTION_IO and remained QUEUED; no Source CLAIM/open/run/Result granted. The three old staging records remain separate.

Next discriminating scientific action: combine the universal first-digit signed observable (3), the proven p-unit full-216 cubic residual at b83a4371, and the Gauss moments into a finite coupled WZ/adjoint relation for (5). Test the nonzero p19/p373 boundaries before generalizing. Native #1559 remains a separately pending actual original-class experiment; no surrogate counts toward it.
