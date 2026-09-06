# X6 upper V26: PF-10 channel nonreciprocity supplies the minimal rank-2 circulation type required by V25

Status: `FREE_RESEARCH / EXACT TYPED BRIDGE + GENERAL RECIPROCITY NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- PF-10 ideal channel state in `PACKET_PATH_FOUNDATION.md`;
- `X6_RANK2_EDGE_CIRCULATION_ODD_HOLONOMY_V25_20260906.md`;
- `X6_FOUR_FIELD_ACTIVE_TRIAD_CODE_V23_20260906.md`;
- BRC exact positive-rational weighting.
Checker: `experiments/x6_dynamic_law_holonomy_v24_20260906/check_channel_circulation_bridge.py`.

## 1. Question

V25 proves that a nonzero antisymmetric edge coupling is sufficient, and rank 2 is minimal within its affine four-field edge-score family, to sustain a deterministic active-triad loop with odd V17 holonomy.

The remaining typing question is whether such an antisymmetric object must be introduced as an entirely new primitive internal variable.

PF-10 already provides a more native source: directed ingress/egress/passage counts.

## 2. Typed four-port restriction of a PF-10 Cell

PF-10 admits, for an ideal six-channel Cell,

`I[0..5]`, `O[0..5]`, `M[a,b] in N_0`.

Do **not** identify the six channel labels with the six spatial axes merely because both cardinalities are six.

For the V23 four-field context, assume only a typed injection from the four labeled field sources into four declared internal channel/port labels. Restrict the PF-10 data to those four ports:

`I,O in N_0^4`,

`M in N_0^(4x4)`.

The remaining two PF-10 channels may retain other semantics and are irrelevant to this restricted bridge.

This source-to-port injection is required semantic interface data. It is not derived from cardinality coincidence.

## 3. Two canonical signed contrasts from nonnegative counts

Define

`u := I-O in Z^4`,

`Omega := M-M^T in Mat_4(Z)`.

Then

`Omega^T=-Omega`.

No negative primitive passage count has been introduced. Signed values occur only as exact contrasts of two admissible nonnegative event counts.

For a four-field code `c(S)` define

`Phi_{I,O,M}(S,T) = u^T c(T) + c(S)^T Omega c(T)`.

This is exactly the V25 affine edge-score family with its coefficients generated from an internal PF-10 snapshot.

For rational `rho>1`,

`W_rho(S->T)=rho^(Phi_{I,O,M}(S,T))`

is strictly positive rational. Thus positive Weighted-BRC can carry the branch masses even though the integer exponent observable is signed.

This respects the standing boundary

`POSITIVE_WEIGHTED_BRC != SIGNED_FORCE/PHASE CANCELLATION`:

the BRC weight is positive; the signed contrast is a separately typed integer relation readout.

## 4. Port-relabel covariance

Let P be any permutation matrix on the four declared source/port labels.

Transport

`c -> P c`,

`I -> P I`,

`O -> P O`,

`M -> P M P^T`.

Then

`u -> P u`,

`Omega -> P Omega P^T`.

Therefore

`Phi_{PI,PO,PMP^T}(PS,PT)=Phi_{I,O,M}(S,T)`

when `PS,PT` denote the correspondingly transported code vectors.

So no absolute source numbering is built into the formula. A particular internal state may break source symmetry, but the law is covariant when the state is transported.

## 5. General reciprocity no-go

The V24 destination-potential theorem extends to symmetric edge scores.

Let G be a finite simple undirected graph. Suppose

`Score(x,y)=U(y)+K(x,y)`

for adjacent x,y, where

`K(x,y)=K(y,x)`.

Assume the deterministic update chooses the unique maximizing neighbor.

Then no directed periodic orbit of length at least three exists.

Proof. On a putative cycle `x_i -> x_{i+1}` with length m>=3, uniqueness gives

`U(x_{i+1})+K(x_i,x_{i+1}) > U(x_{i-1})+K(x_i,x_{i-1})`.

By symmetry, the second edge term is `K(x_{i-1},x_i)`.

Summing over i makes both the U sums and K sums identical after cyclic reindexing, contradicting strict inequality.

Therefore a memoryless unique-max local law needs a **nonreciprocal / antisymmetric transition component** in order to sustain recurrent loops of length at least three.

This theorem is graph-theoretic and independent of the specific field code.

## 6. PF-10 nonreciprocity is exactly the needed type

The antisymmetric PF-10 contrast

`Omega=M-M^T`

vanishes exactly when the restricted directional passage counts are reciprocal pairwise.

If Omega vanishes, the V26 score reduces to a destination potential and V24 applies.

If a more general symmetric passage contribution is added, the reciprocity theorem above still prevents recurrent cycles of length at least three in a unique-max memoryless law unless an antisymmetric component is also present.

Thus the V25 circulation type has a direct internal interpretation:

`DIRECTED PASSAGE IMBALANCE -> ANTISYMMETRIC EDGE CIRCULATION`.

## 7. Exact PF-10 realization of the V25 odd-holonomy example

The V25 coefficients are

`u=(-3,-4,2,1)`

and

```
Omega = [[ 0,-1,-1, 0],
         [ 1, 0, 0, 0],
         [ 1, 0, 0, 0],
         [ 0, 0, 0, 0]].
```

They are realized by the nonnegative PF-10 counts

`I=(0,0,2,1)`,

`O=(3,4,0,0)`,

and passage matrix M with only

`M[1,0]=1`,

`M[2,0]=1`,

all other restricted entries zero.

Then exactly

`I-O=u`,

`M-M^T=Omega`.

So the rank-2 circulation that drives the V25 odd-holonomy six-cycle requires only two directed passage occurrences in this minimal witness.

Again, this does not claim those numerical counts are forced by P000 or are a calibrated physical equilibrium. It proves the **type-level mechanism is already available inside PF-10**.

## 8. Internal-state consequence

The upper architecture now has a concrete path from nonnegative Cell-local relation counts to nontrivial active-triad holonomy:

`PF10 INGRESS/EGRESS/PASSAGE COUNTS`

`-> signed contrasts (u,Omega)`

`-> four-field exact Weighted-BRC edge score`

`-> unique active-triad relation update`

`-> nonzero edge circulation`

`-> V17 S3 holonomy / Ori6 control`.

The internal counts remain a fiber over the spatial Cell. They are not extra spatial dimensions.

## 9. What remains open

The bridge now removes the need to invent a new abstract circulation type.

Still open are:

1. what dynamical law updates `(I,O,M)` after an event;
2. what typed physical relation binds the four field-source labels to four PF-10 ports;
3. whether triadic atomic closure, time dependency or neighboring Cells force a preferred passage imbalance rather than merely permitting one;
4. how unequal force quanta modify the internal counts and branch weights;
5. which port summaries remain operation-safe under future channel-sensitive queries.

The highest-leverage next step is therefore to derive an **update law for the channel-count state itself**, rather than adding further static internal coordinates.
