# R705 — X6 terminal Port observer hierarchy, BRC information bounds and rotation-equivariant addressing

Date: 2026-11-11 Asia/Shanghai. Parent `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, P000 V5 and native signed X6 Cell torsor. Prior author work R704: `4112fd8d076cf03f7040960803d7cb6e48a7f84c`. This is a proved statement **within the static independent terminal Boolean-gate candidate model**, not a native Link/Port or triadic balance law.

## Model
Fix an arbitrary chosen Cell c of the affine Z^6 torsor. Enumerate all 960 ordered signed three-distinct-axis native paths; they meet 160 endpoints. R704 proved that each endpoint e has exactly three distinct third-step directed gates K_e, each controlling exactly two disjoint path sources. Hold first-/second-step gates open and let A_e be the open subset of K_e. The unnormalized BRC source-count observer reads C_e=2|A_e|. For a named set S_e ⊆ K_e of r distinct terminal gates, define the addressed observer O_(e,S_e)(A_e)=(|A_e|, (1_{k∈A_e})_{k∈S_e}). Positivity is path multiplicity, **not** signed-force cancellation.

## Exact observer-quotient theorem
For each endpoint and any r=0,1,2,3, the number of distinct observations is Q(r)=2^r(4-r). To prove this, fix one of 2^r addressed membership bit patterns; the remaining 3-r gates can have any count from 0 to 3-r, giving 4-r possible total counts. All values are realizable; pairs with different addressed bits or different remainder counts are distinguishable.

Consequently, for independent terminal gates at all 160 endpoints, observer state counts are:
- r=0: 4^160 = 2^320 (optimal fixed code: 320 bits).
- r=1: 6^160 (optimal fixed code: **414 bits**, because 2^413 < 6^160 ≤ 2^414).
- r=2: 8^160 = 2^480 (optimal fixed code: 480 bits).
- r=3: 8^160 = 2^480 (optimal fixed code: 480 bits).

With 2 named terminal Port bits and |A_e|, the third Port bit is recovered by subtraction. Hence two named gates plus the endpoint count recover full static terminal support. A third named query carries no new information. The largest unresolved local fiber has 3 subsets for r=0, 2 for r=1, and 1 for r≥2. For heterogeneous query counts r_e, the global state number is ∏_e[2^{r_e}(4-r_e)], with minimum fixed bits ceil(log2(product)). With d candidate gates, the same proof yields Q_d(r)=2^r(d-r+1): d-1 named bits plus the total count reconstruct all gates.

## Exact BRC witness
At relative endpoint e=c+e_0+e_1+e_2 (three positive signed steps), let all other terminal gates be closed, and keep all initial/middle gates open. In state A only the terminal gate with last axis 0 is open, while state B opens only the gate with last axis 1. Both complete endpoint-count histograms are identical (C_e=2, all others 0). The axis-0 named terminal-source query returns 2 in A and 0 in B. Thus a query about the actual last-axis identity distinguishes states identified by the 320-bit histogram observer; the 414-bit addressed observer retains that targeted query, under the explicit static future query scope.

## S6-equivariance and selector obstruction
For any g∈S6, co-transform the signed Cell coordinates, terminal Port address, allowed-gate subset and query label. Then C_{ge}(gA)=C_e(A) and 1_{gk∈gA}=1_{k∈A}; the entire addressed-query family is covariant under the axis-permutation skeleton. But a deterministic intrinsic map that chooses a nonempty proper subset of terminal axes from an unmarked triple cannot be S6-equivariant: the endpoint stabilizer contains S3 acting transitively on its three axes, and only the empty or full subsets are S3-invariant. A chosen named address is therefore external typed query input, co-rotated with the state; it is not selected from an unmarked endpoint by an equivariant rule.

## Verification and provenance
The Python checker reconstructs all 960 signed words, 160 endpoints and 480 disjoint terminal source pairs, exhausts all 8 terminal gate masks and 4 query scopes, verifies the same-histogram witness, tests 720 permutations × 8 masks × 3 addressed queries = 17,280 covariance instances, and confirms the S3 stabilizer obstruction and integer encoding bounds. Exact standard-library integer arithmetic only. Marker: `R705_TERMINAL_GATE_BRC_OBSERVER_LATTICE_EXACT_PASS`. Executable program and evidence JSON accompany this note.

This theorem is an observer and information-cost result for the static **candidate** Port field. Native X6 Link/Port occupancy realizability, V29 PASS/TRANSFER, V39 j-flow, typed TRIADIC_CLOSURE_E and full rotation-generator transport remain open. Next discrimination: pin actual native event contracts and find one reachable two-packet same-count witness for a legal future event, or recompute the reachable state quotient. In parallel construct a three-force single-Cell closure event with explicit provenance, preserving the frozen pin and formal Source ownership gates.