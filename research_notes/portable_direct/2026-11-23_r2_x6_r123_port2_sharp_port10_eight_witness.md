# X6 R123 — sharp Port-2 near-direction bound and an eight-direction Port-10 witness

Date: 2026-11-23. Mathematical status: **AUTHOR EXACT FINITE PROOF / INTEGER RATIONAL REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.

## Scope

The conditional positive-four-weight six-pair BRC integer observer, with physical integer Port, four heights and all six gaps exactly as defined in [R121](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md). The [R122 integer exclusion envelope](https://github.com/awdawmip/enterprise-math/blob/0687aa24f5402da3b35f914dd6907967a9805b94/research_notes/portable_direct/2026-11-23_r2_x6_r122_small_port_near_exclusion_envelope.md) supplies its exhaustive six-gap 3/2 domination bound. This is an observer result, not an assertion about native P000/X6 physical time.

## Theorem 1 — Port 2 sharp bound

For **all** A,B,C,D>0, the strict 3/2-near unoriented direction set at integer Port p=2 has at most **four** elements. The bound is attained at the **integer physical weights (A,B,C,D)=(1,1,100,100)**.

The six capacities there are (2,101,101,101,101,200). The exact optimum is eta_2=48/101, and the threshold is 72/101. The complete strict-near set and exact scores are:

| direction | F_w |
|---|---|
| (0,2,-1) | 48/101 |
| (1,-2,1) | 55/101 |
| (1,0,0) | 1/2 |
| (2,-1,0) | 1/2 |

Proof: R122 proves a four-row *necessary* candidate set at Port 2 uniformly in positive physical weights. Direct exact evaluation above proves all four strict inequalities F_w(a)<72/101 (in particular 1/2<72/101 and 55/101<72/101). Hence the upper bound is attained; no other integer direction can be near. This closes the **maximum cardinality** at Port 2, not the full per-weight Port-2 atlas.

## Theorem 2 — eight exact near directions at Port 10

For the integer positive physical weights **w=(1,3,4,18)** and integer Port p=10, the optimum is eta_10=11/19 and the threshold is 33/38. The complete strict-near set has **eight** elements:

| direction | F_w |
|---|---|
| (1,-3,1) | 19/22 |
| (1,0,0) | 3/5 |
| (4,-1,0) | 11/19 |
| (5,-4,1) | 3/5 |
| (5,-1,0) | 3/5 |
| (6,-4,1) | 12/19 |
| (9,-5,1) | 3/5 |
| (9,-2,0) | 6/7 |

All listed fractions are strictly below 33/38; e.g. 19/22<33/38 by cross-multiplication 722<726. Thus the maximum near-direction count at Port 10 is **at least 8**. R122's universal bound is 20; the interval 8–20 remains open.

## Exact check and reproducibility

The attached [JavaScript integer checker](x6_r123_small_port_sharpness_verify.js) enumerates **all 27** unoriented directions of Port <=2 and **all 1,935** of Port <=10, recomputes six gap numerators and six weight-sum denominators, and performs rational comparisons using exact integer cross-products. It separately recomputes the minimum, threshold and full strict-near direction list. It verifies the two witnesses and the exact scores in the attached JSON. Independently, Python's Fraction arithmetic reproduced the scores and sets.

No continuum sampling or approximate arithmetic establishes the claim. The general upper bound at Port 2 is inherited with its exact finite domination proof from R122. The Port-10 case is an exact finite witness, not a universal maximum theorem.

## Frontier

Find the sharp global maximum for Ports 3–10 and classify attainable near subsets using the four *coupled* positive weights (rather than independent pair capacities). Preserve the frozen model, exact integer Port and R121 source pin; reserve native X6/R063 dynamics for its separate actual authority.
