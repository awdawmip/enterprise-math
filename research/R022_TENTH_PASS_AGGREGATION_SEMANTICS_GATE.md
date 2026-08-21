# R022 Tenth-Pass Deepening — Aggregation-Semantics Gate for Recoalescence

**Researcher-ID:** `EM-R022-HC7B4A`  
**Task:** `RS-R022-HASHCLASH-BRC-TOOL-MINING`  
**Taskbook base:** `89fb6c99fa2a00e42f58c1fc11ea016b7421f3be`  
**Owner PR:** `#497`  
**Status:** `TENTH_PASS / RESEARCH ADDENDUM / NOT CANONICAL`

## Executive result

R022/R023 deliberately use Boolean/final-result-support semantics as the default exactness target. Pass 10 identifies exactly which BRC recoalescence laws depend on that choice.

Let residual branch meanings live in a commutative monoid

`(M, ⊕, 0)`

and define configuration semantics by aggregating branch values with `⊕`.

Then:

- pruning a branch whose semantic value is `0` is monoid-generic;
- forgetting one of two equal residual values is exact exactly when the reachable value is idempotent, `s ⊕ s = s`;
- universal forgetful duplicate recoalescence is exact exactly when all reachable residual values are idempotent;
- under non-idempotent multiplicity semantics, equal branches may still be grouped, but the multiplicity coefficient must be retained;
- absorption/dominance/Set-Cover interpretations require additional idempotent semilattice/distributive structure and are not generic commutative-monoid laws.

Thus RJC is not the universal BRC aggregation algebra. It is the idempotent/join-semilattice specialization of a more general **Residual Aggregate Certificate**.

This explains exactly why HashClash connector `sort -> unique` is safe for the declared existence/support question yet would be wrong for path multiplicity or named provenance.

Recommended classification:

`BRC_AGGREGATION_SEMANTICS_GATE_FOUND / DUPLICATE_FORGET_IFF_IDEMPOTENT / MULTIPLICITY_COEFFICIENT_REQUIRED / ZERO_PRUNE_MONOID_GENERIC / PROVENANCE_STRENGTHENING_KILL / NOT_CANONICAL`.

---

## 1. General residual aggregate semantics

Let each live branch `b` have semantic value

`v(b) in M`.

For a finite branch multiset/configuration `C`, define

`A(C) = ⊕_{b in C} v(b)`.

A proposed rewrite

`C -> D`

is exact for this declared aggregation semantics iff

`A(C) = A(D)`.

Call an independently checkable witness of this equality a **Residual Aggregate Certificate (RAC)**.

When `M` is a join-semilattice and `⊕=join`, RAC reduces to the RJC algebra from pass 3.

## 2. Identity pruning is generic

If a branch has residual semantic value `0`, then

`x ⊕ 0 = x`.

So removing a true zero-contribution branch is exact in every monoid.

This is the generic algebraic core behind an empty-support NCC prune.

However, proving that a branch value is actually `0` remains context/language/observable relative; CS-NCC supplies that proof in the Boolean support setting.

## 3. Duplicate-forgetting criterion

Suppose two branches have exactly the same residual semantic value `s`.

Replacing both by one copy changes aggregate

`s ⊕ s`

to

`s`.

Therefore the rewrite is exact iff

`s ⊕ s = s`.

### Universal Duplicate-Forgetting Theorem

Forgetful duplicate recoalescence is valid for every reachable equal-value pair iff every reachable semantic value is idempotent.

### Necessity

Apply the rule to configuration `[s,s]`.

### Sufficiency

Associativity, commutativity and idempotence allow repeated equal occurrences to be deleted without changing the aggregate.

This is the exact semantic law used implicitly by Boolean-support duplicate elimination.

## 4. Boolean support and min/max score

### Boolean/final-support

`M=P(A)`, `⊕=union`, `0=empty`.

Union is idempotent:

`S union S = S`.

So duplicate residual support branches can be forgotten when no stronger observable such as multiplicity/provenance is declared.

### Best-score-only semantics

For a tropical-style `min` aggregate,

`min(s,s)=s`.

Thus duplicate equal score values may likewise be forgotten if only the optimum score itself is observable.

If the identity of every optimum witness is also observable, the semantic value must be strengthened and the simple scalar `min` model no longer captures the target.

## 5. Multiplicity semantics kills forgetful duplicate merge

For path/result multiplicity:

`M=N` or a count-vector monoid,

`⊕=+`.

Then generally

`s+s != s`.

Minimal witness:

- two equal branches each contribute count 1;
- total multiplicity is 2;
- forgetting one produces 1.

So the HashClash-style `unique` operation would not preserve multiplicity.

This is not a bug in HashClash: its connector is solving an existence/support problem, not preserving the number of predecessor histories.

## 6. Coefficient-preserving recoalescence

Non-idempotent semantics can still compress repeated equal residual values without forgetting them.

Represent

`k copies of s`

as a grouped token

`(s,k)`

with interpretation

`k . s = s ⊕ ... ⊕ s` (`k` times).

For natural multiplicity this is ordinary multiplication/counting.

Example:

four equal contributions of value 3:

`3+3+3+3 = 12`.

Grouped representation `(3,4)` also denotes 12.

So the correct distinction is:

- **forgetful recoalescence** — remove multiplicity, requiring idempotence;
- **coefficient-preserving grouping** — compress representation while retaining multiplicity metadata.

The second is a representation optimization, not semantic erasure.

## 7. Provenance strengthening boundary

Two branches may be equal under support semantics while unequal under provenance semantics.

Support-only values:

`{ok}`, `{ok}`.

Their union is `{ok}`; one copy may be forgotten.

If the observable is strengthened to history provenance:

`{h1}`, `{h2}`,

then forgetting one produces only `{h1}` instead of `{h1,h2}`.

A combined provenance token `{h1,h2}` is exact, but its metadata explicitly retains the distinction.

Therefore “equal residual token” is always typed by the declared semantic carrier. Equality at a weaker observable does not imply equality after observable strengthening.

This aligns with passes 6 and 9: future/observable strengthening creates refinement debt.

## 8. Algebraic gate for BRC rewrite laws

The candidate compiler should gate rewrite laws by aggregation semantics.

### Monoid-generic

- identity/zero-contribution prune;
- exact aggregate-equality verification;
- coefficient grouping when the coefficient action is represented faithfully.

### Requires idempotence

- forget equal duplicate semantic values;
- treating branch configurations as sets instead of multisets.

### Requires idempotent ordered semilattice structure

- absorption/dominance;
- collective dominance;
- monotone support-cover reasoning.

### Requires distributive/join-prime support structure

- pass-7 canonical frontier / exact Set-Cover macro interpretation.

This produces an explicit hierarchy of semantic assumptions instead of silently importing Boolean laws into stronger observables.

## 9. Executable evidence

Artifact:

`experiments/r022_aggregation_semantics_gate.py`.

Focused tests verify:

1. Boolean union duplicate forgetting: exact;
2. natural-number multiplicity duplicate forgetting: inexact;
3. min-score duplicate forgetting: exact;
4. multiplicity coefficient grouping: exact;
5. identity/bottom pruning across union, natural addition and min aggregation: exact;
6. provenance strengthening kills support-only forgetfulness while an explicit union-provenance token repairs it.

Focused pass-10 tests: **4/4 PASS** in the research execution environment.

## 10. Relation to HashClash

The source-backed positive recoalescence witness in `md5_connect_bits` remains valid under R022's declared existence/final-support semantics:

- duplicate `connect_bitdata` states are semantically identical for the residual connector feasibility question under fixed context;
- the continuation only needs existence/support, not predecessor multiplicity;
- therefore idempotent duplicate elimination is appropriate.

R022 must not extrapolate this source behavior into a theorem about count/provenance preservation.

## 11. Relation to R023

No change to R023 is requested.

R023 intentionally formalized only Boolean/result-support semantics and excluded multiplicity, provenance, probability/weights and signed/amplitude carriers.

Pass 10 explains why that scoping was mathematically important: the central `SUPPORT_BRANCH_INVARIANT` and forgetful recoalescence laws use an idempotent support aggregate.

Any future stronger carrier should receive a separate theorem family with its own aggregate laws rather than silently generalizing the Boolean theorem statements.

## 12. Tool delta

### `aggregation_semantics_gate`

Declare:

- aggregate carrier `M`;
- operation `⊕` and identity;
- whether reachable values are idempotent;
- whether coefficients/multiplicity are represented;
- whether an order/absorption law is available;
- whether a distributive/join-prime frontier theorem is available.

Enable compiler rewrites only when their algebraic preconditions are met.

### `residual_aggregate_verify`

Independently verify aggregate equality for explicit finite candidate rewrites, analogous to proof-carrying RJC verification.

### `coefficient_group`

Group equal residual semantic values while preserving the multiplicity coefficient instead of applying forgetful `unique`.

## 13. Prior-art/rooting boundary

Commutative monoids, idempotent semirings, weighted automata, multiplicity/counting semantics, tropical aggregation and provenance semirings are established areas. R022 claims no generic novelty for these algebraic facts.

The Enterprise Math residue is the explicit semantic gate telling the BRC compiler which recoalescence/pruning/cover laws remain legal under which declared observable, and relating that gate back to the concrete HashClash source witness and R023's deliberately Boolean scope.

## 14. R021 feedback

Recommended additions:

1. Type every branch configuration by its aggregation semantics, not only its branch carrier.
2. Generalize RJC conceptually to an aggregate-equality certificate, while retaining RJC as the Boolean/join specialization.
3. State duplicate-forgetting iff reachable aggregate values are idempotent.
4. Keep zero-contribution pruning as the monoid-generic negative rule.
5. For multiplicity, replace forgetful duplicate merge with coefficient-preserving grouping.
6. Disable dominance/Set-Cover fast paths unless idempotent order/distributive preconditions hold.
7. Treat provenance/observable strengthening as a new semantic carrier and charge the resulting refinement debt/replay requirement.
8. Do not modify R023 Boolean Lean statements to absorb stronger carriers; create separate theorem families if needed later.

## 15. Tenth-pass classification

`BRC_AGGREGATION_SEMANTICS_GATE_FOUND / RESIDUAL_AGGREGATE_CERTIFICATE_GENERALIZATION / DUPLICATE_FORGET_IFF_IDEMPOTENT / MULTIPLICITY_COEFFICIENT_REQUIRED / ZERO_PRUNE_MONOID_GENERIC / PROVENANCE_STRENGTHENING_KILL / R021_FEEDBACK_READY / NOT_CANONICAL`.

Cumulative compiler picture after ten passes:

`declared observable/aggregate -> future language -> required precision kernel -> semantic frontier where available -> executable carrier macros -> proof-carrying exact rewrite -> aggregation-gated recoalescence -> quotient-descending operations -> context/language certificate reuse -> future precision debt -> store metadata or replay`.
