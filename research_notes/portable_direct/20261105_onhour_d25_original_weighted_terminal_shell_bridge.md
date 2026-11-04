# D25 — ORIGINAL weighted 216 terminal source connects the half cutoff to the reversed 4F3 boundary

2026-11-05 · TASK_RESEARCH author-side (logical lane `chatgpt-research-onhour-enterprise-math-20260923`). Original Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Scope: exact rational polynomial theorem, exact p³ corollary for all p=6n+1>=7; 80-prime independent integer tests. UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.

## 1. The **original** weighted cutoff, with a finite-order operator

Let `c_k=(1/2)_k(1/3)_k(2/3)_k/(k!)³`, `a_k=2^{-k}c_k`, `F_N(t)=sum_(k=0)^N c_k t^k`, `Y_N(t)=(6θ+1)F_N(t)=sum_(k=0)^N (6k+1)c_k t^k`, `θ=t d/dt`.

Define the differential operator with stated noncommutative order (`θt=t(θ+1)`):

```
D_w = (6θ-5) θ³ - t (6θ+7) (θ+1/2)(θ+1/3)(θ+2/3).
```

**Theorem 1 (all integers N>=0, exact in Q[t]):**

```
D_w Y_N(t) = -(6N+7)(6N+1)(N+1)^3 c_(N+1) t^(N+1).
```

*Proof.* The coefficient of `t^k` for `1<=k<=N` is

```
(6k-5)(6k+1) * [k³ c_k
                  - (k-1+1/2)(k-1+1/3)(k-1+2/3)c_(k-1)] = 0.
```

This is zero by the defining hypergeometric ratio `c_k/c_(k-1)`. The constant term vanishes because `θ³` kills constants. The only term `t^(N+1)` comes from the second operator, with coefficient `-(6N+7)(6N+1)(N+1)^3 c_(N+1)`. There are no higher powers. QED.

The operator is **weighted**: it retains the original factor `6k+1`. The arrangement `t(6θ+7)` is essential; the formal operator cannot be treated as commuting multiplication.

## 2. The p² terminal and its full original-shell propagation

Fix any prime `p=6n+1>=7`, set `N=3n=(p-1)/2`, `K=2n=(p-1)/3`, and evaluate at **the original point** `t=1/2`:

```
W_half = Y_N(1/2)=sum_(k=0)^N (6k+1)a_k.
```

The original coefficients have exact valuations `v_p(c_N)=1`, `v_p(c_(N+1))=2`: the `(1/3)` numerator hits `p/3` at `j=K`; the `(1/2)` numerator additionally hits `p/2` at `j=N`; their denominators are units.

For `N=(p-1)/2`, the leading rational coefficient of the terminal identity is

```
-(6N+7)(6N+1)(N+1)³ = -(3p+4)(3p-2)((p+1)/2)³ = 1 (mod p).
```

Consequently **for every such prime**:

```
D_w Y_N(t) = c_(N+1) t^(N+1) (mod p³) in Z_p[t],
D_w Y_N(1/2) = a_(N+1) (mod p³),
v_p(D_w Y_N(1/2))=2.
```

(The equality modulo p³ retains the full original p² terminal; its coefficient is not zero.)

Define the original nonzero signed boundary `U_p` from the previously established reversed-shell theorem:

```
C_p = 216^(2n) ((2n)!)^5 / (4n+1)! (mod p),
h_(n-1) = (2/3)_(n-1)^3 / ((7/6)_(n-1)(4/3)_(n-1)(n-1)!),
U_p = C_p h_(n-1) 2^(n-1) (mod p).
```

The original upper-shell indexed proof (see `20261105_onhour_d25_weighted_shell_literature_reduction.md` and `20261105_onhour_d25_reversed_shell_homogeneous_4f3.md`) identifies its final `j=3n` unweighted unit with `U_p`. That is exactly the first omitted original coefficient `a_(N+1)`, with the opposite original index-transport sign. Hence

```
a_(N+1)/p² = -U_p (mod p).
```

An independent direct adjacent-term calculation gives a second equivalent description:

```
a_(N+1)/p² = -2 n² (a_N/p) (mod p),
U_p = 2 n² (a_N/p) (mod p).
```

Indeed `a_(k+1)/a_k=((k+1/2)(k+1/3)(k+2/3))/(2(k+1)^3)`; substituting `k=N` and dividing out the new factor `p/2` yields `-1/18 = -2n² (mod p)`.

For `0<=r<n`, all next-step ratios after `a_(N+1)` are p-units and satisfy:

```
a_(N+1+r)/p²
  = -U_p * 2^(-r) * (1)_r(5/6)_r(7/6)_r/(3/2)_r³ (mod p).
```

Let `g_r=(1)_r(5/6)_r(7/6)_r/(3/2)_r³`,
`G_n(t)=sum_(r=0)^(n-1) g_r t^r`.
The original upper-shell weights satisfy `6(N+1+r)+1 = 3p+4+6r = 2(3r+2) (mod p)`. For `r=n` the `(2/3)` numerator hits a second multiple of `p` (now shell terms are of valuation at least 3), hence these `n` terms exhaust the p² shell.

This reconstructs directly from the **single original weighted differential terminal** the previously established shell identity

```
T_A(p) = -2 U_p (3θ+2)G_n(1/2) (mod p),
W_full - W_half = p² T_A(p) (mod p³).
```

In particular, the new exact all-prime bridge is

```
D_w Y_N(1/2) = -p² U_p (mod p³).
```

**What was gained:** the fixed 216 source and original cutoff, the signed nonzero upper-shell boundary, and the reflected 4F3 observer are now connected by one finite exact original differential equation. This is a constructive all-prime relation on the complete original weighted 216 model, not a surrogate norm or a substitution for the native p373 H0/B0.

## 3. Arithmetic evidence

The independent Python checker `d25_original_weighted_half_operator_checker_20261105.py` uses original `binom(2k,k)^2 binom(3k,k)/216^k` integer terms mod `p³`, original coefficient-by-coefficient operator evaluation, and independently evaluates `U_p` from `C_p h_(n-1)` and the full upper shell. It ran on all 80 primes `p=1 mod6`, `7<=p<=997`, with zero failures.

| p | terminal at t=1/2 mod p³ | (terminal/p²) mod p | U_p mod p | T_A mod p |
|---:|---:|---:|---:|---:|
| 7 | 147 | 3 | 4 | 5 |
| 13 | 1690 | 10 | 3 | 10 |
| 19 | 6137 | 17 | 2 | 9 |
| 139 | 598951 | 31 | 108 | 13 |
| 373 | 40347410 | 290 | 83 | 266 |

Original p373 identity: `290+83=373`. This is a finite exact source certificate, not an independent acceptance of LIFT.

## 4. Next exact research unit

Combine this boundary operator with the original half-sum **three-jet** decomposition from `20261105_onhour_d25_original_216_half_three_jet_p3.md`, whose exact remaining third-digit condition is `D0+S2+T_A=0 mod p`. Seek a finite creative-telescoping identity for the weighted centered terminating polynomial and its two parameter jets that realizes `D0+S2=2U_p(3θ+2)G_n(1/2)`. The component `S2` must retain quadratic joint observations on the unit block and first jet in the original single-zero block.

The fixed p373 native H0/B0 divided-power experiment ([X]U mod139129, module rank, semilinear F, eta, signed odd observer, kappa, Delta-R, independent replay) is separately tracked by #1559, still pending an actual authorized executor. Formal native CLAIM/Source checkpoint/Result are not conferred by this author-side proof.
