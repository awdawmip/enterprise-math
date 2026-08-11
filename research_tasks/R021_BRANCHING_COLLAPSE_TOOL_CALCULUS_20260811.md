<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS",
  "title": "R021 Branching Collapse Tool Calculus and On-Demand Refinement",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CRITICAL",
  "frontier": "Determine whether branch-preserving/set-valued collapse can be elevated from a semantic boundary into a reusable exact tool: characterize the right state object, exact composition laws, minimal branching/refinement needed for a declared future language, branch coalescence, and storage/work/depth tradeoffs.",
  "next_action": "Build the generic branching-collapse calculus, prove or kill exactness/minimality claims, implement a finite-state compiler/oracle for minimal branch-safe refinement, and pressure-test arithmetic examples before recommending any shared-tool or theorem surface.",
  "dependencies": [
    {
      "target": "RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE",
      "action": "CONSUME_RESULT_SUPPORT_UNION_AND_BRANCH_TIMING_GATE",
      "satisfied": true
    },
    {
      "target": "RS-R017-PTH-POWER-UNRESOLVED-CARRIER-CLASSIFICATION",
      "action": "CONSUME_ENDPOINT_CELL_FIBRE_AND_RECOLLAPSE_BOUNDARIES",
      "satisfied": true
    },
    {
      "target": "RS-R018-R017-CARRIER-COMPLETENESS-LEAN-FORMALIZATION",
      "action": "CONSUME_LEAN_CHECKED_SATURATION_AND_COMPOSITION_CORE",
      "satisfied": true
    },
    {
      "target": "RS-R019-P018-PRECISION-OBJECT-SEMANTIC-REAUDIT",
      "action": "CONSUME_PRECISION_OBJECT_TYPING",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R015/R016 accepted branch-deferral result-support core",
    "R017 accepted carrier-classification package",
    "R018 Lean-checked CarrierCompleteness core at head 82ae7c0ecf4c83035a60185a81acb6699a9bf446",
    "R019 accepted P018 semantic impact matrix",
    "P023 deterministic factorization/refinement theorem family",
    "R014 representation-resource methodology"
  ],
  "evidence_status": "BRANCHING_COLLAPSE_TOOL_DISCOVERY_GATE",
  "last_progress_ref": "R018 Lean gate accepted / R019 impact matrix frozen",
  "last_progress_at": "2026-08-11T17:21:00+08:00",
  "hard_block": null,
  "tags": [
    "R021",
    "branching-collapse",
    "set-valued",
    "support",
    "nondeterminism",
    "on-demand-refinement",
    "future-language",
    "compiler",
    "pareto"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R021",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R021 — Branching Collapse Tool Calculus and On-Demand Refinement

Status: `READY / P0 / FOUNDATIONAL_CRITICAL / TOOL DISCOVERY GATE / NOT CANONICAL`

## 1. Mother question

The accepted R015–R019 chain established two facts that must be held simultaneously:

1. once a legitimate set-valued result-support state and relational future semantics are fixed, branch timing and intermediate union/coalescence do not change final reachable support;
2. a naive quotient/cell lift can be one-step exact yet fail under repeated coarse composition by introducing spurious final results.

This opens a distinct tool question:

> can collapse be made deliberately branching, rather than globally refined to a deterministic exact state, and thereby obtain an exact and computationally useful representation of future result support?

The task must not assume the answer is yes.

The target is a reusable calculus and executable compiler/oracle that decides when branching is sufficient, how much branching/refinement is minimally necessary, when branches may safely coalesce again, and whether the resulting storage/work/depth tradeoff is genuinely better than deterministic refinement or full-fibre propagation.

## 2. Core semantic objects

Work in a generic finite or finitely enumerable transition setting first.

Let:

- `X` be the fine state space;
- `q : X -> Q` a deterministic coarse observation/collapse;
- `G` a declared family of future generators, each represented by a relation or deterministic operation on `X`;
- `U` a declared future language/horizon built from `G`;
- `o : X -> Y` or a declared final result-support observable.

Do not identify any of the following without proof:

- one coarse label `q(x)`;
- the full fibre `q^{-1}(q(x))`;
- a set of coarse alternatives;
- a set of fine alternatives;
- a set of branch tokens/refined cells;
- a result-support set;
- a path-count or provenance state.

A candidate branching-collapse representation may therefore require a new carrier `B`, an encoder from fine state/support into `B`, and relational/set-valued transitions on `B`.

The task must determine the weakest useful structure on `B`; do not preselect endpoint sets, full fibres, or powersets as the answer.

## 3. R021-T01 — branching-collapse taxonomy and exactness levels

Define a clean taxonomy containing at least:

1. **literal alternative branching** — the current state is genuinely one of several listed states;
2. **cell/fibre branching** — a branch denotes a compatible region/fibre rather than a literal state;
3. **support branching** — the state is the set of currently reachable results/fine states;
4. **branch-token refinement** — branches carry enough hidden correlation/refinement information to remain compositional;
5. **branch-on-demand refinement** — an unsafe operation splits only the currently reachable coarse cells according to the future distinction it needs;
6. **coalesced branching** — branches with equal declared future signatures are merged again.

For every notion distinguish:

- one-step exactness;
- finite-word final-support exactness;
- repeated collapse/re-expansion exactness;
- multiplicity/path-count exactness;
- provenance exactness.

Produce implication and separation diagrams. Every missing implication should be backed by a minimal counterexample when possible.

## 4. R021-T02 — canonical branching repair of an unsafe deterministic collapse

Given `q : X -> Q` and a generator/relation `R`, the naive existential quotient relation

`q[R[q^{-1}(a)]]`

is one-step exact at the cell level but may fail compositionally.

Derive and compare candidate exact repairs.

At minimum investigate:

- partition each fibre by coarse successor-support signature;
- partition each fibre by full future signature for a fixed language `U`;
- keep explicit fine-support subsets inside a coarse fibre;
- attach branch tokens recording the minimum correlation needed for later composition;
- delay splitting until the first generator that actually distinguishes representatives.

For one-step repair, determine whether successor-support partition is the unique coarsest refinement under a precise order.

For finite language/horizon repair, determine whether equality of future support signatures gives the unique coarsest deterministic refinement, and then ask the harder question:

> can a genuinely branching representation use fewer stored carrier states/labels than that deterministic refinement while remaining exact for the same future language?

Root generic automata/coalgebra/abstract-interpretation facts rather than claiming them as new mathematics.

## 5. R021-T03 — branch width and minimal branching complexity

Introduce quantitative invariants for a branching-collapse representation.

Candidates include:

- maximum live branch width `W`;
- cumulative branch creations;
- number of carrier labels/atoms;
- number of transition edges;
- refinement depth;
- maximum compatible fine-fibre size represented by one branch;
- coalescence ratio;
- horizon-dependent width `W_h`;
- language-dependent width `W_U`.

Define at least one mathematically exact **minimal branching width** problem:

> among all representations preserving the declared final result-support for language `U`, what is the least unavoidable branch width subject to a fixed carrier/refinement model?

Do not hide an exact-state encoding inside an uncharged branch token.

If a representation uses labels plus branch-local metadata, count both.

Find finite examples where:

- deterministic refinement is cheaper;
- branching is cheaper;
- they are incomparable because one wins storage while the other wins execution work/depth.

## 6. R021-T04 — on-demand refinement and safe recoalescence

Develop a local algorithmic rule for splitting only when needed.

For a current branch/cell `C` and next operation `R`, partition `C` by the next-step coarse successor-support observable. Execute the refined branches, then ask when some branches may be merged again.

Prove or kill candidate statements of the form:

- local successor-support splitting is sufficient for exactly one next step;
- repeated application of local splitting yields exact finite-word support;
- future-signature equality is sufficient for safe recoalescence;
- recoalescence based only on current coarse output may be unsound;
- branch histories may be consumed exactly when no declared future can distinguish them.

The preferred positive result is an explicit split/execute/coalesce invariant that can serve as a compiler correctness theorem.

If full future signatures are required globally, identify whether the on-demand algorithm nevertheless avoids constructing unreachable/global refinement states.

## 7. R021-T05 — branching versus deterministic refinement: representation/execution Pareto

Compare at least these strategies on the same semantic target:

A. original deterministic coarse collapse with no repair;
B. globally refined deterministic future-complete quotient;
C. full compatible fine-fibre propagation;
D. naive existential coarse branching;
E. exact branch-token representation;
F. branch-on-demand local refinement with recoalescence;
G. exact fine-state execution.

Measure separately:

- stored representation size;
- precomputation/refinement cost;
- transition table size;
- live branch count;
- execution work;
- critical-path depth;
- output materialization cost;
- reuse/amortization across many queries.

A central kill question is:

> is branching merely another encoding of deterministic refinement, or can it produce a genuine storage/execution-depth Pareto advantage?

Investigate the nondeterministic-versus-deterministic automaton analogy carefully, but do not transfer exponential-succinctness conclusions unless the exact Enterprise Math observable/transition model satisfies the needed hypotheses.

## 8. R021-T06 — executable branching-collapse compiler/oracle

Implement an independent finite-state research tool, suggested location:

`experiments/r021_branching_collapse_oracle.py`

with focused tests.

Given a finite fine system, coarse map, generators and bounded future language/horizon, the tool should be able to compute or compare as many of the following as practical:

1. exact fine reachable support;
2. naive quotient relational execution;
3. deterministic future-signature refinement;
4. one-step successor-support refinement;
5. branch-on-demand split/execute/recoalesce execution;
6. full-fibre execution;
7. minimal counterexample when a candidate compression becomes inexact;
8. branch width and representation/work statistics.

For small systems, exhaustively enumerate candidate partitions/refinements and verify claimed minimality/coarseness statements.

Where exact search over all branching representations is combinatorially large, implement a clearly bounded search class and state that restriction explicitly.

Mutation tests must deliberately remove needed branch distinctions, merge inequivalent branches, or re-expand a branch too aggressively and confirm that the oracle detects incorrect final support.

## 9. R021-T07 — arithmetic pressure tests

The generic tool must be tested on arithmetic cases already exposed by the project.

At minimum include:

### A. floor quotient plus translation

`q_r(n) = n // r`, future `+c`.

Known deterministic boundary: `+c` descends functionally through `q_r` iff `r | c`.

When `r` does not divide `c`, determine the minimal branching/on-demand refinement needed for horizons 1, 2, ... and compare it with simply retaining the residue `n mod r`.

This is an important kill test: if exact branching always reconstructs the complete residue immediately at comparable cost, record that negative result.

### B. p-th-power bracket

Use the lower/upper p-th-power bracket from R017/R018.

Separate:

- deferred lower/upper selector use, where the two endpoint observations are already sufficient;
- arbitrary translation/future dynamics, where the bracket cell is not future-complete.

Determine whether branch-on-demand splitting gives a useful intermediate representation between two-neighbour observation and exact fine state.

### C. witness/factor cutoff

Use a small factor/witness example where a low-cutoff stored witness set cannot determine a later higher-cutoff query.

Test whether branching over compatible hidden witness configurations can defer refinement profitably, or merely recreates the full compatible fibre.

### D. at least one relation-composition example

Use a small relation/witness incidence system to test whether branch tokens can retain the middle-incidence correlation that marginals/cardinalities lose.

Do not depend on R020 finishing; use a self-contained finite example.

## 10. R021-T08 — language-relative branching compiler theorem

Seek a theorem-level formulation connecting branching collapse to declared future language.

A strong candidate shape is:

- two branch states are mergeable iff their declared future result-support signatures agree;
- local split classes are induced by the next demanded observation;
- exact execution maintains a representation invariant mapping each live branch to a set of fine states;
- after a finite word, the union of branch denotations has exactly the same final observable support as fine execution.

Determine whether this yields:

1. a unique minimal deterministic quotient;
2. a family of smaller nondeterministic/branching presentations;
3. a canonical minimal branching presentation under an explicit cost/order notion;
4. or no useful uniqueness theorem.

Do not force uniqueness if the representation order has incomparable minima.

## 11. R021-T09 — prior-art/rooting attack

Actively root generic components against relevant established mathematics/computer science, including where appropriate:

- relational / powerset semantics;
- nondeterministic automata and subset construction;
- bisimulation, simulation and behavioural equivalence;
- Myhill–Nerode style future equivalence;
- abstract interpretation and partition refinement;
- CEGAR/on-demand refinement;
- symbolic model checking / belief-state propagation;
- semiring and Boolean matrix semantics;
- lumpability / state aggregation where relevant.

The project-specific residue is not the generic existence of nondeterministic state machines.

The useful residue would be a precise collapse-oriented calculus, exact compiler invariant, arithmetic specialization, and measured Pareto regime showing when branch-preserving collapse is actually advantageous for Enterprise Math future languages.

## 12. R021-T10 — kill criteria

The task must actively attempt to kill the tool hypothesis.

Return a negative or sharply scoped result if any of these dominates:

- exact branching necessarily retains the full fine state for the intended arithmetic languages;
- branch width grows as fast as the original fibre and offers no representation/work advantage;
- safe recoalescence requires precomputing the same global future signature as deterministic refinement;
- minimal branching optimization is computationally intractable in a way that destroys practical value for the intended use;
- apparent compression comes only from ignoring multiplicity/provenance required by the declared observable;
- every claimed advantage disappears after branch-token metadata is charged honestly.

A negative classification is a successful research result.

## 13. Required decision artifacts

Return all of the following:

1. `R021_BRANCHING_COLLAPSE_REPORT.md`;
2. theorem/counterexample table;
3. exact semantic taxonomy and implication diagram;
4. executable oracle/compiler plus focused tests;
5. bounded exhaustive/minimality evidence;
6. arithmetic benchmark table;
7. representation/work/depth Pareto table;
8. prior-art/rooting table;
9. downstream recommendation for P023/P018/R014/P021 and shared-tool routing;
10. one explicit answer to: **is branching collapse a genuinely strong reusable tool, and in what exact semantic regime?**

## 14. Return classification

Preferred positive return if a nontrivial exact tool regime survives:

`BRANCHING_COLLAPSE_TOOL_CORE_FOUND / EXACT_REGIME_CLASSIFIED / ON_DEMAND_COMPILER_CHECKED / PARETO_ADVANTAGE_DEMONSTRATED / NOT_CANONICAL`

If exactness is useful but no robust resource advantage is found:

`BRANCHING_COLLAPSE_EXACT_CALCULUS_FOUND / NO_STRONG_PARETO_ADVANTAGE / SPECIALIZED_TOOL_ONLY / NOT_CANONICAL`

If branching adds no useful power after honest metadata/resource accounting:

`BRANCHING_COLLAPSE_TOOL_HYPOTHESIS_KILLED / DETERMINISTIC_OR_FULL_STATE_DOMINATES / NEGATIVE_RESULT_ACCEPTABLE / NOT_CANONICAL`

If the generic theory is prior art but an Enterprise-specific arithmetic compiler/application survives:

`ROOTING_SUCCESS / ENTERPRISE_BRANCHING_SPECIALIZATION_SURVIVES / TOOL_CANDIDATE / NOT_CANONICAL`

## 15. Scope boundary

This is a discovery/calculus/tool task.

Do not directly rewrite existing shared theorem semantics from this task.

No new Lean formalization is required in this round. If a compact theorem package survives adversarial testing and executable verification, return the exact proposed Lean payload to Driver for a separate formalization gate.
