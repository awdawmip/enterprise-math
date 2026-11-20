# F7 Driver r431 — projective incidence inequality, equality rigidity, and the unique best J-even four-line mask

Date 2026-11-21 (+08:00). Driver logical line `EM-DVR-DEBB5E`, a mathematical continuation from independently saved r430. Original F7 author `EM-CBRCF7-83A1D4` retains all original F7 proofs and ablations. This is a scoped mathematical theorem, not a Native independent Review or an admitted Result.

## General incidence theorem (all finite projective configurations in dimension two)

Let `r>=2`. Choose `x_0,x_1,...,x_r in R^2\{0}` such that the lines `R x_1,...,R x_r` are pairwise distinct and `R x_0` is distinct from all of them. Let
```
q(x)=sum_{j=1}^M w_j 1_{L_j(x)!=0},   w_j>=0,
```
where each `L_j` is a nonzero homogeneous real linear form. Then
```
                 sum_{i=1}^r q(x_i) >= (r-1) q(x_0).          (P_r)
```
The coefficient `r-1` is optimal. If equality holds, every positive-weight `L_j` has kernel **exactly one** of the `r` selected projective lines. Conversely, any nonnegative mixture supported on these `r` kernels has equality.

**Proof.** In `R^2` a nonzero linear form vanishes on precisely one projective line, so among `x_1,...,x_r` it is nonzero on at least `r-1` points. Therefore the individual contribution to the difference
```
  sum_{i=1}^r q(x_i)-(r-1)q(x_0)
   = sum_j w_j [#{i:L_j(x_i)!=0} - (r-1)1_{L_j(x_0)!=0}]
```
is nonnegative. It is **zero** exactly when `L_j(x_i)=0` for one selected `i`: in that case `L_j(x_0)!=0` by the distinct-line assumption, and the bracket is `(r-1)-(r-1)=0`. If its kernel is none of the selected lines, the bracket is `r-(r-1)=1` if `L_j(x_0)!=0`, or `r` otherwise. The latter case includes a form with kernel `R x_0`. Thus equality holds precisely with the claimed support. One such positive-weight form achieves the constant `r-1`, proving sharpness. QED.

## Rigidity for the exact F7 two marks

Apply `(P_4)` to `x_0=(1,0)` and
`x_1=(2,1),x_2=(-2,1),x_3=(1,1),x_4=(-1,1)`. Suppose `q` is J-even, `q(-n,m)=q(n,m)`, and normalized `q(1,0)=1`. The r430 argument shows
```
                    q(2,1)+q(-1,-1) >= 3/2.                (M)
```
If equality holds in (M), then equality holds in `(P_4)`. The general equality classification forces **all positive mass** to the four kernel lines `n=±2m`, `n=±m`. Because `q` is centrally even by construction and J-even by assumption, comparing `q` on a point lying on a single one of these four lines with its J transform forces equality of the total weights on each sign-reflected pair. (Generic points see all terms, and a point on one line sees precisely the weight of that line removed.)

Therefore every equality function is of the form
```
q_{a,b}(n,m)=a [1_{n-2m!=0}+1_{n+2m!=0}]
            +b [1_{n-m!=0}+1_{n+m!=0}],
a,b>=0,    2a+2b=1.                                     (F)
```
Its mark values are `q_{a,b}(2,1)=1-a` and `q_{a,b}(-1,-1)=1-b`.

Now minimize the maximum absolute error relative to both F7 target marks `1/2` over **all** nonnegative homogeneous linear-indicator mixtures that are J-even and satisfy `q(1,0)=1`:
```
 min_q max( |q(2,1)-1/2|, |q(-1,-1)-1/2| ) = 1/4.           (E)
```
Indeed (M) implies the maximum of the two values is at least `3/4`, giving error at least `1/4`. The symmetrized four-line mask with `a=b=1/4` attains `1/4`. Any minimizer must have both marks `<=3/4` and sum `>=3/2`, hence both equal `3/4`; equality forces (F), and `1-a=1-b=3/4` forces `a=b=1/4`. Thus, up to representing the same linear functional with repeated/scaled forms, **the minimizing function is unique**: exactly r429's `qJ`.

This upgrades r430's incidence obstruction into a complete sharp minimax and equality classification for the hyperplane-mask construction class. It explains why reweighting or adding nonnegative homogeneous line indicators cannot improve r429's individual marked-balance error.

## Scope and preserved provenance

The quantifiers concern nonnegative finite mixtures of **homogeneous linear nonvanishing masks** on `Z^2` (proof extends to `R^2`); the theorem makes no claim about arbitrary nonnegative J-even functions, congruence-dependent functions, nonlinear observations, or the all-input `GL_4(Z)` defect after leaving this representation class. The original exact F7 NO_GO remains the separate mother objective.

- Prior Driver r430: `research_notes/driver/2026-11-21_f7_r430_four_ray_hyperplane_mask_balance_obstruction.md@884c4c764ad101764dc471da554f809f812db86a`.
- Driver r429 exact `qJ` and mixed-map global `3/4` defect: `research_notes/driver/2026-11-21_f7_J_symmetrized_GL4_exact_three_quarter_defect_r429.md@d1be8fbdecbc758e9cd61f35dbb06d58cd79e041`.
- Original F7 revised ablation source: `research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py@c9bf0811f8cc17af1fa116af75911ed70b1f26b9`.
- Original F7 frozen Result and failed first-review request remain protected and unchanged. The original writer error and two-file hash discrepancy are separate, as described in Issue #2874 and the earlier frozen manifest audit.

**Layered outcome:** new mathematical proof subunit +1; Native Review admitted 0; Native Result admitted 0; Task completed 0; mother Objective closed 0.
