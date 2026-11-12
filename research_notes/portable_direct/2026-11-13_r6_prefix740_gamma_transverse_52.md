# PREFIX-740-R6 — 52 new frozen-Gamma whole-cell exclusions from transverse extension

Date: 2026-11-13 (Asia/Shanghai). Parent: PREFIX-675. Predecessor: PREFIX-739. Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Statement

Let `Y(p,z)=max(T_p,T_z)` be the two independent Gamma clocks driven by the frozen 189-row BRC stopped-count laws. Write `mu=E[Y]`, `M2=E[Y^2]`, `W=M2-mu^2`, and `V_q=q^2 W-q mu`. Put `e=(0,73/500)`. For each complete closed 384-grid cell `R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]` with `58 <= i < 70`, `96 <= j < 104`, and its transpose, we have for all real `q>=2` and all points in those closed cells,

```
V_q(e)-V_q(p,z) > 125 q^2 > 0.
```

These 192 complete continuous cells exclude global optimizers of the frozen auxiliary Gamma objective. By exact comparison to the original PREFIX-712 fine-cell test, 70 upper cells (140 with transpose) were already certified; 26 upper cells (52 reflected) are not certified by that test. Direct source-set membership checks against PREFIX-713 coupled/multicompetitor, PREFIX-716 and PREFIX-718 are all zero for those 52. The remaining post-718 certified rectangular regions, including PREFIX-739, are index-disjoint from the new 52 coordinates.

Therefore the author-level certified cell union increases from `141474` to `141526` of `147456` complete cells, i.e. `141526/147456 = 70763/73728 ≈ 95.978461371528%`, leaving `5930` cells outside this author-level certificate union.

## Exact proof

For `Q=[a,c]×[b,d]`, the frozen survivor Bernstein controls are `w_{n,k}/binom(n,k)`, symmetric and nondecreasing toward the center on `[0,1/2]`; hence `mu` and `M2` are coordinatewise nondecreasing. Let `L=mu(a,b)`, `H=M2(c,d)`. Since `mu>=0`, on `Q` we have `W<=H-L^2`. For `t=1/q∈(0,1/2]`,

```
[V_q(e)-V_q(p,z)]/q^2
 = W(e)-W(p,z)-t[mu(e)-mu(p,z)]
 >= W(e)-H+L^2-t[mu(e)-L].
```

The right side is affine in `t`, so its minimum on `[0,1/2]` is the smaller of its two endpoint values. Divide each 384-grid cell into four 768-grid closed subrectangles and take the minimum of these exact rational endpoint bounds. Rebuilding the frozen 189-row integer recurrence gives precisely 9529 nonzero survivor coefficients and row 189 empty. The local author computation verified all 96 upper cells in two separate Python integer/`Fraction` batches. Minimum of one-million times exact bounds, floored, is `125036412` (at row `j=96`); hence all exact bounds exceed 125. Exchangeability proves the transposes.

## Historical deduplication

PREFIX-712 compared the different witness `e_0=(0,3/20)` by its two endpoint inequalities `W_0-H+L^2>0` and `W_0-H+L^2-(mu_0-L)/2>0`. Both expressions are nondecreasing in `L>=0` and nonincreasing in `H`. For a coarse-parent rectangle and any fine child, the coarse lower mean is at most the fine lower mean while the coarse upper second moment is at least the fine upper second moment. Thus if a fine child fails the PREFIX-712 endpoint test, its coarse parent also fails. The exact test on the 96 candidates gives, by increasing `j=96..103`, previously-certified upper counts `5,6,7,8,9,11,12,12` (sum 70). The 26 other upper coordinates and transposes are listed in the result JSON.

The historical set test retrieved the original GitHub JSON `PREFIX713_R6_RESULTS.json` (Git blob `0a12cab85b186cda25df45591e50d7904836f7fa`), `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json` (`4945aa30875a70ae047f7d9bef37aed48e1bfb7a`), `PREFIX716_R6_RESULTS.json` (`ea2e3df0da8c4713c531339ce735907ee607dac5`) and `PREFIX718_R6_RESULTS.json` (`af6a51b91e5bd1e3e5a884ad618e0c962c030674`), then compared full reflected integer coordinate sets. Each intersection with the 52 new candidates was empty.

## Reproduction, status and next question

Companion checker: `PREFIX740_R6_GAMMA_TRANSVERSE_52.py`; expected regression summary and 52 coordinates: `PREFIX740_R6_GAMMA_TRANSVERSE_52_RESULTS.json`. The author executed the exact local 96-cell computation in two batches and separately read the original historical JSON with the authenticated GitHub connector. The combined published checker still needs an independent full end-to-end execution with all four historical files present. Current work is independent source science; no shared Task CLAIM, Result, Review or mathematical admission is asserted.

Next: further adaptive-cell certificates near `i=58..69, j>=104` and the diagonal-adjacent unexcluded region, with exact historical union deduplication. Reuse the current frozen pin; preserve PREFIX-740's 52 new coordinates for future disjointness checks.
