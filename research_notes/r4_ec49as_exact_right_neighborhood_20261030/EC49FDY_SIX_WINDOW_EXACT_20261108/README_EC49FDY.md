# EC49FDY — Exact full H4–H9 three-phase optimization for eight frozen early seeds

Date 2026-11-08 Asia/Shanghai. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Input: author-side EC49FDW eight explicit systems in immutable commit `f60cfd6ca32b442661622bb0382dbbd6449778f0`, retaining the original nine-history observer, six signed-native operations and five full positive BRC cache keys.

## New finite result

**In each of the eight EC49FDW constructions, fix only the literal H2 and H3 paths and the given H4–H9 three-phase BRC-key schedule. Allow all H4–H9 legal operation words to change jointly.** Exact mixed-key signed-native-prefix integer optimization produces full H2–H9 minima **118 edges for cases 0–3**, and **120 edges for cases 4–7**, with matching constructed full systems. All eight have exactly **35 early H2–H3 prefix edges**. The minimum extra H4–H9 edge costs are respectively **83** and **85**.

This materially strengthens EC49FDX (which fixed H2–H6): jointly replacing all 18 later words under their given three-stage keys cannot reduce these eight complete systems. The original five-key mother problem seeks <=93 edges and remains open; different early H2/H3 seeds, cache-key sets, per-window mixed-key selection or different schedule can be investigated separately.

## Exact enumeration and MIP structure

For a legal word of operator horizon h and complete positive BRC primitive-count key (x,y,z), signed displacement +2E1 forces
`#e=z`, `#a=z-1`, `#c+#d=x+y-h-1`, `#f=h+1-y-2z`, `#g=h+1-x`.
Splitting c/d and enumerating all distinct operator permutations, then applying the original nine-history observer, yields the exhaustive eligible literal word pools. The quotas at H4...H9 are (2,4,2,4,4,2); the available signature classes and rank-nine constraint force exactly one word from each of 18 groups. The model introduces binary selection x_w for each eligible word and binary paid-prefix y_p for every signed native prefix p not in the fixed H2–H3 union F. It enforces one word in each observation-signature group and `x_w <= y_p` for each native prefix p of a selected word. Objective: `|F| + sum_p y_p`. The objective is exactly the size of the complete ordered native prefix union for each feasible construction. The solver is HiGHS via SciPy MILP with zero MIP gap; its reported integral primal/dual match after rounding numeric values to the nearest exact integer.

## Eight-run evidence

| Case | Late K on H7–H9 | Fixed early edges | Eligible H4–H9 literal words | Unpaid prefix variables | Constraints | Optimal additional edges | Full optimum |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | (4,6,1) | 35 | 1180 | 8081 | 19597 | 83 | **118** |
| 1 | (5,5,1) | 35 | 3042 | 19361 | 51063 | 83 | **118** |
| 2 | (7,3,1) | 35 | 3042 | 19361 | 51063 | 83 | **118** |
| 3 | (8,2,1) | 35 | 1180 | 8081 | 19597 | 83 | **118** |
| 4 | (4,6,1) | 35 | 1180 | 8081 | 19597 | 85 | **120** |
| 5 | (5,5,1) | 35 | 3042 | 19361 | 51063 | 85 | **120** |
| 6 | (7,3,1) | 35 | 3042 | 19361 | 51063 | 85 | **120** |
| 7 | (8,2,1) | 35 | 1180 | 8081 | 19597 | 85 | **120** |

Eight separately executed SciPy HiGHS solves reported OPTIMAL, primal equal to the dual bound, MIP gap=0. Eight newly selected literal full systems were checked: **8/8 complete constructions, 64/64 exact Fraction rank-nine window tests, 192/192 primitive path displacement/length/BRC-key tests**, and all matched the literal prefix count and exactly five full keys. The original eight EC49FDW witnesses additionally provide independent matching 118/120 upper bounds.

The integer optimum proof relies on the enumerator and complete 0–1 model, and on HiGHS reporting an exact matching integer lower bound; it is a solver-backed finite certificate, not an independently formalized proof in Lean. The original independent Fraction validator for full observations is available in EC49FDW, and the current source code revalidates each selected full construction with the existing exact observer.

## Reproducibility and provenance

Run `IDX=0 python EC49FDY_FULL_LATE_MIP.py` from this directory for case 0, changing IDX from 0 to 7 for eight independent runs. Use Python with NumPy and SciPy/HiGHS, and unchanged sibling directories: `EC49FDU_THREE_PHASE_RANK_20261107`, `EC49FDV_QUOTA_THREE_PHASE_20261108`, `EC49FDW_EIGHT_NATIVE_PREFIX_IMPROVEMENTS_20261108`. The Python script outputs a literal 24-path system for every found solution, plus exact finite model counts, primal, dual and gap. `EC49FDY_SOLVER_SUMMARY.json` records the eight executed results.

## Next scientific step

The exact conditional minimum now survives the **full H4–H9 joint optimization**. Next isolate the three assumptions that remain variable in the mother search: (1) different H2/H3 native words and BRC key spending; (2) cross-window mixed keys instead of strictly one key per window; (3) different 3-key arrangements including the four exceptional H4 mixed-key cases. Build a new finite feasibility test at <=93 edges under one changed assumption and preserve the entire signed primitive ordering and nine-history observer. Author-side publication does not create native CLAIM, Result freeze or independent Driver mathematical admission.
