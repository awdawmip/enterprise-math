# D25/LIFT GH-11 and GH-12 — finite-field Gosper pole-orbit and finite-window certificate complexity

Date: 2026-10-28 Asia/Hong_Kong. Task lane: `chatgpt-research-hourly-enterprise-math-20260923`. Parent task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT` (D25/LIFT/JT2, OPEN at last authenticated continuation). Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged.

**Claim status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. GH-3 through GH-10 supply the original, unchanged hypergeometric auxiliary carrier and its labelled S MM/LH source reduction; this note consumes that input without recrediting it. All claims concern an auxiliary scalar coefficient index, not native X6 spatial transport or a proof of the W/S supercongruence.

## Exact rank carrier

For every prime `p >= 5`, set `d = floor((p-1)/4)` and consider

```text
C_0 = 1,
C_{r+1}/C_r = A(r)/B(r),
A(x) = 9(4x+1)^3,
B(x) = (4x+2)(4x+3)(4x+4).
```

Thus `C_r = 9^r (1/4)_r^3/[(1/2)_r(3/4)_r r!]`. Each `C_0,...,C_d` is a `p`-adic unit (not the generally singular subsequent `C_{d+1}`). The frozen GH-3 obligation for `p = 19 (mod 24)`, with `d=(p-3)/4`, is `T_p = sum_{r=0}^d (8r+1) C_r = 0 (mod p)`. Its reduction of the distinct original S source ports is `G_MM=-beta_b^2 T_p`, `G_LH=+beta_b^2 T_p`. The port labels and the finite cutoff remain part of the parent claim.

## GH-11 — global prime-dependent rational certificates have growing denominator cost

**Theorem GH11.1 (pole-orbit bound).** For any `p >= 5`, a rational function `R(x)=P(x)/Q(x)` over `F_p(x)`, written in lowest terms, that obeys the *global polynomial identity*

```text
A(x) R(x+1) - B(x) R(x) = B(x)(8x+1)
```

has `deg Q >= d`. In particular, no polynomial solution exists, and no fixed denominator degree can work uniformly in `p`. The coefficients of `R` are allowed to depend on `p`: this goes beyond GH-7's characteristic-zero obstruction.

**Proof.** If `R` is polynomial of degree `m`, its left side has degree `m+3` with leading coefficient `512 lc(R)`, whereas the right side has degree `4`. Since `512 != 0` in `F_p`, necessarily `m=1`. Comparing degrees four and three in the identity forces `R=x+11/16`. The remaining exact defect, left minus right, is

```text
-9(608x^2 + 356x + 45)/16.
```

It remains a nonzero polynomial modulo every `p>=5`, because `gcd(608,356,45)=1`.

Now suppose `R` has poles over an algebraic closure of `F_p`. Translation by `1` partitions poles into cyclic orbits of length `p`. If one such entire orbit is occupied, `deg Q>=p>=d`. Otherwise choose a maximal non-cyclic consecutive run of poles in one orbit, beginning at `z` and ending at `w` in positive translation order. At `x=z-1`, only `A(x)R(x+1)` can have a pole, so `A(z-1)=0`, giving `z=3/4`. At `x=w`, only `-B(x)R(x)` can have a pole, hence `B(w)=0`, giving `w` among `-1/2,-3/4,-1`. For `p=4d+1`, their smallest forward distance from `3/4` is `d-1` (ending at `-1/2`); for `p=4d+3`, the smallest is `d-1` (ending at `-1`). The run therefore contains at least `d` different poles, counted without multiplicity; `deg Q>=d`. QED.

This is a lower bound on *global* rational telescoping over `F_p(x)` only. It does not preclude a local finite-window solution of complexity depending on `p`, creative telescoping with additional source dimensions, finite-field character sums, or other nonlocal WZ relations.

## GH-12 — finite-window complexity and exact existence of rank-polynomial certificates

**Theorem GH12.1 (finite-window complexity).** Let `R=P/Q` be rational over `F_p(x)`, with reduced degrees `m=deg P`, `n=deg Q`, and `Q(r)Q(r+1)!=0` at all `r=0,...,d-1`. If

```text
A(r) R(r+1) - B(r) R(r) = B(r)(8r+1)
```

holds on each of those `d` ranks, then

```text
max(m+n+3, 2n+4) >= d.
```

In particular, for polynomial certificates and `d>4`, `m>=d-3`. So bounded-degree, prime-dependent rational expressions of bounded numerator and denominator complexity cannot certify all growing finite windows.

**Proof.** Clearing denominators yields

```text
H(x) = A(x)P(x+1)Q(x) - B(x)P(x)Q(x+1)
       - B(x)(8x+1)Q(x)Q(x+1).
```

Its degree is at most `max(m+n+3,2n+4)`. If that maximum were `<d`, the `d` distinct verified roots `0,...,d-1` would force `H=0` identically. But then `R` is a global rational solution with `n<d`, contradicting GH11.1. QED.

**Theorem GH12.2 (constructive certificate and leading coefficient).** Put `c_k=C_k (mod p)` for `0<=k<=d`, and `S_k=sum_{j=0}^{k-1}(8j+1)c_j` with `S_0=0`. For any `lambda in F_p`, define

```text
R_lambda(k) = (lambda + S_k)/c_k   (k=0,...,d).
```

These `d+1` observations admit a *unique* interpolating polynomial of degree at most `d`. At all `r<d`, it satisfies the rank-local telescope `c_{r+1}R_lambda(r+1)-c_rR_lambda(r)=(8r+1)c_r`. The true finite endpoint identity is

```text
T_p = (R_lambda(d)+8d+1)c_d - lambda   (mod p).
```

Do not drop either endpoint or infer `T_p=0` from the existence of the interpolation alone.

Let

```text
V_p = sum_{k=0}^d (-1)^(d-k) binom(d,k)/c_k,
U_p = sum_{k=0}^d (-1)^(d-k) binom(d,k) S_k/c_k.
```

The polynomial's leading coefficient is `(U_p+lambda V_p)/d!`. If `V_p!=0`, the unique choice `lambda=-U_p/V_p` gives degree at most `d-1`; if `V_p=0, U_p!=0`, every `lambda` forces degree exactly `d`; if both vanish, every `lambda` gives degree at most `d-1`. The final situation may exhibit further descent for special `lambda`, but none is assumed generally. This exact finite-difference criterion is a provenance-preserving observer on `(c_0,...,c_d;S_0,...,S_d;lambda)`.

**Proof.** Every `c_k` is nonzero and `d<p`, so ordinary Lagrange interpolation and Newton finite differences are valid over `F_p`. The defining relation gives the recurrence by subtraction of consecutive partial sums and the exact endpoint by adding the `k=d` term. For a degree-`<=d` interpolant the `d`-th forward difference at zero equals `d!` times the leading coefficient, hence the displayed `U_p,V_p` formula. QED.

## Exact finite checks, scope and next operation

The companion standard-library Python checker actually executed: exact rational source recurrence at 40 ranks; exact integer polynomial-defect identity at 4 values for every prime `5<=p<5000`; exact finite-field pole-orbit distances for the same primes; 301 primes `5<=p<2000` for all finite-window telescopes, leading finite-difference certificates and endpoint identities. All assertions passed.

Witnesses `(p,d,U,V,lambda,interpolation degree)`: `(5,1,1,0,0,1)`, `(7,1,5,4,4,0)`, `(19,4,0,0,0,3)`, `(23,5,2,11,4,4)`, `(43,10,9,2,17,9)`, `(191,47,164,0,0,47)`. At `p=19`, the distinct choice `lambda=6` gives the **constant polynomial 6**, showing a small-prime exception to any blanket degree lower bound stronger than GH12.1. All 301 tested `T_p` vanish modulo `p`; this is **finite observation**, not universal proof. In particular, the `p=191` forced maximum-degree finite-window certificate is a precise information-cost witness, not a counterexample to `T_p=0`.

BRC usage: `REUSE_APPLIED` to GH-3 ordered rational rank/valuation carrier, with observer `T_p`, provenance-labelled MM/LH parent sources and intended future summation and next-digit lift. GH11/GH12 retain source order and end-rank contributions; observing only the interpolation existence would erase the original boundary datum. The auxiliary rank index is neither a spatial axis nor an embedding of the Heartbeat World six-dimensional X6 state. No P000 modification is made.

Next exact math unit: seek a source-faithful finite-field character-sum symmetry or genuinely multi-rank / p-parameter WZ relation that enforces the **endpoint identity**, rather than a uniform low-complexity rational single-term antiderivative. Reuse GH-10's two distinct mod-`p^2` harmonic moments and GH-5's labelled MM next-digit ports without conflation. Original H0/B0, `[X]U mod p^2`, Frobenius eta/kappa, native `p=373` experiment, six Hasse J/E labels, both finite boundaries and positive-infinity port remain outside these auxiliary lemmas.

Control provenance: gateway v0.6.11 at this run showed `research_authority_granted=false`, `executor_binding_configured=false`, active control jobs `5/5`. Read-only original Research lane recovery/continuation receipts [#6622](https://github.com/awdawmip/kimi-query-bridge/issues/6622) and [#6623](https://github.com/awdawmip/kimi-query-bridge/issues/6623) show no authorized current own CLAIM/run; predecessor CHECKPOINT claimant mismatch is in [#1558](https://github.com/awdawmip/enterprise-math/issues/1558). GitHub author research is not a Source checkpoint, accepted Result, Research-Activity event or independent review. This artifact creates no new Task or native execution claim.
