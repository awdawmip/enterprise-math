# R5 fifth noise chamber: unique fixed optimum and exactly three first runners-up

Date: 2026-11-18. Author-side independent scientific contribution.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Input, typed model, and question

Scientific input remains frozen at `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The 256-state × 101-budget integer scalar readout `EXACT_R5_ALL_101_BUDGETS.json` has SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Physical query budgets are exactly integers `214,...,314`, with cost equal to the budget itself. Real normal observations obey `|y-N_h(k)| <= eta`, at most `f` observations may be arbitrary unmarked errors, and `tau=2eta` lies in the fifth chamber

`L=25845652773852463277015040000 <= tau < U=58182461585441404127941754880`.

A *fixed schedule* is a predetermined multiset/sequence of query budgets that is always executed in full; ordering is immaterial to identifying the true named scalar state. Let `t=2f+1` for an arbitrary integer `f>=0`. Write `r_k` for the number of occurrences of budget `k`. A schedule is feasible precisely when every unordered pair `(h,j)` satisfies `sum_{k:|N_h(k)-N_j(k)|>tau} r_k >=t`. This pairwise criterion and the exact optimum `735t` are proved in the preceding `r5_f8_h16_full256_fixed_optimum_20261118/RESEARCH.md`. This contribution proves the stronger uniqueness and next-to-optimal classification.

The scalar observer is a derived restricted readout; no claim of losslessly representing the full native X6 relation, histories, or BRC dynamics is made.

## Theorem (unique optimal query multiset, all error budgets)

For every integer `f>=0` and every real `tau in [L,U)`, the **only** optimal fixed query multiset on all 256 named scalar states is

`r_216=r_223=r_296=t`; all remaining `r_k=0`.

Its cost is `735t`. Arbitrary permutations of the same multiset are equivalent schedules.

## Theorem (exact first runner-up classification, all error budgets)

Among fixed, error-robust schedules other than the unique minimum multiset, the exact smallest cost is

`C_fixed,second(f;tau)=735(2f+1)+1`.

Exactly three *different multisets* attain it, obtained from the optimum by changing **one** query as follows:

1. replace one occurrence of budget 216 with 217;
2. replace one occurrence of budget 223 with 224;
3. replace one occurrence of budget 296 with 297.

Each of these remains valid for all 256 states, every integer `f>=0`, and the entire real fifth chamber.

## Exact dual-slack identity and proof

The four real pairs and their nonnegative dual weights are

| Pair | separating budgets for entire fifth chamber | weight |
| --- | --- | ---: |
| (0,64) | 223 through 290 | 223 |
| (1,2) | 214 and 216 through 221 | 1 |
| (2,8) | 215 through 221 | 215 |
| (16,32) | 296 through 312 | 296 |

Let `D_i` denote each such separating-budget set, `lambda=(223,1,215,296)`, `a_i=sum_{k in D_i}r_k`, and `e_i=a_i-t >=0`. Define the *exact budget slack*

`s_k=k - sum_{i:k in D_i} lambda_i >=0`.

The finite enumeration of the displayed four sets gives

`{k:s_k=0}={215,216,223,296}`,
`{k:s_k=1}={217,224,297}`.

All other budgets have integer slack at least 2. Since `sum_i lambda_i=735` and `k=s_k+sum_{i:k in D_i}lambda_i`,

`sum_k k*r_k -735*t = sum_k s_k*r_k +223*e_1+e_2+215*e_3+296*e_4`.  (★)

All terms on the right are nonnegative integers for every feasible fixed schedule. For excess cost zero, all `e_i=0` and only zero-slack budgets occur. The first and fourth witness equalities require `r_223=r_296=t`. The second requires `r_216=t`, and the third then yields `r_215=0`. This proves uniqueness once the preceding theorem's feasible optimum is used.

If the excess cost is one, (★) forces `e_1=e_3=e_4=0`. The case `e_2=1` would require all `r_k` to be zero except at `215,216,223,296`, while simultaneously `r_216=t+1` and `r_215+r_216=t`, which is impossible. Hence all `e_i=0` and `sum s_k*r_k=1`. Exactly one of `217,224,297` occurs, with the remaining queries restricted to the zero-slack types. The four witness equalities determine respectively the three stated one-query replacements and no others.

For sufficiency of all three runner-ups, verify the three replacement triples
`(217,223,296)`, `(216,224,296)`, and `(216,223,297)`
each separate **every one of the 32,640 unordered pairs** at the worst integer threshold `U-1`. The exact frozen integer table is used in `VERIFY_SECOND_BEST_FIXED.py`. For arbitrary `t>=1`, a modified schedule repeats each of the two unchanged original budgets `t` times, and includes `t-1` copies of the changed original budget plus one of its replacement. If either unchanged budget separates a pair, that pair already has at least `t` separated observations. Otherwise the corresponding replacement triple certificate ensures the replacement query separates the pair; then `t-1+1=t`. Thus each modified multiset is feasible for every `t` and `tau<=U-1`; integral center differences extend this to every real `tau<U`. All three cost `735t+1`. Every other feasible multiset has integer excess at least one, completing both minimum and exact equality classifications.

The identity (★) is also a reusable nonnegative *optimality-gap certificate*: it decomposes any fixed schedule's cost excess into per-query dual slack and excess pair coverage.

## Exact validation / reproducibility

The verifier `VERIFY_SECOND_BEST_FIXED.py` consumes the frozen 1,549,048-byte JSON input, validates its SHA-256, all 101 budgets, four witness separating sets at both `L` and `U-1`, the exact slack-zero/unit sets, and all 32,640 unordered pairs for each of the three replacement triples. It additionally checks full schedule coverage and costs for `t=1,3,17,61`; the general all-`t` statement follows from the proof above, not from finite testing.

Executed output: `PASS_R5_UNIQUE_OPTIMUM_THREE_SECOND_BEST_ALL_F`. Full frozen input, this proof, code and stdout are included in the local reproduction archive. Prior project proof and pinned R5 scientific source are reused without repinning.

## Next scientific problem

The complete 256-state *adaptive* value for eight unmarked errors is still bracketed by `8335 <= C_8^*(tau) <= 8343`. The fixed-schedule optimizer is now classified through the first positive cost gap for all `f`; a high-value next route is an exact adaptive decomposition or stronger multi-state adversary certificate. A proof of safety under the scalar readout should not be applied to native X6 observer histories without an explicit future-observation preservation certificate.

Source status: independently saved research note / proof / exhaustive exact finite verification; no claimed native Task CLAIM, Result, Review, or independent acceptance.
