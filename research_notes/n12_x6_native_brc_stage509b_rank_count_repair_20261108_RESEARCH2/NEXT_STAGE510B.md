# Stage510-B continuation — Source-aware exact reachability with public rank counts

Frozen science pins: GK `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Refresh current behavioral norms separately; preserve Stage509-B author/reviewer separation.

Predecessor Stage509-B: `PROOF_STAGE509B.md`, `REPRO_STAGE509B.py`, `STAGE509B_EXECUTED.json` in this directory. Earlier predecessor Stage508-B commit `6b169d6e858353bf253f1a28951ef6c3e8c71e44`.

**Verified correction:** Stage508's opaque `F`-only gaps with no public P counts are falsified by `n=12,h=1,R={2,10,11},S={1,3}`, source sets `x={1,4,7}`, `y={1,7}`. Old compact states equal but `DELETE_KTH_PUBLIC(3)` legal only for x. Corrected `G=(complete F, exact #P)` and directly touched original mask `D_h` are sufficient for the declared grammar. INSERT2 original-neighbor marks are redundant because DELETE2 at the same pre-action state forces the third-from-last (left neighbor) into `D_h`. Program completed 1,839 roots, 48,844 paired future nodes, 59,280 transitions with all assertions passing. Native controls remain unconfirmed due backend mismatch.

**Primary research question:** derive an exact non-exponential or parameterized symbolic transformation to compute `D_h(w)` without full breadth-first enumeration of identity/tag skeletons. Show both soundness and completeness, then benchmark the exact same settings on length 19/h=3 and length 28/h=2: preprocessing states, time, peak RSS, all 12 directions and 144 observer relations.

**Secondary question:** can `#P` in each opaque gap be saturated at a horizon/rank-dependent threshold (e.g. `K+h`) while preserving rank legality and selected public targets through all futures? Prove a congruence or provide a strict collision for the proposed saturation.

Separate open line: 12 signed native directions, all 144 active directed relations, heterogeneous repeated-edge Euler–BRC exact rank/unrank, fully accounted big-integer bit cost, preprocessing, wall time and peak RSS on identical datasets. Distinguish enumeration from random access ranking.
