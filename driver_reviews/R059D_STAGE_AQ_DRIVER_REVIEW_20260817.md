# R059D Stage AQ Driver Review — Native Cell Escape Multipath Reachability

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Task: `RS-R059D-STAGE-AQ-NATIVE-CELL-ESCAPE-MULTIPATH-REACHABILITY`
Researcher: `EM-R059D-AQ-3A7E61`
Taskbook source: `78f0d56edecb5cd57967b9ff0f1a2d3567550120`
Owner branch: `research/r059d-stage-aq-native-cell-escape-multipath-reachability`
Frozen owner head: `144301562371a182da38856844752cce2750eec5`
Artifact payload head: `6170152d0f27a1132845d3890fc68d64b7697c1c`

## Driver disposition

`DRIVER_ACCEPTED__CANONICAL_SET_VALUED_OUTWARD_GEODESIC_ESCAPE_PROVED__CURRENT_CELL_ONLY_OBJECT_DISTINCT_FROM_FIXED_LENGTH_CIRCLE`

The Researcher disposition

`CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__ESCAPE_OBJECT_DISTINCT_FROM_CIRCLE`

is accepted with the typing refinement below: the theorem is about the **specific AQ state space and transition law** — a current-cell state with strict global shell maximization. It is not a theorem that every escape-based realization of a rotating line segment must fail.

## 1. What is accepted

AQ correctly constructs the native elementary triangular cell carrier in the signed-origin setting. In the auxiliary A2 incidence/CELL_ID chart,

`N3(U(i,j))={D(i,j),D(i,j-1),D(i-1,j)}`

and

`N3(D(i,j))={U(i,j),U(i+1,j),U(i,j+1)}`.

Every elementary cell therefore has degree 3. The auxiliary chart does not reintroduce native zero; `+1 ≡ -1 ≡ O_E` remains frozen.

The source-free escape score is accepted:

`SHELL(C)=d_dual(STAR(O_E),C)`.

The closed incidence certificate is

`K(U(i,j))=(3i+1,3j+1)`,

`K(D(i,j))=(3i+2,3j+2)`,

`H=max(|x|,|y|,|x+y|)`,

`SHELL(C)=floor(2*(H(K(C))-2)/3)`.

This is accepted only as a graph-distance/incidence certificate, not as Enterprise length and not as source Euclidean distance.

The all-radius shell laws are accepted:

`|S_s|=6*(floor(s/2)+1)`;

every even-shell cell has exactly one shell-`s+1` neighbor;

every odd-shell cell has exactly two shell-`s+1` neighbors;

hence

`FAR(C)=FAR_PLUS(C)={D in N3(C):SHELL(D)=SHELL(C)+1}`.

All tied outward branches survive. No single path is selected.

## 2. Exact multipath theorem accepted

For the geometric union of all legitimate one-step endpoint seed cells, AQ proves

`SEEDS=B_2=S_0 union S_1 union S_2`,

with 24 distinct cells.

Every AQ edge raises shell by exactly one, so AQ paths are exactly outward dual-graph geodesics and the directed escape graph is acyclic.

For every `J>=0`:

`END_J=S_J union S_(J+1) union S_(J+2)`

and

`REACH_LE_J=B_(J+2)`.

Therefore the exact-J endpoint set is a three-shell band and the up-to-J reachable set is the full dual ball.

The geometric-seed path-count formulas are accepted:

`P_(2n)=24*2^n`,

`P_(2n+1)=30*2^n`.

For one fixed D6 orientation seed family:

`P_(2n)=6*2^n`,

`P_(2n+1)=8*2^n`.

Driver typing note: the 24-seed formula counts paths after geometrically identifying seed cells shared by different endpoint-orientation labels. If one instead keeps orientation labels as provenance, the labeled path count is a different observable. This does not change any reachable-set theorem.

## 3. Circle non-equivalence accepted, with scope correction

The strong obstruction is not merely `24 cells != 6 vertices`; those are different object types. The decisive theorem inside the frozen AQ semantics is:

`SHELL(next)=SHELL(current)+1`

on every positive escape step.

Hence the AQ transition graph admits no directed cycle at all, while the accepted one-step turn object is a closed period-6 endpoint orbit. Therefore **no positive AQ path under the current cell-only transition law can itself be the fixed-length turn orbit**.

At `J=0`, the AQ output is already the 24-cell seed envelope rather than the six endpoint vertices. Thus no `J` makes the current unmodified AQ output equal the accepted one-step circle.

This is sufficient to reject a universal `J=J(r)` exact-recovery theorem for the current AQ output type.

However freeze the following boundary:

`AQ_CELL_ESCAPE_DISTINCT_FROM_CIRCLE != ALL_ESCAPE_BASED_SEGMENT_RULES_DISTINCT_FROM_CIRCLE`.

AQ does **not** rule out a later escape law whose state retains genuine line-segment information, whose micro-escape resets between turn events, or whose admissibility includes an independently justified fixed-length constraint.

## 4. The key structural diagnosis

The user's proposal said: **let the line segment escape through candidate neighboring cells**.

AQ successfully tested the simplest memoryless interpretation, but after Stage D seed construction the evolving state is just a cell. The fixed segment class supplies the initial endpoint/seed geometry and then disappears from the transition state. No line length class, entry/orientation state, or segment footprint constrains subsequent FAR moves.

That loss of segment state is exactly why the theorem becomes a pure radial geodesic-growth theorem:

`cell + global distance from O_E + local maximization -> strict outward DAG`.

This diagnosis is not a defect in AQ; it is the main scientific result of AQ. It isolates the next missing structure.

## 5. Verification audit

Researcher deterministic checker:

- `334521/334521 PASS`;
- digest `20b24c59143b5f5324e39d2c3e8a0735521b367ad9de8b4a0d68c58c20656256`;
- checker source commit `7408454c1b725d52a99a5e9a2bd1120d38de7060`;
- independent BFS shell replay through 134;
- D6 shell validation through 40;
- all `J=0..32` plus checkpoints 64 and 128;
- BFS/DFS endpoint equality and reverse provenance.

Driver independently rederived the core finite combinatorics: degree-3 adjacency, the shell certificate on a large finite neighborhood, shell sizes, even/odd outward branching, and the one-step seed union `B_2`.

History isolation passes. Comparison from frozen pre-AQ parent to the report commit adds only the AQ taskbook and AQ result files; no prior-stage result file is modified or deleted.

## 6. Frozen outcome

Freeze:

`CANONICAL_SET_VALUED_OUTWARD_ESCAPE = PROVED`.

Freeze:

`ALL_ADMISSIBLE_TIED_OUTWARD_PATHS_SURVIVE`.

Freeze:

`AQ_ESCAPE_PATHS = OUTWARD_DUAL_GEODESICS`.

Freeze:

`AQ_STRICT_SHELL_ESCAPE_GRAPH = DAG`.

Freeze:

`CURRENT_AQ_CELL_ONLY_ESCAPE_OBJECT != FIXED_LENGTH_TURN_CIRCLE`.

Do **not** freeze:

`ESCAPE_ROUTE_CANNOT_PRODUCE_CIRCLE`.

That broader statement is not proved.

## 7. Driver next-stage decision

The next stage must not tune `J`, prune valid paths, or simply re-import the accepted circle. It must test the missing noun in the user's rule: **the line segment itself**.

The next object should be a stateful escape system in which candidate-cell motion retains independently defined segment information. The first target is to determine whether retaining segment state changes the strict-DAG theorem and whether a set-valued turn/closure object can emerge without a single-path selector.

A crucial circularity firewall is required:

- AK `SEG_E(r)` membership is already defined by the accepted `tau` orbit and therefore may not be used as a primitive oracle to force recovery of that same orbit;
- AL `K_E(r)` support carrier may be tested only in a separately typed comparison arm with A8 frontier selection disabled;
- source circle/angle/pi may not define candidate transitions.

AQ is accepted and frozen for Driver purposes.
