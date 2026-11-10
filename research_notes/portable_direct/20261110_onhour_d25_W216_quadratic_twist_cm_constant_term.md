# D25 / W216 — quadratic-twist constant-term certificate for the missing CM root

**Date:** 2026-11-10 (Asia/Hong_Kong). **Status:** AUTHOR_SIDE / EXACT ALGEBRAIC REDUCTION / FINITE EXPERIMENT / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.

**Parent Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; Publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific input: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research provenance: `chatgpt-research-onhour-enterprise-math-20260923`, **not** the separate maintenance lane. The mathematical unit below is an author-side continuation and is not a Source-native CLAIM, checkpoint, or proof of the entire LIFT.

## 1. Exact target and consumed input

Let `p=6m+1>3` be prime, with `p=13 or 19 (mod 24)`; equivalently, within `p≡1 (mod6)`, the Legendre symbol `(2/p)=-1`. Work entirely in `F_p` and use p-unit denominators. Define the *unchanged original* Clausen coefficient and sum

```text
B_k = (1/6)_k (1/3)_k / (2^k (k!)^2)    (0<=k<p),
J_p = sum_{k=0}^{p-1} B_k.
```

The preceding unit established that `F0 = J_p² (mod p²)`, a typed first unsigned/signed cutoff, and conditional LIFT identity `(W_p-p)/p² = tau+j²-R_p (mod p)` when `J_p=0 (modp)` and `W_p=p (mod p²)`. Its exact source is `research_notes/portable_direct/20261110_onhour_d25_W216_unsigned_Clausen_square_firstjet_bridge.md`. The smallest unproved CM dependency is a *uniform* demonstration of `J_p=0 (mod p)` for both target residue classes. We construct a different, explicit finite-field representation of this exact dependency.

## 2. Theorem: involution, quadratic character, and Laurent constant term

Write `chi(z)=(z/p)` with `chi(0)=0`. Let `D_n(u,1/2)` be the Dickson power-sum polynomial over `F_p` defined by

```text
D_0(u,1/2)=2;  D_1(u,1/2)=u;
D_n(u,1/2)=u D_(n-1)(u,1/2)-(1/2)D_(n-2)(u,1/2).
```

For `v≠3`, define

```text
t=v-3;
u(v) = (2v³-8v²+v+16) / (2(v-3)²)
     = t+5+7/(2t)+1/(2t²).
C_m = CT_t D_m(t+5+7/(2t)+1/(2t²), 1/2)  in F_p,
T_p = sum_(v in F_p, v!=3) chi(v²-8) D_m(u(v),1/2).
```

Here `CT` extracts the coefficient of `t^0` in an explicit finite Laurent polynomial. **Theorem (all p in the stated target classes):**

```text
J_p = 2^(-m-1) ( C_m - T_p )  (mod p).
```

Consequently the *original* CM first-digit obligation `J_p=0 (mod p)` is exactly equivalent to

```text
T_p = C_m  (mod p), for p=13 or 19 (mod24).
```

This character-twist/constant-term equality is an explicit open arithmetic target, not a proved all-prime cancellation.

### Proof

**Coefficient and constant-term realization.** Because `p=6m+1`, `1/6=-m (modp)`, `1/3=-2m (modp)`. For `0<=k<=m`,

```text
B_k = binom(m,k) binom(2m,k) 2^(-k) (modp);
B_k=0 (modp),  m<k<p.
```

Thus, for the Laurent polynomial `f(x)^m=(x+1)^(2m)(x+2)^m/x^(2m)`,

```text
J_p = 2^(-m) CT_x f(x)^m   (modp).
```

Its exponent support is `[-2m,m]`, strictly contained in `(-(p-1),p-1)`. Exact finite-field power-sum orthogonality yields

```text
sum_(x in F_p^×) f(x)^m = - CT_x f(x)^m.
```

The terms at `x=-1,-2` vanish. Consequently, with `X=F_p\{0,-1,-2}`,

```text
J_p = - 2^(-m) sum_(x in X) f(x)^m.
```

**Nontrivial BRC-type two-branch involution.** Set `w=x+2`, so `w∈F_p\{0,1,2}`. The exact order-two rational operation

```text
w ↦ 2/w, equivalent to x ↦ -2(x+1)/(x+2)
```

preserves the regular domain, and

```text
f(w)=w(w-1)²/(w-2)²,
f(2/w) = 1/(2 f(w)).
```

A fixed point would solve `w²=2`; none exists because `chi(2)=-1`. Thus the regular domain has exactly `(p-3)/2` unordered pairs. Define the pair readout `v=w+2/w`. Its two preimages, when they exist, have discriminant `v²-8`. The excluded value `v=3` corresponds to `w=1,2`. Under `chi(2)=-1`, `v²-8` is never zero, so for each `v≠3` the number of regular `w` is `1+chi(v²-8)`, either 0 or 2.

The two `f`-values of a pair have product `1/2` and sum `u(v)` as given above (verify the rational substitution directly). By the Dickson recurrence their m-th power sum is `D_m(u(v),1/2)`. Hence

```text
sum_(x in X) f(x)^m =
sum_(v≠3) [1+chi(v²-8)] D_m(u(v),1/2) = A_p+T_p,
A_p:=sum_(v≠3) D_m(u(v),1/2).
```

**Untwisted term has an exact CT certificate.** Replace `v=3+t`; the Dickson polynomial is a Laurent polynomial with exponents in `[-2m,m]`. Therefore the same field-power-sum identity gives

```text
A_p = sum_(t in F_p^×) D_m(t+5+7/(2t)+1/(2t²),1/2) = - C_m.
```

Substitution into `J_p=-2^(-m)(A_p+T_p)` proves the theorem. QED.

## 3. Nontrivial signed-branch cancellation and finite checks

This orbit decomposition is not a pointwise-vanishing trick: for `p=13,m=2,v=5`, `u(v)=4`, so `D_2(4,1/2)=4²-1=2 (mod13)`. Individual orbit contributions survive. The exact CM obligation is the **global equality** of the quadratic-twist sum and the Laurent constant term.

A standalone standard-library exact verifier is provided as `research_notes/portable_direct/d25_w216_quadratic_twist_cm_20261110.py`. It checks independent residues from (i) the original finite binomial coefficient, (ii) rational `x`-sum, (iii) pairwise character-twist/Dickson `v`-sum, and (iv) an independent Laurent constant-term recurrence, including proper support and `v=3` exclusion.

Initial exact computations: all **45** eligible primes `p<=1000, p=13 or 19 (mod24)`, plus larger `10069,10099` (**47 prime certificates**), satisfy the proved three-way identities. In all 47 examples, `J_p=0`, hence `T_p=C_m`; this is computational evidence for the unresolved uniform CM claim.

| p | m | J mod p | untwisted A_p | character-twist T_p | CT C_m | regular orbit count |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 2 | 0 | 8 | 5 | 5 | 5 |
| 19 | 3 | 0 | 4 | 15 | 15 | 8 |
| 37 | 6 | 0 | 14 | 23 | 23 | 17 |
| 43 | 7 | 0 | 8 | 35 | 35 | 20 |
| 373 | 62 | 0 | 96 | 277 | 277 | 185 |
| 997 | 166 | 0 | 921 | 76 | 76 | 497 |
| 10069 | 1678 | 0 | 4180 | 5889 | 5889 | 5033 |
| 10099 | 1683 | 0 | 10084 | 15 | 15 | 5048 |

The untwisted `A_p=-C_m (modp)`, and the two nonzero terms cancel in these examples. Scalar finite checks are not native crystalline H0/B0 data.

## 4. BRC / observer scope / next exact scientific actions

**BRC resolution:** `COMPOSE_APPLIED`. Population: all regular x with their ordered original B-coefficient ancestry; invertible branch transformation `w↔2/w`; branch pair invariant `v`; twist `chi(v²-8)` and Dickson sum; the unsigned `C_m` and character-signed `T_p` are separately retained. Future operations allowed: evaluation of `J modp` and its precise implication for the preceding Clausen-square lemma. This certification **does not** authorize projecting away original higher p-adic jets, ordered signed cutoff `R_p`, odd Green/Hesse provenance, or native Frobenius.

**Next portable action:** seek a *uniform exact proof or a valid same-object counterexample* of `T_p=C_m (modp)` for both target classes; investigate a finite Jacobi character-sum transformation for `chi(v²-8)`, keeping the discriminant and Laurent denominator. If established, combine it with prior `F0=J² (modp²)`; then address the separate signed first-jet `tau+j²=R_p` and `W=p (modp²)`.

**Highest native evidence欠项:** same-original-class p=373 H0/B0 divided-power `[X]U mod139129`, module rank, semilinear Frobenius direction, normalization eta, odd signed kappa, original Delta-R and independent replica. Existing support ticket #1559 at `https://github.com/awdawmip/enterprise-math/issues/1559` was OPEN without a confirmed owner at the 2026-11-10 18:25 +0800 read. This exact original experiment remains `NOT_RUN / PENDING_OWNER`. The ordinary finite-field theorem is not substituted for that experiment.

**Source/control:** Previous read `onhour11-20261110-1658-exact-cont-after-unit` is `SUCCEEDED`. The latest read `onhour11-20261110-1825-cont-read` was `QUEUED` on first poll, must be read/reconciled by original request ID. Historical Researcher session `MCP-5378d3819d8947bda9049c9428493e2d` exists but own private session capability is absent (`SESSION_CAPABILITY_REQUIRED`); no live winning CLAIM/run, native task publication or Result is declared. This research note only is author-side durable evidence.

**Mathematical status:** the involution, rational trace, Dickson-twist identity and CT bridge are proved for all target primes. Uniform CM cancellation, original LIFT and native H0/B0 evidence are open, with their original objects and pins preserved.
