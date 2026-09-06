# X6 upper V21: one pure-triadic field is insufficient for deterministic active-triad dynamics or Ori6 bias

Status: `FREE_RESEARCH / EXACT FINITE-SYMMETRY NO-GO + BRC RELATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`;
- BRC relation/provenance semantics.
Checker: `experiments/x6_single_triadic_field_nogo_v21_20260906/check_single_triadic_field_nogo.py`.

## 1. Question

V20 gives a canonical five-dimensional pure-triadic field and an exact S6-covariant contextual coupling.

Can one **single static neighboring pure-triadic field**, together with the current active three-axis context, already define a deterministic S6-equivariant next active triad and thereby generate V17 holonomy/Ori6 control?

For the smallest nonzero V18 field family the answer is no, for exact finite-symmetry reasons.

## 2. Canonical minimal field state

Choose one perfect matching

`M={{a0,b0},{a1,b1},{a2,b2}}`

and one V18 four-triad branch `n_+`.

Let

`v_M=n_+-n_-`

be the matching trade and

`h=F n_+=12 v_M`.

Thus h has triad-coordinate values:

- `+12` on the four even-parity transversal triples;
- `-12` on the four odd-parity transversal triples;
- `0` on the remaining twelve triples.

All thirty nonzero oriented minimal fields `+/-12 v_M`, for the 15 matchings, are S6 translates of this type.

## 3. Stabilizer and active-triad orbits

The exact stabilizer

`H=Stab_{S6}(h)`

has order 24.

It preserves the underlying perfect matching and the parity orientation of the transversal cube.

Its action on the 20 active triads has exactly three orbits:

- four `+12` transversals;
- four `-12` transversals;
- twelve zero-field triads.

The eight nonzero transversals choose exactly one endpoint from each matching pair. The twelve zero-field triads contain one entire matching pair plus one endpoint from another pair.

## 4. Equivariant-selector criterion

Let a candidate deterministic local update be

`f(h,S)=T`

with

`T adjacent to S` in `J(6,3)`.

S6 covariance requires

`f(g h,g S)=g f(h,S)`.

Fixing the canonical h reduces this to H-equivariance.

For one input S, any H-equivariant selected neighbor T must be fixed by the input stabilizer

`H_S={g in H:gS=S}`.

This is the standard finite-symmetry canonical-choice criterion reused from T7.

## 5. No total deterministic selector from one field

For every one of the eight transversal active triads `S` with `h_S=+/-12`:

- `|H_S|=6`;
- no adjacent triad T is fixed by all of `H_S`.

Therefore no H-equivariant deterministic neighbor can be assigned at those inputs.

Hence there is **no total S6-equivariant deterministic J(6,3) update law using only `(h,S)`** for one minimal pure-triadic field h.

This is an exact canonical-choice obstruction, not a numerical optimization failure.

### Boundary zero-field states

For each of the twelve zero-field triads, `|H_S|=2` and exactly one adjacent triad is fixed by `H_S`.

If S contains a whole matching pair plus one endpoint x from a second matching pair, the fixed neighbor keeps the whole pair and replaces x by its matched partner.

Thus symmetry determines an involutive neighbor on this 12-state boundary subset, but cannot extend it equivariantly across the eight transversal states.

## 6. Max-score deterministic rule also fails by ties

A natural attempt is to choose among neighbors T of S those maximizing the field score h_T.

Exact enumeration gives:

- if `h_S=+12`, there are 6 maximizing neighbors, all of score 0;
- if `h_S=-12`, there are 3 maximizing neighbors, all of score +12;
- if `h_S=0`, there are 2 maximizing neighbors, both of score +12.

So no state has a unique max-score neighbor.

The field naturally defines a **relation/weighted branch population**, not a deterministic section.

For example, for any `rho in Q_{>0}` one may define the exact positive-rational transition mass

`W_h(S->T)=1_{T~S} rho^(h_T)`.

This is S6 covariant when h and the active triad are transported together. BRC must retain the resulting branch provenance unless a later operation-safe quotient is proved.

## 7. The transversal cube

The eight nonzero triads are exactly the transversals of the three matching pairs. Under one-bit choices inside the three matching blocks they form a cube `Q3` inside `J(6,3)`.

Parity of the cube coordinate is exactly the sign of h:

- even vertices: `+12`;
- odd vertices: `-12`.

Every cube edge crosses from one field sign to the other.

Every square face of this cube has trivial shared-axis replacement holonomy. Therefore the most obvious static-field subgraph is flat and cannot by itself produce the V17 odd holonomy.

## 8. No simple-triangle Ori6 mass bias from a static destination potential

Use the destination-factorized transition weight above. The weight of a three-edge closed active-triad triangle is, up to a common convention-independent factor,

`rho^(h_{S0}+h_{S1}+h_{S2})`.

There are 120 simple J(6,3) triangles: 60 flat and 60 curved/transposition holonomy triangles.

For the canonical minimal field the score distribution is **identical** in the two holonomy classes:

- 36 triangles with total score 0;
- 12 with score +12;
- 12 with score -12.

for each of flat and curved classes.

Hence the total weighted simple-triangle mass is exactly

`Z_flat(rho)=Z_curved(rho)=36+12 rho^12+12 rho^-12`.

So this static one-field destination-potential model creates no aggregate preference for Ori6 charge zero versus one at the first loop scale.

This is a finite exact no-go for this declared field-to-transition law; it does not forbid richer edge/history couplings.

## 9. Consequence for V17

V17 proves that an active-triad history with transposition holonomy can supply the Ori6 reversal bit conditionally.

V21 now shows that one static minimal pure-triadic field is not enough to generate a unique such history under full S6 covariance:

`ONE STATIC PURE FIELD + CURRENT ACTIVE TRIAD`

`-> BRANCHED RELATION, NOT TOTAL DETERMINISTIC PATH`.

Furthermore the simplest destination-potential weighting does not bias flat versus curved triangle holonomy in aggregate.

Thus the next required context must be richer, for example:

- two or more independently labeled neighboring pure-triadic fields;
- a changing field/history;
- an edge-sensitive coupling;
- an internal/channel or event-phase variable.

## 10. Current frontier

Closed for the minimal V18 field orbit:

- 24-element field stabilizer;
- `4+4+12` active-triad orbit decomposition;
- exact stabilizer fixed-neighbor obstruction on all eight transversal states;
- unique symmetry-fixed boundary involution on the twelve zero states;
- max-score tie census `6/3/2`;
- zero simple-triangle holonomy bias for the static destination-potential law.

Next target:

classify how many **independently labeled pure-triadic context fields** are required to remove the residual S6 canonical-choice obstruction and whether the minimal such context can act as a full relational frame for deterministic multi-Cell updates.

No Foundation promotion or physical field law is claimed.
