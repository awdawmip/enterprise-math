# GEO6: the primitive-coordinate graph application of the accepted spectrum bound

Status at freeze: `UNREVIEWED / RESULT_ONLY / EXISTING_THEOREM_APPLICATION_AND_REMAINING_GAP`.

Author: genuine Driver `EM-DVR-BFF6DC`, SID `MCP-47562f9f432d4978a7bea0dd60ecc4aa`, DA `DA-144D0C4639CACEEE75DC`. This is new source-alignment and application work, with all prior CM24/Parity/CONTROL exposure retained. No scientific program, enumeration, new Task, claim, Native vote, Foundation amendment, or parent closure occurs.

## 1. The one selected arrow and its exact gain

The accepted 2026-08-30 Falconer-shaped result `RR-36E518770A5FB701B42C` proves a connected-subset spectrum theorem and a six-axis unit-step ball bound. Its unresolved residue asks for a P000-compatible local/refinable relation datum. The current Foundation now supplies a particular such datum: **pure coordinate adjacency** on the native spatial Cell torsor.

The arrow evaluated here is exactly

`current X6 pure-coordinate adjacency -> the hypotheses of the already accepted unit-step forcing theorem`.

The resulting application is valid for that named graph. It does not identify this graph with every allowed channel, every decorated-state transition, or complete native rotation dynamics. The gain is a closed, source-bound application interface, not a new Lee-ball formula, a new Falconer theorem, or a claim of mathematical novelty. The historical August result and its review remain unchanged.

All sources below were fetched personally through the managed GitHub connector at the coherent immutable Source `3d9b4cbb60b66e5dc1a01d217fe9a310dae8bdaf`; exact bytes, SHA-256, Git blob, and immutable URLs are in the accompanying context. Rejected research items were checked only to their stated exclusion scope.

## 2. Inputs and existing-work boundary

The mathematical inputs are:

1. `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, §§2–3: native spatial Cell centers form an affine torsor for the signed translation group `Z^6`; primitive coordinate neighbours are `z +/- e_i`. Its §10 gives minimum primitive transition count `N_min(z)=sum_i |z_i|`. Its §§4,9,12–13 distinguish the component quadratic readout, the finite axis-permutation skeleton, richer state, and open dynamics.
2. `research_returns/GEO6_FALCONER_RELATION_DISTANCE_SPECTRUM_RETURN_20260830.md`, Theorems A–C and §§8–10: the accepted connected-spectrum theorem, the unit-step `V_6` bound, the Hamming countermodel, and the two distinct refinement meanings.
3. `driver_reviews/GEO6_FALCONER_RELATION_SPECTRUM_DRIVER_REVIEW_20260830.md`: genuine `ACCEPTED` at exactly that historical finite/model scope.
4. The accepted first-wave prior-art synthesis and its generation-3 Driver review: Lee `V_6`, Hamming, and the already-classical finite layer are continuation-killed at their accepted claim scope. `NO_MATERIAL_MATCH` is not novelty. That maintenance result grants no new selector authority.
5. `src/enterprise_math/brc_contact_horizon.py`: an existing adapter for two tagged native-X6 positions and one signed unit move per action. `contact_class_count(h)-1` is precisely the existing `V_6(h)` count. Its decreasing-horizon contact quotient does not claim preservation of contact history or arbitrary dynamics. The file is read as an existing interface; nothing in it was imported or executed.

P000, Heartbeat World X6/time typing, and the mandatory Joint Relation Observer Preservation contract were loaded from the same immutable Source. Static spatial sets need no time variable. No independent lower-dimensional native world, continuum line, Euclidean angle law, or final Cell-address serialization is introduced.

## 3. Exact type map

Let `C` denote the full native spatial Cell-center torsor. Fix any Cell anchor `c_*`, solely to write a raw signed chart `chi:C -> Z^6`. No global distinguished origin is chosen.

Define the **specific** undirected graph `G_coord` by

`P ~ Q iff chi(Q)-chi(P) belongs to {+e_1,-e_1,...,+e_6,-e_6}`.

Changing anchor translates every chart coordinate by the same vector, so this relation is anchor independent. By Foundation §3 this is exactly the declared pure coordinate graph; an additional channel relation would be a different explicitly typed graph.

Let `d_coord` be ambient shortest-path distance in this graph. The chart is a graph isomorphism to the usual signed-unit-step graph on `Z^6`. Therefore, using the admitted minimum-transition formula,

`d_coord(P,Q) = N_min(chi(Q)-chi(P)) = sum_i |chi_i(Q)-chi_i(P)|`.

This is a count of primitive coordinate transitions. Foundation §4 also defines `d6(P,Q)^2=sum_i(chi_i(Q)-chi_i(P))^2`. The two readouts are distinct. Neither the notation `native distance` nor the existence of a quadratic readout silently changes the graph metric used below.

Translations and the admitted `S6` positive-axis permutation skeleton act by automorphisms of `G_coord`. Thus the application is chart independent and equivariant under those declared operations. No invariance under unspecified additional native rotation dynamics is claimed.

## 4. Application theorem

Let `A` be a finite nonempty set of spatial Cell centers, and require its induced `G_coord` subgraph to be connected. Define the positive ambient graph-distance spectrum

`Delta_coord(A)={d_coord(P,Q): P,Q in A, P != Q}`,

`s=|Delta_coord(A)|`, `D=max_{P,Q in A} d_coord(P,Q)`, and `N=|A|`.

Then

`Delta_coord(A)={1,...,D}`, `s=D`,

and

`N <= V_6(s) := sum_{j=0}^6 2^j binom(6,j) binom(s,j)`.

For a singleton, `D=s=0`, the spectrum is empty, and `N=V_6(0)=1`. As usual `binom(s,j)=0` when `j>s`.

**Proof of the application, not a new proof claim for the classical layer.** The chart identifies `A` with a connected finite subset of the exact unit-step model in the accepted theorem. Its ambient distances agree by §3, so the accepted Theorem A transfers its gap-free spectrum and `s=D`. Fixing one Cell of `A`, every other Cell is in the graph ball of radius `s`; that ball is a translate of the accepted unit-step ball with cardinality `V_6(s)`. This gives the inequality. The chart is lossless on the declared spatial Cell-center population. Decorations and path histories are outside this observer; they are not asserted to be reconstructible from spatial coordinates. QED.

Equivalently `s >= min{r in Z_{>=0}:V_6(r)>=N}`. This is the old exact forcing inequality applied to a now-explicit Foundation graph. It supplies neither an optimal general isodiametric bound nor a classical continuum Falconer exponent.

The count can also be read directly from the existing contact adapter as `N <= contact_class_count(s)-1`. This equality is interface reuse, not a new program, a new test, or a new Tool family.

## 5. Refinement: what is actually inherited

For a fixed anchor and integer `r>=1`, the map with chart expression `z -> rz` multiplies `d_coord` by `r`. Its image of a connected set need not remain connected in the unit-step graph. Consequently the spectrum's **values** multiply by `r`, while its cardinality stays unchanged. Applying the connected-set theorem to that sparse image without checking connectedness would be invalid.

For the already accepted interval-box family, let `A_q` have chart `{0,...,q-1}^6`, `q>=2`. Its graph spectrum is `{1,...,6(q-1)}`. The filled integer refinement is the full box with side length `r(q-1)+1`, not just the sparse dilation of the original points. Its spectrum is `{1,...,6r(q-1)}`. This is exactly the old filled-box refinement application. No canonical physical scale change or refinement rule for a general decorated packet is thereby selected.

## 6. Protected obstructions and observer boundaries

The accepted Hamming family on the same set of raw coordinates uses edges allowing any nonzero one-coordinate jump. That relation has spectrum size six on arbitrarily large six-axis boxes. It remains a valid obstruction for the larger class of **arbitrarily declared relation readouts**. It is not the pure coordinate graph: a jump of magnitude greater than one is not a primitive coordinate neighbour under current Foundation §3.

Thus no old no-go theorem is overturned. Its August statement about missing data is retained as a historical statement. Current Foundation supplies one named primitive graph; it does not select every relation used in the mother question. The present application neither rewrites that old Result nor grants itself Foundation authority.

The full spatial population must be retained for this application. The current joint min-zero observer forgets common-depth displacement `(1,...,1)`; Foundation §§6–8 and the V18 preservation audit already prove that loss. A claim about `N`, connectedness, or pairwise full graph distances cannot replace Cell centers by relative min-zero labels without an observer-specific descent or repair certificate. This note does not derive a new quotient theorem or erase path provenance: no claims are made about past contacts, weighted branches, ordered paths, simultaneous moves, velocity, or state-dependent transport.

Finally, the quadratic readout is not substituted for `d_coord`. For example, three consecutive unit-axis Cells have squared component-distance spectrum `{1,4}` while their transition-distance spectrum is `{1,2}`. This only exhibits a type distinction; it is not a new global impossibility result about quadratic-distance forcing.

## 7. Remaining gap and terminal scope of this unit

Disposition proposed for independent review:

`RESULT_ONLY_TYPED_APPLICATION / REUSE_CLOSURE_FOR_THE_PURE_COORDINATE_GRAPH`.

The source alignment closes the named hypothesis arrow for `G_coord`. It does not close the external-geometry Objective, introduce a successor Task, or prove that a physical/channel relation must equal `G_coord`. Remaining questions include which declared relation a concrete application actually observes, which refinements are lawful for its richer state, and how additional dynamics preserve the chosen graph observer. These require concrete new inputs; this note does not turn them into new Tasks or rename them as progress.

No new classical theorem, novelty certificate, scientific Result, Native Driver review, Working Truth, full-X6 dynamics, or closure follows. The author's source-alignment contribution is explicit, so any decisive mathematical review of this application must come from a genuine nonauthor reviewer.
