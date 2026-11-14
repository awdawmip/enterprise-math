# EC49FGI — Five complete BRC cache keys: 112-edge exact MIP optimum (solver-backed)

Date: 2026-11-10 (Asia/Shanghai). Status: author-side computationally complete; independently checkable exact integer/rational infeasibility proof still pending. Native researcher session was requested separately; this file does not attribute this turn to a predecessor ID.

## Model and verified prior work

Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Frozen original BRC observer/native signed X6 model: `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.

Demand windows H2..H9 require signatures `(16,32), (16,32), (1,2,4,8), (16,32), (1,2,4,8), (1,2,4,8), (1,2,4,8), (16,32)`. Each word has the exact window length and nine-state signature; its ordered signed X6 native expansion returns to displacement `(2,0,0,0,0,0)`. A raw complete key is the triple of positive native occurrences on axes 1,2,3, **including zero components**. Cost is the count of distinct nonempty ordered signed native microstep prefixes.

EC49FGE proved by exhaustive count-state DFA reachability that exactly five raw keys are necessary; all five-key covers have `Base ∪ {K45,K69}`, where `Base={(3,0,1),(2,1,1),(3,1,1)}`, `K45∈{(3,3,1),(4,2,1),(5,1,1),(5,1,2)}`, and `K69∈{(5,5,1),(6,4,1),(7,3,1),(7,3,2)}`. EC49FGF supplied exactly recomputable integer dual lower bounds **greater than 112** for fifteen of these sixteen five-key classes; the sole competitive class, `K45=(4,2,1), K69=(6,4,1)`, had a certified lower bound 110. An explicit valid 112-edge family was already available in EC49FGE.

## New complete computational classification

In the sole competitive class, the finite operation-prefix trie has **10,901 nonroot nodes**, **1,904 native sibling-overlap discounts** and **14,728 inequality rows**. Binary `x_v` selects operation prefix nodes with `x_child<=x_parent`; every (window,signature) demand needs a selected terminal. Native overlap of sibling c/f or d/g contributes a discount `y<=x_sibling1,x_sibling2`. Exact native cost is `Σ_v len(native(lastop(v))) x_v - Σ y`, so minimizing it is an integer linear optimization with no geometry projection or loss of ordered prefixes.

Using SciPy 1.17 / HiGHS 1.8.0, actual integer optimization reported `status=0`, **objective=112**, **integer dual bound=112**, **MIP gap=0**, **MIP nodes=1**. An independent capped decision run on the same full integral feasible set, with explicit constraint `cost<=111`, reported **INFEASIBLE (status=2)** both with presolve enabled and disabled. A separately coded literal nine-state/native X6 replay verified the already published EC49FGE 24-word witness: 24 terminal demands, exactly five complete raw keys, X6 displacement (2,0,0,0,0,0) at every endpoint, and exactly **112** distinct native microstep prefixes.

Therefore the reproducible **solver-backed finite optimum** is
```
C_min(original 24 demands, #raw_complete_keys <= 5) = 112
```

**Proof strength:** This is complete MIP branch-and-bound numerical/computational certification, not yet a standalone replayable *exact-arithmetic UNSAT/Farkas proof* for the cap-111 system. HiGHS does not export such a formal certificate in this evidence set. The already exact-integer-certified unconditional lower bound **110** from EC49FGF remains valid independently of the solver's internal proof. The frozen mother target `#K<=5 AND native prefixes<=93` was already rigorously excluded by that bound. Driver review, formal Result, any change in Foundation and protected P000 remain outside this author-side result.

## Verification and next question

Run `OPENBLAS_NUM_THREADS=1 python VERIFY_EC49FGI.py` from this directory (SciPy+NumPy required; imports the unchanged sibling `../EC49FGF_EXACT_16_CLASS_DUAL_20261110/VERIFY_EC49FGF.py`). The supplied `EXACT_SOLVER_AUDIT_112.json` and `VERIFICATION_EC49FGI.log` are an actually observed local run. For standalone exact 110 dual arithmetic replay, run the predecessor `VERIFY_EC49FGF.py`.

Next: produce a portable **integer/rational infeasibility certificate** for cap 111 (certified branch-and-bound leaf duals or an exhaustive combinatorial DP). Separately, explore the distinct six-key frontier; the EC49FGH study should not be confused with this five-key classification.
