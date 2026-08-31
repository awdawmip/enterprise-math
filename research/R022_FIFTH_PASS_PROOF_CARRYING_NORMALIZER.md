# R022 Fifth-Pass Deepening — Proof-Carrying Normalization and Semantic/Carrier Separation

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `FIFTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

The first four passes established source-backed BRC patterns, an exact Boolean/result-support Residual Join Certificate (RJC) algebra, Set-Cover hardness of minimum existing-token Residual Join Basis (RJB), and laminar/prefix structured fast paths.

The fifth pass separates two questions that had remained partially conflated:

> **Is a proposed branch rewrite exact?**

versus

> **Can we find the cheapest exact rewrite?**

For **explicit finite residual-support signatures**, exactness verification is cheap: compute the old configuration join and the proposed configuration join and compare them. The minimum existing-token basis remains Set-Cover hard. Therefore exact BRC does **not** require trusting the optimizer.

This yields a proof-carrying architecture:

`arbitrary proposer -> exact RJC verifier -> accept exact rewrite or retain original configuration`.

A greedy/heuristic proposer may be suboptimal while remaining semantically safe. Unsafe width caps are rejected independently.

The pass also adds three exact structured algorithms:

- a **weighted laminar RJB dynamic program**;
- a **minimum-cardinality interval-signature greedy fast path**, strictly extending laminarity;
- **overlap-component factorization**, which splits a hard RJB problem into independent connected components.

Recommended classification:

`BRC_PROOF_CARRYING_NORMALIZER_FOUND / EXACTNESS_OPTIMALITY_SEPARATED / SEMANTIC_CARRIER_REALIZABILITY_BOUNDARY_CLASSIFIED / WEIGHTED_LAMINAR_DP_EXACT / INTERVAL_RJB_GREEDY_EXACT / OVERLAP_COMPONENT_FACTORIZATION_EXACT / NOT_CANONICAL`.

---

## 1. Boolean residual signatures as an explicit atom universe

For fixed residual language `U` and output set `Y`, flatten a branch residual signature

`phi(b) : U -> P(Y)`

to a subset of the finite atom universe

`A = U x Y`.

Then a configuration `C` has exact final-support semantics

`J(C) = union_{b in C} phi(b) subseteq A`.

For configurations `C,D`, `C => D` is exact for the declared Boolean/final-support semantics iff

`J(C) = J(D)`.

No minimality assumption appears. An exact but nonminimum basis is still exact.

## 2. Exactness–optimality separation

Assume all signatures are explicit finite subsets/bitsets of `A`.

Given a proposed replacement `D`, exactness verification is one materialized join comparison:

`union phi(C) == union phi(D)`.

By contrast, finding

`min |D| subject to union phi(D) = J(C)`

over an admissible existing-token dictionary is the RJB/Set-Cover-hard problem from pass 3.

Therefore exactness checking and optimum compression have sharply different computational roles.

### Proof-carrying normalizer schema

A BRC compressor can be split into:

1. `proposer(C, budget, structure)` — greedy, bounded exhaustive, ILP/SAT, learned ranking, or another heuristic;
2. `rjc_verify(C,D)` — independently checks join equality;
3. accept `D` only if the verifier passes;
4. otherwise retain `C` or fall back to another exact mode.

The proposer need not be trusted for semantic correctness.

### Synthetic witness

Dictionary:

- `{1,2,3,4}`
- `{1,2,5}`
- `{3,4,6}`
- `{5}`
- `{6}`

A standard uncovered-gain greedy proposer returns width **3**. The exact optimum has width **2**, using `{1,2,5}` and `{3,4,6}`. Both joins equal `{1,2,3,4,5,6}`, so the greedy proposal is **exact but suboptimal**. An uncertified truncation of the greedy basis to width 2 fails the RJC verifier.

Heuristic quality affects compression, not correctness.

## 3. Semantic normal form is not an executable branch basis

Because the ambient support algebra is a powerset under union, every target support `z` has the singleton decomposition

`z = union_{a in z} {a}`.

Those singleton atoms are a canonical semantic description of support facts, but they need not be admissible/executable branch carriers. A runtime token may need a realizable fine-state denotation, downstream correlation, continuation interface, context metadata, or reconstruction/checkpoint contract.

Therefore **semantic atoms are a verification basis, not automatically an execution basis**.

### 1 / 2 / 3 representation witness

Target `z={a,b,c}`; existing dictionary `{a,b}`, `{b,c}`.

- arbitrary synthetic token `z` allowed for free: width `1`;
- existing dictionary: minimum width `2`;
- singleton semantic atoms: width `3`.

All three are semantically exact.

Hence there is no intrinsic minimum branch count without an admissible representation class / carrier grammar and cost model.

## 4. Carrier grammar boundary

A useful next abstraction is an admissible carrier grammar `Gamma` containing primitive runtime tokens, allowed constructors, denotation/proof obligations, transition/decoder/reconstruction rules, and charged construction/storage/execution costs.

Then compression asks for a low-cost `Gamma`-realizable expression whose residual join equals the target.

Special cases:

- existing-token-only `Gamma` -> Set-Cover/RJB regime;
- free arbitrary aggregate token -> width trivially 1 and invalid as an uncharged complexity measure;
- singleton semantic atoms only -> canonical semantic representation but not necessarily executable;
- structured constructors -> intermediate regimes requiring their own exactness/cost theorems.

R022 does not claim a generic optimal grammar solver here.

## 5. Weighted laminar RJB dynamic program

Pass 4 proved the unweighted laminar theorem. The weighted case is also exact.

Let `F` be a finite laminar family of nonempty signatures. For duplicate signatures retain the minimum nonnegative token cost `c(S)`. Build the containment forest. For a node `S`, let `children(S)` be its inclusion-maximal proper descendants. Children are pairwise disjoint.

Define `DP(S)` as the minimum cost of covering all atoms of `S` using tokens from its subtree.

If

`union children(S) != S`,

then `S` contains a private atom absent from every proper descendant, so `S` is mandatory:

`DP(S) = c(S)`.

If

`union children(S) = S`,

then either choose `S`, or exclude it and independently cover all disjoint children:

`DP(S) = min(c(S), sum DP(T) for T in children(S))`.

For inclusion-maximal roots `R_i`, total optimum is `sum DP(R_i)` because distinct roots are disjoint.

### Executable evidence

Exhaustive bounded verification:

- all **63** nonempty laminar families on a 3-atom universe;
- every cost assignment in `{1,2,3}`;
- **2,559** weighted instances;
- **0 counterexamples** against brute-force minimum cost.

## 6. Interval residual-signature fast path

Laminarity is not the only tractable overlap geometry.

Suppose the residual atom universe has a fixed total order and every admissible signature is an interval. Intervals may cross, so this class includes non-laminar families.

### Greedy theorem

For minimum-cardinality exact existing-token basis:

1. take the leftmost uncovered target atom `p`;
2. among intervals containing `p`, choose one with farthest right endpoint;
3. mark it covered;
4. repeat.

### Exchange proof

Any exact cover must choose some interval `I` containing the current leftmost uncovered atom `p`. Let `G` be a candidate containing `p` with farthest right endpoint. All atoms left of `p` are already covered. Replacing `I` by `G` cannot reduce coverage of any still-relevant atom up to `I`'s right endpoint, and `G` reaches at least as far right. Thus some optimum can start with `G`; induct.

### Exhaustive evidence

For a 5-atom line there are 15 nonempty intervals. R022 checked all

`2^15 - 1 = 32,767`

nonempty interval dictionaries:

- **32,767** tested;
- **0 counterexamples**.

The crossing family `[0,1]`, `[1,2]` is not laminar, so this is strictly broader than the laminar fast path.

Scope: an explicit atom order must be certified; arbitrary `U x Y` signatures are not assumed interval-shaped.

## 7. Overlap-component factorization

Construct the token intersection graph:

- one vertex per distinct nonempty residual signature;
- edge `S--T` iff `S intersect T != empty`.

Let connected components be `C_1,...,C_r`.

Distinct components have disjoint aggregate atom supports. Therefore the exact basis problem factorizes:

`nu_D(z) = sum_i nu_{C_i}(union C_i)`.

The same additivity holds for nonnegative token costs.

A bounded solver can solve each component independently. If component sizes are `m_i`, naive subset enumeration scales like

`sum_i 2^(m_i)`

rather than `2^(sum_i m_i)`.

This motivates `hard_overlap_component_size = max_i m_i` as a resource parameter.

### Exhaustive evidence

R022 checked all **32,767** nonempty set dictionaries over a 4-atom universe. In every case:

`global minimum cover count = sum(component minimum cover counts)`.

Counterexamples: **0**.

## 8. Revised residual_join_normalizer architecture

1. materialize or otherwise certify residual signatures;
2. remove bottom;
3. hash-cons equal signatures;
4. pairwise dominance;
5. split by overlap connected components;
6. per component:
   - chain/laminar weighted DP when applicable;
   - interval greedy when an interval order is certified;
   - other structural fast paths;
   - bounded exact collective/RJB solver;
   - heuristic proposer only behind exact RJC verification;
7. if live-memory constraints remain:
   - `REPLAY_EXACT`, with charged checkpoint/recomputation;
   - or explicitly `HEURISTIC`.

This separates semantic safety from optimization quality.

## 9. Certificate ladder

R022 recommends several independent exactness mechanisms rather than one monolithic future-signature computation.

- **Materialized RJC:** explicit finite signatures; verify join equality directly.
- **Local congruence RCC:** a local residual token is proved sufficient for the remaining transition context, as in HashClash connector duplicate elimination.
- **Scoped negative certificate:** CS-NCC / cumulative-footprint CRD proves a branch class empty under a validity region.
- **Structural theorem:** laminar, interval, or component decomposition proves an optimizer action exact/minimal without general Set-Cover search.

The external source systems are useful precisely because they often use cheap local sufficient certificates instead of computing a global future signature.

## 10. Important boundary: implicit signatures

The cheap RJC-verification statement is deliberately scoped to **explicit finite residual signatures**.

If `U` is huge, symbolic, adaptive, or only accessible through an expensive reachability solver, materializing `phi(b)` may dominate the problem. Then exact verification may require a local congruence theorem, symbolic proof, compositional certificate, bounded oracle, or other problem-specific reasoning.

R022 does **not** claim that all exact BRC rewrites are cheaply verifiable. It claims that once the relevant residual-support signatures are explicit/materialized, join preservation is easy to verify even though optimal carrier selection is hard.

## 11. Relation to HashClash and md5collgen

No new source novelty claim is made.

- md5collgen remains a control-signature router with retained payload.
- HashClash connector duplicate elimination is an example where a local executable residual token makes equality verification cheap.
- HashClash failure-prefix reuse is an example where a scoped dependency certificate makes negative pruning cheap.
- HashClash budget/ranking heuristics remain heuristic unless separately certified/replayable.

The fifth pass explains why mature source systems can safely use cheap local reductions without solving a global optimum: local exactness certificates and optimization strategy are separate concerns.

## 12. R021 feedback

Recommended additions:

1. Separate `rewrite_exactness` from `basis_optimality`.
2. Add independent `rjc_verify` for explicit finite signatures.
3. Allow heuristic basis proposers only behind exact verification.
4. Distinguish semantic singleton atoms, executable branch tokens, synthesized aggregates, and carrier grammar/construction cost.
5. Add weighted laminar DP.
6. Add interval-signature greedy fast path.
7. Decompose general RJB by token-overlap connected components before bounded exact search.
8. Track `hard_overlap_component_size`, representation class/carrier grammar, proposer width/cost, verifier pass/fail, and optimality status separately from exactness status.

No correction is requested to R023's Boolean/result-support semantic core.

## 13. Fifth-pass classification

`BRC_PROOF_CARRYING_NORMALIZER_FOUND / EXACTNESS_OPTIMALITY_SEPARATED / SEMANTIC_CARRIER_REALIZABILITY_BOUNDARY_CLASSIFIED / WEIGHTED_LAMINAR_DP_EXACT / INTERVAL_RJB_GREEDY_EXACT / OVERLAP_COMPONENT_FACTORIZATION_EXACT / R021_FEEDBACK_READY / NOT_CANONICAL`.

Cumulative picture:

1. BRC is not a novel generic search algorithm;
2. exact Boolean support rewrites form an RJC join algebra;
3. optimum existing-token realization is hard in general;
4. structured overlap/certificate geometries recover exact fast paths;
5. **semantic exactness can be independently verified from optimization quality**, enabling safe proof-carrying branch compression.
