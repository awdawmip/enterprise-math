# RS-R022-HASHCLASH-BRC-TOOL-MINING — Research Report

**Researcher-ID:** EM-R022-HC7B4A  
**Working term:** Branch-Recoalescence Collapse (BRC) / 分支汇合坍缩 / “多世界坍缩”  
**Taskbook:** `research_tasks/R022_HASHCLASH_BRC_TOOL_MINING_20260811.md`  
**Taskbook commit:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Source locks:**  
- `zhijieshi/md5collgen@19592490cf62d2168e2c2fd8ec4a288236dd9238`
- `cr-marcstevens/hashclash@892f02e6e1faf71c4ae70ad98a98cc707d6ac664`

**Research status:** CANDIDATE RESEARCH HANDOFF / NOT CANONICAL

## Executive verdict

R022 found **real BRC transfer primitives**, but did **not** find a new standalone generic search algorithm that survives prior-art kill tests.

The strongest source-backed results are:

1. **Branch Signature Router (BSR):** md5collgen shows that a large fine state may need only a small **control signature** to select a correct continuation kernel. This does not imply that the state payload itself has been compressed.
2. **Context-relative residual recoalescence:** HashClash's MD5 connector expands multiple bitwise worlds and then erases duplicate six-word residual connector states. Under fixed connection context this is a genuine safe recoalescence event for connector feasibility/final support.
3. **No-Completion Cone Certificate (NCC):** after a connector failure at bit `b`, HashClash identifies later lower paths with the same relevant path-prefix and residual-prefix signature and skips them. This is a concrete negative branch-cone certificate.
4. **Typed BRC-Connect:** forward and backward path populations connect through residual constraints rather than endpoint equality alone. This gives a useful Enterprise Math interface calculus, while the bidirectional search gain itself remains standard meet-in-the-middle.
5. **Causal refinement depth:** useful as a BRC diagnostic for inexact/budgeted collapse, but HashClash's actual `k -> k-1` timeout rollback is only heuristic.
6. **Recoalescence potential:** no generic scalar distance survived. The only exact generic defect is future-signature disagreement itself, which is usually as expensive as the equivalence problem.
7. **Pareto:** generic finite systems do exhibit real storage/work/depth tradeoffs for branching representations, but the clean positive witness reduces to standard NFA-vs-DFA succinctness. There is no evidence that BRC universally dominates deterministic future-complete refinement.

Recommended return classification:

`BRC_TRANSFER_PRIMITIVES_FOUND / EXACT_BUT_SPECIALIZED / PARTIAL_TOOL_VALUE / R021_FEEDBACK_READY / NOT_CANONICAL`

This is intentionally weaker than `BRC_EXTERNAL_TOOL_CORE_FOUND`: the source mechanisms are valuable witnesses and compiler primitives, but their generic algorithmic cores are substantially rooted in automata minimization, meet-in-the-middle, dynamic programming/state memoization, nogood recording, backtracking and CEGAR.

---

# 1. Semantic contract used by R022

Default exactness follows the taskbook:

**declared final result-support exactness**

unless multiplicity, provenance, or optimization score is explicitly named.

Let a branch token `b` at stage `t` denote a set of fine states:

`[[b]]_t ⊆ X_t`.

Let `U_t` be the declared residual future language and `o` the final observable.

Define residual support:

`Supp_t(b,u) = { o(y) : x ∈ [[b]]_t and x --u--> y }`.

For a fine state `x`, write `Supp_t(x,u)` similarly.

Two fine states are residual-future equivalent when

`x ≡_{U_t} y  iff  Supp_t(x,u) = Supp_t(y,u) for every u ∈ U_t`.

The coarsest **token-identification** signature that is exact for this declared semantics is the quotient by `≡_{U_t}`.

Important distinction:

- **exact set union** of branch denotations may be support-safe when the transition semantics distributes over union;
- **forgetting distinctions and representing the union by a coarser token/fibre** is safe only when the token representation has the required residual congruence.

Most false BRC arguments conflate these two operations.

---

# 2. R022-T01 — source lock and architecture extraction

Completed in `research/R022_SOURCE_ARCHITECTURE_MAP.md`.

## md5collgen

`block1.cpp::find_block1` implements a five-way continuation router:

- S11
- S10
- S01
- S00
- Wang fallback

The source's relevant physical route bits are nine bits drawn from the IV:

- bit 31 of `IV[1],IV[2],IV[3]`;
- bit 25 of `IV[1],IV[2],IV[3]`;
- bit 0 of `IV[1],IV[2]`;
- bit 6 of `IV[1]`.

The route label is small, but the complete IV is still passed into the selected continuation. This is a control-path compression witness, not a complete future-state token.

## HashClash

`scripts/cpc.sh` organizes:

`birthday -> start-near-collision -> forward cone + backward cone -> connect -> collision search -> append block`

and retries earlier stages after timeout.

The connector is the key BRC object:

`src/md5connect/main.hpp::connect_bitdata`

contains six 32-bit residual fields, and

`src/md5connect/connect.cpp::md5_connect_bits`

expands possible bitwise connector worlds and executes:

`sort -> unique`

on exact residual tokens after each bit.

A failure at bit `b` feeds a prefix-skip mechanism in `md5_connect` that can eliminate later lower paths sharing the relevant prefix conditions and residual-prefix values.

---

# 3. R022-T02 — Branch Signature Router theorem

## 3.1 Generic formulation

Let continuation algorithms be `{A_a : a ∈ A}`.

For each algorithm define its correctness domain, relative to the declared result semantics:

`D_a = { x ∈ X : A_a is correct on x }`.

A Branch Signature Router consists of:

- signature `sigma : X -> Z`;
- selector `alpha : Z -> A`.

It is correct iff

`for every z ∈ Z, sigma^{-1}(z) ⊆ D_{alpha(z)}`.

This gives a clean theorem.

### BSR Cover Theorem

If the only cost is the number of distinct continuation labels used, the minimum number of router labels equals the minimum number of algorithm correctness domains `{D_a}` required to cover `X`.

Proof sketch:

- every correct route label selects an algorithm whose correctness domain covers its entire fibre;
- fibres selecting the same algorithm can be merged;
- therefore a correct router induces a cover by selected correctness domains;
- conversely, any cover allows each state to be assigned to one covering algorithm.

Thus the minimum-label BSR problem is a solver-domain cover problem. With arbitrary overlapping correctness domains, minimal routers need not be unique.

This is an important correction to the tempting statement:

`minimal correct router = semantic future quotient`.

That statement is false in general because algorithm applicability and semantic future equivalence are different relations.

## 3.2 Three-state kill witness

Synthetic system:

- `C(a)={A,B}`
- `C(b)={A}`
- `C(c)={B}`

where `C(x)` is the set of correct continuation algorithms at state `x`.

There is no one-algorithm router for all three states.

Two incomparable minimal two-block routers exist:

- `{a,b} | {c}`
- `{a,c} | {b}`

Even if all three fine states have the same final semantic support, the algorithm-routing partition still needs two labels.

So BSR is a **continuation-implementation signature**, not necessarily the semantic Myhill-Nerode quotient.

## 3.3 md5collgen bounded exact test

The synthetic source-shaped model exhaustively enumerates all `2^9 = 512` assignments to the nine route-relevant physical bits.

Results:

- five route labels;
- route population in the unconstrained nine-bit model:
  - Wang: 504
  - S00: 2
  - S01: 2
  - S10: 2
  - S11: 2
- when the signature is constrained to be a **subset of the nine physical coordinates**, the minimum exact subset has size **9**;
- deleting any one of the nine physical bits admits a pair of assignments with the same retained coordinates but different routes;
- when arbitrary compiled labels are allowed, five route labels require **3 fixed-width bits**.

Therefore:

**minimal raw-coordinate signature = 9 bits**  
**minimal fixed-width compiled route label = 3 bits**

These are not contradictory. They optimize different representation classes.

## 3.4 Payload accounting

The source continuation still consumes the IV after routing.

Therefore a valid accounting is:

`branch metadata = route token + retained continuation payload`

not

`branch state = 3-bit route token`.

Any Pareto claim that replaces the full continuation payload with the 3-bit route label is rejected as metadata cheating.

## 3.5 T02 verdict

**BSR survives as a generic tool interface**, but:

- its minimality is representation-class dependent;
- solver-domain minimality is not semantic future minimality;
- the md5collgen example gives control compression only;
- the algorithmic core is rooted in finite classification/feature selection/set cover.

---

# 4. R022-T03 — branch cones and BRC-Connect

At an interface stage `t`, model:

- `F_t`: forward branch tokens;
- `B_t`: backward branch tokens.

Let `I_t` be an exact residual interface.

A generic connector asks for pairs `(f,b)` such that

`Compat_t(I_t(f), I_t(b))`

holds and there exists a full completion represented by the pair.

## 4.1 Weakest exact interface

For a fixed context `kappa`, an interface `I_t` is exact for connection if equality/compatibility at the interface preserves exactly the declared completion support.

The coarsest possible exact interface is again induced by residual completion equivalence:

`x ~_conn y`

iff they have the same set of legal completions against every allowed opposite-side residual context.

This is stronger than equality of current endpoints unless endpoint values happen to be a sufficient statistic for every residual constraint.

## 4.2 HashClash source interface

HashClash does not connect lower and upper paths by a simple endpoint equality check.

Its rolling connector state carries:

- `dQt`
- `dQtp1`
- `dFt`
- `dFtp1`
- `dFtp2`
- `dFtp3`

for a raw semantic-field width of 192 bits.

This token is sufficient only relative to fixed:

- lower path;
- upper path;
- stage `t`;
- bit index;
- message differences / step functions.

Thus the correct abstraction is:

`I_hash = (context_id, six-word residual token, bit index)`

not a free-standing 192-bit global state.

## 4.3 Minimality status

R022 did **not** prove that all six HashClash residual words are globally minimal.

What is proved from source structure:

- all six are part of equality;
- all six participate in the connector recurrence or initial residual;
- exact duplicate six-word tokens are used as the implementation's feasibility-state identity.

Generic finite-state tooling can remove candidate interface fields and search for the first wrong completion. That interface-minimization oracle is reusable.

But an actual source-level theorem that no smaller encoded HashClash connector exists would require a dedicated algebraic proof over the MD5 connector equations and is not established here.

## 4.4 Meet-in-the-middle kill

A non-cryptographic 20-variable checksum model was split into two ten-variable cones.

Measured bounded counts:

- full end-check enumeration: `2^20 = 1,048,576`;
- forward frontier: `2^10 = 1,024`;
- backward frontier: `2^10 = 1,024`;
- total bidirectional frontier enumeration: `2,048`;
- work ratio: `512x`;
- exact interface token: 17 bits in the model;
- idealized parallel critical depth:
  - one-way full assignment: 20;
  - two cones plus join: 11.

This is a strong resource benefit but is **ordinary meet-in-the-middle**.

BRC-specific value is not the split itself. It is:

- declaring the exact residual interface;
- distinguishing endpoint coincidence from completion equivalence;
- charging interface-token cost;
- permitting source-justified recoalescence within each cone.

## 4.5 T03 verdict

**Keep `brc_connect` as a generic typed compiler primitive.**  
**Reject any novelty claim based only on bidirectionality.**

---

# 5. R022-T04 — safe recoalescence vs mere collision

## 5.1 Recoalescence Congruence Certificate (RCC)

Proposed reusable certificate:

`RCC = (stage, context, semantics, residual_language, signature, proof)`

Required fields:

1. **stage** — where the merge happens;
2. **context** — fixed external constraints;
3. **semantics** — support/existence, multiplicity, provenance, score, etc.;
4. **residual language/horizon**;
5. **signature value** shared by all merged representatives;
6. **proof obligation/evidence** that equal signature implies equal residual semantics.

For final-support exactness, a sufficient proof obligation is:

`signature(x)=signature(y) => Supp_t(x,u)=Supp_t(y,u) for every u in U_t`.

A stronger local transition-congruence proof may establish this inductively.

## 5.2 HashClash positive witness

In `md5_connect_bits`:

- each current six-word residual state expands through the next bit;
- exact duplicates are erased;
- the remaining bit processing uses the residual state under the same fixed lower/upper context.

This is a real **positive recoalescence** witness.

The semantic scope is local connector feasibility/support. Multiplicity and provenance are explicitly not preserved by `unique`.

## 5.3 Exact-history collapse synthetic test

Generic model:

`r' = (2r + choice) mod 5`

with binary branching at each of 12 stages.

Without merging, hidden histories count:

`2^12 = 4096`.

With exact residual-state recoalescence:

- live residual tokens reach at most 5;
- 3 bits/token are sufficient;
- at most 15 live token bits in the simple accounting.

Exhaustive suffix checks confirm that prefixes with equal residual token have identical residual support in the bounded test.

But the deterministic future-complete quotient also has exactly **5 states**.

This is a key negative result:

**safe recoalescence can be perfectly real while providing zero advantage over the optimal deterministic quotient.**

## 5.4 Current-output equality kill

Synthetic mutation:

- reachable fine states: `{a,b}`;
- a third unreachable state `c` shares the same current coarse output;
- exact future support from `{a,b}` is `{ok0,ok1}`;
- merging to the coarse label and re-expanding its whole fibre `{a,b,c}` creates an extra result `spurious`.

Therefore:

`same current q-value` is not an RCC.

## 5.5 Endpoint/provenance kill

Two histories can reach the same current endpoint `s` while carrying provenance tags `A` and `B`.

Endpoint-only merge is safe if the only observable is endpoint existence.

It is unsafe if provenance is declared observable.

Thus every recoalescence claim must name its semantics.

## 5.6 T04 verdict

HashClash gives a genuine source witness for **semantic safe recoalescence**, not merely a visually attractive collision.

The reusable object is the **RCC**, not “equality” in the abstract.

---

# 6. R022-T05 — branch-local safe / neutral operations

A partial operation `n` is branch-local safe on branch/context `b` when:

1. it is defined on an explicit legal domain;
2. applying it keeps the result inside the declared branch/interface invariant, or moves it to a known equivalent token;
3. it does not change the declared residual final support without a corresponding refinement.

For an invariant signature `sigma`, a simple sufficient condition is:

`x in dom(n) => sigma(n(x)) = sigma(x)`.

This lets a search move inside a branch fibre without forcing a split.

## 6.1 HashClash motivation

MD5 collision work uses local freedoms/tunnels in which modifications preserve an earlier differential path segment and first affect a later state step. Structurally, this is exactly the kind of **local freedom under a guarded invariant** that BRC can model.

The cryptanalytic names are not transferred as new mathematics.

## 6.2 Composition kill

Synthetic partial-map witness:

- branch cell `{a,b}`;
- `n` is defined only at `a` and maps `a -> b`;
- `m` is also defined only at `a` and maps `a -> b`.

Both operations are safe on their own domains.

But `m o n` is undefined because `n(a)=b` and `b` is outside `dom(m)`.

Therefore branch-local safe partial moves do **not** generally form a monoid.

Better algebraic type:

**domain-guarded partial transformation category / semigroupoid.**

## 6.3 T05 verdict

Keep a **Safe Neutral-Move Analyzer (SNMA)** only as a legality checker/enumerator over explicit domains and invariants.

Kill any theorem claiming unconditional closure under composition.

---

# 7. R022-T06 — rollback as on-demand refinement

## 7.1 Exact BRC observation

If an RCC was actually exact for the declared future language, merging its worlds cannot later cause a semantic failure solely because of that merge.

Therefore causal rewind is relevant only when at least one of these is true:

- the earlier collapse was approximate/budgeted;
- heuristic pruning discarded representatives;
- the declared future language changed;
- the stored checkpoint is not future-complete;
- optimization/provenance semantics are stronger than the merge certificate.

## 7.2 Causal refinement depth

For a failed staged execution, define:

**causal refinement depth**

as the number of checkpoints one must rewind to reach the latest checkpoint at which a distinction discarded by an inexact/budgeted collapse can still be restored and replayed to a successful suffix.

Generic finite-state algorithm:

1. compute suffix feasibility/future signatures backward from the failure;
2. inspect prior collapsed checkpoints from latest to earliest;
3. find the latest checkpoint whose collapsed cell mixed representatives with different suffix feasibility;
4. restore that split and replay.

## 7.3 Deeper-rewind kill

Synthetic checkpoint model:

- stage 1 retains fine alternatives `{a,b}`;
- a budgeted transition keeps only `a`'s successor `a2`;
- `a2` later fails;
- `b2` would reach the goal.

One-step rewind to stage 2 cannot recover `b2`.

Rewind to stage 1 can split `a/b`, replay `b`, and recover.

Measured:

`causal refinement depth = 2`.

## 7.4 HashClash comparison

`cpc.sh` uses timeout and then:

`k := max(k-1,0)` with its specific `k > 1 ? k-1 : 0` boundary.

The source does not compute causal refinement depth.

Therefore the HashClash controller is a **motivating heuristic trace**, not a proof of minimal rewind.

## 7.5 Prior-art boundary

This construction is strongly related to:

- CEGAR;
- conflict-directed backtracking/backjumping;
- nogood learning;
- replay from checkpoints.

The BRC-specific residue is the explicit question:

**which collapsed distinction first became semantically necessary under the declared residual future language?**

## 7.6 T06 verdict

Keep `brc_refine_backtrack` only for **inexact/budgeted BRC** and clearly mark the prior-art roots.

---

# 8. R022-T07 — graded recoalescence potential

Chosen-prefix collision methods provide highly structured, cryptography-specific difference measures.

The generic BRC hypothesis asks for a potential `d(b1,b2)` that reliably measures approach to safe recoalescence.

## 8.1 Exact defect object

For finite declared residual language `U_t`, define:

`Delta_U(b1,b2) = { u in U_t : Supp_t(b1,u) != Supp_t(b2,u) }`.

Then

`|Delta_U| = 0`

iff the branches are future-equivalent for the declared support semantics.

This is exact.

But computing it is essentially the future-equivalence problem itself, and there is no general reason for it to decrease monotonically under arbitrary branch-local operations.

## 8.2 Misleading-metric kill

Synthetic witness:

- a coarse geometric distance falls from 2 to 1;
- exact future-support symmetric difference rises from 0 to 2.

Thus “closer in state space” can mean “farther from semantic recoalescence.”

## 8.3 T07 verdict

**Kill `Recoalescence Potential Scheduler` as a generic theorem-strength primitive.**

Retain only:

- problem-specific heuristics;
- or an exact finite diagnostic oracle based on residual future-signature defect.

No generic monotone scalar was found.

---

# 9. R022-T08 — adaptive branch budget and Pareto economics

The correct comparison must charge:

- static transition/table storage;
- branch-token metadata;
- full retained payload/context;
- peak live branch width;
- cumulative work;
- connector/join work;
- execution/critical depth;
- precomputation;
- replay/rewind;
- multiplicity/provenance overhead if required.

## 9.1 NFA/DFA exact Pareto witness

Generic language:

**“the 6th symbol from the end is 1.”**

A standard nondeterministic presentation uses 7 NFA states.

Exact exhaustive determinization/minimization gives 64 DFA states.

Measured:

- NFA states: 7;
- nonempty NFA transition cells: 12;
- max live NFA branch width: 7;
- branch token bits each: 3;
- worst simple live token bits: 21;
- minimal DFA states: 64;
- DFA transition cells: 128;
- runtime DFA state token: 6 bits;
- static state ratio: `64/7 ~= 9.14`;
- static transition-cell ratio: `128/12 ~= 10.67`.

This is a real Pareto frontier:

- branching form: far smaller static machine;
- deterministic form: smaller live runtime state and less per-symbol branch work.

It is not a universal dominance result.

And the phenomenon is standard NFA-vs-DFA succinctness, not new BRC mathematics.

## 9.2 Bidirectional branch-budget witness

20-variable exact checksum model, 17-bit join interface.

For split `s`, charge:

- forward width `2^s`;
- backward width `2^(20-s)`;
- total branch work = sum of the two frontiers;
- interface metadata = total frontier × 17 bits;
- ideal parallel critical depth = `max(s,20-s)+1`.

Balanced optimum:

`s = 10`

with:

- forward width: 1024;
- backward width: 1024;
- max width: 1024;
- total frontier/work: 2048;
- charged interface metadata: 34,816 bits;
- idealized critical depth: 11.

At split 0 or 20, max width is 1,048,576 and charged interface metadata is 17,825,809 bits.

## 9.3 R021 implication

R021's “minimal branch width” should admit a bidirectional interface version:

`min_{t,I_t exact} Objective(W_F(t), W_B(t), |I_t|, JoinWork_t, Depth_t, Replay_t)`.

A simple width objective is:

`min max(W_F(t), W_B(t))`

subject to exact interface semantics, but a realistic optimizer must also charge interface token bits and join work.

## 9.4 T08 verdict

Keep **Adaptive Branch Budgeter (ABB)** as a resource optimizer.

Its novelty is not the Pareto principle; the Enterprise Math value is enforcing exact semantic constraints and preventing hidden metadata from being omitted.

---

# 10. R022-T09 — bounded reconstruction experiments

Artifacts:

- `experiments/r022_brc_synthetic.py`
- `tests/test_r022_brc_synthetic.py`
- `experiments/r022_brc_synthetic_results.json`

All models are non-cryptographic.

## 10.1 Test inventory

1. md5collgen-shaped five-way router;
2. every-route-bit deletion mutation;
3. nonunique minimal solver-router counterexample;
4. exact residual-state recoalescence;
5. current-output-only unsafe merge;
6. endpoint-equality/provenance mismatch;
7. partial neutral-move composition failure;
8. causal rewind requiring depth > 1;
9. misleading recoalescence distance;
10. NFA-vs-DFA Pareto witness;
11. bidirectional exact-interface MITM witness;
12. branch-budget split accounting.

The test module contains 12 focused unit tests and the experiment script runs a self-test before emitting JSON.

## 10.2 Reproducibility

Command:

`python experiments/r022_brc_synthetic.py`

Tests:

`python -m unittest -v tests/test_r022_brc_synthetic.py`

Local research run completed with all tests passing.

---

# 11. R022-T10 — candidate generic tools

## 11.1 `branch_signature_router`

**Status: KEEP**

Contract:

Given finite fine states, a family of continuation correctness domains, and an allowed signature representation class:

- find/test an exact router;
- minimize route labels or permitted features;
- emit deletion witnesses for each claimed necessary feature.

Failure modes:

- route signature correct but payload omitted;
- minimality only within a restricted coordinate family;
- solver routing mistaken for semantic future quotient.

## 11.2 `brc_connect`

**Status: KEEP**

Contract:

Construct forward/backward branch cones and connect them through a declared exact residual interface.

Required output:

- interface semantics;
- compatibility relation;
- token cost;
- connection support;
- optional RCCs for internal branch merging.

Failure mode:

Endpoint equality or partial residual equality produces a spurious connection.

## 11.3 `safe_neutral_moves`

**Status: KEEP, GUARDED**

Contract:

For partial operations and a branch/interface invariant:

- enumerate or verify operations that preserve the invariant on their legal domains;
- verify domain/codomain compatibility before composition.

Failure mode:

safe single moves are treated as a globally closed monoid.

## 11.4 `brc_refine_backtrack`

**Status: KEEP ONLY FOR INEXACT/BUDGETED MODE**

Contract:

Given a failed execution and checkpoint history, find the latest checkpoint where a discarded distinction separates suffix-feasible from suffix-infeasible representatives.

Output:

- causal checkpoint;
- distinction to restore;
- causal refinement depth;
- replay suffix.

Failure mode:

a fixed one-step rollback is reported as causal-minimal.

## 11.5 `recoalescence_potential`

**Status: KILL AS GENERIC SCHEDULER**

Only retain exact finite diagnostic:

`future_signature_defect`.

No generic monotone scalar survived.

## 11.6 `branch_budget_optimizer`

**Status: KEEP**

Contract:

Optimize declared storage/work/depth objectives subject to exactness.

Must charge:

- token bits;
- branch count;
- retained context/payload;
- join structures;
- replay;
- table/precompute storage.

## 11.7 New extracted primitive: `no_completion_cone_certificate`

**Status: KEEP AS ENTERPRISE MATH CERTIFICATE TYPE**

Contract:

Given `(context, stage, residual prefix signature)`, certify that every represented branch has empty completion support for the declared suffix language.

This allows a compiler/runtime to skip an entire homologous branch cone.

Prior-art note:

The algorithmic idea is not new; it is strongly rooted in nogood recording / memoized failure / prefix pruning. The reusable Enterprise Math contribution is the explicit semantic certificate type paired with RCC.

---

# 12. R022-T11 — kill-test matrix

| Kill test | Result | Consequence |
|---|---|---|
| remove one md5collgen raw route bit | every one of 9 removals fails | raw-coordinate minimum is 9 |
| add irrelevant route metadata | correctness unchanged, storage increases | metadata must be charged |
| merge same current coarse output with different residual constraints | creates `spurious` support | current output is not RCC |
| equal endpoint but provenance observable | loses A/B distinction | merge semantics must name observable |
| safe partial moves composed without domain guard | composition undefined | no generic monoid |
| one-step rewind after earlier information loss | cannot recover | causal depth may exceed 1 |
| coarse distance decreases while future defect increases | witnessed | generic RPS killed |
| residual history compression compared to deterministic quotient | 4096 histories -> 5 tokens, but quotient also 5 | safe merge alone gives no BRC advantage |
| bidirectional 20-var split | 512x enumeration reduction | standard MITM, no novelty |
| NFA vs DFA storage comparison | 7 vs 64 states | real Pareto, standard automata phenomenon |
| charge join token bits | balanced split still best in model | interface metadata does not erase this synthetic MITM frontier |

Negative results are retained as part of the task output.

---

# 13. R022-T12 — prior-art/rooting table

| R022 object | Closest established area | R022 classification |
|---|---|---|
| BSR solver-domain routing | classifier/decision tree/feature selection; set cover | reusable contract, not new algorithm |
| residual connector state | dynamic programming / finite-state memoization | genuine BRC witness, known computational pattern |
| exact token merge | DFA state semantics / bisimulation / Myhill-Nerode-style future equivalence | R021-aligned semantic core |
| forward/backward cones | meet-in-the-middle / bidirectional search | not novel |
| HashClash failure-prefix skip | nogood recording / memoized failure / prefix pruning | useful NCC certificate, not new search principle |
| causal refinement controller | CEGAR / backtracking / conflict-directed refinement | BRC-specific checkpoint semantics only |
| tunnel/neutral move abstraction | message modification / local search freedoms / guarded transformations | specialized source inspiration |
| branch-budget optimization | Pareto optimization / automata succinctness / bounded search | standard optimization, exactness accounting is project-specific |
| recoalescence potential | heuristic distance / abstract defect measures | generic monotone form not found |

Primary references used for rooting include:

- Marc Stevens, Arjen Lenstra, Benne de Weger, chosen-prefix collision work for MD5 and HashClash source/project materials;
- Marc Stevens' thesis/work on MD5 collision-finding tunnels;
- Clarke, Grumberg, Jha, Lu, Veith, Counterexample-Guided Abstraction Refinement;
- Schiex and Verfaillie, nogood recording for static/dynamic constraint satisfaction;
- classical automata future-equivalence/determinization concepts already listed in R021.

No theorem in this report relies on novelty of those established mechanisms.

---

# 14. The dual certificate view

R022 suggests one compact extension to R021.

BRC runtime reasoning naturally uses two dual certificate families.

## Positive certificate

**Recoalescence Congruence Certificate (RCC)**

Meaning:

`these histories may forget their past and share one future token`.

Semantic shape:

`equal certified residual signature -> equal declared residual support`.

## Negative certificate

**No-Completion Cone Certificate (NCC)**

Meaning:

`every branch with this residual-prefix signature has empty completion support in this context`.

Semantic shape:

`certified residual signature -> empty declared residual support`.

These are dual uses of future information:

- RCC identifies multiple histories because their futures are equivalent;
- NCC discards a whole class because its future is empty.

HashClash contains concrete local witnesses of both:

- exact duplicate connector states -> positive merge;
- failure-prefix equivalence -> negative pruning.

The pair is more useful to Enterprise Math than the loose analogy “HashClash is parallel branching.”

---

# 15. BRC compiler primitive sketch

A generic finite-state BRC compiler/runtime can expose:

1. `route(state) -> branch_signature`
2. `split(token, op) -> child_tokens`
3. `step(token, op) -> token/support`
4. `connect(forward_token, backward_token, interface) -> support`
5. `recoalesce(tokens, RCC) -> token`
6. `prune(tokens, NCC) -> remaining_tokens`
7. `neutral_move(token, move, domain_certificate) -> token`
8. `rewind(failure, checkpoints) -> refinement_point`
9. `budget(frontiers, token_costs, work, depth) -> policy`

Correctness rule:

No compiler optimization may change declared final result support.

If multiplicity/provenance/score is required, the certificate semantics must be strengthened before the optimization is legal.

---

# 16. Exact answer to the taskbook's central questions

## What hidden fine worlds are saved together?

- md5collgen: the route token groups many IVs only for **continuation selection**, while retaining the IV payload.
- HashClash forward/backward: differential paths represent sets/constraints over many fine bit assignments.
- HashClash connector: many bitcondition histories can reach the same six-word residual connector state and be forgotten for feasibility processing.

## What future operation forces a split?

Any next operation for which the current branch token does not have a single exact successor-support signature.

In HashClash's connector, each next bit calls `connectbits`, which may branch because current residual constraints admit multiple compatible bitcondition continuations.

## What is the least branch token?

It is always relative to a declared semantics and representation class.

- md5collgen raw-coordinate route: 9 physical bits in the bounded source-shaped model.
- md5collgen compiled control label: 5 labels / 3 fixed bits.
- HashClash connector: six 32-bit residual words are source-sufficient under fixed context; actual minimality is not proved.
- generic exact token: a class of residual future-equivalence.

## Which operations are free inside a branch?

Only partial operations proven to preserve the branch/interface invariant on their legal domains. HashClash tunnel-like freedoms motivate this, but the generic structure is domain-guarded and not necessarily closed under arbitrary composition.

## What lets histories permanently forget the past?

An RCC: a proof that the retained residual token is future-complete for the declared semantics under the fixed context.

HashClash's exact duplicate `connect_bitdata` merge is a concrete local instance.

## After failure, what is the earliest distinction to restore?

For exact BRC: none should be needed due solely to an exact merge.

For inexact/budgeted BRC: restore the latest earlier distinction whose representatives have different suffix feasibility and where a discarded representative enables a valid continuation. The distance is causal refinement depth.

HashClash's script does not compute this; it uses fixed one-stage timeout backtracking.

---

# 17. Did md5collgen/HashClash reveal a new Enterprise Math BRC tool?

**Yes, but only in a carefully limited sense.**

They revealed a useful **Enterprise Math BRC tool surface**:

`BSR + typed residual BRC-Connect + RCC/NCC certificates + guarded local moves + causal-refinement controller + metadata-aware branch budgeter`.

The semantic contract is:

> Preserve the declared final result-support exactly by carrying only context-relative residual information proven sufficient for the remaining future language; split only when the next operation distinguishes represented worlds; recoalesce only under an RCC; prune only under an NCC; and charge every branch token, retained context and replay/join cost in resource comparisons.

However:

- the underlying bidirectional search is MITM;
- the positive state merge is finite-state memoization/dynamic programming/future equivalence;
- the negative failure certificate is nogood/prefix-pruning-like;
- causal refinement is CEGAR/backtracking-like;
- the clean Pareto example is NFA-vs-DFA succinctness.

Therefore R022 does **not** claim a new generic computer-science algorithm.

What is new/useful inside Enterprise Math is the **unified collapse calculus and certificate boundary** that lets R021 state exactly which of these external mechanisms can be transplanted without semantic cheating.

---

# 18. Recommended R021 updates

1. Separate **control signature** from **continuation payload** in branch-token accounting.
2. Add solver-domain BSR as a distinct problem from future-equivalence minimization.
3. Add **context-relative residual token** as a first-class branch carrier.
4. Add **RCC** positive merge certificates.
5. Add **NCC** negative empty-future certificates.
6. Generalize minimal branch width to a **bidirectional/interface-cost** optimization.
7. Type branch-local safe operations as partial/domain-guarded transformations, not automatically a monoid.
8. Restrict causal rewind to approximate/budgeted/change-of-language settings.
9. Kill generic scalar recoalescence-potential claims unless monotonicity is proved for the specific system.
10. Keep NFA/DFA, MITM, CEGAR and nogood roots explicit so BRC is not marketed as renaming established algorithms.

See `research/R022_TO_R021_FEEDBACK.md` for the dedicated handoff.

---

# 19. Validation status

Local bounded research execution:

- experiment script self-test: PASS
- focused unit tests: 12/12 PASS
- source revisions: fixed as taskbook requires
- operational collision attack: NOT RUN / NOT NEEDED
- canonical theorem/tool promotion: NOT DONE
- shared research surface mutation: NOT DONE
- R021 feedback: READY

File digests from the research run:

- `r022_brc_synthetic.py`:
  `3aff4eeb88cc5f4c4381e7e169a042f7077014bd53fdc91c7b27666b7f584d48`
- `test_r022_brc_synthetic.py`:
  `26ba191d039dcbf52c9a63ebc46a4bbcc54a1c63b6196fac250e776304b391b9`
- `r022_brc_synthetic_results.json`:
  `4cc1995e16b816dd58dda8de0d1b7ab13c5e8dc0c6d7c15cf7f779dc064f008e`

---

# 20. Return classification

`BRC_TRANSFER_PRIMITIVES_FOUND / EXACT_BUT_SPECIALIZED / PARTIAL_TOOL_VALUE / R021_FEEDBACK_READY / NOT_CANONICAL`
