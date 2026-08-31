# R015 — Result-Support Branch Deferral Invariance Report

Status: `RESULT_SUPPORT_BRANCH_DEFERRAL_PROVED / EXECUTABLE_EXHAUSTIVE_PASS / FOUNDATION_REWRITE_CANDIDATE / NOT_CANONICAL`  
Researcher-ID: `EM-R015-R7A3`  
Task: `RS-R015-RESULT-SUPPORT-BRANCH-DEFERRAL-INVARIANCE`  
Base inspected: `awdawmip/enterprise-math@f9a63e6e558a065acc810981312fcf653505cc03`  
Canonical mutation policy: **none** — R009 and P023 were not modified.

## 1. Driver verdict

The proposed **result-only branch-deferral semantics survives the foundation gate** under the exact contract frozen by R015:

1. state is current-state sufficient: every fact that can alter any declared future is already encoded in the current state;
2. the observable is only final reachable-result **support**;
3. multiplicity, path/provenance, accumulated cost, probability/weights and amplitude are not observables unless promoted into the state/carrier;
4. every future step is a relation on current states, hence acts on supports by relational direct image.

Under that contract, eager branch materialization with arbitrary intermediate coalescence, lazy unresolved support, and direct execution of the composed relation have **exactly the same final reachable-result support for every finite horizon and every initial family**. No counterexample exists inside the declared relational/current-state-sufficient Boolean-support contract.

The generic mathematics is classical prior art. The Enterprise Math result is the semantic consequence: deterministic single-valued descent is sufficient but **not necessary** for exact result-support future execution. A future quotient may be `SUPPORT_SAFE` even when it is not `FUNCTIONAL_SAFE`, provided the quotient state is current-state sufficient and its future action is genuinely relational/direct-image on support.

This report **does not** decide the later carrier question

`a^p < n < (a+1)^p  =>  unresolved state = {a^p,(a+1)^p}`.

No form of that proposition is used in any proof or executable test here.

---

## 2. Frozen semantic contract and notation

Let `X,Y,Z` be arbitrary sets. A relation `R subseteq X x Y` acts on a support `A subseteq X` by

`Phi_R(A) = { y in Y | exists x in A, x R y }`.

For `R subseteq X x Y` and `S subseteq Y x Z`, relation composition is oriented as

`S o R = { (x,z) | exists y in Y, x R y and y S z }`.

Thus a future word `R_1,...,R_n` executes left-to-right on states and right-to-left as functions:

`Phi_Rn o ... o Phi_R1`.

A branch representation may carry several component supports `C_j`. Its result-only denotation is only

`|C| = union_j C_j`.

Two representations are semantically identical for this task iff their unions are equal. Splitting, regrouping, duplicating and deduplicating components are permitted only when they preserve that union. Nothing in the positive theorem identifies two states whose future differs; such a merge would violate current-state sufficiency.

---

## 3. R015-T01 — arbitrary-union preservation

### Theorem

For every set-indexed family `(A_i)_{i in I}` of subsets of `X`, including `I = empty`,

`Phi_R(union_i A_i) = union_i Phi_R(A_i)`.

### Proof

For `y in Y`,

`y in Phi_R(union_i A_i)`

iff there exists `x in union_i A_i` with `x R y`,

iff there exist `i in I` and `x in A_i` with `x R y`,

iff there exists `i in I` such that `y in Phi_R(A_i)`,

iff `y in union_i Phi_R(A_i)`.

The equivalence is pointwise in `y`, so the sets are equal.

For the empty family, `union empty = empty`, and there is no `x in empty`; hence

`Phi_R(empty)=empty`.

Therefore every relational direct-image transformer is a complete join/union homomorphism `P(X) -> P(Y)`.

### Status

`PROVED / ROOTING_SUCCESS / PRIOR_ART`.

---

## 4. R015-T02 — relation composition / future composition

### Theorem

For `R subseteq X x Y` and `S subseteq Y x Z`, with the orientation above,

`Phi_(S o R) = Phi_S o Phi_R`.

### Proof

For any `A subseteq X` and `z in Z`,

`z in Phi_(S o R)(A)`

iff there exists `x in A` with `(x,z) in S o R`,

iff there exist `x in A` and `y in Y` such that `x R y` and `y S z`,

iff there exists `y in Phi_R(A)` such that `y S z`,

iff `z in Phi_S(Phi_R(A))`.

Thus the functions agree on every support.

By induction, for every finite word `R_1,...,R_n`,

`Phi_Rn ... Phi_R1 = Phi_(R_n o ... o R_1)`.

The empty word is the identity relation and identity support transformer.

### Status

`PROVED / ROOTING_SUCCESS / PRIOR_ART`.

---

## 5. R015-T03 — arbitrary finite-horizon eager/lazy/coalescence invariance

### 5.1 Family theorem

Let `(A_i)_{i in I}` be any family of initial supports and let `R_1,...,R_n` be any finite future sequence. Define

`F_n = Phi_Rn o ... o Phi_R1`.

Then

`F_n(union_i A_i) = union_i F_n(A_i)`.

### Proof

T01 says each `Phi_Rk` preserves arbitrary unions. The composition of arbitrary-union-preserving maps again preserves arbitrary unions:

if `F,G` preserve arbitrary unions, then

`(G o F)(union_i A_i)`
`= G(union_i F(A_i))`
`= union_i G(F(A_i))`.

Induction on `n` proves the statement for every finite horizon. Horizon `0` is the identity and is immediate.

### 5.2 Stronger arbitrary intermediate coalescence theorem

At any intermediate time, represent the current uncertainty by an arbitrary family of supports `C=(C_j)`. Its denotation is `|C|=union_j C_j`.

Allow any finite sequence of representation-only operations that preserves `|C|`, including:

- splitting a support into components whose union is the original support;
- regrouping components;
- merging/coalescing components by union;
- duplicating a component;
- deleting exact duplicate copies under set semantics.

When one future relation `R` is executed componentwise, the new denotation is

`union_j Phi_R(C_j) = Phi_R(union_j C_j) = Phi_R(|C|)`

by T01.

Therefore every representation-preserving reorganization before or after a future step leaves the denotation invariant. Induction over an arbitrary finite interleaving of representation operations and future steps proves:

> **Every eager branching/coalescence schedule that preserves current set union has the same final support as the lazy unresolved-support representation.**

Combining with T02 gives the third form:

> **Both equal direct image under the one composed future relation `R_n o ... o R_1`.**

This is stronger than checking one fixed eager schedule. It proves schedule independence at the semantic level.

### 5.3 What is and is not being equated

The theorem equates only final Boolean reachable-result support. It does **not** claim equality of:

- branch counts;
- path witnesses;
- probability mass;
- amplitudes;
- provenance;
- costs;
- hidden-state-sensitive futures.

### Status

`PROVED / ENTERPRISE_SEMANTIC_SPECIALIZATION` (generic proof ingredients are prior art; the collapse-execution consequence is project-specific).

---

## 6. R015-T04 — strongest correct characterization

### 6.1 Exact equivalence: branch deferral iff union preservation

Let `T:P(X)->P(Y)` be arbitrary.

Define **branch-deferral invariance for all families** to mean

`T(union_{i in I} A_i) = union_{i in I} T(A_i)`

for every indexing set `I` and every family `(A_i)_{i in I}`.

Then, literally by definition,

`branch deferral for all set-indexed families`

iff

`T preserves arbitrary unions (complete joins)`.

The empty family matters. If `I=empty` is included, the law forces

`T(empty)=empty`.

If a convention quantifies only over **nonempty** branch families, the result is only preservation of nonempty unions. It does **not** force bottom preservation. In that convention, `T(empty)=empty` must be added separately before identifying `T` with a relational direct image.

The executable `bottom_injection` mutation is the minimal witness to this distinction.

### 6.2 Representation theorem: complete join maps are exactly relational direct images

#### Theorem

For arbitrary sets `X,Y` and arbitrary `T:P(X)->P(Y)`, the following are equivalent:

1. `T` preserves arbitrary unions, including the empty union;
2. for every `A subseteq X`,
   `T(A)=union_{x in A} T({x})`;
3. there exists a relation `R subseteq X x Y` such that `T=Phi_R`.

Moreover the relation is uniquely determined by singleton behavior:

`R_T(x,y) iff y in T({x})`.

#### Proof: 1 => 2

Every set is the union of its singletons:

`A = union_{x in A} {x}`.

Hence arbitrary-union preservation gives

`T(A)=union_{x in A}T({x})`.

For `A=empty`, this also gives `T(empty)=empty`.

#### Proof: 2 => 3

Define `R_T(x,y)` iff `y in T({x})`. Then

`Phi_R_T(A)`
`= {y | exists x in A, y in T({x})}`
`= union_{x in A} T({x})`
`= T(A)`.

Thus `T=Phi_R_T`.

#### Proof: 3 => 1

This is T01.

#### Uniqueness

If `T=Phi_R`, then

`T({x})={y | x R y}`.

So the successor set of every singleton recovers exactly the row of `R`; no other relation has the same direct-image transformer.

Therefore

> **`RESULT_SUPPORT_SAFE_FUTURES` under the frozen carrier are exactly complete join homomorphisms `P(X)->P(Y)`, equivalently relational direct-image dynamics.**

No finiteness assumption is needed for this equivalence.

### 6.3 Finite-union weakening: exactly when it is sufficient

If `X` is finite, the following are equivalent to the three conditions above:

- `T(empty)=empty`;
- `T(A union B)=T(A) union T(B)` for all `A,B subseteq X`.

Reason: every `A subseteq X` is a **finite** union of singletons, so binary-union preservation plus bottom preservation yields singleton generation; the representation theorem then yields arbitrary-union preservation.

For infinite `X`, finite-union preservation plus `T(empty)=empty` is not sufficient.

#### Infinite counterexample

Let `X=Y=N` and define

`T(A)=A` if `A` is finite,

`T(A)=N` if `A` is infinite.

Then `T(empty)=empty` and `T` preserves binary (hence all finite) unions:

- finite union finite: both sides are `A union B`;
- if either operand is infinite, both sides are `N`.

But let `E` be the set of even natural numbers. The singleton family `{ {e} | e in E }` has

`union_{e in E} T({e}) = E`,

while

`T(E)=N`.

So arbitrary-union preservation and relational representation fail.

### 6.4 Useful corollaries

Every result-support-safe transformer is automatically monotone:

if `A subseteq B`, write `B=A union (B\A)` and use union preservation.

Safe transformers are closed under composition (T02/T01), and identity is safe. Thus finite future words remain inside the same class.

### Status

- T04a branch-deferral iff arbitrary-union preservation: `PROVED / ROOTING_SUCCESS / PRIOR_ART`.
- T04b complete-join map iff singleton-generated relational direct image: `PROVED / ROOTING_SUCCESS / PRIOR_ART`.
- T04c finite-X reduction to binary unions + bottom and infinite-X no-go: `PROVED / ROOTING_SUCCESS / PRIOR_ART`.

---

## 7. R015-T05 — Boolean future-matrix equivalence

Assume finite state sets. For `R subseteq X x Y`, define the Boolean adjacency matrix

`M_R[x,y]=1 iff x R y`.

Encode a support `A subseteq X` as a Boolean **row** vector `v_A` with

`v_A[x]=1 iff x in A`.

All addition is `OR`; all multiplication is `AND`.

### 7.1 One-step support propagation

For `y in Y`,

`(v_A M_R)[y]`
`= OR_x (v_A[x] AND M_R[x,y])`

is `1` iff there exists `x in A` with `x R y`, exactly iff

`y in Phi_R(A)`.

Therefore Boolean matrix-vector propagation and relational direct image are identical encodings of final reachable support.

### 7.2 Relation composition

With the row-vector convention,

`M_(S o R) = M_R M_S`

over the Boolean semiring, because

`(M_R M_S)[x,z] = OR_y (M_R[x,y] AND M_S[y,z])`

is `1` exactly when some intermediate `y` witnesses `x R y S z`.

Thus

`v_A M_R1 ... M_Rn`

encodes

`Phi_Rn ... Phi_R1(A)`.

### 7.3 OR distribution / branch coalescence

For any finite family of Boolean support vectors,

`(OR_i v_i) M = OR_i (v_i M)`

pointwise, by distributivity of `AND` over `OR`. Inductively this remains true through every finite Boolean matrix product.

This is the finite-matrix form of T01–T03.

### 7.4 Critical boundary: not a path-count matrix

The matrix equality in R015 is equality of **Boolean reachability**. Multiple paths contributing to one entry combine by idempotent `OR`:

`1 OR 1 = 1`.

Integer/arithmetic matrix multiplication would count paths and generally changes under duplicate branch coalescence. That is deliberately a different semantic carrier.

### Status

`PROVED / ROOTING_SUCCESS / PRIOR_ART`.

---

## 8. R015-T06 — coalescence idempotence

Set support is idempotent:

`A union A = A`.

If two or more branches arrive at the same state, deduplicating them leaves the current support unchanged. For any finite future word `F`,

`F(A union A)=F(A)`

because `A union A=A`; equivalently, by union preservation,

`F(A union A)=F(A) union F(A)=F(A)`.

Thus repeated arrival at one state is observationally invisible **only in result-support semantics**. The multiplicity counterexample below shows why this cannot be generalized to count-sensitive carriers.

### Status

`PROVED / ENTERPRISE_SEMANTIC_SPECIALIZATION`.

---

## 9. Independent executable oracle

Reference implementation:

- `experiments/r015_branch_deferral_oracle.py`
- `tests/test_r015_branch_deferral_oracle.py`

Generated evidence:

- `experiments/r015_enumeration_summary.json`
- `experiments/r015_theorem_counterexample_matrix.json`

The implementation is standard-library Python and uses integer/Boolean exact data only. AST audit found zero floating-point constants and zero true-division nodes.

### 9.1 Three independent engines

1. `eager_support_engine`
   - executes each relation step directly on the current set support;
   - materializes successors and deduplicates after every step.

2. `lazy_support_engine`
   - composes the full relation word first;
   - applies one relational direct image only at the end.

3. `boolean_matrix_engine`
   - converts relations to independent bit-row Boolean adjacency matrices;
   - propagates an integer bitmask support by Boolean matrix action.

The Boolean engine does not call the eager engine for propagation, and the lazy engine independently constructs relation composition.

---

## 10. Exhaustive and property evidence

### 10.1 All two-state relations through horizon 4

A relation on a two-state set has `2^(2*2)=16` possibilities. The oracle exhausts:

- all 16 relations at every future position;
- all 4 initial supports;
- horizons `0,1,2,3,4`.

Exact triple-engine case count:

`4 * (1 + 16 + 16^2 + 16^3 + 16^4) = 279,620`.

All `279,620` cases agree exactly.

Nonzero-horizon composed-matrix orientation checks: `279,616`.

### 10.2 Branch grouping / intermediate coalescence schedule coverage

For bounded duplicate multiplicity at most 2 on the two-state universe, all multiset branch representations were enumerated and grouped by the same Boolean union support:

- union `empty`: 1 representation;
- union `{0}`: 2 representations;
- union `{1}`: 2 representations;
- union `{0,1}`: 22 representations;
- total: 27 representations.

All one-step relation/representation transitions were checked: `16 * 27 = 432`.

Propagating the complete representation-state sets through all relation words to horizon 4 produced:

- `8,311,815` distinct representation-state checks;
- `42,881,022,881` implicit bounded schedule paths represented by the dynamic-programming aggregation.

Every representation with the same current set union had the same next/final set union. The mathematical T03 proof removes the bounded-multiplicity restriction; the exhaustive schedule layer is an independent finite oracle against implementation mistakes.

### 10.3 Exhaustive arbitrary transformers `T:P(X)->P(Y)`

The oracle exhausts every transformer for all

`0 <= |X| <= 3`, `0 <= |Y| <= 2`.

Exact total transformers inspected: `66,094`.

Across the whole bounded universe:

- arbitrary-union preserving: `104`;
- singleton-generated: `104`;
- binary-union + bottom preserving: `104`;
- relational direct-image tables: `104`.

For the required largest cell `|X|=3, |Y|=2`:

- arbitrary transformers: `4^8 = 65,536`;
- arbitrary-union preserving: `64`;
- singleton-generated: `64`;
- binary-union + bottom preserving: `64`;
- relations `X x Y`: `2^(3*2)=64`.

The four classifications coincide exactly, as predicted by T04 for finite `X`.

### 10.4 Random/property tests

Seed `15015`, 500 deterministic randomized trials:

- state sizes through 8;
- horizons through 12;
- all three positive-contract engines agreed.

These trials supplement but do not replace the exhaustive core.

### 10.5 Unit suite

The local `unittest` suite contains 7 focused tests covering:

- T01 relational union preservation;
- T02 composition orientation and Boolean matrix product;
- complete two-state horizon-4 exhaustive comparison;
- complete transformer characterization through `|X|=3,|Y|=2`;
- mutation divergence detection;
- randomized larger systems;
- no-float/no-true-division audit.

Result: **7 passed, 0 failed**.

---

## 11. Mutation tests and minimized divergence witnesses

The oracle deliberately injects three non-union-preserving transformers and requires an eager/lazy mismatch.

### 11.1 `pair_required`

`X={a,b}`, `Y={y}`,

`T(A)={y}` iff both `a` and `b` are present; otherwise `empty`.

Then

`T({a}) union T({b}) = empty`,

but

`T({a,b})={y}`.

So eager singleton materialization gives `empty`, lazy union gives `{y}`.

This is the minimal genuine two-distinct-singleton branch failure found by enumeration (`|X|=2, |Y|=1`).

### 11.2 `exactly_one`

`T(A)={y}` iff exactly one of `a,b` is present.

Then eager singleton processing returns `{y}` while the union `{a,b}` returns `empty`.

This checks the opposite divergence direction.

### 11.3 `bottom_injection`

Minimal arbitrary-family failure:

`X=empty`, `Y={y}`, `T(empty)={y}`.

For the empty branch family, eager union on the right is `empty` while lazy `T(empty)={y}`.

This mutation is why the empty-family/bottom hypothesis must be explicit.

All three mutations were automatically classified non-union-preserving and all three automatically generated eager/lazy divergence witnesses.

---

## 12. Negative boundary counterexamples

These examples attack one frozen assumption at a time. None is a counterexample inside the declared positive contract.

### 12.1 Hidden-history future

Hidden states `h0,h1` both project to one visible current state `s`, but future evolution differs:

`h0 -> y0`, `h1 -> y1`.

After projecting both histories to `{s}`, a future that still reads which history occurred cannot be a function/relation of visible current state alone with exact per-history semantics. The same visible singleton `{s}` would need incompatible future behavior.

Classification:

`SEMANTIC_CONTRACT_VIOLATION / WRONG_STATE_TYPE / CURRENT_STATE_NOT_SUFFICIENT`.

Repair: include the still-future-readable discriminator in the current state before collapsing history.

### 12.2 Multiplicity-sensitive readout

One branch `[x]` and two duplicate branches `[x,x]` have the same Boolean support `{x}`. A readout that returns `y1` for count 1 and `y2` for count 2 distinguishes them.

Classification:

`OUT_OF_CONTRACT_OBSERVABLE / WRONG_STATE_TYPE`.

Repair: use a multiset/count carrier, e.g. an `N`-semimodule, or store the count explicitly.

### 12.3 Support-global nonlinear rule

Use `pair_required` above. The output depends on simultaneous global presence of two support states and cannot be generated pointwise from singleton successors.

Classification:

`THEOREM_HYPOTHESIS_FAILURE / NON_UNION_PRESERVING_TRANSFORMER`.

This is a true eager/lazy divergence, but it lies outside relational direct-image semantics and therefore does not kill R015.

### 12.4 Discarded probability / weights

Two exact weighted states

`(3/4,1/4)` and `(1/4,3/4)`

on support `{x0,x1}` have the same Boolean support but different weighted futures/readouts.

Classification:

`OUT_OF_CONTRACT_OBSERVABLE / WRONG_CARRIER`.

Repair: retain probability distributions/weights and evolve them with a stochastic/weighted kernel. Dropping weights is not a legal support-only collapse when weights remain observable.

### 12.5 Signed/amplitude cancellation

Let both `x0,x1` reach `y`, with amplitudes `+1` and `-1`. Boolean reachability reports `{y}`, but exact amplitude addition cancels to zero, so nonzero-amplitude support is `empty`.

Classification:

`OUT_OF_CONTRACT_OBSERVABLE / BOOLEAN_SUPPORT_NOT_FAITHFUL / RICHER_MODULE_REQUIRED`.

Repair: use a signed/complex linear carrier whose addition retains cancellation. Boolean OR is intentionally not that algebra.

---

## 13. Prior-art / rooting attack

The generic mathematics is not novel and must not be repackaged under Enterprise names.

| R015 object | Rooting result | Enterprise use |
|---|---|---|
| binary relations and relational composition | `ROOTING_SUCCESS / PRIOR_ART` | frozen future-step semantics |
| direct image of a relation on powersets | `ROOTING_SUCCESS / PRIOR_ART` | result-support executor |
| nondeterministic transition / reachable-state sets | `ROOTING_SUCCESS / PRIOR_ART` | operational reading of unresolved support |
| powerset/Kleisli-style relational semantics | `ROOTING_SUCCESS / PRIOR_ART` | composition language |
| complete join / arbitrary-union preserving maps | `ROOTING_SUCCESS / PRIOR_ART` | exact branch-deferral criterion |
| Boolean-semiring reachability | `ROOTING_SUCCESS / PRIOR_ART` | finite future-matrix implementation |
| eager/lazy equality for Enterprise collapse execution under this frozen contract | `ENTERPRISE_SEMANTIC_SPECIALIZATION` | foundation rewrite candidate |
| P023 deterministic-vs-support-safe split | `R015_SPECIFIC_FOUNDATION_IMPACT` | downstream owner proposal only |

Representative roots checked:

1. Alfred Tarski, **On the calculus of relations**, *Journal of Symbolic Logic* 6(3), 73–89 (1941), DOI `10.2307/2268577` — classical relation calculus.
2. Michael O. Rabin and Dana Scott, **Finite Automata and Their Decision Problems**, *IBM Journal of Research and Development* 3(2), 114–125 (1959), DOI `10.1147/rd.32.0114` — foundational finite/nondeterministic automata context.
3. Marta Bílková, Alexander Kurz, Daniela Petrișan, Jiří Velebil, **Relation lifting, with an application to the many-valued cover modality**, *Logical Methods in Computer Science* 9(4:8) (2013), DOI `10.2168/LMCS-9(4:8)2013` — relation lifting and powerset-monad/Kleisli context, explicitly framed as generalizing classical results.
4. Francesco Ciraulo and Michele Contente, **Overlap Algebras: a Constructive Look at Complete Boolean Algebras**, *Logical Methods in Computer Science* 16(1:13) (2020), DOI `10.23638/LMCS-16(1:13)2020` — category extending sets/relations; classically the relevant morphisms are join-preserving maps.
5. Cipriano Junior Cioffo, Fabio Gadducci, Davide Trotta, **A taxonomy of categories for relations**, *Logical Methods in Computer Science* 22(2:36) (2026), DOI `10.46298/lmcs-22(2:36)2026` — modern organization of categories for relations and Kleisli-category viewpoints.

Rooting verdict:

`ROOTING_SUCCESS / PRIOR_ART` for the generic theorem family. No novelty claim is retained for union preservation, relational direct image, nondeterminism, powerset lifting, join homomorphisms or Boolean reachability.

---

## 14. Enterprise Math impact matrix

### 14.1 P023 — Composition-Safe Collapse

Proposed semantic split for a later owner task:

#### `FUNCTIONAL_SAFE`

A coarse/current state has a unique coarse successor for the declared deterministic future. This is current P023 deterministic descent/factorization.

Impact:

- P023-T01 and T02 remain exactly true unchanged for their deterministic map/factorization scope.
- P023-T03–T07 remain exactly true unchanged for deterministic transition-compatible refinement/future closure.
- `FUNCTIONAL_SAFE` is a special case of `SUPPORT_SAFE` where every relational successor support is a singleton (or empty if separately typed partiality permits it).

#### `SUPPORT_SAFE`

Single-valued deterministic descent fails, but the coarse/current state has an exact **set of possible successors**, every future-readable distinction is encoded in the current state, and the declared observable is only reachable-result support. The induced powerset action is relational direct image and therefore complete-join preserving.

Impact:

- all finite future words compose exactly by R015-T02/T03;
- duplicate branches may coalesce;
- deterministic failure alone is no longer sufficient to label the quotient “unsafe” for result-support semantics;
- this should be aligned with, not duplicate, the existing common-surface `A4_P023_relation_observable_bridge`.

#### `SUPPORT_UNSAFE`

At least one required condition fails:

- hidden history/legality/provenance still changes future behavior but is absent from state;
- multiplicity/weights/amplitude remain observable but were discarded;
- the support transformer is genuinely non-union-preserving/global-nonlinear;
- or the declared result observation is not faithfully recoverable from Boolean support.

Then state refinement or a richer carrier is required.

#### Exact theorem rewrite impact

No current P023 theorem is refuted. The required later rewrite is a **scope extension / taxonomy split**, especially in the interpretation of “unsafe collapse”:

`deterministic descent failure`

must be separated from

`result-support future failure`.

The existing rule “discard witness identity only after proving future compatibility” remains correct, but “future compatibility” becomes typed by the declared semantic carrier: functional, support-valued, witness/multiplicity-valued, weighted, etc.

### 14.2 R009 — deterministic downward collapse formalization

`DO_NOT_MODIFY` in R015.

R015 proves no particular arithmetic unresolved carrier. If a later post-R015/R016 task approves one, R009 would need a **new typed support/relation-valued layer beside the deterministic collapse**, not an unproved replacement of canonical downward collapse.

Required future obligations would include:

1. define the proposed unresolved carrier independently of R015;
2. prove that it contains every piece of state future operations may read;
3. prove the induced future action is relational/direct-image for the declared result-support query;
4. prove the observation map from the richer carrier back to existing results;
5. only then compare or specialize canonical deterministic `collapse` theorems.

The statement `{a^p,(a+1)^p}` is deliberately neither assumed nor evaluated here.

### 14.3 P018 — precision projection

P018 precision projection should later distinguish:

- **functional-valued precision projection**: one coarse value/state;
- **support-valued precision projection**: an exact set of unresolved current possibilities.

A support-valued projection is not automatically safe. It is safe exactly when the declared future/result semantics factors through a current-state-sufficient relational support system. R015 therefore widens the admissible exact precision carrier without weakening the future-compatibility proof obligation.

### 14.4 P021 — witness/multiplicity semantics

P021's negative boundary remains intact. Boolean support does not preserve middle-incidence witness identity, path count or multiplicity.

R015 only says that **if the declared query is reachable target support**, witness identity and duplicate multiplicity may be discarded after current-state sufficiency is proved. If a P021 query asks for witness counts/incidence/provenance, it is outside the R015 Boolean carrier and requires the richer A3/A4 witness relation semantics.

Thus R015 is not a workaround for P021 witness-composition obstructions; it identifies a strictly weaker observable for which exact collapse is possible.

### 14.5 R013 — precision-limit closure / fibre calculus

R013 already concluded that task-relative precision is generated by the declared semantic query family, and that point-safe does not imply witness-safe. R015 fits this exactly:

- “reachable-result support” is one declared semantic query family;
- complete-join/relational direct-image sufficiency is the exact compiler criterion for that query;
- witness/multiplicity/weight queries remain different fibres and are not promoted by R015.

No R013 mother theorem needs rewriting. R015 provides a concrete, fully characterized result-support specialization and reinforces R013's rule that the semantic query must be frozen before declaring information discard exact.

### 14.6 R014 — exact-law representation resource calculus

R014's root verdict requires exact semantic-fibre equality **before** comparing storage/work/depth/resource tradeoffs. R015 supplies exactly such an equality certificate for three implementations:

- eager materialization;
- lazy composed-relation execution;
- Boolean-matrix execution.

Only after T03/T05 prove the same result-support law may R014 compare their resource coordinates. Their different storage/precomputation/depth profiles are implementation-resource differences, **not precision differences**.

No new R014 resource calculus is implied.

---

## 15. Machine-readable theorem/counterexample matrix status

`experiments/r015_theorem_counterexample_matrix.json` records:

- T01–T06 theorem status/classification;
- the exact PASS/canonical status;
- strongest characterization assumptions;
- minimized mutation witnesses;
- negative-boundary classifications;
- P023/R009/P018/P021/R013/R014 impact routing.

`experiments/r015_enumeration_summary.json` records exact bounded enumeration counts and randomized/property evidence.

---

## 16. Foundation decision and Driver routing

### Mathematical theorem status

`PROVED` under the frozen result-only/current-state-sufficient relational contract.

### Executable evidence status

`EXECUTABLE_EXHAUSTIVE_PASS` on the declared bounded universes, with mutation tests and randomized extensions.

### Prior-art status

`ROOTING_SUCCESS / PRIOR_ART` for generic relation/powerset/join/Boolean machinery.

### Enterprise semantic impact

`FOUNDATION_REWRITE_CANDIDATE`:

P023's semantic taxonomy should later distinguish `FUNCTIONAL_SAFE`, `SUPPORT_SAFE`, and `SUPPORT_UNSAFE`; deterministic descent should become one stronger safety class rather than the only exact result-support class.

### Canonical status

`NOT_CANONICAL`.

R015 itself makes no canonical R009/P023 change. The independent R016 Lean formalization gate remains a separate required evidence lane before any Driver-authorized foundation rewrite.

### Non-dispatchable next-step candidate after both R015/R016 gates

Only after Driver audits both gates should a later task ask whether a specific arithmetic unresolved collapse carrier is correct and sufficient. That task must prove the carrier from arithmetic/collapse semantics; R015 provides only the generic execution theorem **conditional on having a correct current state**.

---

# Final R015 return

`RESULT_SUPPORT_BRANCH_DEFERRAL_PROVED / EXECUTABLE_EXHAUSTIVE_PASS / FOUNDATION_REWRITE_CANDIDATE / NOT_CANONICAL`
