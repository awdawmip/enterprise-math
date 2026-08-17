# R059D Stage AQ — Native Cell Escape Multipath Reachability Report

Researcher-ID: `EM-R059D-AQ-3A7E61`

Task: `RS-R059D-STAGE-AQ-NATIVE-CELL-ESCAPE-MULTIPATH-REACHABILITY`

Owner branch: `research/r059d-stage-aq-native-cell-escape-multipath-reachability`

Frozen source parent: `c25b6d0385648c27292f25aeeeff2b816654a4ba`

Taskbook source/activation: `78f0d56edecb5cd57967b9ff0f1a2d3567550120`

## Primary result

`CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__ESCAPE_OBJECT_DISTINCT_FROM_CIRCLE`

AQ successfully defines the user's proposed all-path native escape process without choosing UP/DOWN, without using a source circle, and without privileging tied branches.  The resulting object is mathematically rigid, but it is not the previously accepted Enterprise circle.

## 1. Native three-neighbor cell carrier

Using the signed-origin A2 conjugacy only as an incidence/CELL_ID chart, define elementary triangles `U(i,j)` and `D(i,j)`.  Their exact edge-neighbor lists are

`N3(U(i,j))={D(i,j),D(i,j-1),D(i-1,j)}`

and

`N3(D(i,j))={U(i,j),U(i+1,j),U(i,j+1)}`.

Thus every native elementary triangular cell has exactly three edge-adjacent cells.  `+1 ≡ -1 ≡ O_E` remains the native origin and auxiliary zeros never become native coordinates.

The six origin-incident cells form `STAR(O_E)`.

## 2. Exact native shell and FAR rule

The native escape score is dual-graph distance from `STAR(O_E)`.

An exact source-free incidence certificate is obtained from

`K(U(i,j))=(3i+1,3j+1)`

and

`K(D(i,j))=(3i+2,3j+2)`.

If

`H=max(|x|,|y|,|x+y|)`,

then exactly

`SHELL(C)=floor(2*(H(K(C))-2)/3)`.

The shell size is

`|S_s|=6*(floor(s/2)+1)`.

Every even-shell cell has exactly one outward neighbor and every odd-shell cell has exactly two.  Therefore globally

`FAR(C)=FAR_PLUS(C)={D in N3(C):SHELL(D)=SHELL(C)+1}`.

All tied outward branches survive.

## 3. One-step seed theorem

For one AP one-step axis endpoint, all six incident triangular cells are retained; selecting a preferred triangle would already encode an unproved turn direction.

Each orientation has six seeds with shell multiset `{0,0,1,1,2,2}`.  The geometric union over all six D6 endpoint orientations is exactly

`B_2=S_0 union S_1 union S_2`,

with 24 cells.

## 4. Exact all-J escape theorem

Every escape edge raises shell by exactly one, so AQ paths are exactly outward dual-graph geodesics.

For the aggregate one-step seed family:

`END_J=S_J union S_(J+1) union S_(J+2)`

for every `J>=0`, and

`REACH_LE_J=B_(J+2)`.

Thus exact-J endpoints are three complete consecutive shells; up-to-J reachability fills the entire dual ball.

Endpoint counts are

- `9J+24` for even J;
- `9J+21` for odd J.

If `J=2n`, the number of admissible paths is `24*2^n`; if `J=2n+1`, it is `30*2^n`.

For one fixed orientation, the corresponding path counts are `6*2^n` and `8*2^n`.

The first aggregate branch merger occurs at J=2.  Multiplicity is retained only as provenance; no endpoint is deleted because another path reaches it more or fewer times.

## 5. Census

The taskbook-required `J=0..32` census is represented by exact closed formulas plus an endpoint-multiplicity dynamic ledger.  The full multiplicity ledger across those budgets contains 5,496 endpoint records and has SHA-256

`00723fe0bb1c8b7d8526e1083af710c91aef5fa508d599d3028479e538ae5f53`.

Selected values:

- J=0: 24 paths, 24 endpoints, 24 reachable cells;
- J=8: 384 paths, 96 endpoints, 216 reachable cells;
- J=16: 6,144 paths, 168 endpoints, 600 reachable cells;
- J=24: 98,304 paths, 240 endpoints, 1,176 reachable cells;
- J=32: 1,572,864 paths, 312 endpoints, 1,944 reachable cells.

Larger checkpoints:

- J=64: 103,079,215,104 paths, 600 endpoints, 6,936 reachable cells;
- J=128: 442,721,857,769,029,238,784 paths, 1,176 endpoints, 26,136 reachable cells.

The path count is not a probability.

## 6. Structural interpretation

The directed escape graph is a DAG, because shell is a strict integer Lyapunov function.  Ties occur intrinsically on every odd shell, so no single path is selected by the native farthest rule.

Nevertheless the set-valued path family is canonical: once the native carrier, origin star and graph-distance shell are fixed, the complete outward-geodesic family is uniquely determined.

For J>=1, `END_J` is a connected three-shell annular band, not a simple cycle.  `REACH_LE_J` is a filled ball.

## 7. Circle emergence audit

The old circle was not used until after the escape object was frozen.

The AP one-step visible circle is a six-native-vertex period-6 orbit.  AQ already differs at J=0: `END_0` has 24 cells.  For every positive J it has three full shells and more than six cells.

More fundamentally, AQ's directed graph is acyclic.  Therefore no positive AQ escape path can execute a closed period-6 orbit.

Hence no J reproduces the accepted one-step circle exactly.  Since r=1 already fails for every J, there cannot be a universal native relation `J=J(r)` that exactly recovers the accepted circle at every radius without changing the AQ object or pruning valid paths.

The AP axis vertices are incident to the J=0 seed envelope, but that tautological incidence containment is not circle emergence.

## 8. Relation to AP

AQ removes the need to choose a collapse direction only for the new reachability problem.  `COHERENT_COUPLED_COLLAPSE_DIRECTION` is not an AQ axiom.

However AP DOWN+axis completion is not one distinguished AQ path, and neither is `DIRECT_FORWARD_AXIS`: AP evolves a closed endpoint/collapse state orbit, whereas AQ evolves cells strictly outward in a DAG.  Embedding an AP closed cycle into AQ would require a new endpoint-to-cell lift and would contradict strict shell increase.

Thus AQ bypasses, rather than solves, the AP unique-collapse-direction problem.

## 9. Verification

Deterministic checker source commit: `7408454c1b725d52a99a5e9a2bd1120d38de7060`.

Independent run:

- `334521/334521 PASS`;
- digest `20b24c59143b5f5324e39d2c3e8a0735521b367ad9de8b4a0d68c58c20656256`;
- independent BFS shell validation through shell 134;
- D6 validation through shell 40;
- all J=0..32 from all six one-step orientation seed families;
- BFS/DFS equality;
- branch merger accounting;
- reverse provenance reconstruction;
- J=64,128 checkpoints;
- no-native-zero firewall;
- no source geometry in escape score;
- circle/AP comparison only after the AQ escape object was frozen.

History isolation is performed after this report and is not used as theorem evidence.

## 10. Final boundary

AQ proves a canonical set-valued native escape resolver, but the object is a geodesic escape envelope rather than a fixed-length turn circle.

Open beyond AQ:

- whether a second native constraint can cut a meaningful boundary out of the escape ball without reintroducing source geometry or arbitrary path selection;
- whether another seed type or invariant jump law produces a circle-like frontier naturally;
- whether the escape object has independent coordinate-generation significance.

Stop for Driver review.  No later stage is consumed.
