# Unit 1: a two-material Cell-port obstruction and a sharp relaxed turning budget

Progress-Event-ID: EM-20261006-CELL-CLOSURE-U1-PORT-BUDGET-6C4E2A
Status: CONDITIONAL_MODEL_THEOREM / EXECUTED_TYPED_BRC / NOT_A_NATIVE_MATERIAL_HEARTBEAT
Global read snapshot: awdawmip/chatgpt-global-knowledge@bf61ba2736c51dcc9cf9fb72c70a3325bd00a293.
Science source snapshot: awdawmip/enterprise-math@ff90471f4245464de9d132114e135ca235c5a63b.
Logical conversation: chatgpt-heartbeat-cell-attraction-20261006-8b74f0 (not platform-attested).
Own current activity: RA-2A6D0E1D2A490B92D88DE177; Researcher EM-DIRECT-AD9421; public session MCP-1f3fbae41ef5462bbe0cbfb00fc10aa9.
Registration observed at e2a23a181c79ddcb8782a6caa5e591640cd836d6, research_activity_records/RA-2A6D0E1D2A490B92D88DE177.json, blob4029beab23e02c48030f8dbbefb7db743e830cc4. Registration is not a CLAIM or mathematical admission.

## 1. Scope, input, and the new question

The user authorized starting the published Cell-closure roadmap. This unit tests the simplest *direct, no-redirection lift* of the previous positive response model into equal-quantum, distinct-axis three-port packets. It does NOT assume that scalar response weights already are physical forces. It does not rule out unequal triads, material scattering, internal memory, extra boundary channels, or dynamical/accelerating heartbeats. P000 is unchanged.

Use X6 with all six native axes and twelve signed nearest-neighbor steps. Two labelled unit materials coexist at z_A=c and z_B=c+e1. These positions specify this diagnostic preparation, not a solved final position. The choice of e1 is a source preparation, not a reduction of the underlying space. Raw coordinates are not final public Cell addresses.

Retain the earlier CANDIDATE scalar response law chi=mu+lambda*A_X*chi, decaying at infinity, 0<lambda<1/12. Let G(x) sum all ordered path weights lambda^length from the reference Cell to x. Loops and backtracking are included. The input law is a new-model baseline, not a settled native attraction or material constitutive law.

At material A retain the full positive *arrival* response at each signed port:

    I[j,s] = lambda*( G(s*e_j) + G(s*e_j-e1) ), s in {+1,-1}.

The first term is A's own return response; the second is B's response. They are separately source-tagged before aggregation. The final lambda is a real return/probe edge. In contrast to a signed net-drive readout, SELF RETURN IS NOT ERASED. The local seed mu(A)=1 is retained as a source, not silently promoted to an additional directional force.

All quantities below are response-budget readouts, not calibrated mass, energy, probability, or displacement. Relation depth is not physical time.

## 2. Interface contract being tested

The test interface has these explicit, LOWER-LEVEL candidate assumptions:

- Each response contribution carries source, target, signed arrival port, weight and ordered-path provenance.
- A canonical packet consumes an equal positive amount from each of three DISTINCT native axes. Actual signed triad incidence must still be supplied by a native material model.
- Under the direct-lift test, contributions may be grouped but not turned to another axis, duplicated, or supplied from an unrecorded source.
- For a necessary test, relax atomic indivisibility and allow every unsigned three-subset of the six axes. Impossibility in this larger class also excludes its more restrictive direct-lift subclasses. Feasibility in the relaxation DOES NOT prove native feasibility.
- Count/total/dominant CWM values are not three independent forces, and alternative BRC branches are not automatically simultaneous material alternatives. A three-port packet is a JOINT tuple with its supply labels retained.

P000 fixes minimal stable arity and canonical equal-quantum closure, not this direct conversion from scalar field arrival to force. An obstruction here rejects this conversion candidate, NOT P000 and NOT the existence of a full two-material heartbeat.

## 3. Necessary capacity inequality

Let m_j = I[j,+]+I[j,-], T=sum_j m_j. If all budget is covered by equal three-axis packets, then

    max_j m_j <= T/3.                              (1)

Indeed each packet consumes 3w total and at most w on any one axis. Summing over packets proves (1). This uses no Euclidean vector cancellation.

For the present pair, the declared graph symmetries give m=(a,b,b,b,b,b). Put B=5b. If a>B/2, the smallest uncovered TOTAL budget in the permissive fractional incidence model is

    D = a-B/2 > 0.                                (2)

Lower bound: each amount w used on axis1 needs 2w from the transverse supply, so axis1 usage is at most B/2. Sharpness: give each of the ten triples (1,j,k), 2<=j<k<=6, weight b/4. Each transverse axis appears four times, using exactly b; axis1 uses 10b/4=B/2. The leftover is exactly D. This is a budget feasibility certificate, not a full-state quotient or native stability assertion.

## 4. Exact all-depth expressions including self response

Set C=G(e1),

    a0=lambda*(G(0)+G(2e1)),
    b0=2*lambda*G(e1+e2).

Last-step decomposition gives C=a0+5b0. Since G(+/-e_j)=C,

    a=a0+2*lambda*C,
    b=b0+2*lambda*C,
    T=(1+12*lambda)*C,
    D=(a0-5*b0/2)-3*lambda*C.                     (3)

Thus dropping self terms would overstate this obstruction. The executed final certificate uses (3), not a cross-source-only approximation.

## 5. A uniform obstruction, not a tuned decimal

Let x=12*lambda. A B-to-A path has odd length. Its first n-1 steps determine the only possible final step, hence there are at most 12^(n-1) such paths. Separating the unique length-one path yields

    C=lambda+R,
    0<=R<=lambda*x^2/(1-x^2).

Also a0>=lambda and 5b0<=R. Therefore

    D >= lambda-R/2-3*lambda*(lambda+R).           (4)

For EVERY 0<lambda<=1/24, R<=lambda/3 and 3lambda<=1/8. Consequently

    D >= 2*lambda/3 > 0.                         (5)

For the inherited baseline lambda=1/48, R<=lambda/15 and (4) gives

    D >= 3/160 > 0.                              (6)

No claim covering 1/24<lambda<1/12 is made by (5). This is a static response-lift obstruction, not a prohibition on force-driven motion or nonzero-residual heartbeats.

## 6. Sharp minimum budget that must change axis

Now allow a conservative reassignment of arrival budget between axes, while retaining total T. To admit a full cover, the repaired axis1 budget must be at most T/3. Thus the amount moved to another axis is at least

    tau = a-T/3 = (2a-5b)/3 = 2D/3.              (7)

The bound is sharp in the permissive fractional model: move exactly tau from axis1, equally to the other five axes. The new vector is

    (T/3, 2T/15, 2T/15, 2T/15, 2T/15, 2T/15).

Ten triples (1,j,k), each of weight T/30, cover it exactly. All legs are positive and every response budget is accounted for. This construction preserves total response only; it need not preserve path count, histograms, source-port correlations, native incidence or a material update law. The BRC implementation retains the changed carrier statistics rather than declaring them equivalent.

This gives a target for a future material scattering law, NOT authorization to choose an ad hoc isotropizer and call the system physically solved. Actual unsigned/signed incidence, finite quanta, internal state, source dependence and feedback can impose stronger costs or rule it out.

At lambda=1/48, C<=16lambda/15 implies a0/C>=15/16. Then

    tau/T = (a0/C+2lambda)/(1+12lambda)-1/3 >= 9/20.

As lambda tends to zero through this model, a0/C tends to1 and tau/T tends to2/3. The absolute response vanishes, but the relative directional mismatch does not. This is a formal consequence of the weighted-path model, not an assertion about real weak forces.

## 7. Executed BRC certificate

The unchanged src/enterprise_math/brc_weighted.py has blob3f205696709e847909958a153f8fe10d3f6b70f0, SHA2564f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f, 9635 bytes. Its current blob was observed at the science pin. The local adapter removes only the two unused relative imports brc_logarithm and exact_arithmetic. All function/class ASTs remain unchanged; no LN, pi, trig or reference solver is executed.

BRC DAG states retain source/length/endpoint/port tags. Endpoints are a safe quotient only for the declared homogeneous history-blind path extension; full ordered paths are specified by the recurrence, not licensed for general history-dependent material operations. Opposite ports and source labels remain in evidence/ports_by_source_depth.json.

Cross-source arrivals include odd lengths1,3,5,7,9. Self-return paths include lengths2,4,6,8,10 by the exact signed-axis bijection for G(e1), followed by a BRC return edge. Cross-source axial and each transverse-axis counts are respectively

    length1: (1,0); length3: (13,4); length5: (460,240);
    length7: (24585,16440); length9: (1666476,1280160).

For all omitted cross-source paths the actually executed one-state BRC comparison with144 loops, each of weight lambda^2, gives

    E = lambda*(12lambda)^10/(1-(12lambda)^2) = 1/47185920.

The full self tail is coupled by (3), not independently forgotten. For finite-prefix Dhat and tauhat,

    D in [Dhat-(1/2+3lambda)E, Dhat+(1-3lambda)E],
    tau in [tauhat-(1/3+2lambda)E, tauhat+(2/3-2lambda)E].

Executed full-field intervals at lambda=1/48:

    19576426714339/1001929970810880 <= D <= 3915291712967/200385994162176,
    19576426714339/1502894956216320 <= tau <= 3915291712967/300578991243264,
    19576426714339/39711089792070 <= tau/T <= 3915291712967/7942217958414.

Thus tau/T is between approximately0.492971278724 and0.492972080780. The exact fractions, not rounded display values, are the certificate. No omission tail is called structural residue.

Final run:151520 assertions; cwm_edge7, one_state_recurrent_cwm2, cwm_propagate286701, cwm_recoalesce337353. Checks include all endpoint CWM states through depth8, parity, source-reflection covariance, positive realization, separated self returns, last-step partitions, budget-cover certificates, and the information-loss witness below. The provisional cross-only development run was superseded by the self-inclusive run; they are not independent replication. No previous four-material proof is recounted as a new result.

## 8. A precise information-loss witness at the interface

Take six labelled contributions, each generated by a positive BRC edge of weight1/2. In state P, four use port+1 and two port-1. In state Q, two use+1 and one each uses+2,-2,+3,-3.

Both have exactly the same global CWM=(6,3,1/2) and signed drive readout (1,0,0,0,0,0). P has no three-distinct-axis packet. Q has a disjoint equal-weight packet cover:

    (token0,token2,token4), (token1,token3,token5).

Every token is used once. These are joint triples, not three alternative worlds. The same permitted packet-extraction observer distinguishes P from Q. Hence net drive AND global CWM together are insufficient for this declared future operation: signed port incidence is genuine extra interface state. Q's relaxed packet cover is not native stability, and neither P nor Q is asserted to be generated by the fixed two-source preparation above.

## 9. Outcome and next unfinished unit

This unit finishes an exact incompatibility test and quantifies the missing interface: passive propagation plus a direction-faithful equal-quantum direct lift cannot cover the two-material response in the certified parameter range, even with self loops retained. A permissive conservative turning repair exists with a proved sharp budget. Nothing here chooses a final material position, solves a complete heartbeat, classifies primes, modifies square-root arithmetic, or establishes physical parameters.

Next: build ONE source-resolved, signed-port material/Cell transfer relation with a tracked local internal state and actual native paths. Its third contribution must have a recorded source/return, its triple incidence must be independently declared, and any unmatched packet must be retained as changing state rather than cancelled. Test whether this same fixed law meets the necessary budget bound without imposing its desired final position. A convenient fractional cover is not that law. Keep occupancy/contact and boundary constraints explicit. Do not restart square shells or rerun the four-source positivity theorem.

## 10. Provenance and reproducibility

Prior frontier: research_notes/chatgpt_direct/20261006_8B74F0_CELL_ATTRACTION_221.md @ae0012234dfaf2045019fc2b45c04aecd5112318. Roadmap: research_notes/chatgpt_direct/20261006_CELL_CLOSURE_ROADMAP_4D93A7.md @ff90471f4245464de9d132114e135ca235c5a63b. Governing source definitions: P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md; HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.md; HEARTBEAT_WORLD_NATIVE_X6_TIME.md; RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json; docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md and research_constraints/heartbeat_brc_only.json.

The companion unit1_evidence.zip contains this note, the complete new checker, its pinned unchanged BRC dependency, detailed outputs and manifest. Run python check_unit.py after extracting it. This is same-author conditional research, not independent review or formal Task/Result admission. Scope/identity/persistence receipts are recorded separately from mathematical evidence.
