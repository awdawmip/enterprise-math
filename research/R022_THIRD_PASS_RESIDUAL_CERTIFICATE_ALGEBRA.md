# R022 Third-Pass Deepening — Residual Join Certificate Algebra and Exact Branch-Basis Hardness

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `THIRD_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

The second pass separated positive recoalescence certificates (RCC), context-scoped no-completion certificates (CS-NCC), and heuristic budget truncation.

The third pass finds a more general exact object:

**Residual Join Certificate (RJC)**.

For Boolean/final-support semantics, RCC and CS-NCC are not separate algebraic mechanisms. They are special cases of exact rewrites that preserve the join of residual future-support signatures.

This gives a clean answer to the deeper "0 / 1 / many worlds" question:

- **0 worlds** when the residual join is bottom/empty;
- **1 world** when the target residual join is representable by one admissible token;
- **k > 1 worlds** when at least k admissible tokens are required to generate the target join.

The important negative result is equally strong:

> For an explicit finite residual language and a fixed dictionary of admissible branch tokens, finding a minimum-cardinality exact residual basis already contains SET COVER.

Therefore the universal exact `branch_budget_optimizer` is NP-hard in the generic explicit-signature model. Pairwise dominance, maximal-antichain pruning, or arbitrary local redundant-branch deletion are not complete algorithms for exact minimum width.

The algebraic laws themselves are standard finite join-semilattice / powerset semantics, not new mathematics. The Enterprise Math residue is the BRC-specific typing, certificate scope, source instantiation, exact-vs-heuristic budget boundary, and compiler architecture.

New generic executable artifacts:

- `experiments/r022_residual_certificate_algebra.py`
- `experiments/r022_residual_certificate_algebra_results.json`
- `tests/test_r022_residual_certificate_algebra.py`

Focused third-pass validation: **8/8 tests pass** in the local Python execution used for this checkpoint.

---

## 1. Scoped residual signatures

Fix a semantic scope

`omega = (stage t, context kappa, residual language U, observable o, semantics=SUPPORT)`.

For a branch token `b`, define its residual support signature

`phi_omega(b) : U -> P(Y)`,

where `phi_omega(b)(u)` is the final observable support reachable from `b` under residual future `u`.

Let

`L_omega = P(Y)^U`

with pointwise union `vee` and bottom `bottom`.

For a finite live branch configuration `C`, define

`J_omega(C) = vee_{b in C} phi_omega(b)`.

This is exactly the declared final-support semantics of the live configuration.

Important: this definition is **support-only**. Multiplicity, probability, provenance, signed weight or score require a different aggregation algebra and cannot be silently imported.

---

## 2. Residual Join Certificate (RJC)

### Definition

An **RJC** for a rewrite

`C => D`

under scope `omega` is evidence that

`J_omega(C) = J_omega(D)`.

The rewrite may remove branches, identify equal branches, replace several branches by a different admissible token, replace one branch by several, or perform any finite configuration rewrite, provided the residual join is unchanged.

### Immediate exactness theorem

If `C => D` has an RJC under `omega`, then the rewrite preserves declared final result support for every residual future in `U`.

This is definition-level once `phi_omega` is the complete residual support signature. For cheaper local signatures, a separate factorization/congruence proof is still required, exactly as in R021/R023.

---

## 3. Algebraic characterization

Let `Conf(B)` be finite branch configurations with union.

Then

`J_omega : Conf(B) -> L_omega`

is a join-homomorphism:

`J(C union D) = J(C) vee J(D)`.

Define

`C ~=_omega D iff J_omega(C) = J_omega(D)`.

Then:

1. `~=_omega` is an equivalence relation;
2. it is a congruence under configuration union;
3. RJC rewrites compose transitively;
4. the quotient of configurations by this congruence is represented by the image of `J_omega`.

This is standard semilattice kernel/congruence structure. R022 does **not** claim this algebra as novel. Its value is that it places all exact BRC branch reduction operations inside one typed semantic law.

---

## 4. RCC and CS-NCC become special cases

### 4.1 RCC = idempotence

If `phi(a) = phi(b)`, then

`phi(a) vee phi(b) = phi(a)`.

Hence `{a,b} => {a}` is an RJC.

This is the algebra behind HashClash connector `sort -> unique` under fixed context and existence/support semantics.

### 4.2 CS-NCC = bottom elimination

If a context-scoped failure certificate proves `phi(dead) = bottom`, then

`phi(a) vee bottom = phi(a)`,

so `{a,dead} => {a}` is an RJC.

The second-pass dependency-footprint/invalidation rule remains necessary because `phi` is context-relative.

### 4.3 Pairwise dominance = absorption

If `phi(a) <= phi(b)` pointwise, then

`phi(a) vee phi(b) = phi(b)`,

so `a` may be removed when `b` remains.

This is a stronger exact pruning rule than bottom-only NCC.

---

## 5. New primitive: collective residual dominance

Pairwise dominance is not complete.

A branch `b` is **collectively dominated** by survivor set `D` when

`phi(b) <= vee_{d in D} phi(d)`.

Then `D union {b} => D` has an RJC.

### Minimal counterexample

Use one residual future `u` and branch supports

- `A = {1,2}`
- `B = {1,3}`
- `C = {2,3}`.

No branch support is contained in any single other branch. Therefore pairwise dominance removes nothing.

But `A <= B union C`, `B <= A union C`, and `C <= A union B`.

Any one branch may be deleted, and every two-branch subconfiguration has the same total support `{1,2,3}` as all three.

Thus exact BRC compression is not exhausted by equal-signature recoalescence, empty-cone pruning, pairwise subset dominance, or maximal-antichain retention.

---

## 6. Residual Join Basis (RJB)

Fix an admissible token dictionary `D`.

For target residual element `z` define

`nu_D(z) = min |S|`

over finite `S subseteq D` such that

`vee_{s in S} phi(s) = z`.

For a live configuration `C`, use target `z = J(C)`.

Call a minimum `S` a **Residual Join Basis (RJB)**.

This gives the local exact "0 / 1 / many worlds" normal form relative to an explicit admissible dictionary:

- `nu_D(z)=0` iff `z=bottom`;
- `nu_D(z)=1` iff one admissible token carries exactly the target join;
- `nu_D(z)>1` otherwise.

Important: `nu_D` is dictionary-relative. If arbitrary exact union tokens may be synthesized for free, width is trivially one. Therefore every width theorem must charge token dictionary/denotation/constructor cost, consistent with R021's no-free-metadata rule.

---

## 7. Exact branch-basis minimization contains SET COVER

### Reduction

Take an arbitrary SET COVER instance with universe `E` and subsets `S_1,...,S_m`.

Construct a BRC residual-basis instance with:

- one residual future word `u`;
- final result set `Y = E`;
- one admissible branch token `b_i` per subset;
- `phi(b_i)(u) = S_i`;
- starting configuration containing all `b_i`.

Then the target residual join is `union_i S_i`.

A subconfiguration preserves the exact residual join iff its corresponding subsets cover that target. Therefore a minimum-cardinality exact existing-token residual basis is exactly a minimum Set Cover.

Consequences for the explicit finite-signature model:

- minimum exact branch-basis optimization is NP-hard;
- the decision version is in NP and inherits NP-completeness from SET COVER;
- weighted token/storage costs immediately yield a weighted-cover variant;
- a generic exact ABB cannot be expected to have a universal efficient optimizer without additional structure.

Richard Karp's 1972 `SET COVERING` NP-completeness result is the relevant classical root (`Reducibility Among Combinatorial Problems`, DOI `10.1007/978-1-4684-2001-2_9`).

This is a negative result about universal optimization, not about BRC exactness.

---

## 8. Local irredundance is not global minimum

A second finite kill test uses six pairwise-incomparable branch supports:

- `S0={0}`
- `S1={1,2}`
- `S2={1,3}`
- `S3={1,4}`
- `S4={2,3}`
- `S5={2,4}`.

The full target is `{0,1,2,3,4}`.

There are exact irredundant bases of different sizes:

- width 3, e.g. `{S0,S2,S5}`;
- width 4, e.g. `{S0,S1,S2,S3}`.

Thus an algorithm that repeatedly removes *some* currently redundant branch can terminate at a locally irredundant but globally nonminimum basis.

In the executable witness:

- removing `S4`, then `S5`, leaves the width-4 local basis;
- removing `S1`, then `S3`, then `S4`, reaches a width-3 optimum.

So exact local pruning order is itself an optimization issue.

---

## 9. Certificate scope is monotone only toward a smaller future language

If an RJC is valid for residual language `U`, it remains valid after restricting to `U' subseteq U`, because equality of full signatures implies equality after projection.

The converse fails.

Synthetic witness:

- `x` and `y` both produce `{ok}` on future `short`;
- on future `long`, `x` produces `{x-only}` and `y` produces `{y-only}`.

Then `{x} ~= {y}` for language `{short}` but not for `{short,long}`.

Therefore every cached RJC/RJB certificate must record its residual language or a sufficient language-version identifier.

This is the positive-certificate analogue of the second-pass CS-NCC context invalidation rule.

---

## 10. Idempotence is semantics-dependent

The HashClash connector can erase duplicate residual states because the relevant semantics is existence/support.

Under support aggregation, `x vee x = x`.

Under multiplicity/count aggregation, `1 + 1 != 1`.

Synthetic witness:

- two branches each contribute final support `{ok}`;
- support-only merge `{p,q} => {p}` is exact;
- path multiplicity changes from 2 to 1.

Therefore duplicate recoalescence is not a representation-independent law; it relies on an idempotent aggregation semantics.

For multiplicity/provenance-sensitive BRC, either retain the branches, attach a multiplicity/provenance weight/token, or use a different algebra whose aggregation preserves the declared observable.

This supports R023's deliberate decision to keep the Lean core Boolean/result-support only.

---

## 11. Free aggregate-token synthesis trivializes width

The three-branch collective-dominance example has minimum existing-token basis width 2.

If the compiler is allowed to synthesize a new token `UNION = {1,2,3}` at zero cost, the same residual semantics has width 1.

Nothing substantive was gained; the full target denotation was hidden inside the synthesized token.

Therefore exact branch width is meaningful only relative to an admissible token family, token construction rules, token/denotation bits, transition implementation cost, and decoder/reconstruction cost.

This is another form of R021's "free subset atom" kill criterion.

---

## 12. Practical compiler consequence: normalize cheap laws before solving the hard basis problem

The third-pass result suggests a staged exact reducer.

### Layer 1 — cheap canonical reductions

1. **RCC hash-consing:** merge equal residual signatures;
2. **CS-NCC:** remove certified bottom cones;
3. **pairwise dominance:** remove `a` when one survivor `b` satisfies `phi(a)<=phi(b)`;
4. reuse context/language-scoped certificate caches with explicit invalidation.

These are local and easy once signatures/certificates are available.

### Layer 2 — collective exact reduction

Search for `phi(a) <= vee D` or directly solve a bounded RJB problem.

This is where general Set-Cover hardness enters.

### Layer 3 — resource mode

If exact RJB optimization is too expensive:

- `EXACT`: use bounded/exhaustive/ILP/SAT optimization with proof/certificate;
- `REPLAY_EXACT`: evict branches with recoverable checkpoints and charge replay;
- `HEURISTIC`: approximate cover/ranking/beam-like pruning, explicitly dropping exact-support claims.

This integrates directly with the second-pass ABB typing.

---

## 13. Prefix-scoped failure certificates remain structurally easier

The Set-Cover hardness result concerns overlapping **positive residual support signatures** in a general admissible dictionary.

CS-NCC reuse has additional structure.

If dependency footprints satisfy prefix refinement

`delta_{b+1} refines delta_b`,

then equality classes at depth `b+1` refine those at depth `b`.

Hence context-scoped failure regions across depths form a nested refinement hierarchy. A certified empty parent cone makes all descendant branch instances empty as well.

This explains why source-style prefix failure caching can be implemented as a trie/refinement-cache even though unrestricted positive residual-basis minimization is NP-hard.

R022 does not claim that every HashClash dependency mask globally forms a perfect laminar family; the theorem is conditional on a cumulative/prefix-monotone footprint definition.

---

## 14. Prior-art/rooting outcome

The generic mathematics substantially roots to established areas:

| R022 third-pass object | Established root | Enterprise Math residue |
|---|---|---|
| pointwise union of residual support | powerset / Boolean semantics | explicit BRC scope and branch typing |
| RJC congruence | join-semilattice congruence/kernel | executable branch-rewrite certificate |
| minimum residual basis | Set Cover / weighted Set Cover | exact branch-budget formulation |
| abstract joins / approximation | abstract interpretation | exact-vs-heuristic collapse boundary |
| duplicate merge | idempotent aggregation / memoization | observable-typed RCC |
| empty branch prune | bottom elimination / nogood pruning | context-scoped CS-NCC |
| prefix certificate cache | decision-tree/trie/memoized failure | dependency-footprint invalidation contract |

Useful classical roots:

- R. M. Karp, `Reducibility Among Combinatorial Problems`, 1972, DOI `10.1007/978-1-4684-2001-2_9`.
- P. Cousot and R. Cousot, `Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints`, POPL 1977, DOI `10.1145/512950.512973`.

No claim is made that RJC or the join algebra is new mathematics.

---

## 15. Direct R021 feedback

R021 should add a representation/execution layer below its semantic core.

### New certificate type

`ResidualJoinCertificate(scope, lhs_configuration, rhs_configuration, join_signature, proof)`

with scope including stage, context/dependency footprint, residual language, observable/semantics, and admissible token dictionary/version.

### New local width quantity

`residual_join_basis_width = nu_D(J(C))`.

It is exact, dictionary-relative, support-semantic, and NP-hard to minimize in the general explicit finite model.

### New optimizer warnings

- `pairwise dominance complete = false`;
- `locally irredundant = globally minimum` is false;
- `duplicate branch merge` requires idempotent aggregation.

R023's Boolean support core should remain unchanged; multiplicity/provenance belong in a stronger typed carrier.

---

## 16. Candidate tool disposition

### Promote as R022/R021 research-tool candidate

`residual_join_normalizer`

Input:

- finite branch configuration;
- residual signature oracle;
- semantic scope;
- admissible token dictionary;
- optional costs.

Output:

- RCC/CS-NCC/pairwise-dominance reductions;
- collective-dominance witnesses;
- minimum exact basis for bounded instances;
- exact rewrite certificate;
- lower/upper resource bounds;
- explicit `EXACT / REPLAY_EXACT / HEURISTIC` mode.

### Do not claim

- a new generic Set-Cover solver;
- universal polynomial minimum-width BRC;
- branch width independent of token dictionary;
- support-idempotent merge for multiplicity/provenance semantics.

---

## 17. Third-pass classification

Recommended sharpened R022 return:

`BRC_RESIDUAL_CERTIFICATE_ALGEBRA_FOUND / RCC_NCC_UNIFIED_AS_JOIN_REWRITES / COLLECTIVE_DOMINANCE_FOUND / EXACT_BRANCH_BASIS_SET_COVER_HARD / SUPPORT_IDEMPOTENCE_BOUNDARY_CLASSIFIED / R021_FEEDBACK_READY / NOT_CANONICAL`

Interpretation:

- **positive:** BRC now has a coherent exact certificate algebra and a practical layered normalizer;
- **negative:** the algebra is standard, and globally optimal exact branch budgeting is generically combinatorial/NP-hard;
- **most useful new result:** safe exact compression is broader than pairwise merge/prune, but optimizing that broader compression is itself a hard covering problem.
