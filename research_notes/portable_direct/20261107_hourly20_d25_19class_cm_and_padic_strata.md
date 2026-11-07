# D25: 19-class CM/Hasse closure and three-level p-adic Gauss source lift (2026-11-07)

**Status:** AUTHOR-SIDE PROVED ALGEBRA WITH EXTERNAL CM/DEURING INPUT; exact finite regression; UNREVIEWED / NOT_ADMITTED. No native checkpoint, Review or Result asserted.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is a continuation of the 2026-11-07 fourth Fricke jet, especially its previously *conditional* 19-class root, and reuses the already proved 13-class CM calculation. Classical elliptic/CM arithmetic is an external auxiliary model, not a new Enterprise native-world axiom.

## Theorem A — universal 19-class root, and split-class complement

For **every rational prime** `p=8k+3>3`, let
`H_k(w)=sum_{j=0}^k binom(3k+1,j)binom(k,j)w^j` over `F_p`.
Then

```
H_k(1/9)=0 (mod p)   iff   p = 19 (mod 24).
H_k(1/9)!=0 (mod p)  iff   p = 11 (mod 24).
```

For every `p=19 (mod 24)`, the zero is **simple**: `H_k'(1/9)!=0`. This discharges the universal root hypothesis left open in the fourth-jet note. Its 19-class derivative/Fricke formulas therefore hold without that former root condition (subject to their independently stated CM0 and Fricke inputs).

### Lemma A1: exact polynomial quadratic transform

Put `d=2k=(p-3)/4` and

```
L_d(u)=sum_{j=0}^d binom(3d+2,j)binom(d,j)u^j.
```

In `F_p[u]` there is an **exact polynomial identity**

```
H_k(4u(1-u)) = L_d(u).                  (A1)
```

Proof: Gauss's classical formal-power-series quadratic identity gives
`2F1(1/8,3/8;1;4u(1-u))=2F1(1/4,3/4;1;u)`.
For `p=8k+3`, the Gauss coefficients on the left terminate modulo `p` at `j=k`, because `3/8+k=p/8`; the coefficients on the right terminate at `j=d`, because `3/4+d=p/4`. For `n<p`, all factorial denominators are units. The coefficients of both sides through `u^d` therefore agree after reduction. Both reduced polynomials have degree at most `d=2k<p`, so they are equal, not just congruent modulo `u^{d+1}`. In particular, unlike the earlier `p=8k+5` transform, (A1) has **no** extra `(1-2u)^p` factor.

### Lemma A2: Hasse invariant with the correct negative sign

For `u != 0,1` consider `E_u:y^2=x((x+1)^2-u)`. Set `N=(p-1)/2=2d+1`. Its Hasse coefficient is

```
A_p(u)=[x^(p-1)](x((x+1)^2-u))^N
      =sum_{j=0}^d (-u)^j binom(N,j)binom(2N-2j,N).
```

The constant term `binom(p-1,N)=(-1)^N=-1 (mod p)`. Consecutive coefficient ratios are `(j+1/4)(j+3/4)/(j+1)^2`, for `0<=j<d`. They match `L_d`, whose constant coefficient is one. Consequently

```
A_p(u) = -L_d(u)   in F_p[u].           (A2)
```

The sign is different from the `p=5(mod8)` case, where `N` was even; the zero sets agree.

### Lemma A3: CM classification and the value at 1/9

Use the two separately retained quadratic source branches
`u_+=(3+2sqrt(2))/6` and `u_-=(3-2sqrt(2))/6`.
They satisfy `4u_±(1-u_±)=1/9`, and `u_+u_-=1/36`.
Their elliptic curves have good reduction for every `p>3`, since the discriminant is `64u(1-u)^2`.

Their `j` invariants are `2417472 ± 1707264sqrt(2)`, the two roots of the discriminant-`-24` Hilbert class polynomial
`X^2-4834944X+14670139392`. This CM identification, already checked in the preceding 13-class paper, gives imaginary CM field `Q(sqrt(-6))`. Deuring's good-reduction CM criterion makes the Hasse invariant zero exactly at inert primes in that CM field (for the present `p>3`, ramified primes are absent). Within `p=3(mod8)`, quadratic reciprocity yields `(-6/p)=-1` precisely for `p=19(mod24)`, and `+1` for `p=11(mod24)`.

Apply (A1) and (A2) at either `u_±`; the vanishing of `H_k(1/9)` is equivalent to supersingularity. This proves Theorem A. The two branches lie in `F_(p^2)` because `(2/p)=-1`, and are swapped by Frobenius: `u_+^p=u_-`.

### Lemma A4: the first derivative and signed branch invariant

The polynomial `H_k` satisfies the Gauss ODE
`w(1-w)H''+(1-3w/2)H'-(3/64)H=0` in `F_p[w]`.
At an ordinary point `w0=1/9`, a double zero would, by successive derivatives and `deg H=k<p`, force `H` identically zero, contradicting `H(0)=1`. Thus the zero in the 19-class is simple.

Differentiating (A1), without identifying the branches, gives

```
L_d'(u_±) = 4(1-2u_±) H_k'(1/9)
          = ∓(8sqrt(2)/3) H_k'(1/9).
Tr(L_d'(u_±))=0,  Norm(L_d'(u_±))=-(128/9) H_k'(1/9)^2 !=0.     (A3)
```

Here Tr/Norm are relative to `F_(p^2)/F_p`. The nonzero opposite branch derivatives record signed source information despite their common scalar observation `H_k(1/9)=0`. This is an exact typed BRC / observer-preservation application.

## Theorem B — p-adic three-stratum Gauss coefficient reconstruction

For the **same** `p=8k+3>3`, put `a=3k+1`,
`g_n=(1/8)_n(3/8)_n/(n!)^2` (`0<=n<p`).
The exact valuation partition, with no cancellation at individual coefficient level, is

```
v_p(g_n)=0    for 0<=n<=k,              L port;
v_p(g_n)=1    for k<n<=a,               M port;
v_p(g_n)=2    for a<n<p,                U port.
```

These are 0,1,2 because the single numerator roots modulo `p` occur at `j=k` in `(3/8)_n` and at `j=a` in `(1/8)_n`, with unit denominator for `n<p`.

All formulas below are in `Z_(p)` and read modulo the displayed powers of `p`. Define `H_t^(r)=sum_{j=1}^t j^{-r}`, `H_t=H_t^(1)`, and `H_0^(r)=0`.

**L port `0<=n<=k`.** Let `h_n=binom(a,n)binom(k,n)`,
`A=H_a-H_(a-n)`, `B=H_k-H_(k-n)`,
`A2=H_a^(2)-H_(a-n)^(2)`, `B2=H_k^(2)-H_(k-n)^(2)`.
With `U_L=-(3A+B)/8`, `V_L=(9A2+B2)/64`,

```
g_n = h_n [1+p U_L + (p^2/2)(U_L^2-V_L)]  (mod p^3).         (B1)
```

**M port `k<n<=a`.** Put
`M_n=(-1)^(n+k) a! k! (n-k-1)! /[8(a-n)!(n!)^2]`,
`U_M=(-3(H_a-H_(a-n)) + H_(n-k-1)-H_k)/8`. Then

```
g_n = p M_n(1+p U_M)                      (mod p^3).         (B2)
```

**U port `a<n<p`.** Put
`N_n=-3a!k!(n-a-1)!(n-k-1)!/[64(n!)^2]` (the sign uses `a+k=4k+1` odd). Then

```
g_n = p^2 N_n                              (mod p^3).       (B3)
```

Proof: substitute `1/8=-a+3p/8`, `3/8=-k+p/8` into the products. In L, both base products are units and the quadratic elementary symmetric expansion gives (B1). In M, pull out the unique `p/8` factor from the `j=k` port and expand remaining unit factors to order `p` to get (B2). In U, also pull out the unique `3p/8` from the `j=a` port; the remaining product yields (B3). No analytic approximation is used.

## Theorem C — carry-preserving Clausen projection modulo p³

Write `g(w)=L(w)+M(w)+U(w)`, with the three coefficient-index ranges from Theorem B, each reconstructed modulo `p^3`. Let `pi_<p` discard degrees `>=p`. Clausen's exact rational coefficient identity, reduced modulo `p^3`, gives

```
B_<p(w) = pi_<p[ L^2 + 2LM + M^2 + 2LU ] (mod p^3),        (C1)
B_<p(w) = sum_(n=0)^(p-1) ((1/4)_n(1/2)_n(3/4)_n/(n!)^3) w^n.
```

The dropped `MU,U^2` source pairs have valuations at least 3 and 4 respectively. The `pi_<p` operation is essential: evaluating the full Cauchy product first merges terms from `n>=p` that the original finite sum excludes. The original 2304 observer is `(1+8w d/dw)B_<p(w)` at `w=1/9`. This supplies a source-indexed, mod-`p^3` input for the next Fricke transfer problem; it does not by itself identify the separately normalized 216 weighted sum.

## Exact arithmetic, scope, and frontier

Standard-library verifier `d25_19class_cm_hasse_bridge_20261107.py` passed all **167 primes `p<5000, p=3(mod8)`**: 84 split-class `p=11(mod24)`, 83 inert-class `p=19(mod24)`; tests included the **whole polynomial** (A1), the signed Hasse polynomial (A2), both `F_(p²)` branches, root classification and simple roots. Witnesses: `p=11: H=10`; `p=19: H=0,H'=6`; `p=43: H=0,H'=5`; `p=67: H=0,H'=47`.

Second standard-library verifier `d25_19class_padic_strata_20261107.py` passed **21 separate primes `p=3(mod8),11<=p<=491`**, checking **every `0<=n<p`** against the raw rational hypergeometric recurrence modulo `p^3`, each claimed valuation, and the source-filtered Clausen Cauchy convolution against the direct independent `3F2` recurrence modulo `p^3`. Example `p=19`: `g_2=4999, g_3=1672, g_7=4959, g_8=6498` in `Z/(19^3)`.

Dependency: Gauss quadratic transform (DLMF §15.8), the `-24` CM j polynomial and Deuring theorem from the prior CM/Hasse dossier (with cited external sources). Independent mathematical review and native task admission remain pending.

**Next exact science unit:** combine (C1) with the existing signed fourth Fricke jets; compute the first `p`- and `p²`-normalized defect in the comparison with the 216 source partition, keeping the signed `u_±` branch labels and `n>=p` Cauchy cutoff separately. Seek a telescoping certificate for the resulting defect for `p=19,43,67` before generalization. The mother target `Delta_p-R_p=0(mod p), p=13,19(mod24)` stays open.

**Native control:** `em_status` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false` on this turn; Researcher session/claim/run/staging from historical lane remains UNKNOWN/PRESERVE, and previous request IDs `em-h20-20261106-1324-d25-task-r13`, `em-h20-20261106-1324-d25-cont-r13` must not be replayed. Research registration remains `REGISTER_PENDING` with support issue `enterprise-math#1558`. No identity takeover, native checkpoint, Result/freeze/review/admission claimed.
