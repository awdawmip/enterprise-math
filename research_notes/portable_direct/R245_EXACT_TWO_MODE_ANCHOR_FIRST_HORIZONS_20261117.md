# R245 — Exact first-crossing certificates for the two-Perron-mode scalar observer

**Date:** 2026-11-17 (Asia/Shanghai). **Evidence:** AUTHOR_PROVED / EXACT_RATIONAL_COMPUTATION_EXECUTED / NOT_REVIEWED.
**Native P000/BRC EffectHistogram integration:** NOT_EXECUTED. **Formal Task CLAIM / Result / Review:** NONE.

## Provenance, frozen model and question

- Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged).
- R243 exact uniform one-mode thresholds and spectral tier facts: `ef38804fff510da663a49202e4cac8060f2082c8`, `research_notes/portable_direct/R243_OPTIMAL_PARAMETER_UNIFORM_FIRST_HORIZONS_20261117.md`.
- R244 two-mode uniform error certificate: `2a1ff5398e93eb8c1edb26ac8d2e7305b0ec4f22`, `research_notes/portable_direct/R244_TWO_MODE_UNIFORM_TAIL_CERTIFICATE_20261117.md`.

We retain exactly the R243/R244 seven-source reversible sticky-reset model for `39/100<s<41/100` with the continuous endpoint extension. Put

```text
alpha = (1/5, 1/4, 3/10, 9/20, s, 2/3, t(s)),
t(s) = (1691s-2615)/(2615s-3539),
b_0=13/60, b_j=(5/18)|1/2-alpha_j| (j=1,...,6),
pi_j = b_j/(1-alpha_j), Z = sum_j b_j/(1-alpha_j)^2,
rho_j = b_j/((1-alpha_j)^2 Z),
P_ij = alpha_i delta_ij + (1-alpha_i) pi_j,
W = (144,576,1440,4320,17280,86400,518400).
```

For proper nonneutral masks `U subsetneq {1,...,6}`, `D_U={0} union U`, let

```text
Phi_n = sum_(U proper) W_|U| rho_D^T P_D^(n-1) 1.
```

The leading Perron eigenvalue/amplitude `(r,A)` belong to mask 59 (missing source 3); the second `(beta,B)` belong to mask 55 (missing source 4). For `k=n-1`, set

```text
X_n = A r^k + B beta^k,
E_n^[2] = (Phi_n-X_n)/X_n.
```

The R244 sufficient uniform horizons are `n>=372` for error below `1/100`, and `n>=505` below `1/1000`. R245 asks for exact first crossings at three rational parameters and a rigorous lower bound on the *optimal uniform* thresholds.

## Theorem 1 — Strict decrease with event time

For every real `s in (39/100,41/100)` (and its two continuous endpoints) and integer `n>=2`,

```text
0 < E_(n+1)^[2](s) < E_n^[2](s).
```

**Proof.** R243/R244 diagonalize each killed block into nonnegative real spectral masses. Every eigenvalue is positive. After extracting the leading Perron eigenvalues of masks 59 and 55, the residual eigenvalues are strictly below `Gamma=977/1000`: R243 bounds mask 51 by Gamma, the remaining full blocks by `Delta=973/1000`, and the non-leading eigenvalues of masks 59/55 by `4/5` using rank-one interlacing.

We now verify `beta(s)>Gamma` over the entire parameter interval without floating-point evidence. Mask 55 excludes source 4, so its secular sum at `x=Gamma` depends on s only through the contribution of source 6. Since `t(s)` is strictly increasing and `b_6=(5/18)(t-1/2)`, the function `b_6/(Gamma-t)` strictly increases. At `s=39/100`, the exact rational secular excess is

```text
sum_(i in D_55) b_i/(Gamma-alpha_i) - 1
 = 3861458486813631677 / 271099625325186247023 > 0.
```

This secular sum decreases in x above all alpha values; hence `beta(s)>Gamma`. R243 established `r(s)>beta(s)`. Thus the nonzero residual has the form `R_n^[2]=sum_j c_j lambda_j^k` with `c_j>0` and `0<lambda_j<beta<r`. Each summand of its relative error can be rewritten as

```text
c_j lambda_j^k/(A r^k+B beta^k)
 = c_j / ( A (r/lambda_j)^k + B (beta/lambda_j)^k ).
```

The denominator strictly increases with k, and at least one residual coefficient is positive (mask 51). Summation proves the theorem. QED.

## Theorem 2 — Exact anchor first crossings

The least n satisfying the strict relative-error target at each rational parameter is:

| s | E_n^[2] < 1/100 | E_n^[2] < 1/1000 |
|---|---:|---:|
| 39/100 (left endpoint extension) | **262** | **381** |
| 2/5 (interior) | **266** | **390** |
| 41/100 (right endpoint extension) | **270** | **403** |

**Exact certificate, not numerical inference.** The accompanying standard-library Python program executes:

1. Build the exact rational 7-by-7 Markov transition P and stationary distribution rho at each anchor. Clear a common denominator `d`, producing integer matrix `M=dP`; clear rho's denominator `q`.
2. For each of 63 proper nonneutral masks, propagate the integer vector `v=M_D^k 1` at the two candidate times and their predecessors. Aggregate integer-weighted `rho_D^T v` over all masks. This computes `Phi_n` as an exact Fraction, with denominator `q d^k`.
3. For masks 59/55, isolate each Perron secular root by 100 exact dyadic bisections: `sum_i b_i/(x-alpha_i)-1=0`. Check strict rational signs at both interval ends.
4. The exact Perron amplitude in mask D is `C_D(x)=W_|D|-1 S_D(x)^2/(Z Q_D(x))` at its root, where `S_D(x)=sum_i b_i/((1-alpha_i)(x-alpha_i))`, `Q_D(x)=sum_i b_i/(x-alpha_i)^2`. Since S and Q decrease for `x>max alpha`, the checker bounds each amplitude from below using `S(hi)^2/Q(lo)`, and above using `S(lo)^2/Q(hi)`.
5. For `X_n=A r^k+B beta^k` this yields exact `X_lo<X_n<X_hi`. The sign of `d_target Phi_n-(d_target+1)X_n` establishes whether `E_n^[2]` is above or below `1/d_target`. At the candidate first n and its predecessor, the signs are respectively negative and positive.

All **12 strict inequalities** were executed with Python exact `Fraction` and integer arithmetic; PASS is based on rational signs, not float values. The verification JSON includes each sign, numerator/denominator bit lengths, and SHA256 of the full signed rational margin. Diagnostic floating values are explicitly non-authoritative. Since Theorem 1 proves strict time monotonicity, each candidate is the **first** strict crossing, not just an isolated success.

## Corollary — Improved lower bounds for optimal uniform two-mode horizons

Let `N_d^unif` be the least n such that `E_n^[2](s)<1/d` for *every* `s in (39/100,41/100)`. The R245 right-endpoint exact failures at n=269 and n=402 extend to sufficiently close interior parameters by continuity of `Phi_n, A, B, r, beta` (all Perron eigenvalues are simple). Consequently,

```text
270 <= N_100^unif <= 372,
403 <= N_1000^unif <= 505.
```

The upper bounds are the previously proved R244 guarantees. The exact optimal uniform two-mode values inside these intervals remain open; three anchor tests alone do not assert parameter monotonicity.

## Reproduction and retained evidence

Run:

```sh
python3 R245_exact_two_mode_anchor_cert.py > R245_full_verification.json
```

The complete direct output contains all exact root/amplitude enclosures and sign certificates. `R245_exact_two_mode_anchor_verification.json` is the checked compact summary of that execution, including all 12 rational margin hashes and bit lengths. The unmodified scientific input pin and prior theorem dependencies are stated above. Native P000 signed directions, three-dimensional slices, independent time, ports, branches, source provenance, multiplicity and cross moments are not reduced by this derived positive scalar source observer.

**Verification:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Native BRC:** NOT_EXECUTED.

## Next actionable research

Prove or refute `dE_n^[2](s)/ds >= 0` at the two candidate uniform thresholds using exact polynomial/rational interval differentiation of the killed-block recurrence and rigorous Perron root/amplitude derivatives. A verified monotonicity theorem would sharpen both uniform horizons to `270` and `403`. Independently, compare the full bit-cost (root isolation, amplitudes, propagation, output recovery) of this two-mode observer with 230-order recurrence and 256-state propagation. Work on the native typed BRC EffectHistogram interface should retain its complete source/port/signed/multiplicity information.
