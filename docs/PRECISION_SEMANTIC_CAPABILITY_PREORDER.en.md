# Semantic Precision as State Detail × Future Capability

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

The current research lines show that “more state detail” and “more usable future semantics” are independent precision coordinates. A raw quotient can become observationally finer while losing operations or logical laws needed by the declared future language.

This note does not introduce a new Foundation Question. It refines how precision comparisons should be routed.

## 1. Observational refinement is only one coordinate

For one representation P, let

`E(P)`

be the equivalence relation on fine states induced by its current observation/state quotient.

Smaller kernel means more state detail:

`E(P2) subseteq E(P1)`.

This is the ordinary partition/quotient notion of refinement.

It does not say which future actions, logical laws or witness semantics still descend through the representation.

## 2. Future semantic capability is a second coordinate

For one declared future theory T, let

`C_T(P)`

be the task-relevant semantic capabilities that remain safe in representation P.

Depending on the task, these may include:

- operations that preserve the quotient;
- DOMAIN/definedness channels;
- branch/witness identity reflection;
- exact IMAGE reflection under declared hypotheses;
- coefficient laws required to interpret an algebraic encoding;
- provenance/history distinctions that a future operation can reactivate.

This set is **declared-task relative**. It is not intended to list every mathematical property of P.

## 3. Task-relative semantic precision preorder

Define

`P2 >=_T P1`

iff both:

1. `E(P2) subseteq E(P1)` — P2 is observationally at least as fine;
2. `C_T(P1) subseteq C_T(P2)` — P2 loses none of the declared capabilities already available in P1.

Thus semantic refinement is a product-style preorder:

`state detail x safe future capability`.

Raw quotient refinement is only the first projection of this preorder.

## 4. Partition refinement need not preserve operation safety

A unary operation descends through a partition only when equivalent inputs map to equivalent outputs.

A finer partition can destroy that condition because two inputs may remain equivalent while their outputs become separated by the finer partition.

Conversely, a sufficiently fine/discrete partition can remove equivalence constraints and make an operation safe that was unsafe on a coarser partition.

Therefore the safe-operation spectrum is not monotone in either direction under raw partition refinement.

This is already present in the A2 safe-operation algebra line.

## 5. Coefficient refinement reproduces the same nonmonotonicity

For a prime p:

`Z/p^2 Z -> Z/p Z`

is a numeric refinement map: mod `p^2` distinguishes more residues.

But:

- mod p is a field/domain and generically reflects product-zero branch logic;
- mod `p^2` has zero divisors and loses that logical capability.

If branch semantics belongs to T, the two representations are semantically incomparable despite the raw numeric refinement.

If branch semantics is irrelevant to T, mod `p^2` may again be the relevant refinement.

The precision order is therefore genuinely future-language relative.

## 6. Forward syntax preservation does not repair lost capability

A quotient homomorphism still preserves polynomial evaluation perfectly:

`phi(t(x))=t(phi(x))`.

So a representation may preserve the written algebraic syntax while losing a reflection law needed by the exact interpretation.

This shows why capability must be recorded semantically rather than inferred from the presence of the same formula after collapse.

## 7. A semantic join may not exist inside the current representation family

Suppose one task requires both:

- numeric detail at least as fine as mod `p^2`;
- generic product-branch reflection.

Inside the representation family `Z/MZ`, numeric refinement requires

`p^2|M`.

Then M is composite, so the quotient ring is not a domain.

Therefore no scalar modulus realizes the joined requirement.

The abstract semantic join exists as a demand profile, but it is **not representable by the original scalar precision parameter**.

## 8. Nonrealizable join means the state representation must lift

To realize both requirements one must change representation type, for example retain:

- the mod `p^2` numeric residue; and
- an explicit branch/witness channel.

This gives a general architecture rule:

> **If the join of declared precision requirements is not realizable in the current representation class, increasing the old scalar precision parameter is not the solution; the state representation must be enriched or lifted.**

This is the semantic analogue of adding age/source state, witness repair, or operation-word precision when a future law can reactivate those distinctions.

## 9. Requirement joins generalize arithmetic lcm joins

Earlier modular research represented arithmetic requirements as:

`(free-separation flag ; p-adic depths)`

and combined tasks by coordinatewise join.

The semantic preorder extends this idea. A task requirement profile may contain:

- state distinctions;
- safe operations;
- DOMAIN/RELATION witness channels;
- reflection/descent guarantees;
- arithmetic depth resources.

Combining tasks means taking the join of these requirements, not adding scalar precision costs.

Some joins remain finite/modular. Others force a representation lift.

## 10. Relation to witness-semantic descent

Witness descent adds capabilities such as:

- local branch reflection;
- directed joint precision;
- compact/proper witness projection;
- profinite exactness of the fixed witnessed relation.

A representation that distinguishes more numeric states but loses one of these guards is not semantically finer for a task that later reads the witness.

So witness coherence fits naturally inside `C_T(P)` rather than requiring another independent notion of “precision.”

## 11. Foundation routing rule

When comparing two candidate precision states, do not ask only:

`which one has the finer partition / larger modulus / smaller scale?`

Ask instead:

1. Which exact state distinctions are preserved?
2. Which declared future operations still descend?
3. Which logical/witness/reflection laws remain valid?
4. Can one representation semantically dominate the other on all task-relevant coordinates?
5. If not, is a richer representation required to realize the joined demand?

This avoids treating precision as a one-dimensional quantity when the future language has several independent semantic requirements.

## 12. Prior-art boundary

Partition refinement, congruence-preserving operations, preorders and product orders are standard prior mathematics. The Enterprise Math value is the routing principle:

> **task-relative precision orders representations by both observational detail and future semantic capability; raw refinement alone is not enough.**