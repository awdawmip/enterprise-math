# Exact R5 one-gap sensitivity of the radius-2 budget frontier

Date: 2026-11-13. This is a **counterfactual perturbation** of precisely one coordinate gap in the frozen sample, not a repinning of the scientific input (which remains `435e77af0d180eac32bd1f9c4c464bc4010b7551`). The original 953 threshold source and all retained joint certificate provenance remain the baseline.

## Locality of one-gap perturbations

Given a radius-R separation `x[i+1]-x[i]>R`, reducing that one gap to `<=R` while translating all later coordinates by the same amount modifies the total point-spacing sequence at only one position. Every other separator remains fixed and every unaffected component is unchanged up to translation. Consequently the new global optimal budget-cost curve can be recalculated by replacing only the two formerly adjacent component curves by the exact curve of their now-merged component, followed by a min-plus convolution with all unchanged component curves. This is a direct consequence of the factorization theorem in RESEARCH.md, with no approximation.

## Exact frozen R5 sensitivity experiment (R=2)

The original data have exactly 28 gaps of length 3, numbered in increasing coordinate order. For each of the 28 separate experiments, replace **only one gap 3 by 2**, leave all other gaps fixed, and recompute the full fixed-radius optimal budget frontier. Each experiment is an independent changed-input comparison against the same frozen baseline.

- Five perturbations, at separator positions **6, 7, 9, 10, 17**, reduce the minimum required center count from 213 to 212. The new `J_2(212)` values are respectively **1077, 1077, 1075, 1075, 1076**.
- Among all 28 perturbations, only positions **9 and 10** reduce an optimal cost at a budget feasible in both original and modified datasets. In each case only the original boundary budget `K=213` changes, by exactly one unit, **1070 -> 1069**. No other shared-budget cost changes.
- For the other 26 perturbations, all 742 original feasible-budget costs remain identical. None of the changed datasets is claimed to retain the original event count: these are synthetic perturbations of an explicitly defined scalar event coordinate array.

These exact finite observations follow from `R5_R2_GLOBAL_GLUE_SENSITIVITY.py` and are scoped to the frozen coordinate sequence and one-gap perturbation family. Each case computes a newly merged pair curve and recombines unchanged local curves; it verifies every shared-budget change is nonnegative and reports all 28 one-based gap positions.

## General counterexample to universal shared-budget invariance

Take `R=2`, original coordinates `[0,1,2,4,7]`, two centers `K=2`. The single gap `4->7` is 3, so the original instance factors into `[0,1,2,4]` and `[7]`. Its unique feasible two-center choice is `{2,7}`, with distances `[2,1,0,2,0]`, sum **5**.

Reduce just that gap from 3 to 2, obtaining `[0,1,2,4,6]`. The two-center choice `{1,4}` has distances `[1,0,1,0,2]`, sum **4**, satisfying the same radius 2. Direct enumeration verifies the new optimum is 4. Thus crossing the separation threshold **can** improve the optimal cost at an old feasible budget, even though it changes no other gap. The frozen R5 data's sparse cost sensitivity is therefore an observed special property, not a universal invariance theorem.

## Evidence and next issue

The verified main program and its exact `EXACT_OUTPUT.json` remain in this same research directory. Local exact execution of `R5_R2_SEPARATOR_SENSITIVITY.py` and `R5_R2_GLOBAL_GLUE_SENSITIVITY.py` established the 28 experiments and the finite witness. The latter program requires only the published main Python file and standard library. No independent review, native Result, formal CLAIM or full 28-coordinate prefix-index replay is asserted.

Next research: characterize which boundary configurations let a gap reduction decrease `D_R` without decreasing costs at previously feasible budgets; derive a local finite signature that predicts the pair's contribution without reoptimizing its entire frontier; then replay the original 28-coordinate, 8192-query system with the candidate budgets.
