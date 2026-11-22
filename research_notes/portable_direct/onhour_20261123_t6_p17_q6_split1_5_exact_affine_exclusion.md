# T6 p17 vertical order 6 split (1,5): one exact sphere leaf, zero admissible q0 completions

2026-11-23 (Asia/Hong_Kong). **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Preserves original TASK_RESEARCH owner/source boundaries and immutable T6 input pin `d84bd940cfb093cdc60e569f15cad58772a51dca`. Mother T6 objective remains OPEN.

## Precise proposition

For cancellation-normalized signed exponent denominator multisets with mass ≤2331 on each side, let the v17=1 vertical total order equal six, split as positive q=1 and negative q=5. Assume the six globally necessary p17 mixed congruences derived from full equal H0,…,H6, after legitimate v17≥2 cancellation:

```
Σ_{v17=1} signed_m(a) * a_cofactor^(-j) ≡ 0 (mod 17^j),  j=1,…,6.
```

All integer named residual atoms (q,r), 1≤r≤16, retain their full denominator 17(17q+r), cost 289q+17r−1, same-side multiplicity and two-sided cancellation; all q0 signed compensators are allowed. We search the **superset of all residues** without requiring separate 17-smooth cofactors, so the frozen smooth subfamily is covered.

**Result: there is no admissible signed q0 compensation in split (1,5)**. Any actual full T6 collision in the frozen model would have to satisfy these congruences, regardless of its lower-prime completion.

## Complete finite exact enumeration

Reuse the original saturated 16-dimensional p17 q0 basis and exact Gram–Schmidt checker from `T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py`, Git blob `2c1aa73268aa11300a32b9923e3bdbddb6190813`. Its full-lattice determinant is 17²¹. Generate every budget-valid vertical roster at q=1 (16 states) and q=5 (30,040 states), with signed side orientation unique up to exchange. Remove pairs with any identical named vertical atom on opposing sides, because these cancel to an earlier q-order.

| Exhaustive scope | Count |
| --- | ---: |
| Raw vertical side pairs | 480,640 |
| Shared-atom pairs, lower-order reductions | 90,937 |
| Primitive pairs searched | **389,703** |
| Exact GS recursion nodes | **1,293,850** |
| Full weighted-sphere leaves | **1** |
| Two-side budget-valid q0 solutions | **0** |

The smallest vertical masses are 305 and 1461, so for all pairs the necessary squared weighted-sphere radius is bounded by **4,861,576**, below the exact minimal squared GS diagonal (**approximately 17,372,418.62**). Every integer affine q0 completion is enumerated using exact rational floor/ceil candidates at each GS coordinate. This is complete; no floating-point equality or approximate cutoff is used.

### The unique relaxed leaf

At the single GS sphere leaf, named vertical atoms are positive `[(1,4)]` and negative `[(1,8),(2,3),(2,9)]`. The exact q0 signed vector indexed by r=1,…,16 is

```
(-20,5,-7,0,2,-12,6,1,2,3,-3,-1,-1,2,-2,3).
```

This vector **does** satisfy all six mixed modular congruences, and its weighted squared norm is 4,162,929, below its specific sphere squared radius 4,202,026. Nevertheless it violates both **separate** budgets:

| Quantity | Positive | Negative |
| --- | ---: | ---: |
| Vertical mass | 356 | 1782 |
| q0 mass | 3274 | 3371 |
| Total exponent mass | **3630** | **5153** |

Thus the relaxed sphere is necessary but not sufficient, and its **one** leaf is rigorously excluded by original mass constraints. Keeping this witness prevents mistakenly claiming the sphere itself is empty or that modular lattice has no candidates.

Two executions of the standalone author exact script gave the same counts; recorded local certificate SHA256 is `454996d20f6e3e04b9cdf74971cde62dbae561710d3b36056f7f0dd88a41e0d2`. Published compact reproducer imports the immutable-described existing q5 code and independently verifies the unique leaf's six congruences and budget; its separate remote execution is not asserted. The exact locally executed standalone file is preserved in the current runtime; the GitHub author certificate contains the witness and coverage counts.

## Boundary and next precise action

The immediately preceding split (0,6) is already author-excluded by **zero sphere leaves**. This split (1,5) has **one relaxed leaf but zero admissible q0 completions**. Remaining q6 splits **(2,4)** and **(3,3)** are the next unfinished scientific units. Earlier q5 and accepted q1–q4 work are unchanged. Source semantic PROGRESS, independent review and global T6=2332 remain pending. No maintenance identity or historical ownership is used.
