# D25/LIFT — exact original signed W_p four-band p⁴ jet and reverse-tail endpoint

2026-10-25 | TASK_RESEARCH | AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED. Research logical lane `chatgpt-research-hourly-enterprise-math-20260923`, not the maintenance lane. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, FROZEN SCIENTIFIC SOURCE `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is original signed-scalar arithmetic, **not** native same-original-class CM/divided-power Frobenius or source-native checkpoint.

## Independent next question and inherited input

Consume without recrediting the three-band mod-p³ factorization and original rank valuations in `research_notes/portable_direct/20261025_onhour_d25_original_three_band_frobenius_tail.md` (existing current main). The new question is exact mod-p⁴ continuation of the *untruncated* original signed sum and the genuine fourth rank branch. BRC: `COMPOSE_APPLIED` to source-ranked valuation/branch counts and signed sum observer; Boolean support or positive branch counts are not substituted for signed cancellation. No native BRC implementation is claimed executed.

Let p=6m+1 ≥7 be prime, work over Z_(p), and set

```text
a_n=(6n+1)(1/2)_n(1/3)_n(2/3)_n/(2^n(n!)^3);
W_p=sum_{n=0}^{p-1}a_n;
S={2m,3m,4m}; alpha_(2m)=1/3, alpha_(3m)=1/2, alpha_(4m)=2/3;
E_s(n)=product_{0<=j<n, j!=s}(j-s),   r_n=#{s in S:s<n};
d_n=(6n+1)/(2^n(n!)^3) * product_s E_s(n) * product_{s<n}alpha_s;
L_n=sum_s sum_{j<n,j!=s} alpha_s/(j-s);
S_n=sum_s sum_{j<n,j!=s} alpha_s^2/(j-s)^2;
U_n=sum_s sum_{j<n,j!=s} alpha_s^3/(j-s)^3.
```

Every displayed denominator is a p-unit. In particular `j-s` is nonzero with `|j-s|<p`; do **not** divide by 6n+1, which equals p when n=m.

## Theorem 1: exact four-band jet modulo p⁴

For all 0≤n<p there is an **exact rational identity**

```text
a_n = p^r_n * d_n *
      product_s product_{0<=j<n,j!=s}(1 + p*alpha_s/(j-s)).
```

Therefore, with all band quantities reduced modulo p⁴,

```text
W_p = B0+B1+B2+B3 (mod p^4),
B0=sum_{n=0}^{2m} d_n*
     [1+p*L_n+p^2*(L_n^2-S_n)/2
       +p^3*(L_n^3-3*L_n*S_n+2*U_n)/6],
B1=p*sum_{n=2m+1}^{3m}d_n*
     [1+p*L_n+p^2*(L_n^2-S_n)/2],
B2=p^2*sum_{n=3m+1}^{4m}d_n*(1+p*L_n),
B3=p^3*sum_{n=4m+1}^{6m}d_n.
```

**Proof.** The three exact identities `1/3=-2m+p/3`, `1/2=-3m+p/2`, `2/3=-4m+2p/3` rewrite every original rising factor as `j-s+p alpha_s`. Its sole p-divisible factor in the legal original range is at j=s, which contributes `p alpha_s` if s<n. Extract these factors, leaving precisely the labelled unit product above. Newton identities give its first three elementary symmetric coefficients `L`, `(L²-S)/2`, `(L³-3LS+2U)/6`. Multiplying by p^r_n kills terms of degree ≥4-r_n. The intervals 0..2m, 2m+1..3m, 3m+1..4m and 4m+1..6m partition all original ranks. QED. The fourth interval is absent only at precision p³, not p⁴.

## Theorem 2: exact fourth-branch factorial formula and universal terminal coefficient

For 0≤k≤2m-1, writing n=4m+1+k,

```text
d_n=(-1)^m*(24m+7+6k)/(9*2^(4m+1+k)) *
    (2m)!(3m)!(4m)!(2m+k)!(m+k)!k! / ((4m+1+k)!)^3.
```

Every d_n in this interval is a p-unit. The final coefficient satisfies the **all-prime theorem**

```text
d_(p-1) = 5 (mod p),   for every prime p=6m+1>=7.
```

**Proof.** Each `E_s(n)` with n>s equals `(-1)^s s!(n-1-s)!`. Their product supplies the sign `(-1)^(9m)=(-1)^m`; their alpha product is (1/3)(1/2)(2/3)=1/9. No factorial reaches p. At n=p-1=6m, Fermat and Wilson yield

```text
d_(p-1) = [5*(-1)^m/9] *
          [((2m)!(3m)!(4m)!)^2/(24m^3)] (mod p).
```

Wilson pairing gives `(2m)!(4m)!=-1` and `((3m)!)²=(-1)^(m+1)` mod p. Finally `m=-1/6` implies `24m³=-1/9` mod p, so the expression equals 5. QED.

## Theorem 3: a new finite reverse hypergeometric tail kernel

Put `e_k=d_(p-1-k) (mod p)`. For 0≤k≤2m-2, the exact adjacent factorial quotient reduced modulo p gives

```text
e_0=5,
e_(k+1)/e_k =
  [2*(k+1)^3*(6k+11)]/
  [(6k+5)*(k+1+2/3)*(k+1+1/2)*(k+1+1/3)] (mod p).
```

Equivalently, for 0≤k≤2m-1,

```text
e_k = 5 * (11/6)_k*(1)_k^3 * 2^k /
          [(5/6)_k*(5/3)_k*(3/2)_k*(4/3)_k] (mod p),
B3/p^3 = sum_{k=0}^{2m-1}e_k (mod p).
```

**Proof.** From the exact factorial formula,
`d_(n-1)/d_n = (6n-5)/(6n+1) * 2n³/[(n-1-2m)(n-1-3m)(n-1-4m)]`.
Substitute `n=p-(k+1)`, use `m=-1/6` mod p, and telescope starting from the independently proved endpoint e_0=5. Every denominator is a p-unit throughout the exact window; (4/3)_k acquires a p factor first at k=2m **outside** the window. This is a legal finite kernel, not a claim of infinite hypergeometric termination. QED.

## Finite exact arithmetic witnesses and source information loss

At p=13,m=2, modulo 13⁴=28561,

```text
(B0,B1,B2,B3)=(27144,26104,12675,10985)
W_13=19786; B3/p³=5 mod 13.
```

Thus deleting original ranks 4m+1..6m on the strength of the old p³ truncation is demonstrably invalid at p⁴.

The opposite universal assertion (fourth-band **sum** always nonzero) is false: p=1327,m=221 has 442 **individually nonzero** fourth-band coefficients, including the universal terminal 5, but

```text
(B0,B1,B2,B3)=(714030769304,323940026428,737961320675,0)
W_1327=1775932116407 (mod 1327^4=3100870943041);
sum_{n=885}^{1326}d_n=0 (mod 1327).
```

This finite cancellation is not a counterexample to the target p³ supercongruence. The signed rank observer is not recoverable from positive support alone.

The companion standard-library checker was actually executed on **52 primes** (all 50 p=6m+1 in [7,600), plus 1327 and 19963). It independently reconstructs W_p from original Pochhammer recurrence, all p⁴ bands using the source-parameter jet, and the reverse finite-field kernel; verifies d_(p-1)=5, the p³ relation for this finite sample, and both sides of the p⁴ identity. No all-prime p³ cancellation proof, CM/DP experiment, native BRC execution, mathematical admission or independent Driver review is claimed.

## Exact next action

Seek a signed finite-hypergeometric identity coupling **all four** original branches for the p³ digit of W_p-p, first for p≡13,19 (mod24); do not infer it from 52 examples or the fourth-band reverse kernel alone. The unresolved parent D25/LIFT still needs actual same-prime same-original-class H0/B0, [X]U mod p², Frobenius rank/direction/normalization and native κ/Δ_p−R_p correspondence. Frozen scientific Source pin stays unchanged; GitHub portable evidence is not itself a native Source checkpoint.
