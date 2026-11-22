# T6 p=17 q14 split(7,7): sharp H0-constrained q0 occurrence ceiling

Date: 2026-11-22 (Asia/Hong_Kong). Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, publication `TP2-34B106D2512A298C9647`; authored as portable TASK research by the original Research lane `chatgpt-research-onhour-enterprise-math-20260923` (own Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`). Status: **AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED**. Formal T6 CLAIM/PROGRESS is separate.

## Exact scientific inputs

Use the immutable predecessor q14 complete one-power maximal-p17 vertical roster and cancellation-normalized support-disjoint signed pairs: `enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c`, `research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md`. The source author established 60 admissible named atoms, 1,907 complete vertical side rosters and 809,566 unordered opposing-disjoint pairs. These counts and the prior checker are **consumed**, not new output.

The already published budget-only corollary at `research_notes/portable_direct/onhour_20261122_t6_q14_sharp_joint_q0_budget_ceiling.md` established a sharp 26-occurrence ceiling before using observer equality. Here the new input is the actual shape observer `H_0`: equality of the **number of exponent occurrences on both sides**, including q0 and vertical atoms. No mixed congruence or affine search is used.

## Statement (sharp budget + H0 + named-support bound)

For either signed vertical roster `R_s`, let `n_s` be its number of atom occurrences **with multiplicity** (1..7); the sum of its q components equals 7. Every vertical atom `(q,r)` has `1<=r<=16`, cofactor `17q+r` with no prime divisor greater than 17, and positive side mass `289q+17r-1`. Vertical side mass is <=2331, and opposite signed named atoms do not coexist after cancellation. On the q0 side, an occurrence of residual `j` has mass `17j-1` with `1<=j<=16`; opposite equal j also cancel. Let `k_s` count q0 occurrences, again with multiplicity. Impose the genuine zeroth-moment equality

```
H0+: n+ + k+ = n- + k- =: m .
```

Then the exact maximum number of signed q0 atom occurrences in this relaxation is

```
                       k+ + k- <= 17.
```

This is attained with all named supports, composite cofactor factors and multiplicities retained. It improves the previously established budget-only 26 to a **sharp 17** after enforcing H0. The statement concerns a q14 **H0 + budget relaxation**, not a six-moment solution or global T6 exclusion.

## Proof

For a side with `n` vertical occurrences, because `sum q=7`,

```
M(R) = 2023 + 17 sum(r) - n >= 2023 + 16 n.
```

For n=1 the minimum is 2039, achieved by (7,1), with cofactor 120=2^3*3*5. For n=2, an all-r=1 split q+(7-q) is inadmissible: the three unordered splits (1,6),(2,5),(3,4) contain respectively a forbidden cofactor 103, 86=2*43, or 69=3*23. The first achievable two-atom cost is 2072 with (1,1),(6,2), cofactors 18 and 104. For every n=3,...,7 the lower bound 2023+16n is achieved by these smooth all-r=1 partitions:
n=3: (1,3,3); n=4: (1,1,2,3); n=5: (1,1,1,1,3); n=6: (1,1,1,1,1,2); n=7: (1,1,1,1,1,1,1). Here each number q abbreviates named atom (q,1); relevant cofactors 18,35,52 are all 17-smooth.

Thus the following *exact* minimum masses and maximum remaining q0 budgets apply to **every** possible complete side roster (irrespective of sign):

| n | minimum M_n | B_n=2331-M_n | n+floor(B_n/16) | n+floor(B_n/33) |
|---:|---:|---:|---:|---:|
| 1 | 2039 | 292 | 19 | 9 |
| 2 | 2072 | 259 | 18 | 9 |
| 3 | 2071 | 260 | 19 | 10 |
| 4 | 2087 | 244 | 19 | 11 |
| 5 | 2103 | 228 | 19 | 11 |
| 6 | 2119 | 212 | 19 | 12 |
| 7 | 2135 | 196 | 19 | 12 |

Because the cheapest q0 named atom (j=1) costs 16, while every other named atom costs at least 33, and **opposite sides have disjoint q0 supports**, orient the signs so that the j=1 atom, if present, is allowed only on the first side. Its q0 count is bounded by `floor(B_{n+}/16)`; the other side's count is bounded by `floor(B_{n-}/33)`. This remains a valid upper bound if j=1 is absent or a side is empty.

The common H0 occurrence count therefore satisfies

```
m <= min(n+ + floor(B_{n+}/16), n- + floor(B_{n-}/33)).
```

The table shows that the first term is >=18 for all n+ while the second is <=12. Hence

```
k+ + k- = 2m - n+ - n-
         <= 2(n- + floor(B_{n-}/33)) - n+ - n-
         <= n- - 1 + 2 floor(B_{n-}/33).
```

For `n-=1,2,3,4,5,6,7`, these seven upper bounds equal `16,15,16,17,16,17,16`, respectively. Consequently `k+ + k- <= 17`.

**Exact attaining witness, including H0:** choose on the positive side the vertical roster `[(7,1)]` (mass 2039, one occurrence), followed by 10 copies of the q0 named atom `j=1` (10*16). On the negative side choose `[(1,1),(1,1),(2,1),(3,1)]` (mass 2087, four occurrences), followed by 7 copies of q0 `j=2` (7*33). The vertical supports are disjoint because the first side uses only named (7,1), and the q0 supports are j=1 versus j=2. Total side masses are **2199** and **2318**, both <=2331, and H0 counts are `1+10=4+7=11`. Thus 10+7=17 is attainable. A second witness has vertical sides `[(7,1)]` and `[(1,1)]*5+[(2,1)]`, and q0 sides `j=1` repeated 11 versus `j=2` repeated 6; its H0 counts are 12 on both sides.

## Scope and next mathematical obligation

This reduces the admissible *q0 multiplicity* budget from 26 to 17 by using a true observer equality. Both witnesses are **only H0/budget-support witnesses**. They have not been tested for `H_1,...,H_6`, mixed saturated congruences or lower-prime completion; none is claimed to be a cheaper T6 collision. The exact q14 Source preflight, nonauthor examination and independently authorized affine stage retain their original scopes. No original predecessor CLAIM/Run is adopted by this GitHub note.

The next discriminating mathematical step is to apply an independently justified `H1` / denominator-reciprocal congruence restriction to the finitely bounded H0-consistent q0 counts, retaining the same named vertical supports and exact denominators, **after** current Source authorization and predecessor plan are verified. Do not repeat the completed roster census or treat these numeric bounds as full six-moment feasibility.
