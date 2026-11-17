# R5 — Sharp low-analog-noise stability of exact fault-tolerance optima

Date: 2026-11-17. Same pinned derived observer as the adjacent `RESEARCH.md`. Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.

Let each **non-corrupted, non-erased** scalar count reading at budget k be any real number `y` satisfying `|y-N_b(k)|≤η` with common absolute bound `η≥0`. Up to `e` known erasures and `f` arbitrary symbol replacements are allowed at other coordinates. A coordinate is guaranteed to distinguish two masks `a,b` precisely when `|N_a(k)-N_b(k)|>2η`. Write `τ=2η`.

## Sharp theorem in the first exact margin chamber

Define the **exact integer** constant
`δ=76289178155959966960189440`.
The full 256-state exact-count table verifies

`min_(a≠b) max_(k∈{214,223,294}) |N_a(k)-N_b(k)|=δ`,

and **exactly 64 unordered mask pairs** attain δ, including masks (16,32), for which the budget-294 difference is δ and the other two base-budget differences are zero.

For **every** nonnegative integer `e,f` and **every real** `η` satisfying `0≤2η<δ`:

1. The minimum total budget for a fixed nonadaptive repeated query multiset correcting `e` marked erasures and `f` arbitrary replacements **in addition to bounded analog error η** is **exactly** `731(e+2f+1)`. The unique cost-optimal multiset repeats each of 214,223,294 `e+2f+1` times.
2. With sequential feedback on marked erasures and no arbitrary replacements, the minimum worst-case cumulative budget is **exactly** `731+294e`, attained by retry-on-erasure at 214,223,294.

Both hold with adversarially selected analog errors at every uncorrupted position. The equality point `2η=δ` is the **first threshold at which the repeated base triple ceases to separate all 256 states**. Thus the fixed-schedule minimum-cost formula from item 1 is sharp up to the open boundary: at equality the unique cost-`731(e+2f+1)` multiset fails to distinguish the (16,32) pair, and every feasible robust fixed schedule is strictly more expensive.

## Proof

For each mask pair define its **strong disagreement set** `D_τ(a,b)={k:|N_a(k)-N_b(k)|>τ}`. The adversarial mixed fault unique-decoding condition for a fixed schedule is `min_(a≠b) #{i:k_i∈D_τ(a,b)}≥e+2f+1`: disjoint analog intervals act as distinct code symbols, overlapping intervals can be chosen identical by the adversary. This is the same coding-distance criterion applied to these pairwise guaranteed distinctions.

When `τ<δ`, the base triple distinguishes every pair in at least one coordinate whose analog intervals are disjoint; repeating each coordinate r times therefore gives robust strong-distance at least `r=e+2f+1`. The three exact witness pairs (16,17), (16,80), (16,32) have disjoint **raw** disagreement supports, so strong disagreements can only be within those disjoint sets. The weighted lower bound remains `731r`, with equality only at the repeated base triple. For visible-erasure feedback, retrying erased budgets until three received analog values is sufficient for η in this interval, and the late-support-only erasure adversary from `ADAPTIVE_ERASURE_THEOREM.md` still establishes the lower bound `731+294e`.

At `τ=δ`, masks 16 and 32 can choose identical analog readings at all three base budgets: their intervals at K294 touch. Thus the base triple is no longer injective under the allowed analog error. The minimum of the full table's 32,640 pairwise max-gap values is δ, with 64 saturating pairs. This is an exact, finite, integer certificate; the unbounded e,f conclusions follow from the coding proof.

## Verification and next

`VERIFY_R5_MIXED_LOW_NOISE.py` reconstructs the three 256-count vectors from the pinned requirement coefficients using only integer subset-zeta operations; checks δ, 64 saturating pairs, (16,32) and 256 clean signatures. It uses the exact `compact_stdout.json` SHA256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`.

Next: find the exact mixed fault cost transitions for `τ≥δ` by an integer weighted multicover certificate, and investigate interactive arbitrary corruptions. This source-level integer observation theorem does not convert the underlying native X6/BRC provenance and signed path data into a scalar complete state.
