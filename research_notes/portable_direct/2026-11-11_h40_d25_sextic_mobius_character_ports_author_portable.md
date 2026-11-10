# D25/LIFT: sextic character-sum ports and reciprocal Möbius involution

Date: 2026-11-11. **AUTHOR-PROVED / EXACT FINITE-FIELD IDENTITIES / UNREVIEWED / NOT_ADMITTED.** Author-portable result; not a native Source Task checkpoint, Result, independent review, H0/B0 native Frobenius experiment or UR bundle restoration.

Mother: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` (OPEN); Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin: `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`.

## Exact theorem

For every prime `p=6m+1 >=7`, calculate in `F_p`. Reuse the previously published finite Clausen polynomial and its two distinct observer ports:

```text
K_m(X) = sum_{k=0}^m binom(m,k) binom(2m,k) X^k
A_p = K_m(1/2)
B_p = K_m(1/2) + 6 K_m'(1/2)
D_p = F_p \ {0, -1, -2}
U(t) = (t+1)(t+2)^2 / t                  for t in D_p
chi_6(v) = v^m                           (values in mu_6(F_p))
w(t) = (2-3t)/(t+2)
```

Two **exact equalities** hold for all such primes:

```text
A_p = -2^(-2m) sum_{t in D_p} chi_6(U(t))
B_p = -2^(-2m) sum_{t in D_p} chi_6(U(t)) w(t)
```

Define `T(t)=-2(t+1)/(t+2)`. Then `T` is a Möbius involution on `D_p`, with

```text
T(T(t))=t,     U(T(t))*U(t)=2,     w(T(t))=4t+5.
```

It exchanges `0 <-> -1` and `-2 <-> infinity` in the projective line. Thus, writing `S_+=sum_D chi_6(U(t))` and `S_-=sum_D chi_6(U(t))^(-1)`,

```text
S_+ = chi_6(2) * S_-
sum_D chi_6(U(t))*w(t) = chi_6(2)*sum_D chi_6(U(t))^(-1)*(4t+5).
```

The involution has fixed points `-2 +/- sqrt(2)`, hence exactly 2 affine fixed points if `(2/p)=+1`, and none if `(2/p)=-1`. For either prime class `p=6m+1+4epsilon` with `epsilon in {0,1}`, quadratic reciprocity gives `(-6/p)=(-1)^epsilon*(2/p)`. This aligns the previously observed zero-port selector with the fixed-point splitting and its epsilon correction, while leaving the *universal zero-port vanishing theorem* as an open problem.

## Proof, with the operator preserved

For every nonnegative integer m, coefficient extraction yields
`K_m(X)=[t^m](1+t)^m(1+Xt)^(2m)`. Set `P(t)=(1+t)^m(t+2)^(2m)`. At `X=1/2`,
`A_p=2^(-2m)[t^m]P(t)`.

For every polynomial `R(t)` of degree at most `3m`, the exact finite-field identity is

```text
sum_{t in F_p^*} t^(-m) R(t) = -[t^m]R(t).
```

Indeed `p-1=6m` and the only multiple of `6m` among exponents `r-m` for `0<=r<=3m` is zero at `r=m`. Since `t^(-m)P(t)=U(t)^m` on `F_p^*`, and the latter vanishes at `t=-1,-2`, this proves the first character sum.

Differentiating the coefficient identity gives
`K_m'(1/2)=4m*2^(-2m)[t^m]P(t)*t/(t+2)`.
Thus

```text
B_p = 2^(-2m)[t^m](1+t)^m(t+2)^(2m-1)(t+2+24mt)
    = 2^(-2m)[t^m](1+t)^m(t+2)^(2m-1)(2-3t)   (mod p),
```

since `24m = 4(p-1) = -4 (mod p)`. The final polynomial has degree `3m` and vanishes at `t=-1,-2` for `m>=1`. Apply the same power-sum identity to obtain the weighted formula for B.

Direct rational substitution proves `T^2=id`, `U(T)=2/U` and `w(T)=4t+5`; `T` permutes `D_p`, proving the reciprocal identities. The fixed-point equation is `t^2+4t+2=0`, discriminant 8, giving the splitting statement. For odd p>3, `(-3/p)` is +1 if p=1 (mod 6) and -1 if p=5 (mod 6), so `(-6/p)=(-3/p)(2/p)=(-1)^epsilon(2/p)`.

## Integer verification and precise scope

A separate Python author verifier uses **two independent arithmetic expressions** for the ports: direct binomial sums `sum_k binom(m,k)binom(2m,k)2^(-k)`, with derivative weight `1+12k`; and direct finite-field sextic character sums. Every prime `p=6m+1`, `7<=p<=2500` was checked: **178 primes, 204,412 individual t-involution comparisons, 178 two-port matches**, all pass. It also checks reciprocal sums and fixed-point counts.

Selected exact witnesses `(p; A_p,B_p,(2/p),#fixed)`:

```text
7; 2,0,+1,2
13; 0,6,-1,0
19; 0,12,-1,0
157; 0,80,-1,0
373; 0,171,-1,0
1009; 50,0,+1,2
2089; 2019,0,+1,2
```

The universal identities above are hand-proved; the finite sweep checks their implementation. This result does not duplicate the previously published 3243-prime zero-selector experiment or the earlier Clausen and cubic-carrier theorems. Character-sum method applies here to p≡1 (mod6): for the epsilon=1 branch, `m=(p-5)/6` is not an order-six character exponent.

## Next bounded unit and provenance

Seek an exact T-eigenspace/character cancellation formula retaining the weight `w(t)` that distinguishes A from B; use it to prove or refine the conjectural `(-6/p)` all-prime port selector. Keep distinct the actual frozen Source H0/B0 rank, semilinear direction, normalization eta, kappa and Delta-R work, which is NOT_RUN under this author's native authority.

Read/reconcile old requests first. The latest exact Source continuation `h40-20261111-0544-d25-exact-continuation` is SUCCEEDED but `execution_authorized=false`; own recovery-status read requires `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`. This file is GitHub **author-portable evidence only**, with no live native CLAIM/run. UR V2 original object remains pending at exactly 94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; do not redo its already completed mathematics.
