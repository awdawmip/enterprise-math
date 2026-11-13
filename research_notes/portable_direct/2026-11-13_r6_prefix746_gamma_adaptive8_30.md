# PREFIX-746-R6 — 30 additional complete Gamma-grid exclusions via exact 8×8 refinement

2026-11-13 (Asia/Shanghai). Mother objective PREFIX-675, predecessor PREFIX-745.
Frozen scientific source: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Researcher `EM-DIRECT-5E5F0E`, Activity `RA-2D0B93587B06028CFF775009`.
Status **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem
Use the frozen 189-row BRC stopped-survivor kernel and two independent unit-rate Gamma clocks `T_p,T_z`, with `Y=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²`, and `V_q(p,z)=q² W-q mu`.
Set `e=(0,73/500)` and `R_ij=[i/384,(i+1)/384]×[j/384,(j+1)/384]` (closed cell).
For every **real** `q≥2` and all continuous `(p,z)` in the 15 original cells below and the 15 distinct coordinate transposes,

```text
V_q(e) - V_q(p,z) > 11 q² > 0.
```

Hence all 30 complete closed cells are excluded as global maximizers of this frozen auxiliary objective.

## Proof and exact certificate
The frozen integer survivor coefficients are symmetric and Bernstein-monotone toward the center; consequently `mu(p,z)` and `M2(p,z)` are coordinatewise nondecreasing. The original 189-row recurrence (9,529 nonzero positions) and two prior witness-moment SHA256 values were checked locally.

For a rational subrectangle `Q=[a,c]×[b,d]`, let `L=mu(a,b)≥0`, `H=M2(c,d)` and `t=1/q∈(0,1/2]`. For all `(p,z)∈Q`,

```text
(V_q(e)-V_q(p,z))/q²
 = W(e)-M2(p,z)+mu(p,z)²-t*(mu(e)-mu(p,z))
 ≥ W(e)-H+L²-t*(mu(e)-L).
```

The final expression is affine in `t`, so its minimum on `[0,1/2]` occurs at `0` or `1/2`. Partition each whole `R_ij` into 64 closed exact rational `8×8` subrectangles; compute this two-endpoint minimum for each, then the minimum over the 64. Denote the resulting exact rational lower bound by `G_8(i,j)`.

Using Python 3 standard-library `Fraction`, all 15 original cells were checked in bounded local batches. The exact floor of `10^6 G_8` is displayed below. The smallest is **11,934,432** at `(13,52)`; thus every exact `G_8≥11.934432>11`. Exchangeability of `T_p,T_z` proves the transposed cells.

| i | j | floor(10^6 G_8) | floor(original PREFIX-712 bound) |
|---:|---:|---:|---:|
| 9 | 47 | 22680239 | -168971108 |
| 10 | 47 | 27002790 | -164850312 |
| 10 | 48 | 20105480 | -175568312 |
| 11 | 48 | 24535826 | -171331230 |
| 11 | 49 | 18217896 | -181385295 |
| 12 | 49 | 22747775 | -177040130 |
| 13 | 49 | 27509360 | -172487371 |
| 12 | 50 | 16999301 | -186435764 |
| 13 | 50 | 21620243 | -181990942 |
| 14 | 50 | 26470862 | -177340583 |
| 13 | 51 | 16428868 | -190736413 |
| 14 | 51 | 21132267 | -186200483 |
| 15 | 51 | 26063219 | -181461078 |
| 13 | 52 | 11934432 | -198718120 |
| 14 | 52 | 16483549 | -194306447 |

The fourth column is `floor(10^6 G_1)` for the original unsplit PREFIX-712 comparison witness `(0,3/20)`; its sufficient predicate is negative in all 15 cases. These cells are disjoint from the exact coordinate sets in PREFIX-742/743/744, the ranges in PREFIX-745, and PREFIX-741 (whose smaller index is at least 20). Earlier historical certificate support PREFIX-713/716/718 has larger index at least 79, per the predecessor notes. On this documented author-level baseline, the new 15+15 cells are nonoverlapping additions:

```text
141942 + 30 = 141972 / 147456 = 96.2809244792% (author-level, conditional)
147456 - 141972 = 5484 remaining cells.
```

A complete independent historical certificate union audit is still pending. The result is a precise conditional author-level union and a cell-level exact-rational proof, not a formally reviewed/admitted Task Result.

## Discriminating refinement
The exact 4×4 microfloors were negative at `(10,47):-485046`, `(11,48):-3521151`, `(12,49):-5864797`, `(14,50):-2708743`. On the same frozen model and comparison point, the 8×8 bounds above become positive. The improvement comes from certifying narrower enclosures, rather than modifying the auxiliary objective.

## Provenance and reproduction
Companions: `PREFIX746_R6_ADAPTIVE_8X8_30.py` and `PREFIX746_R6_ADAPTIVE_8X8_30_RESULTS.json`.
The local independent implementation copied the recurrence from pinned PREFIX-741, rebuilt the 189-row kernel, checked 9,529 nonzero positions and moment hash regressions, then computed the 15 exact 8×8 certificates in bounded Python runs. The dependent published combined replay has not yet been executed end-to-end. No independent mathematical review has been completed.

Next: execute the combined checker against its published dependencies; audit the entire previous historical union; investigate neighbors `(12,51)`, `(12,52)`, `(15,52)` or alternative witnesses without rebasing the frozen scientific pin.
