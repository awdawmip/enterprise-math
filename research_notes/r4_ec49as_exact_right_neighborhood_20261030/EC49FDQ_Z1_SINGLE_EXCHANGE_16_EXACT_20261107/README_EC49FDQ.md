# EC49FDQ — z=1 full five-key exchange optima (16 events)

**2026-11-07.** Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; immutable predecessor EC49FDP `25a05a9fd25793077bc87e0375a076534bd61df4`. P000, ACTIVE Heartbeat World and joint-relation preservation are retained. Status: author-side finite computation, independent Source Driver review pending.

## Proposition and exact finite coverage

Retain the six original H2/H3 words `de,ed,ce,ec;feg,gef` and their 42 ordered signed-X6 primitive prefixes. For each original EC49FAJ family 1512/1513/2200/2203, retain its four early complete BRC keys, replace its fifth (H9-essential) key by a distinct slot-feasible key with (z=1), and permit arbitrary mixed-key accepted operation words in H4–H9. Preserve original per-window quotas, exact five positive cache keys, nine-state frozen observer and rational rank 9 in each H2–H9 window. Every such fifth-key replacement event has a **computed 0–1 integer minimum greater than 93**.

| Family | replacement (x,y,z) | exact min signed-X6 prefix edges | candidate words | Trie edges |
|---|---|---:|---:|---:|
| 1512 | (4,6,1) | 106 | 1762 | 8116 |
| 1512 | (6,4,1) | 98 | 4966 | 26742 |
| 1512 | (7,3,1) | 102 | 3744 | 21307 |
| 1512 | (8,2,1) | 106 | 1762 | 10205 |
| 1513 | (4,6,1) | 106 | 1762 | 10205 |
| 1513 | (5,5,1) | 102 | 3744 | 21307 |
| 1513 | (6,4,1) | 98 | 4966 | 26742 |
| 1513 | (8,2,1) | 106 | 1762 | 8116 |
| 2200 | (4,6,1) | 102 | 1699 | 8116 |
| 2200 | (6,4,1) | 98 | 4903 | 26742 |
| 2200 | (7,3,1) | 102 | 3681 | 21307 |
| 2200 | (8,2,1) | 110 | 1699 | 10205 |
| 2203 | (4,6,1) | 110 | 1699 | 10205 |
| 2203 | (5,5,1) | 102 | 3681 | 21307 |
| 2203 | (6,4,1) | 98 | 4903 | 26742 |
| 2203 | (8,2,1) | 102 | 1699 | 8116 |

There are **16 distinct z=1 exchange events**, of which 1512/(4,6,1) and 1512/(6,4,1) reproduce the already saved EC49FDO optima 106 and 98. The other **14 are newly solved in this run**. All 16 optimal objectives lie in `{98,102,106,110}`. Together with EC49FDP's 28 rigorously excluded events, the finite 60-event critical-key single-exchange family now has **44 events excluded from cost <=93**. The **16 surviving z>=2 events** remain for further evaluation. This statement fixes the original H2/H3 seed and single-key-replacement family; different seeds or multiple-key changes remain open for the mother <=93 target.

## Integer formulation and evidence

For any accepted horizon `h` and full positive BRC key `(x,y,z)`, use the frozen multiplicities
`a=z-1,e=z,c+d=x+y-h-1,f=h+1-y-2z,g=h+1-x`; enumerate all nonnegative splits and all accepted nine-state DFA words, with `TRANS` and six signatures `(1,2,4,8,16,32)`. Expand each operation word into the frozen ordered **signed** X6 primitive sequence. Prefix-Trie nodes are billed one unit if not among the 42 prepaid seed prefixes.

Binary `y_(h,w)` selects a **complete horizon word**; binary `x_p` marks a billed primitive prefix. `y_(h,w)<=x_terminal`, and `x_child<=x_parent` on non-root edges. For each horizon the four frozen rank clauses `(18,20,33,40)` must each intersect the selected word signatures. Enforce exact H4–H9 slot quotas and at least one selected word for each of four non-seed full keys. Minimize `42 + sum_(p not prepaid) x_p`. Rank clauses are equivalent to rational rank 9 for this frozen six-signature observer; explicit selected witnesses are checked directly using rational linear algebra.

The formulation is sound and complete for the stated finite family: any legal set of words yields feasible `x,y` of its exact union-prefix cost, and any feasible `x,y` selects legal words with actual union-prefix cost no larger than the paid objective (unneeded `x` can be deleted). Numerical HiGHS results returned `OPTIMAL` with matching integer primal and dual values and zero MIP gaps for all 16. Every explicit 22-path witness was independently audited for native signed displacement, full cache-key usage, quotas, original signature, exact rational rank 9 at H2..H9, and directly recounted signed prefixes. This is an exact-integer modeling result with solver-certified optimality statuses; the solver dual certificate was not separately formalized.

## Reproduction

`EC49FDQ_REPLAY.py` is the local executed standalone SciPy/HiGHS model, with no remote/network dependency; e.g.
`OPENBLAS_NUM_THREADS=1 python EC49FDQ_REPLAY.py 2203 4,6,1 5,5,1 6,4,1 8,2,1`.
The sibling `EXACT_REPORT_EC49FDQ.json` contains all 16 full 22-word optimal constructions and the matched primal/dual objectives. An independent SymPy `Matrix.rank()` witness checker was separately executed locally on all 16 exchange outputs plus the original 1512 baseline (17/17 pass). Existing FDO's two optima served as model regressions. The code and evidence intentionally do not assert Source-native CLAIM/Result or independent Driver acceptance.

## Next EC49FDR

Evaluate the remaining **16 z>=2** family/key events using a threshold-93 feasibility approach and reusable exact tail bounds, prioritizing smaller Trie cases and separating build cost from optimizer time. A direct z>=2 full MILP attempt exceeded the available bounded local run, so it is not counted as a result. In parallel, vary the H2/H3 seed and two-key joint selection, preserving the original five-key mother constraints and exploring new prefixes rather than revisiting already classified z=1 exchanges.
