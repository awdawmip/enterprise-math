# R5 — Exact unbounded adaptive *visible-erasure* budget-cost theorem

Date: 2026-11-17. Frozen scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Same 954-event, 256-state derived exact-integer count observer and allowed integer budgets 214–314 as `RESEARCH.md`. Status: `AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED`.

## Theorem

For every integer `e ≥ 0`, consider a sequential deterministic query strategy that sees either the **exact** integer `N_b(K)` or an explicit **erasure marker**, and may choose its next budget accordingly. Up to `e` queries may be erased adversarially; erased queries incur their full budget cost. The strategy must terminate and identify every one of the 256 unknown masks for every such record. Minimize worst-path sum of budgets. Then

`C_adaptive-visible-erasure*(e) = 731 + 294e`,

and this minimum is attained by querying `214`, then `223`, then `294`, retrying the current budget only when an explicit erasure marker appears. The three returned clean values uniquely identify `b`.

For `e=1`, the adaptive optimal cost is **1025** while the best fully precommitted one-erasure-tolerant fixed query multiset costs **1462**. In general the adaptive saving over the optimal fixed erasure schedule is exactly `437e` budget units.

## Proof

Three already certified exact witness pairs share base mask 16 and have disjoint disagreement supports:
- 16 versus 17 differs only at budgets 214–221 (E);
- 16 versus 80 differs only at 223–291 (M);
- 16 versus 32 differs only at 294–313 (L).

The integer-count signature for budgets (214,223,294) is injective on all 256 masks. The retry strategy requires at most `e` unsuccessful attempts. Its successful baseline cost is `214+223+294=731`. Each erased attempt has budget at most 294, so its worst cost is at most `731+294e`. Adversarial erasures of the first `e` attempts at budget 294 show that this bound is attained.

For the matching lower bound, choose true state `b=16`, and let an adversary erase the **first e queries whose budget lies in L**, returning the correct count for all other queries. A strategy that terminates before receiving at least one successful L observation cannot distinguish states 16 and 32, because outside L the two exact response functions agree, and erased L observations carry no value. Thus the realized execution must contain at least `e+1` L queries, each with cost ≥294. Under the same adversarial transcript, an E query is required to distinguish 16 versus 17, and an M query is required to distinguish 16 versus 80; all E and M queries are answered honestly, so each must occur at least once. Their minimum costs are 214 and 223. The supports are pairwise disjoint, hence every correct strategy has a path of cost at least `(e+1)294+214+223=731+294e`. Matching upper and lower bounds establish the formula for every nonnegative integer `e`.

This is an information-theoretic finite-observer result with an **unbounded error-count parameter**, not a universal physical error law. Visible erasures are different from unflagged arbitrary corruptions; the latter still requires a separate adaptive minimax analysis.

## Verification and source

`VERIFY_R5_ADAPTIVE_ERASURE.py` verifies the upper-strategy worst-cost recurrence for e=0,...,15 using exact integers. The universal upper bound follows from budget accounting; the universal lower bound follows from the already fully checked 101-budget exact support sets, documented in `RESULTS_EXACT.json`, and the 256-state injectivity check in `RESEARCH.md`.

No formal R5 CLAIM or Activity/Result authority follows from this portable research addition.
