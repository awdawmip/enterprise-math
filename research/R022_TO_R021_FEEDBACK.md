# R022 to R021 Feedback — Branch-Recoalescence Collapse Tool Mining

**From:** EM-R022-HC7B4A / RS-R022-HASHCLASH-BRC-TOOL-MINING  
**To:** R021 Branching Collapse Tool Calculus  
**Status:** RESEARCH FEEDBACK / NOT CANONICAL  
**R022 taskbook:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`

## Executive recommendation

R022 recommends that R021 keep the Branch-Recoalescence Collapse program, but sharpen it around **typed residual certificates** rather than around the visual metaphor of many branches.

The strongest source-backed addition is a dual certificate calculus:

- **RCC — Recoalescence Congruence Certificate:** positive certificate that histories may forget their past and share one residual future token.
- **NCC — No-Completion Cone Certificate:** negative certificate that an entire residual-prefix class has empty completion support and may be pruned.

HashClash contains local implementation witnesses of both.

At the same time, R022 found no reason to claim that BRC is a new generic search algorithm. The external structures substantially root to standard automata, dynamic programming/state memoization, meet-in-the-middle, nogood pruning, backtracking and CEGAR.

---

## 1. Which R021 branch carrier best matches md5collgen?

**Answer: branch-token refinement over a retained fine payload.**

md5collgen's dispatcher computes a small continuation-control label from a larger IV and then passes the IV into the selected specialized solver.

So the correct carrier is not:

`small token replaces fine state`.

It is:

`(retained continuation payload, small branch-control token)`.

R021 should therefore distinguish at least:

1. **control signature bits**
2. **payload/context bits**
3. **denotation/support metadata**

in branch-storage accounting.

The source-shaped finite model found:

- 9 route-relevant physical IV bits;
- all 9 necessary if the signature must be a raw-coordinate subset;
- 5 compiled route labels;
- 3 fixed-width bits sufficient for the compiled label.

This is an important representation-class distinction.

---

## 2. Which carrier best matches HashClash path populations?

**Answer: constraint-cell/support branching with context-relative residual tokens.**

Forward/backward `differentialpath` objects are partial constraint paths, not literal concrete fine states.

At the connector, the carrier becomes even more compact:

`six-word residual connect token + fixed lower/upper connection context`.

Therefore R021 should add a first-class type:

**context-relative residual branch carrier**

`B = (kappa, t, sigma, denotation_mode)`

where `kappa` is external fixed context and `sigma` is the live residual state.

A token-size claim is invalid unless the cost of `kappa` is accounted for somewhere.

---

## 3. What is genuine safe recoalescence versus only search convergence?

**Genuine safe recoalescence:**

HashClash `md5_connect_bits` expands possible connector states one bit at a time and then sorts and removes exact duplicate six-word `connect_bitdata` states.

Under the same lower/upper path and connection context, the remaining connector computation uses that residual state. Thus duplicate states have the same remaining feasibility continuation.

This is a source-backed local RCC for final-support/existence semantics.

**Not automatically safe:**

- same current endpoint;
- same coarse output;
- same hash-like distance;
- same partial path score;
- two branches merely meeting at a visually identical node.

R021 should distinguish:

1. exact union bookkeeping;
2. token-identification/forgetting.

Only the second needs a future-congruence certificate and creates a real semantic compression claim.

---

## 4. Are branch tokens materially smaller than deterministic future-complete states?

**Sometimes, but R022 found no universal theorem.**

Negative witness:

A 12-step binary residual system has 4096 hidden histories that safely collapse to at most 5 residual tokens. However the optimal deterministic future-complete quotient also has exactly 5 states.

Therefore:

`history compression != advantage over deterministic refinement`.

Positive Pareto witness:

For the language “6th symbol from the end is 1”:

- NFA presentation: 7 states;
- minimal DFA: 64 states;
- NFA max live width: 7.

This gives a real static-storage vs runtime-work Pareto frontier, but it is standard NFA/DFA succinctness.

Recommendation:

R021 should not seek a theorem “branching is smaller.” It should seek **regime conditions** under which a nondeterministic/contextual presentation is Pareto-preferred after all metadata is charged.

---

## 5. Does bidirectional connection change R021's minimal-width problem?

**Yes.**

R021 currently frames minimal branching width primarily as a one-directional runtime problem.

HashClash motivates a dual-frontier objective:

`min_{t,I_t exact} Objective(W_F(t), W_B(t), |I_t|, JoinWork_t, Depth_t, Replay_t)`.

At minimum, expose:

- forward width;
- backward width;
- max of the two;
- sum of the two;
- interface-token bits;
- join-index/table storage;
- join work;
- parallel critical depth.

Synthetic 20-variable exact checksum model:

- one-sided complete enumeration: 1,048,576 assignments;
- balanced split: 1024 + 1024 frontier assignments;
- exact interface: 17 bits;
- charged interface token bits at balanced frontier: 34,816;
- idealized critical depth: 11 vs 20;
- 512x enumeration-work ratio.

This is ordinary MITM, but it demonstrates that **minimal branch width in a BRC compiler must be interface-aware and bidirectional**.

---

## 6. Do local neutral moves enlarge the safe-operation language?

**Yes, locally and conditionally.**

HashClash tunnel/neutral freedoms motivate operations that vary hidden fine details while preserving an earlier branch/path invariant.

Generic R021 formulation:

A partial move `n` is safe on branch `b` only over a legal domain and only if it preserves the declared branch/interface signature or maps to a known equivalent signature.

Do not assume closure.

Kill test:

two partial moves can each be safe on their own domains while their composition is undefined because the first move exits the second move's domain.

Recommendation:

Represent branch-local safe moves as a **domain-guarded partial transformation category/semigroupoid**, not automatically a monoid.

---

## 7. Does backtracking suggest a new notion of causal refinement depth?

**Yes as a useful R021 diagnostic, but not as source-proved novelty.**

Define:

**causal refinement depth**

= the number of checkpoints one must rewind to reach the latest earlier point where an inexact/budgeted collapse discarded a distinction that separates suffix-feasible from suffix-infeasible representatives.

Synthetic kill test requires depth 2; one-step rewind cannot recover a discarded feasible representative.

Important exactness boundary:

If an earlier RCC was genuinely exact for the same declared future language, that merge cannot later cause a support failure. Therefore causal rewind belongs to:

- budgeted/inexact collapse;
- heuristic branch pruning;
- changed future language;
- stronger late observables such as provenance/score.

HashClash `cpc.sh` uses timeout-driven one-stage rollback and does not compute causal depth.

Prior-art root is CEGAR/backtracking/backjumping/nogood learning.

---

## 8. Which candidate tools deserve a shared theorem/tool surface?

### Promote as candidate generic interfaces

#### A. `branch_signature_router`

Purpose:
compile/test a small continuation-control signature.

Required contract:
correctness domains + allowed signature representation class + minimality witness.

Add explicit storage fields:
control bits vs payload/context bits.

#### B. `brc_connect`

Purpose:
connect forward/backward branch cones through an exact residual interface.

Required contract:
interface semantics + compatibility + token cost + result-support exactness.

#### C. `recoalescence_certificate`

Purpose:
validate token-identification merges.

Suggested object:

`RCC(stage, context, semantics, residual_language, signature, proof)`

#### D. `no_completion_cone_certificate`

Purpose:
prune a whole branch-equivalence class known to have empty residual completion support.

Suggested object:

`NCC(stage, context, failure_depth, prefix_signature, dependency_mask, proof)`

#### E. `safe_neutral_moves`

Purpose:
enumerate/verify domain-guarded invariant-preserving partial moves.

Do not export a monoid theorem without extra closure assumptions.

#### F. `brc_refine_backtrack`

Purpose:
for inexact/budgeted execution only, locate the latest recoverable lost distinction and report causal refinement depth.

#### G. `branch_budget_optimizer`

Purpose:
optimize width/storage/work/depth under exactness and complete metadata accounting.

### Do not promote as generic theorem-strength surface

#### `recoalescence_potential`

No generic monotone scalar survived.

At most keep:

`future_signature_defect`

as a finite diagnostic oracle.

---

## 9. Which attractive analogies were killed?

### Killed: “md5collgen compresses the full IV to 3 bits.”

False. It compresses routing control; the selected solver still receives the IV payload.

### Killed: “safe recoalescence means two branches reach the same current output.”

False. Same coarse output can re-expand to spurious fine states.

### Killed: “same endpoint is enough for BRC-Connect.”

False when hidden residual constraints or provenance remain future-observable.

### Killed: “HashClash backtracking is causal rewind.”

False. The script performs a timeout-triggered fixed rollback.

### Killed: “tunnel/neutral operations form a safe monoid.”

False without domain/codomain closure.

### Killed: “near-collision distance is a generic recoalescence potential.”

False. A simple finite model makes geometric distance decrease while exact future-signature defect increases.

### Killed: “history collapse proves branching is better than deterministic refinement.”

False. A 4096-history model collapses to five residual tokens, but its deterministic future-complete quotient also has five states.

### Killed: “HashClash bidirectional gains establish new BRC search complexity.”

False. The generic gain is meet-in-the-middle.

### Killed: “failure-prefix pruning is a novel algorithm.”

False as an algorithmic novelty claim. It is close to nogood/memoized failure/prefix pruning.

The useful R021 extraction is the **typed NCC semantic certificate**.

---

# Proposed R021 theorem/certificate additions

## A. Router correctness-domain theorem

For continuation algorithms `{A_a}` with correctness domains `{D_a}`, a router `(sigma,alpha)` is correct iff every router fibre lies inside the selected algorithm's domain.

Minimum distinct algorithm labels reduce to a minimum cover of the fine state set by correctness domains.

Consequence:

minimal solver routing need not equal semantic future-equivalence and need not be unique.

## B. RCC theorem schema

Let `sigma_t` satisfy:

`sig(x)=sig(y) => Supp_t(x,u)=Supp_t(y,u)` for all declared residual futures `u`.

Then token-identification of histories with the same signature is exact for final result-support.

Strengthen the condition when multiplicity/provenance/score is observed.

## C. NCC theorem schema

Let prefix signature `pi` under context `kappa` satisfy:

`pi(x)=p => Supp_t(x,u)=empty` for every allowed residual future `u`.

Then every branch in that certified signature class may be pruned.

## D. Exact-BRC no-rewind corollary

If an RCC is exact for a fixed declared residual language and no additional heuristic pruning occurs, a later failure cannot be repaired merely by separating histories that were merged under that RCC.

Any needed rewind implies:

- earlier inexactness;
- changed semantics/language;
- or some other non-exact resource decision.

This should prevent causal-rewind reasoning from being incorrectly used to patch an allegedly exact merge.

---

# Suggested R021 implementation delta

1. Add `context_cost` to branch-token cost records.
2. Add `semantics = support | multiplicity | provenance | score`.
3. Split merge operation into:
   - `union_exact`
   - `identify_with_rcc`
4. Add negative `prune_with_ncc`.
5. Add bidirectional resource fields:
   - `W_forward`
   - `W_backward`
   - `interface_bits`
   - `join_work`
6. Add `causal_refinement_depth` only to approximate/budgeted executions.
7. Require all “minimal signature” claims to state the allowed encoding family:
   - raw coordinate subset;
   - arbitrary compiled label;
   - algebraic/compressed encoding.
8. Keep novelty labels separate:
   - source witness;
   - Enterprise Math abstraction;
   - established prior-art root;
   - actually new theorem, if any.

---

# Final R021 handoff

**What survived:**  
A coherent BRC certificate/tool calculus with source witnesses.

**What did not survive:**  
A claim that md5collgen/HashClash contain a previously unknown generic branching algorithm.

**Most valuable new R021 distinction:**  

`positive future-equivalence certificate (RCC)`  
versus  
`negative empty-future certificate (NCC)`.

Together they give a clean algebra of:

`split -> execute -> recoalesce or prune -> connect -> (if approximate) causally refine`.

**Recommended R022 classification:**  
`BRC_TRANSFER_PRIMITIVES_FOUND / EXACT_BUT_SPECIALIZED / PARTIAL_TOOL_VALUE / R021_FEEDBACK_READY / NOT_CANONICAL`
