# X6 native-time cut observers: exact finite cut-lattice law and C12 winding-fiber obstruction

Date: 2026-11-12. Researcher: EM-DIRECT-403AAA. Session: MCP-a88064f3bd7a47c8a315fa4baffeef4e. Activity: RA-3CCFD886BD2BFF49E8A49CB9. Task: RS-X6-NATIVE-TIME-DYNAMICS, immutable publication TP2-91D4A7C2F63805BE21A3. Source authority/CLAIM: separate from this author-side GitHub note. Status: new scoped exact theorem + finite checks; neither a native Cell-to-Cell coupling permission nor independent mathematical acceptance.
Frozen task science pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Applicable currently read norms are not scientific input repins.

## Prior results consumed, not reproved

* P000 TIME_ROLE=TRACE_AND_ORDER_OF_RELATIONAL_CHANGE, X6 native six-dimensional spatial Cell and distinct time.
* Frozen research_notes/VIETE_PHASE_REFINEMENT_VS_PRECISION_PROSTATE_CLOCK_20260905.md and research_notes/VIETE_NATIVE_HALF_TURN_PRINCIPAL_ROOT_BUNDLE_20260905.md: physical C6/C12 event refinement differs from the precision pro-state/root lineage.
* research_notes/X6_NATIVE_EVENT_TIME_AND_MARKOV_MEMORY_V1_20260906.md: local triadic C12 and arbitrary-path history memory, original authorship retained.
* research_notes/X6_NATIVE_EVENT_TRACE_PARTIAL_ORDER_V2_20260906.md: endpoint-safe trace monoid for independently certified events; arbitrary linear extension is an additional serialization observer.
* research_notes/X6_NATIVE_TIME_DURATION_CRITICAL_PATH_V3_20260906.md: conditional calibrated duration is critical-path max-plus, not raw event count.
* research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md, corrected V1R: at a single Cell each declared internal (signed ordered frame F, SHELL/CLOSURE mode) has exact period twelve with T(F,SHELL)=(F,CLOSURE), T(F,CLOSURE)=(R_can(F),SHELL). The mode label is not independently a TRIADIC_CLOSURE_E truth certificate.
* research_notes/driver/2026-11-12_x6_time_ordered_signed_rotation_depth_observability.md is separate unreviewed Driver-algebra evidence. It is neither replayed nor used to infer an admitted physical event.

## Domain and hypothesis: finite independent product, not a granted multi-Cell law

Take m distinguishable Cell-indexed local V1R internal subsystems with initial decorated states s_i and chosen nonnegative finite local event horizons ell_i. Each subsystem has the V1R deterministic local update T_i. Form the **conditional product model**: every component's events are a chain; different components are declared independent only for the endpoint/commuting-update future language and only if their complete typed resource supports, channel/force/path references and updates are in fact certified nonconflicting. Distinct spatial Cells *alone* are insufficient for that permission. Existence of a physical multi-Cell event protocol is NOT assumed proved.

A serial word consists of exactly ell_i occurrences of event i, preserving internal order. Its dependency poset is the disjoint union of m chains. The corresponding trace class forgets the arbitrary interleaving when endpoint-safe independence is certified. The cut after k serialized relation events is an **order ideal** of that poset, encoded by a=(a_1,...,a_m), 0<=a_i<=ell_i and sum a_i=k. A new readout that asks "what state after the kth global serialized event?" is itself serialization-sensitive and therefore is NOT an observer for which the same trace quotient is necessarily safe. A valid readout must retain the chosen ideal (or the full set of ideals at that k).

## Theorem 1: exact cut-state polynomial and minimal state-label budget

Under the above conditional product model, the set I_k of k-event prefix ideals has cardinality

    |I_k| = [x^k] PRODUCT_(i=1)^m (1+x+...+x^{ell_i}).

Every vector a with these bounds/sum yields one ideal, and it is realizable as a prefix of some linear extension: execute a_i events of each local chain before all remaining events. Therefore the coefficient is exact, not a loose upper bound.

If ell_i <=11 for every i, the V1R local orbit does not repeat over 0<=a_i<=ell_i (its exact period is 12). The full decorated state F(a)=(T_1^{a_1}s_1,...,T_m^{a_m}s_m) is then injective on I_k. Thus there are exactly |I_k| physically *model-legal* conditional-product k-cut decorated states, even though the whole trace has one endpoint. An exact predictor with total k and fixed inputs but without an observed k-cut requires |I_k| distinct labels, or ceil(log_2 |I_k|) fixed-length bits, to identify which cut occurred.

The count is observer-specific: the coarser mode-parity observer can identify fewer states. In particular, |I_k| need not equal the number of parity patterns.

**Proof.** Selecting prefixes of each chain gives the Cartesian product of integer intervals. A k-ideal satisfies the sum constraint; multiplication of the geometric polynomials counts the exact integer solutions. Since each local T_i has exact period 12, a_i->T_i^{a_i}s_i is injective on [0,11]. Cartesian product injectivity proves the state count. Exact distinguishability implies a cardinality/bit information lower bound; coding each ideal index attains it. All serial words execute the same total number ell_i on each independent component, so endpoint states agree (componentwise commutation). QED.

## Corollary: six simultaneous one-event Cells

For m=6 and ell_i=1, there are 6!=720 labeled serializations of six local events but only 2^6=64 distinct ideals. The counts at global k=0,...,6 are 1,6,15,20,15,6,1. A k=3 timestamp has 20 possible full decorated states, requiring five selector bits if the serialization choice must be recovered. Their common final endpoint is unique.

This cleanly separates three levels: BRC serial-word multiplicity 720; dependency trace (one class for the six antichain events under its ENDPOINT future lease); and choice of intermediate ideal (20 at cut k=3). None is physical elapsed duration.

## Theorem 2: periodic local C12 phases plus global count lose per-Cell winding

Take m>=2 local deterministic C12 components with ell_i>=12. Consider total global count k=12 and the m possible ideals a^(i) having a_i=12, all other coordinates zero. All m have the SAME full local decorated V1R state tuple (every 12-step local orbit returns to its initial state) and same total k, yet are distinct order ideals/per-Cell source histories. Hence the observer (k, local full decorated V1R phases) has a fiber of at least m and cannot answer exact per-Cell event-count queries. Distinguishing these m alternatives requires at least ceil(log_2 m) bits of winding/source allocation memory in this population.

For equal horizons ell_i=12, there are binomial(m+11,11) k=12 ideals. Exactly m of those have all local phases equal to their starting phases and collapse to one; every other ideal has all a_i in 0..11 and gives a different phase tuple. Consequently there are exactly

    binomial(m+11,11) - (m-1)

distinct full decorated phase vectors at global k=12. In particular, m=2 has 13 ideals and only 12 phase vectors: (0,12) and (12,0) are the exact collision.

**Proof.** Local period 12 gives T_i^12(s_i)=s_i and exact periodicity. Any a_i in 0..12 congruent to zero modulo12 is 0 or12; with sum12 the only phase-zero progress vectors are the m allocations. For every other vector, entries all <=11 and the vector is uniquely recoverable from its component phase. Stars-and-bars counts all nonnegative m-tuples summing to12; the ell_i=12 upper bounds hold automatically. QED.

This is an authentic pair of legal states in the declared V1R *product model*, not a fabricated true/false label for TRIADIC_CLOSURE_E; the stronger assertion of physically admitted multi-Cell coupling is NOT made.

## Exact checks and results

Companion checker: research_notes/portable_direct/x6_time_cut_lattice_verify_20261112_r2.py. Run: `python3 x6_time_cut_lattice_verify_20261112_r2.py`. Output: research_notes/portable_direct/x6_time_cut_lattice_results_20261112_r2.json.

- ell=[1,1,1,1,1,1]: 720 enumerated serializations; cut counts [1,6,15,20,15,6,1]; one endpoint; 5-bit peak.
- ell=[2,3,4]: 1260 serializations; cut counts [1,3,6,9,11,11,9,6,3,1]; 11-state peak/4 bits; mode-parity cut counts [1,3,4,4,4,4,4,4,3,1].
- ell=[3,3,3]: 1680 serializations; cut counts [1,3,6,10,12,12,10,6,3,1]; 12-state peak/4 bits.
- ell=[12,12], k=12: 13 distinct ideals; 12 full V1R phase tuples; exact collision (0,12) versus (12,0).

All finite assertions tested in checker using exact Python integer/tuple arithmetic and full serial-word enumeration in the three bounded cases. The statements for arbitrary m/ell follow from the displayed mathematical proof; finite tests are not claimed as a universal computer proof.

## What this adds to the native-time mother objective

A trace of endpoint-safe independent events is **not** enough to assign a unique decorated state to an arbitrary globally serialized timestamp k. The order-ideal is the precise missing datum; storing all possible k-cut states is another safe observer. When local internal cycles repeat, even a chosen global k plus all current local phases loses which Cell completed whole cycles. This is separate from the previously known single-cell C12 periodic-history obstruction and sharpens it to a multi-Cell, fixed-total-event-count, exact source-allocation residual.

The native P000 time object remains an order/dependency structure, not a 7th spatial coordinate. Precision/root lineage is separate. Physical duration calibration remains open.

## Next discriminating unit

Obtain actual native Cell/Link/Port/force-resource certificates admitting cross-Cell independent V1R events and evaluate whether the desired future observer includes globally kth-cut queries; if so, either retain the selected ideal/serialization or use a trace-safe set-valued k-cut operator. For interacting Cells find an explicit collision or valid coupling where the dependency poset is not a disjoint union and test the same counting using its order-ideal polynomial (the generating sum over all ideals), without inventing event permission. Investigate how calibrated critical-path duration acts on the resulting ideal lattice.

No P000/Foundation change, no formal review or external physical calibration claimed.
