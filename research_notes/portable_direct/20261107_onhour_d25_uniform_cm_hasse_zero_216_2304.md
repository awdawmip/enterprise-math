# D25 — Uniform Hasse-zero theorem for the frozen 216/2304 fibers via CM discriminant -24

Date: 2026-11-07. **Author-side proved using standard CM reduction and Hasse–Witt theorems; finite exact checks; UNREVIEWED / NOT_ADMITTED.** TASK_RESEARCH logical lane `chatgpt-research-onhour-enterprise-math-20260923` only; maintenance lane is excluded. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Continue the prior conditional first-digit law at `46ac1f6c7acc340241ae793feca4ec782ba31bb1` without changing its source or the original p373 native experiment.

## Theorem (two uniform Gauss Hasse zeros)

For **every** prime `p ≡ 13 or 19 (mod 24)`, let `m=(p-1)/6`, `k=(p-3)/8` in the 19-class and `k=(p-5)/8` in the 13-class. In `F_p` define the two *separately sourced* polynomials

```text
Q_A(z) = sum_{i=0}^m binom(m,i) binom(2m,i) z^i
Q_B(w) = sum_{i=0}^k binom(k,i) binom(3k+1,i) w^i .
```

Then
```text
Q_A(1/2) = 0   (mod p),       Q_B(1/9) = 0   (mod p).
```
Both zeros are **simple**: `Q_A'(1/2) != 0`, `Q_B'(1/9) != 0` modulo `p`. Here ordinary derivatives are taken in `F_p[z]` and `F_p[w]`. The result discharges the uniform Hasse-zero *hypotheses* of the preceding first-digit reduction. It is not a proof of either remaining first-digit unit equation or the p³ mother congruence.

### Step 1 — quadratic transport, including the indispensable Euler branch

Work first over characteristic zero near `t=0`; use the standard Gauss quadratic identity

```text
_2F1(a,b; a+b+1/2; 4t(1-t)) = _2F1(2a,2b; a+b+1/2; t).
```

Let `R_A(t)` be the reduction of `_2F1(1/3,2/3;1;t)`; explicitly
`R_A(t)=sum_{i=0}^{2m} binom(2m,i)binom(4m,i)t^i` in `F_p[t]`. Since `1/6=-m`, `1/3=-2m` modulo `p`, the identity, compared through degree `2m<p`, gives an **exact polynomial identity**

```text
R_A(t) = Q_A(4t(1-t))  in F_p[t].                         (1)
```

For B let `R_B(t)` be the reduced `_2F1(1/4,3/4;1;t)`, terminating at the first zero parameter modulo `p`. At `p=8k+3`, `(1/8,3/8) ≡ (-(3k+1),-k)`; the same quadratic identity gives `R_B(t)=Q_B(4t(1-t))`. At `p=8k+5`, the low-degree polynomial `Q_B` comes instead from the **Euler-transformed** parameters `(5/8,7/8) ≡ (-k,-(3k+1))`. Euler's transformation followed by the quadratic identity gives

```text
_2F1(5/8,7/8;1;4t(1-t)) = (1-2t)^(-1) _2F1(1/4,3/4;1;t).
```

Coefficient comparison up to the total polynomial degree `2k+1<p` proves

```text
R_B(t) = (1-2t)^epsilon Q_B(4t(1-t)) in F_p[t],         (2)
epsilon=0 for p≡19 (mod24), epsilon=1 for p≡13 (mod24).
```

These are polynomial identities, not an appeal to an infinite analytic equality after taking `p`-adic truncations. For B at `p≡13`, omitting `1-2t` would be false.

### Step 2 — exact common CM j-invariants

In `Q(s)`, `s²=2`, introduce the algebraic fibers

```text
x_± = (2 ± s)/4;      y_± = (3 ± 2s)/6.
4x_±(1-x_±)=1/2;     4y_±(1-y_±)=1/9.
```

For A use the Hesse cubic `E^A_x: X³+Y³+Z³-3λXYZ=0` with `λ³=1/x`; smooth for `x!=0,1`. Its classical j-function is

```text
j_A(x)=27(1+8x)^3/[x(1-x)^3].
```

For B use the 2-torsion Weierstrass cubic
`E^B_y: Y²=X[X²-2X+(1-y)]`. Its invariants are
`c4=16(1+3y)`, `Δ=64y(1-y)^2`, and

```text
j_B(y)=64(1+3y)^3/[y(1-y)^2].
```

Direct exact arithmetic in `Q(s)`, reducing by `s²=2`, yields

```text
j_A(x_±) = j_B(y_±) = 2417472 ± 1707264 s.          (3)
H_-24(J) = J² - 4834944 J + 14670139392,
H_-24(j_A(x_±))=H_-24(j_B(y_±))=0.                 (4)
```

The displayed `H_-24` is the classical Hilbert class polynomial for the **maximal imaginary quadratic order of discriminant -24**, equivalently `O_{Q(sqrt(-6))}`. Independently tabulated values: https://oeis.org/A305474 and https://web.mat.upc.edu/joan.carles.lario/ellipticm.htm . The j-formula for the Hesse family is standard (e.g. Artebani–Dolgachev, *The Hesse pencil of plane cubic curves*, math.AG/0611590); the B formula follows from the displayed invariants. Thus both specific characteristic-zero fibers have CM by `Q(sqrt(-6))` (up to algebraic isomorphism).

For target primes, quadratic reciprocity gives `(2/p)=(-6/p)=-1`. Hence `p>3` is **inert** in the CM field and unramified. Every fiber above has good reduction: `x(1-x)=1/8`, `y(1-y)=1/36` are `p`-units; the Hesse discriminant is nonzero when `λ³!=1`. Deuring's CM reduction theorem therefore makes the reductions of **both** curves supersingular in characteristic `p`. Source example: Liu–Masri–Young (2015), https://link.springer.com/article/10.1186/s40687-015-0040-y ; standard Hasse criterion for plane cubics as below.

### Step 3 — identify the exact Hasse–Witt coefficient with each polynomial

For a smooth plane cubic `F(X,Y,Z)=0` in characteristic `p`, the Hasse invariant vanishes exactly when the coefficient of `(XYZ)^(p-1)` in `F^(p-1)` vanishes. For the Hesse cubic, expanding the multinomial with `p-1=6m` gives that coefficient

```text
H_A(λ)= sum_{r=0}^{2m} (p-1)!/[r!³(p-1-3r)!] (-3λ)^(p-1-3r).
```

Divide by the nonzero `(-3λ)^(p-1)`. Since
`(p-1)!/(p-1-3r)! ≡ (-1)^(3r)(3r)!` and the sign from `(-3λ)^(-3r)` cancels it, and because
`(1/3)_r(2/3)_r/(r!)²=(3r)!/[27^r(r!)³]`, one gets

```text
H_A(λ)/(-3λ)^(p-1) = R_A(λ^(-3))  (mod p).             (5)
```

For B use the ordinary Weierstrass Hasse coefficient `[X^(p-1)](X[X²-2X+(1-y)])^((p-1)/2)`. With `n=(p-1)/2`, the coefficient is

```text
H_B(y) = (-1)^n sum_{r=0}^{floor(n/2)} (-1)^r
         binom(n,r) binom(2n-2r,n) y^r.               (6)
```

The constant coefficient is `(-1)^n binom(p-1,n)=1 mod p`; successive coefficients have the exact ratio
`(r+1/4)(r+3/4)/(r+1)^2` in `F_p`. Thus

```text
H_B(y)=R_B(y) in F_p[y].                               (7)
```

Supersingularity at `x_±,y_±` makes `R_A(x_±)=R_B(y_±)=0`. Equations (1),(2) and `1-2y_±=∓2s/3 != 0` then give the original `Q_A(1/2)=Q_B(1/9)=0`. QED.

### Step 4 — simplicity of the two frozen zeros

For either polynomial `Q={}_2F1(-u,-v;1;z)` modulo `p`, the Gauss differential equation is
`z(1-z)Q'' + [1-(1-u-v)z]Q' -uv Q=0` (the sign of the last term is `-(-u)(-v)`). Its nonzero solution has degree `u<p`, with `Q(0)=1`. At a point `z0∉{0,1}`, a multiple zero of order `r≥2` gives a nonzero leading term `z0(1-z0)r(r-1)c (z-z0)^(r-2)`, impossible since `r<p`. The two frozen values `1/2,1/9` are regular. Therefore both frozen zeros are simple, so the logarithmic derivative readouts `J_A=(zQ_A')(1/2)`, `J_B=(wQ_B')(1/9)` are nonzero.

## BRC observer, residual and scope

This is a *two-port proof*: the A/216 Hesse plane-cubic coefficient and the B/2304 2-torsion cubic coefficient are computed separately, including B's Euler branch, and joined only by the **exact common CM j-polynomial and Deuring supersingularity**. The source-specific `Q,J,g`, original integer weighted coefficient streams, Hasse lifts, and their `p`-adic digits remain distinct. The observer is vanishing of the two Gauss Hasse polynomials modulo `p`; this operation is scope-safe for proving first-digit divisibility but discards the unit `g=G_p/p` and higher `p`-adic carry, which are retained for the next operation. No full-state redundancy is asserted.

The prior conditional first-digit products are now **unconditionally applicable** for all target primes:

```text
W_p/p ≡ 12 J_A g_A                                          (mod p)
V_p/p ≡ c_B J_B g_B                                        (mod p)
c_B=16 (p≡19 mod24), c_B=128/9 (p≡13 mod24).
```

To prove the first-digit normalization, it remains to establish `12J_A g_A=1` and `c_BJ_B g_B=1` **uniformly**; both `J` are now known nonzero. The higher `F_2,T_11,T_02` and nonzero high-tail carry remain untouched; this result does not claim the mother target `W_p≡p mod p³`.

## Exact independently runnable finite checker

`research_notes/portable_direct/d25_cm_hasse_uniform_zero_check_20261107.py` uses Python 3 standard-library integer modular arithmetic and the quadratic field `F_p[s]/(s²-2)`. It checks **all 77 target primes ≤2000**, both Galois conjugates, their common CM j values, the Hesse and 2-torsion Hasse polynomial zeros, and the original A/B Hasse zeros. It also checks full polynomial quadratic transformations and the B plane-cubic Hasse coefficient for all target primes ≤200. All checks actually returned PASS. Finite tests independently catch algebra/implementation errors; the universal theorem is carried by the preceding proof and the explicitly cited classical CM/Hasse theorems.

## Continuation, source and native benchmark

Next minimal scientific unit: **prove the two first-digit Frobenius/Wronskian unit products** using the now-unconditional Hasse zeros and their simple derivatives; start with an exact identity for `g_A=G_A/p`, `g_B=G_B/p` at the inert fibers and compare the two separate `p`-adic lifts. Then return to the retained signed four-port `p³` transmission. The mother objective `W_p≡p mod p³` for all target primes remains OPEN. The native same-original-class p373 `H0/B0`, divided-power, Frobenius, Hesse κ and independent replication in #1559 remain a distinct **pending native experiment**.

Original `target_request_id=onhour11-20261106-1400-exact-research-lane-continuation`. This run's direct `em_status`, original receipt and reconciliation failed with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`; Site `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. No new Source mutation, native checkpoint, Researcher registration, claim, run, Result, review or admission is asserted. This is GitHub author-side evidence and a reproducible proof.
