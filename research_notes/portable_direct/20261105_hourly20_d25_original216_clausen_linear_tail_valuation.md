# D25 — Original-216 Clausen tail: exact valuation support and linear-time second-digit certificate

Date: 2026-11-05 (Asia/Hong_Kong). Lane: TASK_RESEARCH author-side portable evidence. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific input commit `c47e13e4aba0e006366f989d6334d443f6333ae3`. Scope: original terminating **216** scalar interface; the previously studied quartic **2304** tail is a separate coefficient population. Status: **AUTHOR-DERIVED / EXACT FINITE-SUM PROOF / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED**.

## 1. Original source and exact finite Clausen identity

Let `p=6m+1 >= 7` be prime, and work in `Z_(p)`. Define for `0<=k<p`

```text
b_0 = 1,   b_(k+1)/b_k = (6k+1)(3k+1)/[36(k+1)^2],
w_0 = 1,   w_(k+1)/w_k = (2k+1)(3k+1)(3k+2)/[36(k+1)^3].
F_p = sum_{k=0}^{p-1} b_k,
h_p = sum_{k=0}^{p-1} (12k+1)b_k,
W_p = sum_{k=0}^{p-1} (6k+1)w_k,
T_p = sum_{0<=i,j<p; i+j>=p} (6(i+j)+1)b_i b_j.
```

Here `b_k=(1/6)_k(1/3)_k/(k!)^2 * (1/2)^k` and `w_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3 * (1/2)^k`; denominators are p-units for k<p. The classical formal Clausen square
```text
  _2F_1(1/6,1/3;1;z)^2 = _3F_2(1/2,1/3,2/3;1,1;z)
```
gives coefficientwise `w_k=sum_{i+j=k}b_i b_j` for all `k<p`, after including the argument `z=1/2` in each factor (both sides share the same argument). Apply the weighted operator `1+6 z d/dz` to the finite square before specialization. The product rule gives the **exact rational identity**
```text
           F_p h_p = W_p + T_p.                     (1)
```
Indeed `(1+6 theta)F^2 = F(F+12 theta F)`. This holds without any p-adic approximation.

## 2. Two valuation changes yield a triangular support theorem

For all indices `0<=k<p`, the only numerator factors divisible by `p` in the recurrence of `b_k` occur when `k=m+1` (the factor `6k-5=p`) and when `k=2m+1` (the factor `3k-2=p`). As `k<p`, the denominator `36k^2` is a p-unit. Moreover neither numerator progression hits another multiple of p before k=p. Consequently

```text
 v_p(b_k) = 0  for 0<=k<=m;
          = 1  for m+1<=k<=2m;
          = 2  for 2m+1<=k<p.                         (2)
```

Consider an ordered upper-strip pair `i+j>=p`. If `i<=m`, then `j>=p-i>=p-m=5m+1>2m`, hence its valuation is exactly 2. If both indices exceed m, their total valuation is at least 2; the only potential valuation-2 pairs with both in `(m,2m]` satisfy `i+j<=4m<6m+1=p`, and therefore do **not** lie in the upper strip. All other upper-strip pairs with both indices >m have valuation >=3. Thus the entire strip modulo p^3 is supported **only** by ordered low/high pairs, `i in [1,m]`, `j in [p-i,p-1]`, together with the transpose.

This proves unconditionally for all primes `p=6m+1`:

```text
                         T_p == 0 (mod p^2).         (3)
```

This is a genuine source-separation theorem: it holds for the **216** strip regardless of a selected Gauss factor. In particular, the prior **2304** high strip with a nonzero `T/p` observer must not be substituted here.

## 3. One-pass modular certificate for T_p/p^2

Define `c_0=1` and `c_k` recursively in F_p by stripping the two p factors at their exact occurrence:

```text
 c_k = c_(k-1) * [(6k-5)/p^[k=m+1]] *
                   [(3k-2)/p^[k=2m+1]] * (36k^2)^(-1) mod p.   (4)
```

The indicators are 0 or 1. The p-division is an ordinary exact **integer division** only at the named indices, before reduction modulo p. Then `c_k = b_k / p^{v_p(b_k)} (mod p)`.

Set `A_i=sum_{r=1}^i c_{p-r}` and `B_i=sum_{r=1}^i r c_{p-r}` (mod p). Using `j=p-r` with `1<=r<=i`, the low/high strip theorem gives

```text
 T_p/p^2 = 2 sum_{i=1}^m c_i * [(6i+1) A_i - 6 B_i]  (mod p).   (5)
```

The factor 2 is the transpose. Equation (5) is an **exact all-target second-digit identity** (not a numerical conjecture). It uses O(p) finite-field arithmetic operations and O(p) storage to build the stripped coefficient stream and the prefix sums; a straightforward direct high-strip double sum uses O(p^2) terms. Complexity is scoped to evaluating the *tail digit* after p and the coefficient recurrence are supplied; this does not claim an end-to-end sublinear all-observer algorithm or a native six-axis speedup.

### Connection to original D24 LIFT

For the frozen target primes `p mod 24 in {13,19}`, the accepted original first-digit interface supplies `p | F_p`, `p !| h_p` and `W_p == p (mod p^2)`. Write `G_p=F_p/p` and `Delta_p=(G_p h_p -1)/p (mod p)`. Dividing (1) by p and then extracting the second p-digit gives the **exact target-scope decomposition**

```text
 Delta_p = (W_p-p)/p^2 + T_p/p^2  (mod p).            (6)
```

Here `(W_p-p)/p^2` is well defined by the accepted first-digit theorem, and the second summand is computable from (5). For LIFT, the smallest remaining scalar identity is

```text
 R_p = (W_p-p)/p^2 +
       2 sum_{i=1}^m c_i[(6i+1)A_i-6B_i]  (mod p).   (7)
```

This is a source-faithful **strict interface reduction** to an explicit triangular finite-field sum plus the weighted source's own second digit. It preserves both source coordinates and the original `R_p` comparison. The still-unproved all-prime target identity is (7), not the already-established (1)-(6).

## 4. Actual exact regression (independent direct and compressed calculations)

The self-contained Node 18+ BigInt checker `research_notes/portable_direct/d25_216_clausen_linear_tail_20261105.js` was actually evaluated in the present execution with the same V8 arithmetic. It independently constructs original 216 coefficients, the separate original 2304 weighted coefficients, and the complete O(p^2) upper strip modulo p^3. It also constructs `c_k` from the stripped recurrence and verifies all p-adic quotients and (5) without reading the original upper strip to compute (5).

**PASS** for all **35 primes p=1 mod 6 between 7 and 373**; among these **19** belong to D24's exact classes `p mod24 =13,19`. The observed `W_p=V_p=p (mod p^3)` for the 19 targets is a finite regression result only, not used to prove (1)-(7).

| p | m | T_p mod p^3 | T_p/p^2 mod p | Delta_p mod p |
|--:|--:|--:|--:|--:|
| 13 | 2 | 0 | 0 | 0 |
| 19 | 3 | 4332 | 12 | 12 |
| 37 | 6 | 15059 | 11 | 11 |
| 61 | 10 | 11163 | 3 | 3 |
| 373 | 62 | 27269284 | 196 | 196 |

For p=373, `p^3=51895117`, `F_p=24495656`, `h_p=4236705`, and `W_p=373` modulo p^3. The direct exact convolution yields `T_p=27269284=196 p^2 (mod p^3)`. This is an **original 216** certificate; the earlier Gauss/2304 tail has `T_{373}/373=372` and is a distinct source object.

## 5. BRC observer/future-operation audit and next frontier

Population: the complete finite `k<p` original 216 coefficient set, including the joint high convolution indices. Distinct carriers: low/high index, valuations `0/1/2`, p-unit coefficient, ordered pair and signed 1+6-theta weight. Declared future observation: `T_p/p^2 (mod p)` and the frozen scalar `Delta_p-R_p`. The high-high and intermediate branches are erased **only** by the proved valuation>=3 at this precision; value/derivative ports, original native Frobenius direction, and other precision horizons remain uncompressed. `BRC_REUSE_RESOLUTION=REUSE_APPLIED`.

**Exact next action:** retrieve the frozen, original definition of `R_p` and compare it with the RHS of (7) at the same target primes 13, 19, 373; seek a new finite-field identity or an exact counterexample, then prove/disprove the all-target form. Retain the original p373 H0/B0 divided-power `[X]U mod p^2`, semilinear direction `eta/kappa`, and independent review as separate native evidence obligations. Do not recredit accepted parent UR/JT0, re-run the prior 2304 tail as new evidence, or reinterpret portable output as a native Source checkpoint.

Author research activity remains `REGISTER_PENDING`; no new native Researcher session, CLAIM, OPEN, `publish_checkpoint`, Result or independent mathematical acceptance was created by this author-side note.
