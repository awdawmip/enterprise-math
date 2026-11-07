# Stage511-E — Full-cost Euler–BRC exact ranking comparison

Frozen science inputs (do not update): Global Knowledge `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.

## Exact completed frontier

Stage510-E theorem: Euler word count is in-arborescence determinant times last-exit factorial quotient divided by parallel-edge factorials. Prefix count gives exact lexicographic random-access rank/unrank over native-X6 direction words retaining all 144 ordered adjacency multiplicities. The canonical benchmark `m[i,j]=1+(i*j+i+j)%3` for `i,j=0..11`, start=end=0, has 336 directed edges, all 144 active relations, 943-bit total count. Author-side exact Python checker completed 4,838 exhaustive tiny-matrix cases plus 0/mid/max/pseudorandom 940-bit round trips.

Sources: `PROOF_STAGE510E.md`, `EULER_BRC_RANK.py`, `EULER_BRC_EXECUTED.json` in this folder. The source file was checked against the actual locally executed file by Git blob identity `533fc61021bb03b7bb3204e347a6f189d65d1369`.

## Specific next question

On the identical full-144 active 12-direction heterogeneous inventory, compare the current last-exit determinant prefix evaluator against a **structurally different** exact solution (e.g. reusable arborescence sensitivity updates, rank-aware dynamic programming, or split edge-domain generating functions) for cold and warmed full rank and unrank. Retain true end-to-end costs: input parse/representation, determinant/factorials, cache, big-int bit operations, rank output, wall clock, peak resident memory. A second identical implementation of the same formula is not an independent algorithm comparison.

Add nonsymmetric balanced and open Euler trails, including self-loops and disconnected supports, verifying every boundary case by exhaustive finite small graphs and exact integer arithmetic. Investigate whether low-rank Laplacian updates lower repeated suffix-count cost and characterize the applicable graph family. Keep full 12 signed X6 directions and 144 relation dimensions even if some individual test inventory has zero coefficients; do not interpret static word ranking as physical dynamics.

Another independent research frontier: Stage511-B's non-enumerative exact computation of direct-touch mask `D_h(w)` and gap-local public source-count saturation.
