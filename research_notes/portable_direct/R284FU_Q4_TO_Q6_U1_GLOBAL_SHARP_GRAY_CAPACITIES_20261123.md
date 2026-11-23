# R284FU — Three additional sharp noisy omission capacities, q=4,5,6 and u=1

Date: 2026-11-23, informed portable TASK_RESEARCH.
Status: AUTHOR_EXACT_FINITE_PROOF / NOT_REVIEWED. Auxiliary four-generation binary observer and frozen R284CO lineage only; no change to P000/ACTIVE X6 or Result/CLAIM authority.

## Result

In the R284FM/R284FP/R284FT reset-free cyclic four-label model, with omission budget q per non-atomic transition, arbitrary persistence of prior omissions, one independent Hamming bit flip per read (u=1), stateless stable decoding, no third-phase prefix success and no new-then-old success while a write is paused, the **global optimal** binary widths are

| q | Exactly minimal width |
|---:|---:|
| 4 | 26 |
| 5 | 30 |
| 6 | 34 |

Together with the existing R284FS result n_min(2,1)=18 and R284FT result n_min(3,1)=22, this verifies n_min(q,1)=4q+10 for every INTEGER q in [2,6]. The same formula for unbounded q is now a conjecture, not a theorem.

## Complete finite exclusion

R284FP analytically proves n_min(q,1)>=4q+8 whenever q>=3. It remains to rule out precisely the two next widths, n=4q+8 and 4q+9. The R284FT checker does so using an exhaustive equivalence-class partition of ALL fixed four-code binary labels by seven column multiplicities, a complete six-pair adjacent/opposite distance prefilter, six exact R284FM stable-state observer capacity cuts, and an exact integral flow for source-stable-to-target-stable minimum Hamming distance after each non-atomic partial overwrite. For each surviving histogram it examines every omitted-write type count (total <=q) at every possible attempted-prefix count, and asks by finite BFS whether even one monotone write-order path can avoid necessary third-success and early new/old rollback contradictions. Passing the test would only be necessary; failing all paths is a valid complete exclusion.

| q | Excluded n | All histograms | Distance survivors | Six stable-cut survivors | Edge 0->1 survivors | Edge 1->2 survivors |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 24 | 593775 | 10493 | 7 | 1 | 0 |
| 4 | 25 | 736281 | 23954 | 69 | 10 | 0 |
| 5 | 28 | 1344904 | 24052 | 7 | 1 | 0 |
| 5 | 29 | 1623160 | 49708 | 66 | 10 | 0 |
| 6 | 32 | 2760681 | 49836 | 7 | 1 | 0 |
| 6 | 33 | 3262623 | 95253 | 66 | 10 | 0 |

No possible fixed code or write order at the six examined widths survives. Conversely, R284FE's proven two-group repeated-Gray construction uses two groups of 2q+4u+1=2q+5 bits each, total 4q+10. Its four edges also pass the R284FT necessary prefix oracle at the declared q. Combining the R284FP lower bound, these six finite exclusions and the R284FE explicit legal construction proves the table.

## Reproduction

Run R284FU_q4to6_u1_sharp_gray_checker.py, saved in the same research_notes/portable_direct directory, with Python 3. It imports the previously published exact R284FT_q3u1_22bit_flow_checker.py, changes q only at the declared model parameter, recomputes the entire stable-cut table for each q, and independently iterates every seven-pattern histogram at each of the six sizes. All six exact expected count vectors and the six zero-survivor results are asserted. Standard library only; integer arithmetic; the run was executed successfully by the author. The finite proof relies on the exact flow-prefix lemma proved in R284FT, and the earlier R284FM stable-residual model; independent mathematics Review remains pending.

Frozen source dependencies:
- R284FT exact flow-prefix lemma and q3u1 case: enterprise-math@b654d9bbb0ac5f7083afe24076a8bb24dc4ab1f0, plus checker @543519e94f00aa8c44e5557d86f91cff9f328811.
- R284FP high omission lower bound: enterprise-math@de49ae0239abee14619a730fe6ea60614a2cde5b.
- R284FM reachability and six-pair stable flow-cut: enterprise-math@1d1c5dd412719c7aaf016187b6493b77253cd9f9.
- R284FE repeated-Gray sufficient construction: enterprise-math@9974b3b5a1031bb5c841ab5a4950a9c55baed9e0.
- R284FS q2u1 sharp case: enterprise-math@aa9bd1a7aa77adb171978f03b99eeeac2405dcf0.

## Next

Develop a parameter-uniform argument that the boundary n=4q+8 and n=4q+9 cannot support a four-phase q>=2,u=1 protocol; current exact finite results q=2..6 provide verified test targets. A separate useful extension is q>=2 at u>=2, where the current R284FP necessary width and R284FE Gray construction leave an unknown gap. Preserve last-write provenance when building stronger observer approximations.
