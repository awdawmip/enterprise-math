# PREFIX-752-R6 — Complete original PREFIX-712 fine-grid membership and corrected Gamma support union

Date: 2026-11-13 (Asia/Shanghai). Researcher-ID: `EM-DIRECT-A42CA6`; Activity-ID: `RA-CC3C28AC84F2B156B8AEF954`.
Parent: PREFIX-675. Immediate predecessor: PREFIX-751-R6. Frozen scientific source: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Current proof provenance: `enterprise-math/main@cc961970b212a5de54a534035f695f57ebfa72f2` before the present contribution. Scientific status: **AUTHOR_CERTIFIED_FINITE_SIGNS / UNREVIEWED / NOT_ADMITTED**. The Gamma-clock model is an external two-coordinate auxiliary observer, not a native X6 or complete three-dimensional slice result.

## Problem and exact definitions

Let `D=[0,1/2]^2` be partitioned into `384×384=147456` original fine cells
`F_(u,v)=[u/768,(u+1)/768]×[v/768,(v+1)/768]`, `0≤u,v<384`.
The frozen 189-row BRC survivor law specifies two independent Gamma/Erlang clocks. Set `Y(p,z)=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y²]`, and `W=M2-mu²`.

For the original PREFIX-711/712 comparison witness `e0=(0,3/20)`, the **old PREFIX-712 sufficient certificate** on a fine cell is the strict positivity of

```text
G_uv = W(e0) - M2((u+1)/768,(v+1)/768)
       + mu(u/768,v/768)^2
       - max(0, [mu(e0)-mu(u/768,v/768)]/2).
```

Equivalently, `G_uv=min(L_uv(0),L_uv(1/2))`, with `L` the mean-aware affine-in-`1/q` lower bound. When `G_uv>0`, the original comparison proves `V_q(e0)>V_q(p,z)` for *all real* `q≥2` and all `(p,z)` in that complete closed fine cell.

Let `O712={ (u,v):G_uv>0 }`.
Let `M` be the exact /384 macro-support from PREFIX-751: 3782 macro cells, whose 15128 distinct fine children are `M_fine`.
Let `E` be the 1850 disjoint old positive fine-cell additions from PREFIX-713 coupled/multicompetitor, PREFIX-716 and PREFIX-718. The original source sets give `|M_fine∩E|=342`, with `E∩O712=∅`, and `|O712∪E|=139018`.

## Theorem 752.1 — complete old certificate intersection

Under the frozen integer survivor law, original Gamma(max) moment formula, and the explicitly stated binary64 rounding model validated below:

```text
|O712|                     = 137168
|M_fine|                   = 15128
|M_fine ∩ O712|            = 13142
|M_fine \ O712|            = 1986
|M_fine ∩ E|               = 342
|(O712 ∪ E) ∪ M_fine|      = 140662
147456 - |(O712∪E)∪M_fine| = 6794.
```

Hence the **corrected full historical author-level Gamma exclusion support through PREFIX-749** (at the original fine lattice) is

```text
140662/147456 = 70331/73728 = 95.39252387152778...%.
```

This exact integer-union result supersedes earlier numerators derived by adding macro and fine index counts, notably 142336 and its 96.5278% presentation. It is a conditional *author-certificate geometric support* union, not independent analytic review of every later Gamma inequality.

## Reproducible finite-grid computation

The companion `PREFIX752_R6_FULL_CERTIFIED_FINE_UNION.py` uses Python with NumPy, loads the actual original PREFIX-751 support and explicit historical `E` from its published `PREFIX751_R6_FULL_MACRO_FINE_SUPPORT_CHECK.py`, and rebuilds the *frozen* integer recurrence without changing its scientific input. It checks:

* `N=189`, `WD=2^18`; 9529 nonzero original survivor-count entries; the 189th layer is empty.
* All 385 rational survivor vectors `s_n(i/768)` plus `s_n(3/20)`, with each integer numerator/denominator pair checked against its floating input by exact cross multiplication.
* Each of the 189×189 Gamma convolution coefficients `C_nm=binom(n+m,n)/2^(n+m+1)` and `D_nm=(n+m+1) C_nm` checked against its rational input (error at most `u` for `C`, `500u` for `D`).
* Every one of the 147456 original fine-grid `G_uv` values; complete sign classification is authorized only if all are farther than 0.01 from zero.

Observed complete-grid binary64 diagnostic:

```text
count(G>0)                     137168
min_(all fine cells) |G|       0.01856290810792416
min_(M_fine) |G|               0.14568454734035186
M_fine cells old-positive      13142
M_fine cells old-nonpositive   1986
known E overlap               342
```

The earlier exact-PREFIX750B old-witness checks provide four independent sign/scale spot regressions at `(40,94),(40,95),(41,94),(41,95)`: the approximate `G` values are `2.2535975765062233,-2.6161314893320338,5.318721856186521,0.45232569579683`; these agree with the earlier **exact rational floors** `2253597,-2616132,5318721,452325` when multiplied by 10^6 and floored, respectively. This is a regression, not the error proof.

### Rigorous all-sign rounding enclosure (binary64)

Assume finite, correctly rounded IEEE-754 binary64 input divisions and the standard floating-point arithmetic error model (no overflow/underflow, rounding unit `u=2^-53`); normal NumPy/BLAS positive-sum reductions obey the usual `gamma_k=ku/(1-ku)` bound, regardless of parenthesization. The script explicitly verifies binary64 machine epsilon, input rationals by exact cross-multiplication, and finite output. All coefficients and survivor probabilities are nonnegative, with `0≤s_n≤1`, `0≤C_nm≤1/2`, `0≤D_nm≤189`, and only 189 terms per individual matrix-vector dot.

For a conservative calculation, `gamma_1000<1.12×10^-13`, `Σ_nm C_nm s_n s_m≤189²/2=17860.5`, `Σ_nm D_nm s_n s_m≤189³=6751269`. Count input conversion error and roundoff in both matrix products: the total errors for the two cross sums are bounded respectively by `3×10^-9` and `10^-6`. The one-dimensional sums `Σs_n≤189` and `Σ(n+1)s_n≤17955` have errors below `10^-8`. Including additions and subtractions, the full moment evaluations admit conservative uniform bounds `|Δmu|<10^-6`, `|ΔM2|<10^-4`. As `0≤mu≤378`, the single-square and variance propagation yields `|ΔG_uv|<0.003` throughout the grid (in particular, `<0.01`). No cancellation-based relative-accuracy assumption is used for the final signs.

Because the *observed minimum absolute G* across the full grid exceeds 0.01856, every computed sign equals the exact rational sign under these error assumptions. Thus 137168 and 13142 are **certified finite integer counts**, although the actual entries of `G` were evaluated via floating point. A computer with nonstandard BLAS arithmetic violating these explicit assumptions must use certified intervals or exact Fraction fallbacks before adopting the count.

### Finite set arithmetic

The macro/fine expansion is exact: `(i,j)↦{(2i+a,2j+b):a,b∈{0,1}}`. The PREFIX-751 source script reconstructs `M_fine` and the four historical `E` families, with `|M_fine∩E|=342`.
With `E∩O712=∅`, the inclusion-exclusion identity is

```text
|(O712∪E)∪M_fine|
 = |O712|+|E|+|M_fine|-|M_fine∩O712|-|M_fine∩E|
 = 137168+1850+15128-13142-342 = 140662.
```

All boundaries overlap geometrically but are counted by distinct **cell interiors** and corresponding canonical cell indices, consistently with the prior source convention.

## What was executed and what remains

**Executed in this research turn**: complete frozen 189-row integer recurrence, 385+1 original rational survivor vectors, 189² Gamma coefficient rational-rounding checks, the full 384×384 binary64 sign matrix, the exact 3782-macro support reconstruction from SOURCE-listed family ranges and JSON coordinates, the 15128-cell subset count, the uniform minimum gap check, and the original PREFIX-711/712 baseline 137168 regression. The independent local scan is `/mnt/data/prefix752_numeric_audit.py`; the publication checker has passed syntax compilation. The companion publication checker imports exact PREFIX-751 source lists and has **not yet been run in that fully assembled dependency environment**, so its automatic explicit-E disjointness assertion is a remaining reproducibility check.

**Scientific boundary**: The arithmetic certifies original old-witness signs and resulting integer set union under stated finite precision semantics; all later analytic Gamma exclusion certificates retain their previous **author-side, unreviewed** status. No native-X6 dynamics, shared CLAIM, Result, review or P000 change is asserted.

**Next useful research**: run the published checker on a full independent checkout, obtain its JSON readback and independent reviewer confirmation; then project the resulting 6794 genuinely uncovered fine cells, select nonduplicate regions for new exact Gamma witness or refined moment-bound work, and inspect any theorem-dependent analytic gaps.
