# Stage511-B — Exact reachability synthesis and gap-specific rank-state minimization

Research continuation from Stage510-B (`PROOF_STAGE510B.md`, `REPRO_STAGE510B.py`, `STAGE510B_EXECUTED.json`) and Stage509-B (immutable science commit `94f52374ed15a2a8cb41a7bf8b5aca163e8c1370`).

Frozen scientific pins (unchanged): GLOBAL_KNOWLEDGE `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Refresh only behavioral norms independently.

## Completed precise unit

For the Stage509 BRC grammar and **actual-provenance** direct-touch mask D_h, the opaque-gap count `#P` may be replaced by `min(#P, K−1)`, `K=max(S)`, while preserving all legal futures of depth h and their full 6D/144 ordered-pair observer. For K=1 no count field is needed. The threshold K−1 is best possible as a uniform cap over all horizons (strict h=1 witness for every K>=2). The BRC relation summary F and original mask synthesis remain untouched.

Computational checks: 1,043 roots, 15,801 identity/tag skeleton states, 31,145 paired future nodes, 35,646 legality checks, 30,102 exact full-observer transition comparisons; six lower-cap collision witnesses K=2..7. Reported result: ALL_ASSERTIONS_PASS.

## Primary new research question

Construct an **exact**, non-future-tree-enumerating algorithm for the original direct-touch set `D_h(w)` under adaptive `DELETE_KTH_PUBLIC(k)`, `POP`, `DELETE2`, `INSERT2(c)`, and `SET_END(r,c)`.

Possible route: quotient tagged identity skeletons by a bounded *right-offset + public-rank profile + insertion order* state while preserving enough local source tags to simulate DELETE2 and position shifts. Define a closure transformer; prove soundness and completeness against full original identity-skeleton semantics, not just overapproximate position halos. Complexity claims must account for input tagging, preprocessing, bit length, state construction, and output size. Test on the same n=19,h=3,R={2,11},S={1,3} and n=28,h=2 settings with all 12 signed directions and all 144 ordered relations.

Secondary: derive a reachable-scan, **gap-specific** exact quotient of `#P` finer than uniform `K−1`, and test whether extra reductions depend on h or on the source-ranked language's set S. Witness pairs must have both histories' direct-touch masks calculated from their *own* actual tags.

Separate open line: heterogeneous repeated-edge, 12-direction/144-active-relation Euler–BRC exact ranking and unranking; compare full big-integer bit cost, time, peak RSS on identical inputs, distinguishing ranking from enumeration.

Reviewer/Owner status: independent Driver review pending; native authenticated owner, CLAIM and Result not verified. Do not relabel author-side source persistence as formal acceptance.
