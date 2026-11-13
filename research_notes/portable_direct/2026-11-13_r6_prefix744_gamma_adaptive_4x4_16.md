# PREFIX-744-R6 — 16 further whole-grid exclusions by 4×4 exact rational enclosures

Date: 2026-11-13 (Asia/Shanghai). Predecessor: PREFIX-743. Mother objective: PREFIX-675.
Frozen scientific pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem

Use the same 189-row BRC survivor-count Gamma-clock model, `Y(p,z)=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²`, `V_q(p,z)=q²W-q mu`, and `e=(0,73/500)` as PREFIX-743. Let `R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]` be **closed**.

For every real `q>=2`, at every continuous point in the eight cells listed below and their coordinate transposes, we prove

`V_q(e)-V_q(p,z) > 36 q² > 0.`

The eight original cells are `(13,44),(14,44),(14,45),(15,45),(16,45),(17,46),(18,46),(19,47)`. The transposes give sixteen distinct complete cells.

## Exact certificate

For each `R_ij`, partition into sixteen **closed** `1536×1536`-grid subrectangles `Q=[a,c]×[b,d]`. The frozen Bernstein survivor ratios are symmetric and coordinate-monotone; as previously verified with integer recurrence, both `mu` and `M2` are coordinatewise nondecreasing. Therefore, writing `L=mu(a,b)`, `H=M2(c,d)` and `t=1/q∈(0,1/2]`,

`[V_q(e)-V_q(p,z)]/q² >= W(e)-H+L²-t*(mu(e)-L).`

Its affine minimum on `[0,1/2]` is attained at an endpoint. The minimum of the two endpoint bounds, over all 16 subrectangles of each whole cell, is an exact rational certificate. In parallel, the old PREFIX-712 witness `e0=(0,3/20)` was checked on each unsplit whole cell. The fourth column gives its original sufficient-predicate lower bound, which is negative in all eight cases.

| i | j | floor(10^6 × new 4×4 bound) | floor(10^6 × old unsplit bound) |
|---:|---:|---:|---:|
| 13 | 44 | 41218899 | -114080286 |
| 14 | 44 | 46656522 | -109040668 |
| 14 | 45 | 36791209 | -122127135 |
| 15 | 45 | 42349288 | -116961187 |
| 16 | 45 | 48077835 | -111665694 |
| 17 | 46 | 44552341 | -118729709 |
| 18 | 46 | 50543385 | -113208439 |
| 19 | 47 | 47771633 | -119436584 |

The minimum **integer floor** of the exact bounds is `36,791,209` at `(14,45)`; thus every exact bound is at least `36.791209`, establishing the strict uniform `36q²` inequality. Coordinate exchangeability gives the transposes.

## Nonoverlap and cumulative author union

These eight new cells have smaller coordinate 13–19 and larger coordinate 44–47. They are disjoint from PREFIX-743's 15 originals: its row-44 originals have `i=15,16`, its row-45 originals have `i=17..19` (PREFIX-742), and its new row-46 original is `i=19`. Explicit coordinate comparison with PREFIX-742/743 support excludes their intersection. They are also disjoint from PREFIX-741 and earlier centered / transverse author additions by their coordinate support. Earlier PREFIX-713/716/718 certified coordinate sets have maximum coordinate >=79, as checked in the PREFIX-742 provenance; the exact original PREFIX-712 one-cell predicate fails here, as above.

Using PREFIX-743's provenance-conditioned baseline `141786`, these sixteen cells yield `141786+16=141802` out of `147456` complete cells, leaving `5654` uncovered by the *author-level certificate union*. An independent full-historical audit remains required for promotion of the cumulative figure.

## Actual verification

A separate Python 3 standard-library run independently reconstructed the full frozen 189-row integer kernel, verified 9,529 nonzero survivor positions, normalized Bernstein coefficient monotonicity, and the reference Gamma witness SHA256 regressions. Two exact 4×4 probe batches computed the eight table bounds with arbitrary-precision `Fraction`, and a third run independently checked the eight original PREFIX-712 unsplit bounds. All passed. The published compact dependency-based replay `PREFIX744_R6_ADAPTIVE_4X4_16.py` is available for end-to-end execution; it has not yet been rerun as a single combined program.

## Next

Extend adaptive 4×4 certificate search toward `i<=13` and `j>=47` and test tighter subdivisions, new witnesses, or moment-bound variants where the existing enclosure becomes nonpositive. Execute the compact replay and independently audit historical union membership before formal task-level Result/Review.
