# R5 — Unique exact optimal fixed batch in the last noise chamber, all error counts

**2026-11-18 | AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**

**Frozen model.** Scalar indexed-center observer with named hypotheses h=0,...,255; legal physical budgets 214,...,314; exact input SHA256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b and source pin 435e77af0d180eac32bd1f9c4c464bc4010b7551. Correct real readout is within eta of integer N_h(k). At most f arbitrary unmarked errors; tau=2eta; fixed batch means all queries are scheduled in advance and paid even if a reading would suffice to stop earlier.

**THEOREM (all f).** Set
T = 1876919155234970890319953920000,
D = 1882951873548292168718745600000.
For every real tau in [T,D) and every integer f>=0, the exact minimum fully prepaid fixed-batch cost is

C_fixed_batch(f,tau) = 957*(2*f+1).

The unique optimal multiset, up to ordering, comprises **2f+1 copies each of 217, 218, 224 and 298**. It uses 4*(2f+1) queries. At f=8 the exact fixed-batch cost is **16,269**, comprising 68 queries.

## Four disjoint actual-pair witnesses

At both tau=T and tau=D-1 (and therefore throughout the entire chamber), the exact sets of budgets that separate four pairs are:

| Named pair | Full separation set | Least budget |
|:--|:--|--:|
| (11,14) | {217} | 217 |
| (4,10) | {218,219} | 218 |
| (0,64) | {224,...,290} | 224 |
| (16,32) | {298,...,311} | 298 |

All four sets are **pairwise disjoint**. Every correct identification batch for at most f arbitrary unmarked errors must have at least q=2f+1 separating observations for each pair. This follows from the two-hypothesis indistinguishability lemma: when a batch has d<=2f separating positions, partition those positions between the two possible true hypotheses with at most f corruptions for either, and choose common interval readings in the remaining positions.

Since the four witness separation sets do not intersect, their q required observations must be paid for separately. Each has per-query minimum cost 217, 218, 224 and 298, respectively. Hence cost >= q*(217+218+224+298)=957q. Equality is possible only when **exactly q copies of each cheapest budget** appear and no extra queries are paid, proving uniqueness.

For the matching upper bound, the four budgets {217,218,224,298} were verified to separate **all 32,640 unordered pairs** of the 256 hypotheses at the hardest threshold D-1. For every pair, one of the four queries yields disjoint correct-reading intervals. Repeating each q times therefore ensures >=q separated positions for every pair, giving exact decoding with at most f arbitrary corruptions and cost 957q. This establishes the theorem.

The exact pair-coverage histogram across the four budgets for all 32,640 unordered pairs is:
1 separating budget: 560 pairs; 2: 2,576; 3: 11,984; 4: 17,520.

## Proof-check and scope

Run the accompanying Python standard-library verifier against the unchanged frozen 256x101 integer count JSON file:
python3 VERIFY_R5_NEAR_CHAMBER_ALLF.py EXACT_R5_ALL_101_BUDGETS.json

Actual local execution: exit code 0; stderr PASS_R5_LAST_CHAMBER_ALLF_UNIQUE_FIXED_BATCH. It checks the complete separation sets for four named pairs at both chamber endpoints, their disjointness, and pair coverage at D-1 over every pair. Only exact integer operations are used. This complements the preceding RESEARCH.md in the same directory, which certified the exact global identifiability threshold and maximal predecessor gap. Independent review is pending.

The theorem applies only to the declared scalar indexed-center observer and all-paid fixed batches. It does not reduce native X6 path, joint relations, provenance or future observations to a coordinate quotient. For observation-dependent stopping or adaptive queries the exact optimum is a separate question.

**Next:** determine the largest tau for which *some* three-budget identifying batch exists; analyze the exact general-f optimum with fixed query order but observation-dependent stopping in the last chamber, and review the current frozen-input provenance.
