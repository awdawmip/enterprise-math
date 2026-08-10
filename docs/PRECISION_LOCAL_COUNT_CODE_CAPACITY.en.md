# Local Coefficient-Code Capacity for Exact Branching Precision

Status: `RESEARCH BRIDGE / NONCANONICAL`

Exact natural-count branching does not require the coefficient semiring to be the natural numbers themselves.

For a relation family with bounded one-step outdegree, it is enough that the declared coefficient interface **encode the finite local count alphabet injectively**.

This yields a complete necessary-and-sufficient theorem and a concrete notion of reflection capacity for coefficient capability joins.

## 1. Natural count code of a semiring

Let K be a commutative semiring. The raw successor count n enters K through the canonical natural map

`eta_K(n)=n*1_K`.

For maximum raw outdegree Delta, one weighted branching refinement step can only use counts

`0,1,...,Delta`.

Thus only the restriction

`eta_K | {0,...,Delta}`

matters for exact local count reflection.

## 2. Universal exactness theorem

For all finite relation systems with maximum outdegree at most Delta:

`K-branching refinement = exact N-branching refinement`

at every stage

iff

`eta_K` is injective on `{0,...,Delta}`.

### Sufficiency

On any current partition, every source-to-target-block coefficient lies in the finite alphabet `0..Delta`.

Injectivity means equality of K-weight vectors is exactly equality of natural-count vectors.

Therefore one K-refinement step equals one N-refinement step on every partition. Induction gives identical full refinement sequences and fixed points.

### Necessity

If distinct `r,s<=Delta` have

`eta_K(r)=eta_K(s)`,

construct same-observation sources x,y with respectively r and s distinct successors, all in one current behavioural target class.

Exact N sees different coefficients and splits x/y.

K sees the same code and merges them.

So every local code collision yields an explicit worst-case relation counterexample.

## 3. Reflection capacity

Define the universal local count capacity of K as the largest Delta for which

`eta_K` is injective on `0..Delta`.

This is not a global information capacity of the semiring. It is a task-specific branching reflection threshold.

For one fixed world, realized exactness can hold above this threshold if the colliding local counts never occur in a future-relevant configuration.

## 4. Boolean support capacity

For Boolean OR/AND:

`eta_B(0)=0`,

`eta_B(n)=1` for every `n>=1`.

Therefore:

`capacity(B)=1`.

Boolean support is universally exact for deterministic/partial branching where each source/action has at most one successor, and generically loses multiplicity once outdegree can reach2.

This recovers the deterministic-collapse boundary from the branching-support route.

## 5. Modular count capacity

For `K=Z/MZ`:

`eta_K(n)=n mod M`.

The values `0,...,M-1` are distinct and M collides with0.

Hence:

`capacity(Z/MZ)=M-1`.

The earlier finite modular cutoff theorem `M>Delta` is exactly the statement

`Delta <= capacity(Z/MZ)`.

## 6. Boolean × modular synergy

Take

`K=B x Z/MZ`.

The natural code is

`n -> ([n>0], n mod M)`.

Now count M no longer collides with0:

- 0 -> `(0,0)`;
- M -> `(1,0)`.

The first new collision is

`1` versus `M+1`,

both mapping to `(1,1)`.

Therefore:

`capacity(B x Z/MZ)=M`.

Boolean support adds exactly one universal count level beyond pure modular precision.

This is a genuine capability synergy: the product can reflect a larger local exact world than either channel separately.

## 7. Sharp support + parity example

For M=2:

| count | support | parity | pair |
|---|---:|---:|---:|
| 0 | 0 | 0 | (0,0) |
| 1 | 1 | 1 | (1,1) |
| 2 | 1 | 0 | (1,0) |
| 3 | 1 | 1 | (1,1) |

Boolean alone has capacity1.

Parity alone has capacity1.

Together they have capacity2.

The owner regression exhausts every pair of relations on a two-state set, under constant and identity observations, and verifies that the coupled Boolean×parity branching refinement equals exact N at the full outdegree2 bound.

At outdegree3 the pair fails sharply on counts1 versus3.

## 8. Finite modular families combine by lcm

For moduli `M_1,...,M_k`, the product natural code is the tuple

`(n mod M_1,...,n mod M_k)`.

Two natural numbers have the same tuple exactly when they are congruent modulo

`L=lcm(M_1,...,M_k)`.

Therefore:

`capacity(product_i Z/M_iZ)=L-1`.

This is the local-count version of the modular coefficient join theorem.

Adding Boolean support gives:

`capacity(B x product_i Z/M_iZ)=L`.

Again support separates0 from the first positive multiple L, while `1` and `L+1` remain the next sharp collision.

## 9. Coefficient capability joins can increase reflection power

A semantic capability join is therefore not merely the union of two labels.

When the channels are kept in one **coupled compositional coefficient interface**, their joint code can distinguish local exact values that neither channel distinguishes alone.

This is different from independent readout join:

- independent readout only promises both completed answers separately;
- coupled product preserves the joint local code on each current target class and supports recursive execution.

The capacity theorem applies to the latter.

## 10. Capacity and compositional debt are different phenomena

Two coefficient interfaces can interact in at least two ways.

### Reflection synergy

Their joint natural code is more injective on local count values than either code alone.

Example: Boolean + parity.

### Compositional closure debt

Even when two final interface labels are separately available, their ordinary state join can become transition-unsafe and require further refinement.

These are logically distinct:

- capacity concerns **value reflection on one target block**;
- debt concerns **cross-capability continuation after target partition refinement**.

A representation family may exhibit either, both, or neither.

## 11. Worst-case collision compiler

Given any semiring K and degree bound Delta, the executable layer searches the finite local alphabet for the first code collision

`r<s<=Delta`, `eta_K(r)=eta_K(s)`.

If one exists, it constructs a relation world whose first refinement distinguishes exactly r versus s in natural counts and merges them in K.

Thus failure of the injectivity criterion always has a concrete bounded A4 witness.

## 12. Relation-specific realized precision

The universal capacity is intentionally conservative.

A fixed relation system may be exact with a semiring whose generic capacity is below its maximum raw outdegree because:

- colliding counts never appear on equivalent source states;
- colliding target blocks are already observation-separated;
- later future structure makes the collision irrelevant to the declared quotient.

Therefore retain the distinction:

`universal code capacity`

versus

`realized exact precision of one world`.

## 13. Prior-art boundary

Finite coding, CRT, semiring products and weighted partition refinement are standard prior mathematics/computer science. A4 retains relation/witness ownership; P023/A2 retains future-signature and semantic-precision ownership.

The project value is the exact theorem:

> **a coefficient interface is universally exact for count branching up to outdegree Delta iff its natural-number code is injective on the finite local count alphabet `0..Delta`; coupled capability joins can strictly increase this reflection capacity.**