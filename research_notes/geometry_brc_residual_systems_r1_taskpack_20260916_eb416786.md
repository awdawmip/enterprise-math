# Geometry–BRC Residual Systems v0.1 — R1 program and taskbook handoff

Progress-Event-ID: `GBRC-R1-PROGRAM-TASKPACK-20260916-EB416786`
Research-Activity-ID: `RA-geometry-brc-residual-20260916-eb416786`
Researcher-ID: `EM-DIRECT-EB416786`
Date: `2026-09-16`
Status: `RESEARCH_PROGRAM_DEFINED / NON_EXECUTABLE_TASKBOOK_DRAFTS`
Publication gate: `NEW_PARENT_OBJECTIVE_DRIVER_AUTHORIZATION_PENDING`
Source snapshot: `12cb71806b655935d1c51861fa35d13a01c8ed2e`

User direction: “嗯，建立这套体系，并且发布第一轮的任务书到状态机”.

This source checkpoint establishes the program definition, six bounded first-round taskbooks, dependencies, deliverables and takeover frontier. It is NOT an immutable task publication, CLAIM, accepted theorem, Foundation change, second registry or background worker. The current conversation remains RESEARCHER. No Driver authority is inferred from task importance or another conversation.

## Program and exact first-round scope

Mother question: for a declared geometric operation language, observations and branch semantics, which fine distinctions omitted by a coarse observation must remain as residual memory; how are they transported and composed; when may they be collapsed safely; and when can a positive envelope control their accumulated effect?

Accumulation means composition, not monotone growth. Distinguish retained hidden information, local model defect, transported accumulated defect and future observable difference. An observation fiber is initially a set, not a vector space.

An instance declares `(X,G,q,A,F,O,W,R,encode,H)`: fine states; geometric ports/charts; coarse observation; typed operation alphabet; partial transitions and enabledness; actual readouts; weight type; residual carriers; encoding; and permitted future language/horizon. Separate the set/partial-operation layer, geometric transport layer, positive branch layer and normed/ordered envelope layer.

In the restricted abelian-fiber affine interface, an edge has `r' = T r + d`. First A then B gives `(T_B T_A,T_B d_A+d_B)`. Iterating gives the transported accumulation sum, with earlier defects transported into the later fiber before addition. This is ordinary affine composition, not a new general algebraic theorem. Any state-dependent transport, defect, weight or enabledness must appear in the state.

BRC alternatives preserve the declared branch identities, multiplicities and positive rational weights. CWM alternatives add C and W and take max M. Fully compatible independent serial choices multiply C/W/M; dependent branch choices must retain and sum over their actual compatibility relation. Equal affine labels do not license forgetting a provenance readout. Positive weights cannot average a torsion residual without a separately defined readout, and positive CWM is not signed/complex cancellation.

Safe compression is relative to the complete future language, including partial-operation enabledness. Reuse P023 and the existing partial-operation quotient engine. A one-step repair is `(q,h)`; persistent memory requires future closure. Measure minimal residual alphabet relative to the refinement inside each q-fiber, stating whether the cost is worst-case alphabet, state-dependent code or bit length. Full terminal CWM equivalence and stepwise state congruence are different interfaces; do not identify them without proof.

Reference shifts `r'_v=r_v-a_v` give `d'_e=d_e+T_e a_v-a_w`. All offsets can be removed exactly when the simultaneous equations `a_w=T_e a_v+d_e` have a common solution. Loops imply `(I-T_gamma)a_v=d_gamma`. Identity transport plus nonzero loop defect obstructs removal; nonidentity transport plus nonzero defect alone does not. Separate local fixed points from one common section; loop sufficiency requires explicit connectivity/invertibility assumptions.

For a proved finite nonnegative rational envelope `E_(n+1)<=B E_n+d_n`, a positive rational certificate `Bh<=lambda h`, `lambda<1`, and `0<=d_n<=epsilon h` gives the weighted maximum norm bound `lambda^n ||E_0||_h + epsilon(1-lambda^n)/(1-lambda)`. First prove that this envelope actually bounds the chosen residual readout. Two loops of gain 3/5 have decaying individual path gain and growing depth-total gain; this is not probability normalization or proof of signed-state divergence. The family `B_k=[1-1/k]`, k>=2, is individually stable but its unit-injection equilibrium is k; uniform scale control needs uniform constants, compatible maps and norm comparisons.

### Frozen tetrahedral regression input

Vertices A,B,C,D; edges AB,AC,AD,BC,BD,CD. `V0={v in Z^4:sum v=0}`, `E0={x in Z^6:sum x=0}`, `delta(v)_ij=v_i+v_j`, `R=E0/delta(V0)`.

Matching sums are `(x_AB+x_CD,x_AC+x_BD,x_AD+x_BC)` and star parity is `e=x_AB+x_AC+x_AD mod 2`. Normal representative `N(p,q,e)=(e,0,0,-p-q,q,p-e)`. The existing research baseline is `R ~= A2(Z) + Z/2` as abelian groups, not an equivariant product.

The mod-two state space is `F2^3`, with
`s1(p,q,e)=(p,p+q,e+p)`,
`s2(p,q,e)=(q,p,e)`,
`s3(p,q,e)=(p,p+q,e)`.

Matching-only observations remain permutation-compatible. Star-parity readout requires the extra bit. Starting from e alone with all three generators, the horizon 0/1/2 class counts 2/4/8 are existing results to replay, not new discoveries. Integral-lift legality belongs to the integral model: it requires integer matching sums zero and parity zero; mod-two p=q=0 does not imply integer matching sums zero.

The tetrahedral six edge coordinates are not P000 native spatial coordinates. E0 has rank five and the residual free rank is two. P000 stays fixed. An actual native comparison map, rather than identification by coordinate count, is a separate R1 task. No continuum, force, entropy or physical energy law is inferred.

## Task envelope and dependency semantics

Proposed parent objective ID: `OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS`.
Operational generation: `null / NOT CREATED`.

All six taskbooks have `kind=RESEARCH`, `owner=taskbook/unassigned`, `base_state=DRAFT`, `priority=P2`, `leverage=MEDIUM`, `created_by_role=RESEARCHER`, `task_authority=PENDING_PUBLICATION`, `publication_contract=RESEARCH_TASK_PUBLICATION_V1`, `publication_template=RESEARCH_TASK_PUBLICATION_TEMPLATE_V1`, `identity_policy=AUTO_RESOLVE_OR_ALLOCATE`, `final_response_identity_policy=INHERIT_GLOBAL`, `identity_lane=GBRC-R1`, `origin_kind=DIRECT_USER_DIRECTION`, and no fixed researcher_id/driver_id/execution_id. Registry key equals the reserved task ID. Policy review is pending, not PASS. Parent objective generation must be filled from an authorized operational head before publication.

R1-01 through R1-05 are simultaneous first-wave `NEW_DIRECTION` work packages, not successors justified by an earlier task PASS. R1-06 is `INTEGRATION`. There is no formal predecessor task to relabel or supersede. Dependencies express required input artifacts, not a claim that upstream results exist.

DAG: `01 -> {02,03,05}; {01,02} -> 04; {01,02,03,04,05} -> 06`.
An upstream counterexample must change or stop downstream assumptions. A PASS label without exact evidence does not satisfy a dependency.

## R1-01 — RS-GBRC-R1-TYPED-CARRIER

### Mother question
How can fine state, observation fiber, residual type, partial operation and positive branch metadata form one checkable instance interface, with a faithful tetrahedral baseline?

### Frozen inputs and scope
Use the instance declarations and tetrahedral definitions above, the source proposal, P023 and the September 11 manuscript. Freeze vertex/edge order and action convention. Keep the integral carrier and F2^3 separate. No upstream research task is required.

### Hard target and required outputs
Deliver `instance_schema.json` specifying X/G/q/A/F/O/W/R/encode/H, sources/targets, enabledness and evidence types; `tetrahedron_fixture.json` with eight states, generator actions and matching/e/all-star observations plus symbolic integral definitions; `carrier_bridge.md` listing additional assumptions for each stronger interface; and exact type/negative-input tests with commands and results.

Frontier: the proposal has formulas but no common frozen instance schema or consumable data. First action: declare the schema and generate the minimal fixture from the displayed definitions.

### Research value to preserve
Prevent silent changes between integer, torsion, path and normed residuals. Give all subsequent tasks the same input rather than independent private models.

### Success, kill, and return criteria
Success requires reproducible reconstruction of the same instance and rejection of intended type errors, including mod-two/integer legality confusion. Separate replay from new targets. If a baseline fails, freeze the smallest conflicting input and suspend dependent claims. Return exact inputs, covered scope and smallest unresolved unit.

## R1-02 — RS-GBRC-R1-TRANSPORT-COMPOSITION

### Mother question
Which geometric process labels make path and branch composition closed, and which defects can be removed by a coherent reference section?

### Frozen inputs and scope
Depends on R1-01. Restrict to its declared abelian fibers, homomorphisms and positive branch metadata. General native geometry is not assumed affine. Use the affine and reference-shift identities above as existing algebraic inputs.

### Hard target and required outputs
Deliver `transport_contract.json` with ports, T/d, compatibility and observations; `composition_proof.md` with path expansion and compatible branch composition; `gauge_section.md` with the simultaneous-equation criterion and carefully scoped loop sufficiency or counterexample; and `exact_witnesses.json` for order dependence, incompatible ports, nonremovable identity-transport loop defect, removable nonidentity-loop defect, and incompatible local fixed points.

Frontier: the abstract composition identity is known; the typed geometric/branch interface and global section criterion are not frozen. First action: instantiate two composable edges and locate minimal order-sensitive and incompatible-port examples.

### Research value to preserve
Make transport-before-accumulation executable and distinguish coordinate artifacts from structural obstructions.

### Success, kill, and return criteria
Proofs and exact examples must agree. General affine associativity is not a novelty claim. If finite labels lose the declared future readout, produce a separating context and minimal repair; retaining complete history is not a proof of finite closure. Return both positive and negative scope.

## R1-03 — RS-GBRC-R1-OBSERVER-MEMORY

### Mother question
What is the minimal sufficient residual for the chosen complete future language, and when is terminal CWM behavior too weak to support stepwise geometry/legality observations?

### Frozen inputs and scope
Depends on R1-01. Compare matching-only, e-plus-generators, and an explicitly richer enabledness/port/provenance language. Integral lift predicates remain in the integral model. Distinguish terminal weighted behavior from operation congruence.

### Hard target and required outputs
Deliver `observer_contracts.json`; `minimal_memory.md` with lower-bound distinguishability and sufficiency proofs, including replay of the old 2/4/8 and one-bit baselines; `separation_certificates.json` with state pairs, shortest distinguishing words and differing outputs or legality; and `weighted_vs_contextual.md` proving the precise weighted simplification or giving a counterexample and repair.

Frontier: P023 and existing partial-operation tools cover the general mechanism; the chosen geometry/positive-weight joint boundary remains to earn. First action: check and reuse current `src/enterprise_math/partial_operation_quotient.py` and `composition_safe_collapse.py`, not a second generic refinement engine.

### Research value to preserve
Explain which detail is necessary, which may be discarded, and how memory cost depends on the observer.

### Success, kill, and return criteria
Minimality needs a lower bound and a sufficient encoding. Finite exhaustiveness certifies only the finite instance; integral claims require separate reasoning. If only old one-bit/2/4/8 results are reproduced, return `REPLAY_ONLY`, not a new theorem. Return every unsafe quotient with an explicit witness.

## R1-04 — RS-GBRC-R1-POSITIVE-STABILITY

### Mother question
Can an authentic finite positive residual envelope be derived from geometric transports and branch weights, rather than postulating a favorable contraction matrix?

### Frozen inputs and scope
Depends on R1-01 and R1-02. B is finite nonnegative rational; declare whether weights are probabilities, counts or gains. A torsion state is not forced into a real error norm. Positive-envelope divergence does not certify signed/vector divergence.

### Hard target and required outputs
Deliver `envelope_derivation.md` proving the componentwise domination of the chosen readout; `stability_certificate.json` containing exact h, lambda, injection and norm data plus existing checker version/results; `negative_controls.json` with the two 3/5 loops, B_k=[1-1/k], missing source-bound and norm-comparison failures; and `scope_of_bounds.md` separating finite paths, finite recurrence and uniform scale statements.

Frontier: the existing Bh<h theorem is available; deriving the correct B and its relation to residuals is unfinished. First action: inspect and reuse `src/enterprise_math/brc_weighted_recurrent.py` and the finite recurrent foundation, then derive B from R1-02.

### Research value to preserve
Control branching growth and individual contraction together, with stated constants and clear limits.

### Success, kill, and return criteria
Prove domination before supplying a certificate. No undeclared normalization or deletion of branches to force contraction. If B or the certificate cannot be obtained, report the exact missing assumption or failed criterion. Do not call non-certification a proved dynamical divergence.

## R1-05 — RS-GBRC-R1-NATIVE-GEOMETRY-BRIDGE

### Mother question
Does the finite residual core admit a nontrivial, source-backed native geometry comparison, rather than identifying tetrahedral coordinates with P000 by analogy?

### Frozen inputs and scope
Depends on R1-01. P000 is fixed, not a falsification target. A three-axis slice stays a slice; ordinary vector-space/metric assumptions cannot be inserted into native premises merely to obtain the desired result.

### Hard target and required outputs
Deliver `native_instance_sources.json` naming a minimal existing native finite-observation instance and exact definitions; `comparison_diagram.md` with state/operation/observation maps, commutation proofs and information loss if constructed; `native_obstruction.md` with a genuine obstruction or explicitly weaker missing-map diagnosis; and `contribution_boundary.json` typing native, external, conditional and unestablished statements.

Frontier: the external graph-lattice baseline exists, but this program has no validated native comparison map. First action: read P000 and `native_semantics_admissibility.json`, select the smallest source-defined native instance, and freeze it before comparing.

### Research value to preserve
Determine whether the system has reached native geometry or remains a useful external finite-method integration.

### Success, kill, and return criteria
A nontrivial verified map or precisely scoped negative/undecided report is a valid output, but they are not interchangeable. If the comparison needs rewriting native definitions, stop that route and state the extra assumptions. Preserve the external core; do not interpret comparison failure as refuting P000.

## R1-06 — RS-GBRC-R1-INTEGRATION-FALSIFICATION

### Mother question
Do all first-round interfaces agree on types, observers and evidence strength, and what actual new contribution or exact negative result remains after integration?

### Frozen inputs and scope
Depends on all five prior work packages. Consume exact upstream evidence, not hidden chat summaries. Author self-check and independent review must be separately identified. No upstream result exists merely because this taskbook exists.

### Hard target and required outputs
Deliver `R1_CORE_REPORT.md`; `claim_evidence_matrix.json` with assumptions, sources, proof/finite-check/unresolved status and dependencies; `regression_report.json` covering valid inputs, illegal types, unsafe quotients, order errors, chart/reference defects, branch gains and nonuniform scale examples; and `HANDOFF.md` with completed work, smallest open unit, reusable code and stopped routes.

Frontier: none of the six research tasks has been executed in this publication-preparation turn. First action after upstream artifacts exist: build the claim/evidence matrix and stop on missing or contradictory evidence.

### Research value to preserve
Make the system reproducible, transferable and falsifiable rather than dependent on its originating conversation.

### Success, kill, and return criteria
Require consistent types and observers, no dangling evidence, and a candid conclusion: new scoped result, conditional kernel, integration/replay only, or exact local no-go. If there is no new theorem, return `INTEGRATION_ONLY_NO_NEW_THEOREM`. No automatic second round is triggered by task PASS.

## Sources and reuse map

All following EM paths were read at `12cb71806b655935d1c51861fa35d13a01c8ed2e` unless stated otherwise:

- `research_notes/geometry_brc_residual_systems_20260916_eb416786.md`, blob `6048ea5fefbf4d5c0e1d3795f196e5da8006b58c`: earlier proposal and conditional elementary derivations, not an accepted new foundation.
- `docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md`, blob `0576256c244b158292f6f02eb5532c5dbdcceb30`: `REUSE_APPLIED` to the observer/repair contracts. Execution is assigned to R1-03 and is not asserted here.
- `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`, blob `fbe1fb4ebae63ecea206a2ab62f27918039cdcf3`: `REUSE_APPLIED` for CWM typing and terminal behavior; `COMPOSE_APPLIED` as a task-level design with geometry labels. No BRC software run is asserted.
- User File Library `Enterprise_Math_Research_Note_English.pdf`, file id `file_000000000ae881fa96ac5cb152cdff48`, September 11 revision, sections 2/5/7/11: directly read mathematical baseline. This checkpoint stores a restatement of definitions/results, not the full PDF or a fabricated PDF hash. Historical Lean checkpoint `95a9cd418f6abdb4916f5cf8182437af61dba9db` was not rerun.
- Global P000 router at `awdawmip/chatgpt-global-knowledge@4f0c85763fcac42c1da7a9d4bced3f4411a96fac:projects/enterprise-math/P000_REALITY_FOUNDATION.json`: protected premise; no changes.

## Publication gate and current takeover frontier

The current task publication protocol requires an exact taskbook plus matching immutable record and equivalent preflight. The Objective contract additionally requires new tasks to pin the operational OPEN objective generation. Creating/selecting a new objective is restricted to RESEARCH_DRIVER; `research_role_policy.json#/driver_activation` requires explicit activation in the current conversation. Publishing tasks as a researcher does not itself grant that authority.

Sources: `research_taskbook_contract.json` blob `8bf4183eb46c18ba4e2aef913b7b0f57e6bb490d`; `research_objective_contract.json` blob `8ea2ddf9c7592eace7ff01f41bb305b66470731f`; `research_role_policy.json` blob `e3800cc592f2edeb0315788ff4662ab7756d7ac8`; `research_driver_authority_contract.json` blob `114c7d3611ecfdc88513f6c475116655866dc760`; `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md` blob `819b4d54038bd943c998f3de0861c9f729bd1457`.

No suitable current OPEN parent for this new program was verified. The decorated-carrier objective is CLOSED; the external-geometry objective is OPEN but covers six different geometric transfer routes. Neither is silently reused or reopened. No reserved RS-GBRC task directory was found in the observed task-record tree.

Completed locally: a Chinese program document, six draft taskbooks with the mandatory five content sections, source map, machine-readable round manifest and draft lint. The six IDs are unique and the dependency DAG is acyclic. Draft metadata remains DRAFT/PENDING_PUBLICATION with no fixed execution identity.

Not completed: canonical publication preflight, formal parent objective/selection receipt, immutable task publication records, mathematical execution, formal proof-checker run or independent review. Draft lint PASS must not be represented as a canonical publication or theorem PASS.

Smallest next action: obtain explicit scoped Driver activation for this program and R1 publication; authenticate that authority under current source rules; create/select the OPEN parent with immutable receipt; fill the exact generation into each taskbook; run current policy/publication audits; atomically publish the taskbooks and matching V2 records; verify immutable readbacks. Do not invent a CLAIM or background worker.

This source checkpoint plus the explicit inputs and six complete task-specific envelopes above is sufficient to resume authoring without the prior conversation. The user-facing local package additionally contains structured draft files and lint output; this note does not pretend those package-internal paths already exist as separate files on main.
