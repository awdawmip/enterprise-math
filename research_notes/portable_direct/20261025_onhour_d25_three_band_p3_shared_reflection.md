# D25 / SECOND-DIGIT-LIFT — complete p^3 Clausen polynomial jet and shared reflection

2026-10-25. **AUTHOR_EXACT_DERIVATION / EXACT_CHECKS_PASSED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Neutral author-side evidence; not a Source-native checkpoint/Result/review/benchmark. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research lane `chatgpt-research-onhour-enterprise-math-20260923` is distinct from maintenance lane `chatgpt-hourly-enterprise-math-20260921`.

## New Theorem A — every coefficient to third p-adic digit

For every prime p=6m+1>=7, define
`r_n=(1/6)_n(1/3)_n/(2^n(n!)^2)=product_{i<n}(6i+1)(3i+1)/(36(i+1)^2)`, 0<=n<p, and `M_p(z)=sum_{n<p}r_n z^n`.
For 0<=n<=m let
`b_n=2^{-n}binom(m,n)binom(2m,n)`,
`e_n=-(H_m-H_{m-n})/6-(H_{2m}-H_{2m-n})/3`,
`sigma_n=(H_m^(2)-H_{m-n}^(2))/36+(H_{2m}^(2)-H_{2m-n}^(2))/9`, and `f_n=(e_n^2-sigma_n)/2`.

For the middle band m+1<=n<=2m define
`h_(m+1)=b_m(3m+1)/(36(m+1)^2)`,
`h_(n+1)=h_n[-(n-m)(2m-n)/(2(n+1)^2)]` for n<2m, and
`epsilon_n=e_m+sum_(i=m+1)^(n-1)[1/(6(i-m))-1/(3(2m-i))]`.
For the high band 2m+1<=n<p define
`g_(2m+1)=h_(2m)(12m+1)/(36(2m+1)^2)`,
`g_(n+1)=g_n(n-m)(n-2m)/(2(n+1)^2)` for n<p-1.

**Unconditional polynomial congruence in Z_(p)[z]:**

```
M_p(z) = B_m(z) + p E_m(z) + p^2 F_m(z)  (mod p^3)
B_m(z) = sum_(n=0)^m b_n z^n
E_m(z) = sum_(n=0)^m b_n e_n z^n + sum_(n=m+1)^(2m) h_n z^n
F_m(z) = sum_(n=0)^m b_n f_n z^n
       + sum_(n=m+1)^(2m) h_n epsilon_n z^n
       + sum_(n=2m+1)^(p-1) g_n z^n.
```

**Proof:** At ranks n<=m, factor each (6i+1)(3i+1) against the binomial factor as
`(1-p/[6(m-i)])(1-p/[3(2m-i)])`; expanding the finite product to degree 2 gives e and f. The numerator at i=m contributes exactly one p, with remaining units factoring as
`-[(i-m)(2m-i)/(2(i+1)^2)](1+p/[6(i-m)])(1-p/[3(2m-i)])`.
This yields `r_n=p h_n(1+p epsilon_n) mod p^3` for m<n<=2m. At i=2m a second factor p occurs, and every later multiplier has p-unit denominator, yielding `r_n=p^2g_n mod p^3` for 2m<n<p. These are the complete disjoint rank intervals. All denominators displayed are p-units on their **stated** intervals. Each coefficient is proved; no target LIFT conjecture or finite test is used.

## New Theorem B — one maximal reflected carrier for high-band and cutoff

The previously proved exact rational Clausen identity is
`W_p=M_p(1)[M_p(1)+12N_p]-p^2 T_p (mod p^3)`,
where `N_p=(z d/dz M_p)(1)` and the reflected truncated convolution corner uses `v_h=r_(p-h)/p^2` for h<=m, with `v_1=1/10 mod p` (earlier author proof commit `cefbad99f03e3b79e0cfc9de624481ed2010ae40`).

The same v_h admits the **maximal safe extension 1<=h<=4m**, precisely the full high-rank n=p-h band:
```
v_1 = 10^(-1) (mod p)
v_(h+1) = v_h * 36 h^2 / ((6h+5)(3h+2)) (mod p), 1<=h<4m.
```
Proof: invert the original rank ratio with n=p-h. The denominator is a unit on 1<=h<4m; at h=4m the factor 3h+2=2p is nonunit, marking the genuine high-to-middle crossing. The recurrence is **not** extended across that point.

Put `G=sum_(n=2m+1)^(p-1)g_n`, `B1=sum_(j=0)^m j b_j`, and `S_h=sum_(j=h)^m b_j[6(j-h)+1]` for 1<=h<=m, S_h=0 for m<h<=4m. Reversing the finite old corner sum and using r_j=b_j mod p on j<=m proves
```
G = sum_(h=1)^(4m) v_h (mod p)
T_p = 2 sum_(h=1)^m v_h S_h (mod p)
C_p := 12 B1 G - T_p = 2 sum_(h=1)^(4m) v_h(6 B1-S_h) (mod p).
```
C is a **signed joint observer**, not a theorem that high ranks disappear: at p=19, G=10, T=12, B1=1, hence C=13 mod19 (nonzero).

## Exact open third-digit observer and non-admission boundary

Let `B0=B_m(1)`, `E0=E_m(1)`, `E1=(z d/dz E_m)(1)`, and `F_LM=sum_low b_n f_n +sum_middle h_n epsilon_n`. Theorem A implies unconditionally
`M_p(1)=B0+p E0+p^2(F_LM+G) mod p^3` and `N_p=B1+p E1 mod p^2`.
**Conditionally**, if the still-open target-class Legendre zero `B0=0 mod p` is proved, put `U0=B0/p+E0`. With the inherited accepted first-digit input `W_p=p mod p^2`, `12U0B1=1 mod p`, and the complete residual becomes
```
(W_p-p)/p^2 = J_p (mod p),
J_p = (12U0 B1-1)/p
    + 12B1 F_LM
    + 12U0 E1 + U0^2
    + C_p  (mod p).
```
The first quotient is p-integral under that explicit input. This reduces JT2 exactly to proving the *all-target* Legendre zero and J_p=0, or identifying a genuine counterexample. No independent proof of either was produced here. The original frozen taskbook `R_p` is **not** the Clausen M_p; the final Source `Delta_p-R_p` equivalence and native benchmark remain pending.

**Verification actually executed:** exact modular implementations rederive *every one of p coefficients* of M_p(z) for all 94 primes p<=1200 with p=1 mod6 and additional p=19963, compare independent N_p and original W_p modulo p^3, and check the common v_h and joint C_p. For 15 small primes an independent O(p^2) direct double cutoff sum was checked. 53 target primes passed B0=0 and J_p=0 **as finite tests only**. Examples (p:G,T,C,J): (13:8,0,9,0); (19:10,12,13,0); (211:130,119,202,0); (19963:7392,13363,14014,0). This is author-side Python exact arithmetic, **not** the original Source-native benchmark.

**BRC applied:** retained rank n and reflected h as branch identities, p-valuations 0/1/2, two crossing ports, the e/f/epsilon jets, and the signed downstream (M,N,Q,W) observer. Common v_h is proved lossless for only the high/corner projection: `COMPOSE_APPLIED`, not a new native BRC tool or positive-weight cancellation. The variable z is a formal external generating coordinate, not P000 physical space. Frozen six-native-axis P000 and current ACTIVE worldview remain unchanged.

**Operational evidence:** attempted current native continuation/task reads returned `CONTROL_QUOTA`; Site scope is read-only and no Researcher session key/claim/run or native checkpoint was obtained. Own recovery_status is not callable in the exposed connector. Support owner: issue #1539; write relay/credential configuration requires the original authorized service path and verification, not maintenance identity borrowing. This author note must not be promoted into an admitted Result. Next scientific action: exploit the unified C_p and F_LM/U0 derivative terms to find a global telescoper or counterexample, and independently prove the target Legendre zero, then validate the frozen native Delta_p-R_p/benchmark obligations.
