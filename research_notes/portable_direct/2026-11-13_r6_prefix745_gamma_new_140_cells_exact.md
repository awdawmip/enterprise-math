# PREFIX-745-R6 — 140 additional complete BRC–Gamma grid exclusions
Date: 2026-11-13 (Asia/Shanghai).
Mother objective: PREFIX-675. Predecessor: PREFIX-744.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Researcher: `EM-DIRECT-6C78BC`; Activity: `RA-8E58DEF5D323E5770C2C9043`.
Status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem (exact scope)
Retain the frozen 189-row BRC stopped-survivor kernel. Let `T_p,T_z` be its two independent unit-rate Gamma clocks, `Y(p,z)=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y^2]`, `W=M2-mu^2`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`.
Fix `e=(0,73/500)`. Each `R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]` is a **closed** full grid cell.

For every real `q>=2`, at every continuous point of the **70** cells described in the next table and their **70** distinct transposed cells,
```
V_q(e)-V_q(p,z) > q^2 > 0.
```
Consequently these 140 complete cells contain no global maximizer of this frozen auxiliary objective.

## Exact arithmetic certificate
The original integer survivor recurrence has 189 rows and 9,529 nonzero coefficient positions. The normalized Bernstein coefficients are symmetric and nondecreasing toward the central index, implying coordinatewise monotonicity of `mu` and `M2` for the defined independent Gamma-maximum construction (the exact same premise and integer verification as PREFIX-741).

For a closed subrectangle `Q=[a,c] × [b,d]`, put `L=mu(a,b)>=0`, `H=M2(c,d)`, `mu_e=mu(e)`, `W_e=W(e)`, and `t=1/q∈(0,1/2]`. For all `(p,z)∈Q`,
```
(V_q(e)-V_q(p,z))/q^2
 = W_e-M2(p,z)+mu(p,z)^2-t*(mu_e-mu(p,z))
 >= W_e-H+L^2-t*(mu_e-L).
```
The right side is affine in `t`, hence its minimum over `[0,1/2]` is the minimum of its exact endpoint values. Partition every `R_ij` into sixteen closed rational `1/1536 × 1/1536` subrectangles, compute the endpoint minimum over all sixteen, and denote it `G_ij`.

The Python `Fraction` experiments recomputed the pinned 189-row integer kernel, the 9,529 nonzero terms, the Bernstein symmetry/unimodality checks, and the two original witness moment SHA256 regression values. The candidate-region calculation was executed in bounded independent batches, using **exact arithmetic** for all 70 distinct original cells and the original PREFIX-712 unsplit comparator `e0=(0,3/20)`. Below, `m_j` is `min_i floor(10^6 G_ij)` for the indicated half-open row range.

| j | i range inclusive | Cells | m_j |
|---:|:---:|---:|---:|
| 40 | 4..13 | 10 | 44489051 |
| 41 | 4..13 | 10 | 32835167 |
| 42 | 4..13 | 10 | 21827030 |
| 43 | 7..13 | 7 | 22846919 |
| 44 | 8..12 | 5 | 17067345 |
| 45 | 8..13 | 6 | 7720059 |
| 46 | 9..14 | 6 | 3258261 |
| 47 | 11..14 | 4 | 4043611 |
| 48 | 12..19 | 8 | 1114756 |
| 49 | 14..17 | 4 | 3828802 |

The minimum among all 70 is `floor(10^6 G_12,48)=1114756`, so `G_ij>=1114756/10^6>1` throughout the tested family. The largest (least negative) original unsplit PREFIX-712 comparator floor is `-55864790`, at `(13,40)`. Exact full row coordinates and both lower-bound microfloors appear in the companion `research_notes/portable_direct/PREFIX745_R6_GAMMA_140_RESULTS.json`, with the dependent, deterministic `research_notes/portable_direct/PREFIX745_R6_GAMMA_140_EXACT.py` replay. Coordinate exchangeability supplies the 70 transposed cells.

## Historical certificate support and conditional union
The 70 original cells have `4<=i<=19` and `40<=j<=49`. By explicit index comparison they do not intersect PREFIX-742 (`i=17..19,j=40..45`), PREFIX-743 (`i=14..16,j=40..43`, `(15,44),(16,44),(19,46)`) or PREFIX-744 (eight explicitly listed original cells), nor the PREFIX-741 lower-index-at-least-20 set. Earlier PREFIX-713/716/718 author certificates have upper-coordinate minima at least 79 as documented in PREFIX-742/743; preceding centered/transverse additions have either both indices at least 20 or an upper index at least 70. The original PREFIX-712 sufficient full-cell predicate was recomputed and is negative on every original cell (and symmetry covers transposes).

**Relative to the PREFIX-744 author's historical baseline** `141802` excluded cells, the present evidence adds `2×70=140` pairwise distinct cells:
```
141802 + 140 = 141942
141942 / 147456 = 23657 / 24576 = 96.26057942708333...%
147456 - 141942 = 5514
```
This is a provenance-conditioned **author-level** union, with independent complete historic set-audit still outstanding. It is not a formal task Result/Review or Foundation admission.

## Actual verification and reproducibility
A local Python 3 standard-library implementation from the pinned PREFIX-741 mathematical recurrence computed the bounds for the 70 original cells in separate batches, with exact `Fraction` arithmetic; all 70 new lower floors exceed 1,000,000, and all 70 old sufficient-test floors are negative. The printed per-cell arithmetic results are preserved in the companion result JSON. The compact published replay is source-dependent on `PREFIX741_R6_INNER_STRIP_194.py` and still requires one full end-to-end independent run in a matching source environment. This note records the complete exact certificate algorithm, not a claimed independent mathematical review.

## Next
Reproduce the 70 cells through the published compact checker and audit the complete historical 384-grid certificate union. Study the adjacent failed cells `(10,47),(11,48),(12,49),(13,49),(13,50),(14,50)` with adaptive 8×8 bounds or alternative moment enclosures, preserving the frozen scientific pin.
