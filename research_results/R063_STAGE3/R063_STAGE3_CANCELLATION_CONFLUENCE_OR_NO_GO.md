# R063 Stage 3 — Cancellation Confluence / No-Go

Status: `COUNT_LEVEL_CONFLUENT / POSITION_LEVEL_NONCONFLUENT_WITH_MINIMAL_WITNESS`
Researcher-ID: `EM-R063S3-F1CF9D`

## Count-level normal form

For a `C4` count vector `(n0,n1,n2,n3)`, cancellation removes opposite labels `(0,2)` and `(1,3)`. Every rewrite reduces total cardinality by two, so termination is immediate. The two signed differences

`x=n0-n2`, `y=n1-n3`

are invariants. The unique commutative-count normal form has counts

`(max(x,0), max(y,0), max(-x,0), max(-y,0))`.

Hence signed cancellation is confluent after forgetting positions.

## Position-retaining rewrite is not confluent

At process level retain the product partial order inherited from source positions and delete the two selected opposite-labelled cells. Different maximal cancellations may leave different induced residual posets.

The smallest exact witness is

`p=iij`, `q=ij` (component traces `(2,1)` and `(1,1)`), a `3 x 2` rectangle.

There are two `+X_i` cells, one `-X_i` cell and three `+X_j` cells. Maximal cancellation leaves one of the two positive `X_i` cells. The two residual posets have respectively **one** and **two** minimal elements, so they are not isomorphic even as plain posets. Their target linearization supports are respectively

`{ijjj}`

and

`{ijjj, jijj}`.

Thus cancellation pairing changes the representative-level normal form and its path readout.

## Minimality

Positional ambiguity requires both `ac>0` and `bd>0` and unequal signed-channel populations with a majority of at least two. Therefore both source traces must contain both letters. The only smaller positive two-letter rectangle is `2 x 2`, where necessarily `(1,1)x(1,1)` gives one positive and one negative `X_i`, leaving no positional survivor. The `3 x 2` witness is minimal by interaction-cell count.

## Strongest choice-free survivor

No unique pairing is forced by the frozen semantics. A minimum-first and a maximum-first rule, for example, are both deterministic rules on the same inherited order and both preserve the count theorem while giving different residual readouts. Selecting either would add process-selection semantics.

The canonical object is instead the finite set `NF(P)` of **all** maximal residual induced subposets. Taking the union of their order-respecting linearizations yields a choice-free relation without inventing a matching selector.

`SIGNED_CANCELLATION_TRACE_NORMAL_FORM_EXACT = true`.

`POSITION_RETAINING_CANCELLATION_REWRITE_CONFLUENT = false`.
