# PREFIX-759-R6: exact beta–binomial Gamma(max) moment-gap bounds

Date: 2026-11-13 (Asia/Shanghai). Author-level mathematical continuation of PREFIX-757/758 under PREFIX-675.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Object: **external** independent two-Gamma-clock auxiliary model (not an asserted X6-native temporal bridge).
Researcher-ID `EM-DIRECT-2102B9`; session `MCP-4994e6622b304d76ade2af09b79aec4f`; Activity-ID `RA-2C5621D588B243BEA61AFD52`.
Evidence status: `AUTHOR_ANALYTIC_DERIVATION_AND_EXACT_RATIONAL_REPLAY / UNREVIEWED / NOT_ADMITTED`.

## Theorem 759.1

Assume the all-row survivor order and the frozen first-death predicate from PREFIX-756/757: all paths survive rows 1–24 and precisely the two extreme count paths die at row 25. Thus for `x∈[0,1/2]`:

```
S_25(x) = 1 - x^25 - (1-x)^25,
g(x) = P(T_x=25) = x^25 + (1-x)^25 >= 2^-24.
```

For real `0<=p1<p2<=1/2`, set `D=S_25(p2)-S_25(p1)>0`. For arbitrary `z∈[0,1/2]`, let `C_x|T_x=m ~ Gamma(m,1)` and `Y(p,z)=max(C_p,C_z)` with independent clocks. For every real `r>0`, writing `I_{1/2}(a,b)` for the regularized incomplete beta CDF at 1/2:

```
E[Y(p2,z)^r]-E[Y(p1,z)^r]
 >= D*g(z)*r*Gamma(r+25)/25! * I_{1/2}(25,r+25)
 >= D*2^-24*r*Gamma(r+25)/25! * I_{1/2}(25,r+25) > 0.
```

For integer `m>=1`, the uniform coefficient is exactly rational:

```
C_m = [m*(m+24)!/(25!*2^24)] *
      [sum_{k=25}^{m+49} binom(m+49,k)/2^(m+49)].
E[Y(p2,z)^m]-E[Y(p1,z)^m] >= D*C_m.
```

This is a strictly stronger bound than the PREFIX-758 *first-term-only* Erlang-CDF bound for each positive moment order.

## Proof

Let `H_x(t)=P(C_x>t)` and `F_x(t)=1-H_x(t)`. The all-row order gives, for `t>0`,
`H_p2(t)-H_p1(t) >= D e^-t t^25/25!`.
The actual row-25 kill atom gives `F_z(t)>=g(z) F_25(t)`, where

```
F_25(t)=P(Gamma(25,1)<=t)
       =1-e^-t sum_{j=0}^{24} t^j/j!.
```

By independence, the survival-tail difference of the maxima is the product `(H_p2-H_p1)*F_z`. Thus its lower bound is `D*g(z)*e^-t*t^25*F_25(t)/25!`. The finite stopping horizon ensures the tail-moment formula `E[W^r]=r∫_0^∞ t^(r-1)P(W>t)dt` applies. Hence

```
Delta M_r >= r*D*g(z)/25! *
             ∫_0^∞ t^(r+24)*e^-t*F_25(t)dt.
```

For independent `A~Gamma(25,1)`, `B~Gamma(r+25,1)`, the integral equals `Gamma(r+25)*P(A<=B)`; the ratio `A/(A+B)` has the `Beta(25,r+25)` law. So `P(A<=B)=I_{1/2}(25,r+25)`. For positive integer `m`, the beta-binomial tail identity gives the stated finite sum. Finally, `g(z)>=2^-24` follows from symmetry and the convexity of `z^25+(1-z)^25` and is tight at `z=1/2`. QED.

## Exact quantitative comparisons

```
m=1:
  C_1 = 156538814160047/4722366482869645213696
      ~ 3.3148383279419453e-8
  PREFIX-758 C_1 = 15801325804719/4722366482869645213696
  new/old = 156538814160047/15801325804719 (~9.9067)
m=2:
  C_2 = 4465042313279197/2361183241434822606848
      ~ 1.8910189751160186e-6
  PREFIX-758 C_2 = 805867616040669/4722366482869645213696
  new/old = 686929586658338/61989816618513 (~11.0813)
```

For `p1=0,p2=1/4`, `D=281263154558295/281474976710656`; the improved uniform mean gap is at least
`44028600681469517259721439865/1329227995784915872903807060280344576`.

The improvement derives from retaining the **entire Gamma(25) CDF** instead of its first positive power-series term. The parameter-dependent `g(z)` expression yields an even stronger bound at all `z<1/2`.

## Verification and next experiment

Local Python-stdlib Fraction execution of the companion `PREFIX759_R6_BINOMIAL_GAMMA_CHECK.py` passed at orders `1,2,3,4,5,10`: two independently evaluated rational representations (finite Erlang expansion and beta-binomial sum) matched exactly, all coefficients strictly improved on PREFIX-758, and the stated special fractions were verified. The raw results are in `PREFIX759_R6_BINOMIAL_GAMMA_RESULTS.json`.

This lower bound concerns positive raw moments. **Variance monotonicity and the composite extremal functional `V_q=q² Var(Y)-q E[Y]` remain distinct questions**; no extra certified 1/768 parameter cell is claimed.

Source references:
- Frozen BRC science `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
- `2026-11-13_r6_prefix757_soft_centered_masks_strict_gamma_order.md` Git blob `b5e98311f42cee1885c80703742677a4089b1356`.
- `2026-11-13_r6_prefix758_first_kill_mass_gamma_moment_bounds.md` Git blob `4fa5c29d74835c3d82c313fa5696b1263af8c299`.

Next: apply the exact `z`-dependent gap to an actually unexcluded fine-grid comparator, retaining variance bounds and the frozen science. Independent mathematical review of the beta-gamma argument and inherited row-25 condition remains open. No shared CLAIM/Result/Review was obtained by this direct proof.
