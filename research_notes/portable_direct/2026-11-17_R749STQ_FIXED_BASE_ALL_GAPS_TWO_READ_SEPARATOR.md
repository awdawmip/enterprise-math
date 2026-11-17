# R749STQ — Exact adjacent-read separator threshold for the entire fixed-base congruence family

Date: 2026-11-17. Evidence: `AUTHOR_EXACT_NOT_REVIEWED`.
Scientific pin (unchanged): `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Predecessor: R749STP, `research_notes/portable_direct/2026-11-17_R749STP_EXACT_INITIAL_ADJACENT_TWO_READ_OPTIMALITY.md` at `1215873a2b5364202b0c8990b9bdb48cc2afc808`.
This is an **auxiliary five-source scalar observer**. No native X6 or Port/Cell equivalence is asserted.

## Model and exact theorem

The five labeled nonnegative source coordinates have weights `(1,1,2,3,6)`. Let `C_n` count tuples with weighted sum at most `n-1`, and `T_n` be the sum of the *first* weight-one coordinate over the same population. Set

```
S(n) = 18 n^4 + 54 n^3 - 345 n^2 + 2070 n - 16315,
Y_n(e,d) = n^3 (T_n + e)/(C_n + d) - S(n)/108.
D_n(e,d) = Y_n(e,d) - Y_{n+6}(e,d).
```

For each positive integer `h`, compare candidates `q=73`, `p=73+6h` using the same first two consecutive observations. Each candidate has its own nuisance pair, `(e,d),(E,D) in [-2,2]^2`, fixed across both reads. Define

```
H_h = [Y_73(e,d)-Y_79(e,d)]
    - [Y_(73+6h)(E,D)-Y_(79+6h)(E,D)].
delta_h = min_{[-2,2]^4} H_h.
```

**Theorem.** For every integer `h>=1`,

1. The exact attained minimum is
   `delta_h = D_73(-2,2) - D_(73+6h)(2,-2)`.
2. `delta_h` is strictly increasing in `h`, and
   ```
   delta_20 = -191487918321907500088582 / 11634459400665158622199815 < 0,
   delta_21 = 80015723664272810907563 / 15593573618164568131752840 > 0.
   ```
3. **For h>=21 (p>=199), `H_h>=delta_21>0` throughout the entire real nuisance cube**. Thus the two initial observations separate the two candidate sets. If each of the four scalar input readings is perturbed by at most `eta`, this sign remains positive for every `eta<delta_21/4` (approximately `0.0012828317232405353`).
4. **For 1<=h<=20, `H_h` takes both signs and zero is attained** for legal real nuisance states. This is a sharp threshold for this **particular difference-of-two-reads statistic**, not a claim that the full two-dimensional observation vectors coincide.

This extends the R749STP special pair `h=32` (73/265) to an infinite family and determines the exact transition point `h=21`, with no finite truncation of `h`.

## Proof

**Step 1 — exact six-phase counting polynomials.** Writing `n=73+6k`, `k>=0`, the counts are

```
C_n = (k+13)(k+14)(54k^3+2097k^2+27103k+116595)/30
T_n = (k+12)(k+13)(k+14)(216k^3+8532k^2+112161k+490715)/120.
```

For rigor, the generating functions in the index `n` are

```
sum C_n z^n = z / [(1-z)^3 (1-z^2)(1-z^3)(1-z^6)],
sum T_n z^n = z^2 / [(1-z)^4 (1-z^2)(1-z^3)(1-z^6)].
```

After multiplication by suitable polynomials these have denominators `(1-z^6)^6` and `(1-z^6)^7`, with numerator degrees 23 and 29, respectively. On the residue class `n=73+6k`, their coefficient functions are therefore exact polynomials of degree at most 5 and 6 for all `k>=0`. The displayed polynomials are uniquely certified by 6 and 7 exact integer dynamic-programming counts; further independent counts are cross-checked in the script.

**Step 2 — nuisance monotonicity.** For `n=73+6k`, `N=n+6`, differentiation gives

```
partial_e D_n >= a(k) = n^3/(C_n+2) - N^3/(C_N-2),
-partial_d D_n >= b(k) =
  n^3(T_n-2)/(C_n+2)^2 - N^3(T_N+2)/(C_N-2)^2.
```

The exact rational polynomials obtained after substituting the Step 1 formulas have strictly positive denominator coefficients and strictly positive numerator coefficients, respectively 8 and 19 numerator coefficients (degrees 7 and 18). Thus `a(k),b(k)>0` for every real `k>=0`, and `D_n` increases in `e` and decreases in `d` over the entire legal square. In particular, `D_n(-2,2)` is the attained minimum and `D_n(2,-2)` is the attained maximum.

**Step 3 — strict decrease of the upper envelope.** Let `U(k)=D_(73+6k)(2,-2)`. Substitution gives a rational polynomial for `U(k)-U(k+1)` with strictly positive numerator and denominator coefficients (13 numerator coefficients, degree 12); the attached exact certificate constructs and checks every coefficient. Therefore `U(k+1)<U(k)` for every real `k>=0`.

**Step 4 — exact transition and zero.** Independence of the nuisance squares gives
`min H_h=D_73(-2,2)-U(h)` and
`max H_h=D_73(2,-2)-D_(73+6h)(-2,2)`.
Step 3 makes `delta_h` strictly increasing. Exact endpoint substitution gives the rational witnesses in the theorem. For `1<=h<=20` the minimum is negative, while
```
max H_h >= U(0)-U(h) >= U(0)-U(1) > 0.
```
By continuity along a path between the two attained corners, `H_h=0` somewhere in the legal cube. For `h>=21`, `delta_h>=delta_21>0`. Finally, four scalar reading perturbations each bounded by `eta` change `H_h` by at most `4 eta`, establishing the uniform noise bound.

## Exact reproducibility, provenance and remaining problem

The companion `R749STQ_FIXED_BASE_ALL_GAPS_CERT.py` uses exact integer dynamic programming, `sympy` polynomial algebra and rational arithmetic, and outputs `R749STQ_FIXED_BASE_ALL_GAPS_RESULTS.json`. It checks the counting identities, coefficient-by-coefficient positivity of all three global rational inequalities, both exact threshold fractions, and their direction. Locally executed: **PASS** on 2026-11-17. Proof is author-checked and is awaiting independent review; no Lean formalization or project theorem promotion is claimed.

The family has infinitely many allowed positive integer gaps and continuously varying real nuisance parameters. The full two-observation-vector collision problem for `1<=h<=20`, the best linear/nonlinear decision statistics and their noise margins, and provenance-preserving typed BRC/Port/Cell observation lifts remain worthwhile next questions. Preserve the exact five-source input pin and all source labels for any lift.
