# PREFIX-741-R6 — 194 new complete-grid exclusions in the frozen BRC–Gamma inner strip

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: PREFIX-740. Status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem (one uniform witness, all real q >= 2)

Let `Y(p,z)=max(T_p,T_z)` for the two independent Gamma clocks from the frozen 189-level BRC survivor-count recurrence. Let `mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²` and `V_q(p,z)=q²W(p,z)-q mu(p,z)`. Fix `e=(0,73/500)`, and let `R_ij=[i/384,(i+1)/384] x [j/384,(j+1)/384]`.

For every point in each complete **closed** cell `R_ij` with `i` in the specified half-open row interval, and in its coordinate transpose, and for **every real** `q>=2`, the strict uniform inequality holds:

```
V_q(e)-V_q(p,z) > q^2 > 0.
```

| j | admissible i interval | new upper cells | minimum floor(10^6 * exact cell lower bound) |
|---:|---|---:|---:|
| 40 | [20,26) | 6 | 76822785 |
| 41 | [20,29) | 9 | 64435515 |
| 42 | [20,30) | 10 | 52351966 |
| 43 | [20,30) | 10 | 40623320 |
| 44 | [20,30) | 10 | 29297111 |
| 45 | [20,30) | 10 | 18416958 |
| 46 | [20,30) | 10 | 8022371 |
| 47 | [21,30) | 9 | 4306928 |
| 48 | [22,30) | 8 | 1234142 |
| 49 | [24,30) | 6 | 5198650 |
| 50 | [25,30) | 5 | 3439333 |
| 51 | [26,30) | 4 | 2260654 |

Thus 97 upper triangular cells and 97 pairwise distinct transposed cells, **194 complete continuous grid cells**, are excluded from the global maximizer set of the auxiliary Gamma objective. The exact lower-bound floors also yield the non-strict numerical comparison `V_q(e)-V_q(p,z) >= (1234142/1000000) q²`. The strict bound `> q²` follows directly from the 97 exact rational cell tests.

## Exact mathematical proof

The 189-row frozen integer recurrence yields 9,529 nonzero survivor coefficients. The normalized Bernstein coefficients `w[n,k]/binom(n,k)` are symmetric and nondecreasing from the boundary to the center; both `mu` and `M2` are coordinatewise nondecreasing on the relevant parameter domain.

For any closed parameter subrectangle `Q=[a,c] x [b,d]`, set
```
L=mu(a,b), H=M2(c,d), W_e=W(e), mu_e=mu(e).
```
Then `mu(p,z)>=L>=0`, `M2(p,z)<=H`, and `W(p,z)<=H-L²` throughout `Q`. With `t=1/q` and `q>=2`, the exact comparison satisfies

```
[V_q(e)-V_q(p,z)]/q²
    = W_e-W(p,z)-t(mu_e-mu(p,z))
    >= W_e-H+L²-t(mu_e-L).
```

The right side is affine in `t` on `[0,1/2]`. Its minimum is therefore the smaller of the exact rational endpoint values at `0` and `1/2`. For each candidate `R_ij`, subdivide into four closed `768 x 768` rational-grid subrectangles and compute the minimum of their two endpoint bounds using Python arbitrary-precision integers and `Fraction`.

The original Gamma moment kernel is `binom(n+m,n)/2^(n+m+1)`, implemented with the integer scale `C[n,m]=binom(n+m,n)*2^(2N-2-n-m)`, `Z=2^(2N-1)`. This is the same frozen 189-level model as PREFIX-731 through PREFIX-740, with no floating-point proof comparisons. The recomputed witness mean and variance numerator SHA256 regressions agree with the existing frozen source.

Every one of the 97 selected cells has exact lower bound **strictly greater than 1**. The minimum rational certificate floor multiplied by one million is 1,234,142, attained in row `j=48` (the selected cell with `i=22`). Exchangeability of the two independent same-family clocks yields the transposed cells, and no selected upper cell lies on the index diagonal.

## Exact deduplication against previous authored grid certificates

1. The original PREFIX-712 384-cell endpoint certificate used `e0=(0,3/20)`. The exact same 384-cell endpoint predicate was evaluated for **all 97 selected cells** and failed in each. This checks absence from that prior sufficient certificate, not a claim of failure of the underlying inequality.
2. The original immutable PREFIX-713 coupled, PREFIX-713 multi-competitor, PREFIX-716 and PREFIX-718 JSON coordinate sets were fetched and compared by reflected integer coordinate sets. Their respective intersection sizes with the 194 selected cells are all zero. The smallest coordinate maximum among those four historical sets is respectively 128, 79, 79 and 110; the largest coordinate maximum in the new set is 51.
3. Later PREFIX-729–PREFIX-740 author additions occupy central blocks with both indices >=30, or transverse regions with a coordinate >=70. Every new cell has one index in [20,30) and both <=51. Thus these later additional regions are index-disjoint. The earlier PREFIX-731–PREFIX-734 central squares are included in that statement.

Taking the PREFIX-740 author's exactly deduplicated baseline `141526/147456`:
```
141526 + 194 = 141720
141720/147456 = 5905/6144 = 96.110026041666...%
147456 - 141720 = 5736.
```
The remaining 5,736 cells are presently outside this author-level sufficient-exclusion union; they are not asserted to contain maximizers.

## Executed validation, immutable artifacts, and limits

- Actual 189-row integer recurrence reconstructed; `rows[189]` empty and 9,529 nonzero survivor positions checked. Symmetry and Bernstein monotonicity checked as exact integer comparisons.
- All 97 positive upper-cell bounds were computed with integer/`Fraction` arithmetic, in seven separately executed local batches of at most 20 cells. The initial 108-cell search also tested 11 cells not selected; those are not claimed as exclusions.
- Original PREFIX-713/716/718 JSON source bytes were read through the authenticated GitHub connector; all four precise set intersections were independently recomputed with integer coordinate sets.
- Program: `PREFIX741_R6_INNER_STRIP_194.py`; results with all 97 integer microfloors, 194 unique cell coordinates and source blob identifiers: `PREFIX741_R6_INNER_STRIP_194_RESULTS.json`. Both published to canonical main and read back at immutable commits. The combined published Python checker has **not** been rerun end-to-end; its row-scoped predicates reproduce the validated batch semantics. Independent mathematical review and formal task admission are outstanding.
- No shared Task CLAIM, Result, Review, Working Truth or Foundation change is asserted; this is a directly persisted portable scientific note under the existing PREFIX-675 objective.

## Next discriminating question

Expand the inner strip toward smaller `i` and larger `j` with adaptive 4x4 or stronger rational moment enclosures, checking both fixed and q-dependent witnesses. Run the combined PREFIX-741 script end-to-end from the frozen source, then independently audit the historical union (especially the original 384-cell PREFIX-712 sufficient test and later rectangular support) before promoting the 96.1100% author-level count.
