# PREFIX-746-R6 — 114 new whole-grid Gamma exclusions by exact 4×4 / 8×8 moment enclosures

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675. Predecessor: PREFIX-745. Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**. This concerns the frozen BRC-stopped-survivor Gamma *auxiliary model*; X6/Heartbeat Foundation promotion is a separate question.

## Theorem and full domain

Let `T_p,T_z` be independent unit-rate Gamma clocks from the frozen 189-row BRC survivor counts; let `Y=max(T_p,T_z)`, `mu(p,z)=E[Y]`, `M2(p,z)=E[Y²]`, `W=M2-mu²`, and `V_q=q²W-q mu`. Fix `e=(0,73/500)`. The 384-grid cells are CLOSED: `R_ij=[i/384,(i+1)/384]×[j/384,(j+1)/384]`.

**For every real q>=2 and every continuous (p,z) in each of the 57 following full closed cells and their 57 transposed cells**, the strict inequality holds:

```
V_q(e)-V_q(p,z) > (6/5)*q² > 0.
```

Thus these 114 whole cells exclude the global maximizers of this auxiliary objective.

| j | original i values | count | smallest floor(10^6× exact gap/q² lower) |
|---:|---|---:|---:|
| 46 | 15,16 | 2 | 33042798 |
| 47 | 10,15–18,20 | 6 | 24371089 |
| 48 | 11,20,21 | 3 | 24535826 |
| 49 | 12,13,18–23 | 8 | 22747775 |
| 50 | 13–24 | 12 | 2338297 |
| 51 | 15–25 | 11 | 1484642 |
| 52 | 16–30 | 15 | **1245155** |
| **Total** | | **57** | |

## Exact certificate proof

The pinned integer survivor recurrence has 189 rows and 9,529 nonzero coefficient positions. Its normalized Bernstein coefficients are symmetric and nondecreasing toward the middle, giving coordinatewise nondecreasing Gamma-maximum moments `mu` and `M2`. For a closed subrectangle `Q=[a,c]×[b,d]`, put `L=mu(a,b)>=0`, `H=M2(c,d)`, and `t=1/q∈(0,1/2]`. Then

```
[V_q(e)-V_q(p,z)]/q²
= W(e)-M2(p,z)+mu(p,z)^2-t*(mu(e)-mu(p,z))
>= W(e)-H+L^2-t*(mu(e)-L).
```

The final expression is affine in `t`; its minimum on `[0,1/2]` is its smaller endpoint value. Divide every candidate full cell into `k×k` equal closed rational subrectangles; use `k=8` at precisely `(10,47),(11,48),(12,49),(13,49),(13,50),(14,50),(15,51),(16,52)`, and `k=4` for the other 49. All integer boundary coordinates are exact, with `Fraction` evaluation throughout. For the 57 original cells the minimum certified microfloor is `1245155` at `(17,52)`. The exact lower bound is therefore at least `1245155/1000000 > 6/5`; coordinate exchangeability proves the 57 distinct transposes.

For historical collision testing, the **original** PREFIX-712 single-full-cell sufficient bound with its original witness `e0=(0,3/20)` was evaluated for all 57 original cells. Every resulting exact lower bound is negative, with maximal microfloor `-102756816` at `(30,52)`. None of these 57 meets that original sufficient predicate.

The companion `PREFIX746_R6_GAMMA_114_RESULTS.json` records, for each cell, `[i,j,subdivision, floor(1e6*new_exact_lower),floor(1e6*old_exact_lower)]`. The `PREFIX746_R6_GAMMA_114_EXACT.py` checker reconstructs these 114 comparisons via the published exact integer kernel in `PREFIX741_R6_INNER_STRIP_194.py`.

## History / author-level union

Explicit index comparisons exclude overlap with the PREFIX-741 row ranges and exact PREFIX-742, PREFIX-743, PREFIX-744, PREFIX-745 new-cell sets. The previously certified `(17,46),(18,46),(19,47)` were excluded from this new set. PREFIX-712's actual single-cell sufficient predicate was retested above. The published PREFIX-742/743 notes describe earlier PREFIX-713/716/718 certificates with upper-coordinate minimum >=79, while the current upper coordinates are <=52; the complete older certificate union remains to be independently audited. Consequently, **conditional on PREFIX-745's reported author union**:

```
141942 + 2×57 = 142056 of 384² = 147456 cells
142056/147456 = 96.337890625%
Remaining: 5400 cells
```

The 114-cell exclusion theorem uses the exact comparison certificate without relying on the accumulated historical count.

## Actual execution / verification

An independent local Python 3 implementation rebuilt the 189-row kernel, checked its 9,529 nonzero positions and normalized Bernstein symmetry/unimodality, and matched the published witness digests:

```
SHA256(str(mu(e).numerator)) = 797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e
SHA256(str(W(e).numerator))  = 814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae
```

All 57 fresh comparisons and 57 historical original-witness full-cell predicates were executed to completion with exact integers/Fraction, in nine bounded batches, and matched every archived integer microfloor. No floating-point inequality drives certification. The compact GitHub code is a distinct, published dependent reproducer; full end-to-end execution of that published file against its repository dependency remains an open verification item, as does independent mathematical review.

## Next scientific unit

Re-run the published compact checker end-to-end and audit the complete historical union; then explore `j>=53` and the marginal band near `(15,51)` by adaptive refinements or alternative witnesses. Preserve the frozen scientific pin, provenance and live shared-owner boundaries.
