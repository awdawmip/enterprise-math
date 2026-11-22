# T6 / maximal p=17 / vertical order 6 split (0,6): exact global mixed-congruence exclusion

2026-11-23 (Asia/Hong_Kong). **TASK_RESEARCH portable author result; AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Mother task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` remains OPEN.

## Statement and model

For full exponent multisets of mass at most 2331 on each side and equal shape observers H0,…,H6, use frozen task `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` at commit `d84bd940cfb093cdc60e569f15cad58772a51dca`. After cancelling common atoms with denominator divisible by 17² (see prior author result `onhour_20261123_t6_p17_high_valuation_and_global_mixed_congruences.md`), the remaining signed v17=1 part satisfies, for j=1,…,6,

```
sum_{17∤a} m_a * a^{-j} = 0  (mod 17^j).
```

In the vertical-order-6, signed split (0,6), put every q≥1 vertical atom on the negative side, leaving no vertical atom on the positive side. Atom (q,r) denotes the full denominator 17(17q+r), mass 289q+17r−1, 1≤r≤16. The q0 compensators have denominators 17r and masses 17r−1, r=1,…,16. Their signed multiplicities preserve actual named factors, signs and repetitions.

**Result.** No cancellation-normalized split (0,6) configuration of this kind satisfies all six globally necessary mixed congruences with both side masses ≤2331. This holds even if the 17-free remainder is arbitrary. The larger class allowing all r=1,…,16, without an extra 17-smooth filter, was searched; thus the frozen smooth admissible subfamily is included.

## Exact calculation and finite completeness

Reuse the p17 q0 saturated 16-dimensional integer lattice at pinned Git blob `d9ac014355a6a1058cc8a0cf2141a01082628881`, already checked in `T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py` (blob `2c1aa73268aa11300a32b9923e3bdbddb6190813`). Its determinant is 17²¹ and the six modular equations have precisely that index by a unit inverse-Vandermonde minor. Thus the 16 basis rows span the entire q0 kernel; no modular solutions are lost.

Enumerate every finite nondecreasing multiset of named vertical atoms whose q-values sum to six and whose total exponent mass ≤2331: **47,628 complete vertical rosters**. There is no opposite-side shared vertical named atom because the positive vertical roster is empty.

For each vertical roster, construct an integral affine particular q0 correction using exact six successive modular solves, and search the entire affine lattice using exact rational Gram–Schmidt and a **necessary** weighted Euclidean ball for two-sided q0 mass. Every budget-feasible q0 vector lies in this ball:

```
||diag(17r-1) * u||² ≤ B_plus² + B_minus².
```

The smallest vertical mass is 1750; consequently across all rosters R²≤2331²+(2331−1750)²=**5,771,122**. The minimal squared GS diagonal is exactly

```
8350069911612335617606677214061177705401058080646556447012234889468081355909
/480650972868542992444263969893692042421717754534280313801217347854273
```

(about 17,372,418.62), strictly larger than every radius squared. At each GS coordinate only floor and ceiling of the exact affine center can possibly enter the ball. The exact rational recursive search visits **224,133 nodes**, reaches **0 full sphere leaves**, and finds **0 budget-valid q0 completions**. Branch rejection is based on a strict rational squared-norm comparison; there is no numerical near-equality cutoff.

The original complete local calculation was executed twice, with identical certificate and SHA256 `69ee91f15f82e7a98d4311d0a089175fa9df67d1de3850822ce49c250179855d` for the standalone local evidence JSON. The repository includes a compact reusable q6 checker which imports the immutable-described q5 checker in the same directory and asserts the exact integer totals; this new wrapper's separate execution is **not** claimed here. The repository's corresponding author certificate preserves the exact counts and digest-independent semantic fields.

## Scope and recovery

Previous q5 complete mixed-congruence exclusion is reused, not recomputed or reassigned. Remaining q6 splits **(1,5), (2,4), (3,3)** are OPEN, along with higher p17 orders, lower maximal primes, the global T6 threshold, independent mathematical review and formal Source Result. The next useful science is the exact split (1,5) with the same globally necessary mixed congruences, preserving distinct signed-side budgets. Avoid replacing this condition by stronger equality of p17-only rational moments.

Provenance: original ordinary Research lane `chatgpt-research-onhour-enterprise-math-20260923`; original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. No new winning T6 CLAIM/RUN or native semantic PROGRESS is asserted. Source task pin and P000 unchanged.
