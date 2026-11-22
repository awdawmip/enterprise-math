# T6 maximal p17 valuation-one / q7 split(2,5): exact affine mixed-congruence exclusion

Date 2026-11-23 (Asia/Hong_Kong). TASK_RESEARCH ordinary logical lane `chatgpt-research-onhour-enterprise-math-20260923`, researcher source attribution `EM-X6-FB6990`, original public SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Evidence **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. T6 mother objective OPEN. Neither original Source publication nor Activity confers an active CLAIM/Result.

## Frozen inputs and globally necessary congruences

Frozen scientific task: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` @ `d84bd940cfb093cdc60e569f15cad58772a51dca` with blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`. Each side has exponent mass at most 2331. Preserve each full named denominator, signs, multiplicities, and equality of all original `H0,...,H6`. After cancelling common named atoms and using the existing author p17² cancellation lemma, write the maximal-p17 valuation-one atoms as `a=17(r+17q)` with `q>=0`, `1<=r<=16`, and exact exponent mass `289q+17r-1`.

If `u_r` is the signed q0 multiplicity and `m_(q,r)` is the signed vertical atom multiplicity, original full observer equality implies the six **necessary** modular equalities, for `j=1,...,6`:

```
sum_(r=1..16) u_r * inverse(r^j,17^j)
 + sum_(q>=1,r=1..16) m_(q,r) * inverse((r+17q)^j,17^j)
 == 0 (mod 17^j).
```

The lower-prime denominators are unrestricted; this is not a p17-only equality of rational moments.

## Exact finite computation and coverage

The partition-and-named-residue generator yields precisely 152 admissible vertical order-2 side rosters and 30,040 vertical order-5 rosters under the side mass budget. Thus the oriented product contains **4,566,080** exact named side pairs. Exactly **1,359,386** share a vertical named atom across sides (and reduce to lower vertical order), leaving **3,206,694** primitive pairs in the fixed (2,5) split.

The homogeneous q0 solution lattice reuses the original saturated 16x16 integer row basis from `research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json` (blob `d9ac014355a6a1058cc8a0cf2141a01082628881`) with index `17^21`. The six exact modular lifts give an integral particular representative, and every possible q0 signed completion is that representative plus this full homogeneous lattice.

Put `W=diag(16,33,...,271)`. The true separate mass budgets imply the necessary weighted-ball inequality

```
||W*u||^2 <= (2331-cost(V+))^2 + (2331-cost(V-))^2 = R^2.
```

Maximum `R^2=3,774,069`. The exact minimum squared orthogonal Gram–Schmidt diagonal of the weighted saturated lattice is

```
8350069911612335617606677214061177705401058080646556447012234889468081355909
/480650972868542992444263969893692042421717754534280313801217347854273
```

(about 17,372,418.62), strictly larger than every radius squared in this split. For each affine center only the exact floor/ceiling choices can be inside the necessary sphere. Recursive exact `Fraction` GS evaluation with provable partial-norm pruning therefore exhausts the entire integer solution space; there is no floating-point equality tolerance.

The original standalone Python/SymPy computation was executed for all ten disjoint left-index ranges `[0,16),[16,32),...,[128,144),[144,152)` with all 30,040 right rosters in each range. Ten source JSON SHA-256 hashes and bounds are stored in the published certificate. Results:

| Statistic | Exact total |
|---|---:|
| Raw named pairs | 4,566,080 |
| Shared vertical support | 1,359,386 |
| Primitive pairs | 3,206,694 |
| Exact GS recursion nodes | 7,848,081 |
| Complete necessary-sphere leaves | **0** |
| Original-budget-valid q0 completions | **0** |

The compact reproducible Python checker `research_checks/T6_P17_Q7_SPLIT2_5_MIXED_AFFINE_CHECK_20261123_0405.py` was published to GitHub, reusing the original pinned q5 checker without altering its 16D lattice; **this compact wrapper has not separately been executed after publication**. The standalone calculation and chunk JSON are the actual author execution evidence, not an independent review.

## Proposition and next real unit

**Author exact finite conclusion:** no primitive maximal-p17 valuation-one vertical order-seven signed pair of split (2,5) respecting both mass budgets can satisfy all globally necessary mixed 17-adic reciprocal congruences; arbitrary lower-prime completion cannot restore a necessary modular candidate.

Combine with the separately saved q7 split(0,7) and split(1,6) source records only at their own author evidence strength. Remaining order-seven split **(3,4)** is the next smallest unit; then examine q8, maintaining the exact current frozen Source selection, original side budgets, signed support, and lower-prime completion obligations. Do not repeat accepted earlier campaigns or existing q6 computations, and do not advertise p17 or global T6 completion.

## Control boundary

The exact original T6 Task read `onhour-20261123-0315-t6-current-task-read-v1` was later consumed `SUCCEEDED / error=null`, projecting owner `taskbook/unassigned`, current `state.claim_id=null`, and `execution_authorized=false`. Historical `onhour-20261123-0105-t6-current-source-cont-v1` succeeded but is not current write authority. No T6 CLAIM/RUN, native semantic PROGRESS, Result freeze or independent mathematical admission is claimed. Only the actual Research lane is represented.
