<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R022-HASHCLASH-BRC-TOOL-MINING",
  "title": "R022 Branch-Recoalescence Collapse Tool Mining from md5collgen and HashClash",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_TRANSFER",
  "frontier": "Use md5collgen and HashClash as mature branching-search systems to pressure-test the R021 branching-collapse calculus and extract reusable Enterprise Math tools for low-dimensional branch routing, bidirectional branch connection, on-demand refinement, backtracking, safe neutral moves, graded recoalescence, and resource-aware branch control.",
  "next_action": "Freeze the two source revisions, reconstruct their branch state machines without cryptographic narrative shortcuts, encode both in the Branch-Recoalescence Collapse calculus, prove or kill candidate transferable invariants, and prototype only the generic tools that survive adversarial tests.",
  "dependencies": [
    {
      "target": "RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS",
      "action": "CONSUME_CURRENT_BRANCHING_COLLAPSE_INTERFACE_AND_FEED_BACK_CONCRETE_PATTERNS_WITHOUT_ASSUMING_R021_POSITIVE",
      "satisfied": true
    },
    {
      "target": "R015/R016 result-support branch-deferral core",
      "action": "CONSUME_FINAL_SUPPORT_AND_BRANCH_TIMING_DISTINCTION",
      "satisfied": true
    },
    {
      "target": "P023 deterministic factorization/refinement family",
      "action": "USE_AS_DETERMINISTIC_BASELINE",
      "satisfied": true
    }
  ],
  "source_refs": [
    "zhijieshi/md5collgen master@19592490cf62d2168e2c2fd8ec4a288236dd9238",
    "zhijieshi/md5collgen:block1.cpp static S11/S10/S01/S00/Wang branch router",
    "cr-marcstevens/hashclash master@892f02e6e1faf71c4ae70ad98a98cc707d6ac664",
    "cr-marcstevens/hashclash:scripts/cpc.sh birthday/forward/backward/connect/collision-search/backtrack orchestration",
    "Marc Stevens HashClash project documentation and chosen-prefix collision papers as provenance/prior art",
    "R021 taskbook at main@15e9dcb67ce1f78b320099f2078c733bcba39ebb"
  ],
  "evidence_status": "EXTERNAL_SOLVER_TO_BRC_TOOL_MINING_GATE",
  "last_progress_ref": "R021 branching-collapse taskbook opened; external source revisions locked for R022",
  "last_progress_at": "2026-08-11T17:39:00+08:00",
  "hard_block": null,
  "tags": [
    "R022",
    "branch-recoalescence-collapse",
    "BRC",
    "md5collgen",
    "hashclash",
    "branch-routing",
    "meet-in-the-middle",
    "backtracking",
    "safe-neutral-moves",
    "recoalescence",
    "tool-mining",
    "pareto"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R022",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R022 — Branch-Recoalescence Collapse Tool Mining from md5collgen and HashClash

Status: `READY / P0 / FOUNDATIONAL_TRANSFER / EXTERNAL SOLVER MINING / NOT CANONICAL`

## 1. Naming and mother question

For this task use the formal working term:

**Branch-Recoalescence Collapse (BRC) / 分支汇合坍缩**.

The informal nickname **Many-World Collapse / 多世界坍缩** may be used in explanatory notes, but theorem/tool names should use BRC unless this task produces a demonstrably better term.

The reason for the name is structural rather than metaphorical:

`coarse state -> branch only when a future distinction demands it -> execute compatible branches -> prune impossible branches -> safely recoalesce branches that no declared future can distinguish`.

The mother question is:

> do the mature collision-search architectures embodied by md5collgen and HashClash expose reusable BRC primitives that are stronger than ordinary parallel search, generic backtracking, or deterministic global refinement, and can those primitives become exact Enterprise Math tools?

This task must use BRC essentially. A result that merely explains MD5/SHA-1 cryptanalysis, tunes implementation parameters, or parallelizes existing code does not satisfy the task.

The cryptanalytic repositories are experimental source systems. The intended output is generic mathematics and generic search/refinement tooling, not a repackaged attack utility.

## 2. Why these two source systems form a useful pair

Treat the repositories as two ends of one branch-control spectrum.

### 2.1 md5collgen: small compiled branch family

In `block1.cpp`, the solver inspects a small number of intermediate-state conditions and routes into one of four Stevens sub-solvers `S11`, `S10`, `S01`, `S00`, otherwise falling back to a Wang path.

Abstract this as:

`fine/intermediate state x -> small discriminant signature sigma(x) -> one branch-specialized solver A_sigma`.

The research question is not how to reproduce the collision. It is whether this is an instance of a general **minimal branch-signature compiler**: retain only the future-relevant bits needed to choose a correct specialized continuation rather than retaining the full fine state or prebuilding one globally refined deterministic machine.

### 2.2 HashClash: dynamically generated branch populations

The chosen-prefix orchestration exposes a larger pipeline:

`birthday bridge -> forward differential-path population -> backward differential-path population -> middle connection -> terminal search`,

with bounded branch populations, memory/work tradeoffs, and rollback to an earlier near-collision stage when a later branch family fails.

Abstract this as:

`generate branch cones from constrained boundaries -> compress/filter branch tokens -> connect compatible cones at an interface -> continue from the joined state -> rewind locally on failure`.

The research question is whether this yields a general **bidirectional BRC connector plus adaptive rebranching calculus**.

## 3. Semantic discipline

Before proposing tools, define a generic staged constrained transition system.

Let:

- `X_t` be the fine state space at stage `t`;
- `C_t` be the accumulated constraint language at stage `t`;
- `q_t : X_t -> Q_t` be a coarse observation;
- `sigma_t : X_t -> S_t` be a candidate branch discriminant/interface signature;
- `G_t` be the allowed next-stage transitions or relations;
- `U_t` be the declared residual future language;
- `o` be the final result-support observable.

A live BRC branch should be represented explicitly, for example by a tuple

`b = (cell/support C, branch token tau, accumulated constraints kappa, stage t)`.

Do not identify `tau` with a full fine state unless the cost is charged honestly.

Define denotation `[[b]] subseteq X_t` and require every exact algorithmic claim to state what is preserved:

- existence of at least one completion;
- final reachable support;
- exact endpoint state;
- multiplicity/path count;
- provenance/history;
- optimization score only.

BRC exactness in this task defaults to **declared final result-support exactness** unless a stronger observable is explicitly named.

## 4. R022-T01 — source lock and architecture extraction

Freeze the exact source revisions listed in metadata and build a compact architecture map.

For md5collgen identify at minimum:

- the branch discriminants used before selecting `S11/S10/S01/S00/Wang`;
- which state information is discarded after routing;
- what each specialized branch assumes about its input;
- where branch failure/retry occurs;
- whether the five solver families are semantically disjoint, overlapping, or merely performance-specialized.

For HashClash identify at minimum:

- birthday-stage state and output interface;
- forward path carrier;
- backward path carrier;
- connection interface;
- filtering/ranking constraints;
- branch-count/memory controls;
- rollback point and rollback depth;
- terminal success certificate.

Produce `R022_SOURCE_ARCHITECTURE_MAP.md`.

Do not copy large code bodies. Record source file/function coordinates and the abstract state transition they realize.

## 5. R022-T02 — static branch-signature theorem from md5collgen

Model the md5collgen router as a finite family of continuation procedures `{A_s}` indexed by a discriminant `sigma(x)`.

Investigate the exact generic problem:

> given fine states `x` and a family of future continuation algorithms, what is the coarsest signature `sigma` that routes every reachable state to a continuation family preserving the declared final support?

Compare at least:

1. full fine-state routing;
2. routing by the observed discriminant bits used by md5collgen;
3. routing by future-support equivalence;
4. routing by one-step successor-support equivalence;
5. a learned/minimized discriminant obtained by exhaustive deletion of signature components on a bounded model.

Seek a theorem or counterexample of the form:

`minimal correct router signature = quotient by continuation-behaviour equivalence`

under explicit assumptions.

If multiple incomparable minimal signatures exist, preserve that result rather than forcing uniqueness.

Candidate generic tool hypothesis:

**Branch Signature Router (BSR)** — compile a small future-relevant branch token from a large fine state.

The tool hypothesis is killed if the signature is only a hard-coded artifact of MD5 and does not survive generic finite models or arithmetic pressure tests.

## 6. R022-T03 — branch cones and bidirectional connection

Abstract HashClash forward/backward construction into two branch sets at an interface stage `t`:

`F_t = reachable forward branch tokens`,

`B_t = backward-compatible branch tokens`.

Define an interface compatibility predicate `K(f,b)` and a joined denotation.

Prove or kill a **Bidirectional Recoalescence Criterion**:

> when `K(f,b)` holds and the joined interface token is sufficient for the residual future language, all pre-interface histories whose residual signatures agree may be discarded or recoalesced without changing final result support.

Separate three cases:

- exact equality of a sufficient interface state;
- compatibility of partial constraints without exact state equality;
- heuristic closeness only.

Only the first two may support exact BRC claims.

Determine the minimal interface information needed for connection. Measure the cost of storing full endpoints versus compressed interface signatures.

Candidate generic tool hypothesis:

**BRC-Connect** — construct forward and backward branch cones and join them through the weakest exact interface signature.

Compare with ordinary meet-in-the-middle. The project-specific novelty, if any, must come from branch-token minimality, exact recoalescence semantics, or on-demand refinement rather than the generic existence of bidirectional search.

## 7. R022-T04 — safe recoalescence versus mere collision

The cryptanalytic sources make equality/collision visually tempting. Do not equate every equality event with safe recoalescence.

For branch states `b1,b2` at the same stage define residual future signatures

`Phi_U(b) = final result support reachable from [[b]] under residual language U`.

Use the exact safe merge baseline:

`b1 ~_U b2 iff Phi_U(b1) = Phi_U(b2)`.

Then investigate cheaper sufficient certificates, including:

- equality of full deterministic interface state;
- equality of compressed interface state plus equal residual constraints;
- equality of a continuation-router signature;
- equality of current coarse output only.

Produce minimal counterexamples for every unsound cheaper certificate.

This task must explicitly distinguish:

`search collision` from `semantic safe recoalescence`.

A key desired result is a reusable certificate format stating exactly why two branches may be merged.

## 8. R022-T05 — neutral/tunnel moves as branch-preserving safe operations

Hash collision search uses local freedoms often described through tunnels, neutral bits, message modification, or related path-preserving degrees of freedom.

Do not import those names as new mathematics. Abstract the structural question:

> once a branch has accumulated constraints `kappa`, which local transformations may vary the hidden fine state while preserving the branch's already-declared interface/future obligations?

For each branch `b`, define a candidate partial safe-move family `N_b`.

Test whether these moves form any useful structure under the actual legality domains:

- partial monoid/action;
- groupoid-like local symmetry;
- closure system;
- merely an unstructured compatibility relation.

Connect this carefully to the project's existing safe-operation algebra. Do not force a total monoid if legality depends on the current branch.

Candidate generic tool hypothesis:

**Safe Neutral-Move Analyzer (SNMA)** — find local branch-preserving moves that explore a fibre without triggering unnecessary refinement.

The tool hypothesis is killed if the safe moves require essentially full fine-state simulation or have no reusable legality criterion.

## 9. R022-T06 — rollback as on-demand refinement rather than restart

HashClash may retreat to an earlier near-collision stage when a later attempt fails.

Model a staged BRC execution with checkpoints

`b_0 -> b_1 -> ... -> b_k`.

When the live branch family at stage `k` becomes empty or exceeds a resource threshold, compare:

A. restart from the beginning;
B. retain all fine state globally to avoid failure;
C. rewind to the earliest checkpoint whose unresolved branch choice can still alter feasibility;
D. rewind only one step;
E. refine the failing branch token locally and replay downstream.

Define **minimal causal rewind depth** if possible:

> the latest checkpoint at which splitting a previously coalesced class can restore a completion that was lost by an over-coarse branch decision.

Seek an exact or bounded algorithm for finite systems.

Candidate generic tool hypothesis:

**Backtrack Refinement Controller (BRCtrl)** — identify where an inexact/failed branch abstraction first discarded a necessary distinction and refine from that point only.

Connect to counterexample-guided refinement prior art and identify what remains genuinely specific to BRC.

## 10. R022-T07 — graded recoalescence potential from near-collision ladders

Chosen-prefix methods reduce a structured difference over several near-collision blocks instead of demanding immediate identity.

Abstract this into a potential `d(b1,b2)` or defect vector measuring how far two branch worlds are from an exact recoalescence certificate.

Investigate whether a useful potential can satisfy some of:

- zero exactly implies safe recoalescence;
- each repair stage decreases the potential under a declared strategy;
- potential components correspond to independent future distinctions;
- potential predicts expected remaining branch work;
- potential supports admissible search ordering.

Do not assume Hamming distance is the right abstraction.

Candidate generic tool hypothesis:

**Recoalescence Potential Scheduler (RPS)** — rank branch pairs by a mathematically justified distance-to-safe-merge.

Kill the hypothesis if the potential is cryptographic-path-specific or non-monotone in generic systems.

## 11. R022-T08 — adaptive branch budget and branch-width economics

HashClash exposes explicit tradeoffs among stored path counts, memory, path-type range, connection work, and number of repair blocks.

Translate these into R021 resource quantities rather than treating them as implementation knobs.

Measure at least:

- maximum live branch width `W`;
- cumulative branch creation count;
- bytes or abstract token units stored per branch;
- branch-token entropy/signature width;
- forward cone size;
- backward cone size;
- connection candidate count/density;
- prune ratio;
- recoalescence ratio;
- rewind depth;
- expected recomputation work;
- critical path depth;
- precomputation versus per-query work.

Compare:

1. full fine-state propagation;
2. deterministic future-complete refinement;
3. forward-only branching;
4. bidirectional BRC;
5. BRC with safe neutral moves;
6. BRC with local rewind/refinement.

Candidate generic tool hypothesis:

**Adaptive Branch Budgeter (ABB)** — choose branch width and interface refinement to minimize a declared storage/work/depth objective while preserving exact final support.

No advantage counts unless branch-token metadata is charged.

## 12. R022-T09 — concrete BRC reconstruction experiments

Build bounded, reproducible experiments that reconstruct structural mechanisms without turning the task into an operational collision-attack project.

Use two layers:

### Layer A — source-faithful structural traces

Instrument or re-express only enough of the source logic to observe:

- branch router signatures;
- number of candidate branches after each stage;
- pruning events;
- connection events;
- rollback events;
- state/signature sizes.

Use fixed educational/test vectors or source-provided benign examples.

### Layer B — synthetic finite transition systems

Construct small systems with the same branching motifs but no cryptographic meaning:

- a five-way static continuation router resembling `S11/S10/S01/S00/fallback`;
- forward/backward branch cones with a middle interface;
- neutral moves inside a branch fibre;
- dead-end branches requiring rewind;
- graded defects requiring multiple repair stages.

Exhaustively compute exact fine-state support and compare every BRC compression against it.

The synthetic layer is required for theorem/minimality claims because it permits exhaustive truth checking independent of cryptographic heuristics.

Suggested experiment root:

`experiments/r022_hashclash_brc/`

## 13. R022-T10 — candidate generic tool prototypes

Prototype only candidates that survive T02-T09.

Preferred generic, non-cryptographic tool interfaces include:

1. `branch_signature_router` — infer/test minimal continuation signatures on finite systems;
2. `brc_connect` — forward/backward branch-cone connector with exact interface certificates;
3. `safe_neutral_moves` — enumerate or verify branch-preserving partial operations;
4. `brc_refine_backtrack` — localize the earliest lost distinction and refine/replay;
5. `recoalescence_potential` — test potential functions against exact future-equivalence;
6. `branch_budget_optimizer` — compare storage/work/depth Pareto frontiers.

A prototype must expose its semantic contract and failure mode. Do not merely wrap the external cryptanalytic binaries.

If two candidates collapse to the same underlying primitive, merge them.

If none survives, return a negative tool-mining result.

## 14. R022-T11 — adversarial kill tests

Actively try to destroy every appealing transfer claim.

Required attacks include:

- replace the md5collgen discriminant with a smaller signature and seek the first incorrect continuation;
- add irrelevant discriminant bits and quantify useless storage;
- force two HashClash-like branches to share the same current coarse output but different residual constraints and test unsafe merging;
- construct an interface where forward/backward endpoint equality is insufficient because hidden provenance is still observable later;
- construct a case where local neutral moves are individually safe but composition leaves the legal domain;
- construct a case where one-step rewind cannot recover a lost future but deeper causal rewind can;
- construct a misleading distance metric that decreases while true future-signature distance increases;
- charge all hidden metadata and retest every claimed Pareto gain.

Negative results are first-class deliverables.

## 15. R022-T12 — relation to established prior art

Root the generic pieces against established areas including as appropriate:

- differential cryptanalysis and differential-path construction;
- neutral bits, tunnels and message modification;
- birthday search;
- meet-in-the-middle and bidirectional search;
- constraint programming and backtracking;
- counterexample-guided abstraction refinement;
- symbolic execution/model checking;
- nondeterministic automata and future equivalence;
- partial actions and local symmetries;
- branch-and-bound and heuristic search;
- state aggregation/lumpability.

Do not claim these generic ideas as new.

The Enterprise Math residue, if positive, must be one or more of:

- a precise BRC semantic carrier and certificate;
- a minimal branch-signature theorem;
- a minimal exact connection interface theorem;
- a safe branch-local operation algebra;
- a causal rewind/refinement theorem;
- a graded recoalescence potential with exact semantics;
- a measured regime where BRC gives a real storage/work/depth Pareto advantage;
- a compiler/oracle combining these pieces for arbitrary finite future languages.

## 16. R022-T13 — direct feedback into R021

Return a dedicated section `R022_TO_R021_FEEDBACK.md` answering:

1. which R021 branch carrier best matches md5collgen;
2. which R021 branch carrier best matches HashClash path populations;
3. whether the source systems exhibit genuine safe recoalescence or only search convergence;
4. whether branch tokens are materially smaller than deterministic future-complete states;
5. whether bidirectional connection changes the R021 minimal-width problem;
6. whether local neutral moves enlarge the useful safe-operation language;
7. whether backtracking suggests a new notion of causal refinement depth;
8. which candidate tools deserve addition to the shared theorem/tool surface;
9. which attractive analogies were killed.

Do not wait for R021 to finish. This task is permitted to return concrete counterexamples or constructions that force R021 to revise its conjectures.

## 17. Success and kill criteria

A positive task result requires at least one reusable BRC primitive that is both:

- semantically exact for a declared observable/future language; and
- nontrivially useful after honest resource accounting.

Strong positive examples include:

- a branch signature strictly smaller than the deterministic future-complete state while supporting exact on-demand continuation;
- a bidirectional connector whose interface representation yields a real resource advantage;
- a safe branch-local operation family that avoids otherwise necessary refinement;
- a causal rewind rule that provably preserves exactness while avoiding global restart;
- a generic recoalescence certificate that can be checked locally;
- a combined BRC compiler outperforming deterministic refinement on at least one non-cryptographic benchmark without losing final support.

Return a negative classification if:

- all useful source behaviour reduces to ordinary parallelism/backtracking with no new BRC semantic content;
- exact branch signatures reconstruct the full fine state;
- safe connection requires the same global information as deterministic refinement;
- neutral moves are too source-specific to generalize;
- metadata costs erase all Pareto gains;
- the apparent benefit depends on heuristic rather than exact support preservation.

## 18. Required deliverables

Return at minimum:

1. `R022_HASHCLASH_BRC_REPORT.md`;
2. `R022_SOURCE_ARCHITECTURE_MAP.md`;
3. `R022_BRC_SEMANTIC_MODEL.md`;
4. md5collgen branch-signature theorem/counterexample table;
5. HashClash branch-cone/connect/recoalescence theorem/counterexample table;
6. neutral-move legality/algebra table;
7. rollback/causal-refinement table;
8. recoalescence-potential experiments;
9. storage/work/depth Pareto table;
10. generic prototype tools that survived kill tests;
11. focused tests and mutation tests;
12. prior-art/rooting table;
13. `R022_TO_R021_FEEDBACK.md`;
14. one explicit answer to: **did md5collgen/HashClash reveal a new Enterprise Math BRC tool, and exactly what is its semantic contract?**

## 19. Return classification

Preferred strong positive return:

`BRC_EXTERNAL_TOOL_CORE_FOUND / EXACT_TRANSFER_CLASSIFIED / GENERIC_PROTOTYPE_CHECKED / PARETO_ADVANTAGE_DEMONSTRATED / R021_FEEDBACK_READY / NOT_CANONICAL`

Useful scoped positive return:

`BRC_TRANSFER_PRIMITIVES_FOUND / EXACT_BUT_SPECIALIZED / PARTIAL_TOOL_VALUE / R021_FEEDBACK_READY / NOT_CANONICAL`

Negative but successful return:

`HASHCLASH_BRC_ANALOGY_CLASSIFIED / NO_NEW_GENERIC_TOOL / SOURCE_SPECIFIC_OR_METADATA_DOMINATED / R021_KILL_EVIDENCE_READY / NOT_CANONICAL`

## 20. Final research discipline

Do not ask whether the external projects are "already parallel". That is not the relevant property.

Ask instead, at every stage:

1. what incompatible fine possibilities are currently being preserved together;
2. what exact future distinction forces them to split;
3. what minimal token remembers the correlation needed after the split;
4. what local operations preserve that token's obligations;
5. what certificate allows two histories to forget their differences and safely merge;
6. when failure proves that an earlier merge/refinement was too aggressive;
7. whether recovering the lost distinction locally is cheaper than globally refining from the start.

The task succeeds only if these questions materially shape the analysis and the produced tools.
