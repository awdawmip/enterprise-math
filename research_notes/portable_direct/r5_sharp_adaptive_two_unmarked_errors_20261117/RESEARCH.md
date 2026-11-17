# R5: sharp adaptive cost for two arbitrary unmarked errors

Date: 2026-11-17 (Asia/Shanghai). Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Sharp theorem (derived scalar observer)

In the frozen 954-event integer-count observer, let `b=0,...,255` be the effective closure mask, and let `N_b(k)` denote its exact positive scalar count for an integer budget `k=214,...,314`. A query costs `k`. Every uncorrupted real reading has absolute error at most `eta`, while at most **two** readings may be arbitrary unmarked replacements. The next queried budget may depend on all preceding observations. Require recovery of the true mask on *every* permitted transcript, minimizing worst-case total queried budget.

Define `delta=76289178155959966960189440`. For every real `eta>=0` with `2 eta < delta`,

```
min_adaptive_worst_total_cost(f=2,e=0;eta) = 2621.
```

The already established sharp fixed-query benchmark costs `(2*f+1)*(214+223+294)=3655`. Adaptivity saves 1034 budget units (about 28.29% of fixed). The one-error (`f=1`) adaptive optimum is 1676; both theorems refer to the same frozen derived observer.

## Constructive upper bound

Use the three budgets in this order: **294,223,214**. At each budget, map each real observation to its unique exact count center whose closed `eta`-interval contains it, or an out-of-alphabet marker when none does. The minimum positive center spacing among these budgets is exactly `delta`; consequently legitimate readings map to their correct count center and arbitrary replacements to any center or marker.

Keep an upper bound `r` on errors not yet conclusively observed, initially `r=2`. At each budget:

- `r=2`: read three times. If unanimous, their count symbol must be true. Otherwise continue the *same* budget to a fourth reading; a symbol occurring three times is true, and a pattern `2+1+1` has its doubleton true. If the fourth reading yields a `2+2` tie, read a fifth time; the unique triple majority is true. Subtract the number of observed nonmatching symbols from the remaining error allowance.
- `r=1`: read twice. Agreement is true; disagreement forces a third read, which is necessarily true. Subtract the number of nonmatching symbols.
- `r=0`: one reading is true.

In every case with `r=2`, an apparent doubleton at length four with two other distinct symbols must be true: otherwise at least three readings would be corrupted. For length five, at most two are corrupt, so a triple majority exists and equals the truth. The finalized exact count symbols at the three budgets form a known injection on all 256 masks.

Worst-case branch accounting, with suffixes under the remaining-error rule:

| first nonunanimous 3-read budget | worst cost |
|---|---:|
| 294 | `4*294 + 1088 = 2264` |
| 223 | `3*294 + 4*223 + 3*214 = 2416` |
| 214 | `3*294 + 3*223 + 5*214 = 2621` |
| none | `3*(294+223+214)=2193` |

A fifth read after a discrepancy consumes two errors, allowing each subsequent budget to be read only once. Four-read cases with two observed errors are cheaper. Hence the worst upper cost is exactly `2621`. An explicit constructive witness is three matching true readings at 294, three at 223, and three readings followed by a `2+2` tie at 214 requiring the fifth.

## Matched lower bound: exact four-state adversarial decision game

Use the frozen witnesses with common base mask 16. Masks 17, 80 and 32 each differ from 16 **only** at their corresponding budget windows, over the full 101-budget domain:

| state | all differing budgets from state 16 | minimal query cost |
|---|---|---:|
| 17 | 214 through 221 | 214 |
| 80 | 223 through 291 | 223 |
| 32 | 294 through 313 | 294 |

These windows are disjoint. For this restricted four-state population, at each window `j=1,2,3` there are only two true observation types: `1` if the true state is the corresponding alternative, and `0` for all other three states. An arbitrary corrupted report may be `0`, `1`, or a third symbol `2` outside both legitimate count-intervals. Every available original budget maps to at most one such binary test, and the cheapest test costs respectively `c=(214,223,294)`. Thus the restricted zero-noise, two-error decision game supplies a valid lower bound for the complete 256-state real-noise problem.

For a transcript, let `d=(d_0,d_1,d_2,d_3)` count mismatched test answers relative to the four candidates, capped at 3 (which denotes eliminated). Initially `d=(0,0,0,0)`. For test `j`, response `a in {0,1,2}` and candidate `h in {0,1,2,3}`, set

```
T_j(d,a)_h = min(3, d_h + 1[a != 1[h == j]]) .
```

Candidate `h` remains possible iff `d_h <= 2`. Define `V(d)=0` when at most one candidate survives. Otherwise let

```
V(d) = min_{j in {1,2,3} productive}
       (c_j + max_{a in {0,1,2}: some candidate survives T_j(d,a)}
                   V(T_j(d,a))).
```

A nonproductive test has an admissible self-loop `T_j(d,a)=d`, so repeating it cannot improve the guaranteed finite worst-case cost; it may be discarded. Every productive transition strictly increases a noneliminated mismatch coordinate or eliminates a candidate, so the recursion is acyclic on the finite set `{0,1,2,3}^4`.

The stored exact-integer dynamic-programming certificate evaluates `V((0,0,0,0))=2621`, reaching 175 states, including 163 nonterminal states, and checks every productive action's Bellman lower inequality. Therefore any adaptive decoding scheme has worst cost at least 2621, regardless of extra scalar detail or other budgets. Together with the construction, this proves the exact optimum.

## Reproducibility and limitations

`VERIFY_R5_ADAPTIVE_TWO_UNMARKED_ERRORS.py` was actually executed with frozen `COHORTS_3_BUDGETS.json` and `EXACT_R5_ALL_101_BUDGETS.json`. The independent original full-count source has SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The verifier:

- reconstructed all 768 exact three-budget counts using eight subset-zeta passes and checked them against full prior counts;
- checked 256 distinct signatures and exact minimum spacing `delta`;
- scanned all 101 budgets for each of the three disjoint-window witnesses;
- exhaustively checked 72 local symbolic finite-response patterns (`64` with two remaining corruptions, `7` with one, `1` with zero) including recognized wrong centers and out-of-alphabet responses;
- combined possible local transcripts with an exact cost recursion;
- computed and checked the complete 175-state finite adversarial min-max certificate.

Stdout: `PASS_R5_SHARP_ADAPTIVE_TWO_UNMARKED_ERRORS_2621`. `RESULTS_TWO_ERRORS_EXACT.json` preserves the result, computed bounds, branch and witness records. No floating-point computation, unexecuted native BRC procedure or model-independent information claim is used.

This theorem concerns the declared **derived scalar-count quotient only**. P000 native six-axis geometry, signed joint relations, path history, provenance, and future observer closure are not collapsed by it.

## Continuation

Compute or characterize the sharp adaptive cost for `f>=3` errors and for `2eta>=delta`. A promising general construction uses confidence-adaptive repeated sampling with a finite adversarial minimax kernel analogous to the four-state proof. Separately retain the original optimizer `max-new/min-old` recourse problem on K=214..291 and native BRC joint-observer preservation.

Researcher origin: `EM-DIRECT-C52C70`; Activity `RA-E56F584D739D86CC48916236`. Formal R5 CLAIM not assumed; independent mathematical review pending.
