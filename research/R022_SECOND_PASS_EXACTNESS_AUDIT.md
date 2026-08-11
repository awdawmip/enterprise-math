# R022 Second-Pass Exactness Audit — Context-Scoped Certificates and Budget Semantics

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `SECOND_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

This addendum pressure-tests the first R022 return rather than replacing it. The first-pass classification remains:

`BRC_TRANSFER_PRIMITIVES_FOUND / EXACT_BUT_SPECIALIZED / PARTIAL_TOOL_VALUE / R021_FEEDBACK_READY / NOT_CANONICAL`.

The second pass adds two sharpenings:

1. HashClash must be split into **exact local reduction**, **completeness-neutral structure**, and **heuristic/budgeted truncation**. The source does not justify treating all branch-budget knobs as exact BRC.
2. The negative No-Completion Cone Certificate (NCC) is more accurately a **context-scoped certificate with a dependency footprint and invalidation rule**. HashClash already implements this pattern when it reuses or invalidates cached lower-path failures across changing upper paths.

No operational collision attack was run. All new executable evidence is a generic finite-state synthetic model.

---

## 1. Source exactness stratification

R022 should not classify the whole HashClash pipeline under one semantic label. The locked source contains at least three distinct kinds of operation.

### 1.1 Exact local reduction under a fixed context

#### A. Connector duplicate elimination

Source:

- `src/md5connect/main.hpp::connect_bitdata`
- `src/md5connect/connect.cpp::md5_connect_bits`

For one fixed lower path, upper path, stage `t`, bit index and MD5 difference context, the connector expands a set of six-word residual states and then applies exact duplicate elimination (`sort` followed by `unique`). Subsequent bit processing depends on the surviving residual state plus that fixed context.

Therefore duplicate elimination is a genuine local BRC recoalescence for **existence/final-support semantics** of the connector. It intentionally does not preserve multiplicity or path provenance.

#### B. Context-scoped failure-prefix reuse

Source:

- `src/md5connect/connect.cpp::md5_connect`
- `src/md5connect/connect.cpp::md5_connect_bits`
- `src/md5connect/connect.cpp::connectbits2`
- `src/md5connect/main.hpp::binary_search_lower_paths`

When connection fails at bit `b`, the implementation can mark later lower paths as already bad when they share the required lower-path prefix characteristics and the relevant `dF` prefixes. This is not a context-free nogood. The cache is reused across upper paths only while the new upper path remains equal far enough (`bequal`) and the relevant residual prefixes still agree; otherwise `isgood` is invalidated.

This is the source pattern behind the strengthened certificate proposed below.

### 1.2 Completeness-neutral structure, before truncation

The following operations can reorganize work without changing final support **provided all generated branches are retained or eventually replayed**:

- forward/backward decomposition;
- bidirectional connection through an exact interface;
- thread-level parallelism;
- ordering/grouping branches for cache reuse.

The speedup from the split remains ordinary meet-in-the-middle / separator-style dynamic programming. BRC adds typed interface semantics and certificate accounting, not a new bidirectional complexity theorem.

### 1.3 Not exact without an additional certificate or replay guarantee

The locked source also contains aggressive resource controls:

- `src/md5forward/main.hpp::path_container_autobalance` uses `ubound`, `maxcond`, condition estimates and tunnel thresholds to limit stored path populations;
- `src/md5backward/main.hpp::path_container_autobalance` similarly limits backward populations;
- `src/md5connect/main.hpp::path_container::push_back` keeps path candidates according to best-condition/tunnel/completeness scores;
- `scripts/cpc.sh::doconnect` kills a connection phase after a resource/time threshold;
- `scripts/cpc.sh::auto_kill` terminates a near-collision attempt after the configured timeout;
- the outer script then uses a fixed `k -> max(k-1,0)` backtrack.

These mechanisms are excellent engineering for finding a collision, but **they are not by themselves exact final-support transformations**. A branch-width cap or score cutoff can discard the only representative carrying a future result.

Therefore R022/R021 must not cite HashClash's width controls as source evidence that an exact Adaptive Branch Budgeter may arbitrarily drop branches.

The exact rule is:

> A budget decision may discard a live branch only when the discard is justified by an exact empty-future certificate, an exact dominance certificate for the declared observable, or a replay/checkpoint contract that keeps the discarded distinction recoverable and charges the expected recomputation.

Otherwise the execution mode is heuristic/approximate.

---

## 2. Context-Scoped No-Completion Cone Certificate (CS-NCC)

The first-pass NCC was:

`NCC(stage, context, failure_depth, prefix_signature, dependency_mask, proof)`.

The source audit suggests making the context dependence operational rather than descriptive.

### 2.1 Certificate schema

Define a connector-prefix dependency footprint

`delta_b(branch, context)`

that contains exactly the data on which connector feasibility through failure depth `b` depends.

A **Context-Scoped NCC** is:

`CSNCC = (stage, b, delta_value, semantics, proof_of_empty_completion)`.

It has two operations:

1. `reuse(candidate, context')` iff `delta_b(candidate,context') = delta_value`;
2. `invalidate` whenever the dependency footprint no longer matches.

### 2.2 Exact reuse theorem schema

Assume connector prefix execution through depth `b` factors through `delta_b`:

`delta_b(x,kappa) = delta_b(y,lambda)`

implies identical reachable connector-state sets after every prefix step through `b`.

If the reachable connector-state set is empty at depth `b` for one representative of a footprint class, then it is empty at depth `b` for every representative in that class.

Hence the whole class can be pruned for that connector context.

This is simply factorization of failure through a sufficient dependency footprint; it is not a new generic nogood-learning theorem. Its BRC value is to make **negative branch-cone compression** symmetric with positive RCC recoalescence.

### 2.3 HashClash instantiation

`md5_connect` already behaves like a dependency-footprint cache:

- `isgood[i]` remembers the failure depth for a lower path;
- `bequal` measures how much of the new upper path is unchanged from the previous one;
- `dFt`, `dFtp1`, `dFtp2`, `dFtp3` are masked to the failure prefix;
- `lastdFp1/2/3` records which residual components actually participated in the failing bit;
- a cached failure survives only when the new context agrees on the necessary prefix data.

So the source contains not merely an NCC, but an **NCC validity-region/invalidation mechanism**.

---

## 3. New synthetic kill tests

New generic artifacts:

- `experiments/r022_brc_certificate_audit.py`
- `experiments/r022_brc_certificate_audit_results.json`
- `tests/test_r022_brc_certificate_audit.py`

Focused result: **4/4 tests pass** under Python 3.13 in the second-pass execution environment.

### 3.1 Certificate reuse over a branch class

The finite connector has 1024 lower branches.

A failure certificate at depth 4 with dependency footprint

- connector state before failure: `{0}`;
- local lower feature: `(0,1)`;
- local upper feature: `1`

certifies **34 branches** as failing at that same depth.

This demonstrates the intended negative-cone reuse semantics.

### 3.2 Context omission is unsound

A branch that fails at depth 3 under upper context

`(0,1,0,1,1)`

succeeds when only the upper component at the failure depth changes:

`(0,1,0,0,1)`.

Therefore a certificate that stores the lower prefix but omits the relevant context component can false-prune a successful branch.

This is the synthetic analogue of HashClash's `bequal`/prefix invalidation logic.

### 3.3 Width-cap exactness kill

Two live branches carry final supports `{0}` and `{1}`.

An un-certified width cap that keeps only one branch changes exact support from

`{0,1}`

to

`{0}`.

Therefore "choose a branch budget" is not an exact operation by itself.

A branch budgeter must expose one of:

- `EXACT_CERTIFIED_PRUNE`;
- `EXACT_REPLAYABLE`;
- `HEURISTIC_APPROXIMATE`.

---

## 4. Consequence for Adaptive Branch Budgeter

The first-pass ABB survives, but its semantic contract should be strengthened.

### 4.1 Required exactness mode

Every budget action should carry:

`budget_mode ∈ {EXACT, REPLAY_EXACT, HEURISTIC}`.

#### EXACT

Every removed branch has an RCC/NCC/dominance-style certificate proving no declared result support is lost.

#### REPLAY_EXACT

The branch is evicted from live memory but remains recoverable from a charged checkpoint/compact replay description. Storage falls at the price of expected recomputation and rewind depth.

#### HEURISTIC

The branch is genuinely discarded based on rank, score, width, time or probability. Exact final support is no longer claimed.

### 4.2 Revised Pareto accounting

In addition to the existing fields, ABB should charge:

- certificate bytes/token bits;
- dependency-footprint bits;
- certificate cache size;
- invalidation rate;
- checkpoint/replay bytes;
- expected recomputation after eviction;
- semantic mode (`EXACT`, `REPLAY_EXACT`, `HEURISTIC`).

This prevents HashClash-style engineering heuristics from being accidentally promoted into exact BRC theorems.

---

## 5. Positive and negative certificate duality

The refined BRC execution algebra is now:

`split -> execute -> {positive merge by RCC | negative prune by CS-NCC | retain distinct} -> connect -> optional replay/refinement`.

### Positive certificate — RCC

`same sufficient residual signature => same declared residual future support`.

Use: identify histories and forget provenance not declared observable.

### Negative certificate — CS-NCC

`same sufficient failure footprint => empty residual completion support`.

Use: discard an entire branch class.

### Why the duality matters

RCC compresses several **successful/live residual worlds into one**.

CS-NCC compresses several **failed residual worlds into zero**.

Both require factorization through a sufficient runtime encoding. Both are context/language/observable relative. Neither may be inferred from current coarse equality alone.

---

## 6. Alignment with R023 semantic Lean core

R023 Draft PR #498 formalized the R021 Boolean/result-support core after the first R022 owner checkpoint.

The second-pass results are compatible with that formalization:

1. **NO_RESURRECTION:** R022's control token, payload, connection context and certificate footprint together belong to the complete runtime encoding. A 3-bit md5collgen route label is not a complete semantic encoder.
2. **ONE_STEP_COARSEST:** uniqueness is a quotient/factorization statement. R022 still permits multiple incomparable coordinate encodings or solver-domain routers when the representation class changes.
3. **SUPPORT_BRANCH_INVARIANT:** exact connector duplicate elimination is an instance of lossless support-preserving branching/recoalescence under its fixed context.
4. **FORGETFUL_RECOALESCENCE_IFF:** RCC remains language/observable relative; R022 does not weaken this.
5. **R022 addition beyond R023's semantic core:** negative empty-future certificates, dependency-footprint cache invalidation, bidirectional interface economics, partial safe operations, causal replay metrics and budget-mode typing belong to the representation/execution layer, not the Boolean semantic theorem core.

No R023 semantic correction is requested by this audit.

---

## 7. Prior-art rooting after the second pass

The novelty boundary remains conservative.

- HashClash chosen-prefix collision/differential-path construction: source phenomenon and cryptanalytic provenance, not BRC novelty.
- Forward/backward cones: meet-in-the-middle / bidirectional search.
- Connector residual-state deduplication: dynamic programming / memoization over a sufficient state.
- Context-scoped failure certificate reuse: nogood recording, dependency-directed backtracking, look-back learning and incremental cache validity are clear prior-art relatives.
- Local refinement after spurious/inexact collapse: CEGAR.
- Storage/work tradeoffs: automata succinctness and elimination-vs-conditioning style time-space tradeoffs.

Primary rooting surfaces already identified by R022 include Marc Stevens' HashClash/chosen-prefix collision materials; Clarke-Grumberg-Jha-Lu-Veith on counterexample-guided abstraction refinement; Stallman-Sussman on dependency-directed backtracking; and Dechter's bucket-elimination/conditioning framework.

The Enterprise Math residue is the **typed certificate/exactness calculus and its accounting discipline**, not a claim of inventing these search paradigms.

---

## 8. Updated R021 feedback delta

Add the following to the first-pass `R022_TO_R021_FEEDBACK.md` packet:

1. Upgrade `NCC` to **context-scoped NCC with dependency footprint and invalidation**.
2. Treat certificate caching as a first-class BRC primitive:
   - positive RCC cache;
   - negative CS-NCC cache;
   - explicit validity region.
3. Add branch-budget semantic mode:
   - `EXACT`;
   - `REPLAY_EXACT`;
   - `HEURISTIC`.
4. Do not use HashClash `ubound/maxcond/tunnel/bestpath/timeout` controls as evidence of exact pruning unless a separate correctness certificate is proved.
5. Charge certificate footprint/cache/invalidation and checkpoint-replay cost in the representation/work/depth Pareto.
6. Keep causal refinement depth outside exact RCC execution; it belongs to approximate/budgeted, changed-language or stronger-observable runs.

---

## 9. Second-pass verdict

The second pass strengthens rather than expands the original R022 claim.

### Survives strongly

- control-vs-semantic branch signature distinction;
- context-relative connector residual state;
- RCC positive recoalescence certificate;
- **CS-NCC negative cone certificate with invalidation**;
- typed BRC-Connect;
- branch-local partial safe operations;
- exact/replay/heuristic budget-mode distinction;
- causal refinement depth as an approximate/replay diagnostic;
- storage/work/depth Pareto accounting.

### Still killed

- generic new search-algorithm novelty;
- unconditional safe-move monoid;
- current-output/endpoint-only recoalescence;
- generic monotone recoalescence potential;
- interpreting HashClash's heuristic width/time controls as exact-support transformations;
- interpreting md5collgen's 3-bit compiled route as a 3-bit semantic state.

### Recommended classification

`BRC_TRANSFER_PRIMITIVES_FOUND / CONTEXT_SCOPED_CERTIFICATE_CALCULUS_SHARPENED / EXACT_VS_HEURISTIC_BUDGET_BOUNDARY_FOUND / R021_FEEDBACK_READY / NOT_CANONICAL`
