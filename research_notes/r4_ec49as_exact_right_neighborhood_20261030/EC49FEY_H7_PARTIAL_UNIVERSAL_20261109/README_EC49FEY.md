# EC49FEY — Four exact H7-mixed 23-word BRC branches, two open

Date: 2026-11-09. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: **author-side exact finite partial classification**, pending independent Driver review. Original P000, ACTIVE Heartbeat World and nine-state signed-X6 word grammar unchanged.

## Mathematical result

For each of the four high-horizon sets below, H2 is low quartet `(1,2,4,8)`, H3 is high `(16,32)`, H7 is mixed type B `(1,8,16)`, three other late horizons are high `(16,32)`, and other late horizons low quartet. Exactly 23 distinct (h,signature) required paths, at most five complete positive forward BRC keys, native endpoint `(+2,0,0,0,0,0)` and cost = union of nonempty **ordered signed X6 microstep prefixes**.

| Four late high-bearing horizons | Original type B signature-feasible key configurations | Exact certified C_native lower bound |
| --- | ---: | ---: |
| 4579 | 744 | 101 |
| 4679 | 1,296 | 105 |
| 4789 | 2,208 | 108 |
| 5679 | 2,592 | 108 |
| **Four solved cases** | **6,840** | **≥101** |

The same four bounds hold for type-C `(2,4,32)` mirror via frozen operation/key involution. The original 2026-11-08 EC49FEU full H7 census contains 20,568 feasible typed-B inventories across six late-high subsets. Two unresolved sets are **5789 (8,352 feasible configurations)** and **6789 (5,376)**; 13,728 typed-B feasible remain. The other four candidate late-high subsets are signature-infeasible. Do not count B/C typed branches as necessarily distinct underlying inventories.

## Exact certificate method

For high set S containing H7 and H9, pool the complete positive BRC keys available to the H3 high pair, H7 mixed signature 16, and three other late high pairs. This superset includes each original five-key inventory, and allowing every signature group to pick from the pool only relaxes cost minimization. Enumerate every signed native word `W_g` in 23 required `(h,signature)` groups and its set of nonempty signed microstep prefixes `P(w)`.

Each certificate contains nonnegative exact integer weights `T_(g,p)`, 23 group lower guarantees `gamma_g`, and `Q=1,000,000`. Verify `sum_g T_(g,p)≤Q` for every prefix and `sum_(p∈P(w)) T_(g,p)≥gamma_g` for every candidate word. Then for each legal path choice,

`Q*C_native ≥ Σ_p Σ_g T_(g,p) ≥ Σ_g gamma_g`.

A separate Python standard-library integer checker independently reconstructed all words, exact six-axis endpoint, positive full keys, original nine-state signature, prefix and all inequalities; **all four returned EXACT_INTEGER_PASS**. Coefficient search used SciPy/HiGHS but the proof does not depend on LP solver correctness.

The four checked pools total 269,442 original operation words across branches and 1,577,344 group/prefix constraints. Full integer coefficients, verification records, word model and executable reproduction code accompany this note.

## Open work and observed execution limitation

The next `H7 5789` pooled dual coefficient optimization was launched; word/prefix enumeration succeeded, but the LP optimization did not return a coefficient candidate within this run's execution bound, so **no bound is asserted** for this set. `H7 6789` not attempted. Neither incomplete candidate search nor incomplete primal/dual optimization refutes possible useful constructions there. Next test 5789 with specialized structured dual, warm-start or smaller decomposition, then 6789, followed by H8 mixed placements. Mother target remains five complete BRC keys and signed native cost ≤93, with 94 previously known upper construction.

## Reproduction

From expanded archive: `python3 VERIFY_EC49FEY.py UNIVERSAL_H7_4579.json UNIVERSAL_H7_4679.json UNIVERSAL_H7_4789.json UNIVERSAL_H7_5679.json`. Full artifact readback and transport manifest accompany published evidence. These are author-side records, not a native Result or independent Driver mathematical admission.

Source activity: `EM-DIRECT-4FB3A8 / TASK_RESEARCH`; RA `RA-9854AC2E5AA8BFD1F95D7C37`, session Source verified; formal CLAIM and execution authorization not granted.