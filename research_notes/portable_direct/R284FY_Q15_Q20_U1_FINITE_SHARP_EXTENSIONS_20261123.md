# R284FY — Exact finite q=15..20 sharp capacities for reset-free noisy four-phase tags

Date: 2026-11-23 (Asia/Shanghai).
Research mode: informed portable TASK_RESEARCH, unshared science.
Status: AUTHOR_EXACT_FINITE_COMPUTATION / PINNED_LEMMA_DEPENDENT / NOT_INDEPENDENTLY_REVIEWED.
Parent frontier: R284FV -> R284FW -> R284FX, and frozen R284FP/R284FE analytical bounds. No new P000, world axiom, formal Task, CLAIM or Result is asserted.

## Exact finite statement

In the four-fixed-binary-codeword reset-free cyclic model of R284FV/R284FX, with q missed attempted bit writes per publication, unlimited cross-generation retained omissions, u=1 read flip, stateless correct stable reads and no third-phase read/new-to-old rollback while publishing:

**n_min(q,1)=4q+10, for each integer q=15,16,17,18,19,20.**

Thus the new sharp bit widths are **70,74,78,82,86,90** respectively. Combined with pinned q=2..14 results, this extends the *author-level finite established range* to 2<=q<=20, subject to the cited mathematical input lemmas and computation correctness. The all-q statement is open.

## Method and mathematical coverage

For q>=3, the pinned R284FP inequality gives n>=4q+8. The pinned R284FE two-block Gray construction attains n=4q+10 for u=1. It suffices to exclude n=4q+8 and n=4q+9.

XOR-normalize phase 0 to zero. Delete constant column types, since they carry no phase distinction and cannot improve capacity. Every remaining column has one of the seven nonzero 3-bit phase-(1,2,3) patterns. For each candidate width n, enumerate **every** nonnegative seven-histogram x with sum n, a total of binomial(n+6,6). Check all six pairwise codeword-distance necessities and, for survivors, all six exact eight-vertex residue-flow cuts, using R284FM. On stable-cut survivors, check all omission histories and monotone count-lattice update orders on the first two publication edges via R284FT's exact integer-flow prefix oracle. A violated prefix requirement rules out the complete protocol.

The table reports actual exact-integer author executions, not extrapolated counts:

| q | n=4q+8: histograms / six distances / stable cuts / first-edge / two edges | n=4q+9: histograms / six distances / stable cuts / first-edge / two edges |
|---:|---|---|
| 15 | 185250786 / 3474987 / 7 / 1 / 0 | 201359550 / 4827423 / 66 / 10 / 0 |
| 16 | 256851595 / 4828071 / 7 / 1 / 0 | 277962685 / 6593608 / 66 / 10 / 0 |
| 17 | 350161812 / 6594330 / 7 / 1 / 0 | 377447148 / 8868270 / 66 / 10 / 0 |
| 18 | 470155077 / 8869070 / 7 / 1 / 0 | 504981379 / 11762331 / 66 / 10 / 0 |
| 19 | 622614630 / 11763213 / 7 / 1 / 0 | 666563898 / 15403949 / 66 / 10 / 0 |
| 20 | 814216767 / 15404917 / 7 / 1 / 0 | 869107785 / 19940218 / 66 / 10 / 0 |

**5,596,673,112** seven-histogram configurations tested in total; **118,330,387** passed the distance necessities. For all twelve parameter/width pairs, stable survivors were exactly 7 or 66. On the first publication edge survivors were exactly F0 or F1--F10, respectively, with A=2q+5, B=2q+3 as defined in R284FW. Every one failed by the end of edge two (zero complete first-two-edge survivors). This also supplies a finite-data crosscheck of the R284FW family obstruction, not an all-q family completeness proof.

## Recalculation provenance and output certificate

Pinned algorithm definitions on Enterprise Math:
- `research_notes/portable_direct/R284FV_stable_cut_scan.cpp`: Git blob `66f5cab9d6882f74fb63ae1500dd0b0ff0941a8b`.
- `research_notes/portable_direct/R284FV_prefix_count_lattice.py`: Git blob `77ceb62e51e87737d53193b86e5e40799f8716d4`.
- `research_notes/portable_direct/R284FW_ALL_Q_PARAMETRIC_FIRST_EDGE_SURVIVOR_SECOND_EDGE_OBSTRUCTION_20261123.md`: Git blob `18f9befb076f784d5aad4b11e0717109d0e850ee`.
- Parent R284FX exact output note Git blob `a5eb4c6c7bd15ea8755c2d3d6e3eee3ad5b46138`.

The author compiled a faithful local transcription of the pinned C++ scanner using `g++ -O3 -std=c++17`, and ran an equivalent transcription of the pinned standard-library Python integral-flow and count-lattice core, extending only the parameter interval and the main entry. A q=5, n=28/29 control run reproduced the earlier exact source counts 7/66 and first-edge 1/10, second-edge 0/0. The 12 production pairs were each computed and their 7/66 full stable histogram output lists retained locally; the source-checker core was run on them, and a second pass verified the explicit F0--F10 equality for each q. No floating-point arithmetic enters either scientific decision procedure.

The published companion `R284FY_q15_q20_reproduce.sh` runs the **original** R284FV repository implementations instead of the local transcription: the original C++ source is compiled and the original Python module's main-range assertion is bypassed only by importing its existing `safe_path` function and assigning its q parameter. It asserts exact F-family equality and no two-edge survivors. The CSV `R284FY_results.csv` records observed rows plus SHA256 of each complete stable histogram list from the local author calculation, allowing an independent rerun to compare actual bytes. Those SHA256 are author evidence, not independent corroboration.

All statements of optimality rely on correctness of R284FP lower bound, R284FM/R284FT flow oracles, R284FE upper construction and the complete finite integer computation. Formal Result, independent Review and strict Activity audit have not taken place.

## New exact mathematical frontier

For every integer q=15..20 the observed stable-cut counts remained 7/66 and first-edge survivors remained F0/F1--F10. The principal open lemma is still the **parameter-uniform** completeness of that eleven-family classification for every q>=2 (or sufficiently large q). A potentially useful next route is symbolic elimination of the six-cut disjunctions followed by parametric first-edge count-lattice obstruction, with independent reproduction of the finite results. Once proved, R284FW's all-q barrier and the existing upper bound would yield the infinite-parameter capacity theorem.

This work retains the original frozen scientific inputs, author provenance, identity boundary and pending Activity checkpoint; it does not use the temporal/state observation as proof of formal Task ownership.
