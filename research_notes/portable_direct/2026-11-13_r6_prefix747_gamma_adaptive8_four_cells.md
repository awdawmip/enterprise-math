# PREFIX-747-R6 — Four more exact Gamma exclusion cells by 8×8 refinement

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675. Predecessor: PREFIX-746.
Researcher-ID: `EM-DIRECT-6649FC`; Research-Activity-ID: `RA-E1A8598C3ED2BB594F68B2AE`.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Evidence grade: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Exact auxiliary-model proposition

Use the frozen 189-layer stopped-survivor BRC kernel, two independent unit-rate Gamma clocks `T_p,T_z`, `Y=max(T_p,T_z)`, `mu(p,z)=E[Y]`, `M2(p,z)=E[Y²]`, and `W=M2-mu²`.
Define `V_q(p,z)=q²W(p,z)-q*mu(p,z)`, comparator `e=(0,73/500)`, and full **closed** 384-grid cell
`R_ij=[i/384,(i+1)/384]×[j/384,(j+1)/384]`.

For each continuous `(p,z)` in `R_(11,50)`, `R_(12,51)` or their two coordinate transposes, and **every real `q≥2`**:

```
V_q(e)-V_q(p,z) > 11*q² > 0.
```

Therefore all four full closed cells are excluded from global maximizers of this frozen auxiliary objective.

## Certified enclosure and proof

The frozen integer recurrence yields 9,529 nonzero survivor-coefficient positions; all checked rows are symmetric and their normalized Bernstein coefficients nondecreasing toward the center. It follows, via stochastic ordering of the stopped Gamma clock, that both `mu` and `M2` are coordinatewise nondecreasing on the considered domain. The two-Gamma max moments are evaluated using the exact integer kernel
`C[n,m]=binom(n+m,n)*2^(2N-2-n-m)`, `Z=2^(2N-1)` with `N=189`, as in PREFIX-741.

For an exact rational subrectangle `Q=[a,c]×[b,d]`, set `L=mu(a,b)`, `H=M2(c,d)`, `t=1/q∈(0,1/2]`. By monotonicity `mu≥L≥0`, `M2≤H`. Thus

```
[V_q(e)-V_q(p,z)]/q²
 = W(e)-M2(p,z)+mu(p,z)²-t*(mu(e)-mu(p,z))
 >= W(e)-H+L²-t*(mu(e)-L).
```

The right-hand expression is affine in `t`, so its minimum over `[0,1/2]` is attained at `0` or `1/2`. Partition each whole `R_ij` into 8×8 closed rational subrectangles; let `G_8(i,j)` be the minimum of those exact two-endpoint bounds over all 64 pieces. Exchangeability gives the same bound for each transposed cell.

All arithmetic used for each reported minimum is exact `fractions.Fraction` arithmetic. The displayed values are **floor(10^6 G_s)**, with the floor taken after the exact minimum, not floating-point approximations:

| (i,j) | 2×2 | 4×4 | 8×8 |
|---|---:|---:|---:|
| (11,50) | -74,544,460 | -16,501,384 | **12,610,669** |
| (12,51) | -76,791,948 | -17,685,531 | **11,955,704** |

Therefore both exact `G_8>11`. The sign switches between 4×4 and 8×8 without any change to the model or comparator.

## Reproduction and provenance

Companion checker: `PREFIX747_R6_GAMMA_4_CELLS.py`, importing the published exact SOURCE comparator/moments from `PREFIX741_R6_INNER_STRIP_194.py`. Companion JSON: `PREFIX747_R6_GAMMA_4_CELLS_RESULTS.json`.

Each of the two original-cell calculations was **independently executed in a fresh local Python process** on 2026-11-13, using a reconstructed exact 189-row recurrence (matching PREFIX-741), after checking 9,529 nonzero positions, Bernstein symmetry/unimodality, and the two frozen witness-moment SHA256 regressions. Observed floors: `(11,50) -> (-74544460,-16501384,12610669)`; `(12,51) -> (-76791948,-17685531,11955704)`. The integrated published checker has not yet been successfully rerun end-to-end in one invocation; previous combined attempts exceeded their local timeouts after printing the first passing cell. Each original cell was separately checked to completion.

Historical non-overlap: the exact original-coordinate sets in the published PREFIX-742/743/744/745/746 JSONs were fetched and searched for `(11,50),(50,11),(12,51),(51,12)`; neither pair appeared. The intervening PREFIX-741 cells have smaller index ≥20; prior author notes place the relevant older PREFIX-713/716/718 cells at larger index ≥79, and PREFIX-712's original witness had no sufficient certificate in this inner band. This supports four additions to the **documented author-level baseline**; a global independent complete union audit remains open.

```
Prior PREFIX-746 author baseline: 141972 / 147456
New distinct certified cells: 4
PREFIX-747 author baseline: 141976 / 147456 = 17747/18432
Approximate fraction: 96.2836371528%
Author-level unexcluded complete cells: 5480
```

## Next research unit

Re-run the dependent companion checker against all exact repository dependencies, independently audit the entire historical cell-coordinate union, and investigate neighbors `(12,52)`, `(10,50)`, `(11,51)` using selective 8×8 or finer refinements and possible alternative comparison points. Preserve the frozen scientific pin, original Task/Owner semantics and independent review boundary.
