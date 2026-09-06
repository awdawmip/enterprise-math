# X6 upper V24: two-field triadic edge curl is the minimal linear S6-covariant non-gradient driver on J(6,3)

Status: `FREE_RESEARCH / EXACT REPRESENTATION + EDGE-CURL DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- `X6_SINGLE_TRIADIC_FIELD_DYNAMICS_NOGO_V21_20260906.md`;
- `X6_FOUR_FIELD_ACTIVE_TRIAD_CODE_V23_20260906.md`;
- `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`.
Checker: `experiments/x6_triadic_edge_curl_v24_20260906/check_triadic_edge_curl.py`.

## 1. Why a deterministic scalar potential still cannot generate holonomy

V23 makes it possible to encode all 20 active triads by four labeled field readings. Using balanced ternary, one can compress an injective four-field signature

`(d1,d2,d3,d4) in {-1,0,1}^4`

to the scalar

`J=d1+3d2+9d3+27d4`.

All twenty J values are distinct.

Thus a unique S6-covariant deterministic update can be defined by

`f_J(S)=the adjacent T with maximal J(T)`.

However this still cannot create nontrivial loop holonomy.

### General scalar-potential cycle no-go

Let G be any finite undirected graph with an injective scalar potential J on vertices. Define `f(v)` to be the unique neighbor of v with maximal J.

Any directed cycle of f has length exactly two.

Indeed, for a hypothetical cycle

`v_0 -> v_1 -> ... -> v_{m-1} -> v_0`, `m>=3`,

at each vertex `v_i`, the predecessor `v_{i-1}` is also a neighbor, so

`J(v_{i+1}) > J(v_{i-1})`.

Chaining these strict inequalities around the parity classes gives a contradiction for both odd and even m.

Hence only backtracking 2-cycles remain.

For the J(6,3) shared-axis connection, an edge followed immediately by its inverse has identity holonomy. Therefore no static scalar-potential greedy dynamics can generate the V17 nontrivial S3 holonomy/Ori6 charge.

For the explicit V23 balanced-ternary code, exact enumeration gives three 2-cycles with basin sizes `10,6,4`; the other 14 triads enter one of them in one step.

This is a law-class no-go, not a defect of the chosen four-field code.

## 2. Antisymmetric edge space

Let `E^-` be the rational vector space of antisymmetric functions on oriented edges of J(6,3):

`omega(S,T)=-omega(T,S)`

for adjacent S,T.

There are 90 unoriented graph edges, so `dim E^-=90`.

S6 acts on `E^-` by relabeling the six native axes, including the induced sign when a canonical oriented-edge basis is reversed.

Let K be the V20 irreducible five-dimensional pure-triadic field representation.

The key question is how many S6-equivariant edge 1-forms can be built linearly from one or more K fields.

## 3. One pure field: the only equivariant linear edge 1-form is a gradient

For `h in K`, the obvious antisymmetric edge field is

`(dh)(S,T)=h(T)-h(S)`.

This is S6 equivariant and has zero circulation on every closed loop.

Exact character computation over all 720 elements of S6 gives

`dim Hom_{S6}(K,E^-)=1`.

Since `d:K->E^-` is nonzero, it spans the entire equivariant Hom space.

Therefore:

`EVERY S6-EQUIVARIANT EDGE 1-FORM LINEAR IN ONE PURE TRIADIC FIELD IS A SCALAR GRADIENT`.

So one pure field cannot produce linear curl, even before choosing a deterministic update rule.

This strengthens V21.

## 4. Two pure fields: unique alternating bilinear curl channel

For two fields `h,k in K`, define

`Omega_{h,k}(S,T)=h(S)k(T)-h(T)k(S)`.

Then:

- `Omega_{h,k}` is antisymmetric in the graph edge;
- it is alternating in the field pair `h,k`;
- it is bilinear;
- it is S6 equivariant under simultaneous relabeling of both fields and the edge.

It therefore defines a nonzero equivariant map

`Lambda^2 K -> E^-`.

Using

`chi_{Lambda^2 K}(g)=(chi_K(g)^2-chi_K(g^2))/2`,

an exact 720-element character sum gives

`dim Hom_{S6}(Lambda^2 K,E^-)=1`.

Hence `Omega` is, up to one overall scalar, the **unique S6-equivariant alternating bilinear antisymmetric edge channel** built from two pure-triadic fields.

In the exact category

`linear edge response + S6 covariance + antisymmetric edge signal`,

one field can only produce a gradient, while two fields are minimally sufficient for curl.

This is a scoped minimality theorem, not a universal claim about arbitrary nonlinear dynamics.

## 5. Discrete circulation

For an oriented graph triangle `(S,T,U)`, define

`Curl_Omega(S,T,U)=Omega(S,T)+Omega(T,U)+Omega(U,S)`.

Explicitly,

`Curl_Omega`

`=h(S)k(T)-k(S)h(T)`

` + h(T)k(U)-k(T)h(U)`

` + h(U)k(S)-k(U)h(S)`.

This is twice the oriented area determinant of the three evaluation points `(h,k)` in the two-field plane, in the usual algebraic sense.

Unlike a gradient, it need not vanish.

## 6. Exact curved-holonomy witness

Take the positive minimal fields associated to the perfect matchings

`M0={{0,1},{2,3},{4,5}}`,

`M1={{0,1},{2,4},{3,5}}`.

Let `h=v_M0`, `k=v_M1`.

On the curved J(6,3) triangle

`023 -> 024 -> 034 -> 023`,

the canonical shared-axis transport holonomy fixes axis 0 and swaps axes 2 and 3. Thus its S3 holonomy is a transposition and its V16 conditional Ori6 charge is one.

The two-field edge circulation is exactly

`Curl_Omega=-3`.

Therefore the minimal two-field curl channel can be nonzero on an odd-holonomy relation loop.

This does not mean every nonzero curl loop is odd or that the field universally prefers odd holonomy.

## 7. Exact positive-rational directed BRC weights

Let `rho in Q_{>0}` and define on every oriented adjacent active-triad edge

`W_rho(S->T | h,k)=rho^(Omega_{h,k}(S,T))`.

Since the minimal fields have integer coordinates, every exponent is integral and the weight is a positive rational.

Reversal gives

`Omega(T,S)=-Omega(S,T)`,

so

`W(S->T)/W(T->S)=rho^(2 Omega(S,T))`.

For an oriented closed loop L,

`product_{e in L} W(e) / product_{e in reverse(L)} W(e)`

`=rho^(2 sum_{e in L}Omega(e))`.

Hence nonzero discrete circulation creates an exact nonreciprocal loop-weight ratio.

For the curved witness above the forward/reverse ratio is

`rho^-6`.

This is an exact positive Weighted-BRC dynamics candidate. It is not a probability law until a normalization/choice protocol is declared.

## 8. The two-field curl is not itself an Ori6 selector

For all unordered pairs of distinct-matching minimal fields, exact enumeration shows nonzero-circulation simple triangles occur in both holonomy classes.

Two pair-context types occur:

- 240 field pairs with C3 residual stabilizer: 36 flat and 36 curved triangles have nonzero circulation;
- 180 field pairs with V4 residual stabilizer: 32 flat and 32 curved triangles have nonzero circulation.

So two-field curl supplies the missing non-gradient **drive**, but not a universal parity-only classifier of chart holonomy.

V16/V17 still determine Ori6 charge from the actual active-triad loop holonomy once a path is realized.

## 9. Why this is the right next layer

The upper hierarchy is now:

`one static field -> only gradient linear edge signal -> no holonomy drive`,

`two fields -> unique wedge/curl edge channel -> possible nonreciprocal loops`,

`three labeled fields -> possible complete S6 relational frame`,

`four labeled fields -> full active-triad identity code from readings`.

These are different capabilities and their minimum context sizes need not coincide.

## 10. Current frontier

Closed:

- scalar-potential greedy cycle no-go;
- unique one-field linear gradient channel;
- unique two-field alternating bilinear curl channel;
- explicit odd-holonomy triangle with nonzero curl;
- exact positive-rational directed loop-weight family;
- proof that curl is not by itself a universal Ori6 classifier.

Next target:

study the finite weighted active-triad dynamics generated by `W_rho` together with the V17 holonomy ledger: classify stationary/recurrent cycle structure and determine whether multi-field updates can create a self-consistent feedback law in which triadic curl biases relation paths and the resulting holonomy feeds back into V13/V15 phase reversal.

No Foundation promotion, physical nonreciprocal force law or external novelty claim is made.
