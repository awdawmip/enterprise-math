# EC49FDN — Four 94-edge five-key neighborhoods: exact mixed-horizon optimum

Date 2026-11-07. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Author-side computational optimization; independently reviewable and not Source-admitted.

## Scientific question and new result

The parent H2–H9 problem seeks a construction with at most 93 distinct nonempty **ordered, signed native-X6 primitive-step prefixes**, exactly five complete positive BRC cache keys, no more than six nine-state transfer signatures, net displacement (2,0,0,0,0,0), and rational observer rank nine at every horizon.

The four EC49FAJ witnesses (source ranks 1512,1513,2200,2203) attain 94 edges using H2 words `de,ed,ce,ec` and H3 words `feg,gef`. Fix these six early words, contributing 42 distinct primitive prefixes. For **each** witness separately retain its exact five complete BRC keys as an unordered admissible set, but now permit **every H4–H9 horizon to mix any of those five keys freely**, selecting any displacement-valid ordered operation word in the frozen six-signature language. Each window must have exact rational observer rank 9.

This extends the original single-key-per-horizon witness family. The four finite-family optima are:

| EC49FAJ source rank | Eligible H4–H9 words | Signed Trie edges | LP bound (incl. H2/H3) | Integer optimum | Explicit witness |
|---|---:|---:|---:|---:|---:|
| 1512 | 3744 | 19962 | 93 | **94** | 94 |
| 1513 | 3744 | 19962 | 93 | **94** | 94 |
| 2200 | 3681 | 19962 | 94 | **94** | 94 |
| 2203 | 3681 | 19962 | 94 | **94** | 94 |

All four 0–1 MILP solves returned OPTIMAL with reported MIP gap zero and lower bound 94; direct independent word/observer/path verification confirms the upper bound. The continuous relaxation shows a **one-edge integrality gap** in the first two families (one optimal LP basis has fourteen half-valued prefix variables), but is tight in the other two.

**Finite theorem (computational certificate):** With this fixed H2/H3 seed and with the full cache-key set fixed to any one of the four named EC49FAJ sets, changing any H4–H9 operations, their order, their signatures or how the five keys are distributed among horizons cannot produce 93 edges. The global five-key H2–H9 mother objective remains open when the cache-key set or early seed is changed.

## Complete candidate domain and equivalence

Allowed native operations are the frozen seven-operation alphabet `a,b,c,d,e,f,g`, with `b` excluded by the signed target. Candidate words have length h, net positive E1 displacement two, and complete positive key (x,y,z,0,0,0). Their exact multiplicities follow from the signed source equations: `a=z-1`, `e=z`, `c+d=x+y-h-1`, `f=h+1-y-2z`, `g=h+1-x`; enumerate every nonnegative c/d split and legal ordering with the existing nine-state transfer automaton.

For the six original transfer signatures numbered 1,2,4,8,16,32, rational rank nine is exactly the conjunction of four clauses with bitmasks 18,20,33,40. The published replay checks this exhaustively on all 64 subsets of the six signatures with exact Fraction elimination (25 masks have rank 9). The signature restriction is part of this frozen model.

Create a signed primitive Trie from all admissible candidate words. Each nonroot vertex v has binary `x_v`, selecting that edge, and is constrained by `x_v <= x_parent(v)`. A root child has only `x_v <= 1`. For each of the 6 horizons and four rank clauses, require at least one selected terminal in a signature satisfying the clause. Pay `42 + sum x_v` for vertices whose prefixes are not in the six fixed early words; the other vertex costs are zero. Every legal word family produces a feasible closure; every feasible integer solution contains enough terminals to construct a legal family with no greater paid cost. Thus the exact 0–1 minimum equals the finite signed-prefix problem minimum under these fixed assumptions.

## Reproduction and evidence status

Run `OPENBLAS_NUM_THREADS=1 python REPLAY_EC49FDN.py > results.json` using Python 3 with NumPy and SciPy HiGHS. The script imports the already-published adjacent `EC49FDL_TEN_MIXED_PAIR_EXACT_20261107/REPLAY_EC49FDL_PORTABLE.py` to preserve exact signed primitives and observer semantics; the explicit 94-edge roots are from `EC49FAJ_H9_KEY_REUSE/VERIFY_EC49FAJ.js`. It checks the 64 signature masks, all four original witnesses, integer-optimality status, and newly reconstructed chosen-word witnesses, including full signed X6 displacement, exact rational nine-state rank, five full keys, six signatures, and native prefix count.

The stored `EXACT_REPORT_EC49FDN.json` contains the four optimized selections and solver metrics. This is computational integer-optimality evidence plus direct exact arithmetic validation of matching upper bounds; the lower bounds rely on HiGHS and model equivalence, not a separate formally checked UNSAT certificate. No native CLAIM, Source Result or Driver mathematical admission is asserted.

## Next scientific unit EC49FDO

Use the four 94-edge key families as verified baselines, then exchange one of the **four non-H2/H3 full keys**, screening key sets for genuine nine-rank feasibility and cost rather than treating all alternatives as already excluded. Alternatively change the H2/H3 root seed and optimize jointly. Seek a <=93-edge complete signed word witness and validate every original constraint before proposing parent-objective closure.
