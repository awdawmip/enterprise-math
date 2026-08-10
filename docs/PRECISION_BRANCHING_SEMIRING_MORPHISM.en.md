# Branching Semiring Morphisms and Structural Trace Folds

Status: `RESEARCH BRIDGE / NONCANONICAL`

Support, exact multiplicity and modular multiplicity can be placed in one recursive branching framework by changing the coefficient semiring carried by each successor behavioural type.

The same framework also exposes a crucial negative boundary: a coefficient product is a common refinement of two views, but can preserve extra cross-view successor correlation and therefore fail to be their coarsest semantic state join.

## 1. K-valued branching signatures

Choose a commutative semiring K.

A raw relation has one unit contribution for every distinct source-target pair. At branching depth h, group target states by their depth-h K-behavioural type and add one in K for every raw target in that type.

Thus each action stores a finitely supported K-valued function on child behavioural types.

Important cases:

- `K=N`: exact number of raw successors of each behavioural type;
- `K=B`: presence/absence of each type;
- `K=Z/MZ`: successor multiplicity modulo M;
- product semirings: paired coefficient capabilities.

## 2. Semiring morphisms induce recursive coarse maps

Let

`phi:K->L`

be a semiring homomorphism.

To map one K-branching signature to L:

1. recursively map every child K-signature to its L-signature;
2. map every coefficient by phi;
3. if several richer child types collapse to one L-child type, add their mapped coefficients in L;
4. drop resulting zero coefficients.

This recursively defined map commutes exactly with direct construction from the raw relation.

Therefore:

`beta^K_h(x)=beta^K_h(y)`

implies

`beta^L_h(x)=beta^L_h(y)`.

So the K-branching partition always refines its homomorphic L-image.

## 3. Concrete coefficient quotient: N -> Boolean

The positivity map

`n |-> [n>0]`

is a semiring homomorphism from natural counts to Boolean OR/AND.

Its recursive branching image is exactly the support branching signature from the parent A4 generation.

Hence the earlier count-to-support theorem is not an isolated recursion: it is one instance of the general coefficient-morphism rule.

## 4. Concrete coefficient quotient: N -> Z/MZ

Reduction

`n |-> n mod M`

is also a semiring homomorphism.

It produces a modular branching world in which successor multiplicities are remembered only modulo M.

Unlike Boolean support, modular count can annihilate a genuinely nonempty successor class. Example mod2:

- zero successors -> coefficient0;
- two equivalent successors -> coefficient0.

Thus modular branching and support branching encode different capabilities even though both are quotients of exact natural counts.

## 5. Branching coefficient quotient and terminal trace fold are different operations

Given a K-branching signature and literal word w, compute the terminal K-valued trace recursively:

- empty word contributes `1_K` to the current observation;
- for first action a, multiply each child suffix trace by that child-type coefficient;
- add over all child types.

This exactly reproduces raw K-semiring path execution.

Therefore there is a horizontal structural map

`K-branching -> K-terminal-word trace`.

This map is not a coefficient quotient. It folds successor grouping by semiring multiplication/addition along the word.

## 6. The coefficient/trace commuting square

For semiring morphism `phi:K->L`, the two routes commute:

`K branching --trace--> K word traces`

`    | phi_*                 | phi`

`    v                       v`

`L branching --trace--> L word traces`.

The reason is exactly preservation of zero, one, addition and multiplication by phi.

This separates two possible information losses:

1. **vertical coefficient loss** — K to L;
2. **horizontal structural loss** — branching grouping to terminal trace aggregation.

They are independent axes.

## 7. Boolean support and parity count are incomparable views

Compare the natural count maps

`N -> B`

and

`N -> Z/2Z`.

They are not ordered by factorization.

- counts0 and2: Boolean distinguishes absent/present, parity merges them;
- counts1 and2: parity distinguishes, Boolean merges them.

Hence neither coefficient view determines the other on unbounded natural multiplicities.

This is another exact example where “more precise” is task-relative rather than one scalar coefficient order.

## 8. Product semiring gives a common refinement

The product coefficient world

`B x Z/2Z`

stores both presence and parity of each successor behavioural type.

Projection to either coordinate is a semiring homomorphism, so product branching refines both Boolean-support branching and parity branching.

For raw successor counts0,1,2,3 the product values are:

- 0 -> `(0,0)`;
- 1 -> `(1,1)`;
- 2 -> `(1,0)`;
- 3 -> `(1,1)`.

Thus the product retains the joined coefficient capabilities but remains coarser than exact N-counts.

## 9. Direct product branching can overretain cross-capability correlation

A subtle new boundary appears at deeper branching horizons.

Suppose child behavioural types are classified separately by:

- their Boolean-support future behaviour;
- their parity-count future behaviour.

A direct `B x Z/2Z` child type records **which Boolean type and parity type belong to the same successor**.

But a task that merely requires both complete interfaces side by side only needs:

- the full Boolean branching signature; and
- the full parity branching signature.

It need not retain their per-successor pairing.

### Sharp witness

Construct three possible child product-types:

- A = `(Boolean-empty, parity-zero)`;
- C = `(Boolean-present, parity-zero)`;
- D = `(Boolean-present, parity-one)`.

Let source p have raw child counts

`A=1, C=0, D=1`.

Let q have

`A=2, C=1, D=1`.

Then the separate Boolean views agree:

- A-type is present;
- a Boolean-present type is present.

The separate parity views also agree:

- total parity-zero child count is odd in both cases;
- parity-one child count is odd in both cases.

So p/q are equivalent in each complete coefficient interface, and remain equivalent in the ordinary state-partition join of those two interfaces.

But their direct product branching signatures differ, because the product remembers the detailed A/C/D pairing and multiplicity pattern.

The executable branch realizes this with an eight-state depth-two relation fixture.

Therefore:

`direct coefficient product branching`

can be strictly finer than

`coarsest state partition retaining both separate branching interfaces`.

## 10. Representation product is not automatically semantic join

This is the same architectural warning seen elsewhere in Enterprise Math:

> combining two sufficient representations by taking their raw product can silently retain correlation that neither declared task asks for.

A product is a safe upper bound, not automatically a minimal joined precision.

If the task truly needs cross-capability correlation on the same successor branch, the product detail is justified.

If it only needs the two interfaces independently, retaining that pairing is overprecision.

Thus semantic requirement join and representation product must be distinguished.

## 11. Generic factorization principle

The current hierarchy is best viewed as two commuting but independent choices:

### Branching coefficient world

Choose K and coefficient morphisms between K-worlds.

### Structural observation interface

Choose whether the future retains branching structure or folds it into word traces.

Changing either choice can change the state kernel.

A scalar “relation precision” cannot summarize both axes.

## 12. Prior-art boundary

Semiring-weighted automata, weighted bisimulation, coalgebra morphisms, product semirings and trace semantics are standard prior mathematics/computer science. A4 retains relation/witness ownership; P023/A2 retains future-signature/precision ownership.

The project value is the explicit precision diagram:

> **coefficient morphisms and trace folds are different coarse maps, they commute under semiring homomorphisms, and even a categorical coefficient product can overretain task-irrelevant successor correlation.**