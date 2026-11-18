# R5: exact two eleven-state certificates cover 96 hypothesis subsets
Date: 2026-11-18. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Model and frozen input
This is a *derived scalar integer-center observer*, not the complete P000 / native X6 relational state. Frozen science commit: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. The all-101-budget derived integer count table `EXACT_R5_ALL_101_BUDGETS.json` has SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b` (available in the companion reproducibility ZIP). Allowed query budgets/costs k=214,...,314. Correct real readouts satisfy |y-N_h(k)| <= tau/2, and at most 8 readouts may suffer arbitrary unmarked corruption. C_8(H;tau) denotes the exact adversarial minimax total query cost with adaptive queries and stopping, for named hypotheses H.

Let
- L=25845652773852463277015040000
- U=58182461585441404127941754880
- H0={18,24,82,34,17}
- A={0,16,32,144,208,240}
- B={0,16,48,144,208,240}.

## Theorem
For **every real tau with L <= tau < U**, and every H satisfying either
H0 ⊆ H ⊆ H0 ∪ A or H0 ⊆ H ⊆ H0 ∪ B,

**C_8(H;tau)=8335.**

There are exactly 2^6+2^6-2^5=**96 distinct named populations** satisfying these alternatives (5–11 hypotheses), since |A∩B|=5. The two maximal eleven-state populations and all their intermediate subsets have the same exact cost. The previously certified full 256-state bracket remains 8335 <= C_8(full;tau) <= 8343.

## Proof and exact finite certificate
At a query k, compatible correct-response support is S_k(y;tau)={h∈H: |y-N_h(k)|<=tau/2}. The inclusion-maximal supports are precisely maximal sorted-center windows with span <= tau. Independently enumerate them by sweeping doubled observation coordinates across closed endpoints 2N_h(k)±tau and intervening open intervals. Every support is contained in a maximal support, and larger support gives the adversary weakly better outcomes for independent per-hypothesis error counters.

Keep counters e_h in {0,...,9}; 9 indicates elimination. For maximal support m, T_m increments counters of hypotheses outside m (saturated at 9). The exact recursion is
`V(e)=0` if at most one hypothesis has e_h<=8;
otherwise `V(e)=min_k (k+max_m V(T_m(e)))`.
A positive-cost action with a self-loop cannot produce guaranteed finite termination and may be discarded; every retained transition increases at least one live counter. Two budgets having identical *complete* maximal-support families have identical transitions at every counter state, so retain the cheaper one. All 101 budgets are enumerated before this cost-preserving action reduction. The C++17 integer Bellman solver retains all 11 counters and exact states.

Independent support generators agreed on **2 populations × 2 endpoints × 101 budgets = 404** complete families. Four exact Bellman roots returned:

| Population | tau | Exact value | Cached states | Distinct actions |
|---|---|---:|---:|---:|
| H0∪A | L | 8335 | 4,043,982 | 10 |
| H0∪A | U−1 | 8335 | 10,317,926 | 10 |
| H0∪B | L | 8335 | 5,877,822 | 10 |
| H0∪B | U−1 | 8335 | 10,235,929 | 10 |

All four processes exited 0; exact stdout and stdin SHA-256 hashes are in RESULTS_ELEVEN.json. The earlier exact five-state lower certificate gives C_8(H0;L)=8335. Monotonicity in hypothesis inclusion and tau sandwiches any listed H at all tau in [L,U−1]. Since center differences are integers, the complete response-support families are unchanged on [U−1,U), extending the result to the entire real chamber.

This is a scoped exact integer computation/author proof; independent mathematical review is pending. The scalar observer cannot be silently identified with complete native P000/X6 state or its branch/path/BRC provenance.

## Reproduce / next research unit
With the frozen table matching the stated SHA, Python 3 and a C++17 compiler:

`python3 VERIFY_R5_ELEVEN_CERTIFICATE.py EXACT_R5_ALL_101_BUDGETS.json EXACT_ELEVEN_SUBSET.cpp > reproduced.json`

The validator checks the input SHA, all 404 window/sweep support families, and all four integer Bellman roots. Companion full-source ZIP includes the frozen table and SHA256 manifest.

Next: find a twelfth named hypothesis that raises one maximal eleven-state value above 8335, or reduce the 256-state upper bound 8343 by a certified adaptive decision strategy. Preserve each named hypothesis and its error count, as well as the native observer/future-operation typing boundary.
