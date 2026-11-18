# R5 — Complete first-query cost diagram on the fifth noise interval

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Frozen object and proposition

Frozen science: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Exact input table `EXACT_R5_ALL_101_BUDGETS.json`, SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. States h=0,...,255; query budgets k=214,...,314, each of cost k; closed correct-response rule `2|y-N_h(k)| <= tau`, and no corrupted observations (f=0).

The diameter lies in [L,U) with
```text
L = 25845652773852463277015040000
U = 58182461585441404127941754880
C = 53550705027838197293383680000
```

Let F_k(tau) be the exact optimal worst-case total cost of an adaptive strategy whose *first query is required to be budget k*, followed by unrestricted adaptive choices from **all 101** budgets, with early stopping when one named state remains compatible. The full formula, valid for **every real** L<=tau<U, is:

| k | F_k(tau) |
|---|---|
| 214 or 215 | 948 |
| 216–218 | k+519 |
| 219, tau<C | 738 |
| 219, tau>=C | 952 |
| 220–221 | k+733 |
| 222 | k+735 |
| 223–290 | k+512 |
| 291–295 | k+735 |
| 296–312 | k+439 |
| 313–314 | k+735 |

Consequences: C_0(tau)=735 throughout; the **only** optimal first actions are 216, 223 and 296. Of 101 forced-first cost functions, 100 are completely invariant over the whole interval. Only k=219 jumps, by exactly 214, at C. The cheapest nonoptimal first action incurs a cost penalty of 1 (k=217,224,297).

For unknown and query-varying tau in [L,U), the prior strict-open envelope theorem shows the minimax forced-first-action game is the fixed tau=U-1 game. The table's right-hand side for k=219 is thus the exact unknown-diameter result as well.

## Exact finite proof and independently checked supports

For each action k and fixed tau, denote by R_k(tau) the inclusion-maximal supports of correct real observations. For equal-radius intervals on the line these are precisely maximal sorted-center windows of diameter <=tau. As an independent reconstruction, sweep all exact endpoints 2N_h(k)±tau, testing endpoints and inter-endpoint midpoints. The two methods agree on all 1,818 tested support families.

For a nonempty candidate set S the exact zero-error Bellman equation is:
```text
V_tau(S) = 0, if |S|<=1;
V_tau(S) = min_{k=214..314} (k + max_{R in R_k(tau)} V_tau(S intersect R))
otherwise, ignoring actions admitting a nonempty child S intersect R=S.
F_k(tau) = k + max_{R in R_k(tau)} V_tau(Full intersect R).
```
Dropping unchanged-belief actions from the **continuation** minimum is exact because a positive-cost query with an unchanged worst-case response can never improve the minimum. For the **forced initial query**, an unchanged response is retained in F_k, including the paid cost k. Nonmaximal response supports are dominated by maximal ones. Every recursive continuation transition strictly reduces a finite set S; the exhaustive memoized recursion proves exact optimality with no heuristic prunes or f>0 assumptions. All 101 budgets are enumerated at every continuation node; earlier 7/8-action-reduction results are not used to compute this theorem.

Correct-response supports can change only as tau crosses one of the exact integer differences |N_i(k)-N_j(k)|. Exhaustively enumerating center differences from all 256 states across 101 actions yields exactly 17 distinct internal thresholds between L and U. Each threshold starts one new half-closed chamber, so 18 chamber representatives suffice to prove the formula over all real tau. The code independently constructs all 18 chambers directly from the frozen input and evaluates 101 forced-root values in every chamber: **18×101=1,818 support-family crosschecks**, plus unrestricted Bellman solutions. Precisely one F_k changes at any threshold, namely k=219 at C.

## Reproducibility, limitations and frontier

Run `python3 VERIFY_R5_F0_ROOT_PHASES_FULL.py EXACT_R5_ALL_101_BUDGETS.json > RESULTS_R5_F0_ROOT_PHASES_FULL.json`. Original executed checker exit=0, status `PASS_R5_FULL256_F0_FORCED_ROOT_FIFTH_CHAMBERS`; exact input SHA checked. Original full result JSON SHA256 `fa9a84b5d69f14f2a313985922b43288ec9bd81f305e855f4c2c4ce3bb7a6268`. The full input, complete result JSON, standalone checker and proof are in the locally verified handoff ZIP; the Source JSON gives compact formula, chamber endpoints and verification metadata.

Mathematical scope is the frozen **derived scalar observer**. It is not a native six-dimensional-X6 completeness claim. The next objective remains the full256, eight-error adaptive optimum between 8335 and 8343. An f=0 first-action cost inequality alone cannot exclude an f=8 first action. Independent review and formal result admission have not been performed.
