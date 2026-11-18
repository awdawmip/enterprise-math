# X6 Unit138 — exact rank-one carrier Voronoi/Delaunay executable consumer boundary

Date: 2026-11-18. Mother objective: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Research lane: chatgpt-research-onhour-enterprise-math-20260923; own author EM-X6-FB6990. **AUTHOR SOURCE-EXACT REPLICA CHECK / FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Input pins and actual scope

- Frozen signed-native P000 V5 and six-axis Cell torsor: enterprise-math `59538f585d037d09ef687b28715c4bc1a3f9fe03`.
- Pre-rebase comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Newly selected **historical executable consumer** `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py`, frozen and current **same Git blob** `900e246b0dafaa35d2452191e3df508a2d15a389`. Its `delaunay_cells` at lines 134–153 constructs **only noncollinear empty-circle boundary sets**; `dual_adjacent` at 157–198 and `dual_edges` at 201–209 use rational Euclidean carrier bisector feasibility. This is a carrier-only original consumer, not native signed-X6.
- Historical result `research_notes/TOOL_DISCOVERY_CARRIER_VORONOI_DELAUNAY_DUAL_CELL_RESULT_20260823.md` frozen blob `f02124cce925bc181821f9429c87364c8652ffd5`; current main adds a 2026-11-15 notice distinguishing the present signed-six-axis native comparator from the older carrier-specific claim. Prior native discrete Voronoi/tie work `research_notes/X6_LP026_LP028_NATIVE_DISCRETE_VORONOI_BISECTOR_TIE_20261115_0300.md` is consumed, **not recalculated**.

## Exact theorem and smallest witness

For three distinct collinear Cartesian-Euclidean carrier sites with positions ordered `s1,s2,s3`, the nearest-site Voronoi codimension-one pair relation is exactly `{s1,s2}` and `{s2,s3}`. Proof: parameterize their common line by a unit direction. Squared-distance differences eliminate all perpendicular query coordinates, so each nearest-site region is a strip bounded by the midlines of consecutive site coordinates. The nonconsecutive sites cannot tie for the minimum because the intermediate site is strictly closer on their common bisector. Conversely each consecutive-site midpoint bisector supports an unbounded one-dimensional common nearest-site boundary.

The source's `delaunay_cells` scans only noncollinear triples, so **for all such collinear three-site inputs** it returns no 2D Delaunay cell, while `dual_edges` returns the two genuine Voronoi edges. The smallest integer example `A=(0,0), B=(1,0), C=(2,0)` has `delaunay_cells={}`, `dual_edges={{A,B},{B,C}}`. A consumer equating `dual_edges` with edges derived from these rank-two Delaunay cells outside the rank-two domain would therefore lose two real adjacency relations.

This is a **rank-one affine-dimension/type-interface gap**, not a contradiction in the original checker’s explicitly rank-two/noncollinear theorem, not a global source failure, and not a primitive signed-native geometry or BRC theorem. The correct implementation route is to (a) constrain the `delaunay_cells` contract to rank-two noncollinear cases and report `RANK_ONE_UNSUPPORTED` to broader callers, or (b) add an explicit rank-one consecutive-site Delaunay-edge specialization, retaining ties and labels. Neither choice can silently be added to the frozen accepted artifact without scoped approval.

## Executed finite evidence

Local independent checker `research_checks/X6_UNIT138_CARRIER_RANK_ONE_DUALITY_CHECK_20261118.py` reproduces the relevant source functions exactly as written, but **does not import or execute the entire original historical script**. It exhaustively enumerates all `C(25,3)=2300` distinct-coordinate unordered triples from the lattice square `[-2,2]^2` using exact `Fraction` arithmetic and always-on exceptions. The `152` collinear triples each have zero noncollinear Delaunay cells and exactly the expected two consecutive-neighbour Voronoi edges. All `2148` noncollinear triples have exactly one three-site Delaunay cell and three Voronoi adjacency edges. Zero check failures.

The checker ran under normal Python, `-O`, `-OO`. All three JSON outputs had identical SHA256 `1ae34edf1cfe851721007f421574907208eb796fd1924fdeb54ed722581adc04`. Exact certificate: `research_checks/X6_UNIT138_CARRIER_RANK_ONE_DUALITY_RESULTS_20261118.json`. Original R063 six-file/512-case benchmark not rerun.

## Boundaries / next action

This extends actual 28-LP LP026/LP028 **downstream executable consumer typing** with a new rank-one source condition. It does not locate the alleged historical LP011 signed-native dominant-axis caller or LP019 natural N-BRC subtraction caller: both remain `UNRESOLVED_PROVENANCE`. Preserve all Units1–137, current Activity #151 and native PROGRESS through Unit137; no duplicate proofs, no borrowed maintenance identity, no self-admission.

A subsequent authorized code revision should target only a demonstrated production consumer that requires rank-one coverage, then run exact original-object regression of that consumer. Next scientific audit should pursue a genuinely unchecked consumer crossing carrier comparator, min-zero observer or signed-native Cell input types, retaining exact file/line and input/observer provenance; independent Driver review and the original R063 benchmark remain separate.

Author status: SOURCE-ATTESTED / BOUNDED-EXACT-EXECUTED / UNREVIEWED / NOT_ADMITTED.
