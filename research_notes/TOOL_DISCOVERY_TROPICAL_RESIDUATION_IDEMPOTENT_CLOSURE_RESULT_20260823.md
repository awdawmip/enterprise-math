# Tool Discovery A — Tropical / Residuation / Idempotent Closure Calculus — Result

Researcher-ID: `EM-TDTR-4FFCEA`  
Task-ID: `RS-TD-TR-TROPICAL-RESIDUATION-IDEMPOTENT-CLOSURE-CALCULUS`  
Owner branch: `research/tool-tropical-residuation-idempotent-closure`  
Taskbook source baseline: `c0663825763b33e629394e68066386da93675320`  
Terminal classification: **`NEW_ENTERPRISE_TOOL_INTERFACE`**  
Hard target: **`ENTERPRISE_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_TOOL_CLASSIFIED` — SATISFIED**

## 0. Executive result

The capability gap is real, but it is narrower than “tropical/residuation is new.”

Enterprise Math already owns genuine P008-style order adjunction. Therefore scalar residuation, threshold pullback, and the Galois law by themselves are not new capability. The new reusable layer is:

> **explicitly weighted finite transition/constraint semantics  
> -> idempotent-semiring matrix composition  
> -> fixed-length path envelope  
> -> all-path closure under exact cycle/completeness hypotheses  
> -> improving-cycle obstruction/certificate  
> -> matrix residual inequality solver  
> -> finite Bellman least/greatest fixed-point solver.**

This layer survives mandatory dedup because no current T0–T9 family owns the combination of explicit semiring-valued path composition, all-path closure, and weighted Bellman/fixed-point envelope computation. The residual component is classified as reuse/extension of the P008 adjoint pattern, not as a new theorem.

The mathematical content is classical idempotent-semiring / shortest-longest-path / residuation / finite-lattice fixed-point mathematics. No new classical theorem is claimed. What is new is an Enterprise semantic interface with strict weight provenance, exact failure boundaries, cross-domain reuse, and deterministic certificates.

The strongest justified terminal classification is therefore:

`NEW_ENTERPRISE_TOOL_INTERFACE`

and not `NEW_GLOBAL_TOOL_FAMILY`, because the theorem layer is classical and a substantial subcomponent (residuation) is already owned by P008-style order-adjoint machinery.

## 1. Source and information discipline

Only the taskbook and taskbook-authorized dependency/source surfaces were used.

Exact inputs:

- taskbook: `research_tasks/TOOL_DISCOVERY_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_CALCULUS_20260823.md@c0663825763b33e629394e68066386da93675320`;
- toolbox registry: `enterprise_toolbox_registry.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`;
- method inventory: `research_method_inventory.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`;
- invocation policy: `tool_invocation_policy.json@bd10bc351dbe7c90b47a3ffba3ef7796479170f5`;
- P008 specialization source blob: `src/enterprise_math/material_adjoint.py@3a1962b6fe9e62ada6675143e17c3e6ff0fe2fe0`;
- adjoint threshold-pullback source blob: `src/enterprise_math/adjoint_boundary_precision.py@a1e73b6d97f116cbb1127d1ba08a47a061318897`.

No external literature was used and no unlisted research report was opened.

## 2. Admissible semantic contract

The interface starts only from caller-declared weighted semantics.

Required data:

1. finite state/index sets;
2. a declared directed transition/relation support;
3. a declared weight map `w`;
4. a declared idempotent semiring/dioid-like carrier
   `(S, ⊕, ⊗, 0, 1)`;
5. the meaning of weights: cost, delay, grade, capacity, score, threshold increment, or another caller-supplied semantic;
6. an explicit order convention and infinity/unreachable convention.

Forbidden constructions remain forbidden:

- bare incidence does not generate a weight;
- edge count or path length is not a metric/cost unless declared;
- native addresses do not become numerical scores;
- implementation priority is not mathematical weight;
- path-envelope output does not automatically become probability, amplitude, energy, utility, distance, or geometry.

### 2.1 Canonical order

If `⊕` is idempotent, define

`a ≼ b  iff  a ⊕ b = b`.

This is a partial order in general.

For max-plus `(max,+)`, `≼` is the usual numeric `≤`.

For min-plus `(min,+)`, `≼` is the reverse of the usual numeric order. Thus “larger in the canonical order” means “smaller numerical cost.”

No total-order shortcut is part of the generic interface.

## 3. Classified reusable API

The following interface is justified at the stated levels.

| API | Status | Exact contract |
|---|---|---|
| `VALIDATE_SEMIRING` | ACCEPTED_INTERFACE | Check the declared finite law table exactly, or accept caller-supplied proved laws for non-finite carriers. |
| `WEIGHTED_RELATION` | ACCEPTED_INTERFACE | Build a semiring-valued matrix/operator only from explicit caller weights. |
| `COMPOSE` | ACCEPTED_INTERFACE | Semiring matrix/relation composition. |
| `PATH_VALUE` | ACCEPTED_INTERFACE | `⊗`-product of weights along one declared path. |
| `POWER(k)` | PROVED | `A^k` is the exact envelope of length-`k` paths. |
| `CLOSURE/KLEENE_STAR` | CONDITIONAL | Exact all-path envelope when a finite simple-path reduction or a separately declared complete/star-continuous carrier justifies it. |
| `RESIDUAL_RIGHT` | CONDITIONAL / P008-OVERLAP | Greatest `x` with `A⊗x ≼ b` when the required scalar residuals and finite meets exist. |
| `RESIDUAL_LEFT` | CONDITIONAL / P008-OVERLAP | Greatest `y` with `y⊗A ≼ b` under the dual typed conditions. |
| `BELLMAN_OPERATOR` | ACCEPTED_INTERFACE | Declared monotone operator such as `T(x)=b⊕A⊗x`. |
| `LEAST_FIXED_POINT` | CONDITIONAL | Exact by bottom iteration on a declared finite complete ordered carrier. |
| `GREATEST_FIXED_POINT` | CONDITIONAL | Exact by top iteration on a declared finite complete ordered carrier. |
| `OPTIMAL_PATH_CERT` | AVAILABLE | Predecessor/equality witness from the dynamic recurrence when a finite optimum exists. |
| `UNBOUNDED_CYCLE_CERT` | PROVED/SUPPORTED | Improving cycle plus exact cycle value. |
| `OBSTRUCTION` | REQUIRED | Missing weight semantics/laws/residual/completeness, improving cycle, failed quotient weight descent, etc. |

No production `src/enterprise_math` module is created in this task. The taskbook made it optional; the classification is frozen at the interface/checker level so Driver can decide later whether to integrate it.

## 4. Structural theorem ledger

### TR-1. Idempotent natural order

**Claim.** If `(S,⊕)` is associative, commutative, and idempotent, then
`a≼b iff a⊕b=b` is a partial order.

**Status:** `CLASSICAL / PROVED_FOR_INTERFACE`.

- reflexive: `a⊕a=a`;
- antisymmetric: `a⊕b=b` and `b⊕a=a`; commutativity gives `a=b`;
- transitive: from `a⊕b=b`, `b⊕c=c`,
  `a⊕c=(a⊕b)⊕c=b⊕c=c`.

**Boundary:** without idempotence, this canonical-order construction can fail even reflexivity. Ordinary addition has `1+1=2≠1`.

### TR-2. Matrix power = fixed-length path envelope

Let `A=(a_ij)` be the semiring-valued transition matrix.

**Claim.**

`(A^k)_ij = ⊕_{p:i->j, |p|=k} ⊗_{e in p} w(e)`.

**Status:** `CLASSICAL / EXACTLY CHECKED`.

**Proof.** Induction on `k`. The step from `k` to `k+1` partitions every length-`k+1` path by its penultimate state `r`; distributivity gives the matrix-product recurrence.

Checker coverage:

- min-plus matrices, `k=0..4`;
- max-plus matrices, `k=0..4`;
- all exact integer arithmetic;
- every checked equality matched.

### TR-3. Finite simple-path closure under non-improving cycles

Let `1` denote the multiplicative identity. Suppose every cycle value `c` satisfies

`c ≼ 1`.

This is exactly “non-improving cycle” in the canonical order.

**Claim.** Every walk can have repeated cycles deleted without decreasing its canonical value. Hence on `n` states,

`A* = I ⊕ A ⊕ ... ⊕ A^(n-1)`

for the all-path envelope whenever a finite optimum is sought in this cycle regime.

**Status:** `CLASSICAL / PROVED_FOR_FINITE_PATH SPECIALIZATION / EXACTLY CHECKED`.

**Reason.** If a walk factors as `u · cycle · v`, monotonicity of `⊗` and
`cycle_value ≼ 1` give

`value(u·cycle·v) ≼ value(u·v)`.

Repeated deletion yields a simple path of at most `n-1` edges with value at least as good in canonical order.

Specializations:

- min-plus: every cycle has numerical weight `>=0`;
- max-plus: every cycle has numerical weight `<=0`.

Checker verifies cyclic min-plus and max-plus examples with no improving cycles against exhaustive simple-path enumeration.

### TR-4. Improving-cycle obstruction

If a cycle has value `c ≻ 1`, traversing it repeatedly gives a strictly improving chain in standard min-plus/max-plus specializations.

**Status:** `CLASSICAL / CERTIFICATE INTERFACE ACCEPTED / EXACTLY CHECKED`.

- min-plus example: cycle value `-1`, hence repeated traversal drives cost downward without finite minimum;
- max-plus example: cycle value `+2`, hence repeated traversal drives score upward without finite maximum.

The checker returns the exact cycle

`0 -> 1 -> 2 -> 0`

with the exact improving value.

**Important distinction.** In a separately declared complete idempotent carrier an infinite supremum/infimum may exist as a carrier element. In an incomplete carrier such as integer max-plus without `+∞`, the improving chain has no supremum in the carrier. Therefore the interface must return either a declared completed value or `UNBOUNDED/INCOMPLETE_CARRIER`; it may not silently invent completion.

### TR-5. Matrix residual law

Assume every scalar left multiplication `x -> a⊗x` is residuated and the needed finite meets exist.

Write `a\b` for the greatest scalar `x` satisfying `a⊗x≼b`.

For `A:S^n->S^m`, define

`(A\b)_j = ∧_i (a_ij \ b_i)`.

Then

`A⊗x ≼ b  iff  x ≼ A\b`.

The left residual is analogous:

`y⊗A ≼ b  iff  y ≼ b/A`

with the correctly typed componentwise meet.

**Status:** `CLASSICAL / EXACTLY CHECKED / P008_ORDER_ADJOINT_OVERLAP`.

**Proof.**

`A⊗x≼b`
iff for every `i`,
`⊕_j a_ij⊗x_j ≼ b_i`
iff for every `i,j`,
`a_ij⊗x_j≼b_i`
iff for every `i,j`,
`x_j≼a_ij\b_i`
iff for every `j`,
`x_j≼∧_i(a_ij\b_i)`.

The checker validates all inputs in small finite capped max-plus matrices:

- right residual result `[2,1]`;
- left residual result `[1,3]`;
- exhaustive Galois-law mismatch count `0`.

**Dedup ruling.** This theorem is not new Enterprise mathematics. It is the matrix/multi-state specialization of the same order-adjoint concept already represented by P008-style machinery. It contributes to the interface only when assembled with weighted semiring path composition/closure.

### TR-6. Finite Bellman least/greatest fixed points

On a finite complete ordered carrier `S^n`, let

`T(x)=b⊕A⊗x`.

`T` is monotone.

**Claim.**

- iteration from bottom stabilizes at the least fixed point;
- iteration from top stabilizes at the greatest fixed point.

**Status:** `CLASSICAL / EXACTLY CHECKED`.

**Proof.** Bottom iteration is ascending because `⊥≼T(⊥)` and monotonicity preserves the chain. Finiteness forces stabilization. Any fixed point bounds every iterate, so the stabilized point is least. The top argument is dual.

Checker example has exactly three fixed points:

`[1,1], [2,2], [3,3]`.

It recovers:

- least fixed point `[1,1]`;
- greatest fixed point `[3,3]`.

### TR-7. Relabeling invariance

If `P` is a state permutation, relabeling sends `A` to `PAP^{-1}` at the index level.

**Claim.** Path powers and closure relabel equivariantly.

**Status:** `CLASSICAL / EXACTLY CHECKED`.

The checker permutes a weighted DAG and verifies that closure before/after relabeling is exactly the corresponding permuted matrix.

## 5. Mandatory dedup

| Existing owner | Overlap | What remains outside it | Verdict |
|---|---|---|---|
| P008 / current order-adjoint machinery | threshold pullback, Galois/adjoint law, scalar monotone residual pattern | semiring-valued multi-state path composition, `A^k` path envelope, all-path closure, improving-cycle semantics, Bellman closure | **RESIDUAL COMPONENT REUSE/EXTENSION; OVERALL NOT DUPLICATE** |
| T1 Scale Enumeration | counts scales/shells, finite differences, generating functions | weighted path optimum/envelope is not enumeration | **DISTINCT** |
| T3 Typed Incidence Circuit | cycle/circuit witness may expose the combinatorial support of an improving cycle | whether the cycle is improving depends on declared weights; closure value is not T3 output | **COMPOSE FOR CERTIFICATE SUPPORT ONLY** |
| T6 Operation-Safe Quotient | certifies which distinctions/operations may descend | weighted operator descends only if declared weights are preserved on quotient fibers | **T6 PRECONDITION, NOT OWNER OF CLOSURE** |
| T9 Holonomy/Gluing | loop transport defect and route dependence | an optimized weighted path envelope is not automatically holonomy | **DISTINCT UNLESS LOOP DEFECT IS THE ACTUAL INVARIANT** |

### 5.1 Why this is not `EXTEND_P008_ORDER_ADJOINT` overall

If the task stopped at

`A⊗x≼b iff x≼A\b`

the correct terminal result would be `EXTEND_P008_ORDER_ADJOINT`.

It does not stop there. `POWER`, finite `CLOSURE`, explicit improving-cycle certificates, and Bellman closure on weighted transition systems do not reduce to a one-map threshold pullback. These operations supply a real path-compositional capability gap.

### 5.2 Why this is not merely `COMPOSE_P008_T3_T6`

P008 explains residual adjunction; T3 can expose a cycle support; T6 can certify a quotient. None of them computes

`I⊕A⊕A^2⊕...`

or supplies the weighted all-path envelope. Therefore composition of existing tools does not recreate the principal new capability.

## 6. Two-domain reuse gate

## Application A — explicitly weighted provenance/path system

A depth-18 branching/recoalescing DAG was constructed with caller-supplied integer edge costs.

Properties:

- states: `55`;
- source-target paths: exactly `2^18 = 262,144`;
- no cost was inferred from incidence or path length;
- exhaustive path enumeration optimum: `33`;
- min-plus all-pairs closure optimum: `33`;
- cubic closure cell-update upper bound used for the comparison:
  `55^3 = 166,375`.

Thus even on this finite regression instance, the closure representation processes fewer cubic state triples than there are source-target paths, before counting the per-path edge processing required by enumeration.

As depth `d` grows, the graph has `1+3d` states while the path family has `2^d` members. The interface therefore replaces exponential path enumeration by polynomial state-space closure.

**Gate verdict:** `PASS — REAL COMPRESSION`.

## Application B — threshold/precision inequality propagation

This application is not a renamed shortest-path query.

Carrier:

`S = {-∞,0,1,...,6}`

with max as `⊕` and saturated addition as `⊗`.

Semantic reading:

- each variable is an explicitly declared finite grade/precision level;
- matrix entry `a_ij` is an explicitly declared grade increment required by transformation `j -> i`;
- output vector `b` is a declared cap/threshold vector;
- the problem is to find the componentwise greatest admissible input-grade vector satisfying

`A⊗x ≼ b`.

Regression dimensions:

- carrier size: `8`;
- variables: `4`;
- brute-force assignments: `8^4 = 4096`;
- matrix scalar constraints: `3*4 = 12`;
- feasible assignments: `336`;
- exact right residual:
  `[1,5,2,2]`.

The residual law proves that this vector dominates every feasible assignment componentwise, so the solver replaces state-by-state search with a matrix residual computation.

**Gate verdict:** `PASS — DISTINCT DOMAIN AND REAL INEQUALITY-SOLVER COMPRESSION`.

## 7. Required negative boundaries

### N1. Bare unweighted relation

Input: edge `0->1`, no declared weights.

Result:

`OBSTRUCTION: MISSING_DECLARED_WEIGHT_SEMANTICS`.

No path length/cost is inferred.

### N2. Non-idempotent addition

Ordinary addition has

`1+1=2 != 1`.

Therefore the claimed canonical order `a≼b iff a⊕b=b` is not even reflexive in general.

Result:

`OBSTRUCTION: NON_IDEMPOTENT_ADDITION`.

### N3. Partial order / total-order shortcut failure

Use the powerset dioid with union as `⊕` and intersection as `⊗`.

`{p}` and `{q}` are incomparable under the natural subset order, despite having equal cardinality.

Any implementation that “takes the larger” by rank/cardinality loses semantic information.

Result:

`OBSTRUCTION: PARTIAL_ORDER_REQUIRES_MEETS/JOINS; TOTAL_SORT_FORBIDDEN`.

### N4. Improving cycle

Checked exact witnesses:

- min-plus cycle value `-1`;
- max-plus cycle value `+2`.

Result on non-completed carriers:

`UNBOUNDED_CYCLE_CERT`.

### N5. Nonresiduated operator

On the diamond lattice `P({p,q})`, define the monotone map

- `f(top)=top`;
- `f(x)=bottom` for every proper subset.

For `b=bottom`, the feasible preimage set is

`{bottom,{p},{q}}`.

It has no greatest element because `{p}` and `{q}` are incomparable and `top` is not feasible.

Therefore no residual exists at `b`.

Result:

`OBSTRUCTION: OPERATOR_NOT_RESIDUATED`.

### N6. Incomplete carrier

In max-plus over `N ∪ {-∞}` without `+∞`, a positive cycle gives the chain

`0 < 1 < 2 < ...`.

No element of the carrier is its supremum: any candidate `c` is defeated by `c+1`.

Result:

`OBSTRUCTION: INCOMPLETE_CARRIER` or an improving-cycle certificate, not a silently created `+∞`.

### N7. T6-safe support quotient but failed weight descent

States `u` and `v` have identical unweighted successor class `t`, so an unweighted support quotient may identify them.

Declared outgoing weights differ:

- `w(u,t)=1`;
- `w(v,t)=2`.

The weighted operator is not constant on the quotient fiber.

Result:

`OBSTRUCTION: QUOTIENT_DOES_NOT_PRESERVE_DECLARED_WEIGHTS`.

Thus T6 safety for the declared unweighted operation is necessary but not sufficient for weighted-semiring descent.

### N8. Path envelope is not automatically a native metric

Directed declared costs:

- `a->b = 1`;
- `b->a = 3`.

Min-plus closure gives `d(a,b)=1`, `d(b,a)=3`.

Symmetry fails. Therefore the path envelope cannot be promoted to a metric without separate metric hypotheses.

Result:

`OBSTRUCTION: PATH_ENVELOPE_NOT_NATIVE_METRIC`.

## 8. Classical-prior-art / Enterprise-novelty split

| Item | Classification |
|---|---|
| idempotent natural order | classical |
| min-plus/max-plus matrix algebra | classical |
| matrix powers as path envelopes | classical |
| Kleene/path closure | classical |
| Floyd-Warshall/Bellman dynamic closure | classical |
| improving-cycle unboundedness | classical |
| residuated maps / Galois law | classical and P008-overlap |
| finite monotone least/greatest fixed points | classical |
| strict Enterprise explicit-weight firewall | new Enterprise interface discipline |
| unified closure/residual/fixed-point obstruction API | new Enterprise interface |
| T6 weight-descent condition made explicit | new interface composition rule, not theorem novelty |
| two-domain reusable compression contract | new Enterprise tool-interface evidence |
| genuinely new theorem | **NONE CLAIMED** |

Therefore:

`CLASSICAL_IDEMPOTENT_ALGEBRA_PACKAGED_FOR_ENTERPRISE != NEW_THEOREM`.

## 9. Checker freeze

Required executable:

`scripts/tool_discovery_tropical_residuation_idempotent_closure_check.py`

Checker commit:

`96a77567142b0eb19d8a4ddb402ce08d08869441`

Checker SHA256:

`c18bf6c3b312946ce5d067dd4a86cddab7743dee33d427927c50c7f0f2ade6bb`

Execution:

`python scripts/tool_discovery_tropical_residuation_idempotent_closure_check.py`

Exact result:

- `pass_count = 40`;
- `mismatch_count = 0`;
- floating approximation: none;
- integer/sentinel exact arithmetic only.

Mandatory regression coverage present:

- min-plus and max-plus matrices;
- fixed-length powers vs exhaustive path envelopes;
- acyclic closure vs exhaustive all-path enumeration;
- cyclic systems with and without improving cycles;
- left/right residual Galois laws on a finite carrier;
- Bellman least/greatest fixed points;
- unreachable/infinity conventions;
- relabeling invariance;
- both Enterprise applications;
- all required negative counterexamples.

## 10. Acceptance-gate decision

1. explicit weighted semantic input contract — **PASS**;
2. reusable closure/residual/fixed-point API — **PASS**;
3. nontrivial algebraic law/certificate — **PASS**;
4. exact failure boundaries — **PASS**;
5. two-domain reuse — **PASS**;
6. real path-search / inequality-search compression — **PASS**;
7. exact dedup against P008 and T1/T3/T6/T9 — **PASS**.

## 11. Frozen terminal classification

### Strongest classification

**`NEW_ENTERPRISE_TOOL_INTERFACE`**

### Component-level ownership

- residuation/Galois adjunction alone:
  `EXTEND_P008_ORDER_ADJOINT`;
- improving-cycle combinatorial support:
  may compose with `T3_TYPED_INCIDENCE_CIRCUIT`;
- quotient preprocessing:
  may compose with `T6_OPERATION_SAFE_QUOTIENT`, but only with independent weight-descent verification;
- all-path weighted closure / semiring matrix composition / Bellman envelope:
  **new Enterprise capability gap filled by this interface**.

### Explicit non-claims

- no new tropical theorem;
- no new Galois-adjunction theorem;
- no weight inference from unweighted Enterprise structure;
- no native metric theorem;
- no quotient selection by target optimization;
- no foundation mutation.

`ENTERPRISE_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_TOOL_CLASSIFIED`

**FROZEN: `NEW_ENTERPRISE_TOOL_INTERFACE`**

STOP.
