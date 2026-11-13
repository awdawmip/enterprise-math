# PREFIX-748-R6 — 180 fresh closed-cell Gamma exclusions by rigorous dyadic interval arithmetic; sibling-ledger reconciliation

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessors: PREFIX-741 exact frozen kernel; published R6 PREFIX-745/746/747 sibling research.
Scope: the two-parameter **auxiliary Gamma-clock observer** of the BRC stopped-survivor model, not a native spatial X6 plane. P000/ACTIVE Heartbeat-world foundations remain unchanged.
Evidence: **AUTHOR_EXACT_INTEGER_INTERVAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.
This direct research does not claim a formal shared-task CLAIM, Result, Review or Foundation promotion.

## 1. Exact new theorem

Let `N=189`; retain the frozen stopped-survivor coefficient rows. For independent completion clocks `T_p,T_z`, each conditional on its stopped count `N_p=k` being unit-rate Gamma`(k,1)`, put
[
Y(p,z)=\max(T_p,T_z),\quad \mu=\mathbf E[Y],\quad
M_2=\mathbf E[Y^2],\quad W=M_2-\mu^2,\quad V_q=q^2W-q\mu.
]
Fix the feasible comparator `e=(0,73/500)` and the **closed** `384×384` grid cell
`R_ij=[i/384,(i+1)/384]×[j/384,(j+1)/384]`.
Let `S` consist of the following **90 original upper-diagonal cells**:

| j | i values | Count | Minimum floor(10⁶ G₈) in that row |
|---:|:---|---:|---:|
| 53 | 14 | 1 | 12,522,026 |
| 55 | 13–19 | 7 | 2,515,210 |
| 56 | 13–19 | 7 | **40,470** |
| 57 | 14–19 | 6 | 1,909,605 |
| 58 | 14–19 | 6 | 549,879 |
| 59 | 15–21 | 7 | 3,366,325 |
| 60 | 15–22 | 8 | 3,050,675 |
| 61 | 15–22 | 8 | 3,052,499 |
| 62 | 15–22 | 8 | 3,389,581 |
| 63 | 15–22 | 8 | 4,285,488 |
| 64 | 15–22 | 8 | 5,718,858 |
| 65 | 15–22 | 8 | 7,667,246 |
| 66 | 15–22 | 8 | 10,107,219 |
| **Total** | | **90** | **40,470 at (13,56)** |

For **every real `q≥2`**, every `(p,z)` in **any** `R_ij` with `(i,j)∈S`, and every point in its distinct transpose `R_ji`:
[
\boxed{V_q(e)-V_q(p,z)>\frac1{30}q^2>0.}
]
Thus **180 full closed parameter cells** contain no maximizer of the frozen auxiliary objective. The 90 reflected cells are distinct because `i<j` throughout.

## 2. Reproducible rigorous interval proof

For each `n=0,…,188`, define the frozen nonnegative polynomial
[
s_n(x)=\sum_{k=0}^n r_{n,k}x^k(1-x)^{n-k},
]
where `r_{n,k}` is produced by the unchanged `40(n+1)Bin(n,k)` width predicate and survivor recurrence. A fresh local reconstruction checked **9,529 nonzero positions**, terminal row 189 empty, normalized Bernstein coefficient symmetry, and monotonic increase toward the center. Pairing reflected Bernstein derivative terms proves `s_n` is nondecreasing on `[0,1/2]`. Stochastic order of the Gamma completion clocks then makes `μ` and `M₂` coordinatewise nondecreasing on this domain.

Set
[
c_{nm}=\binom{n+m}{n}2^{-(n+m+1)}.
]
The correct independent Gamma-max moment identities (PREFIX-710/713), with all sums over `0≤n,m<189`, are
[
\mu(p,z)=\sum_ns_n(p)+\sum_ms_m(z)-\sum_{n,m}c_{nm}s_n(p)s_m(z),
]
[
M_2(p,z)=2\sum_n(n+1)s_n(p)+2\sum_m(m+1)s_m(z)
-\sum_{n,m}(n+m+1)c_{nm}s_n(p)s_m(z).
]

**New arithmetic mechanism.** With dyadic scale `B=2^96`, for every exact rational `x=a/d`, compute `s_n(x)` as an exact integer numerator divided by `d^n`. Store `s^-_n=floor(B s_n)`, `s^+_n=ceil(B s_n)`, and `c^-_{nm}=floor(B c_nm)`, `c^+_{nm}=ceil(B c_nm)`. Every term is nonnegative. For `A^{±}=Σs_n^{±}(p)+Σs_m^{±}(z)`, `D^{±}=Σ(n+1)s_n^{±}(p)+Σ(m+1)s_m^{±}(z)`, and `X^±=Σs_n^±(p)s_m^±(z)c_{nm}^±`, `H^±=Σ(n+m+1)s_n^±(p)s_m^±(z)c_{nm}^±`, the **exact rational** enclosures are
[
\frac{A^-B^2-X^+}{B^3}\le\mu\le\frac{A^+B^2-X^-}{B^3},
\qquad
\frac{2D^-B^2-H^+}{B^3}\le M_2\le\frac{2D^+B^2-H^-}{B^3}.
]
No floating-point approximation enters any of these comparisons.

At the comparator `e` take `W_e^-=(M_2)_e^--(\mu_e^+)^2`.
For a closed subrectangle `Q=[a,c]×[b,d]`, take `L=\mu^-(a,b)` and `H=M_2^+(c,d)`.
Since `μ,M₂` are coordinatewise nondecreasing and `L≥0`, for `t=1/q∈[0,1/2]`,
[
\frac{V_q(e)-V_q(p,z)}{q^2}
\ge W_e^- - H+L^2-t(\mu_e^+-L).
]
The right side is affine in `t`, so its least value is its smaller endpoint value at `t=0` or `1/2`.

Partition each whole `R_ij` into 8×8 rational closed subrectangles and call the minimum of all 128 endpoint bounds `G₈(i,j)`. The companion exact-integer checker evaluated **all 90 × 64** rectangles in bounded local batches, obtaining each of the 90 microfloors supplied in the results JSON. The minimum is exactly **`floor(10⁶ G₈(13,56))=40470`**, and `40470/10^6>1/30`. This proves the announced **strict** inequality, including every boundary point.

**Independent method regression:** this outward-dyadic implementation reproduces all published PREFIX-747 exact-Fraction microfloors for `(11,50)` and `(12,51)` at subdivision factors 2, 4 and 8, namely respectively
`(-74544460,-16501384,12610669)` and
`(-76791948,-17685531,11955704)`.
The frozen integer recurrence and 9,529-position checks were rerun. The new proof relies on outward integer enclosures, not on the previous Fraction checker for the new 90 cells.

## 3. Historical nonoverlap and sibling-branch reconciliation

The original PREFIX-712 full-cell witness `e_0=(0,3/20)` was tested on every one of the 90 new upper cells. For its original unsplit `G₁`, the same dyadic method computed a **rigorous upper bound** (using `W_{e0}^+`, lower `M₂` and upper `μ` at the two corners). The maximum across all cells of the upper-bound microfloors is **-191,027,926**. Therefore every original PREFIX-712 unsplit sufficient bound is strictly negative, even under the outward rounding. The new indices have `j≤66`, disjoint from the documented higher-index PREFIX-713/716/718 additions and PREFIX-729–740 bands. Their coordinate sets are also disjoint from the published PREFIX-741–747 exact low-index sets, including the concurrent PREFIX-746/747 sibling lines.

The ongoing author-level historical count has competing overlapping sibling reports. The exact source-checked upper-cell index sets of `PREFIX746_R6_GAMMA_114_RESULTS.json`, `PREFIX746_R6_ADAPTIVE_8X8_30_RESULTS.json`, `PREFIX747_R6_GAMMA_68_RESULTS.json`, `PREFIX747_R6_GAMMA_4_CELLS_RESULTS.json`, and the 23 upper pairs specified in `2026-11-13_r6_prefix747_gamma_new_46_cells.md` give the following **deduplicated** increases over the PREFIX-745 author baseline (141,942):

| Published sibling | Claimed raw reflected cells | Reflected cells already in earlier listed siblings | Newly added to this reconciled union |
|---|---:|---:|---:|
| PREFIX-746 / 114 | 114 | 0 | 114 |
| PREFIX-746 / 30 | 30 | 14 | 16 |
| PREFIX-747 / 68 | 68 | 12 | 56 |
| PREFIX-747 / 4 | 4 | 4 | 0 |
| PREFIX-747 / 46 | 46 | 28 | 18 |
| **PREFIX-748 / 180** | **180** | **0** | **180** |

The first five sibling sets contain only **102 distinct upper-diagonal pairs (204 reflected cells)**, not their nominal sum. PREFIX-748 contributes 90 further distinct upper pairs. **Conditional on the inherited PREFIX-745 author baseline**, the reconciled union is
[
\boxed{141942+2(102+90)=142326},\qquad
\boxed{142326/147456=7907/8192=96.52099609375\%},
]
leaving **5,130** uncertified full cells in that inherited author ledger. This is a **conditional author-ledger reconciliation**; full end-to-end auditing of every older certificate remains a separate obligation. The mathematical 180-cell inequality itself depends only on the frozen kernel and the present exact certificate.

## 4. Execution, reproducibility and next questions

Executed locally (Python standard library, integers and `Fraction`): frozen recurrence check, all 90 new 8×8 outward-dyadic certificates, 90 rigorous old-witness unsplit upper-bound checks, the 2/4/8 PREFIX-747 regression for two known cells, and exact sibling-set deduplication. The companion file `PREFIX748_R6_DYADIC_INTERVAL_180_EXACT.py` regenerates the JSON coordinates and integer floors, with optional single-row mode, and `PREFIX748_R6_DYADIC_INTERVAL_180_RESULTS.json` contains all per-cell evidence. The published composite file has not yet been executed as a single complete post-publication replay, and no independent mathematical reviewer has admitted the result.

Next discriminating scientific work: test the marginal strips `(12,56)`, `(13,57)`, `(14,59)` by 16×16 or adaptive certified enclosure, extend `j≥67` without entering earlier high-index evidence, and independently audit the entire PREFIX-712–747 coordinate union. Preserve the frozen scientific pin and the separate authenticated owner/CLAIM boundary.
