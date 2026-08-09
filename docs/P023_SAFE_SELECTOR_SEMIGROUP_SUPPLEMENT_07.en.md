# P023 — Safe-Selector Stable Equivalence, Supplement 07

Status: `ACTIVE RESEARCH NOTE`  
Scope: stable equivalence of safe-precision selector words  
Depends on: P023 Stage 2 safe-precision interior and P020 finite stabilization  
Discipline: semigroups of monotone/idempotent operators and common fixed-point iteration are established mathematics. This note records the exact Enterprise Math precision interpretation and the stable-equivalence bridge to P019-style collapse words.

## 1. Motivation

Stage 2 gives, for every finite deterministic operation family `A`, a safe-precision selector

\[
S_A(E)=\operatorname{Safe}_A(E),
\]

which returns the largest `A`-compatible equivalence relation contained in the input precision relation `E`.

Each selector is monotone, reductive and idempotent.

A natural question is whether several requirements can be enforced by applying their individual selectors once in sequence. Stage 2 gave an explicit counterexample: one pass can depend on order and can even destroy compatibility with a selector processed earlier.

The correct question is therefore dynamical:

> if one fixes a selector word and repeats the **same whole word**, what is its finite stable value?

## 2. Setup

Let

\[
S_1,\ldots,S_m
\]

be safe selectors corresponding to finite operation families

\[
A_1,\ldots,A_m.
\]

Define one selector word

\[
W=S_m\circ\cdots\circ S_1.
\]

Every `S_i` is monotone and reductive on the finite poset of equivalence relations refining the chosen finite state space.

Let

\[
A_\cup=A_1\cup\cdots\cup A_m.
\]

## 3. P023-S3-T01 — Fixed points of a selector word are exactly common fixed points

Status: `PROVED`.

For every precision relation `E`,

\[
\boxed{
W(E)=E
\iff
S_i(E)=E\text{ for every }i.
}
\]

Equivalently,

\[
\boxed{
\operatorname{Fix}(W)
=
\bigcap_i\operatorname{Fix}(S_i)
=
\operatorname{Fix}(S_{A_\cup}).
}
\]

### Proof

Because every selector is reductive,

\[
W(E)
\subseteq
S_{m-1}\cdots S_1(E)
\subseteq\cdots\subseteq
S_1(E)
\subseteq E.
\]

If `W(E)=E`, the first and last elements of this descending chain are equal. By antisymmetry every intermediate relation equals `E`. In particular `S_1(E)=E`. Repeating the same argument through the intermediate equalities gives `S_i(E)=E` for every `i`.

The converse is immediate: if every selector fixes `E`, so does their composition.

Finally, `S_i(E)=E` means exactly that `E` supports all operations in `A_i`; satisfying every `i` is equivalent to supporting their union. ∎

Notice that idempotence of the individual selectors is not needed for the fixed-word implication itself; reductivity is enough. Idempotence identifies each selector's fixed points with the relevant compatibility requirement.

## 4. P023-S3-T02 — Repeated selector word stabilizes to the joint safe precision

Status: `PROVED` for finite state spaces.

The word `W` is monotone and reductive because it is a composition of monotone reductive maps. The equivalence-relation poset is finite. Therefore P020 finite stabilization applies.

For every initial precision `E_0`, finite iteration of `W` reaches the greatest `W`-fixed relation below `E_0`.

Using T01,

\[
\boxed{
\operatorname{stab}_W(E_0)
=
S_{A_\cup}(E_0).
}
\]

So repeated sequential enforcement of a fixed word eventually reaches the same coarsest common-safe precision as simultaneous family closure.

## 5. P023-S3-T03 — Stable output is independent of selector order

Status: `PROVED` for finite state spaces.

Take two selector words that contain the same operation requirements, possibly in different order and with arbitrary repetition. If the union of required operation families is the same, their fixed-point sets are the same by T01. P020 therefore selects the same greatest fixed point below every initial precision.

Hence

\[
\boxed{
\operatorname{stab}_{W_1}(E)
=
\operatorname{stab}_{W_2}(E)
}
\]

whenever `W_1` and `W_2` contain the same selector requirements.

Transient refinement paths can still differ substantially. Stage 2's five-state witness has different first-pass results for `F→G` and `G→F`, but the second repeated pass in either order reaches the same discrete common-safe partition.

Thus:

\[
\boxed{
\text{one-pass order matters; stable safe precision does not.}
}
\]

## 6. P023-S3-T04 — Stable-equivalence semigroup collapses to union of requirements

Status: `PROVED` at the finite selector-family level.

Define two selector words to be **stably equivalent** when their repeated action has the same stabilized input-output map on every finite initial precision relation.

By T02–T03, the stable class of a word depends only on the union of operation requirements appearing in the word.

Under concatenation, these unions combine by set union:

\[
\boxed{
[W_A]\,[W_B]
\longmapsto
A\cup B.
}
\]

Repetition is absorbed:

\[
A\cup A=A,
\]

and order disappears:

\[
A\cup B=B\cup A.
\]

Therefore the stable-equivalence quotient of the finite safe-selector word semigroup is an idempotent commutative join structure indexed by finite operation-requirement sets.

This is structurally parallel to P019, where transient collapse-word order may differ while stable equivalence is controlled by the lcm of exponent requirements. Here the stable invariant is not an lcm; it is the union of future-operation requirements.

## 7. Why this does not contradict the Stage 2 no-go

Stage 2 disproved the shortcut

\[
S_B(S_A(E))=S_{A\cup B}(E)
\]

in general.

Supplement 07 proves instead

\[
\boxed{
\operatorname{stab}_{S_B\circ S_A}(E)
=S_{A\cup B}(E).
}
\]

The distinction is exactly the difference between one transient word application and finite stabilization of the fixed word.

This is the same discipline already used elsewhere in Enterprise Math: transient nonconfluence does not imply distinct stable maps.

## 8. Executable audit

`src/enterprise_math/p023_selector_semigroup.py` implements:

- one application of a selector word;
- repeated fixed-word stabilization;
- the joint operation-family safe selector;
- fixed-word/common-compatibility auditing.

`tests/test_p023_selector_semigroup.py` includes:

- the five-state order-dependent one-pass witness;
- verification that both repeated orders reach the same joint safe precision;
- exhaustive three-state testing over every pair of deterministic maps and every binary initial observation;
- fixed-point/common-compatibility checks over finite partitions;
- finite class-count termination auditing.

Finite checks audit the implementation. T01–T04 follow from reductivity, fixed-point characterization and P020 finite stabilization.

## 9. Next question

The selector-word result suggests two sharper directions:

1. formalize the fixed-point intersection/stable-word theorem abstractly for monotone reductive endomaps, so P019 collapse words and P023 selector words share one reusable theorem;
2. study whether the `regular scale + localized bounded detail` precision objects from Stage 2 admit efficient canonical representation under repeated union of operation requirements, without expanding into arbitrary database-like indexing.
