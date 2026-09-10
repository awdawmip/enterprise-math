# Native Coverage audit: three observers, asymmetric support, and resource-aware recall

Status: RESEARCH_NOTE / ISOLATED_PINNED_SOURCE_EXECUTION / NOT_PROMOTED
Progress-Event-ID: NOLLM-NATIVE-COVERAGE-AUDIT-20260910-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local continuity key, not an authenticated platform ID)
Mode: TASK_RESEARCH / direct user continuation / no formal Task-ID or CLAIM
Date: 2026-09-10
EM read snapshot: 902318ee8a5dd5065fa43710c3521898bec4120b
Nollm read snapshot: 91bd14ab394e87931b45baaaa87671f30fcfd706
Parent: research_notes/nollm_finite_carry_routing_20260910_c6c82.md at 6a771b279a255e7eb034529ef85e2f91d0fdd7c2
New experiment directory: experiments/nollm_native_coverage_audit_20260910_c6c82/

## 1. Exact question and recovered boundary

Consume the ten existing activity checkpoints. The next question is whether the preceding finite-state controller and external routing comparisons satisfy the ACTUAL Nollm propagation interface. This is not another prime-atlas expansion.

The answer requires separating geometry support, path counts, positive-weight sums, max-path scores, search budgets, and physical communication capacity. The code below investigates native sampled Coverage and the actual Recall selection loop, not an assumed stochastic decoder or an arbitrary permutation network disguised as Coverage.

All mathematical models here are ordinary rank-two lattice / algorithm comparison slices. P000, native direction semantics and Nollm runtime are not modified. No semantic corpus or real agent recall accuracy is measured. The original problem of intrinsic ordinary-number multiplication in a planar field remains open within this research project.

## 2. What the current Nollm source actually permits

The verified Nollm README is V3.14, evidence-first, geometry-native and single-entry. It explicitly excludes a second external graph/vector/semantic index as a required correctness path. Physical layers and disposable aggregation orders are different. Therefore the preceding binary tree and Benes networks remain COMPARISON MODELS, not architecture-authorized drop-in implementations. No new physical wire-length, queue-capacity or parallel-timing model was found in the inspected kernel/recall interface; prior switch-stage counts cannot be read as Nollm clock times.

The active geometry has beta=2^(1/4), adjacent orientation 22.5 degrees, increasing layer indices FINER. The active default supports chart_id=default, phase=null, layers -64..64 and a finite axial storage radius. These are software coordinate constraints, not a new all-integer physical embedding.

Important correction to the prior broad 'seven-branch' description:

- coverage_template.py retains DEFAULT_FANOUT_LIMIT=7 for compiled templates; lateral ring1 has six offsets.
- kernel_registry.py explicitly removes default-profile compiled up/down templates from the active set and calls expand_physical_coverage instead.
- physical_coverage.py aliases expand_approximate_coverage.
- approximate_coverage.py uses 96 deterministic microtriangle samples and permits up to EIGHT retained targets per directed expansion.
- BridgeSpec schema separately allows max_fanout 1..64. This is not a bandwidth guarantee or evidence that all those entries are legal semantic bridges.

Thus none of these numbers is a universal vertex degree or 'seven physical wires' contract. The inspected dynamic kernel uses fixed Q40 coefficients and Q16 output weights; exact integer evaluation of that code is not proof that its 96-sample geometric approximation is exact.

CURRENT_MAX_COVERAGE_DOWN_STEPS=2 belongs to the writable-field safety contract. It is not treated as a universal Recall depth limit. Our tests independently specify a +/-2 layer window, up to20 propagation steps, and explicit beams.

## 3. Execution boundary and source provenance

Four complete files were fetched at the immutable Nollm commit, saved without byte changes, and verified by Git blob SHA1:

- packages/nollm-core/src/nollm_core/approximate_coverage.py: b322638a0fe77e57ec84ac32cf817749a8b06582
- packages/nollm-core/src/nollm_core/coverage_contract.py: f08885e526248597edbd840b134bf7dbb26e1420
- packages/nollm-core/src/nollm_core/fixed_point.py: 9ea00e3c84a82f480c692a6ca0ca717a579dab60
- packages/nollm-core/src/nollm_core/recall.py: 02c148caad1929a0f72055100b75f806f55a956d

kernel_harness.py removes ONLY top-level relative imports from the parsed source and executes the unchanged function/class bodies with declared fixtures. The actual contract dataclasses/constants, Q16 normalization, coverage expansion and recall functions are used. GeometryAddress, atom/handle/trace and storage access are minimal fixtures, with valid default addresses. A synthetic marker is supplied at each visited location to expose traversal; this is NOT a populated persistent Nollm workspace, full Core test suite, Host/provider run, or semantic-retrieval benchmark.

The native geometric cases use coverage_up/down only, no lateral or persistent Bridges. A separate four-node case uses an explicit synthetic graph. A stronger hybrid case uses the real sampled Coverage plus TWO TEST Bridge anchors; those anchors are not evidence-backed production writes. No Nollm file is patched. A candidate filter-order diff is generated only inside the experiment outputs.

The published adapter can use bundled source_snapshots or NOLLM_CORE_SOURCE pointing to a local directory containing the four immutable source files. Missing source is an execution dependency, never silently reimplemented geometry. Source references are already durable in awdawmip/Nollm; the downloadable bundle also includes their exact bytes.

## 4. Up/down is not an inverse operation

At the origin, native up has only the origin of layer -1, weight65536. Native down has seven targets in layer+1: the center has72/96 hits and weight49152, while each surrounding cell has4/96 hits with deterministic Q16 rounding.

Enumerate exactly TWO kernel steps without Recall's previously-visited suppression:

order | path count | endpoint cells | paths returning to origin | sum of Q16 product weights at origin | best left-folded two-step Q16 score
DOWN then UP |25|13|7|201387/262144|49152
UP then DOWN |7|7|1|3/4|49152

Each diagnostic weight-product row sums to one over all endpoints. These are optional sum-product observers, not memory-confidence probabilities. The native Recall observer instead multiplies/floors along a path and takes a maximum when paths meet. It does not add all seven returning paths, and does not preserve a Hecke path-multiplicity measure. Q16 rounding is per step; no associative exact-real semiring identity is silently asserted.

IMPORTANT: Actual Recall retains the initial origin score65536. The displayed49152 is an EXACTLY-TWO-STEP observer, not the score which a full Recall result reports for its starting cell.

There is a simple scope-limited inverse obstruction. Distinct source cells (layer0,q0,r0) and (layer0,q1,r0) both assign positive up-weight to the same coarse cell, respectively65536 and4779. If P encodes an arbitrary source identity only as positive normalized mass and a nonnegative stochastic decoder R satisfies PR=I, then a shared positive intermediate output would require its decoder row to concentrate at each of two different identities, impossible. Thus such a scalar-mass-only encoding has no universal stochastic left inverse. This does NOT say Nollm deletes stored atoms, forbid signed reconstruction, or exclude retaining source labels/evidence. It identifies what the compressed observer alone cannot carry.

## 5. Native retained support is directed, even before beam pruning

Scan every layer0 source in the hex disk of radius18, and evaluate both directions. There are1027 source cells,2054 expansions and7946 positive directed target relations. For each relation, invoke the reverse kernel at the target WITHOUT clipping its output to the original disk.

Exactly66 relations have no directly reciprocal retained edge. The first such source radius is4. A compact witness is

S=(layer0,q=-4,r=2) --UP, hit1, Q16=683--> T=(layer-1,q=-2,r=0).

DOWN(T) retains (layer0):(-3,1),(-3,2),(-2,0),(-2,1), with weights36864,8875,5461,14336; S is absent.

This is an exact fact about the declared deterministic sample code. It does not prove that exact positive-area polygon overlap is asymmetric. Replacing an undirected physical-overlap assumption by this active directed retained-support relation matters before any search analysis.

Observed expansion histogram:
UP fanout1:25,2:30,3:678,4:294;
DOWN fanout3:36,4:558,5:342,6:36,7:55.
No eight-target example occurs in this disk; eight is the CODE LIMIT, not an observed frequency claim. Every sampled expansion passes hit-count96 and Q16-sum65536 checks.

## 6. Geometric support and actual search are different populations

From a single origin, only up/down, layers within +/-2, exact breadth-first SUPPORT traversal gives:

maxsteps | distinct accessible cells | cells on layer0
2 |41|13
4 |173|37
6 |329|67
8 |617|139
10 |1103|223
12 |1679|349
16 |3191|625
20 |5405|1039

Counts are reachable locations in an isolated coordinate experiment, not recalled real statements, path multiplicities or independent memory items. This support reference ignores scoring and beam, while retaining the exact active directed kernel.

At maxsteps8, actual Recall visits fewer locations:

beam | original loop | filter-before-slice research variant
1 |3|9
2 |12|17
4 |22|33
8 |46|65
16 |78|117
32 |131|187
64 |199|259
128 |309|397
512 |617|617
4096 |617|617

The original loop sorts candidates and slices to beam BEFORE discarding previously processed, dominated candidates. Those candidates can consume all available beam slots, after which the filter leaves an empty frontier. With beam1 it visits exactly the origins of layers0,-1,-2, then stops before maxsteps8 and returns budget_exhausted=False. Reachable live alternatives were discarded. Thus that false flag must not be treated as proof of a completely explored locality, much less global absence.

The research variant moves the slice after the existing filter. This changes no kernel or score recurrence and does not add an external index. It visits9 cells at beam1, matching the one-entry ceiling1+beam*maxsteps. A second variant records discarded live candidate occurrences and includes this in the loss/exhaustion flag. Its visits/scores match the filter-order-only variant. The ledger counts discarding EVENTS, not distinct permanently lost cells; a discarded state may be reached later.

At beam512 and4096, original and variant have identical result signatures and cover all617 locations within the declared eight-step support horizon. Their exhaustion flags remain true because further propagation beyond that horizon is possible; true does not mean a failure inside the horizon.

An additional36 combinations (four origins, three depths, three beams) check source support membership and the1+BH ceiling. In ten original cases the false exhaustion flag coexists with omitted reachable locations. The variant never visits fewer locations in this finite grid; no universal monotonic-improvement theorem is claimed. Total coverage-only Recall executions:102, including original and the two variants.

## 7. Beam order is not the only issue: a score is not a sufficient future state

The original best and merged dictionaries collapse paths primarily by cell and current score/path. They do not retain bridge-use as part of the dominance key even though future bridge traversal depends on it.

Four-node synthetic witness, maxsteps3, beam100, bridge budget1:

E --bridge(weight1)--> X;
E --down(weight1/2)--> A --up(weight1)--> X;
X --bridge(weight1)--> Y.

The score1 state at X has already used its only bridge. The score1/2 state still has its bridge available and can reach Y. Original Recall discards the latter and misses Y. Increasing beam does not help; the filter-order-only variant also misses Y. This is a missing resource coordinate, not a lack of geometric reachability.

Stronger hybrid witness: use ACTUAL sampled Coverage, E=(0,0,0), X=(0,1,0), Y=(0,100,0), where tuples are(layer,q,r), and add only the TEST Bridges E->X and X->Y, each unit weight and maxsteps1. With maxsteps3,beam4096,layerdelta2,bridgebudget1:

- original visits96 distinct cells and does not reach Y;
- exhaustive feasible path enumeration finds three paths to Y, with scores2730,824,1592;
- the best is UP,DOWN,BRIDGE, using its only bridge at the last step;
- a reference dynamic program keyed by exact(depth,cell,bridge_used) reaches Y at score2730;
- reference checks use528 path-state appearances and132 merged resource-state appearances, not that many independent memories.

The reference DP preserves reachability and maximum numerical score. It does NOT promise all provenance or a globally lexicographically smallest path when distinct pre-rounding scores later tie under Q16 flooring.

The sufficient dominance contract for numerical future scores must include the remaining operations/resources: greater score alone is insufficient if fewer actions remain legal. Monotonicity of floor(score*weight/65536) proves max-score pruning safe within an identical future-resource state for numerical outputs. Resource-constrained labelling is classical; the contribution here is the exact counterexample in this source loop and the bounded native-kernel hybrid reproduction, not a new general shortest-path theorem.

## 8. Implication for the original research direction

The earlier Hecke/radix field is an arithmetic carrier with exact quotient identities. The inspected default Coverage is a sampled directed encounter relation. Recall is a budgeted max-path traversal over it, not a permutation router or conservative message sum. These are distinct interfaces.

Do not insert an external relation graph / Benes fabric as a production correctness layer without explicit architecture authority. A stable arithmetic identity and a finite carry converter may remain useful research tools, but a proposed placement must be evaluated through the native single-entry visibility and budget semantics. Occupancy uniformity alone says little about which identity can actually be encountered.

This turn separates at least five losses: geometric sampling/reverse-support loss; beam truncation; dominance erasing remaining resources; max-path observation erasing multiplicity; and deliberate state/identity compression. None establishes loss of original persisted evidence by itself.

REUSE_EXECUTED: four hash-pinned Nollm source files, preserving actual fixed-point and Recall bodies. EXTEND_EXISTING_TOOL: isolated diagnostic adapters and a review-only filter-order diff, not a replacement Core or new global calculus. COMPOSE_APPLIED (BRC): preserve source identity, target identity, direction, path multiplicity, remaining resources and chosen observer before any total-only summary. The no-inverse argument applies only to the stated positive-mass observer. Future operations distinguish labels that a cell/score summary erases.

## 9. Validation, publication boundary and next unit

Both final executions produced byte-identical results.json and all five auxiliary result/certificate files. Source files pass Git-blob integrity before execution. Every reciprocal edge check invokes the actual reverse expansion; no cropped-boundary artifact is counted. Two distinct resource witnesses are separated from the main native-geometry scan.

No production source is modified, no full Core/package/provider suite is claimed, no semantic benchmark is claimed, and no physical bandwidth/clock/cable measurement is inferred. No Working Truth or Foundation admission is made.

Next bounded unit: take the native reachable-state reference and a resource-aware/loss-reporting candidate into a proper Nollm Core fixture with approved entry, occupancy and Bridge contracts; compare identical labelled populations before any new layout or routing change. The minimal actionable regression tests are beam1 early termination and the one-bridge-budget hybrid. Further mathematical work should measure visibility of arithmetic labels under this native observer rather than continuing to optimize an external topology alone.

Classical comparison: Ahmadi, Raith and Jalili, Resource Constrained Pathfinding with A* and Negative Weights, arXiv:2503.11037. This is context for resource-aware labels, not evidence for the present code-specific counts. Nollm source paths and immutable hashes above are the primary evidence for implementation facts.
