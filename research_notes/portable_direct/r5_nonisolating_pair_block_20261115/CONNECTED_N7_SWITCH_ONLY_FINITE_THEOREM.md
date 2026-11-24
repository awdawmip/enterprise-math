# R5: 7-event connected attachment with joint-only Q and no new rank arcs

Date: 2026-11-15. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Scope: auxiliary one-dimensional indexed-center, integer cost, radius 2; **EXACT FINITE ENUMERATION / NOT_REVIEWED**.

## Finite theorem

Start from the five-event gaps (3,2,2,3), and append two more events using consecutive gaps **(2,1)** rather than the previous radius-separating (3,1). Thus the seven-event gap word is

    (3,2,2,3,2,1)

and the jointly closed coordinates for the two zero-based cuts 0 and 3 are (0,2,4,6,8,10,11). Select exactly **K=4** indexed centers, cover all seven events within distance 2, and minimize the sum of nearest-center integer distances.

For the four masks (uncontracted, a only, b only, both), all optimum costs are **5** and optimizer-family cardinalities are respectively **(5,12,9,17)**. Their intersection residual P=(Fa intersect Fb) minus F0 is empty; the joint-only residual is exactly

    Q = { {1,2,3,6} }.

The complete rank-labeled optimum-path edge supports satisfy **E_ab = E_a union E_b**, including start/sink arcs. Index 5 and index 6 are each absent in some optimal sets of *every* mask; neither is a forced appended center. The attachment separator has length 2 (within the covering radius), so the previous radius-separated block-factorization proof does not apply to this example.

This is a stronger **finite connected-attachment witness** of switch-only Q: an added pair shares coverage reach with the prefix. The unbounded family proved in the preceding note remains the currently established arbitrary-m theorem.

## Complete finite classification of the short attachment alphabet

Keep the first four gaps, K=4 and cuts fixed, and enumerate **all** suffix gap pairs (u,v) in {1,2}². Exact four-mask results:

| (u,v) | Optimum costs | (#F0,#Fa,#Fb,#Fab) | #P | #Q | #joint-only arcs |
|---|---|---|---:|---:|---:|
| (1,1) | (4,4,4,4) | (3,4,3,4) | 0 | 0 | 0 |
| (1,2) | (5,5,5,5) | (5,12,6,13) | 0 | 0 | 0 |
| (2,1) | (5,5,5,5) | (5,12,9,17) | 0 | 1 | 0 |
| (2,2) | (6,6,6,6) | (6,16,10,22) | 0 | 2 | 2 |

Thus (2,1) is the unique appendix in this specified four-word alphabet producing nonempty joint-only Q **without** any new joint-only rank arc.

## Proof by finite exhaustive enumeration

The attached standard-library executable `VERIFY_R5_CONNECTED_7EVENT_SWITCH.py` examines all C(7,4)=35 possible center sets for every closure mask and each of the four suffix words, **560 exact integer candidate evaluations** in total. For each candidate it computes all seven nearest distances, rejects coverage failures, and retains exactly the minimizers. Set differences/intersections are calculated from full optimizer families; each increasing selected-index tuple is converted to a sequence of center-rank and index-labeled arcs including start and terminal arcs, and neutral arcs are counted by set difference. The code asserts the displayed (2,1) family count, unique Q, common minimum cost, no neutral arcs, and neither appended index being universally present. This exhaustive finite domain establishes the table and finite theorem.

This witness motivates investigating repeating (2,1) attachments. Local exploratory data for m<=6 suggest persistent mixed-color Q with no neutral rank arcs, but no arbitrary-m conclusion is asserted here; the load-bearing step is a nonseparable center-budget/coverage invariant.

Scientific state: AUTHOR_FINITE_EXACT_CHECKED / NOT_REVIEWED. No formal Task/CLAIM, native-X6 transfer, or mathematical promotion is asserted.
