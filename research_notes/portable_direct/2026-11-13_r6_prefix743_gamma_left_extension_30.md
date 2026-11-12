# PREFIX-743-R6 — 30 new whole-cell Gamma exclusions by exact left-band extension

Date: 2026-11-13 (Asia/Shanghai). Parent objective: PREFIX-675. Predecessor: PREFIX-742.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Evidence status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem

Let `T_p,T_z` be independent Gamma clocks from the frozen 189-row BRC survivor recurrence; set `Y=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y^2]`, `W=M2-mu^2`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`. Fix `e=(0,73/500)` and the **closed** grid cells
`R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]`.

For every **real** `q>=2`, every continuous point in the following 15 closed cells and their 15 transposes, we have

`V_q(e)-V_q(p,z) > q^2/5 > 0.`

The 15 original cells are
`i∈{14,15,16}, j∈{40,41,42,43}`, plus `(15,44),(16,44),(19,46)`.
The 30 cells are distinct (all original indices satisfy `i<j`).

## Certificate argument

The frozen kernel is reconstructed with 189 integer survivor rows and 9,529 nonzero positions. Its normalized Bernstein coefficients are symmetric and nondecreasing from each boundary toward the center. The Gamma survival tail and both `mu` and `M2` are coordinatewise nondecreasing in `(p,z)`.

On any closed subrectangle `Q=[a,c]×[b,d]`, put `L=mu(a,b)`, `H=M2(c,d)`, `mu_e=mu(e)`, `W_e=W(e)`. For `t=1/q∈(0,1/2]`, the exact comparison obeys

`[V_q(e)-V_q(p,z)]/q^2 >= W_e-H+L^2-t*(mu_e-L).`

The right hand side is affine in `t`, so checking `t=0` and `t=1/2` is sufficient. Subdivide each full grid cell into four *closed* 768-grid rectangles; compute the minimum of their two exact rational endpoint bounds. Exact computations use Python arbitrary-precision integers and `fractions.Fraction`, with no floating comparisons.

The following integers are `floor(10^6 * exact lower bound)`. The fourth column independently evaluates the original PREFIX-712 one-piece 384-cell lower-bound predicate with `e0=(0,3/20)`. All fourth-column values are negative, hence these cells did not pass that *old sufficient predicate*.

| i | j | New lower floor | Old lower floor |
|---:|---:|---:|---:|
| 14 | 40 | 44249754 | -50971250 |
| 15 | 40 | 49632601 | -46031393 |
| 16 | 40 | 55072219 | -41073324 |
| 14 | 41 | 31102949 | -66260451 |
| 15 | 41 | 36545914 | -61222046 |
| 16 | 41 | 42069797 | -56139115 |
| 14 | 42 | 18447719 | -81066300 |
| 15 | 42 | 23924235 | -75957526 |
| 16 | 42 | 29503816 | -70779891 |
| 14 | 43 | 6327117 | -95340836 |
| 15 | 43 | 11812152 | -90188404 |
| 16 | 43 | 17420361 | -84944813 |
| 15 | 44 | 249834 | -103869726 |
| 16 | 44 | 5861201 | -98587394 |
| 19 | 46 | 1965070 | -107599732 |

The global minimum new floor is `249834` at `(15,44)`. Since `249834 / 10^6 > 1/5`, the claimed strict bound holds throughout each original closed cell. Symmetry of the independent clocks extends it to the transposes.

## Historical union and exact scope

These 30 cells have `14<=min(i,j)<=19` and `max(i,j)<=46`. The PREFIX-742 author records show all original PREFIX-713/716/718 certified sets have coordinate maxima >=79, so their intersection is empty. Later PREFIX-729–PREFIX-740 additions occupy either central regions with both indices >=30 or transverse regions with a coordinate >=70, and PREFIX-741 has minimum coordinate >=20. PREFIX-742 uses only lower coordinates 17–19 with upper coordinates 40–45, while the sole new `(19,46)` lies outside it. The new cells do not overlap any of these published supports. The original PREFIX-712 sufficient predicate was recomputed exactly for all 15 original cells and failed in every case, with transposes following symmetry.

Consequently, **relative to the PREFIX-742 author's stated union**, the deduplicated count increases by 30:

`141756 + 30 = 141786` of `384^2=147456` cells; `5670` cells remain outside this author-level exclusion union.

This counting step inherits upstream author certificates, including their not-yet-completed independent audit; no mathematical admission or formal shared Result/Review is claimed.

## Validation and reproducibility

Actual local standalone Python 3 standard-library execution reconstructed the 189-row kernel, checked 9,529 nonzero positions and normalized Bernstein monotonicity, checked the pinned witness mean/variance numerator SHA256 regressions, and recomputed **all 15** exact 2×2 new and **15** old unsplit cell bounds. All passed, with the table above matching output. The standalone local verification source and output are preserved in the running research environment. The published compact replay `PREFIX743_R6_GAMMA_LEFT_EXTENSION_30.py` imports the existing published PREFIX-741 exact kernel; its direct end-to-end execution and independent audit remain future checks.

Files: `PREFIX743_R6_GAMMA_LEFT_EXTENSION_30.py` and `PREFIX743_R6_GAMMA_LEFT_EXTENSION_30_RESULTS.json`. Frozen scientific pin remains unchanged.

## Next question

Test the adjacent `i=13..16, j=40..45` frontier with refined rational enclosures or new comparison witnesses and verify the strict `q>=2` gap. Run the compact checker end-to-end from the repository, independently audit the full historical 384-grid union, and only then evaluate formal Source task admission.
