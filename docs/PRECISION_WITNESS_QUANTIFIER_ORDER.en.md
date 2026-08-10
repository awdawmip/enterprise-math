# Witness Quantifier Order Across Precision

Status: `RESEARCH BRIDGE / NONCANONICAL`

A finite-precision existence statement has a different logical shape from an exact witnessed-state statement. The gap can be decomposed into three separate quantifier/descent steps.

## 1. Starting local statement

For a labelled world law, finite precision typically gives

`for every precision M`

`there exists a local label lambda_M`

`there exists a local state x_M`

such that the local branch law holds.

Symbolically:

`forall M exists lambda_M exists x_M : P_(lambda_M)(x_M) mod M`.

This does not yet provide one label or one state that persists across precisions.

The exact target statement is instead

`exists lambda_* exists x in Z^n : P_(lambda_*)(x)=0`.

The two statements differ in both quantifier order and state space.

## 2. First exchange: precision versus witness label

The first desired normalization is

`forall M exists lambda_M`

`=>`

`exists lambda_* forall M`.

This implication is false in general.

It becomes valid under the witness-coherence hypotheses from the finite-branch theorem:

- precision supports finite joint refinement;
- admissible witness supports shrink under refinement;
- the witness space is compact (finite labels are the simplest case);
- the local quotient is branch-reflecting, so every local solution contributes an actual witness support.

Then the witness supports have the finite-intersection property and one `lambda_*` survives every precision.

This is a genuine quantifier swap, justified by compactness/coherence rather than syntax.

## 3. Failure of the first exchange: witness escape

For infinite labels `k=1,2,...` with local support

`S_M={k:M divides k}`,

we have

`forall M exists k_M`

but

`not exists k forall M`.

Every fixed label is eventually blocked, while the chosen local label grows with precision.

So a noncompact witness space can make

`forall precision exists witness`

strictly weaker than

`exists witness forall precision`.

## 4. Directedness is part of the first exchange

Even a finite witness space does not force coherence if the declared precision family cannot form joint refinements.

If only separate prime moduli are inspected, local labels at p and q need not be tested together at the lcm pq. The missing joint precision can hide incompatibility.

Thus the exchange needs a finite-intersection structure on precisions, not merely many individually fine observations.

For modular systems this is supplied by an lcm-directed family such as all moduli or one nested power ladder.

## 5. Second exchange: local branch states versus one completion state

Once a fixed label `lambda_*` survives, the statement becomes

`forall M exists x_M : P_(lambda_*)(x_M) mod M`.

For a fixed finite system of integer polynomial equations, compactness of the profinite state space gives

`exists x_hat in Z_hat^n : P_(lambda_*)(x_hat)=0`.

So for a stable branch law, separately chosen local states can be normalized into one compatible completion state.

This is the all-moduli compactness theorem.

It is not automatic if the branch law or state semantics change with precision.

## 6. Third step: completion versus exact state

The final implication is

`exists x_hat in Z_hat^n`

`=>?`

`exists x in Z^n`.

This is not a quantifier rearrangement inside one compact space. It is a **change of world** from the completion back to the exact integer state space.

It requires a route-specific descent theorem such as profinite exactness:

`closure(S_Z)=S_hat`.

Affine integer equations satisfy this.

The intersective ghost polynomial does not.

## 7. Complete normalization chain

Under the necessary guards, exact witnessed existence can be reached through:

`forall M exists lambda_M exists x_M`

`--[branch reflection + directed witness compactness]-->`

`exists lambda_* forall M exists x_M^(lambda_*)`

`--[state compactness for fixed branch]-->`

`exists lambda_* exists x_hat in Z_hat^n`

`--[branch profinite exactness/descent]-->`

`exists lambda_* exists x in Z^n`.

Each arrow has a different mathematical justification and a different failure mode.

## 8. Three sharp failure modes

### Failure A — local branch reflection

The mod15 product ghost is locally solvable but has no labelled branch mod15.

The starting `exists lambda_M` statement is already false even though the unlabelled numeric law is true.

### Failure B — witness compactness/coherence

The infinite-label escape has a labelled branch at every modulus but no one label survives all moduli.

The first quantifier exchange fails.

### Failure C — exact state descent

The intersective polynomial has one profinite state satisfying all finite precisions but no integer state.

The final descent fails.

These are different errors and require different repairs.

## 9. Fixed witness versus varying witness precision

A particularly important special case is the difference between

`exists one integer x such that for all M, P(x)==0 mod M`

and

`for all M, exists x_M such that P(x_M)==0 mod M`.

The first implies `P(x)=0` exactly because an integer divisible by every M is zero.

The second yields only a profinite witness in general.

Thus **when the witness is bound** relative to the precision quantifier is itself part of the semantics.

## 10. Foundation consequence

A future/precision system should not summarize an existential statement only by its local truth value. If the exact theory later needs the witness, the representation must preserve enough structure to justify the relevant quantifier exchanges.

The right question is not merely:

`is every finite world locally satisfiable?`

but:

`which witness variables are already bound globally, which may vary with precision, and what theorem lets those quantifiers commute?`

Compactness, finite-intersection arguments and profinite descent are standard prior mathematics. The Enterprise Math value is the explicit precision interpretation of witness-binding order.