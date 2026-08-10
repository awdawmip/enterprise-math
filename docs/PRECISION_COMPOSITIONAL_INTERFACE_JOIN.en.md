# Independent Readout Join versus Compositional Interface Join

Status: `RESEARCH BRIDGE / NONCANONICAL`

Two semantic capabilities can be combined in at least two different ways. Merely retaining both final coarse labels is weaker than requiring both operations to continue executing on one shared quotient state space.

This distinction resolves the apparent tension in the semiring-product generation: a product representation can be overprecision for the first task and exactly the coarsest repair for the second.

## 1. One K-valued relation interface

Fix a finite state set, an initial observation partition E_0, a relation family, and coefficient semiring K.

On a current partition E, action a assigns to each target E-class C the weight

`(# raw a-successors in C) * 1_K`.

A K-interface descends on E when equivalent sources have identical K-weight vectors over the **current E-target classes** for every action.

Iterating splits by these vectors yields the unique coarsest K-stable refinement of E_0.

The fixed-point sequence agrees with the recursive K-branching signature kernels.

## 2. Independent readout join

Suppose two declared tasks require coefficient interfaces K and L separately.

Compute their individual coarsest stable quotients

`E_K`, `E_L`.

If the only requirement is:

> from the current state representation, recover the final K-label and the final L-label independently,

then the coarsest state partition is simply

`J = E_K intersect E_L`,

the ordinary joint refinement / kernel intersection.

No claim is made that either transition interface remains executable on J.

This is a **readout join**.

## 3. Why the readout join can break operation safety

Safe operation capability is not monotone under raw state refinement.

An operation can be stable on E_K because several target states share one K-class. Refining those targets using L may split that K-class. Two source states that previously sent the same K-weight into the old class can now distribute K-weight differently among the new joint classes.

Therefore K can become unsafe on

`J=E_K intersect E_L`

even though it was safe on E_K.

The same can happen symmetrically to L.

This is exactly the general safe-operation nonmonotonicity from the semantic-precision line, now realized inside a multivalued weighted relation.

## 4. Shared compositional join

A stronger task requires:

> one common quotient state space on which both K- and L-valued transition interfaces remain directly executable, so later futures can continue from the same coarse successor states.

Then the partition must be stable for **both** coefficient weight vectors measured against its own target classes.

Starting from E_0, split simultaneously by all K and L target-block weight vectors and iterate.

The fixed point

`E_comp(K,L)`

is the unique coarsest shared-state quotient supporting both operations compositionally.

Equivalently:

`E_comp(K,L) = Closure_(K,L)(E_0)`.

## 5. Exact two-stage decomposition

The same final quotient is obtained by:

1. compute E_K and E_L separately;
2. take their readout join J;
3. close J again under the joint K,L operation requirement.

Thus

`E_comp(K,L) = Closure_(K,L)(J)`.

This separates two resources:

- **static label join** — distinctions needed to recover both interface labels;
- **compositional closure** — extra distinctions needed so both interfaces remain safe after the other one's target splits are visible.

## 6. Compositional closure debt

Define

`debt_blocks`

as

`#blocks(E_comp) - #blocks(J)`.

Also record the number of strict fixed-point rounds required after J.

These are not universal complexity measures, but they quantify one exact task-relative precision tax:

> how much extra state is required solely because the two capabilities must continue to compose on one shared successor state space?

Zero debt means the independent readout join is already operation-safe for the full capability family.

Positive debt means cross-capability refinement has reactivated hidden transition differences.

## 7. Product semiring theorem

For two semirings K and L, the target-block weight in the product semiring is exactly

`(K-weight, L-weight)`.

Therefore one simultaneous K,L refinement step equals one `(K x L)` refinement step on the same current partition.

By induction their complete fixed-point sequences agree:

`E_comp(K,L) = E_(K x L)`.

Hence the direct product semiring is the **canonical coarsest coefficient representation for the coupled shared-state operation interface**.

This does not contradict the parent product-overprecision witness, because that witness compared the product against the weaker independent-readout task.

## 8. Sharp Boolean + parity debt witness

Use the parent eight-state coefficient-correlation fixture.

Individually:

- Boolean-support branching reaches a stable quotient E_B;
- mod2 parity branching reaches a stable quotient E_2;
- both keep source states p/q equivalent.

Their ordinary readout join J also keeps p/q equivalent.

But J has split several target states differently from either individual quotient. On J:

- p and q distribute Boolean support differently among the new target blocks;
- they also distribute parity weight differently.

Thus J is no longer stable for the required operations.

One additional compositional repair round separates p/q.

In this fixture:

`debt_blocks=1`,

and the post-join closure needs exactly one strict refinement round.

## 9. Morphism-ordered interfaces have zero debt

Suppose a semiring homomorphism

`phi:K->L`

makes L a coefficient quotient of K.

On any fixed partition, equality of K-weight vectors implies equality of their L-images. Therefore K-stability on that partition already implies L-stability.

Consequences:

- the K-stable quotient refines the L-stable quotient;
- the independent readout join is just the K quotient;
- adding the L capability creates no new shared-state refinement;
- compositional debt is zero.

Concrete examples:

`N -> Boolean`,

`N -> Z/MZ`.

So a richer coefficient interface can subsume its morphic quotients without interaction tax.

## 10. One dominating interface can absorb several capabilities

If a family includes exact N-count branching together with Boolean support and mod-M count, N maps homomorphically to both poorer coefficient worlds.

The shared compositional join therefore equals the N-count stable quotient itself.

No extra product correlation is required beyond what exact count branching already retains.

This gives a practical compiler rule:

> remove semiring interfaces already factored through a declared dominating interface before computing a shared-state join.

## 11. Semantic join is interface-sensitive

There is no contradiction between:

`product can be overprecision`

and

`product is the coarsest shared-state join`.

The task changed.

### Independent readout semantics

Need to know two completed answers separately.

Minimal state kernel = intersection of the two answer kernels.

### Coupled compositional semantics

Need both transition structures to operate on the same recursively usable coarse successor states.

Minimal state = joint operation-congruence closure, equivalently product-semiring branching fixed point.

Thus “join” must always specify whether future operations may compose across the joined capabilities.

## 12. Architecture consequence

A representation can be sufficient as a static readout and insufficient as a compositional state.

This distinction appears repeatedly across Enterprise Math:

- a scalar potential can answer one current query but fail Markov continuation;
- independently sufficient quotient labels can fail after their target partitions are jointly refined;
- product states can overretain correlation for static tasks but become necessary for shared dynamic continuation.

So state minimality is inseparable from the declared continuation interface.

## 13. Prior-art boundary

Congruence closure, weighted bisimulation, product semirings and partition refinement are standard prior mathematics/computer science. A4 retains relation/witness ownership; P023/A2 retains future-signature and semantic-precision ownership.

The project value is the exact routing principle:

> **independent output joins and compositional state joins are different precision problems; the gap between them is a measurable closure debt created by cross-capability continuation.**