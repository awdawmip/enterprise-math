# Task-Relative Semantic Precision Is a Preorder, Not One Scalar

Status: `RESEARCH BRIDGE / NONCANONICAL`

Several current routes show the same negative boundary: a representation can distinguish more raw states while supporting fewer future operations or logical laws. Therefore observational refinement alone is not a sufficient definition of “more precise” for a declared task.

## 1. Two independent coordinates

For a representation P relative to future theory T, separate:

### Observational equivalence

`E(P)` records which fine states remain indistinguishable.

A representation P2 is observationally finer than P1 when

`E(P2) subseteq E(P1)`.

For partitions, every P2 block lies inside a P1 block.

### Semantic capability

`C_T(P)` is the set of declared task capabilities that genuinely descend through P, for example:

- safe operations;
- branch/witness reflection;
- exact IMAGE reflection under a stated bound;
- DOMAIN legality channels;
- coefficient laws needed by the future language.

The vocabulary is task-relative rather than universal.

## 2. Semantic refinement preorder

Define

`P2 >=_T P1`

iff both:

1. `E(P2) subseteq E(P1)`;
2. `C_T(P1) subseteq C_T(P2)`.

Thus a semantic refinement must never lose an already-required declared capability while making state distinctions at least as fine.

This is a product-style preorder on **state detail × semantic capability**.

## 3. Finer state partition can lose a safe operation

Take state set `{0,1,2,3}`.

Coarse partition:

`{0,1,2}|{3}`.

Finer partition:

`{0,1}|{2}|{3}`.

Let unary operation t satisfy

`t(0)=0`, `t(1)=2`, `t(2)=0`, `t(3)=3`.

On the coarse quotient, the whole first block maps back into the same coarse block, so t descends safely.

On the finer quotient, states0 and1 are still equivalent but their images0 and2 are not. Therefore t is unsafe.

Hence raw partition refinement can remove safe-operation capability.

The reverse can also happen: a discrete refinement removes equivalence constraints and can make an operation safe that was unsafe on a coarser partition.

So the safe-operation spectrum is not monotone in either direction under raw partition refinement.

## 4. Coefficient refinement gives the same tradeoff

For one prime p, there is a quotient map

`Z/p^2 Z -> Z/p Z`.

Therefore mod `p^2` is numerically finer than mod p.

But:

- mod p is a field/domain and generically reflects product-zero branch logic;
- mod `p^2` has zero divisors and does not.

If the declared task reads both numeric residues and labelled product branches, neither representation semantically dominates the other:

- mod `p^2` has more numeric detail;
- mod p has a logical capability that mod `p^2` lacks.

They are semantically incomparable.

## 5. Raw “higher precision” can therefore be task-relative

If the task only observes residues and never reactivates product-branch semantics, mod `p^2` is the relevant refinement of mod p.

If the task requires branch reflection, that raw numeric order no longer determines semantic precision.

Thus precision order depends on the future language, exactly as P023 requires.

The same pair of representations may be ordered for one task and incomparable for another.

## 6. Abstract joins may not be realizable in one representation class

The abstract semantic join of two requirements can demand both:

- mod `p^2` numeric detail;
- generic integral-domain product-branch reflection.

Restrict representations to scalar integer quotients `Z/MZ`.

To numerically refine mod `p^2`, one needs

`p^2 | M`.

Then M is composite, so `Z/MZ` is not a domain.

Therefore **no scalar modulus realizes the abstract semantic join**.

This is stronger than incomparability: the desired least common refinement lies outside the original representation family.

## 7. Semantic precision can force a representation lift

To realize both capabilities, the state must be lifted or factorized, for example by retaining:

- the mod `p^2` numeric residue; and
- an explicit branch/witness label or relation channel.

The solution is not “choose a larger modulus.” It is “change what the state carries.”

This is a general precision-lift pattern:

`required semantic join not realizable in current representation class`

`=> enrich/lift representation rather than extrapolate one scalar precision axis`.

## 8. Relation to safe-operation algebra

The safe-operation monoid attached to a quotient is derived from which operations preserve its equivalence classes.

A finer partition is not guaranteed to preserve the safe-operation family of a coarser one. Therefore quotient detail and operation language were already separate coordinates in the safe-operation line.

Coefficient branch reflection shows the same architecture on a different surface.

The common lesson is:

> **precision must include what future operations/laws remain executable, not only how fine the current observational partition is.**

## 9. Capability sets are declarations, not universal truth tables

The semantic capability set should contain only distinctions relevant to the declared task/future theory.

For one task, “field product-branch reflection” may be irrelevant and should not block a numeric refinement.

For another, it may be essential.

This avoids turning the semantic preorder into an impossible order over every mathematical property of a representation.

## 10. Precision joins and world design

A semantic requirement profile can be viewed as a demand vector:

- state distinctions that must survive;
- operations that must descend;
- witness/reflection laws that must remain valid;
- coefficient/depth resources that must be available.

Combining tasks takes a join of requirements. If no existing representation realizes that join, the correct world-design move is to add the missing state/witness channel or change representation type.

Thus “precision increase” can be a structural state-space refinement, not merely a larger denominator/modulus/cutoff.

## 11. Prior-art boundary

Partition refinement, congruence-preserving operations, product preorders and quotient-ring properties are standard prior mathematics. The Enterprise Math value is the task-relative semantic ordering and the explicit nonrealizable-join boundary across state and coefficient precision.