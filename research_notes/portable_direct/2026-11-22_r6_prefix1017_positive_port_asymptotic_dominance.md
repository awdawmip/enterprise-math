# PREFIX-1017 — Eventual strict positive-port dominance and two-term asymptotic coefficient

Date: 2026-11-22 (+08). Research status: **AUTHOR_ASYMPTOTIC_PROOF / EXACT_INTEGER_AND_SYMBOLIC_CHECKED / NOT_REVIEWED**. This is a portable continuation of PREFIX-1016, not a Result, independent Review, or Foundation promotion.

## Precise inherited BRC object

The scientific input remains frozen **P000 V5** at `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`. Keep the candidate Stage46 twelve-direction signed BRC transition `w(h,d)=1-6[h=d]`, the original (Cell 0, incoming port -e1), the two orientations of the absorbed Link `{0,e1}`, and grade k=1 (one negative native step). Coherent amplitudes are summed **only inside identical Cell–terminal-port fibres** before squaring. This paper studies the already established exact terminal observer; it does not run a replacement native transition or claim a physical-time law.

Let `Q⁺_{n,1}` and `Q⁺_{n,*}` be the integer squared-numerator masses of the distinguished terminal positive port and any single one of the other five positive ports (not the sum of five). Put `Δ⁺_n=Q⁺_{n,1}-Q⁺_{n,*}`, `m=n-4>=1`, and

```text
A6(r) = sum_{a1+...+a6=r} (r!/(a1!...a6!))^2.
```

The **exact** source theorem is [PREFIX-1016](https://github.com/awdawmip/enterprise-math/blob/f92e6bcc26ce177ac70648adb62a0cf0aa7ef37c/research_notes/portable_direct/2026-11-22_r6_prefix1016_positive_port_three_A6_shifts.md):

```text
Δ⁺_{m+4} = c1(m) A6(m+1) + c2(m) A6(m+2) + c3(m) A6(m+3),
c1(m) = -72(72m²+163m+80)/(5(m+1)),
c2(m) = 2(144m³+1135m²+2367m+1310)/(5(m+1)(m+2)),
c3(m) = -2(m+8)(2m+5)/(5(m+2)).
```

## New theorem: asymptotic positivity, including first correction

As `m` tends to positive infinity,

```text
Δ⁺_{m+4}/A6(m+3) = 175/(36m) - 73/(6m²) + O(m^-3).
```

Equivalently, `lim_{m→∞} m Δ⁺_{m+4}/A6(m+3)=175/36>0`. In particular there is an integer `N` such that **Δ⁺_n>0 for every n>=N**. This resolves the *eventual* sign, without a claimed explicit threshold; the all-length `n>=5` conjecture remains open.

### Proof (discrete collision count and asymptotic expansion)

1. The exact integer count `A6(r)` is the collision coefficient of two six-label words. Fixing the sixth Laurent variable to 1 gives the exact constant-term representation
   `A6(r)=CT[(1+z1+...+z5)^r (1+z1^-1+...+z5^-1)^r]`.
   Its torus coefficient integral has a unique maximum at all angles zero, with quadratic normalized modulus
   `1 - (1/6) Σθ_i² + (1/36)(Σθ_i)² + O(|θ|⁴)`.
   The quadratic form is positive definite. Split a small neighborhood from the exponentially smaller complement, rescale angles by `r^-1/2`, and expand the even analytic logarithm. Gaussian domination of the rescaled integral yields a complete integer-power expansion, including
   `A6(r)=C 36^r r^-5/2(1+α/r+β/r²+γ/r³+O(r^-4))`
   for some `C>0` and real `α,β,γ`. This is an asymptotic analysis of the **exact BRC-derived combinatorial observer**, not a new classical physical reference trajectory.

2. The first correction `α` can be evaluated with exact sixth-category cumulants (no numerical π or trigonometric propagation). Set `y6=0`, `u_i=y_i-(Σ y_j)/6`. Under the Gaussian from the quadratic form, `Cov(u_i,u_j)=3 δ_ij-1/2`. Hence
   `E[(1/6)Σu_i⁴]=75/4` and `E[((1/6)Σu_i²)²]=35/4`.
   The quartic logarithm is one twelfth of the centered fourth cumulant, so
   `α=[75/4 - 3(35/4)]/12=-5/8`.

3. Put `t=1/m`. For `s=1,2,3`, use the common expansion
   `A6(m+s)/(C36^m m^-5/2)=36^s(1+st)^-5/2[1+αt/(1+st)+βt²/(1+st)²+γt³/(1+st)³+O(t⁴)]`.
   Substitute the **exact** rational `c_s(1/t)`. Elementary rational formal-series collection gives
   ```text
   Δ⁺_{m+4}/(C36^m m^-5/2)
     = 226800 t + (1178064 α/5 - 2263140)t² + O(t³)
     = 226800 t - 2410398 t² + O(t³).
   ```
   The unknown coefficients `β,γ` cancel in the displayed terms; the cancellation of the lower-order powers is an exact identity of the three rational coefficients.

4. Finally,
   `A6(m+3)/(C36^m m^-5/2)=36³[1+(α-15/2)t+O(t²)]`.
   Division yields exactly
   ```text
   m Δ⁺_{m+4}/A6(m+3) = 175/36 - 73/(6m) + O(m^-2).
   ```
   Positivity eventually follows since `A6(m+3)>0` and `175/36>0`. QED.

The proof requires no unverified fit of a recurrence or floating-point evidence; its remaining all-length gap is an **effective, small-length sign certificate**, rather than uncertainty about the asymptotic sign.

## Independent exact calculation

The companion Python checker evaluates the six-label collision integers via
`A_d(r)=Σ_{k=0}^r binom(r,k)^2 A_{d-1}(r-k)`, `A_1(r)=1`, with arbitrary-precision integers. It compares PREFIX-1016's three-shift rational expression (exact fractions) for every `m=1,...,300` (i.e. `n=5,...,304`) and checks all 300 contrasts are positive. It also checks the formal-series coefficient `226800`, its next coefficient `1178064 α/5-2263140`, and the normalized `-73/6` correction symbolically.

Selected comparisons of the exact ratio `mΔ⁺/A6(m+3)` with `175/36-73/(6m)`:

| m | Exact ratio (rounded for display only) | Two-term estimate |
| ---: | ---: | ---: |
| 20 | 4.296946914149758 | 4.252777777777778 |
| 50 | 4.625308300846467 | 4.617777777777778 |
| 100 | 4.741362339827189 | 4.739444444444444 |
| 200 | 4.800761555... | 4.800277777... |
| 300 | see companion exact JSON | 4.820555555... |

The exact inequality check is integer/rational; displayed decimals are only for readability. PREFIX-1016's first five known contrasts are repeated as consistency checks. No new independent Stage46 native dynamic evolution or external physical benchmark was executed.

## Scientific distinction and next question

**New:** eventual strict sign and its exact leading coefficient with first correction. **Inherited:** the all-length three-A6-shift equality; its symbolic and finite BRC-derived observer evidence. **Open:** prove `Δ⁺_n>0` for **every** integer `n>=5`, or produce an exact counterexample. A useful next strategy is a rigorous explicit remainder bound for the collision-coefficient asymptotic plus a finite exact certificate, or a positive Gram/recurrence inequality directly from the frozen BRC Laurent packet. Keep future Cell–port/branch/sign provenance when changing the observer; this theorem is only about the declared final terminal-port squared mass.

Mother question `B_fix,odd(32)∈{19,20}` remains unresolved. Historical contribution provenance: `EM-DIRECT-FBEA5D`, Activity `RA-3FB2D033BE6048D8712FF056`; current native CLAIM/PROGRESS/Activity rights must be checked separately. Retain `NOT_REVIEWED` until a genuinely independent review.
