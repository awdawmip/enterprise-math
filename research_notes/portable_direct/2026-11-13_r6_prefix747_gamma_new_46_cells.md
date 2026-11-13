# PREFIX-747-R6 — 46 new complete BRC–Gamma grid exclusions by 8×8 exact enclosures

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675; predecessor: PREFIX-746.
Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Author identity: `EM-DIRECT-E5C659` (locally allocated direct-research handle; no authenticated native CLAIM).
Activity: `RA-4B660204C01B01C2A0AF1982`.
Grade: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Exact theorem

Retain the pinned 189-row survivor-count kernel and the auxiliary construction from PREFIX-741 and PREFIX-746: `T_p,T_z` are independent unit-rate Gamma clocks; `Y=max(T_p,T_z)`, `mu(p,z)=E[Y]`, `M2(p,z)=E[Y²]`, `W=M2-mu²`, and `V_q=q²W-q mu`. Let `e=(0,73/500)`. Define **closed** 384-grid cells
`R_ij=[i/384,(i+1)/384]×[j/384,(j+1)/384]`.

For **every real q >= 2** and **every continuous (p,z)** in each of the following **23** cells and their **23** distinct coordinate transposes,

```
V_q(e) - V_q(p,z) > 6 q² > 0.
```

In particular, these 46 full cells contain no global maximizer of this frozen **Gamma auxiliary objective**.

| j | new original i values | count | min floor(10^6 × exact normalized lower bound) |
|---:|---|---:|---:|
| 45 | 7 | 1 | 29948255 |
| 46 | 7, 8 | 2 | 21989561 |
| 47 | 7, 8, 9 | 3 | 14749094 |
| 48 | 7, 8, 9, 10 | 4 | 8233883 |
| 49 | 8, 9, 10, 11 | 4 | 6037447 |
| 50 | 10, 11, 12 | 3 | 8455657 |
| 51 | 12, 13, 14 | 3 | 11955704 |
| 52 | 13, 14, 15 | 3 | 11934432 |
| **Total** | | **23** | **6037447** |

The weakest tested cell is `(8,49)`, with `floor(10^6 G_8,49)=6037447>6000000`.

## Exact proof

The pinned BRC recurrence has 189 rows and 9,529 nonzero survivor coefficients. The checked normalized Bernstein symmetry and monotonicity of the frozen Gamma construction imply that `mu` and `M2` are coordinatewise nondecreasing. For any closed rational subrectangle `Q=[a,c]×[b,d]`, put `L=mu(a,b)>=0`, `H=M2(c,d)`, `mu_e=mu(e)`, `W_e=W(e)`, and `t=1/q∈(0,1/2]`. Then

```
(V_q(e)-V_q(p,z))/q²
  = W_e - M2(p,z) + mu(p,z)² - t*(mu_e-mu(p,z))
 >= W_e - H + L² - t*(mu_e-L).
```

The last expression is affine in `t` so its minimum over `[0,1/2]` occurs at an endpoint. Partition each of the 23 cells into 64 closed rational subrectangles with `k=8` in each coordinate. Let `G_ij` be the minimum of the 128 exact rational endpoint values, grouping the two t-endpoints for each subrectangle. All 23 computed `G_ij` have `floor(10^6 G_ij)>=6037447`, yielding the uniform strict gap `>6`. Symmetry of the two independent clocks gives the same result for each transpose. The 23 originals all lie strictly above the diagonal so the transposes are distinct.

The exact integer recurrence and witness digests were checked locally against the frozen published dependency:
```
SHA256(str(mu(e).numerator)) = 797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e
SHA256(str(W(e).numerator)) = 814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae
```
The reproduction of the earlier `(12,48)` 4×4 certificate exactly matched `1114756` from PREFIX-745 before computing the new cells. Every one of the 23 new 8×8 probes was executed locally in independently bounded Python standard-library exact-Fraction runs; each also checked the original PREFIX-712 unsplit witness `(0,3/20)`, and all 23 original predicates had strictly negative lower bounds. Per-cell integer microfloors and regression results are in the companion JSON. The published compact dependent checker is separately available; full one-process end-to-end replay of that published checker is pending.

## Nonoverlap and conditional author union

Exact coordinate-set comparisons against the published PREFIX-742, 743, 744, 745, **and currently published PREFIX-746 (57 upper cells)** results returned zero intersections for all 23 originals. PREFIX-741's region uses `i>=20` and cannot intersect this wedge. Earlier PREFIX-713/716/718 extras are located at upper-coordinate indices >=79, whereas these new cells have `j<=52`; PREFIX-712's original sufficient test was explicitly rerun on each candidate and returned negative. The PREFIX-729–740 areas recorded in PREFIX-741 do not intersect this small-index wedge.

**Conditional on the previously reported PREFIX-746 author-level union of 142056**, this adds 46 new reflected complete cells:
```
142056 + 46 = 142102 / 147456 = 71051/73728 ≈ 96.36908637%
unexcluded cells under this author certificate union = 5354.
```
This area count remains conditional on the historical author-union baseline; a full independent audit of every older certificate is outstanding. The 46-cell inequality is supported independently by its exact per-cell checks.

## Smallest unfinished question

Independently run the complete published checker with all dependencies; independently audit the historical certificate union; then test the adjacent finer-grid boundary at `(7,49),(9,50),(11,51),(12,52)` or extend to `j>=53`, changing witness or adaptive subdivision if needed. Retain frozen science and avoid taking any unrelated active Owner/CLAIM.
