# R5 — Complete nine-chamber fixed mixed-fault noise-cost theorem

Date: 2026-11-17. Frozen scientific input `435e77af0d180eac32bd1f9c4c464bc4010b7551`; author result **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. This extends this directory's `RESEARCH.md` (first three chambers) and previously established error-free nine-step absolute-noise cost phase diagram to **every nonnegative erasure and corruption allowance**.

## Problem and theorem

Observer: frozen 954-event indexed-center positive integer count `N_b(k)`, 256 effective masks `b∈{0,...,255}`, 101 allowed integer budgets `214≤k≤314`. Count semantics are exact cohort subset-zeta `N_b(k)=Σ_{T⊆b} A_T(k)` at the declared frozen input. A fixed multiset of queries may repeat budgets; its cost is `Σk`. Every intact observation is a real `y` satisfying `|y-N_b(k)|≤η`; in addition there may be up to `e` marked erasures and up to `f` adversarial, unmarked arbitrary replacements at distinct sample positions. The adversary knows the mask. We require worst-case unique decoding of all 256 masks.

Let `τ=2η≥0`, `r=e+2f+1`, where `e,f` are arbitrary nonnegative integers. Define `Δ_{-1}=0`, and for `j=0,...,8` the exact constants `Δ_j` below.

**Theorem.** For every `j=0,...,8` and every real `τ∈[Δ_{j-1},Δ_j)`, the least possible fixed-query total cost for adversarial mixed faults is **exactly `r C_j`**, where the indicated three budgets, each repeated **`r` times**, achieve the value:

| `j` | `Δ_{j-1}` (inclusive) | `Δ_j` (exclusive) | three budgets | `C_j` |
|---|---|---|---|---:|
| 0 | 0 | 76289178155959966960189440 | (214,223,294) | 731 |
| 1 | 76289178155959966960189440 | 3133722521542003559403356160 | (214,223,295) | 732 |
| 2 | 3133722521542003559403356160 | 13883516118328421520506880000 | (214,223,296) | 733 |
| 3 | 13883516118328421520506880000 | 25845652773852463277015040000 | (215,223,296) | 734 |
| 4 | 25845652773852463277015040000 | 58182461585441404127941754880 | (216,223,296) | 735 |
| 5 | 58182461585441404127941754880 | 92195224223274674159616000000 | (216,223,297) | 736 |
| 6 | 92195224223274674159616000000 | 267753525139190986466918400000 | (217,223,297) | 737 |
| 7 | 267753525139190986466918400000 | 651779164849779092423599718400 | (217,224,297) | 738 |
| 8 | 651779164849779092423599718400 | 1744659037213380157479321600000 | (217,224,298) | 739 |

The theorem covers all `0≤2η<1744659037213380157479321600000`. It makes no cost claim for `2η` at or beyond this final limit. Optimality of the *value* and existence of the displayed schedule are established; uniqueness of optimal fixed multisets in the later chambers is not needed.

## Load-bearing proof

**Criterion.** A pair of masks `(a,b)` has a guaranteed distinguishing sample at `k` if and only if `|N_a(k)-N_b(k)|>τ`; their two permitted analog intervals are then disjoint. The exact necessary-and-sufficient condition for correcting `e` erasures and `f` arbitrary replacements is that every mask pair have at least `r=e+2f+1` such strong sample *positions*, including multiplicities. Necessity follows by erasing up to `e` strongly distinct samples and partitioning the at most `2f` remaining positions between the two candidate error sets, while choosing overlapping intervals at weak positions. Sufficiency follows by triangle/disjoint-coordinate counting after erasures.

**Upper bound.** For each displayed three-budget tuple `Q_j`, the finite exact integer identity

`min_{a<b} max_{k∈Q_j}|N_a(k)-N_b(k)| = Δ_j`

is verified on all 32,640 unordered pairs. Therefore, if `τ<Δ_j`, every mask pair has at least one strong coordinate among the three. Repeating each coordinate `r` times provides at least `r` strong positions and costs `rC_j`.

**Exact integer dual lower bound.** At the left endpoint `τ_j=Δ_{j-1}`, the companion JSON provides for every `j` a short list of nonnegative **integer** weights `λ_{j,a,b}` attached to distinct mask pairs. The complete certificate establishes two assertions:

`Σ_{a<b} λ_{j,a,b}=C_j`

and, for **every one of the 101 budgets** `k`,

`Σ_{a<b} λ_{j,a,b} · 1[|N_a(k)-N_b(k)|>τ_j] ≤ k.`

Let `n_k` be the query multiplicities of *any* fixed strategy feasible at some `τ≥τ_j`. The strong-disagreement set can only shrink as `τ` increases. Hence each certified pair requires `Σ_k n_k 1[|N_a(k)-N_b(k)|>τ_j]≥r`. Summing these inequalities with the integer nonnegative weights, and applying the 101 certified dual inequalities, gives

`Σ_k k n_k ≥ Σ_k n_k Σ_{a<b}λ_{j,a,b}1[|N_a(k)-N_b(k)|>τ_j] ≥ rΣ_{a<b}λ_{j,a,b}=rC_j.`

This matches the upper bound throughout `[τ_j,Δ_j)` and proves the theorem for **every** `e,f`, including unbounded repetition counts. It is an exact rational/integer dual certificate; no floating-point LP output is used as a proof premise.

**Small duals.** The middle window uses pair `(0,64)` with weight equal to the middle budget (223 or 224). The late window uses pair `(16,32)` with weight equal to the late budget (294–298). The early window requires at most three pairs: its nine exact pair/weight lists are in the JSON and Python verifier. For example, chamber `j=4` (cost 735) uses early `(1,2):214` and `(2,8):2`; their combined strong-support weight never exceeds the individual query budget, while their weights total 216. This resolves the case where no single early witness alone proves the optimum. The duals combine BRC-derived source-count distinctions without collapsing which mask pairs carry them.

## Verification

`VERIFY_R5_NINE_CHAMBER_MIXED_FAULT_DUALS.py` is a Python-standard-library proof-checker. It reconstructs all 25,856 integer counts from pinned nonnegative source-requirement cohorts with exact 8-stage subset-zeta addition, verifies 293,760 exact unordered-pair/three-budget comparisons, checks every one of the 909 budget-level integer dual inequalities, and checks the nine sums of weights. With the second optional input it independently compares all 25,856 integer counts to an earlier exact full-budget DP table. Local checked run yielded `PASS_R5_NINE_CHAMBER_ALL_EF_INTEGER_DUALS`.

Reproduce in this directory using the existing frozen R5 reproduction bundle's two input files:

```bash
python VERIFY_R5_NINE_CHAMBER_MIXED_FAULT_DUALS.py INPUT_COHORTS.json EXACT_R5_ALL_101_BUDGETS.json
```

Required input SHA-256: compact `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`; optional independent full table `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Both were present in the previously saved `EnterpriseMath_R5_mixed_fault_adaptive_erasure_20261117.zip` research bundle; input bytes, not current HEAD, define this calculation.

The frozen scalar observer retains the positive path/source cohort model; signed/phase/native X6 source is not inferred from eight scalar bits. Formal Task/CLAIM and independent review remain separate.

## Next unresolved unit

For `τ≥1744659037213380157479321600000`, three fixed budgets cannot achieve the previous guarantee; seek a four-or-more-read mixed-fault min-cost certificate, with possible departures from the simple `r×` scaling. Also retain interactive unmarked-corruption feedback, source-preserving joint readouts and `max-new/min-old` optimizer replacement-distance objectives.
