# EC49FBJ — Eight alternative L/M key schedules, whole-H9 native-X6 optimal witnesses
Date: 2026-11-05. TASK_RESEARCH author-side calculation. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Scientific question and exact scope
The mother problem seeks the smallest signed native-X6 primitive-prefix edge union supporting rational observation rank nine at every horizon H2–H9 with at most five complete positive BRC cache keys. Earlier author-side whole-problem bounds were 80 ≤ E* ≤ 94; these remain the mother-problem references.

Here fix H2={fe,ge}, H3={feg,gef}, preserving their 16 common prefix edges and their three full positive keys. Choose one remaining key L for all H4,H5,H6, and another key M for all H7,H8,H9, with complete six coordinates (x,y,z,0,0,0). Test L=(4,3,1) and (5,2,1) and M=(5,5,1),(6,4,1),(7,3,1),(8,2,1). All eight pairs occur in EC49FBH's necessary-pair domain. Each horizon chooses unrestricted eligible ordered operation words satisfying terminal native signed-X6 displacement (2,0,0,0,0,0), the exact nine-state observation signature, and four rank-nine clause families for H4–H8, with F and G signatures at H9.

**Eight full-window scoped optimizer results**:

| L | M | signed-prefix E* | H2–H6 edges in exhibited optimizer witness |
| --- | --- | ---: | ---: |
| (4,3,1) | (5,5,1) | 130 | 82 |
| (4,3,1) | (6,4,1) | 130 | 82 |
| (4,3,1) | (7,3,1) | 136 | 82 |
| (4,3,1) | (8,2,1) | 161 | 91 |
| (5,2,1) | (5,5,1) | 136 | 82 |
| (5,2,1) | (6,4,1) | 130 | 82 |
| (5,2,1) | (7,3,1) | 130 | 82 |
| (5,2,1) | (8,2,1) | 136 | 82 |

All eight solver runs ended with HiGHS status 0 and reported zero MIP gap, with reported dual objective equal to E* minus the 16 prepaid edges (up to floating-rounding). An independent Python standard-library checker recomputed every exhibited word's six-dimensional signed displacement, full six-component positive key, nine-state signature, exact required-clause coverage, and distinct signed native primitive-prefix edge union. All eight independent witness checks passed.

The candidate enumerator uses the frozen endpoint/count identities: for horizon h and K=(x,y,z,0,0,0), counts are a=z−1, e=z, c+d=x+y−h−1, f=h+1−y−2z, g=h+1−x; enumerate all orderings and all c/d splittings. No continuum transformation is introduced.

## A finer finding: local prefix minimum versus global continuation

For L=(4,3,1), M=(8,2,1), the full nine-window optimal witness has 91 edges already at H6. Imposing the additional constraint E(H2–H6)≤90 made the complete H2–H9 model infeasible in a separate HiGHS run (status 2). Hence within this exact schedule every complete valid solution has at least 91 early edges, and the exhibited 161-edge optimum reaches that early threshold. The broader two-key-schedule early bound reported in EC49FBH allowed more flexible key assignments; it is not being substituted for this fixed-per-window result. This is a concrete example of a globally required early prefix cost that depends on the selected late key schedule.

A separate contrast: the two L choices have equal per-horizon eligible operation-word counts for each fixed M, yet cost differs: M=(8,2,1) yields 161 versus 136. Thus counts of candidate words alone are insufficient to predict cross-horizon primitive-prefix sharing.

## Model-to-MILP equivalence

Create one binary variable t_v for every non-root edge in the trie of exact native signed primitive steps. Require t_v≤t_parent for non-root parents and fix the 16 original early edges at t_v=1 with zero cost. For each of the 22 rank/signature clauses, require sum of t_v over matching terminal leaves ≥1. Minimize sum of non-prepaid t_v plus 16. A legal word family induces a feasible downward-closed union of its prefixes with equal cost. Conversely any feasible t-vector contains terminal leaves satisfying every clause, and the union of their primitive prefixes has no greater cost. The integer optimum therefore equals the defined finite prefix-edge minimum. The lower-bound computations were performed by SciPy/HiGHS; the upper witnesses and all their observable conditions were independently integer-audited. Independent pure integer lower-bound reconstruction remains a useful follow-up.

All results are scoped to the specified fixed H2/H3 plus particular L/M horizon schedule. Existing 94-edge mother construction stays in a different family.

## Reproduction and evidence

`VERIFY_EC49FBJ.py L M seconds`, e.g. `python VERIFY_EC49FBJ.py 4,3,1 8,2,1 45`, generates raw finite candidates, builds the exact native signed trie and runs SciPy/HiGHS. Eight runs were executed with SciPy 1.17.0; typical trie node counts: M=(8,2,1) 8,860/8,116, M=(7,3,1) 19,396, M=(6,4,1) 25,604. The reproduced witness lists, reported dual bounds, and all eight selected solutions are in `EXACT_REPORT_EC49FBJ.json`. The second script `CROSSCHECK_EC49FBJ.py` checks the compact aggregate certificate without optimization.

The early-cap90 model was run on the L431/M821 case with a 22-clause trie and a single additional integer early-prefix cap. Infeasibility was reported, separate from the primary optimum. Author-side mathematical evidence only; official Source Result/Driver review awaits actual task authorization.

## Next scientific unit

Allow flexible H4–H9 allocations of the two remaining keys across the other EC49FBH configurations (or change H2/H3). Quantify and optimize which key may appear at which horizon, preserving actual six-axis signed paths, full key identities and cross-horizon prefix sharing; prioritize candidates with the possibility of lowering the 94-edge global upper bound.

Provenance: EC49FBI `732a619117cc6afc987b8ce2e430256d59271e23`, EC49FBH `26d3b584ca34ff7439ba0c5879f93a1cc40ee29a`, frozen `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Project P000/ACTIVE worldview unchanged.
