# Unit249 — chronological source-route replay separates two centre-Port precision update candidates

Date: 2026-11-22; `RS-X6-NATIVE-TIME-DYNAMICS` / `TP2-91D4A7C2F63805BE21A3`.
Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. The project P000 signed six-axis Cell torsor, selected three-axis native slice, three-force intact occupancy and chronological BRC identifiers remain as originally frozen at `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.

## Direct reuse of actual prior source cases

This experiment consumes *without regenerating them* the [36 original Unit245 optimal labelled-triad BRC traces](https://github.com/awdawmip/enterprise-math/blob/f56840285cafeb9f5767ea91e903e1f53808186f/research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json), and validates original zero-centre terminal C24 readouts against [Unit247's own exact certificate](https://github.com/awdawmip/enterprise-math/blob/0628624fc23d1f34521119b809398c0146ed9bbb/research_checks/X6_TIME_UNIT247_PORT_PRECISION_C24_COSET_RESULTS_20261122_0000.json). No fresh shortest-path or original native benchmark execution is asserted.

We keep every labelled A/B primitive step, occupancy guard, original signed ring winding `(-12,+12)`, unique available directed ingress `x_i→P` and egress `P→x_j`, and exact route cost. Compare two **conditional precision update laws** on the same preserved BRC histories:
- `Z`: zero additive precision changes on both centre edges, the original Unit247 candidate;
- `C`: Unit248 compensating law `alpha_i=-B(i), beta_j=B(j)`, with `B(k)=sum_{r<k}g_r` and `g5=g10=3` (other ring weights zero), and all inverse ring-edge weights negated.

For each labelled triad `T`, let `c_T` count complete centre passages and `L_T` its signed original ring count. The full chronological replay gives
[
\boxed{\Delta_T^C-\Delta_T^Z=(B(j)-B(i))c_T\pmod N.}
]
This is exact for every path in the specified directed graph: only centre events differ between the candidate update laws. For all 36 shortest certificates, Unit246's replayed source counts satisfy `c_A+c_B=m(d)=12/gcd(12,d)` and one triad carries all passages. The six eligible ingress/egress positions split into `B=0` for 0,2,4 and `B=3` for 6,8,10.

## Sharp discrimination classification

For identical-B-class ingress and egress, the signed centre increment difference is zero, so the labelled terminal C12 and C24 readouts coincide under the two laws. For cross-class pairs, the nonzero difference is `±3m(d)`. With even nonzero `d`, `m(d)` is one of `2,3,6`, and `3m(d)` is nonzero modulo both 12 and 24. Thus every one of the **18 cross-class ordered pairs** is distinguishable by terminal C12 and terminal C24 readout, and every one of the **18 within-class pairs** is indistinguishable by that same terminal observer:

[
\boxed{\#\operatorname{Distinguishable}_{C12}
=\#\operatorname{Distinguishable}_{C24}=18\text{ of }36.}
]

Most importantly, the two **existing 28-native-event shortest opposite-winding** guarded histories change their labelled C24 terminal predictions from the original `(18,6)` under `Z` to:
[
\boxed{(i,j)=(6,0):\ (12,6),\qquad(8,2):\ (18,0)}
]
under `C`. The input paths and event costs are unchanged; this is an observer-law distinction on the original evidence.

## Exact execution

A Node-compatible dependency-free JS checker was **executed in current V8** on the actual immutable Unit245 36-case and Unit247 terminal-result bytes. It replayed every ordered primitive event, verified labelled target-empty occupancy, signed ring winding and exact native step count, retained complete centre passages, checked original Unit247 C24 readouts, and independently verified Unit248's scalar cocycle. **2145 exact integer assertions; 36 source routes; zero failures.** It did not simulate a physical environment or a Source-admitted precision sensor.

The shortest actionable existing source-route measurement candidates are the `(6,0)` and `(8,2)` 28-event paths. Both laws also differ on the 8-event single-triad same-Cell test from Unit248. Which law applies to the world remains an experimental question; precision should be measured independently at the declared C12/C24 resolution. Preserve all original Cell, Port, labelled triad, event order and environmental states in any physical replay.

No new claim/run, Native semantic PROGRESS, Driver review, accepted Result or R063 native six-file benchmark is asserted. The earlier Source materialization issue remains [#2903](https://github.com/awdawmip/enterprise-math/issues/2903).
