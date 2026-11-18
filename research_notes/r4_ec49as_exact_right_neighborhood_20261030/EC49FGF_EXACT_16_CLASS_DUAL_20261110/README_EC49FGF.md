# EC49FGF — Original BRC mother target: exact 110-edge lower bound under five complete keys

2026-11-10 (Asia/Shanghai). Author-side Researcher-ID: EM-DIRECT-946FC2; Research-Activity-ID: RA-2B5BD2E9D3418811000E7405. Mathematical admission/independent Driver review pending.

## Exact frozen claim

Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Frozen original nine-state BRC observer and ordered signed-X6 microsteps: EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py, Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859 (within the same research_notes/r4_ec49as_exact_right_neighborhood_20261030 parent directory). No scientific rebase or change to P000/worldview.

Original 24 demands at windows H2..H9 require signatures (16,32); (16,32); (1,2,4,8); (16,32); (1,2,4,8); (1,2,4,8); (1,2,4,8); (16,32). Each operation word has the specified length, its exact 9-state terminal signature and endpoint count(e)=count(a)+1, equivalent to native X6 signed displacement (+2,0,0,0,0,0). Each raw complete cache key is the three-tuple of positive occurrences on native axes 1,2,3. Zero components are counted as part of a distinct raw key. The cost counts unique nonempty ORDERED signed-native microstep prefixes across the 24 words.

**Theorem (author-side, exact finite computation with integer dual certificate).** Any legal 24-demand family using at most five distinct raw complete keys satisfies

    C_native >= 110 > 93.

Therefore the original frozen simultaneous objective (five raw keys AND at most 93 native prefix edges) has no solution in this exact model. The 112-edge complete five-key family in EC49FGE provides an upper bound, so the exact minimum lies between 110 and 112 inclusive.

## Why these 16 classes exhaust the key constraint

The earlier EC49FGE proved by complete count-state/DFA coverage that exactly five raw keys are necessary; they have the form

    Base={(3,0,1),(2,1,1),(3,1,1)}
    K45 in {(3,3,1),(4,2,1),(5,1,1),(5,1,2)}
    K69 in {(5,5,1),(6,4,1),(7,3,1),(7,3,2)}.

All 16 pairs occur, and there are no other five-key covers. This round independently re-ran DFA/count-state enumeration (94 eligible keys, 16 covers, 2502 live non-dead states at H9). Earlier reported 2832 H9 quotient states included the dead state and thus differ in that detail while agreeing on exact coverage.

## Exact LP lower-bound certificate

For each of 16 key sets, enumerate all allowed words via exact integers. Build the prefix trie of operations. For each nonroot operation-prefix v, binary x_v records use. Monotonicity x_child<=x_parent (root exempt) and one selected terminal per demanded signature give the exact support model. Each operation has native length 2 or 4. Only c/f and d/g siblings share one initial native microstep, and those sharing prefixes diverge at their next native step. Introduce pair discounts y<=x_c,x_f or y<=x_d,x_g. Consequently the literal native prefix count is exactly

    C = SUM_v len(last_operation(v))*x_v - SUM_eligible_pairs y.

The integer program's [0,1] LP relaxation supplies a valid lower bound. Express all constraints as G*x<=h and 0<=x<=1, with integer objective c*x. For ANY integer vector z<=0 and scale S>0, set r=S*c-G.T*z. The following is an exact proof, independent of floating-point solver accuracy:

    S*c*x = z*(G*x)+r*x >= z*h + SUM_j min(0,r_j).

The tool SciPy/HiGHS only proposes z: round S times its inequality marginals to an integer and clip to <=0. The checker itself recomputes the right-hand side from integer arrays and requires every bound >=1760 for S=16. The proof's validity depends on exact enumeration and this checked integer inequality, not on treating floating-point LP equality as a theorem.

## Sixteen certified integer numerators (divide by 16 for edge count)

| K45 \ K69 | (5,5,1) | (6,4,1) | (7,3,1) | (7,3,2) |
|---|---:|---:|---:|---:|
| (3,3,1) | 1919 | 1866 | 1956 | 1839 |
| (4,2,1) | 1833 | **1760** | 1832 | 1896 |
| (5,1,1) | 1957 | 1867 | 1919 | 1832 |
| (5,1,2) | 2233 | 2158 | 2232 | 2146 |

Every value was recomputed by the executed integer verifier. The unique competitive profile K45=(4,2,1), K69=(6,4,1) has the lower bound 110. All other classes have certified lower bound >112. The previous five-key 112-edge witness uses the competitive profile. The precise 110/111/112 minimum remains an integer-tightening question; a predecessor SciPy MIP zero-gap computation reported 112 for the competitive profile and has its own evidence level.

## Reproduction

Run from this folder with NumPy and SciPy/HiGHS:

    OPENBLAS_NUM_THREADS=1 python VERIFY_EC49FGF.py
    python EC49FGF_support_independent.py

The first command regenerates EXACT_REPORT_EC49FGF.json; the second verifies 16 exact raw-key families using standard-library integers. The source and report are author-verified. Mathematical Result registration/Driver independent admission remain pending because there is no current immutable publication for historical task EC49AS. The frozen input and all protected P000 fields are unchanged.

## Next scientific unit

Determine the exact integer minimum 110, 111, or 112 inside the sole competitive profile using a certified 110/111 infeasibility check or a better explicit family; then study the exact trade-off between native edge count and raw complete-key count without altering the frozen original problem.
