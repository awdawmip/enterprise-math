# Quadratic Packet Native One-Clock Self-Composition — Independent Semantic Audit RAW

Status: `FROZEN RAW / BLIND-FORWARD / SOURCE-UNEXPOSED`

Researcher-ID: `EM-QPNCA-4F0348`

Task-ID:

`RS-QUADRATIC-PACKET-NATIVE-ONE-CLOCK-COLLAPSE-BRIDGE-INDEPENDENT-AUDIT`

Hard target:

`NC3_OBSERVABLE_COMPLETE_SELF_COMPOSITION_INDEPENDENTLY_DERIVED_NARROWED_OR_REFUTED_WITH_SEMANTIC_CIRCULARITY_AUDITED`

Primary raw verdict (taskbook vocabulary):

`REFUTED`

Frozen-packet verdict mapping:

`REFUTED_BY_ADMISSIBLE_COUNTERMODEL`

Outcome class:

`KILL` for NC3/OCSC as a consequence of the declared S1+S2 sector plus ordinary predictive/composition-complete semantics.

This raw verdict is frozen before opening the originating theorem, originating candidate/Phase-B audit, prior QP-R2 source work, or higher-residual source work.

## 0. Independence and input provenance

The blind-forward mathematical audit used only:

1. the frozen OCSC packet content from commit `3383d7c94ac9eb65f8d64e2c74448b5cfb0e9e2a`;
2. the Foundation snapshot explicitly whitelisted by that packet: `main@1c71c3ee6c4fb483c27f2f72e445ccc83a392824` files `FOUNDATIONAL_LOGIC.md`, `PACKET_PATH_FOUNDATION.md`, `native_semantics_admissibility.json`, `lineage_e002_predictive_quotient.json`, `lineage_p023_safe_quotient.json`, and `lineage_p020_wellfounded.json`;
3. elementary finite deterministic-system reasoning.

No withheld route proof/audit/source mathematics was opened before this freeze.

### Input-pin integrity defect

The dispatch/taskbook metadata names

`research_inputs/QUADRATIC_PACKET_NATIVE_ONE_CLOCK_SELF_COMPOSITION_SEMANTIC_AUDIT_PACKET_20260825.md`

with claimed blob

`8f5e5a6866bde5381e4d9e4fec4463c8b9753b7c`.

However, the dispatch also pins frozen input commit `3383d7c94ac9eb65f8d64e2c74448b5cfb0e9e2a`, and that commit freezes the packet under the actual path

`research_inputs/QUADRATIC_PACKET_OBSERVABLE_COMPLETE_SELF_COMPOSITION_INDEPENDENT_AUDIT_PACKET_20260825.md`

with repository blob

`72c43ee09b81d4d53e75e7e800b5da0f0206e1bc`.

The metadata-named path is absent at the frozen commit/owner head, and the claimed `8f5e5a...` object could not be resolved through the connected repository service. I therefore do not fabricate equality of the pins. The semantic audit below is tied to the unique packet actually frozen by the dispatch-pinned commit. This provenance defect requires separate control-plane correction if exact blob-pin integrity is a later acceptance gate; it does not supply or alter any mathematical premise below.

## 1. Ambient system and declared sector predicates

Let

`C=(X,0,c)`

be finite, deterministic, pointed, and satisfy `c(0)=0`. Put

`X* = X \ {0}`

and

`R_j = c^j(X*) ∩ X*`.

I treat the packet's task-local sector predicates exactly as declared:

### S1 — one-clock

`|X* \ R_1| = 1`.

Operational reading: there is exactly one nonzero source state with no nonzero predecessor under `c`.

This is a defensible graph-theoretic meaning of “one-clock”, but it is only a source-count statement. It is not an observable-capacity bound and does not say that there is only one nonzero predictive state type.

### S2 — genuine finite downward collapse

`c` is nontrivial on `X*`, and every `x∈X*` reaches `0` after finitely many iterations.

Operational reading: the nonzero transition graph is finite and acyclic toward the distinguished absorbing state `0`.

This is a defensible downward/well-founded sector typing. It is a termination condition, not a depth-two condition.

## 2. Explicit non-circular operational semantics

Fix a declared observation map

`o : X -> A`.

For each state define its full future observation trace

`T_o(x) = ( o(c^k(x)) )_{k>=0}`.

Define future equivalence

`x ≡_o y  <=>  T_o(x)=T_o(y)`.

Let

`q : X -> Q = X/≡_o`

be the coarsest full-future predictive quotient.

These definitions do not mention `R_2`, residual depth two, quadratic/rank-two structure, or the desired NC3 conclusion.

### Primitive

A declared state language is **primitive for the future language** when its predictive state object is the coarsest quotient sufficient to reproduce every declared future observation and the induced transition. Equivalently, no strict quotient preserves all declared future predictions.

This is behavioral minimality, not “has no `R_2` layer”.

### One-clock

For this task, one-clock means S1 above: exactly one nonzero source in the finite deterministic transition graph.

It does not mean “at most two nonzero predictive states” unless that extra capacity statement is separately declared.

### Observable state capacity

The observable predictive capacity of `(C,o)` is the number/type structure of states in the minimal predictive quotient `Q` (or its nonzero part when the zero class is excluded).

Capacity is derived from the declared future language; it is not inferred from the number of graph sources.

### Self-composition completeness

The declared language is **self-composition complete** when repeated application of `c` is representable on the same predictive state object without any refinement of `Q`.

Formally, there exists

`c_bar : Q -> Q`

such that

`q ∘ c = c_bar ∘ q`,

and the declared future observations are read from iterates of `c_bar`.

For full-future equivalence this factorization is automatic: equality of future traces is preserved by left shift, so `x≡_o y` implies `c(x)≡_o c(y)`.

This is a genuine operational closure condition and does not encode NC3.

### Hidden residual precision

A residual distinction is hidden relative to the declared language if two implementation states are identified by the declared state descriptor but some allowed future self-composition distinguishes them. In quotient notation, hidden precision exists if the proposed descriptor identifies `x,y` while some future observation of `c^k(x),c^k(y)` differs.

The minimal full-future predictive quotient has no such hidden distinction by construction.

### Legitimate additional observable type vs hidden/redundant state

A distinction is a **legitimate additional predictive type** when two states have different declared future traces and hence must remain in different classes of `Q`.

A distinction is **hidden implementation state** when it is not represented in `Q` but would be needed to predict a declared future.

A label is **redundant presentation state** when different labels lie in the same future-equivalence class and the dynamics factors through that identification.

Thus “there are several residual depths” is not by itself evidence of hidden precision. The question is whether those depths are predictively distinguishable in the declared future language.

## 3. Structural lemma: S1+S2 force a chain, but do not bound its length

### Lemma

Every finite pointed deterministic system satisfying S1 and S2 has its nonzero states arranged in a single directed chain

`x_{m-1} -> x_{m-2} -> ... -> x_1 -> x_0 -> 0`

for some `m>=1`.

### Proof

S2 makes the directed graph on `X*` acyclic, with every nonzero state having exactly one outgoing edge toward eventual absorption at `0`.

Suppose some nonzero state had two distinct nonzero predecessors. Following predecessor chains backward from those two predecessors must terminate, by finiteness and acyclicity, at two distinct nonzero states with no nonzero predecessor. Those would be two distinct elements of `X*\R_1`, contradicting S1.

Hence every nonzero state has at most one nonzero predecessor.

Now take any nonzero state and follow predecessors backward until a source is reached. S1 says the source is unique, so every nonzero state lies on the forward orbit of that unique source. Therefore the whole nonzero graph is one chain. QED.

### Consequence

For the chain of `m` nonzero states,

`R_j = {x_0,...,x_{m-1-j}}`

for `0<=j<m`, so

`|R_j| = m-j`,

and every nonempty residual level strictly shrinks:

`R_{j+1} proper-subset R_j`.

Therefore S1+S2 admit chains of arbitrary finite depth. Neither one-source typing nor well-foundedness supplies a two-step bound.

## 4. The `J_3` countermodel

Take

`X={0,x_0,x_1,x_2}`

with

`c(0)=0`,

`c(x_0)=0`,

`c(x_1)=x_0`,

`c(x_2)=x_1`.

Then

`R_1={x_0,x_1}`,

`R_2={x_0}`,

`R_3=empty`.

Hence

`empty proper-subset R_2 proper-subset R_1`.

S1 holds because

`X*\R_1={x_2}`.

S2 holds because every nonzero state reaches `0` in at most three applications.

### A defensible primitive observable language

Use the minimal instantaneous observation

`o(0)=0`,

`o(x_0)=o(x_1)=o(x_2)=1`.

So the only immediate observable asks whether the system is still unresolved/nonzero. Do not add a depth label by hand.

Under repeated self-composition, the full future traces are

`T_o(0)   = 0000...`,

`T_o(x_0) = 1000...`,

`T_o(x_1) = 1100...`,

`T_o(x_2) = 1110...`.

All four traces are distinct. Therefore the coarsest predictive quotient is the identity quotient: all four states are behaviorally necessary for the declared future language.

Consequently `J_3` is simultaneously:

- one-clock under S1;
- finite and downward under S2;
- primitive/minimal for the declared future observation language;
- self-composition complete, because `c` already acts on the minimal predictive states and all iterates remain representable without refinement;
- free of hidden residual precision relative to that language, because every future-distinguishable state is already represented;
- composition-safe, because the predictive quotient is a forward congruence;
- well-founded and finitely stabilizing;
- nevertheless equipped with a proper nonempty intermediate residual `R_2`.

This is an admissible finite countermodel to NC3/OCSC under non-circular operational meanings of the audited terms.

## 5. Longer-residual pressure: the entire `J_m` family survives

For every `m>=3`, define

`J_m : x_{m-1}->x_{m-2}->...->x_0->0`.

With the same binary nonzero observation `o`, the future trace of `x_i` is exactly `i+1` leading `1` symbols followed by zeros. Thus all nonzero depths are pairwise future-distinguishable.

The coarsest predictive quotient is again the identity. Hence every `J_m` is primitive/minimal for that declared future language, self-composition complete, composition-safe, one-source, and well-founded.

But for every `m>=3`,

`empty proper-subset R_2 proper-subset R_1`.

So `J_3` is not a corner case. There is an unbounded family of countermodels.

## 6. Why predictive minimization does not imply NC3

The coarsest future-predictive quotient preserves exactly the distinctions required by the declared future language. It does not minimize the number of time-to-absorption stages subject to an external depth bound.

For `J_m` with the binary nonzero observation, remaining lifetime is observable through repeated composition, so each depth has a distinct future trace. Merging two depths destroys prediction of the future zero/nonzero sequence.

Therefore predictive minimality can require arbitrarily many residual depths. It gives no route to `R_2=empty` and no route to a depth-two capacity bound.

## 7. Why composition-safe quotient semantics do not imply NC3

The exact generic condition for deterministic self-composition to descend through a quotient `q` is

`q(x)=q(y) => q(c(x))=q(c(y))`.

Equivalently, `ker(q)` is forward invariant and `c` factors as `c_bar` on the quotient.

This condition controls legality of composition after information loss. It says nothing about the height of the quotient transition graph.

The identity quotient of every `J_m` satisfies it, and the minimal future-predictive quotient in the binary-observation example is exactly that identity quotient.

Thus composition-safe factorization and predictive sufficiency both survive arbitrarily long residual chains. The missing ingredient for NC3 is an independent capacity/height restriction, not factorization.

## 8. Why well-founded stabilization does not imply NC3

S2 already gives well-founded finite stabilization at `0`. Well-foundedness asserts that a descending process terminates; it does not assert that it terminates in at most two nonzero stages.

`J_m` is well-founded for every finite `m`.

Therefore finite stabilization/well-foundedness cannot derive NC3 without an additional uniform height bound.

## 9. The relabeling branch does not rescue the claim under S2

The frozen NC3 form allows

`R_2=empty`

or

`R_2 ~= R_1`

under an allowed type-preserving relabeling.

Under the ordinary mathematical meaning of relabeling as a bijection of the finite declared residual state language, `R_2 ~= R_1` requires equal finite cardinality.

But in every S1+S2 chain while `R_2` is nonempty,

`|R_2|=|R_1|-1`.

More generally, a nonempty finite residual set cannot be carried bijectively onto a strictly later residual level indefinitely under a well-founded collapse without creating a nonterminating invariant part.

Hence, under ordinary bijective relabeling, the second branch is unavailable in the nonempty downward case and NC3 effectively reduces to a depth bound `R_2=empty`, i.e. chain length at most two nonzero stages.

If `~=` is instead intended to ignore cardinality and compare only a coarser externally declared “type”, that type quotient must be specified independently. Otherwise the phrase can be made true by defining away exactly the residual distinction under audit, which is semantic circularity rather than derivation.

## 10. Strictly weaker non-circular replacement for the self-composition role

The operational content genuinely needed to say “repeated self-composition introduces no undeclared predictive state” is not NC3. A strictly weaker invariant principle is:

### FCSC — Future-Complete Self-Composition

For a fixed declared observation/future language, let `q:X->Q` be its minimal predictive quotient. Require:

1. **observation sufficiency**: all declared observations factor through `q`;
2. **composition congruence**: `q(x)=q(y)` implies `q(c(x))=q(c(y))`;
3. **minimality**: no strict quotient of `Q` preserves 1 and 2 together with all declared future predictions.

Equivalently, repeated self-composition is represented by one fixed induced map `c_bar:Q->Q`, and no refinement of `Q` is ever required to predict the declared future language.

FCSC is invariant under allowed relabelings because it depends only on the behavioral quotient and conjugacy class of the induced transition, not on coordinates, basis, matrices, or carrier labels.

FCSC is strictly weaker than NC3: every `J_m` with the binary nonzero future language satisfies FCSC, while every `J_m` for `m>=3` violates NC3.

FCSC exactly separates “hidden state appears under composition” from “the already-declared predictive state machine has more than two residual depths”. The latter is not a compositional defect.

### If a two-stage result is genuinely required

Then an additional statement must be declared explicitly, for example:

`OBSERVABLE_HEIGHT_2: the minimal future-complete predictive quotient has no nonzero state after two induced self-compositions.`

That is a falsifiable sector capacity axiom. It is not a consequence of primitive/minimal predictive completeness, one-source typing, factorization, or well-foundedness. Calling it “complete” does not derive it.

## 11. Semantic circularity audit

There are two non-circular meanings of the pressured terms:

- `primitive` = minimal sufficient predictive quotient;
- `complete under self-composition` = closed/factorizable state descriptor sufficient for all declared future compositions.

Under those meanings, NC3 is false by `J_3` and `J_m`.

NC3 becomes derivable only if one strengthens a premise to something equivalent to a depth/capacity exclusion, e.g.:

- “primitive means no composition-distinct residual beyond the first residual”; or
- “complete means the second image is empty or type-identical to the first”; or
- “observable capacity is at most two nonzero composition stages”.

The first two are direct target leakage. The third is a legitimate additional axiom, but then the proof of NC3 is just unpacking that extra capacity declaration.

Thus the explanatory claim “NC3 follows from primitive + complete” is circular unless a strictly weaker, independently justified capacity certificate is supplied.

## 12. Foundation-snapshot comparison available inside the blind packet

The whitelisted current Foundation semantics support the negative result rather than NC3:

- Foundational logic forbids copying a desired output condition into a native premise and calling recovery a derivation.
- Native admissibility requires future-language typing and rejects target leakage.
- Predictive quotient semantics provide behavioral minimality, but no residual-depth-two theorem.
- Composition-safe quotient semantics provide factorization/congruence, but no height bound.
- Well-founded finite stabilization provides eventual termination, but no two-step termination bound.

Therefore no currently whitelisted weaker Foundation principle derives NC3 at its frozen exact strength.

## 13. Sector boundary

This verdict is only about the task-local finite deterministic one-clock/downward sector and the semantics of NC3/OCSC within it.

It does not universalize to recurrent systems, arbitrary packet/path dynamics, Boolean BRC, all N0 relations, or any algebraic/rank-two output.

The countermodel does not say a two-stage sector is illegitimate. It says that such a sector must be separately declared/justified; it is not forced by the audited words “primitive”, “one-clock”, “downward”, or “observable-complete”.

## 14. Raw conclusion

The kill condition in the taskbook is met.

`J_3` is an explicit finite model satisfying defensible primitive, one-clock, downward, observable-complete and composition-safe semantics while retaining

`empty proper-subset R_2 proper-subset R_1`.

Moreover, `J_m` gives an unbounded family of such models.

Therefore the frozen NC3/OCSC statement is **not** independently derivable from the weaker native semantics available in the blind phase. Its Foundation-facing explanatory status is refuted.

The strongest surviving non-circular self-composition principle is the weaker behavioral condition FCSC. Any genuine depth-two conclusion requires an explicit additional observable-capacity/height axiom.

Frozen primary raw verdict:

`REFUTED`

Frozen packet-class mapping:

`REFUTED_BY_ADMISSIBLE_COUNTERMODEL`

No originating/source-side material has been consulted at this freeze boundary.
