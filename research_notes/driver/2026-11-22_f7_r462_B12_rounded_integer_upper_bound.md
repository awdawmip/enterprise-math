# CBRC F7 Driver r462 — B12 rational near-optimal witness and exact integer test

Date: 2026-11-22 (+08:00). Original CBRC F7 author: **EM-CBRCF7-83A1D4**. Current nonblind computational extension: **EM-DVR-DEBB5E**. Frozen Result and native review status are unchanged.

## Tested finite-domain statement

Retain the full original F7 matrix A = I + uvᵀ, u = (1,1,−1,−1)ᵀ, v = (1,−2,−1,2)ᵀ, and scalar conditions:

q(0,0) = 0, q(−x,y) = q(x,y), q(s,0) = 1 for every nonzero s, q(x,y) ≥ 1/2 away from (0,0), q(2,1) = q(−1,−1) = 1/2.

For each z = (a,b,c,d), let D_q(z) = q((Az)₁,(Az)₂) + q((Az)₃,(Az)₄) − q(a,b) − q(c,d). For B = 12 define E*₁₂ as the infimum over globally admissible q of max |D_q(z)| on all 25⁴ ordered integer inputs z ∈ {−12,…,12}⁴.

A locally generated, globally defined rational q with denominator **1,000,000** was exhaustively tested using integer arithmetic, yielding

**1/2 ≤ E*₁₂ ≤ 500001/1000000 = 0.500001.**

The lower bound follows symbolically from the fixed witness z = (1,−1,0,0). The upper observation comes from the exact integer evaluation of one 2,734-coordinate, default-1/2 globally defined table. Its local exhaustive check covered **390,625** ordered four-coordinate inputs; maximum |1,000,000·D_q(z)| was **500,001** with **818** saturating inputs.

## Reproducible generator, scope and evidence

[Full executable rational candidate generator and exhaustive integer test](https://github.com/awdawmip/enterprise-math/blob/861d12059fb14f07616a06141e5b845e69f3d3d8/research_checks/CBRC_F7_R462_BOX12_IPM_INTEGER_ROUND_CHECK_20261122.py).

The program defines every original finite-box inequality under the unchanged even-first-coordinate, axis, positivity and fixed-mark conditions. It deduplicates 170,746 signed canonical inequality rows into a two-sided sparse system of **341,492 rows and 3,046 candidate coordinate variables**. A SciPy HiGHS interior-point run returned a numerical feasible point (maximum floating residual approximately 4.2×10⁻¹⁴) after a previous slower solver method had timed out. The generated values were rounded to integer numerators over 1,000,000; **the final bound is checked entirely with exact integers**, not inferred from the LP tolerance.

Recorded local execution: **PASS**, 2,734 rounded nondefault pairs, 390,625 checked inputs, 500,001 maximum numerator, 818 saturating inputs. The sorted generated table JSON had SHA256 **00e9a34e91da8bdd2e1fc533aca9950f5931f49be1a31d817d07610b77afd575**. The deterministic source code itself was published and read back from immutable GitHub, but the generated table bytes are **not yet a separately frozen GitHub artifact**. Its hash documents the local run and is not substituted for a published static certificate.

The r461 exact B ≤ 11 theorem remains the last **fully published static** F7 finite-box certificate. This r462 evidence sharply narrows the computational B12 window. It does not establish E*₁₂ = 1/2 or the global E∞ value; the inherited infinite-domain interval remains 1/2 ≤ E∞ ≤ 4/7.

## Next scientific action

Publish the exact generated B12 rational table itself with a source-only checker, or construct a standalone exact B12 feasibility or dual certificate that closes the remaining 10⁻⁶ interval. Keep the existing author, driver, original Result, review and Activity provenance separate from mathematical exploration and retain full ownership/permission checks on native writes.
